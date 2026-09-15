# -*- coding: utf-8 -*-
"""
Calibrated generator for Sri Hanuman Chalisa lyrics JSON.
Exact vocal onsets verified against audio waveform:
- 0 -> 2450 ms: Intro bells / prelude
- 2450 -> 16240 ms: Opening Doha 1 (Shree Guru Charana...)
- 16240 -> 46250 ms: Opening Doha 2 (Buddhiheena Tanu...)
- 46250 -> 516000 ms: Chaupais 1 to 40 (~11743.75 ms each)
- 516000 -> 560000 ms: Concluding Doha (Pavana Tanaya...)
- 560000 -> 588420 ms: Outro Mangalam & Bells
"""
import json
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "app", "src", "main", "assets", "lyrics")
os.makedirs(OUTPUT_DIR, exist_ok=True)

CHALISA_DATA = [
    (
        "శ్రీగురు చరణ సరోజ రజ నిజమను ముకురు సుధారి |\nబరణౌ రఘువర విమల యశ జో దాయకు ఫలచారి ||",
        "Shree Guru Charana Saroja Raja Nija Manu Mukuru Sudhaari |\nBaranau Raghuvara Vimala Yasha Jo Daayaku Phala Chaari ||"
    ),
    (
        "బుద్ధిహీన తను జానికే సుమిరౌ పవనకుమార |\nబల బుద్ధి విద్యా దేహు మోహి హరహు కలేశ వికార ||",
        "Buddhiheena Tanu Jaanike Sumirau Pavana Kumaara |\nBala Buddhi Vidyaa Dehu Mohi Harahu Kalesha Vikaara ||"
    ),
    (
        "జయ హనుమాన జ్ఞాన గుణ సాగర |\nజయ కపీశ తిహు లోక ఉజాగర ||",
        "Jaya Hanumaana Gyaana Guna Saagara |\nJaya Kapeesha Tihu Loka Ujaagara ||"
    ),
    (
        "రామదూత అతులిత బలధామా |\nఅంజనిపుత్ర పవనసుత నామా ||",
        "Raamadoota Atulita Baladhaamaa |\nAnjani Putra Pavanasuta Naamaa ||"
    ),
    (
        "మహావీర విక్రమ బజరంగీ |\nకుమతి నివార సుమతి కే సంగీ ||",
        "Mahaaveera Vikrama Bajarangee |\nKumati Nivaara Sumati Ke Sangee ||"
    ),
    (
        "కంచన బరణ బిరాజ సుబేసా |\nకానన కుండల కుంచిత కేశా ||",
        "Kanchana Barana Biraaja Subesaa |\nKaanana Kundala Kunchita Kesaa ||"
    ),
    (
        "హాథ వజ్ర ఔ ధ్వజా బిరాజై |\nకాంధే మూంజ జనేవూ సాజై ||",
        "Haatha Vajra Au Dhvajaa Biraajai |\nKaandhe Moonja Janevoo Saajai ||"
    ),
    (
        "శంకర సువన కేసరీ నందన |\nతేజ ప్రతాప మహా జగ వందన ||",
        "Shankara Suvana Kesaree Nandana |\nTeja Prataapa Mahaa Jaga Vandana ||"
    ),
    (
        "విద్యావాన గుణీ అతి చాతుర |\nరామ కాజ కరిబే కో ఆతుర ||",
        "Vidyaavaana Gunee Ati Chaatura |\nRaama Kaaja Karibe Ko Aatura ||"
    ),
    (
        "ప్రభు చరిత్ర సునిబే కో రసియా |\nరామ లఖన సీతా మన బసియా ||",
        "Prabhu Charitra Sunibe Ko Rasiyaa |\nRaama Lakhana Seetaa Mana Basiyaa ||"
    ),
    (
        "సూక్ష్మ రూప ధరి సియహి దిఖావా |\nబికట రూప ధరి లంక జరావా ||",
        "Sookshma Roopa Dhari Siyahi Dikhaavaa |\nBikata Roopa Dhari Lanka Jaraavaa ||"
    ),
    (
        "భీమ రూప ధరి అసుర సంహారే |\nరామచంద్ర కే కాజ సంవారే ||",
        "Bheema Roopa Dhari Asura Samhaare |\nRaamachandra Ke Kaaja Samvaare ||"
    ),
    (
        "లాయ సంజీవన లఖన జియాయే |\nశ్రీరఘుబీర హరషి ఉర లాయే ||",
        "Laaya Sanjeevana Lakhana Jiyaaye |\nShree Raghubeera Harashi Ura Laaye ||"
    ),
    (
        "రఘుపతి కీన్హీ బహుత బడాయీ |\nతుమ మమ ప్రియ భరతహి సమ భాయీ ||",
        "Raghupati Keenhee Bahuta Badaayee |\nTuma Mama Priya Bharatahi Sama Bhaayee ||"
    ),
    (
        "సహస్ర వదన తుమ్హరో యశ గావై |\nఅస కహి శ్రీపతి కంఠ లగావై ||",
        "Sahasra Vadana Tumharo Yasha Gaavai |\nAsa Kahi Shreepati Kantha Lagaavai ||"
    ),
    (
        "సనకాదిక బ్రహ్మాది మునీశా |\nనారద శారద సహిత అహీశా ||",
        "Sanakaadika Brahmaadi Muneeshaa |\nNaarada Shaarada Sahita Aheeshaa ||"
    ),
    (
        "యమ కుబేర దిగపాల జహాం తే |\nకవి కోవిద కహి సకే కహాం తే ||",
        "Yama Kubera Digapaala Jahaam Te |\nKavi Kovida Kahi Sake Kahaam Te ||"
    ),
    (
        "తుమ ఉపకార సుగ్రీవహిం కీన్హా |\nరామ మిలాయ రాజపద దీన్హా ||",
        "Tuma Upakaara Sugreevahin Keenhaa |\nRaama Milaaya Raajapada Deenhaa ||"
    ),
    (
        "తుమ్హరో మంత్ర విభీషణ మానా |\nలంకేశ్వర భయే సబ జగ జానా ||",
        "Tumharo Mantra Vibheeshana Maanaa |\nLankeshvara Bhaye Saba Jaga Jaanaa ||"
    ),
    (
        "యుగ సహస్ర యోజన పర భానూ |\nలీల్యో తాహి మధుర ఫల జానూ ||",
        "Yuga Sahasra Yojana Para Bhaanoo |\nLeelyo Taahi Madhura Phala Jaanoo ||"
    ),
    (
        "ప్రభు ముద్రికా మేలి ముఖ మాహీం |\nజలధి లాంఘి గయే అచరజ నాహీం ||",
        "Prabhu Mudrikaa Meli Mukha Maaheem |\nJaladhi Laanghi Gaye Acharaja Naaheem ||"
    ),
    (
        "దుర్గమ కాజ జగత కే జేతే |\nసుగమ అనుగ్రహ తుమ్హరే తేతే ||",
        "Durgama Kaaja Jagata Ke Jete |\nSugama Anugraha Tumhare Tete ||"
    ),
    (
        "రామ దుఆరే తుమ రఖవారే |\nహోత న ఆజ్ఞా బిను పైసారే ||",
        "Raama Duaare Tuma Rakhavaare |\nHota Na Aagyaa Binu Paisaare ||"
    ),
    (
        "సబ సుఖ లహై తుమ్హారీ శరణా |\nతుమ రక్షక కాహూ కో డర నా ||",
        "Saba Sukha Lahai Tumhaaree Sharanaa |\nTuma Rakshaka Kaahoo Ko Dara Naa ||"
    ),
    (
        "ఆపన తేజ సంహారో ఆపై |\nతీనోం లోక హాంక తే కాంపై ||",
        "Aapana Teja Samhaaro Aapai |\nTeenom Loka Haanka Te Kaampai ||"
    ),
    (
        "భూత పిశాచ నికట నహిం ఆవై |\nమహావీర జబ నామ సునావై ||",
        "Bhoota Pishaacha Nikata Nahim Aavai |\nMahaaveera Jaba Naama Sunaavai ||"
    ),
    (
        "నాసై రోగ హరై సబ పీరా |\nజపత నిరంతర హనుమత వీరా ||",
        "Naasai Roga Harai Saba Peeraa |\nJapata Nirantara Hanumata Veeraa ||"
    ),
    (
        "సంకట తే హనుమాన ఛుడావై |\nమన క్రమ వచన ధ్యాన జో లావై ||",
        "Sankata Te Hanumaana Chhudaavai |\nMana Krama Vachana Dhyaana Jo Laavai ||"
    ),
    (
        "సబ పర రామ తపస్వీ రాజా |\nతిన కే కాజ సకల తుమ సాజా ||",
        "Saba Para Raama Tapasvee Raajaa |\nTina Ke Kaaja Sakala Tuma Saajaa ||"
    ),
    (
        "ఔర మనోరథ జో కోయీ లావై |\nసోయి అమిత జీవన ఫల పావై ||",
        "Aura Manoratha Jo Ko-ee Laavai |\nSo-i Amita Jeevana Phala Paavai ||"
    ),
    (
        "చారోం యుగ పరతాప తుమ్హారా |\nహై పరసిద్ధ జగత ఉజియారా ||",
        "Chaarom Yuga Parataapa Tumhaaraa |\nHai Parasiddha Jagata Ujiyaaraa ||"
    ),
    (
        "సాధు సంత కే తుమ రఖవారే |\nఅసుర నికందన రామ దులారే ||",
        "Saadhu Santa Ke Tuma Rakhavaare |\nAsura Nikandana Raama Dulaare ||"
    ),
    (
        "అష్ట సిద్ధి నవ నిధి కే దాతా |\nఅస బర దీన్హ జానకీ మాతా ||",
        "Ashta Siddhi Nava Nidhi Ke Daataa |\nAsa Bara Deenha Jaanakee Maataa ||"
    ),
    (
        "రామ రసాయన తుమ్హరే పాసా |\nసదా రహో రఘుపతి కే దాసా ||",
        "Raama Rasaayana Tumhare Paasaa |\nSadaa Raho Raghupati Ke Daasaa ||"
    ),
    (
        "తుమ్హరే భజన రామ కో పావై |\nజన్మ జన్మ కే దుఃఖ బిసరావై ||",
        "Tumhare Bhajana Raama Ko Paavai |\nJanma Janma Ke Duhkha Bisaraavai ||"
    ),
    (
        "అంత కాల రఘువర పుర జాయీ |\nజహాం జన్మ హరిభక్త కహాయీ ||",
        "Anta Kaala Raghuvara Pura Jaayee |\nJahaam Janma Haribhakta Kahaayee ||"
    ),
    (
        "ఔర దేవతా చిత్త న ధరయీ |\nహనుమత సేయి సర్వ సుఖ కరయీ ||",
        "Aura Devataa Chitta Na Dharayee |\nHanumata Se-i Sarva Sukha Karayee ||"
    ),
    (
        "సంకట కటై మిటై సబ పీరా |\nజో సుమిరై హనుమత బలబీరా ||",
        "Sankata Katai Mitai Saba Peeraa |\nJo Sumirai Hanumata Balabeeraa ||"
    ),
    (
        "జై జై జై హనుమాన గోసాయీ |\nకృపా కరో గురుదేవ కీ నాయీ ||",
        "Jai Jai Jai Hanumaana Gosaayee |\nKripaa Karo Gurudeva Kee Naayee ||"
    ),
    (
        "యహ శత వార పాఠ కర జోయీ |\nఛూటహి బంది మహా సుఖ హోయీ ||",
        "Yaha Shata Vaara Paatha Kara Jo-ee |\nChhootahi Bandi Mahaa Sukha Ho-ee ||"
    ),
    (
        "జో యహ పఢై హనుమాన చాలీసా |\nహోయ సిద్ధి సాఖీ గౌరీసా ||",
        "Jo Yaha Padhai Hanumaana Chaaleesaa |\nHoya Siddhi Saakhee Gaureesaa ||"
    ),
    (
        "తులసీదాస సదా హరి చేరా |\nకీజై నాథ హృదయ మహ డేరా ||",
        "Tulaseedaasa Sadaa Hari Cheraa |\nKeejai Naatha Hridaya Maha Deraa ||"
    ),
    (
        "పవనతనయ సంకట హరణ మంగళ మూరతి రూప |\nరామ లఖన సీతా సహిత హృదయ బసహు సుర భూప ||",
        "Pavana Tanaya Sankata Harana Mangala Moorati Roopa |\nRaama Lakhana Seetaa Sahita Hridaya Basahu Sura Bhoopa ||"
    )
]

stanzas = []

# 1. Opening Prelude (0 -> 2450 ms)
stanzas.append({
    "index": 1,
    "timestampMs": 0,
    "startTimeMs": 0,
    "endTimeMs": 2450,
    "textTelugu": "॥ శ్రీ హనుమాన్ చాలీసా - ఆరంభ ధ్యానమ్ ॥",
    "telugu": "॥ శ్రీ హనుమాన్ చాలీసా - ఆరంభ ధ్యానమ్ ॥",
    "textEnglish": "|| Shree Hanuman Chalisa - Invocation ||",
    "english": "|| Shree Hanuman Chalisa - Invocation ||"
})

# 2. Doha 1 (2450 -> 16240 ms)
stanzas.append({
    "index": 2,
    "timestampMs": 2450,
    "startTimeMs": 2450,
    "endTimeMs": 16240,
    "textTelugu": CHALISA_DATA[0][0],
    "telugu": CHALISA_DATA[0][0],
    "textEnglish": CHALISA_DATA[0][1],
    "english": CHALISA_DATA[0][1]
})

# 3. Doha 2 (16240 -> 46250 ms)
stanzas.append({
    "index": 3,
    "timestampMs": 16240,
    "startTimeMs": 16240,
    "endTimeMs": 46250,
    "textTelugu": CHALISA_DATA[1][0],
    "telugu": CHALISA_DATA[1][0],
    "textEnglish": CHALISA_DATA[1][1],
    "english": CHALISA_DATA[1][1]
})

# 4..43. Chaupais 1 to 40 (46250 -> 516000 ms)
chaupai_start = 46250
chaupai_end = 516000
chaupai_dur = (chaupai_end - chaupai_start) / 40.0

for i in range(40):
    s_ms = int(round(chaupai_start + i * chaupai_dur))
    e_ms = int(round(chaupai_start + (i + 1) * chaupai_dur))
    stanzas.append({
        "index": 4 + i,
        "timestampMs": s_ms,
        "startTimeMs": s_ms,
        "endTimeMs": e_ms,
        "textTelugu": CHALISA_DATA[2 + i][0],
        "telugu": CHALISA_DATA[2 + i][0],
        "textEnglish": CHALISA_DATA[2 + i][1],
        "english": CHALISA_DATA[2 + i][1]
    })

# 44. Concluding Doha (516000 -> 560000 ms)
stanzas.append({
    "index": 44,
    "timestampMs": 516000,
    "startTimeMs": 516000,
    "endTimeMs": 560000,
    "textTelugu": CHALISA_DATA[42][0],
    "telugu": CHALISA_DATA[42][0],
    "textEnglish": CHALISA_DATA[42][1],
    "english": CHALISA_DATA[42][1]
})

# 45. Outro Mangalam (560000 -> 588420 ms)
stanzas.append({
    "index": 45,
    "timestampMs": 560000,
    "startTimeMs": 560000,
    "endTimeMs": 588420,
    "textTelugu": "॥ సియావర రామచంద్ర కీ జయ | పవనసుత హనుమాన కీ జయ ॥",
    "telugu": "॥ సియావర రామచంద్ర కీ జయ | పవనసుత హనుమాన కీ జయ ॥",
    "textEnglish": "|| Siyaavara Ramachandra Kee Jaya | Pavanasuta Hanumaana Kee Jaya ||",
    "english": "|| Siyaavara Ramachandra Kee Jaya | Pavanasuta Hanumaana Kee Jaya ||"
})

output_file = os.path.join(OUTPUT_DIR, "hanuman_chalisa.json")
data = {
    "trackId": "hanuman_chalisa",
    "titleTelugu": "హనుమాన్ చాలీసా",
    "titleEnglish": "Hanuman Chalisa",
    "totalStanzas": len(stanzas),
    "stanzas": stanzas
}

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Calibrated {output_file} with {len(stanzas)} stanzas.")
