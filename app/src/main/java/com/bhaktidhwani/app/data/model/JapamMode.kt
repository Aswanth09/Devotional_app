package com.bhaktidhwani.app.data.model

/**
 * Loop count presets for Japam chanting.
 */
enum class JapamMode(val targetCount: Int, val label: String) {
    ONE_TIME(1, "1x"),
    ELEVEN_TIMES(11, "11x"),
    TWENTY_ONE_TIMES(21, "21x"),
    HUNDRED_EIGHT(108, "108x"),
    INFINITE(-1, "∞");

    companion object {
        fun fromTargetCount(targetCount: Int): JapamMode {
            return entries.firstOrNull { it.targetCount == targetCount } ?: ONE_TIME
        }
    }
}

/**
 * Runtime state representing the active iteration and target count of Japam chanting.
 */
data class JapamCounterState(
    val mode: JapamMode = JapamMode.ONE_TIME,
    val currentIteration: Int = 1,
    val totalTarget: Int = 1
) {
    val isInfinite: Boolean get() = mode == JapamMode.INFINITE
    val isCompleted: Boolean get() = !isInfinite && currentIteration >= totalTarget
}
