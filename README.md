# Devotional Chants (భక్తి ధ్వని)

<p align="center">
  <img src="app/src/main/res/drawable/app_icon.png" width="128" height="128" alt="Devotional Chants Logo" />
</p>

<p align="center">
  <strong>A Sacred, 100% Offline Android Devotional Audio Experience for Devotees and Elders</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Android_8.0+_(API_26+)-3DDC84?style=for-the-badge&logo=android&logoColor=white" alt="Platform" />
  <img src="https://img.shields.io/badge/Language-Kotlin_2.0-7F52FF?style=for-the-badge&logo=kotlin&logoColor=white" alt="Language" />
  <img src="https://img.shields.io/badge/UI-Jetpack_Compose_Material_3-4285F4?style=for-the-badge&logo=jetpackcompose&logoColor=white" alt="Jetpack Compose" />
  <img src="https://img.shields.io/badge/Playback-Media3_%2F_ExoPlayer-FF6F00?style=for-the-badge&logo=googleplay&logoColor=white" alt="Media3" />
  <img src="https://img.shields.io/badge/Architecture-Clean_%2F_Offline--First-00897B?style=for-the-badge" alt="Offline First" />
  <img src="https://img.shields.io/badge/APK_Size-45.6_MB-E91E63?style=for-the-badge" alt="APK Size" />
</p>

---

## 🌟 Overview

**Devotional Chants** is a premium, offline-first Android application dedicated to traditional Indian devotional chants, stotras, and saptashatis. Engineered specifically for devotees, families, and elderly listeners, the app delivers pristine full-length studio renditions paired with real-time, time-synchronized bilingual lyrics (Telugu script with English phonetic transliteration) that automatically scroll in harmony with the chanting vocal.

The app operates **completely standalone with zero internet connectivity required** after installation—no streaming buffering, no third-party trackers, no accounts, and no banner advertisements.

---

## ✨ Key Features

- **🕉️ 6 Core Full-Length Devotional Chants**: Includes authoritative renditions such as M.S. Subbulakshmi's complete Sri Vishnu Sahasranamam (29m 50s), Hariharan's Sri Hanuman Chalisa (9m 48s), and traditional Tirumala Balaji Govinda Namalu (12m 25s).
- **📜 Sub-Second Time-Synchronized Bilingual Lyrics**: Full stotra text displayed in authentic Telugu script alongside clear English transliteration. Active verses highlight dynamically with zero latency and scroll into view automatically.
- **🪔 Sacred Temple Sanctum Aesthetics**: Warm golden glow visual themes, rich temple maroon and sanctum dark backgrounds, pulsating diya flame animations, and an adaptive brass deepam launcher emblem.
- **👴 Elder-Friendly Interaction**: High-contrast typography, generous touch targets (min 48dp), simple single-tap playback, persistent playback controls, and crystal-clear audio tuning.
- **🔔 Foreground Media3 Audio Service**: Continuous background playback powered by AndroidX Media3/ExoPlayer with lockscreen and notification drawer media controls (`MediaNotificationManager`).
- **📱 Ultra-Lightweight Footprint**: Complete self-contained release package is under **46 MB**, well within the 100 MB budget, while bundling over **1 hour and 10 minutes** of full-length CD-quality devotional audio.

---

## 🎵 Devotional Audio Catalog

| Track Title | Deity / Theme | Duration | Stanzas | Audio Format |
| :--- | :--- | :--- | :--- | :--- |
| **Sri Vishnu Sahasranama Stotram** | Lord Maha Vishnu | `29m 50s` (1790.9s) | 123 | 68 kbps AAC-LC CBR |
| **Sri Hanuman Chalisa** | Lord Hanuman | `09m 48s` (588.4s) | 45 | 68 kbps AAC-LC CBR |
| **Govinda Namalu** | Lord Venkateswara (Tirumala Balaji) | `12m 25s` (745.4s) | 111 | 68 kbps AAC-LC CBR |
| **Sri Krishna Ashtakam** | Lord Sri Krishna | `07m 51s` (471.0s) | 11 | 68 kbps AAC-LC CBR |
| **Garuda Gamana Tava Charana** | Lord Hari / Venkateswara | `06m 54s` (414.5s) | 18 | 68 kbps AAC-LC CBR |
| **Sri Lakshmi Ashtottara Shatanamavali** | Goddess Mahalakshmi | `04m 43s` (283.9s) | 110 | 68 kbps AAC-LC CBR |
| **Total Catalog** | — | **~71 mins** | **418** | **All Embedded Locally** |

---

## 🏛️ Architecture & Tech Stack

```
app/src/main/
├── java/com/bhaktidhwani/app/
│   ├── data/
│   │   ├── model/           # AudioTrack, Lyrics, Stanza, Language models
│   │   └── repository/      # LocalAudioRepository, LocalLyricsRepository
│   ├── playback/            # DevotionalAudioService, DevotionalMediaController,
│   │                        # MediaNotificationManager (AndroidX Media3 / ExoPlayer)
│   ├── ui/
│   │   ├── components/      # MiniPlayer, PlaybackControls, BottomNavigation
│   │   ├── screens/         # WelcomeScreen, HomeScreen, PlayerScreen, LyricsSheet
│   │   ├── theme/           # Color, Type, Theme (DevotionalChantsTheme)
│   │   └── viewmodel/       # MainViewModel (StateFlow-driven UI State)
│   └── MainActivity.kt      # Edge-to-edge Compose entry point
├── assets/lyrics/           # Sub-second synchronized JSON arrays (Telugu + English)
└── res/
    ├── drawable/            # App icons, vector deepams, sacred artwork
    └── raw/                 # Embedded AAC-LC audio files (.m4a)
```

- **Jetpack Compose & Material 3**: Fully declarative modern Android UI utilizing edge-to-edge layouts, smooth animated transitions, and custom canvas-drawn temple diya elements.
- **AndroidX Media3 (1.4.1)**: Dedicated `MediaSessionService` implementation decoupling audio playback from UI lifecycle, preventing stutter or drops when screen turns off.
- **StateFlow & Clean MVVM**: Reactive unidirectional data flow through `MainViewModel` ensuring sub-millisecond lyrics lookups via binary search without UI lag.
- **Audio Pipeline**: Master MP3s compressed via FFmpeg into 68-80 kbps AAC-LC CBR with EBU R128 loudness normalization (`-16 LUFS`) and 60 Hz high-pass acoustic filtering.

---

## 🚀 Quick Start & Deployment

### 1. Direct Physical Device Deployment (via ADB)

Connect your Android smartphone or tablet to your development workstation via USB with **USB Debugging** enabled:

```powershell
# 1. Verify connected physical device
adb devices

# 2. Install the compiled release APK directly
adb install -r app/build/outputs/apk/release/app-release.apk

# 3. Launch the application immediately
adb shell am start -n com.bhaktidhwani.app/.MainActivity
```

---

### 2. Manual APK Sideload & Explorer Access

The production-ready release APK is generated at:
- **Relative Path**: `app/build/outputs/apk/release/app-release.apk`
- **File Size**: `45.56 MB`

#### Reveal APK in Windows File Explorer:
Run the following PowerShell command to instantly open and highlight the release APK:
```powershell
explorer.exe /select,"app\build\outputs\apk\release\app-release.apk"
```

#### Step-by-Step Sideload Instructions:
1. **Transfer File**: Connect your phone via USB (File Transfer / MTP) and copy `app-release.apk` to your phone's `Download` folder (or send via Bluetooth / Nearby Share / WhatsApp).
2. **Open Files**: On your Android phone, open the **Files** or **My Files** app and navigate to **Downloads**.
3. **Allow Installation**: Tap `app-release.apk`. If prompted with *"For your security, your phone is not allowed to install unknown apps from this source"*, tap **Settings** and toggle **Allow from this source**.
4. **Install**: Tap **Install**, wait 5 seconds, then tap **Open** to begin chanting.

---

### 3. Local Build & Test Commands

Ensure a JDK (Java 17 or higher) is available:

```powershell
# Run unit tests across all test suites
./gradlew.bat testDebugUnitTest

# Assemble Debug APK (for testing)
./gradlew.bat assembleDebug

# Assemble Production Release APK (minified with R8)
./gradlew.bat assembleRelease
```

---

## ⚙️ Environment Configuration

The repository uses environment variables to avoid hardcoding machine-specific SDK and tool paths.

1. Copy `.env.example` to `.env`:
   ```powershell
   Copy-Item .env.example .env
   ```
2. Adjust your local paths in `.env`:
   ```ini
   ANDROID_SDK_ROOT=C:\Users\<username>\AppData\Local\Android\Sdk
   ANDROID_HOME=C:\Users\<username>\AppData\Local\Android\Sdk
   ADB_PATH=C:\Users\<username>\AppData\Local\Android\Sdk\platform-tools\adb.exe
   FFMPEG_PATH=C:\Program Files (x86)\ClipGrab\ffmpeg.exe
   ```
> **Security Note**: `.env` and `.env.local` are strictly ignored by `.gitignore` to prevent leaking personal paths or signing credentials into source control.

---

## 🛠️ Audio Pipeline & Synchronization Tooling

Located in the [`scripts/`](file:///d:/Devotional_app/scripts/) folder:

- **`download_audio.ps1`**: Automated YouTube master track extraction via `yt-dlp` and FFmpeg.
- **`compress_audio.ps1`**: Encodes master tracks to 68-80 kbps AAC-LC CBR with EBU R128 normalization into `app/src/main/res/raw/`.
- **`update_durations.ps1`**: Reads millisecond audio durations directly via FFmpeg and updates `LocalAudioRepository.kt`.
- **`transcribe_and_align.py`**: Acoustic Voice Activity Detection (VAD) and speech energy engine for sub-second verse onset extraction.
- **`sync_lyrics.py`**: Regenerates and audits all 6 bilingual lyrics files in `app/src/main/assets/lyrics/` ensuring timeline monotonicity and full track coverage.
- **`setup_icons.ps1`**: Generates multi-density launcher icon buckets (mdpi, hdpi, xhdpi, xxhdpi, xxxhdpi) from `app_icon.png`.

---

## 📜 License

Designed and developed for devotional, cultural, and spiritual upliftment. Distributed under the MIT License.
