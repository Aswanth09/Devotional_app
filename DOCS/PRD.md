# Product Requirement Document (PRD)

## 1. Product Overview
* **Product Name:** Bhakti Dhwani (Offline Devotional Music Player)
* **Target Audience:** Family, parents, and elderly users seeking a simple, friction-free devotional chanting and music experience.
* **Core Value Proposition:** A Spotify-inspired, 100% offline devotional audio streaming experience with built-in voice-optimized audio compression, time-synchronized Telugu/English lyrics, senior-friendly high-contrast UI, and spiritual utilities like Japam/loop counters.
* **Primary Platform:** Android (Native Kotlin / Jetpack Compose).
* **Delivery Mechanism:** Direct APK installation (Target size: < 100 MB with bundled offline audio assets).

---

## 2. User Personas & Problems Addressed

### Persona 1: Elderly Parent / Homemaker
* **Needs:** 
  * Wants to listen to *Vishnu Sahasranamam*, *Govinda Namalu*, or *Hanuman Chalisa* during morning pooja or evening prayers.
  * Prefers reading along in Telugu script.
  * Struggles with tiny buttons, complex nested menus, ads, and network buffering issues common on commercial apps (Spotify/YouTube).
* **Pain Points Addressed:**
  * Zero reliance on internet connectivity (works seamlessly in airplane mode or pooja rooms without Wi-Fi).
  * High-contrast UI, extra-large touch targets (minimum 48-64 dp), clear typography.
  * Time-synced lyrics with auto-scrolling and active line highlighting in native Telugu.

### Persona 2: Working Professional / Chanting Practitioner
* **Needs:**
  * Repeated chanting (*Japam*) for stotras like *Hanuman Chalisa* (e.g., 11 times or 21 times).
  * Smooth lock-screen and notification controls so playback doesn't stop when walking or multitasking.
* **Pain Points Addressed:**
  * Native Japam/Loop counter preset (1x, 11x, 21x, 108x, Infinite).
  * Background playback service powered by Android Jetpack Media3.

---

## 3. Scope & Release Strategy

### Phase 1: Launch Roster (6 Core Offline Tracks)
1. **Vishnu Sahasranamam** (Lord Vishnu) — ~28–30 min
2. **Hanuman Chalisa** (Lord Hanuman) — ~9–10 min
3. **Govinda Namalu** (Lord Venkateswara) — ~5–6 min
4. **Lakshmi Ashtottaram (108 Names)** (Goddess Lakshmi) — ~6–7 min
5. **Garuda Gamana Tava** (Lord Vishnu / Krishna) — ~4–5 min
6. **Krishna Ashtakam** (*Krishnam Vande...*) (Lord Krishna) — ~4–5 min

### Phase 2: Catalog Expansion (Up to 15–20 Tracks)
* Expansion capacity up to 20 tracks while maintaining the strict **< 100 MB APK ceiling** using built-in automated 80 kbps AAC-LC / Opus compression.

---

## 4. Key Functional Requirements

### 4.1. Welcome & Onboarding Experience
* **Frequency:** App opens to the Welcome Screen **every single session** to establish a peaceful, reverent entry mindset.
* **Hero Element:** Centered **Animated Namaste (Pranama)** vector animation (Lottie `.json` asset, lightweight < 40 KB).
* **Headline:** *"Welcome to Devotional Songs"* (Telugu: *"భక్తి గీతాలు - స్వాగతం"* optional bilingual header).
* **Primary Call to Action (CTA):** Prominent, high-contrast button labeled **"Get Started"** (Large touch target, elevation, haptic feedback) navigating directly to the Main Library.

### 4.2. Spotify-Style Library & Browsing
* **Header Bar:** Warm greeting (dynamic: *"శ్రీరామ జయం - శుభోదయం"* / *"Good Morning"*) with quick search.
* **Horizontal Filter Chips (Sticky Bar):**
  * `All` | `Vishnu` | `Venkateswara` | `Hanuman` | `Lakshmi` | `Krishna`
* **Featured Quick-Access Grid (2x2):**
  * Quick-launch cards for high-frequency daily prayers (*Hanuman Chalisa*, *Govinda Namalu*).
* **Vertical Track List (Spotify Layout):**
  * **Artwork Thumbnail:** High-definition, compressed WebP deity image (rounded corners, 56x56 dp).
  * **Title & Subtitle:** Large bold Telugu title with secondary English transliteration and deity classification.
  * **Trailing Action:** Duration indicator and instant Play shortcut.
* **Persistent Bottom Mini-Player:**
  * Floats above system navigation when a track is active.
  * Shows track thumbnail, scrolling track title, instant Play/Pause button, and progress indicator.
  * Tapping expands into the Full-Screen Audio Player.

### 4.3. Full-Screen Audio Player
* **Visuals:** Large central deity artwork with soft ambient glow matching deity color tones.
* **Playback Controls:**
  * Extra-large Play/Pause button (72x72 dp touch target).
  * Previous / Next track buttons.
  * 10-second seek backward / forward buttons for easy re-listening to stanzas.
  * Interactive scrubber with elapsed time and remaining duration.
* **Japam / Repeat Counter:**
  * Dedicated loop selector button: Cycle through `Off`, `11x`, `21x`, `108x`, `∞ (Infinite)`.
  * Visual badge displaying current iteration (e.g., *"Chant 3 of 11"*).
* **Lyrics Sheet Launcher:** Swipe-up gesture or dedicated "Lyrics" pill button to reveal synchronized lyrics.

### 4.4. Time-Synchronized Lyrics Engine
* **Format Support:** Bundled `.lrc` (LRC format with millisecond timestamps `[mm:ss.xx]`) or structured JSON timestamps.
* **Dual Script Toggle:** Instant 1-tap switcher:
  * **తెలుగు (Telugu - Default & Primary)**
  * **English (Transliteration)**
* **Real-Time Highlighting (Karaoke Mode):**
  * The active stanza/line dynamically illuminates with high contrast (Saffron Gold background tint / bold text).
  * Smooth auto-scroll keeps the current line centered on screen.
* **Typography Controls:** Accessibility font-size adjustment (+ / -) to allow elderly users to scale text from `18sp` to `28sp`.

### 4.5. Audio Engine & Background Playback
* **Architecture:** Android Jetpack Media3 (`ExoPlayer`) integrated with a foreground `MediaSessionService`.
* **Lock Screen & Notification Controls:**
  * Persistent media notification with Play, Pause, Skip, and Repeat controls.
  * Deity artwork displayed on lock screen.
* **Audio Focus Management:** Gracefully pauses during incoming phone calls and resumes after call termination.

---

## 5. Non-Functional & Technical Constraints

| Parameter | Specification |
| :--- | :--- |
| **Total Target APK Size** | Strictly $\le 100	ext{ MB}$ (with 6 initial tracks $pprox 45	ext{ MB}$; up to 20 tracks $pprox 85	ext{ MB}$) |
| **Audio Compression Profile** | AAC-LC / M4A at $80	ext{ kbps}$ joint-stereo / speech profile ($44.1	ext{ kHz}$) |
| **Offline Reliability** | 100% offline. Zero remote API network calls or external CDN dependencies. |
| **Android Version Support** | Min SDK: 24 (Android 7.0 Nougat) to cover older family devices; Target SDK: 34+ |
| **UI Framework** | 100% Jetpack Compose with Material 3 design tokens |
| **Performance Target** | App cold startup $< 1.2	ext{ seconds}$; zero audio glitching on screen lock |

---

## 6. Compression & Asset Pipeline

To ensure maximum audio clarity with minimum file footprint:
* **Audio Encoding Pipeline:**
  * Master recordings are pre-processed through automated FFmpeg script:
    `ffmpeg -i input.wav -c:a aac -b:a 80k -ar 44100 -ac 2 output.m4a`
  * High frequencies ($>16	ext{ kHz}$) rolled off smoothly to optimize speech clarity and eliminate hiss.
* **Image Compression:**
  * All deity artworks converted to WebP at 80% quality ($< 45	ext{ KB}$ per image).
* **Animation Asset:**
  * Namaste animation embedded as lightweight vector Lottie JSON ($< 35	ext{ KB}$).

---

## 7. Success Criteria & Acceptance Metrics

1. **Self-Contained Functionality:** App installs via APK, launches in Airplane Mode, and plays all 6 tracks with synchronized Telugu lyrics without a single dropped frame or network prompt.
2. **Elderly Usability Standard:** All primary controls exceed 48 dp; default Telugu typography is easily readable at arm's length.
3. **Chant Accuracy:** Synchronized highlighting precisely matches the recitation timestamp within $\pm 250	ext{ ms}$.
4. **Storage Compliance:** Built release APK size does not exceed 100 MB.
