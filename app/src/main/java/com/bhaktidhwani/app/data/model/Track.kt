package com.bhaktidhwani.app.data.model

import androidx.annotation.DrawableRes
import androidx.annotation.RawRes

/**
 * Represents a devotional audio track in Bhakti Dhwani.
 * Contains both Telugu and English metadata, deity classification, and local resource bindings.
 */
data class Track(
    val id: String,
    val titleTelugu: String,
    val titleEnglish: String,
    val deity: String,
    val deityTelugu: String,
    @RawRes val rawResId: Int,
    @DrawableRes val thumbnailResId: Int,
    val durationMs: Long,
    val lyricsAssetPath: String,
    val descriptionTelugu: String = "",
    val descriptionEnglish: String = ""
)
