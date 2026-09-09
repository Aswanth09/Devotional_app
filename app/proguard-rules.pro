# Devotional Chants Production Proguard Rules

# Keep Media3 classes, interfaces, and sessions
-keep class androidx.media3.** { *; }
-keep interface androidx.media3.** { *; }
-dontwarn androidx.media3.**

# Keep DataStore Preferences
-keep class androidx.datastore.** { *; }
-dontwarn androidx.datastore.**

# Keep Lottie Animation Runtime
-keep class com.airbnb.lottie.** { *; }
-dontwarn com.airbnb.lottie.**

# Keep Kotlin Coroutines
-keep class kotlinx.coroutines.** { *; }
-dontwarn kotlinx.coroutines.**

# Keep Data Models
-keep class com.bhaktidhwani.app.data.model.** { *; }

# Keep Devotional Audio Service and Receivers
-keep class com.bhaktidhwani.app.playback.** { *; }

# Keep Compose Runtime
-keep class androidx.compose.** { *; }
