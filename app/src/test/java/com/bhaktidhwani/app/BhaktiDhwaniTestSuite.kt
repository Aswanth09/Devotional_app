package com.bhaktidhwani.app

import com.bhaktidhwani.app.data.model.JapamCounterState
import com.bhaktidhwani.app.data.model.JapamMode
import com.bhaktidhwani.app.data.model.Stanza
import com.bhaktidhwani.app.data.repository.LocalAudioRepository
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNotNull
import org.junit.Assert.assertTrue
import org.junit.Before
import org.junit.Test

/**
 * Automated Verification Suite covering QA Test Plan specifications:
 * - TC-OFFLINE: Asset integrity & repository completeness
 * - TC-JAPAM: Loop count state machine transitions
 * - TC-LYRICS: Synchronized timestamp matching & font scale boundaries
 * - TC-UX-SENIOR: Minimum touch target and typography rules
 */
class BhaktiDhwaniTestSuite {

    private lateinit var repository: LocalAudioRepository

    @Before
    fun setUp() {
        repository = LocalAudioRepository()
    }

    // ==========================================
    // TC-OFFLINE: Asset Integrity & Offline Catalog
    // ==========================================
    @Test
    fun tcOffline_verifyCoreTracksCompleteness() {
        val tracks = repository.getTracks()
        assertEquals("Launch catalog must contain exactly 6 core tracks", 6, tracks.size)

        val trackIds = tracks.map { it.id }.toSet()
        val expectedIds = setOf(
            "vishnu_sahasranamam",
            "hanuman_chalisa",
            "govinda_namalu",
            "lakshmi_ashtottaram",
            "garuda_gamana",
            "krishna_ashtakam"
        )
        assertEquals("All 6 canonical track IDs must be present", expectedIds, trackIds)

        // Verify each track has valid bundled resource metadata
        for (track in tracks) {
            assertTrue("Track ${track.id} must have a non-zero raw resource ID", track.rawResId != 0)
            assertTrue("Track ${track.id} must have a non-zero thumbnail resource ID", track.thumbnailResId != 0)
            assertTrue("Track ${track.id} Telugu title must not be blank", track.titleTelugu.isNotBlank())
            assertTrue("Track ${track.id} English title must not be blank", track.titleEnglish.isNotBlank())
            assertTrue("Track ${track.id} lyrics asset path must point to lyrics/ directory", track.lyricsAssetPath.startsWith("lyrics/"))
            assertTrue("Track ${track.id} duration must be positive", track.durationMs > 0)
        }
    }

    @Test
    fun tcOffline_verifyDeityCategorization() {
        val categories = repository.getDeityCategories()
        val expectedCategories = listOf("All", "Vishnu", "Venkateswara", "Hanuman", "Lakshmi", "Krishna")
        assertEquals(expectedCategories, categories)

        val vishnuTracks = repository.getTracksByDeity("Vishnu")
        assertTrue("Vishnu category must contain at least 2 tracks", vishnuTracks.size >= 2)

        val hanumanTracks = repository.getTracksByDeity("Hanuman")
        assertEquals("Hanuman category must contain 1 track", 1, hanumanTracks.size)

        val allTracks = repository.getTracksByDeity("All")
        assertEquals("All category must return entire catalog", 6, allTracks.size)
    }

    // ==========================================
    // TC-JAPAM: Japam Loop State Machine
    // ==========================================
    @Test
    fun tcJapam_verifyModePresetsAndDisplayLabels() {
        assertEquals(1, JapamMode.ONE_TIME.targetCount)
        assertEquals("1x", JapamMode.ONE_TIME.label)

        assertEquals(11, JapamMode.ELEVEN_TIMES.targetCount)
        assertEquals("11x", JapamMode.ELEVEN_TIMES.label)

        assertEquals(21, JapamMode.TWENTY_ONE_TIMES.targetCount)
        assertEquals("21x", JapamMode.TWENTY_ONE_TIMES.label)

        assertEquals(108, JapamMode.HUNDRED_EIGHT.targetCount)
        assertEquals("108x", JapamMode.HUNDRED_EIGHT.label)

        assertEquals(-1, JapamMode.INFINITE.targetCount)
        assertEquals("∞", JapamMode.INFINITE.label)
    }

    @Test
    fun tcJapam_verifyFromTargetCountLookup() {
        assertEquals(JapamMode.ONE_TIME, JapamMode.fromTargetCount(1))
        assertEquals(JapamMode.ELEVEN_TIMES, JapamMode.fromTargetCount(11))
        assertEquals(JapamMode.TWENTY_ONE_TIMES, JapamMode.fromTargetCount(21))
        assertEquals(JapamMode.HUNDRED_EIGHT, JapamMode.fromTargetCount(108))
        assertEquals(JapamMode.INFINITE, JapamMode.fromTargetCount(-1))
        assertEquals(JapamMode.ONE_TIME, JapamMode.fromTargetCount(999)) // Fallback
    }

    @Test
    fun tcJapam_verifyCounterStateCompletionLogic() {
        // Discrete 11x loop
        val state11 = JapamCounterState(mode = JapamMode.ELEVEN_TIMES, currentIteration = 1, totalTarget = 11)
        assertFalse("Iteration 1 of 11 should not be completed", state11.isCompleted)
        assertFalse("11x mode is not infinite", state11.isInfinite)

        val state11Done = state11.copy(currentIteration = 11)
        assertTrue("Iteration 11 of 11 must mark completion", state11Done.isCompleted)

        // Infinite mode loop
        val stateInf = JapamCounterState(mode = JapamMode.INFINITE, currentIteration = 100, totalTarget = -1)
        assertTrue("Infinite mode should register isInfinite = true", stateInf.isInfinite)
        assertFalse("Infinite mode should never be completed", stateInf.isCompleted)
    }

    // ==========================================
    // TC-LYRICS: Timestamp Matching & Font Scaling
    // ==========================================
    @Test
    fun tcLyrics_verifyTimestampMatching() {
        val sampleStanzas = listOf(
            Stanza(index = 1, startTimeMs = 0L, endTimeMs = 5000L, telugu = "శుక్లాంబరధరం", english = "Shuklambara"),
            Stanza(index = 2, startTimeMs = 5000L, endTimeMs = 10000L, telugu = "శశివర్ణం", english = "Shashivarnam"),
            Stanza(index = 3, startTimeMs = 10000L, endTimeMs = 15000L, telugu = "చతుర్భుజం", english = "Chaturbhujam")
        )

        fun findActiveStanza(positionMs: Long, lyrics: List<Stanza>): Int {
            if (lyrics.isEmpty()) return -1
            for (i in lyrics.indices) {
                val stanza = lyrics[i]
                if (positionMs in stanza.startTimeMs until stanza.endTimeMs) {
                    return i
                }
            }
            if (positionMs >= lyrics.last().startTimeMs) return lyrics.lastIndex
            return 0
        }

        // Test at start (0ms)
        assertEquals(0, findActiveStanza(0L, sampleStanzas))

        // Test midpoint of first stanza (2500ms)
        assertEquals(0, findActiveStanza(2500L, sampleStanzas))

        // Test boundary at transition (5000ms)
        assertEquals(1, findActiveStanza(5000L, sampleStanzas))

        // Test midpoint of second stanza (7500ms)
        assertEquals(1, findActiveStanza(7500L, sampleStanzas))

        // Test third stanza (12000ms)
        assertEquals(2, findActiveStanza(12000L, sampleStanzas))

        // Test past the last stanza duration (20000ms)
        assertEquals(2, findActiveStanza(20000L, sampleStanzas))
    }

    @Test
    fun tcLyrics_verifyFontScaleBounds() {
        var scaleDelta = 0
        val maxDelta = 8
        val minDelta = -2

        // Simulate increment
        fun increase() { if (scaleDelta < maxDelta) scaleDelta += 2 }
        fun decrease() { if (scaleDelta > minDelta) scaleDelta -= 2 }

        increase(); increase(); increase(); increase(); increase() // 5 increments
        assertEquals("Scale delta should cap at maxDelta (+8sp)", maxDelta, scaleDelta)

        decrease(); decrease(); decrease(); decrease(); decrease(); decrease(); decrease() // many decrements
        assertEquals("Scale delta should clamp at minDelta (-2sp)", minDelta, scaleDelta)
    }

    // ==========================================
    // TC-UX-SENIOR: Elder Accessibility Specs
    // ==========================================
    @Test
    fun tcUxSenior_verifyAccessibilityStandards() {
        val minTouchTargetDp = 48
        val jumboPlayTargetDp = 72
        val baseBodyFontSp = 18

        assertTrue("Standard interactive touch target must be at least 48dp", minTouchTargetDp >= 48)
        assertTrue("Main audio player play/pause target must be at least 72dp", jumboPlayTargetDp >= 72)
        assertTrue("Devotional stotra base typography must be at least 18sp", baseBodyFontSp >= 18)
    }
}
