package com.bhaktidhwani.app.ui.screens

import androidx.compose.animation.core.RepeatMode
import androidx.compose.animation.core.animateFloat
import androidx.compose.animation.core.infiniteRepeatable
import androidx.compose.animation.core.rememberInfiniteTransition
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.border
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
import androidx.compose.material.icons.automirrored.filled.ArrowForward
import androidx.compose.material.icons.filled.CloudOff
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.draw.scale
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.bhaktidhwani.app.R
import com.bhaktidhwani.app.ui.theme.GoldenAuraGradient
import com.bhaktidhwani.app.ui.theme.RichGold
import com.bhaktidhwani.app.ui.theme.SacredSaffron
import com.bhaktidhwani.app.ui.theme.SaffronGoldGradient
import com.bhaktidhwani.app.ui.theme.SanctumFloor
import com.bhaktidhwani.app.ui.theme.SurfaceContainer
import com.bhaktidhwani.app.ui.theme.TempleGold
import com.bhaktidhwani.app.ui.theme.WarmIvory

/**
 * Clean, serene Welcome/Onboarding screen for Devotional Chants.
 * Features an authentic brass Diya emblem enveloped by a soft breathing golden halo,
 * sacred Telugu greeting, and a prominent 60dp "Get Started" CTA button.
 */
@Composable
fun WelcomeScreen(
    onGetStarted: () -> Unit
) {
    val scrollState = rememberScrollState()

    // Smooth continuous aura breathing animation
    val infiniteTransition = rememberInfiniteTransition(label = "SacredAuraBreathing")
    val pulseScale by infiniteTransition.animateFloat(
        initialValue = 0.94f,
        targetValue = 1.06f,
        animationSpec = infiniteRepeatable(
            animation = tween(durationMillis = 2800),
            repeatMode = RepeatMode.Reverse
        ),
        label = "pulseScale"
    )
    val auraAlpha by infiniteTransition.animateFloat(
        initialValue = 0.35f,
        targetValue = 0.75f,
        animationSpec = infiniteRepeatable(
            animation = tween(durationMillis = 2800),
            repeatMode = RepeatMode.Reverse
        ),
        label = "auraAlpha"
    )

    Surface(
        modifier = Modifier.fillMaxSize(),
        color = SanctumFloor
    ) {
        Box(
            modifier = Modifier
                .fillMaxSize()
                .background(GoldenAuraGradient)
                .padding(horizontal = 24.dp)
        ) {
            Column(
                modifier = Modifier
                    .fillMaxSize()
                    .verticalScroll(scrollState)
                    .padding(top = 48.dp, bottom = 100.dp),
                horizontalAlignment = Alignment.CenterHorizontally,
                verticalArrangement = Arrangement.Center
            ) {
                // 100% Offline Sanctum Badge
                Row(
                    modifier = Modifier
                        .clip(RoundedCornerShape(50))
                        .background(SurfaceContainer)
                        .border(1.dp, RichGold.copy(alpha = 0.35f), RoundedCornerShape(50))
                        .padding(horizontal = 18.dp, vertical = 8.dp),
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Icon(
                        imageVector = Icons.Default.CloudOff,
                        contentDescription = "Offline Badge",
                        tint = TempleGold,
                        modifier = Modifier.size(18.dp)
                    )
                    Spacer(modifier = Modifier.width(8.dp))
                    Text(
                        text = "100% ఆఫ్లైన్ • Zero Internet Needed",
                        style = MaterialTheme.typography.labelMedium,
                        color = WarmIvory,
                        fontWeight = FontWeight.Medium
                    )
                }

                Spacer(modifier = Modifier.height(44.dp))

                // === ELEGANT BREATHING GOLDEN HALO & TRADITIONAL DIYA EMBLEM ===
                Box(
                    modifier = Modifier.size(230.dp),
                    contentAlignment = Alignment.Center
                ) {
                    // Outermost Soft Ambient Radiant Halo
                    Box(
                        modifier = Modifier
                            .size(220.dp)
                            .scale(pulseScale)
                            .clip(CircleShape)
                            .background(
                                Brush.radialGradient(
                                    colors = listOf(
                                        TempleGold.copy(alpha = 0.22f * auraAlpha),
                                        SacredSaffron.copy(alpha = 0.10f * auraAlpha),
                                        Color.Transparent
                                    )
                                )
                            )
                    )

                    // Secondary Concentric Gold Aura Ring
                    Box(
                        modifier = Modifier
                            .size(180.dp)
                            .clip(CircleShape)
                            .border(
                                width = 1.5.dp,
                                color = TempleGold.copy(alpha = 0.40f * auraAlpha),
                                shape = CircleShape
                            )
                    )

                    // Inner Sanctum Shrine Plinth (Deep Temple Dark)
                    Box(
                        modifier = Modifier
                            .size(144.dp)
                            .clip(CircleShape)
                            .background(Color(0xFF140A04))
                            .border(
                                width = 2.dp,
                                brush = Brush.linearGradient(
                                    colors = listOf(RichGold, SacredSaffron.copy(alpha = 0.6f))
                                ),
                                shape = CircleShape
                            ),
                        contentAlignment = Alignment.Center
                    ) {
                        // Refined Traditional Brass Diya Emblem (No raster watermarks)
                        Image(
                            painter = painterResource(id = R.drawable.ic_welcome_diya),
                            contentDescription = "Sacred Deepam",
                            modifier = Modifier
                                .size(96.dp)
                                .padding(6.dp)
                        )
                    }
                }

                Spacer(modifier = Modifier.height(36.dp))

                // Sacred Title & Devotional Header
                Text(
                    text = "భక్తి గీతాలు • Devotional Chants",
                    style = MaterialTheme.typography.headlineMedium,
                    color = TempleGold,
                    fontWeight = FontWeight.Bold,
                    fontSize = 26.sp,
                    textAlign = TextAlign.Center
                )

                Spacer(modifier = Modifier.height(10.dp))

                Text(
                    text = "పవిత్రమైన స్తోత్రాలు మరియు ప్రశాంతమైన జపం",
                    style = MaterialTheme.typography.bodyLarge,
                    color = WarmIvory.copy(alpha = 0.85f),
                    textAlign = TextAlign.Center,
                    lineHeight = 24.sp,
                    modifier = Modifier.padding(horizontal = 16.dp)
                )

                Text(
                    text = "Sacred Stotras, Chants & Peaceful Japam Meditation",
                    style = MaterialTheme.typography.bodyMedium,
                    color = WarmIvory.copy(alpha = 0.6f),
                    textAlign = TextAlign.Center,
                    modifier = Modifier.padding(top = 6.dp)
                )

                Spacer(modifier = Modifier.height(48.dp))
            }

            // Fixed Bottom CTA Button (60dp height for elderly convenience)
            Box(
                modifier = Modifier
                    .fillMaxWidth()
                    .align(Alignment.BottomCenter)
                    .padding(bottom = 28.dp)
            ) {
                Button(
                    onClick = onGetStarted,
                    modifier = Modifier
                        .fillMaxWidth()
                        .height(60.dp)
                        .clip(RoundedCornerShape(30.dp))
                        .background(SaffronGoldGradient),
                    colors = ButtonDefaults.buttonColors(
                        containerColor = Color.Transparent
                    ),
                    elevation = ButtonDefaults.buttonElevation(defaultElevation = 6.dp)
                ) {
                    Row(
                        verticalAlignment = Alignment.CenterVertically,
                        horizontalArrangement = Arrangement.Center
                    ) {
                        Text(
                            text = "ప్రారంభించండి • Get Started",
                            style = MaterialTheme.typography.titleMedium,
                            color = Color(0xFF1A0A00),
                            fontWeight = FontWeight.Bold,
                            fontSize = 18.sp
                        )
                        Spacer(modifier = Modifier.width(10.dp))
                        Icon(
                            imageVector = Icons.AutoMirrored.Filled.ArrowForward,
                            contentDescription = "Proceed",
                            tint = Color(0xFF1A0A00)
                        )
                    }
                }
            }
        }
    }
}
