package com.bhaktidhwani.app.ui.screens

import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Forward10
import androidx.compose.material.icons.filled.KeyboardArrowDown
import androidx.compose.material.icons.filled.KeyboardArrowUp
import androidx.compose.material.icons.filled.Pause
import androidx.compose.material.icons.filled.PlayArrow
import androidx.compose.material.icons.filled.Replay10
import androidx.compose.material.icons.filled.Repeat
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Slider
import androidx.compose.material3.SliderDefaults
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.bhaktidhwani.app.data.model.JapamMode
import com.bhaktidhwani.app.ui.theme.DevotionalSurface
import com.bhaktidhwani.app.ui.theme.GoldenAuraGradient
import com.bhaktidhwani.app.ui.theme.RichGold
import com.bhaktidhwani.app.ui.theme.SacredSaffron
import com.bhaktidhwani.app.ui.theme.SaffronGoldGradient
import com.bhaktidhwani.app.ui.theme.SanctumFloor
import com.bhaktidhwani.app.ui.theme.SurfaceContainer
import com.bhaktidhwani.app.ui.theme.TempleGold
import com.bhaktidhwani.app.ui.theme.WarmIvory
import com.bhaktidhwani.app.ui.viewmodel.MainViewModel

/**
 * Full Audio Player Screen featuring large 280x280dp deity artwork,
 * Japam mode selector, 72dp jumbo play button, high-contrast scrubber,
 * and swipe-up lyrics trigger.
 */
@Composable
fun PlayerScreen(
    viewModel: MainViewModel,
    onCollapse: () -> Unit,
    onOpenLyrics: () -> Unit
) {
    val activeTrack by viewModel.activeTrack.collectAsState()
    val isPlaying by viewModel.isPlaying.collectAsState()
    val currentPositionMs by viewModel.currentPositionMs.collectAsState()
    val durationMs by viewModel.durationMs.collectAsState()
    val japamState by viewModel.japamState.collectAsState()
    val scrollState = rememberScrollState()

    val track = activeTrack ?: return

    Surface(
        modifier = Modifier.fillMaxSize(),
        color = SanctumFloor
    ) {
        Column(
            modifier = Modifier
                .fillMaxSize()
                .background(GoldenAuraGradient)
                .verticalScroll(scrollState)
                .padding(horizontal = 24.dp, vertical = 16.dp),
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.SpaceBetween
        ) {
            // Top Navigation Bar with Downward Collapse Caret
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(top = 8.dp),
                horizontalArrangement = Arrangement.SpaceBetween,
                verticalAlignment = Alignment.CenterVertically
            ) {
                IconButton(
                    onClick = onCollapse,
                    modifier = Modifier
                        .size(48.dp)
                        .clip(CircleShape)
                        .background(SurfaceContainer)
                ) {
                    Icon(
                        imageVector = Icons.Default.KeyboardArrowDown,
                        contentDescription = "Collapse Player",
                        tint = TempleGold,
                        modifier = Modifier.size(32.dp)
                    )
                }

                // Deity Badge
                Surface(
                    shape = RoundedCornerShape(20.dp),
                    color = DevotionalSurface,
                    border = androidx.compose.foundation.BorderStroke(1.dp, RichGold.copy(alpha = 0.3f))
                ) {
                    Text(
                        text = track.deityTelugu,
                        style = MaterialTheme.typography.labelMedium,
                        color = TempleGold,
                        fontWeight = FontWeight.SemiBold,
                        modifier = Modifier.padding(horizontal = 14.dp, vertical = 6.dp)
                    )
                }

                Spacer(modifier = Modifier.size(48.dp)) // Balance symmetry
            }

            Spacer(modifier = Modifier.height(16.dp))

            // 280x280dp Deity Artwork with Glowing Golden Halo
            Box(
                modifier = Modifier
                    .size(280.dp)
                    .clip(RoundedCornerShape(28.dp))
                    .background(Color(0xFF22170F))
                    .border(2.dp, RichGold.copy(alpha = 0.6f), RoundedCornerShape(28.dp)),
                contentAlignment = Alignment.Center
            ) {
                Image(
                    painter = painterResource(id = track.thumbnailResId),
                    contentDescription = track.titleEnglish,
                    contentScale = ContentScale.Crop,
                    modifier = Modifier.fillMaxSize()
                )
            }

            Spacer(modifier = Modifier.height(20.dp))

            // Title & Subtitle Metadata
            Column(
                horizontalAlignment = Alignment.CenterHorizontally,
                modifier = Modifier.fillMaxWidth()
            ) {
                Text(
                    text = track.titleTelugu,
                    style = MaterialTheme.typography.headlineMedium,
                    color = TempleGold,
                    fontWeight = FontWeight.Bold,
                    fontSize = 24.sp,
                    textAlign = TextAlign.Center,
                    maxLines = 2,
                    overflow = TextOverflow.Ellipsis
                )
                Text(
                    text = track.titleEnglish,
                    style = MaterialTheme.typography.bodyLarge,
                    color = WarmIvory.copy(alpha = 0.8f),
                    textAlign = TextAlign.Center,
                    modifier = Modifier.padding(top = 4.dp)
                )
            }

            Spacer(modifier = Modifier.height(16.dp))

            // Japam Repetition HUD & Mode Selector
            JapamSelectorSection(
                currentMode = japamState.mode,
                currentIteration = japamState.currentIteration,
                totalTarget = japamState.totalTarget,
                onSelectMode = { viewModel.setJapamMode(it) }
            )

            Spacer(modifier = Modifier.height(16.dp))

            // Tactile High-Contrast Scrubber Slider
            val maxSlider = if (durationMs > 0) durationMs.toFloat() else 1f
            val currentSlider = currentPositionMs.toFloat().coerceIn(0f, maxSlider)

            Column(modifier = Modifier.fillMaxWidth()) {
                Slider(
                    value = currentSlider,
                    onValueChange = { newValue ->
                        viewModel.seekTo(newValue.toLong())
                    },
                    valueRange = 0f..maxSlider,
                    colors = SliderDefaults.colors(
                        thumbColor = SacredSaffron,
                        activeTrackColor = SacredSaffron,
                        inactiveTrackColor = Color(0xFF3B3835)
                    ),
                    modifier = Modifier.fillMaxWidth()
                )

                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.SpaceBetween
                ) {
                    Text(
                        text = formatTime(currentPositionMs),
                        style = MaterialTheme.typography.labelSmall,
                        color = WarmIvory.copy(alpha = 0.7f)
                    )
                    Text(
                        text = formatTime(durationMs),
                        style = MaterialTheme.typography.labelSmall,
                        color = WarmIvory.copy(alpha = 0.7f)
                    )
                }
            }

            Spacer(modifier = Modifier.height(16.dp))

            // Jumbo Control Cluster (10s Rewind, 72dp Jumbo Play/Pause, 10s Forward)
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceEvenly,
                verticalAlignment = Alignment.CenterVertically
            ) {
                // 10s Rewind Button
                IconButton(
                    onClick = { viewModel.seekBackward(10000L) },
                    modifier = Modifier
                        .size(54.dp)
                        .clip(CircleShape)
                        .background(SurfaceContainer)
                        .border(1.dp, RichGold.copy(alpha = 0.3f), CircleShape)
                ) {
                    Icon(
                        imageVector = Icons.Default.Replay10,
                        contentDescription = "Rewind 10 seconds",
                        tint = WarmIvory,
                        modifier = Modifier.size(28.dp)
                    )
                }

                // Jumbo 72dp Play/Pause Button
                Box(
                    modifier = Modifier
                        .size(76.dp)
                        .clip(CircleShape)
                        .background(SaffronGoldGradient)
                        .border(2.dp, TempleGold, CircleShape)
                        .clickable { viewModel.playPause() },
                    contentAlignment = Alignment.Center
                ) {
                    Icon(
                        imageVector = if (isPlaying) Icons.Default.Pause else Icons.Default.PlayArrow,
                        contentDescription = if (isPlaying) "Pause" else "Play",
                        tint = Color(0xFF1E1000),
                        modifier = Modifier.size(40.dp)
                    )
                }

                // 10s Forward Button
                IconButton(
                    onClick = { viewModel.seekForward(10000L) },
                    modifier = Modifier
                        .size(54.dp)
                        .clip(CircleShape)
                        .background(SurfaceContainer)
                        .border(1.dp, RichGold.copy(alpha = 0.3f), CircleShape)
                ) {
                    Icon(
                        imageVector = Icons.Default.Forward10,
                        contentDescription = "Forward 10 seconds",
                        tint = WarmIvory,
                        modifier = Modifier.size(28.dp)
                    )
                }
            }

            Spacer(modifier = Modifier.height(20.dp))

            // Bottom Lyrics Sheet Trigger Pill
            Surface(
                modifier = Modifier
                    .clip(RoundedCornerShape(24.dp))
                    .clickable { onOpenLyrics() },
                color = SurfaceContainer,
                border = androidx.compose.foundation.BorderStroke(1.dp, RichGold.copy(alpha = 0.4f)),
                shape = RoundedCornerShape(24.dp)
            ) {
                Row(
                    modifier = Modifier.padding(horizontal = 20.dp, vertical = 10.dp),
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Icon(
                        imageVector = Icons.Default.KeyboardArrowUp,
                        contentDescription = "View Lyrics",
                        tint = TempleGold,
                        modifier = Modifier.size(20.dp)
                    )
                    Spacer(modifier = Modifier.width(8.dp))
                    Text(
                        text = "సాహిత్యం చూడండి • View Lyrics",
                        style = MaterialTheme.typography.labelLarge,
                        color = TempleGold,
                        fontWeight = FontWeight.Bold
                    )
                }
            }
        }
    }
}

@Composable
private fun JapamSelectorSection(
    currentMode: JapamMode,
    currentIteration: Int,
    totalTarget: Int,
    onSelectMode: (JapamMode) -> Unit
) {
    Column(
        horizontalAlignment = Alignment.CenterHorizontally,
        modifier = Modifier
            .fillMaxWidth()
            .clip(RoundedCornerShape(18.dp))
            .background(SurfaceContainer.copy(alpha = 0.6f))
            .border(1.dp, RichGold.copy(alpha = 0.2f), RoundedCornerShape(18.dp))
            .padding(12.dp)
    ) {
        // HUD Status Banner
        Row(
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.Center
        ) {
            Icon(
                imageVector = Icons.Default.Repeat,
                contentDescription = null,
                tint = TempleGold,
                modifier = Modifier.size(16.dp)
            )
            Spacer(modifier = Modifier.width(6.dp))
            Text(
                text = if (currentMode == JapamMode.INFINITE) {
                    "జపం: $currentIteration / ∞ (నిరంతర జపం)"
                } else {
                    "జపం: $currentIteration / $totalTarget ఆవర్తనాలు"
                },
                style = MaterialTheme.typography.titleSmall,
                color = TempleGold,
                fontWeight = FontWeight.Bold
            )
        }

        Spacer(modifier = Modifier.height(10.dp))

        // Preset Selector Pills (1x, 11x, 21x, 108x, ∞)
        Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.SpaceEvenly
        ) {
            JapamMode.entries.forEach { mode ->
                val isSelected = mode == currentMode
                Surface(
                    modifier = Modifier
                        .clip(RoundedCornerShape(16.dp))
                        .clickable { onSelectMode(mode) },
                    color = if (isSelected) SacredSaffron else DevotionalSurface,
                    border = androidx.compose.foundation.BorderStroke(
                        1.dp,
                        if (isSelected) TempleGold else RichGold.copy(alpha = 0.2f)
                    ),
                    shape = RoundedCornerShape(16.dp)
                ) {
                    Text(
                        text = mode.label,
                        style = MaterialTheme.typography.labelSmall,
                        color = if (isSelected) Color(0xFF1E1000) else WarmIvory,
                        fontWeight = if (isSelected) FontWeight.Bold else FontWeight.Medium,
                        modifier = Modifier.padding(horizontal = 12.dp, vertical = 6.dp)
                    )
                }
            }
        }
    }
}

private fun formatTime(ms: Long): String {
    val totalSeconds = (ms / 1000).coerceAtLeast(0)
    val minutes = totalSeconds / 60
    val seconds = totalSeconds % 60
    return String.format("%02d:%02d", minutes, seconds)
}
