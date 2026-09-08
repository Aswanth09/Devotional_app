package com.bhaktidhwani.app.ui.screens

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
import androidx.compose.foundation.lazy.itemsIndexed
import androidx.compose.foundation.lazy.rememberLazyListState
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Close
import androidx.compose.material.icons.filled.Sync
import androidx.compose.material.icons.filled.Translate
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.bhaktidhwani.app.data.model.Stanza
import com.bhaktidhwani.app.ui.theme.DevotionalSurface
import com.bhaktidhwani.app.ui.theme.GoldenAuraGradient
import com.bhaktidhwani.app.ui.theme.RichGold
import com.bhaktidhwani.app.ui.theme.SacredSaffron
import com.bhaktidhwani.app.ui.theme.SanctumFloor
import com.bhaktidhwani.app.ui.theme.SurfaceContainer
import com.bhaktidhwani.app.ui.theme.TempleGold
import com.bhaktidhwani.app.ui.theme.WarmIvory
import com.bhaktidhwani.app.ui.viewmodel.MainViewModel
import com.bhaktidhwani.app.ui.viewmodel.ScriptMode

/**
 * Synced Lyrics Sheet with auto-scrolling LazyColumn, dual-script toggle (Telugu <-> English),
 * elder-friendly [A-] / [A+] font scalers, and glowing active stanza highlighting.
 */
@Composable
fun LyricsSheet(
    viewModel: MainViewModel,
    onClose: () -> Unit
) {
    val activeTrack by viewModel.activeTrack.collectAsState()
    val stanzas by viewModel.stanzas.collectAsState()
    val activeIndex by viewModel.activeStanzaIndex.collectAsState()
    val scriptMode by viewModel.scriptMode.collectAsState()
    val fontScaleDeltaSp by viewModel.fontScaleDeltaSp.collectAsState()
    val listState = rememberLazyListState()

    // Smoothly auto-scroll to the current active stanza
    LaunchedEffect(activeIndex) {
        if (activeIndex in stanzas.indices) {
            val targetScroll = (activeIndex - 1).coerceAtLeast(0)
            listState.animateScrollToItem(targetScroll)
        }
    }

    val track = activeTrack ?: return

    Surface(
        modifier = Modifier.fillMaxSize(),
        color = SanctumFloor
    ) {
        Column(
            modifier = Modifier
                .fillMaxSize()
                .background(GoldenAuraGradient)
                .padding(horizontal = 20.dp, vertical = 12.dp)
        ) {
            // Drag Handle Bar
            Box(
                modifier = Modifier
                    .width(44.dp)
                    .height(4.dp)
                    .clip(RoundedCornerShape(2.dp))
                    .background(RichGold.copy(alpha = 0.5f))
                    .align(Alignment.CenterHorizontally)
            )

            Spacer(modifier = Modifier.height(12.dp))

            // Header Row: Title, Stanza Counter, Close Button
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceBetween,
                verticalAlignment = Alignment.CenterVertically
            ) {
                Column(modifier = Modifier.weight(1f)) {
                    Text(
                        text = track.titleTelugu,
                        style = MaterialTheme.typography.titleLarge,
                        color = TempleGold,
                        fontWeight = FontWeight.Bold,
                        fontSize = 20.sp
                    )
                    val stanzaText = if (activeIndex in stanzas.indices) {
                        "శ్లోకం ${activeIndex + 1} / ${stanzas.size}"
                    } else {
                        "మొత్తం ${stanzas.size} శ్లోకాలు"
                    }
                    Text(
                        text = "$stanzaText • ${track.deityTelugu}",
                        style = MaterialTheme.typography.bodySmall,
                        color = WarmIvory.copy(alpha = 0.7f)
                    )
                }

                IconButton(
                    onClick = onClose,
                    modifier = Modifier
                        .size(44.dp)
                        .clip(CircleShape)
                        .background(SurfaceContainer)
                ) {
                    Icon(
                        imageVector = Icons.Default.Close,
                        contentDescription = "Close Lyrics",
                        tint = WarmIvory
                    )
                }
            }

            Spacer(modifier = Modifier.height(12.dp))

            // Control Bar: Script Switcher + Font Scalers + Sync Indicator
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .clip(RoundedCornerShape(16.dp))
                    .background(SurfaceContainer)
                    .border(1.dp, RichGold.copy(alpha = 0.25f), RoundedCornerShape(16.dp))
                    .padding(horizontal = 12.dp, vertical = 8.dp),
                horizontalArrangement = Arrangement.SpaceBetween,
                verticalAlignment = Alignment.CenterVertically
            ) {
                // Script Mode Toggle Pill (Telugu <-> English)
                Surface(
                    modifier = Modifier
                        .clip(RoundedCornerShape(14.dp))
                        .clickable { viewModel.toggleScript() },
                    color = DevotionalSurface,
                    border = androidx.compose.foundation.BorderStroke(1.dp, TempleGold.copy(alpha = 0.5f)),
                    shape = RoundedCornerShape(14.dp)
                ) {
                    Row(
                        modifier = Modifier.padding(horizontal = 12.dp, vertical = 6.dp),
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        Icon(
                            imageVector = Icons.Default.Translate,
                            contentDescription = "Switch Script",
                            tint = TempleGold,
                            modifier = Modifier.size(16.dp)
                        )
                        Spacer(modifier = Modifier.width(6.dp))
                        Text(
                            text = if (scriptMode == ScriptMode.TELUGU) "తెలుగు (Telugu)" else "English (లిపి)",
                            style = MaterialTheme.typography.labelSmall,
                            color = WarmIvory,
                            fontWeight = FontWeight.SemiBold
                        )
                    }
                }

                // Font Scaler Buttons ([A-] / [A+])
                Row(verticalAlignment = Alignment.CenterVertically) {
                    Surface(
                        modifier = Modifier
                            .clip(CircleShape)
                            .clickable { viewModel.decreaseFontSize() },
                        color = DevotionalSurface,
                        border = androidx.compose.foundation.BorderStroke(1.dp, RichGold.copy(alpha = 0.3f)),
                        shape = CircleShape
                    ) {
                        Text(
                            text = "A-",
                            style = MaterialTheme.typography.labelMedium,
                            color = WarmIvory,
                            fontWeight = FontWeight.Bold,
                            modifier = Modifier.padding(horizontal = 10.dp, vertical = 4.dp)
                        )
                    }

                    Spacer(modifier = Modifier.width(8.dp))

                    Surface(
                        modifier = Modifier
                            .clip(CircleShape)
                            .clickable { viewModel.increaseFontSize() },
                        color = DevotionalSurface,
                        border = androidx.compose.foundation.BorderStroke(1.dp, RichGold.copy(alpha = 0.3f)),
                        shape = CircleShape
                    ) {
                        Text(
                            text = "A+",
                            style = MaterialTheme.typography.labelMedium,
                            color = TempleGold,
                            fontWeight = FontWeight.Bold,
                            modifier = Modifier.padding(horizontal = 10.dp, vertical = 4.dp)
                        )
                    }
                }

                // Sync Status Chip
                Row(verticalAlignment = Alignment.CenterVertically) {
                    Icon(
                        imageVector = Icons.Default.Sync,
                        contentDescription = "In Sync",
                        tint = Color(0xFF4CAF50),
                        modifier = Modifier.size(14.dp)
                    )
                    Spacer(modifier = Modifier.width(4.dp))
                    Text(
                        text = "లైవ్",
                        style = MaterialTheme.typography.labelSmall,
                        color = Color(0xFF81C784),
                        fontWeight = FontWeight.Bold
                    )
                }
            }

            Spacer(modifier = Modifier.height(14.dp))

            // Auto-scrolling Stanza Stream
            if (stanzas.isEmpty()) {
                Box(
                    modifier = Modifier
                        .fillMaxSize()
                        .padding(bottom = 60.dp),
                    contentAlignment = Alignment.Center
                ) {
                    Text(
                        text = "సాహిత్యం అందుబాటులో ఉంది...",
                        style = MaterialTheme.typography.bodyLarge,
                        color = WarmIvory.copy(alpha = 0.5f)
                    )
                }
            } else {
                LazyColumn(
                    state = listState,
                    modifier = Modifier.fillMaxSize(),
                    contentPadding = PaddingValues(top = 8.dp, bottom = 48.dp),
                    verticalArrangement = Arrangement.spacedBy(14.dp)
                ) {
                    itemsIndexed(stanzas, key = { index, _ -> index }) { index, stanza ->
                        val isActive = index == activeIndex
                        StanzaItem(
                            stanza = stanza,
                            isActive = isActive,
                            scriptMode = scriptMode,
                            fontScaleDeltaSp = fontScaleDeltaSp,
                            onClick = {
                                viewModel.seekTo(stanza.startTimeMs)
                            }
                        )
                    }
                }
            }
        }
    }
}

@Composable
private fun StanzaItem(
    stanza: Stanza,
    isActive: Boolean,
    scriptMode: ScriptMode,
    fontScaleDeltaSp: Int,
    onClick: () -> Unit
) {
    val primaryText = if (scriptMode == ScriptMode.TELUGU) stanza.telugu else stanza.english
    val secondaryText = if (scriptMode == ScriptMode.TELUGU) stanza.english else stanza.telugu

    val primaryFontSize = (if (isActive) 21 else 18) + fontScaleDeltaSp
    val secondaryFontSize = (if (isActive) 15 else 13) + fontScaleDeltaSp

    Box(
        modifier = Modifier
            .fillMaxWidth()
            .clip(RoundedCornerShape(16.dp))
            .background(if (isActive) SurfaceContainer else Color.Transparent)
            .border(
                width = if (isActive) 1.5.dp else 0.dp,
                color = if (isActive) TempleGold else Color.Transparent,
                shape = RoundedCornerShape(16.dp)
            )
            .clickable { onClick() }
            .padding(14.dp)
    ) {
        Row(
            modifier = Modifier.fillMaxWidth(),
            verticalAlignment = Alignment.Top
        ) {
            // Saffron Left Indicator Bar for Active Verse
            if (isActive) {
                Box(
                    modifier = Modifier
                        .width(4.dp)
                        .height(36.dp)
                        .clip(RoundedCornerShape(2.dp))
                        .background(SacredSaffron)
                )
                Spacer(modifier = Modifier.width(12.dp))
            }

            Column(modifier = Modifier.weight(1f)) {
                // Verse Index Chip
                Text(
                    text = "శ్లోకం ${stanza.index}",
                    style = MaterialTheme.typography.labelSmall,
                    color = if (isActive) TempleGold else WarmIvory.copy(alpha = 0.4f),
                    fontWeight = FontWeight.Bold,
                    fontSize = 11.sp
                )

                Spacer(modifier = Modifier.height(4.dp))

                // Primary Verse Text
                Text(
                    text = primaryText,
                    style = MaterialTheme.typography.bodyLarge,
                    color = if (isActive) WarmIvory else WarmIvory.copy(alpha = 0.65f),
                    fontWeight = if (isActive) FontWeight.Bold else FontWeight.Normal,
                    fontSize = primaryFontSize.sp,
                    lineHeight = (primaryFontSize * 1.5).sp,
                    textAlign = TextAlign.Start
                )

                // Secondary Transliteration
                Spacer(modifier = Modifier.height(4.dp))
                Text(
                    text = secondaryText,
                    style = MaterialTheme.typography.bodyMedium,
                    color = if (isActive) TempleGold.copy(alpha = 0.85f) else WarmIvory.copy(alpha = 0.4f),
                    fontSize = secondaryFontSize.sp,
                    lineHeight = (secondaryFontSize * 1.4).sp,
                    textAlign = TextAlign.Start
                )
            }
        }
    }
}
