package com.bhaktidhwani.app.data.model

/**
 * Represents a timestamped stanza for time-synchronized stotra chanting.
 */
data class Stanza(
    val index: Int,
    val startTimeMs: Long,
    val endTimeMs: Long,
    val telugu: String,
    val english: String
)
