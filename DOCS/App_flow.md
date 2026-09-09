# App Flow & Navigation Architecture: Devotional Chants

## 1. High-Level Navigation State Machine

```
   ┌────────────────────────────────────────────────────────┐
   │                  Welcome / Intro Screen                │
   │  - Animated Namaste (Pranama Lottie)                   │
   │  - "Welcome to Devotional Songs"                       │
   │  - [Get Started Button]                                │
   └───────────────────────────┬────────────────────────────┘
                               │ Tap "Get Started"
                               ▼
   ┌────────────────────────────────────────────────────────┐
   │            Main Library Screen (Spotify-Style)         │
   │  - Sticky Deity Filter Pills                           │
   │  - Quick Daily Cards (2x2)                             │
   │  - Vertical Devotional Track List                      │
   └─────────────┬────────────────────────────▲─────────────┘
                 │ Tap Track                  │ Back / Swipe Down
                 ▼                            │
   ┌──────────────────────────────────────────┴─────────────┐
   │             Full-Screen Audio Player View              │
   │  - Deity Art & Large Title / Subtitle                  │
   │  - Scrubber & Jumbo Controls                           │
   │  - Japam / Repeat Mode Selector                        │
   └─────────────┬────────────────────────────▲─────────────┘
                 │ Tap / Drag "Lyrics" Pill   │ Dismiss Sheet
                 ▼                            │
   ┌──────────────────────────────────────────┴─────────────┐
   │              Time-Synced Lyrics Sheet                  │
   │  - Dual Language Switcher (తెలుగు / English)           │
   │  - Auto-Scrolling, Highlighting Stanzas                │
   │  - Font Size Scale (+ / -)                             │
   └────────────────────────────────────────────────────────┘
```

---

## 2. Screen-by-Screen User Journeys

### Screen 1: Welcome / Entry Screen (`WelcomeScreen`)
* **Trigger:** App launch (runs on every session).
* **UI Elements:**
  * Background gradient: Warm Temple Gold (`#FFF8E7` to `#FFE082`) or Deep Spiritual Maroon.
  * Centered Lottie animation of folding palms (*Namaste*).
  * Main headline: *"భక్తి గీతాలు - స్వాగతం"* / *"Welcome to Devotional Songs"*.
  * Subtext: *"Offline Chants & Stotras for Daily Peace"*.
  * Bottom CTA: Large elevated button *"Get Started"*.
* **Actions & Transitions:**
  * Tapping **"Get Started"** navigates to `LibraryScreen` via a smooth fade-in slide transition.
  * The back button from `LibraryScreen` closes the app (Welcome screen is popped off the backstack to prevent loop traps).

### Screen 2: Devotional Library (`LibraryScreen`)
* **Header Area:**
  * Greeting text: *"శుభోదయం / Good Morning"*.
  * Search bar icon for fast in-memory track filtering.
* **Filter Pills (Horizontal Carousel):**
  * Chips: `All`, `Vishnu`, `Venkateswara`, `Hanuman`, `Lakshmi`, `Krishna`.
  * Tapping a chip filters the list below instantly without latency.
* **Top 2x2 Quick Cards:**
  * Most frequent morning stotras (*Hanuman Chalisa*, *Govinda Namalu*).
  * Tapping immediately starts playback.
* **Main Track List (Spotify Layout):**
  * Each item displays: Deity WebP artwork, Telugu Track Name (bold 18sp), Deity category, Duration, and a round Play button.
  * Tapping any track launches playback and presents the **Mini-Player Bar** or immediately expands into the **Full Player**.
* **Persistent Bottom Mini-Player Bar:**
  * Visible globally above system navigation whenever a song is active.
  * Displays: Small deity thumbnail, marquee scrolling song title, large Play/Pause toggle, and a thin linear progress bar.
  * Tap interaction: Expands smoothly into `PlayerScreen`.

### Screen 3: Full-Screen Audio Player (`PlayerScreen`)
* **Presentation:** Modal bottom sheet or shared element transition expanding from the Mini-Player.
* **UI Hierarchy:**
  * **Top Bar:** Collapse chevron button (down arrow) and Track Deity Title.
  * **Center:** Rounded artwork portrait (280x280 dp) with subtle drop shadow.
  * **Track Info:** Title in large bold Telugu script (`22sp`) and English subtext (`16sp`).
  * **Scrubber Bar:** High-contrast slider with clear elapsed and remaining timestamps.
  * **Controls Strip:**
    * Left: 10s Rewind.
    * Center: Jumbo Play/Pause button (`72x72 dp`).
    * Right: 10s Fast-Forward.
  * **Japam (Chant Repeat) Pill:**
    * Tapping cycles state: `1x` $ightarrow$ `11x` $ightarrow$ `21x` $ightarrow$ `108x` $ightarrow$ `∞`.
    * Displays active chant HUD: *"Chant 2 of 11"*.
  * **Lyrics Bottom Trigger:** Prominent pill button labeled *"Lyrics / సాహిత్యం ⌃"*.

### Screen 4: Time-Synced Lyrics Modal (`LyricsScreen`)
* **Presentation:** Swipe-up full-height bottom sheet layered over the player.
* **Top Header Controls:**
  * **Language Switcher:** Segmented pill toggle: `[ తెలుగు ]` | `[ English ]`.
  * **Text Scaler:** Accessibility buttons `[ A- ]` and `[ A+ ]` adjusting font size between `18sp` and `28sp`.
  * Close / Drag handle bar.
* **Dynamic Lyrics Feed:**
  * Vertical `LazyColumn` showing complete stanzas.
  * **Synchronized State:** The active verse highlights with a soft saffron glow background, bold gold lettering, and smoothly auto-scrolls to viewport center.
  * **Manual Override:** The user can freely scroll up/down without pausing playback.

---

## 3. Jetpack Compose Navigation & Backstack Definition

| Route | Composable Target | Backstack Behavior | Transition Animation |
| :--- | :--- | :--- | :--- |
| `"welcome"` | `WelcomeScreen()` | Replaced upon launch (`popUpTo("welcome") { inclusive = true }`) | Fade out |
| `"library"` | `LibraryScreen()` | App root destination. Pressing hardware Back exits app. | Slide in from right |
| `"player"` | `PlayerScreen()` | Modal / Bottom Sheet over `"library"`. Back dismisses to Library. | Slide up from bottom |
| `"lyrics"` | `LyricsModalSheet()` | Sub-sheet attached to `"player"`. Back collapses to Player. | Slide up modal |

---

## 4. Audio Playback State Lifecycle Flow

1. **User taps a song card** $ightarrow$ UI dispatches `PlayTrackIntent(trackId)` to `DevotionalViewModel`.
2. **`DevotionalAudioService`** receives MediaController command:
   * Sets up ExoPlayer with local asset URI (`android.resource://...`).
   * Starts foreground service with system notification.
   * Requests audio focus.
3. **Screen off / Device Locked:**
   * Notification shade maintains track state.
   * Lock screen displays deity artwork and Play/Pause controls.
4. **Track completion:**
   * If `currentIteration < targetLoopCount`: Increments counter, seeks to 0, loops seamlessly.
   * If loop count met: Plays next track in queue or stops gracefully.
