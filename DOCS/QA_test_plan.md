# QA Test Plan: Devotional Chants

## 1. Overview & Quality Objectives
* **Product:** Devotional Chants (Offline Devotional Music Player)
* **Goal:** Verify that the 100% offline devotional audio player functions with zero audio stutters, delivers flawless background playback, displays accurate Telugu time-synced lyrics, handles Japam looping state transitions, and remains strictly accessible for elderly family users.
* **Target Environment:** Android devices running API 24 (Android 7.0) through API 34+ (Android 14).

---

## 2. Test Execution Matrix

| Test Suite ID | Domain | Primary Objective |
| :--- | :--- | :--- |
| **TC-OFFLINE** | Offline Resilience & Asset Integrity | Ensure zero remote dependencies and full functionality in Airplane Mode. |
| **TC-AUDIO** | Audio Engine & Media3 Playback | Validate foreground service, lock-screen controls, and audio focus transitions. |
| **TC-JAPAM** | Japam / Loop State Machine | Verify loop counts (1x, 11x, 21x, 108x, ∞) and counter HUD accuracy. |
| **TC-LYRICS** | Time-Synced Lyrics Engine | Validate millisecond sync, active highlighting, auto-scroll, and Telugu script rendering. |
| **TC-UX-SENIOR**| Senior Usability & Navigation | Test touch targets, font scaling, contrast, and navigation transitions. |
| **TC-PERF** | Performance & Storage Compliance | Confirm APK size ceiling (< 100 MB), cold-start time, and memory stability. |

---

## 3. Detailed Test Cases

### Suite 1: Offline Resilience & Asset Integrity (TC-OFFLINE)

* **TC-OFFLINE-01: Airplane Mode Fresh Launch**
  * **Pre-condition:** Enable Airplane Mode; disable Wi-Fi and Cellular Data completely.
  * **Steps:**
    1. Launch the app fresh from cold start.
    2. Confirm Welcome Screen loads with animated Namaste.
    3. Tap "Get Started".
    4. Browse all 6 tracks in the Spotify-style library.
    5. Play each track sequentially.
  * **Expected Result:** Every track plays instantaneously from bundled raw resources without network errors, timeouts, or blank screens.

* **TC-OFFLINE-02: Zero External Network Calls**
  * **Method:** Run APK with Android Studio Network Profiler attached.
  * **Expected Result:** Zero outbound HTTP/HTTPS calls during any user interaction.

---

### Suite 2: Audio Engine & Media3 Playback (TC-AUDIO)

* **TC-AUDIO-01: Background Playback on Screen Lock**
  * **Steps:**
    1. Start playing *Vishnu Sahasranamam*.
    2. Press the hardware power button to lock the device.
    3. Keep device locked for 15 minutes.
  * **Expected Result:** Audio plays continuously with zero dropouts or stuttering; CPU wake-lock keeps the playback service alive.

* **TC-AUDIO-02: Lock Screen & Notification Tray Controls**
  * **Steps:**
    1. Swipe down the Android notification shade while audio is playing.
    2. Verify notification displays: Deity artwork, Track Title in Telugu/English, Play/Pause toggle, and Progress bar.
    3. Tap Pause $ightarrow$ audio stops immediately. Tap Play $ightarrow$ audio resumes smoothly.
  * **Expected Result:** Notification controls update bidirectionally with the app UI state.

* **TC-AUDIO-03: Audio Focus Interruption (Incoming Phone Call)**
  * **Steps:**
    1. Play *Govinda Namalu*.
    2. Place an incoming phone call to the test device.
  * **Expected Result:** Devotional audio pauses immediately upon incoming ring. Once the call ends, audio resumes smoothly without user intervention.

* **TC-AUDIO-04: Audio Ducking (System Notification / GPS Prompt)**
  * **Steps:**
    1. Play *Hanuman Chalisa*.
    2. Trigger a transient system alert chime.
  * **Expected Result:** Track volume ducks (drops by ~60%) for the duration of the notification sound and smoothly restores to 100%.

---

### Suite 3: Japam / Loop State Machine (TC-JAPAM)

* **TC-JAPAM-01: Discrete Loop Iteration (11x Preset)**
  * **Steps:**
    1. Open *Hanuman Chalisa* in the Full Player.
    2. Select the Japam counter and set mode to `11x`.
    3. Confirm UI displays badge: `"Chant 1 of 11"`.
    4. Fast-forward playback scrubber to the last 3 seconds of the track.
    5. Let track finish.
  * **Expected Result:**
    * Audio seeks back to 00:00 and immediately restarts playing.
    * Counter badge updates to `"Chant 2 of 11"`.
    * Track stops automatically and resets after completing iteration 11.

* **TC-JAPAM-02: Infinite Mode (∞)**
  * **Steps:**
    1. Set loop mode to `∞`.
    2. Allow track to complete end-of-file.
  * **Expected Result:** Track restarts indefinitely until manually paused by the user.

---

### Suite 4: Time-Synced Lyrics Engine (TC-LYRICS)

* **TC-LYRICS-01: Telugu Script Rendering & Font Clarity**
  * **Steps:**
    1. Open the Lyrics view for *Lakshmi Ashtottaram*.
    2. Verify Telugu conjunct characters (*vattulu*, *guninthalu*) like `క్ష్మీ`, `ష్టో`, `త్త` render crisply without broken square glyphs (tofu).
  * **Expected Result:** Correct native glyph rendering using standard system Unicode fonts.

* **TC-LYRICS-02: Real-Time Highlighting & Active Line Scroll**
  * **Steps:**
    1. Play *Krishna Ashtakam*.
    2. Observe the lyrics sheet during stanza transitions.
  * **Expected Result:**
    * The active stanza highlights in Saffron Gold within $\pm 250$ ms of the spoken vocal.
    * The active stanza automatically scrolls to the vertical center of the screen.

* **TC-LYRICS-03: Script Switcher Toggle**
  * **Steps:**
    1. Tap the script switcher pill (`తెలుగు` $\leftrightarrow$ `English`).
  * **Expected Result:** Text instantly transforms to English transliteration without resetting the current scroll position or interrupting audio playback.

* **TC-LYRICS-04: Font Size Scalability**
  * **Steps:**
    1. Use the `+` font scaling control to increase font size to maximum (`28sp`).
  * **Expected Result:** Text wraps cleanly without truncation, overlapping, or clipping off-screen.

---

### Suite 5: Senior Usability & Navigation (TC-UX-SENIOR)

* **TC-UX-01: Minimum Touch Target Compliance**
  * **Inspection:** Verify with Layout Inspector that:
    * Play/Pause in Full Player is $\ge 72 	imes 72$ dp.
    * Mini-player Play/Pause and Next buttons are $\ge 48 	imes 48$ dp.
    * "Get Started" button on the Welcome screen is $\ge 56$ dp in height.
  * **Expected Result:** 100% compliance with Android Accessibility standards (WCAG AAA).

* **TC-UX-02: Session Re-entry Behavior**
  * **Steps:**
    1. Launch app $ightarrow$ Welcome Screen shows $ightarrow$ tap "Get Started" $ightarrow$ Library opens.
    2. Kill the app process from recent apps.
    3. Re-launch the app.
  * **Expected Result:** The Welcome screen with the animated Namaste displays every single time as specified.

* **TC-UX-03: Persistent Mini-Player Bar**
  * **Steps:**
    1. Play any song from the Library screen.
    2. Scroll through the track library.
  * **Expected Result:** Mini-player remains sticky at the bottom above system navigation and does not occlude the last item in the list.

---

### Suite 6: Performance & Storage Compliance (TC-PERF)

* **TC-PERF-01: Release APK Size Ceiling**
  * **Method:** Run `./gradlew assembleRelease` and inspect output `.apk` file.
  * **Target:** Total size $\le 100	ext{ MB}$ (Expected initial 6-track build: $42	ext{ MB} - 48	ext{ MB}$).
  * **Failure Criteria:** Any build exceeding $100	ext{ MB}$.

* **TC-PERF-02: Cold Startup Time**
  * **Method:** Measure cold-start latency using Android Vitals / ADB `am start -W`.
  * **Target:** Initial draw to Welcome Screen $< 1.2$ seconds on mid-range devices.

* **TC-PERF-03: Memory Stability during Long Recitations**
  * **Steps:**
    1. Play *Vishnu Sahasranamam* (30 minutes) on repeat for 2 hours continuously.
    2. Monitor memory allocation using Android Studio Memory Profiler.
  * **Expected Result:** Memory footprint remains flat ($\le 120	ext{ MB}$ RAM consumption) with zero OutOfMemory (OOM) leaks.
