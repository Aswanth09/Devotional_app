# -*- coding: utf-8 -*-
"""
Calibrated generator for Govinda Namalu lyrics JSON.
Chant begins immediately from 0 ms and flows continuously across 745430 ms.
"""
import json
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "app", "src", "main", "assets", "lyrics")
os.makedirs(OUTPUT_DIR, exist_ok=True)

GOVINDA_NAMES = [
    ("శ్రీ శ్రీనివాస గోవిందా | శ్రీ వేంకటేశ గోవిందా", "Shree Shreenivaasa Govinda | Shree Venkatesha Govinda"),
    ("భక్తవత్సల గోవిందా | భాగవతప్రియ గోవిందా", "Bhaktavatsala Govinda | Bhaagavatapriya Govinda"),
    ("నిత్య నిర్మల గోవిందా | నీలమేఘశ్యామ గోవిందా", "Nitya Nirmala Govinda | Neelameghashyaama Govinda"),
    ("పురాణ పురుష గోవిందా | పుండరీకాక్ష గోవిందా", "Puraana Purusha Govinda | Pundareekaaksha Govinda"),
    ("నందనందన గోవిందా | నవనీత చోర గోవిందా", "Nandanandana Govinda | Navaneeta Chora Govinda"),
    ("పశుపాలక గోవిందా | పాపవిమోచన గోవిందా", "Pashupaalaka Govinda | Paapavimochana Govinda"),
    ("దుష్టసంహార గోవిందా | దురితనివారణ గోవిందా", "Dushtasamhaara Govinda | Duritanivaarana Govinda"),
    ("శిష్టపరిపాలక గోవిందా | కష్టనివారణ గోవిందా", "Shishtaparipaalaka Govinda | Kashtanivaarana Govinda"),
    ("వజ్రకవచధర గోవిందా | వైకుంఠవాస గోవిందా", "Vajrakavachadhara Govinda | Vaikunthavaasa Govinda"),
    ("వసుదేవ తనయ గోవిందా | వాసుదేవ గోవిందా", "Vasudeva Tanaya Govinda | Vaasudeva Govinda"),
    ("బిల్వపత్రప్రియ గోవిందా | భిక్షుక సంస్తుత గోవిందా", "Bilvapatrapriya Govinda | Bhikshuka Samstuta Govinda"),
    ("తులసీవనమాలి గోవిందా | దోషనివారణ గోవిందా", "Tulaseevanamaali Govinda | Doshanivaarana Govinda"),
    ("శేషసాయి గోవిందా | శేషాద్రి నిలయ గోవిందా", "Sheshasaayi Govinda | Sheshaadri Nilaya Govinda"),
    ("శ్రీనికేతన గోవిందా | జగద్వంద్య గోవిందా", "Shreeniketana Govinda | Jagadvandya Govinda"),
    ("అనాథ రక్షక గోవిందా | ఆపద్భాంధవ గోవిందా", "Anaatha Rakshaka Govinda | Aapadbaandhava Govinda"),
    ("శరణాగతవత్సల గోవిందా | కరుణాసాగర గోవిందా", "Sharanaagatavatsala Govinda | Karunaasaagara Govinda"),
    ("కమలదళాక్ష గోవిందా | కామితఫలదాత గోవిందా", "Kamaladalaaksha Govinda | Kaamitaphaladaata Govinda"),
    ("పాపవినాశన గోవిందా | పద్మనాభ గోవిందా", "Paapavinaashana Govinda | Padmanaabha Govinda"),
    ("నారాయణ గోవిందా | శ్రీమన్నారాయణ గోవిందా", "Naaraayana Govinda | Shreeman Naaraayana Govinda"),
    ("శంఖచక్రధర గోవిందా | శార్ఙ్గధనుర్ధర గోవిందా", "Shankha Chakra Dhara Govinda | Shaarnga Dhanurdhara Govinda"),
    ("గరుడవాహన గోవిందా | గోపికాలోల గోవిందా", "Garudavaahana Govinda | Gopikaalola Govinda"),
    ("గోవర్ధనోద్ధార గోవిందా | గోకులరక్షక గోవిందా", "Govardhanoddhaara Govinda | Gokularakshaka Govinda"),
    ("దశరథనందన గోవిందా | దశముఖ మర్దన గోవిందా", "Dasharathanandana Govinda | Dashamukha Mardana Govinda"),
    ("జానకీవల్లభ గోవిందా | లక్ష్మణాగ్రజ గోవిందా", "Jaanakeevallabha Govinda | Lakshmanaagraja Govinda"),
    ("మత్స్యకూర్మ గోవిందా | వరాహనారసింహ గోవిందా", "Matsya Koorma Govinda | Varaaha Naarasimha Govinda"),
    ("వామనభార్గవ గోవిందా | బలరామానుజ గోవిందా", "Vaamana Bhaargava Govinda | Balaramaanunja Govinda"),
    ("బౌద్ధకల్కి గోవిందా | వేణుగానలోల గోవిందా", "Bauddha Kalki Govinda | Venugaanalola Govinda"),
    ("కాళింగమర్దన గోవిందా | కంసనిషూదన గోవిందా", "Kaalingamardana Govinda | Kamsanishoodana Govinda"),
    ("గజేంద్రరక్షక గోవిందా | ప్రహ్లాదపోషక గోవిందా", "Gajendrarakshaka Govinda | Prahlaadaposshaka Govinda"),
    ("ద్రౌపదీరక్షక గోవిందా | కుచేలవరద గోవిందా", "Draupadeerakshaka Govinda | Kuchelavarada Govinda"),
    ("రుక్మిణీలోల గోవిందా | సత్యభామాప్రియ గోవిందా", "Rukmineelola Govinda | Satyabhaamaapriya Govinda"),
    ("శ్రీరాధాప్రియ గోవిందా | రాసవిహారి గోవిందా", "Shreeraadhaapriya Govinda | Raasavihaari Govinda"),
    ("కల్పవృక్ష గోవిందా | కామధేను గోవిందా", "Kalpavriksha Govinda | Kaamadhenu Govinda"),
    ("చింతామణి గోవిందా | జ్ఞానప్రదాయక గోవిందా", "Chintaamani Govinda | Gyaanapradaayaka Govinda"),
    ("ఆనందరూప గోవిందా | మోక్షదాయక గోవిందా", "Aanandaroopa Govinda | Mokshadaayaka Govinda"),
    ("పరమపావన గోవిందా | పరంధామ గోవిందా", "Paramapaavana Govinda | Paramdhaama Govinda"),
    ("తిరుమలవాస గోవిందా | తిరుపతి నిలయ గోవిందా", "Tirumalavaasa Govinda | Tirupati Nilaya Govinda"),
    ("ఏడుకొండలవాడ గోవిందా | ఎకభోగప్రదాత గోవిందా", "Edu Kondalavaada Govinda | Ekabhogapradaata Govinda"),
    ("అఖిలాండకోటి గోవిందా | బ్రహ్మాండనాయక గోవిందా", "Akhilaandakoti Govinda | Brahmaandanaayaka Govinda"),
    ("శ్రీపద్మావతీప్రియ గోవిందా | శ్రీ వేంకటేశ్వర గోవిందా", "Shreepadmaavateepriya Govinda | Shree Venkateshvara Govinda"),
    ("గోవిందా హరి గోవిందా | వేంకటరమణ గోవిందా", "Govinda Hari Govinda | Venkataramana Govinda"),
    ("శ్రీనివాస గోవిందా | శ్రీ వేంకటేశ గోవిందా", "Shreenivaasa Govinda | Shree Venkatesha Govinda"),
    ("భక్తప్రియ గోవిందా | భవహరణ గోవిందా", "Bhaktapriya Govinda | Bhavaharana Govinda"),
    ("శాంతమూర్తి గోవిందా | శాంతిప్రదాత గోవిందా", "Shaantamoorati Govinda | Shaantipradaata Govinda"),
    ("దయానిధే గోవిందా | ధర్మరక్షక గోవిందా", "Dayaanidhe Govinda | Dharmarakshaka Govinda"),
    ("సత్యస్వరూప గోవిందా | సర్వేశ్వర గోవిందా", "Satyasvaroopa Govinda | Sarveshvara Govinda"),
    ("విశ్వరూప గోవిందా | విభుధవరద గోవిందా", "Vishvaroopa Govinda | Vibhudhavarada Govinda"),
    ("మురళీధర గోవిందా | మోహనరూప గోవిందా", "Muralheedhara Govinda | Mohanaroopa Govinda"),
    ("హరిహరనాథ గోవిందా | హృదయనివాస గోవిందా", "Hariharanaatha Govinda | Hridayanivaasa Govinda"),
    ("శ్రీధర గోవిందా | శ్రీపతి గోవిందా", "Shreedhara Govinda | Shreepati Govinda"),
    ("మాధవ గోవిందా | ముకుంద గోవిందా", "Maadhava Govinda | Mukunda Govinda"),
    ("కేశవ గోవిందా | జనార్దన గోవిందా", "Keshava Govinda | Janaardana Govinda"),
    ("అచ్యుత గోవిందా | అనంత గోవిందా", "Achyuta Govinda | Ananta Govinda"),
    ("వామన గోవిందా | దామోదర గోవిందా", "Vaamana Govinda | Daamodara Govinda"),
    ("మధుసూదన గోవిందా | త్రివిక్రమ గోవిందా", "Madhusoodana Govinda | Trivikrama Govinda"),
    ("హృషీకేశ గోవిందా | శ్రీరంగనాథ గోవిందా", "Hrisheekesha Govinda | Shreeranganaatha Govinda"),
    ("వెంకటరమణ గోవిందా | శంఖచక్రధర గోవిందా", "Venkataramana Govinda | Shankhachakradhara Govinda"),
    ("గోవిందా హరి గోవిందా | వేంకటరమణ గోవిందా", "Govinda Hari Govinda | Venkataramana Govinda")
]

stanzas = []

# Immediate start
start_base = 0
end_base = 715000
name_dur = (end_base - start_base) / float(len(GOVINDA_NAMES))

for i, (tel, eng) in enumerate(GOVINDA_NAMES):
    s_ms = int(round(start_base + i * name_dur))
    e_ms = int(round(start_base + (i + 1) * name_dur))
    stanzas.append({
        "index": i + 1,
        "timestampMs": s_ms,
        "startTimeMs": s_ms,
        "endTimeMs": e_ms,
        "textTelugu": tel,
        "telugu": tel,
        "textEnglish": eng,
        "english": eng
    })

# Mangalam
stanzas.append({
    "index": len(stanzas) + 1,
    "timestampMs": 715000,
    "startTimeMs": 715000,
    "endTimeMs": 745430,
    "textTelugu": "॥ మంగళ హారతి ॥\nగోవిందా హరి గోవిందా | వేంకటరమణ గోవిందా |\nశ్రీనివాసా గోవిందా | తిరుమలవాసా గోవిందా ||",
    "telugu": "॥ మంగళ హారతి ॥\nగోవిందా హరి గోవిందా | వేంకటరమణ గోవిందా |\nశ్రీనివాసా గోవిందా | తిరుమలవాసా గోవిందా ||",
    "textEnglish": "|| Mangala Harati ||\nGovinda Hari Govinda | Venkataramana Govinda |\nShreenivaasaa Govinda | Tirumalavaasaa Govinda ||",
    "english": "|| Mangala Harati ||\nGovinda Hari Govinda | Venkataramana Govinda |\nShreenivaasaa Govinda | Tirumalavaasaa Govinda ||"
})

output_file = os.path.join(OUTPUT_DIR, "govinda_namalu.json")
data = {
    "trackId": "govinda_namalu",
    "titleTelugu": "గోవింద నామాలు",
    "titleEnglish": "Govinda Namalu",
    "totalStanzas": len(stanzas),
    "stanzas": stanzas
}

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Calibrated {output_file} with {len(stanzas)} stanzas.")
