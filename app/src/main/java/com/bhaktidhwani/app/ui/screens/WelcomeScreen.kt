package com.bhaktidhwani.app.ui.screens

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
import androidx.compose.material.icons.filled.CheckCircle
import androidx.compose.material.icons.filled.CloudOff
import androidx.compose.material.icons.filled.GraphicEq
import androidx.compose.material.icons.filled.Repeat
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
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.airbnb.lottie.compose.LottieAnimation
import com.airbnb.lottie.compose.LottieCompositionSpec
import com.airbnb.lottie.compose.LottieConstants
import com.airbnb.lottie.compose.rememberLottieComposition
import com.bhaktidhwani.app.ui.theme.GoldenAuraGradient
import com.bhaktidhwani.app.ui.theme.RichGold
import com.bhaktidhwani.app.ui.theme.SacredSaffron
import com.bhaktidhwani.app.ui.theme.SaffronGoldGradient
import com.bhaktidhwani.app.ui.theme.SanctumFloor
import com.bhaktidhwani.app.ui.theme.SurfaceContainer
import com.bhaktidhwani.app.ui.theme.TempleGold
import com.bhaktidhwani.app.ui.theme.WarmIvory

/**
 * Onboarding/Welcome screen featuring the sacred Namaste Lottie animation,
 * bilingual headline, offline verification badge, and elder-friendly CTA.
 */
@Composable
fun WelcomeScreen(
    onGetStarted: () -> Unit
) {
    val composition by rememberLottieComposition(
        LottieCompositionSpec.Asset("anim/namaste_anim.json")
    )
    val scrollState = rememberScrollState()

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
                    .padding(top = 40.dp, bottom = 100.dp),
                horizontalAlignment = Alignment.CenterHorizontally,
                verticalArrangement = Arrangement.Center
            ) {
                // 100% Offline Sanctum Badge
                Row(
                    modifier = Modifier
                        .clip(RoundedCornerShape(50))
                        .background(SurfaceContainer)
                        .border(1.dp, RichGold.copy(alpha = 0.4f), RoundedCornerShape(50))
                        .padding(horizontal = 16.dp, vertical = 8.dp),
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
                        color = WarmIvory
                    )
                }

                Spacer(modifier = Modifier.height(32.dp))

                // Lottie Sacred Namaste Animation Container
                Box(
                    modifier = Modifier
                        .size(180.dp)
                        .clip(CircleShape)
                        .background(Color(0xFF2A1C10))
                        .border(2.dp, RichGold, CircleShape),
                    contentAlignment = Alignment.Center
                ) {
                    LottieAnimation(
                        composition = composition,
                        iterations = LottieConstants.IterateForever,
                        modifier = Modifier.size(150.dp)
                    )
                }

                Spacer(modifier = Modifier.height(28.dp))

                // Bilingual Welcome Headline
                Text(
                    text = "భక్తి ధ్వని",
                    style = MaterialTheme.typography.headlineLarge,
                    color = TempleGold,
                    fontWeight = FontWeight.Bold,
                    fontSize = 34.sp,
                    textAlign = TextAlign.Center
                )

                Text(
                    text = "Bhakti Dhwani • Devotional Chants",
                    style = MaterialTheme.typography.titleMedium,
                    color = WarmIvory.copy(alpha = 0.9f),
                    textAlign = TextAlign.Center,
                    modifier = Modifier.padding(top = 4.dp)
                )

                Text(
                    text = "పవిత్రమైన స్తోత్రాలు, ప్రశాంతమైన జపం మరియు సహజమైన సాహిత్యంతో మీ ఆధ్యాత్మిక ప్రయాణాన్ని ప్రారంభించండి.",
                    style = MaterialTheme.typography.bodyLarge,
                    color = WarmIvory.copy(alpha = 0.75f),
                    textAlign = TextAlign.Center,
                    lineHeight = 26.sp,
                    modifier = Modifier.padding(top = 12.dp, start = 8.dp, end = 8.dp)
                )

                Spacer(modifier = Modifier.height(32.dp))

                // Feature Highlights for Elders
                FeatureBadge(
                    icon = Icons.Default.Repeat,
                    titleTelugu = "నిరంతర జపం (Japam Chanting)",
                    description = "11x, 21x, 108x లేదా నిరంతర ఆవర్తనాలతో ప్రార్థన."
                )

                Spacer(modifier = Modifier.height(12.dp))

                FeatureBadge(
                    icon = Icons.Default.GraphicEq,
                    titleTelugu = "సమకాలీకరించిన సాహిత్యం (Live Lyrics)",
                    description = "స్పష్టమైన తెలుగు మరియు ఇంగ్లీష్ పెద్ద అక్షరాల లిపి."
                )

                Spacer(modifier = Modifier.height(12.dp))

                FeatureBadge(
                    icon = Icons.Default.CheckCircle,
                    titleTelugu = "సహజమైన సౌకర్యం (Simple & Clear)",
                    description = "పెద్ద బటన్లు, ప్రకటనలు లేవు, సులభమైన వాడకం."
                )
            }

            // Fixed Bottom CTA Button (64dp height for elderly convenience)
            Box(
                modifier = Modifier
                    .fillMaxWidth()
                    .align(Alignment.BottomCenter)
                    .padding(bottom = 24.dp)
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
                            color = Color(0xFF1E1000),
                            fontWeight = FontWeight.Bold,
                            fontSize = 18.sp
                        )
                        Spacer(modifier = Modifier.width(10.dp))
                        Icon(
                            imageVector = Icons.AutoMirrored.Filled.ArrowForward,
                            contentDescription = "Proceed",
                            tint = Color(0xFF1E1000)
                        )
                    }
                }
            }
        }
    }
}

@Composable
private fun FeatureBadge(
    icon: ImageVector,
    titleTelugu: String,
    description: String
) {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .clip(RoundedCornerShape(16.dp))
            .background(SurfaceContainer.copy(alpha = 0.7f))
            .border(1.dp, RichGold.copy(alpha = 0.15f), RoundedCornerShape(16.dp))
            .padding(14.dp),
        verticalAlignment = Alignment.CenterVertically
    ) {
        Box(
            modifier = Modifier
                .size(42.dp)
                .clip(CircleShape)
                .background(SacredSaffron.copy(alpha = 0.2f)),
            contentAlignment = Alignment.Center
        ) {
            Icon(
                imageVector = icon,
                contentDescription = null,
                tint = TempleGold,
                modifier = Modifier.size(22.dp)
            )
        }
        Spacer(modifier = Modifier.width(14.dp))
        Column {
            Text(
                text = titleTelugu,
                style = MaterialTheme.typography.titleSmall,
                color = WarmIvory,
                fontWeight = FontWeight.SemiBold
            )
            Text(
                text = description,
                style = MaterialTheme.typography.bodySmall,
                color = WarmIvory.copy(alpha = 0.65f),
                modifier = Modifier.padding(top = 2.dp)
            )
        }
    }
}
