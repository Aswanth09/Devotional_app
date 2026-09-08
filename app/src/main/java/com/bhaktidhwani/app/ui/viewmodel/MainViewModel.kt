package com.bhaktidhwani.app.ui.viewmodel

import android.app.Application
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.viewModelScope
import com.bhaktidhwani.app.data.model.JapamCounterState
import com.bhaktidhwani.app.data.model.JapamMode
import com.bhaktidhwani.app.data.model.Stanza
import com.bhaktidhwani.app.data.model.Track
import com.bhaktidhwani.app.data.repository.LocalAudioRepository
import com.bhaktidhwani.app.playback.DevotionalMediaController
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.SharingStarted
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.combine
import kotlinx.coroutines.flow.stateIn
import kotlinx.coroutines.launch

enum class ScriptMode {
    TELUGU,
    ENGLISH
}

/**
 * Main ViewModel orchestrating library tracks, playback controls,
 * time-synced lyrics calculation, and elder-friendly font scaling.
 */
class MainViewModel(
    application: Application,
    val repository: LocalAudioRepository = LocalAudioRepository(),
    val mediaController: DevotionalMediaController = DevotionalMediaController(application, repository)
) : AndroidViewModel(application) {

    // Category Filter
    private val _selectedCategory = MutableStateFlow("All")
    val selectedCategory: StateFlow<String> = _selectedCategory.asStateFlow()

    // Track Listing
    private val _allTracks = MutableStateFlow(repository.getTracks())
    val tracks: StateFlow<List<Track>> = combine(_allTracks, _selectedCategory) { tracks, category ->
        if (category == "All") tracks else tracks.filter { it.deity.equals(category, ignoreCase = true) }
    }.stateIn(viewModelScope, SharingStarted.Lazily, repository.getTracks())

    // 2x2 Quick picks for morning chants
    val quickPicks: List<Track> = repository.getTracks().take(4)

    val categories: List<String> = repository.getDeityCategories()

    // Playback States forwarded from MediaController
    val activeTrack: StateFlow<Track?> = mediaController.currentTrack
    val isPlaying: StateFlow<Boolean> = mediaController.isPlaying
    val playbackState: StateFlow<Int> = mediaController.playbackState
    val isBuffering: StateFlow<Boolean> = mediaController.isBuffering
    val currentPositionMs: StateFlow<Long> = mediaController.currentPositionMs
    val durationMs: StateFlow<Long> = mediaController.durationMs
    val playbackSpeed: StateFlow<Float> = mediaController.playbackSpeed
    val japamState: StateFlow<JapamCounterState> = mediaController.japamState

    // Time-Synced Lyrics
    private val _stanzas = MutableStateFlow<List<Stanza>>(emptyList())
    val stanzas: StateFlow<List<Stanza>> = _stanzas.asStateFlow()

    // Script & Font Accessibility
    private val _scriptMode = MutableStateFlow(ScriptMode.TELUGU)
    val scriptMode: StateFlow<ScriptMode> = _scriptMode.asStateFlow()

    private val _fontScaleDeltaSp = MutableStateFlow(0)
    val fontScaleDeltaSp: StateFlow<Int> = _fontScaleDeltaSp.asStateFlow()

    // Current active stanza computed in real time
    val activeStanzaIndex: StateFlow<Int> = combine(currentPositionMs, _stanzas) { position, lyrics ->
        findActiveStanza(position, lyrics)
    }.stateIn(viewModelScope, SharingStarted.Lazily, -1)

    init {
        // Automatically load lyrics whenever activeTrack changes
        viewModelScope.launch {
            activeTrack.collect { track ->
                if (track != null) {
                    val loaded = repository.loadLyrics(getApplication(), track.lyricsAssetPath)
                    _stanzas.value = loaded
                } else {
                    _stanzas.value = emptyList()
                }
            }
        }
    }

    private fun findActiveStanza(positionMs: Long, lyrics: List<Stanza>): Int {
        if (lyrics.isEmpty()) return -1
        for (i in lyrics.indices) {
            val stanza = lyrics[i]
            if (positionMs in stanza.startTimeMs until stanza.endTimeMs) {
                return i
            }
        }
        // If past the last stanza's start, return last
        if (positionMs >= lyrics.last().startTimeMs) {
            return lyrics.lastIndex
        }
        return 0
    }

    fun selectCategory(category: String) {
        _selectedCategory.value = category
    }

    fun playTrack(track: Track) {
        mediaController.playTrack(track)
    }

    fun play() {
        mediaController.play()
    }

    fun pause() {
        mediaController.pause()
    }

    fun playPause() {
        mediaController.playPause()
    }

    fun seekTo(positionMs: Long) {
        mediaController.seekTo(positionMs)
    }

    fun seekForward(ms: Long = 10000L) {
        mediaController.seekForward(ms)
    }

    fun seekBackward(ms: Long = 10000L) {
        mediaController.seekBackward(ms)
    }

    fun setPlaybackSpeed(speed: Float) {
        mediaController.setPlaybackSpeed(speed)
    }

    fun setJapamMode(mode: JapamMode) {
        mediaController.setJapamMode(mode)
    }

    fun resetJapamCounter() {
        mediaController.resetJapamCounter()
    }

    fun toggleScript() {
        _scriptMode.value = if (_scriptMode.value == ScriptMode.TELUGU) ScriptMode.ENGLISH else ScriptMode.TELUGU
    }

    fun increaseFontSize() {
        if (_fontScaleDeltaSp.value < 8) {
            _fontScaleDeltaSp.value += 2
        }
    }

    fun decreaseFontSize() {
        if (_fontScaleDeltaSp.value > -2) {
            _fontScaleDeltaSp.value -= 2
        }
    }

    override fun onCleared() {
        super.onCleared()
        mediaController.release()
    }
}
