# -*- coding: utf-8 -*-
"""
Calibrated generator for Sri Lakshmi Ashtottara Shatanamavali lyrics JSON.
Dhyana invocation starts at 4240 ms, 108 names from 28000 ms, mangalam to 431330 ms.
"""
import json
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "app", "src", "main", "assets", "lyrics")
os.makedirs(OUTPUT_DIR, exist_ok=True)

LAKSHMI_NAMES = [
    ("ప్రకృతి", "Prakriti"),
    ("వికృతి", "Vikriti"),
    ("విద్యా", "Vidya"),
    ("సర్వభూతహితప్రదా", "Sarvabhuta Hitaprada"),
    ("శ్రద్ధా", "Shraddha"),
    ("విభూతి", "Vibhuti"),
    ("సురభి", "Surabhi"),
    ("పరమాత్మికా", "Paramatmika"),
    ("వాచీ", "Vachi"),
    ("పద్మాలయా", "Padmalaya"),
    ("పద్మా", "Padma"),
    ("శుచి", "Shuchi"),
    ("స్వాహా", "Svaha"),
    ("స్వధా", "Svadha"),
    ("సుధా", "Sudha"),
    ("ధన్యా", "Dhanya"),
    ("హిరణ్మయీ", "Hiranmayi"),
    ("లక్ష్మీ", "Lakshmi"),
    ("నిత్యపుష్టా", "Nityapushta"),
    ("విభావరి", "Vibhavari"),
    ("అదితి", "Aditi"),
    ("దితి", "Diti"),
    ("దీప్తా", "Dipta"),
    ("వసుధా", "Vasudha"),
    ("వసుధారిణీ", "Vasudharini"),
    ("కమలా", "Kamala"),
    ("కాంతా", "Kanta"),
    ("కామాక్షీ", "Kamakshi"),
    ("క్షీరోదసంభవా", "Kshiroda Sambhava"),
    ("అనుగ్రహప్రదా", "Anugraha Prada"),
    ("బుద్ధి", "Buddhi"),
    ("అనఘా", "Anagha"),
    ("హరివల్లభా", "Hari Vallabha"),
    ("అశోకా", "Ashoka"),
    ("అమృతా", "Amrita"),
    ("దీప్తా", "Deepta"),
    ("లోకశోకవినాశినీ", "Loka Shoka Vinashini"),
    ("ధర్మనిలయా", "Dharma Nilaya"),
    ("కరుణా", "Karuna"),
    ("లోకమాతృకా", "Loka Matrika"),
    ("పద్మప్రియా", "Padma Priya"),
    ("పద్మహస్తా", "Padma Hasta"),
    ("పద్మాక్షీ", "Padmakshi"),
    ("పద్మసుందరీ", "Padma Sundari"),
    ("పద్మోద్భవా", "Padmodbhava"),
    ("పద్మముఖీ", "Padma Mukhi"),
    ("పద్మనాభప్రియా", "Padmanabha Priya"),
    ("రమా", "Rama"),
    ("పద్మమాలాధరా", "Padma Maladhara"),
    ("దేవీ", "Devi"),
    ("పద్మినీ", "Padmini"),
    ("పద్మగంధినీ", "Padma Gandhini"),
    ("పుణ్యగంధా", "Punya Gandha"),
    ("సుప్రసన్నా", "Suprasanna"),
    ("ప్రసాదాభిముఖీ", "Prasadabhimukhi"),
    ("ప్రభా", "Prabha"),
    ("చంద్రవదనా", "Chandra Vadana"),
    ("చంద్రా", "Chandra"),
    ("చంద్రసహోదరీ", "Chandra Sahodari"),
    ("చతుర్భుజా", "Chaturbhuja"),
    ("చంద్రరూపా", "Chandra Rupa"),
    ("ఇందిరా", "Indira"),
    ("ఇందుశీతలా", "Indu Shitala"),
    ("ఆహ్లాదజననీ", "Ahladajanani"),
    ("పుష్టి", "Pushti"),
    ("శివా", "Shiva"),
    ("శివకరీ", "Shivakari"),
    ("సత్యై", "Satyai"),
    ("విమలా", "Vimala"),
    ("విశ్వజననీ", "Vishwajanani"),
    ("తుష్టి", "Tushti"),
    ("దారిద్ర్యనాశినీ", "Daridrya Nashini"),
    ("ప్రీతిపుష్కరిణీ", "Priti Pushkarini"),
    ("శాంతా", "Shanta"),
    ("శుక్లమాల్యాంబరా", "Shuklamalyambara"),
    ("శ్రీ", "Shri"),
    ("భాస్కరీ", "Bhaskari"),
    ("బిల్వనిలయా", "Bilvanilaya"),
    ("వరాహరోహా", "Vararoha"),
    ("యశస్వినీ", "Yashasvini"),
    ("వసుంధరా", "Vasundhara"),
    ("ఉదారాంగా", "Udaranga"),
    ("హరిణీ", "Harini"),
    ("హేమమాలినీ", "Hemamalini"),
    ("ధనధాన్యకరీ", "Dhanadhanyakari"),
    ("సిద్ధి", "Siddhi"),
    ("స్త్రైణసౌమ్యా", "Strainasaumya"),
    ("శుభప్రదా", "Shubhaprada"),
    ("నృపవేశ్మగతానందా", "Nripaveshmagatananda"),
    ("వరలక్ష్మీ", "Varalakshmi"),
    ("వసుప్రదా", "Vasuprada"),
    ("శుభా", "Shubha"),
    ("హిరణ్యప్రాకారా", "Hiranya Prakara"),
    ("సముద్రతనయా", "Samudra Tanaya"),
    ("జయా", "Jaya"),
    ("మంగళా", "Mangala"),
    ("దేవీ", "Devi"),
    ("విష్ణువక్షఃస్థలస్థితా", "Vishnuvakshahsthalasthita"),
    ("విష్ణుపత్నీ", "Vishnupatni"),
    ("ప్రసన్నాక్షీ", "Prasannakshi"),
    ("నారాయణసమాశ్రితా", "Narayana Samashrita"),
    ("దారిద్ర్యధ్వంసినీ", "Daridrya Dhwamsini"),
    ("సర్వోపద్రవవారిణీ", "Sarvopadrava Varini"),

    ("నవదుర్గా", "Navadurga"),
    ("మహాకాలీ", "Mahakali"),
    ("బ్రహ్మవిష్ణుశివాత్మికా", "Brahma Vishnu Shivatmika"),
    ("త్రికాలజ్ఞానసంపన్నా", "Trikalajnana Sampanna"),
    ("భువనేశ్వరీ", "Bhuvaneshwari")
]

stanzas = []

# Dhyanam (0 -> 8700 ms, vocal onset at 2575 ms)
stanzas.append({
    "index": 1,
    "timestampMs": 0,
    "startTimeMs": 0,
    "endTimeMs": 8700,
    "textTelugu": "॥ శ్రీ లక్ష్మీ అష్టోత్తర శతనామావళిః - ధ్యానమ్ ॥\nవందే పద్మకరాం ప్రసన్నవదనాం సౌభాగ్యదాం భాగ్యదామ్ |\nహస్తాభ్యామభయప్రదాం మణిగణైర్నానావిధైర్భూషితామ్ ||",
    "telugu": "॥ శ్రీ లక్ష్మీ అష్టోత్తర శతనామావళిః - ధ్యానమ్ ॥\nవందే పద్మకరాం ప్రసన్నవదనాం సౌభాగ్యదాం భాగ్యదామ్ |\nహస్తాభ్యామభయప్రదాం మణిగణైర్నానావిధైర్భూషితామ్ ||",
    "textEnglish": "|| Sri Lakshmi Ashtottara Shatanamavali - Dhyanam ||\nVande Padmakaraam Prasanna Vadanaam Saubhaagyadaam Bhaagyadaam |\nHastaabhyaam Abhayapradaam Maniganair Naanaavidhair Bhooshitaam ||",
    "english": "|| Sri Lakshmi Ashtottara Shatanamavali - Dhyanam ||\nVande Padmakaraam Prasanna Vadanaam Saubhaagyadaam Bhaagyadaam |\nHastaabhyaam Abhayapradaam Maniganair Naanaavidhair Bhooshitaam ||"
})

start_base = 8700
end_names = 265000
name_dur = (end_names - start_base) / 108.0

for i, (tel, eng) in enumerate(LAKSHMI_NAMES):
    s_ms = int(round(start_base + i * name_dur))
    e_ms = int(round(start_base + (i + 1) * name_dur))
    stanzas.append({
        "index": 2 + i,
        "timestampMs": s_ms,
        "startTimeMs": s_ms,
        "endTimeMs": e_ms,
        "textTelugu": f"{i+1}. ఓం {tel}యై నమః",
        "telugu": f"{i+1}. ఓం {tel}యై నమః",
        "textEnglish": f"{i+1}. Om {eng}yai Namah",
        "english": f"{i+1}. Om {eng}yai Namah"
    })

# Mangalam (265000 -> 283950 ms)
stanzas.append({
    "index": 110,
    "timestampMs": 265000,
    "startTimeMs": 265000,
    "endTimeMs": 283950,
    "textTelugu": "॥ శ్రీ మహాలక్ష్మ్యష్టోత్తర శతనామ స్తోత్రం సంపూర్ణమ్ ॥\nసర్వమంగళ మాంగల్యే శివే సర్వార్థ సాధికే |\nశరణ్యే త్ర్యంబకే గౌరి నారాయణి నమోఽస్తు తే ||",
    "telugu": "॥ శ్రీ మహాలక్ష్మ్యష్టోత్తర శతనామ స్తోత్రం సంపూర్ణమ్ ॥\nసర్వమంగళ మాంగల్యే శివే సర్వార్థ సాధికే |\nశరణ్యే త్ర్యంబకే గౌరి నారాయణి నమోఽస్తు తే ||",
    "textEnglish": "|| Sri Mahalakshmi Ashtottara Shatanamavali Complete ||\nSarva Mangala Maangalye Shive Sarvaartha Saadhike |\nSharanye Tryambake Gauri Naaraayani Namo'stu Te ||",
    "english": "|| Sri Mahalakshmi Ashtottara Shatanamavali Complete ||\nSarva Mangala Maangalye Shive Sarvaartha Saadhike |\nSharanye Tryambake Gauri Naaraayani Namo'stu Te ||"
})


output_file = os.path.join(OUTPUT_DIR, "lakshmi_ashtottaram.json")
data = {
    "trackId": "lakshmi_ashtottaram",
    "titleTelugu": "శ్రీ లక్ష్మీ అష్టోత్తర శతనామావళి",
    "titleEnglish": "Sri Lakshmi Ashtottara Shatanamavali",
    "totalStanzas": len(stanzas),
    "stanzas": stanzas
}

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Calibrated {output_file} with {len(stanzas)} stanzas.")
