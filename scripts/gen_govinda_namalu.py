# -*- coding: utf-8 -*-
"""
Full-Coverage Generator for Sri Govinda Namalu lyrics JSON.
Covers the entire 12:25 audio (745430 ms) from 0 ms to conclusion:
- 0 -> 12000 ms: Invocatory Harati
- 12000 -> 648000 ms: 108 Sacred Govinda Namavali Stanzas (~5888.89 ms each)
- 648000 -> 672000 ms: Govinda Nama Phalasruti Shlokam
- 672000 -> 696000 ms: Sri Venkateswara Dhyana & Sharanagati
- 696000 -> 720000 ms: Sri Venkateswara Mangalashasanam
- 720000 -> 745430 ms: Concluding Maha Mangala Harati
"""
import json
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "app", "src", "main", "assets", "lyrics")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 108 Namavali pairs
GOVINDA_108_NAMES = [
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
    ("గోవిందా హరి గోవిందా | వేంకటరమణ గోవిందా", "Govinda Hari Govinda | Venkataramana Govinda"),
    ("క్షీరాబ్ధిశయన గోవిందా | శేషశయన గోవిందా", "Ksheeraabdhishayana Govinda | Sheshashayana Govinda"),
    ("గరుడధ్వజ గోవిందా | నరహరిరూప గోవిందా", "Garudadhvaja Govinda | Narahariroopa Govinda"),
    ("పట్టాభిరామ గోవిందా | పరంధామ గోవిందా", "Pattaabhiraama Govinda | Paramdhaama Govinda"),
    ("జగదోద్ధార గోవిందా | జలజనాభ గోవిందా", "Jagadoddhaara Govinda | Jalajanaabha Govinda"),
    ("దీనబంధో గోవిందా | దీనరక్షక గోవిందా", "Deenabandho Govinda | Deenarakshaka Govinda"),
    ("భక్తరక్షక గోవిందా | భవభయనాశక గోవిందా", "Bhaktarakshaka Govinda | Bhavabhayanaashaka Govinda"),
    ("వేంకటాచలనికేతన గోవిందా | విఘ్ననాశక గోవిందా", "Venkataachalaniketana Govinda | Vighnanaashaka Govinda"),
    ("పరమానంద గోవిందా | పద్మనయన గోవిందా", "Paramaananda Govinda | Padmanayana Govinda"),
    ("దివ్యరూప గోవిందా | దీనదయాల గోవిందా", "Divyaroopa Govinda | Deenadayaala Govinda"),
    ("సుప్రసన్న గోవిందా | సర్వోత్తమ గోవిందా", "Suprasanna Govinda | Sarvottama Govinda"),
    ("భక్తచింతామణి గోవిందా | భక్తవర్ధన గోవిందా", "Bhaktachintaamani Govinda | Bhaktavardhana Govinda"),
    ("కళ్యాణ శ్రీనివాస గోవిందా | కరుణారససింధు గోవిందా", "Kalyaana Shreenivaasa Govinda | Karunaarasasindhu Govinda"),
    ("మంగళప్రదాత గోవిందా | మహనీయగుణధామ గోవిందా", "Mangalapradaata Govinda | Mahaneeyagunadhaama Govinda"),
    ("సర్వలోకనాథ గోవిందా | సర్వసుఖప్రదాత గోవిందా", "Sarvalokanaatha Govinda | Sarvasukhapradaata Govinda"),
    ("జగన్నాథ గోవిందా | జనార్దనరూప గోవిందా", "Jagannaatha Govinda | Janaardanaroopa Govinda"),
    ("వేంకటేశ గోవిందా | వృషభాద్రివాస గోవిందా", "Venkatesha Govinda | Vrishabhaadrivaasa Govinda"),
    ("ఆనందసింధు గోవిందా | ఆశ్రితవత్సల గోవిందా", "Aanandasindhu Govinda | Aashritavatsala Govinda"),
    ("పద్మావతీ మనోహర గోవిందా | పరతత్వస్వరూప గోవిందా", "Padmaavatee Manohara Govinda | Paratatvasvaroopa Govinda"),
    ("కోటి సూర్యప్రకాశ గోవిందా | చంద్రముఖ గోవిందా", "Koti Sooryaprakaasha Govinda | Chandramukha Govinda"),
    ("ఆనందవర్ధన గోవిందా | ఆపదుద్ధార గోవిందా", "Aanandavardhana Govinda | Aapaduddhaara Govinda"),
    ("వైకుంఠనాథ గోవిందా | వరప్రదాత గోవిందా", "Vaikunthanaatha Govinda | Varapradaata Govinda"),
    ("భక్తపోషక గోవిందా | భవబంధవిమోచన గోవిందా", "Bhaktaposhaka Govinda | Bhavabandhavimochana Govinda"),
    ("సద్గతిస్వరూప గోవిందా | సర్వపూజిత గోవిందా", "Sadgatisvaroopa Govinda | Sarvapoojita Govinda"),
    ("వేంకటరమణ గోవిందా | సంకటనాశన గోవిందా", "Venkataramana Govinda | Sankatanaashana Govinda"),
    ("ఏడుకొండలవాడ గోవిందా | గోవిందా గోవిందా", "Edu Kondalavaada Govinda | Govinda Govinda"),
    ("అనాథరక్షక గోవిందా | గోవిందా గోవిందా", "Anaatharakshaka Govinda | Govinda Govinda"),
    ("ఆపద్బాంధవ గోవిందా | గోవిందా గోవిందా", "Aapadbaandhava Govinda | Govinda Govinda"),
    ("భక్తవత్సల గోవిందా | గోవిందా గోవిందా", "Bhaktavatsala Govinda | Govinda Govinda"),
    ("శ్రీ వేంకటేశ్వర గోవిందా | గోవిందా గోవిందా", "Shree Venkateshvara Govinda | Govinda Govinda"),
    ("తిరుమలవాస గోవిందా | గోవిందా గోవిందా", "Tirumalavaasa Govinda | Govinda Govinda"),
    ("గోవిందా హరి గోవిందా | వేంకటరమణ గోవిందా", "Govinda Hari Govinda | Venkataramana Govinda"),
    ("శ్రీనివాసా గోవిందా | శ్రీ వేంకటేశా గోవిందా", "Shreenivaasaa Govinda | Shree Venkateshaa Govinda"),
    ("భక్తపోషక గోవిందా | పరంధామ గోవిందా", "Bhaktaposhaka Govinda | Paramdhaama Govinda"),
    ("నిత్యనిర్మల గోవిందా | పరమాత్మా గోవిందా", "Nityanirmala Govinda | Paramaatmaa Govinda"),
    ("సర్వసమర్థ గోవిందా | సర్వేశ్వర గోవిందా", "Sarvasamartha Govinda | Sarveshvara Govinda"),
    ("మురళీగానలోల గోవిందా | మోహనకృష్ణ గోవిందా", "Muralheegaanalola Govinda | Mohanakrishna Govinda"),
    ("రాధామాధవ గోవిందా | రాసవిహారి గోవిందా", "Raadhaamaadhava Govinda | Raasavihaari Govinda"),
    ("శ్రీరంగనాథ గోవిందా | శేషాచలవాస గోవిందా", "Shreeranganaatha Govinda | Sheshaachalavaasa Govinda"),
    ("కరుణానిధే గోవిందా | కమలనాభ గోవిందా", "Karunaanidhe Govinda | Kamalanaabha Govinda"),
    ("వేంకటనాథ గోవిందా | వేదాంతవేద్య గోవిందా", "Venkatanaatha Govinda | Vedaantavedya Govinda"),
    ("అఖిలభూపాల గోవిందా | అవ్యయమూర్తి గోవిందా", "Akhilabhoopaala Govinda | Avyayamoorati Govinda"),
    ("జ్ఞానస్వరూప గోవిందా | జగద్రక్షక గోవిందా", "Gyaanasvaroopa Govinda | Jagadrakshaka Govinda"),
    ("గోవిందా హరి గోవిందా | వేంకటరమణ గోవిందా", "Govinda Hari Govinda | Venkataramana Govinda"),
    ("శ్రీ శ్రీనివాస గోవిందా | శ్రీ వేంకటేశ గోవిందా", "Shree Shreenivaasa Govinda | Shree Venkatesha Govinda"),
    ("ఏడుకొండలవాడ వెంకటరమణా | గోవిందా గోవిందా", "Edu Kondalavaada Venkataramanaa | Govinda Govinda"),
    ("ఆపద్బాంధవా అనాథరక్షకా | గోవిందా గోవిందా", "Aapadbaandhavaa Anaatharakshakaa | Govinda Govinda"),
    ("భక్తవత్సలా తిరుమలవాసా | గోవిందా గోవిందా", "Bhaktavatsalaa Tirumalavaasaa | Govinda Govinda"),
    ("గోవిందా హరి గోవిందా | వేంకటరమణ గోవిందా", "Govinda Hari Govinda | Venkataramana Govinda")
]

stanzas = []

# 1. Invocatory Opening Harati (0 -> 12000 ms)
stanzas.append({
    "index": 1,
    "timestampMs": 0,
    "startTimeMs": 0,
    "endTimeMs": 12000,
    "textTelugu": "॥ శ్రీ వేంకటేశ్వర గోవింద నామావళిః - ఆరంభమ్ ॥\nశ్రీ శ్రీనివాస గోవిందా | శ్రీ వేంకటేశ గోవిందా |\nభక్తవత్సల గోవిందా | భాగవతప్రియ గోవిందా ||",
    "telugu": "॥ శ్రీ వేంకటేశ్వర గోవింద నామావళిః - ఆరంభమ్ ॥\nశ్రీ శ్రీనివాస గోవిందా | శ్రీ వేంకటేశ గోవిందా |\nభక్తవత్సల గోవిందా | భాగవతప్రియ గోవిందా ||",
    "textEnglish": "|| Sri Venkateshwara Govinda Namavali - Opening ||\nShree Shreenivaasa Govinda | Shree Venkatesha Govinda |\nBhaktavatsala Govinda | Bhaagavatapriya Govinda ||",
    "english": "|| Sri Venkateshwara Govinda Namavali - Opening ||\nShree Shreenivaasa Govinda | Shree Venkatesha Govinda |\nBhaktavatsala Govinda | Bhaagavatapriya Govinda ||"
})

# 2. 108 Sacred Govinda Namas (12000 -> 648000 ms, ~5888.89 ms each)
start_names = 12000
end_names = 648000
dur_per_name = (end_names - start_names) / float(len(GOVINDA_108_NAMES))

for i, (tel, eng) in enumerate(GOVINDA_108_NAMES):
    s_ms = int(round(start_names + i * dur_per_name))
    e_ms = int(round(start_names + (i + 1) * dur_per_name))
    stanzas.append({
        "index": 2 + i,
        "timestampMs": s_ms,
        "startTimeMs": s_ms,
        "endTimeMs": e_ms,
        "textTelugu": f"{i+1}. {tel}",
        "telugu": f"{i+1}. {tel}",
        "textEnglish": f"{i+1}. {eng}",
        "english": f"{i+1}. {eng}"
    })

# 3. Phala-Sruti Shlokam (648000 -> 672000 ms)
stanzas.append({
    "index": len(stanzas) + 1,
    "timestampMs": 648000,
    "startTimeMs": 648000,
    "endTimeMs": 672000,
    "textTelugu": "॥ గోవింద నామ ఫలశ్రుతిః ॥\nగోవింద నామ సంకీర్తనం సర్వపాప నివారణమ్ |\nసర్వకామప్రదం పుణ్యం శ్రీనివాస ప్రసాదకమ్ ||\nజన్మమృత్యుజరావ్యాధి భయహృత్ భక్తిదాయకమ్ ||",
    "telugu": "॥ గోవింద నామ ఫలశ్రుతిః ॥\nగోవింద నామ సంకీర్తనం సర్వపాప నివారణమ్ |\nసర్వకామప్రదం పుణ్యం శ్రీనివాస ప్రసాదకమ్ ||\nజన్మమృత్యుజరావ్యాధి భయహృత్ భక్తిదాయకమ్ ||",
    "textEnglish": "|| Govinda Nama Phalasruti ||\nGovinda Naama Samkeertanam Sarvapaapa Nivaaranam |\nSarvakaamapradam Punyam Shreenivaasa Prasaadakam ||\nJanmamrityujaraavyaadhi Bhayahrit Bhaktidaayakam ||",
    "english": "|| Govinda Nama Phalasruti ||\nGovinda Naama Samkeertanam Sarvapaapa Nivaaranam |\nSarvakaamapradam Punyam Shreenivaasa Prasaadakam ||\nJanmamrityujaraavyaadhi Bhayahrit Bhaktidaayakam ||"
})

# 4. Sri Venkateswara Sharanagati & Dhyana Slokas (672000 -> 696000 ms)
stanzas.append({
    "index": len(stanzas) + 1,
    "timestampMs": 672000,
    "startTimeMs": 672000,
    "endTimeMs": 696000,
    "textTelugu": "॥ శ్రీ వేంకటేశ్వర శరణాగతి శ్లోకమ్ ॥\nవినా వేంకటేశం న నాథో న నాథః సదా వేంకటేశం స్మరామి స్మరామి |\nహరే వేంకటేశ ప్రసీద ప్రసీద ప్రియం వేంకటేశ ప్రయచ్ఛ ప్రయచ్ఛ ||\nశ్రీ వేంకటాచలాధీశం శ్రీయాధ్యాసిత వక్షసమ్ | శ్రితచేతన మందారం శ్రీనివాసమహం భజే ||",
    "telugu": "॥ శ్రీ వేంకటేశ్వర శరణాగతి శ్లోకమ్ ॥\nవినా వేంకటేశం న నాథో న నాథః సదా వేంకటేశం స్మరామి స్మరామి |\nహరే వేంకటేశ ప్రసీద ప్రసీద ప్రియం వేంకటేశ ప్రయచ్ఛ ప్రయచ్ఛ ||\nశ్రీ వేంకటాచలాధీశం శ్రీయాధ్యాసిత వక్షసమ్ | శ్రితచేతన మందారం శ్రీనివాసమహం భజే ||",
    "textEnglish": "|| Sri Venkateswara Sharanagati Shlokam ||\nVinaa Venkatesham Na Naatho Na Naathah Sadaa Venkatesham Smaraami Smaraami |\nHare Venkatesha Praseeda Praseeda Priyam Venkatesha Prayachha Prayachha ||\nShree Venkataachalaadheesham Shreyaadhyaasita Vakshasam | Shritachetana Mandaaram Shreenivaasamaham Bhaje ||",
    "english": "|| Sri Venkateswara Sharanagati Shlokam ||\nVinaa Venkatesham Na Naatho Na Naathah Sadaa Venkatesham Smaraami Smaraami |\nHare Venkatesha Praseeda Praseeda Priyam Venkatesha Prayachha Prayachha ||\nShree Venkataachalaadheesham Shreyaadhyaasita Vakshasam | Shritachetana Mandaaram Shreenivaasamaham Bhaje ||"
})

# 5. Sri Venkateswara Mangalashasanam (696000 -> 720000 ms)
stanzas.append({
    "index": len(stanzas) + 1,
    "timestampMs": 696000,
    "startTimeMs": 696000,
    "endTimeMs": 720000,
    "textTelugu": "॥ శ్రీ వేంకటేశ్వర మంగళా శాసనమ్ ॥\nశ్రియః కాంతాయ కళ్యాణనిధయే నిధయేఽర్థినామ్ |\nశ్రీవేంకటనివాసాయ శ్రీనివాసాయ మంగళమ్ ||\nమంగళం కోసలేంద్రాయ మహనీయ గుణాత్మనే |\nచక్రవర్తి తనూజాయ సార్వభౌమాయ మంగళమ్ ||",
    "telugu": "॥ శ్రీ వేంకటేశ్వర మంగళా శాసనమ్ ॥\nశ్రియః కాంతాయ కళ్యాణనిధయే నిధయేఽర్థినామ్ |\nశ్రీవేంకటనివాసాయ శ్రీనివాసాయ మంగళమ్ ||\nమంగళం కోసలేంద్రాయ మహనీయ గుణాత్మనే |\nచక్రవర్తి తనూజాయ సార్వభౌమాయ మంగళమ్ ||",
    "textEnglish": "|| Sri Venkateswara Mangalashasanam ||\nShriyah Kaantaaya Kalyaananidhaye Nidhaye'rthinaam |\nShreevenkatanivaasaaya Shreenivaasaaya Mangalam ||\nMangalam Kosalendraaya Mahaneeya Gunaatmane |\nChakravarti Tanoojaaya Saarvabhaumaaya Mangalam ||",
    "english": "|| Sri Venkateswara Mangalashasanam ||\nShriyah Kaantaaya Kalyaananidhaye Nidhaye'rthinaam |\nShreevenkatanivaasaaya Shreenivaasaaya Mangalam ||\nMangalam Kosalendraaya Mahaneeya Gunaatmane |\nChakravarti Tanoojaaya Saarvabhaumaaya Mangalam ||"
})

# 6. Concluding Maha Mangala Harati & Jayam (720000 -> 745430 ms)
stanzas.append({
    "index": len(stanzas) + 1,
    "timestampMs": 720000,
    "startTimeMs": 720000,
    "endTimeMs": 745430,
    "textTelugu": "॥ సర్వ మంగళ హారతి - గోవింద నామ సంకీర్తనం సంపూర్ణమ్ ॥\nగోవిందా హరి గోవిందా | వేంకటరమణ గోవిందా |\nశ్రీనివాసా గోవిందా | తిరుమలవాసా గోవిందా ||\nసర్వే జనాః సుఖినో భవంతు | సమస్త సన్మంగళాని భవంతు ||",
    "telugu": "॥ సర్వ మంగళ హారతి - గోవింద నామ సంకీర్తనం సంపూర్ణమ్ ॥\nగోవిందా హరి గోవిందా | వేంకటరమణ గోవిందా |\nశ్రీనివాసా గోవిందా | తిరుమలవాసా గోవిందా ||\nసర్వే జనాః సుఖినో భవంతు | సమస్త సన్మంగళాని భవంతు ||",
    "textEnglish": "|| Sarva Mangala Harati - Govinda Namavali Complete ||\nGovinda Hari Govinda | Venkataramana Govinda |\nShreenivaasaa Govinda | Tirumalavaasaa Govinda ||\nSarve Janaah Sukhino Bhavantu | Samasta Sanmangalaani Bhavantu ||",
    "english": "|| Sarva Mangala Harati - Govinda Namavali Complete ||\nGovinda Hari Govinda | Venkataramana Govinda |\nShreenivaasaa Govinda | Tirumalavaasaa Govinda ||\nSarve Janaah Sukhino Bhavantu | Samasta Sanmangalaani Bhavantu ||"
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

print(f"Calibrated {output_file} with {len(stanzas)} stanzas spanning 0 ms to 745430 ms (12:25).")
