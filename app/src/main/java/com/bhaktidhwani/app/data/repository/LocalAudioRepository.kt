package com.bhaktidhwani.app.data.repository

import android.content.Context
import com.bhaktidhwani.app.R
import com.bhaktidhwani.app.data.model.Stanza
import com.bhaktidhwani.app.data.model.Track
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import org.json.JSONObject

/**
 * LocalAudioRepository manages access to offline devotional audio tracks,
 * local metadata, deity groupings, and time-synced lyrics parsing.
 */
class LocalAudioRepository {

    val coreTracks: List<Track> = listOf(
        Track(
            id = "vishnu_sahasranamam",
            titleTelugu = "శ్రీ విష్ణు సహస్రనామ స్తోత్రము",
            titleEnglish = "Sri Vishnu Sahasranama Stotram",
            deity = "Vishnu",
            deityTelugu = "శ్రీ మహావిష్ణువు",
            rawResId = R.raw.vishnu_sahasranamam,
            thumbnailResId = R.drawable.art_vishnu,
            durationMs = 30020L,
            lyricsAssetPath = "lyrics/vishnu_sahasranamam.json",
            descriptionTelugu = "1000 దివ్య నామాల పవిత్ర స్తోత్రం",
            descriptionEnglish = "Chanting of the 1000 Divine Names of Lord Vishnu"
        ),
        Track(
            id = "hanuman_chalisa",
            titleTelugu = "హనుమాన్ చాలీసా",
            titleEnglish = "Hanuman Chalisa",
            deity = "Hanuman",
            deityTelugu = "శ్రీ హనుమాన్",
            rawResId = R.raw.hanuman_chalisa,
            thumbnailResId = R.drawable.art_hanuman,
            durationMs = 30020L,
            lyricsAssetPath = "lyrics/hanuman_chalisa.json",
            descriptionTelugu = "గోస్వామి తులసీదాస్ రచించిన రక్షా స్తోత్రం",
            descriptionEnglish = "Forty Hymns of Strength and Protection"
        ),
        Track(
            id = "govinda_namalu",
            titleTelugu = "గోవింద నామాలు",
            titleEnglish = "Govinda Namalu",
            deity = "Venkateswara",
            deityTelugu = "శ్రీ వేంకటేశ్వర స్వామి",
            rawResId = R.raw.govinda_namalu,
            thumbnailResId = R.drawable.art_venkateswara,
            durationMs = 30020L,
            lyricsAssetPath = "lyrics/govinda_namalu.json",
            descriptionTelugu = "తిరుమల వేంకటేశ్వర స్వామి నామ సంకీర్తన",
            descriptionEnglish = "Sacred Chants of Lord Venkateswara Balaji"
        ),
        Track(
            id = "lakshmi_ashtottaram",
            titleTelugu = "శ్రీ లక్ష్మీ అష్టోత్తర శతనామావళి",
            titleEnglish = "Sri Lakshmi Ashtottara Shatanamavali",
            deity = "Lakshmi",
            deityTelugu = "శ్రీ మహాలక్ష్మి దేవి",
            rawResId = R.raw.lakshmi_ashtottaram,
            thumbnailResId = R.drawable.art_lakshmi,
            durationMs = 30020L,
            lyricsAssetPath = "lyrics/lakshmi_ashtottaram.json",
            descriptionTelugu = "అష్టైశ్వర్య ప్రదాయక దివ్య స్తోత్రం",
            descriptionEnglish = "108 Auspicious Names of Goddess Lakshmi"
        ),
        Track(
            id = "garuda_gamana",
            titleTelugu = "గరుడ గమన తవ చరణ కమలమిహ",
            titleEnglish = "Garuda Gamana Tava Charana",
            deity = "Vishnu",
            deityTelugu = "శ్రీ మహావిష్ణువు",
            rawResId = R.raw.garuda_gamana,
            thumbnailResId = R.drawable.art_vishnu,
            durationMs = 30020L,
            lyricsAssetPath = "lyrics/garuda_gamana.json",
            descriptionTelugu = "శంకరాచార్య విరచిత గరుడ గమన స్తోత్రం",
            descriptionEnglish = "Classical Stotra in Reverence to Lord Vishnu"
        ),
        Track(
            id = "krishna_ashtakam",
            titleTelugu = "శ్రీ కృష్ణాష్టకం",
            titleEnglish = "Sri Krishna Ashtakam",
            deity = "Krishna",
            deityTelugu = "శ్రీ కృష్ణ పరమాత్మ",
            rawResId = R.raw.krishna_ashtakam,
            thumbnailResId = R.drawable.art_krishna,
            durationMs = 30020L,
            lyricsAssetPath = "lyrics/krishna_ashtakam.json",
            descriptionTelugu = "వసుదేవసుతం దేవం కంసచాణూరమర్దనం",
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
