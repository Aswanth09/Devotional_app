package com.bhaktidhwani.app.ui.navigation

import androidx.compose.runtime.Composable
import androidx.navigation.NavHostController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.bhaktidhwani.app.ui.screens.LibraryScreen
import com.bhaktidhwani.app.ui.screens.LyricsSheet
import com.bhaktidhwani.app.ui.screens.PlayerScreen
import com.bhaktidhwani.app.ui.screens.WelcomeScreen
import com.bhaktidhwani.app.ui.viewmodel.MainViewModel

sealed class Screen(val route: String) {
    data object Welcome : Screen("welcome")
    data object Library : Screen("library")
    data object Player : Screen("player")
    data object Lyrics : Screen("lyrics")
}

/**
 * Main application navigation graph coordinating screen transitions
 * across Welcome, Library, Player, and LyricsSheet according to App_flow.md.
 */
@Composable
fun AppNavigation(
    viewModel: MainViewModel,
    navController: NavHostController = rememberNavController()
) {
    NavHost(
        navController = navController,
        startDestination = Screen.Welcome.route
    ) {
        composable(Screen.Welcome.route) {
            WelcomeScreen(
                onGetStarted = {
                    navController.navigate(Screen.Library.route) {
                        popUpTo(Screen.Welcome.route) { inclusive = true }
                    }
                }
            )
        }

        composable(Screen.Library.route) {
            LibraryScreen(
                viewModel = viewModel,
                onOpenPlayer = {
                    navController.navigate(Screen.Player.route)
                }
            )
        }

        composable(Screen.Player.route) {
            PlayerScreen(
                viewModel = viewModel,
                onCollapse = {
                    navController.popBackStack()
                },
                onOpenLyrics = {
                    navController.navigate(Screen.Lyrics.route)
                }
            )
        }

        composable(Screen.Lyrics.route) {
            LyricsSheet(
                viewModel = viewModel,
                onClose = {
                    navController.popBackStack()
                }
            )
        }
    }
}
