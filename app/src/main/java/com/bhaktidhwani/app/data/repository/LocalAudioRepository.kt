package com.bhaktidhwani.app.data.repository

import android.content.Context
import com.bhaktidhwani.app.R
import com.bhaktidhwani.app.data.model.Stanza
import com.bhaktidhwani.app.data.model.Track
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import org.json.JSONObject

/**
 * Single source of truth for offline devotional audio tracks and lyrics.
 * Operates 100% offline without remote network calls.
 */
class LocalAudioRepository {

    val coreTracks: List<Track> = listOf(
        Track(
            id = "vishnu_sahasranamam",
            titleTelugu = "à°¶à±à°°à±€ à°µà°¿à°·à±à°£à± à°¸à°¹à°¸à±à°°à°¨à°¾à°® à°¸à±à°¤à±‹à°¤à±à°°à°®à±",
            titleEnglish = "Sri Vishnu Sahasranama Stotram",
            deity = "Vishnu",
            deityTelugu = "à°¶à±à°°à±€ à°®à°¹à°¾à°µà°¿à°·à±à°£à±à°µà±",
            rawResId = R.raw.vishnu_sahasranamam,
            thumbnailResId = R.drawable.art_vishnu,
            durationMs = 30020L,
            lyricsAssetPath = "lyrics/vishnu_sahasranamam.json",
            descriptionTelugu = "1000 à°¦à°¿à°µà±à°¯ à°¨à°¾à°®à°¾à°² à°ªà°µà°¿à°¤à±à°° à°¸à±à°¤à±‹à°¤à±à°°à°‚",
            descriptionEnglish = "Chanting of the 1000 Divine Names of Lord Vishnu"
        ),
        Track(
            id = "hanuman_chalisa",
            titleTelugu = "à°¹à°¨à±à°®à°¾à°¨à± à°šà°¾à°²à±€à°¸à°¾",
            titleEnglish = "Hanuman Chalisa",
            deity = "Hanuman",
            deityTelugu = "à°¶à±à°°à±€ à°¹à°¨à±à°®à°¾à°¨à±",
            rawResId = R.raw.hanuman_chalisa,
            thumbnailResId = R.drawable.art_hanuman,
            durationMs = 30020L,
            lyricsAssetPath = "lyrics/hanuman_chalisa.json",
            descriptionTelugu = "à°—à±‹à°¸à±à°µà°¾à°®à°¿ à°¤à±à°²à°¸à±€à°¦à°¾à°¸à± à°°à°šà°¿à°‚à°šà°¿à°¨ à°°à°•à±à°·à°¾ à°¸à±à°¤à±‹à°¤à±à°°à°‚",
            descriptionEnglish = "Forty Hymns of Strength and Protection"
        ),
        Track(
            id = "govinda_namalu",
            titleTelugu = "à°—à±‹à°µà°¿à°‚à°¦ à°¨à°¾à°®à°¾à°²à±",
            titleEnglish = "Govinda Namalu",
            deity = "Venkateswara",
            deityTelugu = "à°¶à±à°°à±€ à°µà±‡à°‚à°•à°Ÿà±‡à°¶à±à°µà°° à°¸à±à°µà°¾à°®à°¿",
            rawResId = R.raw.govinda_namalu,
            thumbnailResId = R.drawable.art_venkateswara,
            durationMs = 30020L,
            lyricsAssetPath = "lyrics/govinda_namalu.json",
            descriptionTelugu = "à°¤à°¿à°°à±à°®à°² à°µà±‡à°‚à°•à°Ÿà±‡à°¶à±à°µà°° à°¸à±à°µà°¾à°®à°¿ à°¨à°¾à°® à°¸à°‚à°•à±€à°°à±à°¤à°¨",
            descriptionEnglish = "Sacred Chants of Lord Venkateswara Balaji"
        ),
        Track(
            id = "lakshmi_ashtottaram",
            titleTelugu = "à°¶à±à°°à±€ à°²à°•à±à°·à±à°®à±€ à°…à°·à±à°Ÿà±‹à°¤à±à°¤à°° à°¶à°¤à°¨à°¾à°®à°¾à°µà°³à°¿",
            titleEnglish = "Sri Lakshmi Ashtottara Shatanamavali",
            deity = "Lakshmi",
            deityTelugu = "à°¶à±à°°à±€ à°²à°•à±à°·à±à°®à±€ à°¦à±‡à°µà°¿",
            rawResId = R.raw.lakshmi_ashtottaram,
            thumbnailResId = R.drawable.art_lakshmi,
            durationMs = 30020L,
            lyricsAssetPath = "lyrics/lakshmi_ashtottaram.json",
            descriptionTelugu = "à°…à°·à±à°Ÿà±ˆà°¶à±à°µà°°à±à°¯ à°ªà±à°°à°¦à°¾à°¯à°• à°¦à°¿à°µà±à°¯ à°¸à±à°¤à±‹à°¤à±à°°à°‚",
            descriptionEnglish = "108 Auspicious Names of Goddess Lakshmi"
        ),
        Track(
            id = "garuda_gamana",
            titleTelugu = "à°—à°°à±à°¡ à°—à°®à°¨ à°¤à°µ à°šà°°à°£ à°•à°®à°²à°®à°¿à°¹",
            titleEnglish = "Garuda Gamana Tava Charana",
            deity = "Vishnu",
            deityTelugu = "à°¶à±à°°à±€ à°®à°¹à°¾à°µà°¿à°·à±à°£à±à°µà±",
            rawResId = R.raw.garuda_gamana,
            thumbnailResId = R.drawable.art_vishnu,
            durationMs = 30020L,
            lyricsAssetPath = "lyrics/garuda_gamana.json",
            descriptionTelugu = "à°¶à°‚à°•à°°à°¾à°šà°¾à°°à±à°¯ à°µà°¿à°°à°šà°¿à°¤ à°—à°°à±à°¡ à°—à°®à°¨ à°¸à±à°¤à±‹à°¤à±à°°à°‚",
            descriptionEnglish = "Classical Stotra in Reverence to Lord Vishnu"
        ),
        Track(
            id = "krishna_ashtakam",
            titleTelugu = "à°¶à±à°°à±€ à°•à±ƒà°·à±à°£à°¾à°·à±à°Ÿà°•à°‚",
            titleEnglish = "Sri Krishna Ashtakam",
            deity = "Krishna",
            deityTelugu = "à°¶à±à°°à±€ à°•à±ƒà°·à±à°£ à°ªà°°à°®à°¾à°¤à±à°®",
            rawResId = R.raw.krishna_ashtakam,
            thumbnailResId = R.drawable.art_krishna,
            durationMs = 30020L,
            lyricsAssetPath = "lyrics/krishna_ashtakam.json",
            descriptionTelugu = "à°µà°¸à±à°¦à±‡à°µà°¸à±à°¤à°‚ à°¦à±‡à°µà°‚ à°•à°‚à°¸à°šà°¾à°£à±‚à°°à°®à°°à±à°¦à°¨à°‚",
            descriptionEnglish = "Eight Divine Verses in Praise of Lord Krishna"
        )
    )

    fun getTracks(): List<Track> = coreTracks

    fun getTrackById(id: String): Track? = coreTracks.firstOrNull { it.id == id }

    fun getTracksByDeity(deity: String): List<Track> {
        return if (deity.equals("All", ignoreCase = true)) {
            coreTracks
        } else {
            coreTracks.filter { it.deity.equals(deity, ignoreCase = true) }
        }
    }

    fun getDeityCategories(): List<String> = listOf("All", "Vishnu", "Venkateswara", "Hanuman", "Lakshmi", "Krishna")

    /**
     * Parses lyrics JSON asynchronously on Dispatchers.IO.
     */
    suspend fun loadLyrics(context: Context, assetPath: String): List<Stanza> = withContext(Dispatchers.IO) {
        try {
            val jsonString = context.assets.open(assetPath).bufferedReader().use { it.readText() }
            val rootObject = JSONObject(jsonString)
            val stanzasArray = rootObject.getJSONArray("stanzas")
            val stanzas = ArrayList<Stanza>(stanzasArray.length())
            for (i in 0 until stanzasArray.length()) {
                val item = stanzasArray.getJSONObject(i)
                stanzas.add(
                    Stanza(
                        index = item.getInt("index"),
                        startTimeMs = item.getLong("startTimeMs"),
                        endTimeMs = item.getLong("endTimeMs"),
                        telugu = item.getString("telugu"),
                        english = item.getString("english")
                    )
                )
            }
            stanzas
        } catch (t: Throwable) {
            emptyList()
        }
    }
}

