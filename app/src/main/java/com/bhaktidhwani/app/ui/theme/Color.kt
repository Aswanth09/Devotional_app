package com.bhaktidhwani.app.ui.theme

import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color

// Brand Core Colors - Sacred Serenity Palette
val SacredSaffron = Color(0xFFFF6F00)
val DeepSaffron = Color(0xFFE65100)
val TempleGold = Color(0xFFFFD54F)
val RichGold = Color(0xFFEBC23E)
val WarmIvory = Color(0xFFFFF8E1)
val SoftIvory = Color(0xFFFFF8E7)
val SandalwoodAsh = Color(0xFFB0A89C)
val SmokedBrass = Color(0xFF2A2620)
val TempleMaroon = Color(0xFF3E000C)
val SanctumFloor = Color(0xFF121212)
val DevotionalSurface = Color(0xFF1A1A1A)
val SurfaceContainer = Color(0xFF201F1F)
val SurfaceContainerHigh = Color(0xFF2A2A2A)
val ActiveSanctuary = Color(0xFF22201D)
val OutlineMuted = Color(0xFF594136)
val PureWhite = Color(0xFFFFFFFF)

// Material 3 Dark Theme Colors
val M3Primary = Color(0xFFFFB691)
val M3OnPrimary = Color(0xFF552000)
val M3PrimaryContainer = Color(0xFFFF6F00)
val M3OnPrimaryContainer = Color(0xFFFFFFFF)
val M3Secondary = Color(0xFFEBC23E)
val M3OnSecondary = Color(0xFF3C2F00)
val M3SecondaryContainer = Color(0xFFB69200)
val M3OnSecondaryContainer = Color(0xFF3A2D00)
val M3Background = Color(0xFF121212)
val M3OnBackground = Color(0xFFFFF8E1)
val M3Surface = Color(0xFF181716)
val M3OnSurface = Color(0xFFFFF8E1)
val M3SurfaceVariant = Color(0xFF2A2620)
val M3OnSurfaceVariant = Color(0xFFE1BFB0)
val M3Outline = Color(0xFFA98A7C)
val M3OutlineVariant = Color(0xFF594136)

// Sacred Gradients
val SaffronGoldGradient = Brush.horizontalGradient(
    colors = listOf(SacredSaffron, RichGold)
)

val GoldenAuraGradient = Brush.verticalGradient(
    colors = listOf(Color(0xFF2A1C10), Color(0xFF121212))
)

val SanctumCardGradient = Brush.verticalGradient(
    colors = listOf(Color(0xFF25221F), Color(0xFF191816))
)
