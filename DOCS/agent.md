# Agent Instructions & Workflow: Devotional Chants

## 1. Agent Role & Mission
* **Role:** Autonomous Android Lead Engineer & Implementation Agent (Google Antigravity).
* **Mission:** Build, test, and deliver a production-ready, 100% offline devotional audio streaming Android app named **Devotional Chants** strictly adhering to `PRD.md`, `TRD.md`, `App_flow.md`, `Implementation.md`, and `QA_test_plan.md`.
* **Primary Constraints:**
  * **Zero Remote Dependencies:** App must function 100% offline in Airplane Mode.
  * **Size Ceiling:** Final release APK must not exceed **100 MB**.
  * **Senior Accessibility:** Touch targets $\ge 48	ext{ dp}$ (Play/Pause $\ge 72	ext{ dp}$), minimum font size $18	ext{ sp}$, high-contrast colors.
  * **No Hand-Coding Required by User:** The agent writes, organizes, and verifies all code, assets, scripts, and Gradle tasks autonomously.

---

## 2. Agent Execution Workflow

The agent must execute tasks sequentially across 5 distinct execution gates:

```
[Gate 1: Context Ingestion] ──► [Gate 2: Scaffolding & Assets] ──► [Gate 3: Media3 Core Engine]
                                                                          │
[Gate 5: Build & Verification] ◄── [Gate 4: Compose UI & Sync Engine] ◄────┘
```

### Gate 1: Context Ingestion & Project Setup
1. Read and index all reference documents: `PRD.md`, `TRD.md`, `App_flow.md`, `Implementation.md`, and `QA_test_plan.md`.
2. Inspect workspace for directory structure; initialize standard Android Gradle Kotlin DSL project scaffolding if missing.
3. Configure `app/build.gradle.kts` with dependencies defined in Section 7 of `TRD.md`.
4. Ensure `isShrinkResources = false` is maintained so raw audio files in `res/raw/` are not stripped.

### Gate 2: Static Asset Preparation & Packaging
1. Ensure all 6 core audio tracks exist under `app/src/main/res/raw/` using valid Android resource identifiers (lowercase, underscores):
   * `vishnu_sahasranamam.m4a`
   * `hanuman_chalisa.m4a`
   * `govinda_namalu.m4a`
   * `lakshmi_ashtottaram.m4a`
   * `garuda_gamana.m4a`
   * `krishna_ashtakam.m4a`
2. If audio files are provided in uncompressed format, run the batch script specified in Section 3.2 of `TRD.md` to encode them to 80 kbps AAC-LC.
3. Verify local JSON lyrics schemas exist in `app/src/main/assets/lyrics/` with millisecond timestamps and bilingual text (Telugu + English).
4. Verify Lottie animation file `namaste_anim.json` is placed in `app/src/main/assets/anim/`.

### Gate 3: Core Audio Playback Engine
1. Implement `DevotionalAudioService` extending `MediaSessionService`.
2. Configure singleton `ExoPlayer` instance with `AudioAttributes` handling audio focus.
3. Implement `PlayerNotificationManager` for lock-screen controls and foreground service notification.
4. Implement the Japam/loop counter state machine in accordance with Section 5 of `TRD.md`.

### Gate 4: Compose UI & Time-Synced Lyrics Engine
1. Implement theme tokens in `ui/theme/` (Deep Saffron `#E65100`, Temple Maroon `#3E000C`, Soft Ivory `#FFF8E7`).
2. Build UI screens according to `App_flow.md`:
   * `WelcomeScreen`: Lottie Namaste, bilingual header, large "Get Started" CTA.
   * `LibraryScreen`: Sticky filter pills, 2x2 daily cards, Spotify-style track rows.
   * `MiniPlayerBar`: Persistent bottom bar with Play/Pause toggle and title marquee.
   * `PlayerScreen`: Large artwork, jumbo controls, scrubber, Japam pill selector.
   * `LyricsScreen`: Stanza list with 150 ms polling flow, active line highlight, auto-scroll, and script switcher.

### Gate 5: Build, Test & APK Verification
1. Run lint checks and verify zero compiler warnings in Kotlin code.
2. Run automated tests matching test suites in `QA_test_plan.md`:
   * Verify Japam counter loops correctly to 0 and counts iterations.
   * Verify time-sync binary search logic.
3. Execute `./gradlew assembleDebug` and `./gradlew assembleRelease`.
4. Inspect the generated APK file size:
   * **Target:** $\le 100	ext{ MB}$.
   * If APK size exceeds 100 MB, alert the user and trigger re-compression of audio assets.

---

## 3. Strict Coding & Architectural Rules for the Agent

1. **No Pseudo-Code:** All generated files must be fully implemented, syntactically correct Kotlin/Compose code. Never leave `// TODO` or placeholder stubs in core audio logic.
2. **Audio Stability Guarantee:** Playback logic must never run on the Main UI thread. All disk I/O (lyrics JSON parsing) must execute via `Dispatchers.IO`.
3. **Elderly Usability Guardrails:**
   * Every clickable item must have a minimum touch target of `48.dp`.
   * Full player Play/Pause button must be $\ge 72	ext{ dp}$.
   * Never hardcode tiny text sizes; default body text must be $\ge 18	ext{ sp}$.
4. **Offline Isolation:** Never add dependencies or code that attempt network calls, remote CDNs, or external tracking analytics.
5. **Session Rule:** Welcome screen must be shown on every fresh app launch, but must be removed from the backstack once "Get Started" is tapped so back-press exits cleanly.
