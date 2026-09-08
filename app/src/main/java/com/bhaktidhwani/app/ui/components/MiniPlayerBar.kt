package com.bhaktidhwani.app.ui.components

import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Pause
import androidx.compose.material.icons.filled.PlayArrow
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.LinearProgressIndicator
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.bhaktidhwani.app.data.model.Track
import com.bhaktidhwani.app.ui.theme.DevotionalSurface
import com.bhaktidhwani.app.ui.theme.RichGold
import com.bhaktidhwani.app.ui.theme.SacredSaffron
import com.bhaktidhwani.app.ui.theme.TempleGold
import com.bhaktidhwani.app.ui.theme.WarmIvory

/**
 * Sticky floating mini-player bar displayed above navigation
 * when an audio track is loaded.
 */
@Composable
fun MiniPlayerBar(
    track: Track,
    isPlaying: Boolean,
    currentPositionMs: Long,
    durationMs: Long,
    onPlayPause: () -> Unit,
    onExpandPlayer: () -> Unit,
    modifier: Modifier = Modifier
) {
    val progress = if (durationMs > 0) {
        (currentPositionMs.toFloat() / durationMs.toFloat()).coerceIn(0f, 1f)
    } else 0f

    Box(
        modifier = modifier
            .fillMaxWidth()
            .padding(horizontal = 12.dp, vertical = 6.dp)
            .clip(RoundedCornerShape(16.dp))
            .background(DevotionalSurface)
            .border(1.dp, RichGold.copy(alpha = 0.35f), RoundedCornerShape(16.dp))
            .clickable { onExpandPlayer() }
    ) {
        Column {
            // Top edge slim progress bar
            LinearProgressIndicator(
                progress = { progress },
                modifier = Modifier
                    .fillMaxWidth()
                    .height(3.dp),
                color = SacredSaffron,
                trackColor = Color(0xFF33302C)
            )

            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .height(64.dp)
                    .padding(horizontal = 12.dp),
                verticalAlignment = Alignment.CenterVertically
            ) {
                // 48x48dp Deity Artwork
                Image(
                    painter = painterResource(id = track.thumbnailResId),
                    contentDescription = track.titleEnglish,
                    contentScale = ContentScale.Crop,
                    modifier = Modifier
                        .size(48.dp)
                        .clip(RoundedCornerShape(10.dp))
                        .border(1.dp, TempleGold.copy(alpha = 0.5f), RoundedCornerShape(10.dp))
                )

                Spacer(modifier = Modifier.width(12.dp))

                // Track Titles
                Column(
                    modifier = Modifier.weight(1f)
                ) {
                    Text(
                        text = track.titleTelugu,
                        style = MaterialTheme.typography.titleSmall,
                        color = WarmIvory,
                        fontWeight = FontWeight.Bold,
                        fontSize = 15.sp,
                        maxLines = 1,
                        overflow = TextOverflow.Ellipsis
                    )
                    Text(
                        text = "${track.deityTelugu} • ${track.titleEnglish}",
                        style = MaterialTheme.typography.bodySmall,
                        color = TempleGold.copy(alpha = 0.8f),
                        fontSize = 12.sp,
                        maxLines = 1,
                        overflow = TextOverflow.Ellipsis
                    )
                }

                Spacer(modifier = Modifier.width(8.dp))

                // 48x48dp Play/Pause Button
                IconButton(
                    onClick = onPlayPause,
                    modifier = Modifier
                        .size(48.dp)
                        .clip(CircleShape)
                        .background(SacredSaffron)
                ) {
                    Icon(
                        imageVector = if (isPlaying) Icons.Default.Pause else Icons.Default.PlayArrow,
                        contentDescription = if (isPlaying) "Pause" else "Play",
                        tint = Color(0xFF1E1000),
                        modifier = Modifier.size(28.dp)
                    )
                }
            }
        }
    }
}
