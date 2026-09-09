package com.bhaktidhwani.app.ui.screens

import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.CheckCircle
import androidx.compose.material.icons.filled.Equalizer
import androidx.compose.material.icons.filled.PlayArrow
import androidx.compose.material.icons.filled.Search
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
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
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.bhaktidhwani.app.R
import com.bhaktidhwani.app.data.model.Track
import com.bhaktidhwani.app.ui.components.MiniPlayerBar
import com.bhaktidhwani.app.ui.theme.DevotionalSurface
import com.bhaktidhwani.app.ui.theme.RichGold
import com.bhaktidhwani.app.ui.theme.SacredSaffron
import com.bhaktidhwani.app.ui.theme.SaffronGoldGradient
import com.bhaktidhwani.app.ui.theme.SanctumCardGradient
import com.bhaktidhwani.app.ui.theme.SanctumFloor
import com.bhaktidhwani.app.ui.theme.SurfaceContainer
import com.bhaktidhwani.app.ui.theme.TempleGold
import com.bhaktidhwani.app.ui.theme.WarmIvory
import com.bhaktidhwani.app.ui.viewmodel.MainViewModel

/**
 * Devotional Library screen offering deity filtering, quick morning chant cards,
 * Spotify-style elder-accessible track listings, and the sticky Mini-Player bar.
 */
@Composable
fun LibraryScreen(
    viewModel: MainViewModel,
    onOpenPlayer: () -> Unit
) {
    val tracks by viewModel.tracks.collectAsState()
    val selectedCategory by viewModel.selectedCategory.collectAsState()
    val activeTrack by viewModel.activeTrack.collectAsState()
    val isPlaying by viewModel.isPlaying.collectAsState()
    val currentPositionMs by viewModel.currentPositionMs.collectAsState()
    val durationMs by viewModel.durationMs.collectAsState()

    Scaffold(
        containerColor = SanctumFloor,
        bottomBar = {
            if (activeTrack != null) {
                MiniPlayerBar(
                    track = activeTrack!!,
                    isPlaying = isPlaying,
                    currentPositionMs = currentPositionMs,
                    durationMs = durationMs,
                    onPlayPause = { viewModel.playPause() },
                    onExpandPlayer = onOpenPlayer
                )
            }
        }
    ) { innerPadding ->
        LazyColumn(
            modifier = Modifier
                .fillMaxSize()
                .padding(innerPadding),
            contentPadding = PaddingValues(bottom = 24.dp)
        ) {
            // Header Top Bar
            item {
                LibraryHeader()
            }

            // Sticky Deity Filter Chips
            item {
                DeityFilterRow(
                    categories = viewModel.categories,
                    selectedCategory = selectedCategory,
                    onSelectCategory = { viewModel.selectCategory(it) }
                )
            }

            // Morning Chants Quick-Access 2x2 Grid
            if (selectedCategory == "All") {
                item {
                    Text(
                        text = "ఉదయకాల ప్రార్థనలు • Morning Chants",
                        style = MaterialTheme.typography.titleMedium,
                        color = TempleGold,
                        fontWeight = FontWeight.Bold,
                        fontSize = 18.sp,
                        modifier = Modifier.padding(horizontal = 20.dp, vertical = 12.dp)
                    )
                }

                item {
                    MorningChantsGrid(
                        quickPicks = viewModel.quickPicks,
                        activeTrackId = activeTrack?.id,
                        isPlaying = isPlaying,
                        onTrackClick = { track ->
                            viewModel.playTrack(track)
                            onOpenPlayer()
                        }
                    )
                }
            }

            // All Stotras Section Header
            item {
                Row(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(horizontal = 20.dp, vertical = 16.dp),
                    horizontalArrangement = Arrangement.SpaceBetween,
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Text(
                        text = if (selectedCategory == "All") "అన్ని స్తోత్రాలు • All Stotras" else "$selectedCategory స్తోత్రాలు",
                        style = MaterialTheme.typography.titleLarge,
                        color = WarmIvory,
                        fontWeight = FontWeight.Bold
                    )
                    Text(
                        text = "${tracks.size} స్తోత్రాలు",
                        style = MaterialTheme.typography.bodySmall,
                        color = SandalwoodAsh()
                    )
                }
            }

            // Vertical Track List
            items(tracks, key = { it.id }) { track ->
                val isCurrent = activeTrack?.id == track.id
                TrackListItem(
                    track = track,
                    isCurrent = isCurrent,
                    isPlaying = isCurrent && isPlaying,
                    onTrackClick = {
                        viewModel.playTrack(track)
                        onOpenPlayer()
                    },
                    onPlayClick = {
                        if (isCurrent) {
                            viewModel.playPause()
                        } else {
                            viewModel.playTrack(track)
                        }
                    }
                )
            }
        }
    }
}

@Composable
private fun LibraryHeader() {
    Column(
        modifier = Modifier
            .fillMaxWidth()
            .padding(horizontal = 20.dp, vertical = 16.dp)
    ) {
        Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.SpaceBetween,
            verticalAlignment = Alignment.CenterVertically
        ) {
            Row(verticalAlignment = Alignment.CenterVertically) {
                Image(
                    painter = painterResource(id = R.drawable.ic_namaste),
                    contentDescription = "Namaste Emblem",
                    modifier = Modifier
                        .size(40.dp)
                        .clip(CircleShape)
                        .background(SurfaceContainer)
                        .padding(4.dp)
                )
                Spacer(modifier = Modifier.width(12.dp))
                Column {
                    Text(
                        text = "భక్తి గీతాలు",
                        style = MaterialTheme.typography.titleLarge,
                        color = TempleGold,
                        fontWeight = FontWeight.Bold
                    )
                    Text(
                        text = "Devotional Chants Sanctum",
                        style = MaterialTheme.typography.bodySmall,
                        color = WarmIvory.copy(alpha = 0.7f)
                    )
                }
            }

            // Offline Verified Pill
            Row(
                modifier = Modifier
                    .clip(RoundedCornerShape(20.dp))
                    .background(Color(0xFF1B2E1E))
                    .border(1.dp, Color(0xFF4CAF50), RoundedCornerShape(20.dp))
                    .padding(horizontal = 10.dp, vertical = 5.dp),
                verticalAlignment = Alignment.CenterVertically
            ) {
                Icon(
                    imageVector = Icons.Default.CheckCircle,
                    contentDescription = "Offline Ready",
                    tint = Color(0xFF4CAF50),
                    modifier = Modifier.size(14.dp)
                )
                Spacer(modifier = Modifier.width(6.dp))
                Text(
                    text = "ఆఫ్లైన్ సిద్ధం",
                    style = MaterialTheme.typography.labelSmall,
                    color = Color(0xFFE8F5E9),
                    fontWeight = FontWeight.SemiBold
                )
            }
        }
    }
}

@Composable
private fun DeityFilterRow(
    categories: List<String>,
    selectedCategory: String,
    onSelectCategory: (String) -> Unit
) {
    LazyRow(
        modifier = Modifier.fillMaxWidth(),
        contentPadding = PaddingValues(horizontal = 20.dp, vertical = 4.dp),
        horizontalArrangement = Arrangement.spacedBy(10.dp)
    ) {
        items(categories) { category ->
            val isSelected = category == selectedCategory
            Surface(
                modifier = Modifier
                    .clip(RoundedCornerShape(24.dp))
                    .clickable { onSelectCategory(category) },
                color = if (isSelected) SacredSaffron else DevotionalSurface,
                border = androidx.compose.foundation.BorderStroke(
                    1.dp,
                    if (isSelected) TempleGold else RichGold.copy(alpha = 0.25f)
                ),
                shape = RoundedCornerShape(24.dp)
            ) {
                Text(
                    text = category,
                    style = MaterialTheme.typography.labelLarge,
                    color = if (isSelected) Color(0xFF1E1000) else WarmIvory,
                    fontWeight = if (isSelected) FontWeight.Bold else FontWeight.Medium,
                    modifier = Modifier.padding(horizontal = 18.dp, vertical = 10.dp)
                )
            }
        }
    }
}

@Composable
private fun MorningChantsGrid(
    quickPicks: List<Track>,
    activeTrackId: String?,
    isPlaying: Boolean,
    onTrackClick: (Track) -> Unit
) {
    Column(
        modifier = Modifier
            .fillMaxWidth()
            .padding(horizontal = 20.dp),
        verticalArrangement = Arrangement.spacedBy(12.dp)
    ) {
        val chunked = quickPicks.chunked(2)
        for (row in chunked) {
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.spacedBy(12.dp)
            ) {
                for (track in row) {
                    val isCurrent = activeTrackId == track.id
                    QuickPickCard(
                        track = track,
                        isCurrent = isCurrent,
                        isPlaying = isCurrent && isPlaying,
                        onClick = { onTrackClick(track) },
                        modifier = Modifier.weight(1f)
                    )
                }
                if (row.size == 1) {
                    Spacer(modifier = Modifier.weight(1f))
                }
            }
        }
    }
}

@Composable
private fun QuickPickCard(
    track: Track,
    isCurrent: Boolean,
    isPlaying: Boolean,
    onClick: () -> Unit,
    modifier: Modifier = Modifier
) {
    Box(
        modifier = modifier
            .height(84.dp)
            .clip(RoundedCornerShape(14.dp))
            .background(SanctumCardGradient)
            .border(
                1.dp,
                if (isCurrent) SacredSaffron else RichGold.copy(alpha = 0.2f),
                RoundedCornerShape(14.dp)
            )
            .clickable { onClick() }
            .padding(8.dp)
    ) {
        Row(
            modifier = Modifier.fillMaxSize(),
            verticalAlignment = Alignment.CenterVertically
        ) {
            Image(
                painter = painterResource(id = track.thumbnailResId),
                contentDescription = track.titleEnglish,
                contentScale = ContentScale.Crop,
                modifier = Modifier
                    .size(68.dp)
                    .clip(RoundedCornerShape(10.dp))
            )
            Spacer(modifier = Modifier.width(10.dp))
            Column(
                modifier = Modifier.weight(1f),
                verticalArrangement = Arrangement.Center
            ) {
                Text(
                    text = track.titleTelugu,
                    style = MaterialTheme.typography.titleSmall,
                    color = if (isCurrent) TempleGold else WarmIvory,
                    fontWeight = FontWeight.Bold,
                    fontSize = 13.sp,
                    maxLines = 2,
                    overflow = TextOverflow.Ellipsis
                )
                Text(
                    text = track.deityTelugu,
                    style = MaterialTheme.typography.bodySmall,
                    color = SandalwoodAsh(),
                    fontSize = 11.sp,
                    maxLines = 1
                )
            }
        }
    }
}

@Composable
private fun TrackListItem(
    track: Track,
    isCurrent: Boolean,
    isPlaying: Boolean,
    onTrackClick: () -> Unit,
    onPlayClick: () -> Unit
) {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .padding(horizontal = 20.dp, vertical = 6.dp)
            .clip(RoundedCornerShape(16.dp))
            .background(if (isCurrent) SurfaceContainer else DevotionalSurface)
            .border(
                1.dp,
                if (isCurrent) SacredSaffron.copy(alpha = 0.6f) else RichGold.copy(alpha = 0.15f),
                RoundedCornerShape(16.dp)
            )
            .clickable { onTrackClick() }
            .padding(12.dp),
        verticalAlignment = Alignment.CenterVertically
    ) {
        // 56x56dp Deity WebP Artwork
        Image(
            painter = painterResource(id = track.thumbnailResId),
            contentDescription = track.titleEnglish,
            contentScale = ContentScale.Crop,
            modifier = Modifier
                .size(56.dp)
                .clip(RoundedCornerShape(12.dp))
                .border(1.dp, RichGold.copy(alpha = 0.3f), RoundedCornerShape(12.dp))
        )

        Spacer(modifier = Modifier.width(14.dp))

        // Titles & Duration
        Column(
            modifier = Modifier.weight(1f)
        ) {
            Text(
                text = track.titleTelugu,
                style = MaterialTheme.typography.titleMedium,
                color = if (isCurrent) TempleGold else WarmIvory,
                fontWeight = FontWeight.Bold,
                fontSize = 17.sp,
                maxLines = 1,
                overflow = TextOverflow.Ellipsis
            )
            Text(
                text = "${track.deityTelugu} • ${track.titleEnglish}",
                style = MaterialTheme.typography.bodyMedium,
                color = WarmIvory.copy(alpha = 0.7f),
                fontSize = 13.sp,
                maxLines = 1,
                overflow = TextOverflow.Ellipsis,
                modifier = Modifier.padding(top = 2.dp)
            )
        }

        Spacer(modifier = Modifier.width(10.dp))

        // 48dp Instant Play / Pause Touch Target
        IconButton(
            onClick = onPlayClick,
            modifier = Modifier
                .size(48.dp)
                .clip(CircleShape)
                .background(if (isCurrent && isPlaying) SacredSaffron else SurfaceContainer)
                .border(
                    1.dp,
                    if (isCurrent) TempleGold else RichGold.copy(alpha = 0.3f),
                    CircleShape
                )
        ) {
            Icon(
                imageVector = if (isCurrent && isPlaying) Icons.Default.Equalizer else Icons.Default.PlayArrow,
                contentDescription = if (isPlaying) "Pause" else "Play",
                tint = if (isCurrent && isPlaying) Color(0xFF1E1000) else TempleGold,
                modifier = Modifier.size(24.dp)
            )
        }
    }
}

@Composable
private fun SandalwoodAsh(): Color = WarmIvory.copy(alpha = 0.6f)
