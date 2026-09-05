package com.bhaktidhwani.app.playback

import android.content.Intent
import android.os.Bundle
import androidx.annotation.OptIn
import androidx.media3.common.AudioAttributes
import androidx.media3.common.C
import androidx.media3.common.Player
import androidx.media3.common.util.UnstableApi
import androidx.media3.exoplayer.ExoPlayer
import androidx.media3.session.DefaultMediaNotificationProvider
import androidx.media3.session.MediaSession
import androidx.media3.session.MediaSessionService
import androidx.media3.session.SessionCommand
import androidx.media3.session.SessionCommands
import androidx.media3.session.SessionResult
import com.bhaktidhwani.app.data.model.JapamCounterState
import com.bhaktidhwani.app.data.model.JapamMode
import com.google.common.util.concurrent.Futures
import com.google.common.util.concurrent.ListenableFuture

/**
 * Foreground MediaSessionService that coordinates ExoPlayer audio playback,
 * audio focus management, lock-screen notifications, and the Japam loop counter state machine.
 */
class DevotionalAudioService : MediaSessionService() {

    private var mediaSession: MediaSession? = null
    private lateinit var exoPlayer: ExoPlayer
    private lateinit var notificationManager: MediaNotificationManager

    companion object {
        const val CUSTOM_ACTION_SET_JAPAM_COUNT = "com.bhaktidhwani.app.SET_JAPAM_COUNT"
        const val CUSTOM_ACTION_RESET_JAPAM = "com.bhaktidhwani.app.RESET_JAPAM"
        const val CUSTOM_ACTION_GET_JAPAM_STATE = "com.bhaktidhwani.app.GET_JAPAM_STATE"
        const val EXTRA_JAPAM_TARGET_COUNT = "extra_japam_target_count"
        const val EXTRA_JAPAM_CURRENT_COUNT = "extra_japam_current_count"
        const val EXTRA_JAPAM_MODE_NAME = "extra_japam_mode_name"
    }

    private var japamState: JapamCounterState = JapamCounterState()

    @OptIn(UnstableApi::class)
    override fun onCreate() {
        super.onCreate()

        // 1. Initialize notification channel
        notificationManager = MediaNotificationManager(this)
        notificationManager.createNotificationChannel()

        // 2. Configure ExoPlayer with AudioAttributes for audio focus handling (pause on calls, transient duck)
        val audioAttributes = AudioAttributes.Builder()
            .setUsage(C.USAGE_MEDIA)
            .setContentType(C.AUDIO_CONTENT_TYPE_MUSIC)
            .build()

        exoPlayer = ExoPlayer.Builder(this)
            .setAudioAttributes(audioAttributes, /* handleAudioFocus = */ true)
            .setSeekBackIncrementMs(10000L)
            .setSeekForwardIncrementMs(10000L)
            .build()

        // 3. Attach Japam loop counter state machine listener
        exoPlayer.addListener(object : Player.Listener {
            override fun onPlaybackStateChanged(playbackState: Int) {
                if (playbackState == Player.STATE_ENDED) {
                    handleTrackEnded()
                }
            }

            override fun onMediaItemTransition(mediaItem: androidx.media3.common.MediaItem?, reason: Int) {
                // When a new media item is selected, reset iteration counter to 1
                if (reason == Player.MEDIA_ITEM_TRANSITION_REASON_PLAYLIST_CHANGED) {
                    japamState = japamState.copy(currentIteration = 1)
                }
            }
        })

        // 4. Configure custom commands for MediaSession callback
        val customCommands = SessionCommands.Builder()
            .add(SessionCommand(CUSTOM_ACTION_SET_JAPAM_COUNT, Bundle.EMPTY))
            .add(SessionCommand(CUSTOM_ACTION_RESET_JAPAM, Bundle.EMPTY))
            .add(SessionCommand(CUSTOM_ACTION_GET_JAPAM_STATE, Bundle.EMPTY))
            .build()

        val sessionCallback = object : MediaSession.Callback {
            override fun onConnect(
                session: MediaSession,
                controller: MediaSession.ControllerInfo
            ): MediaSession.ConnectionResult {
                val connectionResult = super.onConnect(session, controller)
                val availableSessionCommands = connectionResult.availableSessionCommands
                    .buildUpon()
                    .add(SessionCommand(CUSTOM_ACTION_SET_JAPAM_COUNT, Bundle.EMPTY))
                    .add(SessionCommand(CUSTOM_ACTION_RESET_JAPAM, Bundle.EMPTY))
                    .add(SessionCommand(CUSTOM_ACTION_GET_JAPAM_STATE, Bundle.EMPTY))
                    .build()
                return MediaSession.ConnectionResult.accept(
                    availableSessionCommands,
                    connectionResult.availablePlayerCommands
                )
            }

            override fun onCustomCommand(
                session: MediaSession,
                controller: MediaSession.ControllerInfo,
                customCommand: SessionCommand,
                args: Bundle
            ): ListenableFuture<SessionResult> {
                when (customCommand.customAction) {
                    CUSTOM_ACTION_SET_JAPAM_COUNT -> {
                        val target = args.getInt(EXTRA_JAPAM_TARGET_COUNT, 1)
                        val mode = JapamMode.fromTargetCount(target)
                        japamState = JapamCounterState(
                            mode = mode,
                            currentIteration = 1,
                            totalTarget = if (mode == JapamMode.INFINITE) -1 else mode.targetCount
                        )
                        return Futures.immediateFuture(
                            SessionResult(SessionResult.RESULT_SUCCESS, createJapamBundle())
                        )
                    }
                    CUSTOM_ACTION_RESET_JAPAM -> {
                        japamState = japamState.copy(currentIteration = 1)
                        return Futures.immediateFuture(
                            SessionResult(SessionResult.RESULT_SUCCESS, createJapamBundle())
                        )
                    }
                    CUSTOM_ACTION_GET_JAPAM_STATE -> {
                        return Futures.immediateFuture(
                            SessionResult(SessionResult.RESULT_SUCCESS, createJapamBundle())
                        )
                    }
                }
                return super.onCustomCommand(session, controller, customCommand, args)
            }
        }

        // 5. Initialize MediaSession
        mediaSession = MediaSession.Builder(this, exoPlayer)
            .setCallback(sessionCallback)
            .build()

        // 6. Set Notification Provider
        setMediaNotificationProvider(
            DefaultMediaNotificationProvider.Builder(this)
                .setChannelId(MediaNotificationManager.CHANNEL_ID)
                .setNotificationId(MediaNotificationManager.NOTIFICATION_ID)
                .build()
        )
    }

    private fun handleTrackEnded() {
        val isInfinite = japamState.mode == JapamMode.INFINITE
        val canLoop = isInfinite || japamState.currentIteration < japamState.totalTarget

        if (canLoop) {
            japamState = japamState.copy(currentIteration = japamState.currentIteration + 1)
            exoPlayer.seekTo(0L)
            exoPlayer.play()
        } else {
            exoPlayer.pause()
            exoPlayer.seekTo(0L)
        }
    }

    private fun createJapamBundle(): Bundle {
        return Bundle().apply {
            putInt(EXTRA_JAPAM_CURRENT_COUNT, japamState.currentIteration)
            putInt(EXTRA_JAPAM_TARGET_COUNT, japamState.totalTarget)
            putString(EXTRA_JAPAM_MODE_NAME, japamState.mode.name)
        }
    }

    override fun onGetSession(controllerInfo: MediaSession.ControllerInfo): MediaSession? {
        return mediaSession
    }

    override fun onTaskRemoved(rootIntent: Intent?) {
        val player = mediaSession?.player
        if (player == null || !player.playWhenReady || player.mediaItemCount == 0) {
            stopSelf()
        }
    }

    override fun onDestroy() {
        mediaSession?.run {
            player.release()
            release()
            mediaSession = null
        }
        super.onDestroy()
    }
}
