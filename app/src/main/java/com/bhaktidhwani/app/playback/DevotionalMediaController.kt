package com.bhaktidhwani.app.playback

import android.content.ComponentName
import android.content.Context
import android.net.Uri
import android.os.Bundle
import androidx.annotation.OptIn
import androidx.core.content.ContextCompat
import androidx.media3.common.MediaItem
import androidx.media3.common.MediaMetadata
import androidx.media3.common.PlaybackParameters
import androidx.media3.common.Player
import androidx.media3.common.util.UnstableApi
import androidx.media3.session.MediaController
import androidx.media3.session.SessionCommand
import androidx.media3.session.SessionResult
import androidx.media3.session.SessionToken
import com.bhaktidhwani.app.data.model.JapamCounterState
import com.bhaktidhwani.app.data.model.JapamMode
import com.bhaktidhwani.app.data.model.Track
import com.bhaktidhwani.app.data.repository.LocalAudioRepository
import com.google.common.util.concurrent.ListenableFuture
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.Job
import kotlinx.coroutines.SupervisorJob
import kotlinx.coroutines.cancel
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.isActive
import kotlinx.coroutines.launch

/**
 * Client-side controller that asynchronously connects Compose UI components
 * to DevotionalAudioService via Media3 MediaController.
 * Exposes observable StateFlows for reactive UI consumption.
 */
@OptIn(UnstableApi::class)
class DevotionalMediaController(
    private val context: Context,
    private val repository: LocalAudioRepository = LocalAudioRepository()
) {

    private val scope = CoroutineScope(SupervisorJob() + Dispatchers.Main)
    private var controllerFuture: ListenableFuture<MediaController>? = null
    private var mediaController: MediaController? = null
    private var positionPollingJob: Job? = null

    // Connection State
    private val _isConnected = MutableStateFlow(false)
    val isConnected: StateFlow<Boolean> = _isConnected.asStateFlow()

    // Playback States
    private val _currentTrack = MutableStateFlow<Track?>(null)
    val currentTrack: StateFlow<Track?> = _currentTrack.asStateFlow()

    private val _isPlaying = MutableStateFlow(false)
    val isPlaying: StateFlow<Boolean> = _isPlaying.asStateFlow()

    private val _playbackState = MutableStateFlow(Player.STATE_IDLE)
    val playbackState: StateFlow<Int> = _playbackState.asStateFlow()

    private val _isBuffering = MutableStateFlow(false)
    val isBuffering: StateFlow<Boolean> = _isBuffering.asStateFlow()

    private val _currentPositionMs = MutableStateFlow(0L)
    val currentPositionMs: StateFlow<Long> = _currentPositionMs.asStateFlow()

    private val _durationMs = MutableStateFlow(0L)
    val durationMs: StateFlow<Long> = _durationMs.asStateFlow()

    private val _playbackSpeed = MutableStateFlow(1.0f)
    val playbackSpeed: StateFlow<Float> = _playbackSpeed.asStateFlow()

    // Japam State
    private val _japamState = MutableStateFlow(JapamCounterState())
    val japamState: StateFlow<JapamCounterState> = _japamState.asStateFlow()

    init {
        initializeController()
    }

    private fun initializeController() {
        try {
            val sessionToken = SessionToken(
                context,
                ComponentName(context, DevotionalAudioService::class.java)
            )

            controllerFuture = MediaController.Builder(context, sessionToken)
                .setListener(object : MediaController.Listener {
                    override fun onCustomCommand(
                        controller: MediaController,
                        command: SessionCommand,
                        args: Bundle
                    ): ListenableFuture<SessionResult> {
                        if (command.customAction == DevotionalAudioService.ACTION_JAPAM_STATE_CHANGED) {
                            updateJapamStateFromBundle(args)
                        }
                        return super.onCustomCommand(controller, command, args)
                    }
                })
                .buildAsync()

            controllerFuture?.addListener({
            try {
                val controller = controllerFuture?.get() ?: return@addListener
                mediaController = controller
                _isConnected.value = true

                // Attach player listener
                controller.addListener(object : Player.Listener {
                    override fun onIsPlayingChanged(playing: Boolean) {
                        _isPlaying.value = playing
                        if (playing) {
                            startPositionPolling()
                        } else {
                            stopPositionPolling()
                            _currentPositionMs.value = controller.currentPosition
                        }
                    }

                    override fun onPlaybackStateChanged(state: Int) {
                        _playbackState.value = state
                        _isBuffering.value = (state == Player.STATE_BUFFERING)
                        _durationMs.value = if (controller.duration > 0) controller.duration else 0L
                    }

                    override fun onMediaItemTransition(mediaItem: MediaItem?, reason: Int) {
                        val id = mediaItem?.mediaId
                        val track = if (id != null) repository.getTrackById(id) else null
                        _currentTrack.value = track
                        _durationMs.value = if (controller.duration > 0) controller.duration else (track?.durationMs ?: 0L)
                    }

                    override fun onPlaybackParametersChanged(playbackParameters: PlaybackParameters) {
                        _playbackSpeed.value = playbackParameters.speed
                    }
                })

                // Sync initial states
                _isPlaying.value = controller.isPlaying
                _playbackState.value = controller.playbackState
                _isBuffering.value = (controller.playbackState == Player.STATE_BUFFERING)
                _durationMs.value = if (controller.duration > 0) controller.duration else 0L
                _playbackSpeed.value = controller.playbackParameters.speed

                val currentId = controller.currentMediaItem?.mediaId
                if (currentId != null) {
                    _currentTrack.value = repository.getTrackById(currentId)
                }

                if (controller.isPlaying) {
                    startPositionPolling()
                }

                // Query initial Japam state
                queryInitialJapamState()

            } catch (e: Exception) {
                _isConnected.value = false
            }
        }, ContextCompat.getMainExecutor(context))
    } catch (t: Throwable) {
        _isConnected.value = false
    }
}

    private fun startPositionPolling() {
        positionPollingJob?.cancel()
        positionPollingJob = scope.launch {
            while (isActive) {
                mediaController?.let { controller ->
                    _currentPositionMs.value = controller.currentPosition
                    if (controller.duration > 0) {
                        _durationMs.value = controller.duration
                    }
                }
                delay(150L) // 150ms smooth update interval for time-synced lyrics
            }
        }
    }

    private fun stopPositionPolling() {
        positionPollingJob?.cancel()
        positionPollingJob = null
    }

    /**
     * Loads and immediately starts playing a devotional track.
     */
    fun playTrack(track: Track) {
        val controller = mediaController ?: return
        val rawUri = Uri.parse("android.resource://${context.packageName}/${track.rawResId}")
        val artworkUri = Uri.parse("android.resource://${context.packageName}/${track.thumbnailResId}")

        val mediaMetadata = MediaMetadata.Builder()
            .setTitle(track.titleTelugu)
            .setSubtitle(track.titleEnglish)
            .setArtist(track.deity)
            .setArtworkUri(artworkUri)
            .build()

        val mediaItem = MediaItem.Builder()
            .setMediaId(track.id)
            .setUri(rawUri)
            .setMediaMetadata(mediaMetadata)
            .build()

        controller.setMediaItem(mediaItem)
        controller.prepare()
        controller.play()
        _currentTrack.value = track
    }

    fun play() {
        mediaController?.play()
    }

    fun pause() {
        mediaController?.pause()
        mediaController?.let {
            _currentPositionMs.value = it.currentPosition
        }
    }

    fun playPause() {
        val controller = mediaController ?: return
        if (controller.isPlaying) {
            pause()
        } else {
            play()
        }
    }

    fun seekTo(positionMs: Long) {
        val controller = mediaController ?: return
        val boundedPosition = positionMs.coerceIn(0L, _durationMs.value.coerceAtLeast(0L))
        controller.seekTo(boundedPosition)
        _currentPositionMs.value = boundedPosition
    }

    fun seekForward(ms: Long = 10000L) {
        val current = _currentPositionMs.value
        seekTo(current + ms)
    }

    fun seekBackward(ms: Long = 10000L) {
        val current = _currentPositionMs.value
        seekTo(current - ms)
    }

    fun setPlaybackSpeed(speed: Float) {
        val controller = mediaController ?: return
        val clampedSpeed = speed.coerceIn(0.5f, 2.0f)
        controller.setPlaybackSpeed(clampedSpeed)
        _playbackSpeed.value = clampedSpeed
    }

    fun setJapamMode(mode: JapamMode) {
        val controller = mediaController ?: return
        val args = Bundle().apply {
            putString(DevotionalAudioService.EXTRA_JAPAM_MODE_NAME, mode.name)
            putInt(DevotionalAudioService.EXTRA_JAPAM_TARGET_COUNT, mode.targetCount)
        }
        val command = SessionCommand(DevotionalAudioService.ACTION_SET_JAPAM_MODE, Bundle.EMPTY)
        controller.sendCustomCommand(command, args)

        _japamState.value = JapamCounterState(
            mode = mode,
            currentIteration = 1,
            totalTarget = if (mode == JapamMode.INFINITE) -1 else mode.targetCount
        )
    }

    fun resetJapamCounter() {
        val controller = mediaController ?: return
        val command = SessionCommand(DevotionalAudioService.ACTION_RESET_JAPAM_COUNTER, Bundle.EMPTY)
        controller.sendCustomCommand(command, Bundle.EMPTY)
        _japamState.value = _japamState.value.copy(currentIteration = 1)
    }

    private fun queryInitialJapamState() {
        val controller = mediaController ?: return
        val command = SessionCommand(DevotionalAudioService.ACTION_GET_JAPAM_STATE, Bundle.EMPTY)
        val future = controller.sendCustomCommand(command, Bundle.EMPTY)
        future.addListener({
            try {
                val result = future.get()
                if (result.resultCode == SessionResult.RESULT_SUCCESS) {
                    updateJapamStateFromBundle(result.extras)
                }
            } catch (e: Exception) {
                // Ignore failure to fetch initial state
            }
        }, ContextCompat.getMainExecutor(context))
    }

    private fun updateJapamStateFromBundle(bundle: Bundle) {
        val current = bundle.getInt(DevotionalAudioService.EXTRA_JAPAM_CURRENT_COUNT, 1)
        val target = bundle.getInt(DevotionalAudioService.EXTRA_JAPAM_TARGET_COUNT, 1)
        val modeName = bundle.getString(DevotionalAudioService.EXTRA_JAPAM_MODE_NAME)
        val mode = if (modeName != null) {
            try {
                JapamMode.valueOf(modeName)
            } catch (e: Exception) {
                JapamMode.fromTargetCount(target)
            }
        } else {
            JapamMode.fromTargetCount(target)
        }

        _japamState.value = JapamCounterState(
            mode = mode,
            currentIteration = current,
            totalTarget = target
        )
    }

    fun release() {
        stopPositionPolling()
        scope.cancel()
        controllerFuture?.let { future ->
            MediaController.releaseFuture(future)
        }
        mediaController = null
        _isConnected.value = false
    }
}
