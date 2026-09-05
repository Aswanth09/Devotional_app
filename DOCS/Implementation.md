# Implementation Plan: Bhakti Dhwani

## 1. Execution Roadmap

```
Phase 1: Project Scaffolding & Dependencies
  └── Gradle setup, permissions, directories, Compose theme, Lottie integration

Phase 2: Data Models & Static Asset Ingestion
  └── Raw audio placement, JSON lyrics schemas, WebP artworks, repository layer

Phase 3: Media3 Background Audio Engine
  └── PlaybackService, MediaSession, ExoPlayer singleton, notification manager, audio focus

Phase 4: UI Development (Jetpack Compose)
  └── Welcome screen, Spotify-style Library, persistent Mini-Player, Full Player

Phase 5: Time-Synced Lyrics & Japam State Machine
  └── 150ms position polling flow, auto-scroll LazyColumn, loop counter cycle

Phase 6: Verification, Optimization & Build
  └── Airplane mode tests, <100 MB APK verification, Proguard rules, release APK build
```

---

## 2. Phase-by-Phase Step Breakdown

### Phase 1: Project Scaffolding & Dependencies
1. **Manifest Configuration (`AndroidManifest.xml`):**
   * Register `DevotionalAudioService` with `android:foregroundServiceType="mediaPlayback"`.
   * Add permissions: `FOREGROUND_SERVICE`, `FOREGROUND_SERVICE_MEDIA_PLAYBACK`, `POST_NOTIFICATIONS`, `WAKE_LOCK`.
2. **Build Configuration (`app/build.gradle.kts`):**
   * Target SDK 34, Min SDK 24.
   * Add dependencies: `media3-exoplayer`, `media3-session`, `media3-ui`, `lottie-compose`, `datastore-preferences`.
   * Disable resource shrinking to protect `res/raw/*.m4a`.
3. **Theme & Design Tokens:**
   * Configure `Color.kt` with Deep Saffron (`#E65100`), Temple Maroon (`#3E000C`), Soft Ivory (`#FFF8E7`), and Gold accents (`#FFD54F`).
   * Set minimum accessibility text size to `18sp` in `Type.kt`.

### Phase 2: Data Models & Asset Ingestion
1. **Model Definitions:**
   * `Track.kt`: ID, title (Telugu & English), deity, rawResId, thumbnailResId, durationMs.
   * `Stanza.kt`: index, startTimeMs, endTimeMs, telugu, english.
   * `JapamMode.kt`: enum (`ONE_TIME(1)`, `ELEVEN_TIMES(11)`, `TWENTY_ONE_TIMES(21)`, `HUNDRED_EIGHT(108)`, `INFINITE(-1)`).
2. **Asset Organization:**
   * Place compressed 80 kbps audio files in `res/raw/`.
   * Place WebP artworks in `res/drawable/`.
   * Place timestamped JSON lyrics in `assets/lyrics/`.
   * Place animated Namaste Lottie JSON in `assets/anim/namaste_anim.json`.
3. **LocalAudioRepository:**
   * Expose immutable list of the 6 core tracks.
   * Implement helper function to parse local JSON lyrics via Kotlinx Serialization or Gson into `List<Stanza>`.

### Phase 3: Media3 Background Audio Engine
1. **`DevotionalAudioService.kt`:**
   * Subclass `MediaSessionService`.
   * Initialize singleton `ExoPlayer` instance configured with `AudioAttributes` for media playback and audio focus handling.
   * Implement `MediaSession.Callback` to intercept custom actions (e.g., Japam mode updates).
2. **`MediaNotificationManager.kt`:**
   * Build notification channel (`devotional_playback_channel`).
   * Bind `PlayerNotificationManager` with lock-screen visibility (`VISIBILITY_PUBLIC`).
3. **Audio Focus Handling:**
   * Automatically pause playback on incoming phone calls; resume upon call end.
   * Implement ducking on short notification chimes.

### Phase 4: UI Development (Jetpack Compose)
1. **`WelcomeScreen.kt`:**
   * Render Lottie composition for Namaste icon (`LottieAnimation`).
   * Display bilingual welcome headline.
   * Button `Get Started` navigating to Library with backstack pop.
2. **`LibraryScreen.kt`:**
   * Sticky horizontal filter pills (`All`, `Vishnu`, `Venkateswara`, `Hanuman`, `Lakshmi`, `Krishna`).
   * 2x2 grid for daily quick-play stotras.
   * Spotify-style vertical track items (56x56 dp artwork, 18sp Telugu title, English subtext, play icon).
3. **`MiniPlayerBar.kt`:**
   * Sticky bottom component displayed whenever a track is active.
   * Marquee text for track title, 48x48 dp Play/Pause button, thin progress bar.
   * Click expands `PlayerScreen`.
4. **`PlayerScreen.kt`:**
   * 280x280 dp rounded deity artwork with soft shadow.
   * 72x72 dp jumbo Play/Pause button, 10s seek forward/rewind buttons.
   * Scrubber slider with elapsed and remaining timestamps.
   * Japam selector pill with current count HUD.

### Phase 5: Time-Synced Lyrics & Japam State Machine
1. **Japam Logic:**
   * Listen to `Player.STATE_ENDED`.
   * If current iteration < target, increment iteration count, seek to 0, and replay.
   * If target reached, reset and stop.
2. **Lyrics Synchronization:**
   * Launch coroutine polling `exoPlayer.currentPosition` every 150 ms.
   * Binary search active stanza matching `startTimeMs <= currentPosition < endTimeMs`.
   * Scroll `LazyColumn` via `rememberLazyListState().animateScrollToItem(activeIndex)`.
   * Provide dynamic script switcher (Telugu $\leftrightarrow$ English) and font scaling (+ / -).

### Phase 6: Verification, Optimization & Build
1. **Run QA test suites:**
   * Airplane mode validation (`TC-OFFLINE-01`).
   * Screen lock endurance playback (`TC-AUDIO-01`).
   * Telugu font rendering & conjunct characters (`TC-LYRICS-01`).
2. **Execute Build:**
   * Run `./gradlew assembleRelease`.
   * Verify output APK size is $\le 100	ext{ MB}$.
