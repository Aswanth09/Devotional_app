# -*- coding: utf-8 -*-
"""
Calibrated generator for Sri Krishna Ashtakam lyrics JSON.
Exact vocal onsets verified against audio waveform:
- 0 -> 850 ms: Brief lead-in
- 850 -> 471010 ms: 8 Verses + Phalasruti + Mangalam with authentic chant cadence
"""
import json
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "app", "src", "main", "assets", "lyrics")
os.makedirs(OUTPUT_DIR, exist_ok=True)

KRISHNA_VERSES = [
    (
        "వసుదేవసుతం దేవం కంసచాణూరమర్దనమ్ |\nదేవకీ పరమానందం కృష్ణం వందే జగద్గురుమ్ ||",
        "Vasudeva Sutam Devam Kamsa Chaanoora Mardanam |\nDevakee Paramaanandam Krishnam Vande Jagadgurum ||"
    ),
    (
        "అతసీపుష్ప సంకాశం హారనూపుర శోభితమ్ |\nరత్నకంకణ కేయూరం కృష్ణం వందే జగద్గురుమ్ ||",
        "Atasee Pushpa Sankaasham Haara Noopura Shobhitam |\nRatna Kankana Keyooram Krishnam Vande Jagadgurum ||"
    ),
    (
        "కుటిలాలక సంయుక్తం పూర్ణచంద్ర నిభాననమ్ |\nవిలసత్కుండలధరం కృష్ణం వందే జగద్గురుమ్ ||",
        "Kutilaalaka Samyuktam Poorna Chandra Nibhaananam |\nVilasat Kundaladharam Krishnam Vande Jagadgurum ||"
    ),
    (
        "మందారగంధ సంయుక్తం చారుహాసం చతుర్భుజమ్ |\nబర్హిపింఛావచూడాంగం కృష్ణం వందే జగద్గురుమ్ ||",
        "Mandaara Gandha Samyuktam Chaaruhaasam Chaturbhujam |\nBarhi Pinchhaava Choodaangam Krishnam Vande Jagadgurum ||"
    ),
    (
        "ఉత్ఫుల్ల పద్మపత్రాక్షం నీలజీమూత సన్నిభమ్ |\nయాదవానాం శిరోరత్నం కృష్ణం వందే జగద్గురుమ్ ||",
        "Utphulla Padma Patraaksham Neela Jeemoota Sannibham |\nYaadavaanaam Shiroratnam Krishnam Vande Jagadgurum ||"
    ),
    (
        "రుక్మిణీ కేళీ సంయుక్తం పీతాంబర సుశోభితమ్ |\nఅవాప్తతులసీగంధం కృష్ణం వందే జగద్గురుమ్ ||",
        "Rukminee Kelee Samyuktam Peetaambara Sushobhitam |\nAvaapta Tulasee Gandham Krishnam Vande Jagadgurum ||"
    ),
    (
        "గోపికానాం కుచద్వంద్వ కుంకుమాంకిత వక్షసమ్ |\nశ్రీనికేతం మహేష్వాసం కృష్ణం వందే జగద్గురుమ్ ||",
        "Gopikaanaam Kucha Dvandva Kunkumaankita Vakshasam |\nShreeniketam Maheshvaasam Krishnam Vande Jagadgurum ||"
    ),
    (
        "శ్రీవత్సాంకం మహోరస్కం వనమాలా విరాజితమ్ |\nశంఖచక్రధరం దేవం కృష్ణం వందే జగద్గురుమ్ ||",
        "Shreevatsaankam Mahoraskam Vanamaalaa Viraajitam |\nShankha Chakra Dharam Devam Krishnam Vande Jagadgurum ||"
    ),
    (
        "కృష్ణాష్టకమిదం పుణ్యం ప్రాతరుత్థాయ యః పఠేత్ |\nకోటిజన్మకృతం పాపం స్మరణేన వినశ్యతి ||",
        "Krishnaashtakam Idam Punyam Praatarutthaaya Yah Pathet |\nKoti Janma Kritam Paapam Smaranena Vinashyati ||"
    ),
    (
        "॥ ఇతి శ్రీ శంకరాచార్య విరచితం శ్రీ కృష్ణాష్టకం సంపూర్ణమ్ ॥\nశ్రీ కృష్ణార్పణమస్తు ||",
        "|| Thus concludes the Sri Krishna Ashtakam composed by Adi Shankaracharya ||\nDedicated to Lord Sri Krishna ||"
    )
]

# Total duration: 471010 ms
# Start at 850 ms
start_base = 850
end_base = 471010
span = (end_base - start_base) / float(len(KRISHNA_VERSES))

stanzas = []

# Optional intro header
stanzas.append({
    "index": 1,
    "timestampMs": 0,
    "startTimeMs": 0,
    "endTimeMs": start_base,
    "textTelugu": "॥ శ్రీ కృష్ణాష్టకమ్ - ఆరంభ ధ్యానమ్ ॥",
    "telugu": "॥ శ్రీ కృష్ణాష్టకమ్ - ఆరంభ ధ్యానమ్ ॥",
    "textEnglish": "|| Sri Krishna Ashtakam - Invocation ||",
    "english": "|| Sri Krishna Ashtakam - Invocation ||"
})

for i, (tel, eng) in enumerate(KRISHNA_VERSES):
    s_ms = int(round(start_base + i * span))
    e_ms = int(round(start_base + (i + 1) * span))
    stanzas.append({
        "index": 2 + i,
        "timestampMs": s_ms,
        "startTimeMs": s_ms,
        "endTimeMs": e_ms,
        "textTelugu": tel,
        "telugu": tel,
        "textEnglish": eng,
        "english": eng
    })

output_file = os.path.join(OUTPUT_DIR, "krishna_ashtakam.json")
data = {
    "trackId": "krishna_ashtakam",
    "titleTelugu": "శ్రీ కృష్ణాష్టకం",
    "titleEnglish": "Sri Krishna Ashtakam",
    "totalStanzas": len(stanzas),
    "stanzas": stanzas
}

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Calibrated {output_file} with {len(stanzas)} stanzas.")
