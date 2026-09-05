# Technical Requirements Document (TRD)

## 1. System Architecture & Tech Stack

### 1.1 Core Platform Specifications
* **Language:** Kotlin 2.0+
* **UI Toolkit:** Jetpack Compose (Declarative UI) with Material 3 Design Tokens
* **Audio Playback Engine:** AndroidX Media3 (`androidx.media3:media3-exoplayer:1.3.1`, `androidx.media3:media3-session:1.3.1`, `androidx.media3:media3-ui:1.3.1`)
* **Vector Animation Runtime:** `com.airbnb.android:lottie-compose:6.4.0`
* **Architecture Pattern:** Clean Architecture with Unidirectional Data Flow (UDF) / MVVM
* **State Management:** Kotlin StateFlow & Jetpack ViewModel
* **Local Persistence:** Jetpack DataStore (User preferences, last-played track, font size scale)
* **Minimum SDK:** API 24 (Android 7.0 Nougat) — covers 99%+ of legacy family devices
* **Target / Compile SDK:** API 34+ (Android 14)
* **Build Tooling:** Gradle (Kotlin DSL - `build.gradle.kts`)

---

## 2. Audio Engine Architecture & Background Playback

### 2.1 Media3 Architecture Overview
The application separates UI presentation from playback runtime using AndroidX Media3's client-server architecture:

```
┌────────────────────────────────────────────────────────┐
│                      UI Layer                          │
│  (Compose Screens: Welcome, Library, Player, Lyrics)   │
└───────────────────────────▲────────────────────────────┘
                            │ MediaController (IPC / Async)
┌───────────────────────────▼────────────────────────────┐
│         PlaybackService (MediaSessionService)          │
│  ┌──────────────────────────────────────────────────┐  │
│  │           ExoPlayer Instance (Singleton)         │  │
│  │  - Loop / Japam Counter Logic                    │  │
│  │  - Audio Focus (AudioManager.AUDIOFOCUS_GAIN)    │  │
│  │  - Raw Resource Asset Loader                     │  │
│  └──────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────┐  │
│  │           MediaNotificationManager               │  │
│  │  - Foreground Service (POST_NOTIFICATIONS)       │  │
│  │  - System Lock Screen / Notification Tray        │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────┘
```

### 2.2 Foreground Service & Permissions
* **Foreground Service Type:** `android:foregroundServiceType="mediaPlayback"` declared in `AndroidManifest.xml`.
* **Permissions Required:**
  * `android.permission.FOREGROUND_SERVICE`
  * `android.permission.FOREGROUND_SERVICE_MEDIA_PLAYBACK`
  * `android.permission.POST_NOTIFICATIONS` (Runtime prompt on Android 13+)
  * `android.permission.WAKE_LOCK` (Prevents CPU sleep while chanting with screen off)

### 2.3 Audio Focus Strategy
* Configure `AudioAttributes`:
  ```kotlin
  val audioAttributes = AudioAttributes.Builder()
      .setUsage(C.USAGE_MEDIA)
      .setContentType(C.AUDIO_CONTENT_TYPE_MUSIC)
      .build()
  exoPlayer.setAudioAttributes(audioAttributes, /* handleAudioFocus = */ true)
  ```
* **Behaviors:**
  * **Incoming Call / Ringtone:** Automatically pauses playback. Resumes smoothly when the call terminates.
  * **Navigation Chimes / Notifications:** Transient ducking (lowers devotional track volume momentarily).

---

## 3. Audio Asset Compression & Processing Pipeline

### 3.1 Encoding Profile
To preserve crisp Sanskrit/Telugu chanting diction without artifacts while fitting within the < 100 MB budget:
* **Codec:** AAC-LC (MPEG-4 Audio inside `.m4a` container)
* **Bitrate:** 80 kbps Constant Bitrate (CBR) joint stereo / mono voice profile
* **Sample Rate:** 44,100 Hz
* **Channel Layout:** Stereo (or Mono for solo recitations)
* **High-Pass / Low-Pass Filters:** High-pass at 60 Hz (cuts mic rumble) and gentle low-pass at 16,500 Hz (cuts hiss).

### 3.2 Automated Batch Compression Script (`compress_audio.sh`)
Antigravity or developers can run this script to pre-process master tracks before bundling into `app/src/main/res/raw/`:

```bash
#!/usr/bin/env bash
# Automated Audio Compression Script for Bhakti Dhwani
# Requires ffmpeg installed

INPUT_DIR="./raw_audio"
OUTPUT_DIR="./app/src/main/res/raw"
mkdir -p "$OUTPUT_DIR"

for file in "$INPUT_DIR"/*.{mp3,wav,m4a,flac}; do
  [ -f "$file" ] || continue
  filename=$(basename -- "$file")
  name="${filename%.*}"
  # Standardize name to valid Android resource identifier (lowercase, underscores)
  clean_name=$(echo "$name" | tr '[:upper:]' '[:lower:]' | tr ' -' '__')
  
  echo "Processing: $filename -> ${clean_name}.m4a"
  ffmpeg -y -i "$file" \
    -vn \
    -c:a aac -b:a 80k \
    -ar 44100 \
    -filter:a "highpass=f=60,lowpass=f=16500,loudnorm=I=-16:TP=-1.5:LRA=11" \
    "$OUTPUT_DIR/${clean_name}.m4a"
done

echo "Compression complete. Total size in raw/:"
du -sh "$OUTPUT_DIR"
```

---

## 4. Time-Synchronized Lyrics Engine

### 4.1 Lyrics File Format (`.lrc` / JSON)
Lyrics are packaged as local JSON or standard `.lrc` assets inside `app/src/main/assets/lyrics/`.

**Structure (`vishnu_sahasranamam_lyrics.json`):**
```json
{
  "trackId": "vishnu_sahasranamam",
  "titleTelugu": "శ్రీ విష్ణు సహస్రనామ స్తోత్రమ్",
  "titleEnglish": "Sri Vishnu Sahasranama Stotram",
  "stanzas": [
    {
      "index": 1,
      "startTimeMs": 12400,
      "endTimeMs": 19800,
      "telugu": "శుక్లాంబరధరం విష్ణుం శశివర్ణం చతుర్భుజమ్ |\nప్రసన్నవదనం ధ్యాయేత్ సర్వవిఘ్నోపశాంతయే ||",
      "english": "Shuklaambaradharam Vishnum Shashivarnam Chaturbhujam |\nPrasanna Vadanam Dhyaayet Sarva Vighnopa Shaantaye ||"
    },
    {
      "index": 2,
      "startTimeMs": 20100,
      "endTimeMs": 28400,
      "telugu": "యస్యద్విరదవక్త్రాద్యాః పారిషద్యాః పరః శతమ్ |\nవిఘ్నం నిఘ్నంతి సతతం విష్వక్సేనం తమాశ్రయే ||",
      "english": "Yasyadviradavaktraadyaah Paarishadyaah Parah Shatam |\nVighnam Nighnanti Satatam Vishvaksenam Tamaashraye ||"
    }
  ]
}
```

### 4.2 Synchronization Runtime Logic
* Jetpack Compose observes playback position updates polled at a 150 ms cadence via a Kotlin `flow`:
  ```kotlin
  fun pollPlaybackPosition(exoPlayer: Player): Flow<Long> = flow {
      while (currentCoroutineContext().isActive) {
          if (exoPlayer.isPlaying) {
              emit(exoPlayer.currentPosition)
          }
          delay(150L)
      }
  }.flowOn(Dispatchers.Main)
  ```
* Binary search calculates active stanza index: `startTimeMs <= currentPosition && currentPosition < endTimeMs`.
* `LazyListState.animateScrollToItem(activeIndex)` scrolls the active Telugu stanza into the vertical viewport center.

---

## 5. Japam (Loop Count) Logic & Audio Transitions

### 5.1 Loop Counter State Machine
* **Options:** `LoopMode.ONE_TIME`, `LoopMode.ELEVEN_TIMES`, `LoopMode.TWENTY_ONE_TIMES`, `LoopMode.HUNDRED_EIGHT_TIMES`, `LoopMode.INFINITE`.
* **State Implementation:**
  ```kotlin
  data class JapamCounterState(
      val mode: LoopMode = LoopMode.ONE_TIME,
      val currentIteration: Int = 1,
      val totalTarget: Int = 1
  )
  ```
* **Transition Trigger:** Attaches `Player.Listener.onPlaybackStateChanged`:
  * When state reaches `Player.STATE_ENDED`:
    * If `currentIteration < totalTarget` or `mode == LoopMode.INFINITE`:
      * Increment `currentIteration`.
      * Seek to 0 (`exoPlayer.seekTo(0)`).
      * `exoPlayer.play()`.
    * Else: Complete playback and show completion status.

---

## 6. Project Directory & Package Structure

```
app/
 ├── src/
 │    └── main/
 │         ├── assets/
 │         │    ├── anim/
 │         │    │    └── namaste_anim.json       # Lottie animation (<35 KB)
 │         │    └── lyrics/
 │         │         ├── vishnu_sahasranamam.json
 │         │         ├── hanuman_chalisa.json
 │         │         ├── govinda_namalu.json
 │         │         ├── lakshmi_ashtottaram.json
 │         │         ├── garuda_gamana.json
 │         │         └── krishna_ashtakam.json
 │         ├── res/
 │         │    ├── drawable/                     # WebP deity artworks (<45 KB each)
 │         │    │    ├── art_vishnu.webp
 │         │    │    ├── art_hanuman.webp
 │         │    │    ├── art_venkateswara.webp
 │         │    │    ├── art_lakshmi.webp
 │         │    │    └── art_krishna.webp
 │         │    └── raw/                          # Compressed 80 kbps M4A audio files
 │         │         ├── vishnu_sahasranamam.m4a
 │         │         ├── hanuman_chalisa.m4a
 │         │         ├── govinda_namalu.m4a
 │         │         ├── lakshmi_ashtottaram.m4a
 │         │         ├── garuda_gamana.m4a
 │         │         └── krishna_ashtakam.m4a
 │         └── java/com/bhaktidhwani/app/
 │              ├── data/
 │              │    ├── model/Track.kt, Stanza.kt, JapamMode.kt
 │              │    └── repository/LocalAudioRepository.kt
 │              ├── playback/
 │              │    ├── DevotionalAudioService.kt
 │              │    └── MediaNotificationManager.kt
 │              ├── ui/
 │              │    ├── theme/Color.kt, Type.kt, Theme.kt
 │              │    ├── welcome/WelcomeScreen.kt
 │              │    ├── library/LibraryScreen.kt, MiniPlayerBar.kt
 │              │    ├── player/PlayerScreen.kt, JapamCounterBadge.kt
 │              │    └── lyrics/LyricsScreen.kt, LyricsStanzaItem.kt
 │              └── MainActivity.kt
 └── build.gradle.kts
```

---

## 7. Build Configuration & Guardrails (`build.gradle.kts`)

```kotlin
plugins {
    alias(libs.plugins.android.application)
    alias(libs.plugins.kotlin.android)
    alias(libs.plugins.compose.compiler)
}

android {
    namespace = "com.bhaktidhwani.app"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.bhaktidhwani.app"
        minSdk = 24
        targetSdk = 34
        versionCode = 1
        versionName = "1.0.0"
    }

    buildTypes {
        release {
            isMinifyEnabled = true
            isShrinkResources = false // Preserve raw audio resources
            proguardFiles(getDefaultProguardFile("proguard-android-optimize.txt"), "proguard-rules.pro")
        }
    }

    buildFeatures {
        compose = true
    }
}

dependencies {
    // Jetpack Compose & Material 3
    implementation(platform(libs.androidx.compose.bom))
    implementation(libs.androidx.material3)
    implementation(libs.androidx.ui)
    implementation(libs.androidx.ui.tooling.preview)

    // AndroidX Media3
    implementation(libs.androidx.media3.exoplayer)
    implementation(libs.androidx.media3.session)
    implementation(libs.androidx.media3.ui)

    // Lottie Compose
    implementation("com.airbnb.android:lottie-compose:6.4.0")

    // Preferences DataStore
    implementation("androidx.datastore:datastore-preferences:1.1.1")
}
```
