package com.bhaktidhwani.app.playback

import android.app.NotificationChannel
import android.app.NotificationManager
import android.content.Context
import android.os.Build

/**
 * Manages notification channel configuration and notification presentation for background devotional audio playback.
 */
class MediaNotificationManager(private val context: Context) {

    companion object {
        const val CHANNEL_ID = "devotional_playback_channel"
        const val NOTIFICATION_ID = 1008
    }

    init {
        createNotificationChannel()
    }

    fun createNotificationChannel() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val notificationManager = context.getSystemService(Context.NOTIFICATION_SERVICE) as? NotificationManager
            val existingChannel = notificationManager?.getNotificationChannel(CHANNEL_ID)
            if (existingChannel == null) {
                val channel = NotificationChannel(
                    CHANNEL_ID,
                    "భక్తి ధ్వని • Devotional Playback",
                    NotificationManager.IMPORTANCE_LOW
                ).apply {
                    description = "Continuous stotra chanting with lock-screen devotional controls"
                    setShowBadge(false)
                    lockscreenVisibility = android.app.Notification.VISIBILITY_PUBLIC
                }
                notificationManager?.createNotificationChannel(channel)
            }
        }
    }
}
