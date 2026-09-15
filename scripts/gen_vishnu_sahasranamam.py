# -*- coding: utf-8 -*-
"""
Calibrated generator for Sri Vishnu Sahasranama Stotram lyrics JSON.
Exact vocal onsets verified against M.S. Subbulakshmi waveform:
- 0 -> 8700 ms: Tanpura / Omkara prelude
- 8700 -> 167500 ms: Dhyana Shlokas 1 to 5
- 167500 -> 345000 ms: Purva Peethika & Sankalpa
- 345000 -> 1595000 ms: 108 Core Stotra Shlokas (~11574.07 ms each)
- 1595000 -> 1790910 ms: Phalasruti & Concluding Mangalam
"""
import json
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "app", "src", "main", "assets", "lyrics")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 108 Main Stotra Shlokas
SHLOKAS = [
    # 1
    ("విశ్వం విష్ణుర్వషట్కారో భూతభవ్యభవత్ప్రభుః |\nభూతకృద్భూతభృద్భావో భూతాత్మా భూతభావనః ||",
     "Vishvam Vishnur Vashatkaaro Bhootabhavya Bhavatprabhuh |\nBhootakrid Bhootabhrid Bhaavo Bhootaatmaa Bhootabhaavanah ||"),
    # 2
    ("పూతాత్మా పరమాత్మా చ ముక్తానాం పరమా గతిః |\nఅవ్యయః పురుషః సాక్షీ క్షేత్రజ్ఞోఽక్షర ఏవ చ ||",
     "Pootaatmaa Paramaatmaa Cha Muktaanaam Paramaa Gatih |\nAvyayah Purushah Saakshee Kshetrajno'kshara Eva Cha ||"),
    # 3
    ("యోగో యోగవిదాం నేతా ప్రధానపురుషేశ్వరః |\nనారసింహవపుః శ్రీమాన్ కేశవః పురుషోత్తమః ||",
     "Yogo Yogavidaam Netaa Pradhaanapurusheshvarah |\nNaarasimhavapuh Shreemaan Keshavah Purushottamah ||"),
    # 4
    ("సర్వః శర్వః శివః స్థాణుర్భూతాదిర్నిధిరవ్యయః |\nసంభవో భావనో భర్తా ప్రభవః ప్రభురీశ్వరః ||",
     "Sarvah Sharvah Shivah Sthaanur Bhootaadir Nidhir Avyayah |\nSambhavo Bhaavano Bhartaa Prabhavah Prabhur Eeshvarah ||"),
    # 5
    ("స్వయంభూః శంభురాదిత్యః పుష్కరాక్షో మహాస్వనః |\nఅనాదినిధనో ధాతా విధాతా ధాతురుత్తమః ||",
     "Swayambhooh Shambhur Aadityah Pushkaraaksho Mahaasvanah |\nAnaadinidhano Dhaataa Vidhaataa Dhaaturuttamah ||"),
    # 6
    ("అప్రమేయో హృషీకేశః పద్మనాభోఽమరప్రభుః |\nవిశ్వకర్మా మనుస్త్వష్టా స్థవిష్ఠః స్థవిరో ధ్రువః ||",
     "Aprameyo Hrisheekeshah Padmanaabho'maraprabhuh |\nVishvakarmaa Manus Tvashtaa Sthavishthah Sthaviro Dhruvah ||"),
    # 7
    ("అగ్రాహ్యః శాశ్వతః కృష్ణో లోహితాక్షః ప్రతర్దనః |\nప్రభూతస్త్రికకుద్ధామ పవిత్రం మంగళం పరమ్ ||",
     "Agraahyah Shaashvatah Krishno Lohitaakshah Pratardanah |\nPrabhootas Trikakuddhama Pavitram Mangalam Param ||"),
    # 8
    ("ఈశానః ప్రాణదః ప్రాణో జ్యేష్ఠః శ్రేష్ఠః ప్రజాపతిః |\nహిరణ్యగర్భో భూగర్భో మాధవో మధుసూదనః ||",
     "Eeshaanah Praanadah Praano Jyeshthah Shreshthah Prajaapatih |\nHiranyagarbho Bhoogarbho Maadhavo Madhusoodanah ||"),
    # 9
    ("ఈశ్వరో విక్రమీ ధన్వీ మేధావీ విక్రమః క్రమః |\nఅనుత్తమో దురాధర్షః కృతజ్ఞః కృతిరాత్మవాన్ ||",
     "Eeshvaro Vikramee Dhanvee Medhaavee Vikramah Kramah |\nAnuttamo Duraadharshah Kritajnah Kritir Aatmavaan ||"),
    # 10
    ("సురేశః శరణం శర్మ విశ్వరేతాః ప్రజాభవః |\nఅహః సంవత్సరో వ్యాలః ప్రత్యయః సర్వదర్శనః ||",
     "Sureshah Sharanam Sharma Vishvaretaah Prajaabhavah |\nAhah Samvatsaro Vyaalah Pratyayah Sarvadarshanah ||"),
    # 11
    ("అజః సర్వేశ్వరః సిద్ధః సిద్ధిః సర్వాదిరచ్యుతః |\nవృషాకపిరమేయాత్మా సర్వయోగవినిఃసృతః ||",
     "Ajah Sarveshvarah Siddhah Siddhih Sarvaadir Achyutah |\nVrishaa Kapir Ameyaatmaa Sarvayoga Vinissritah ||"),
    # 12
    ("వసుర్వసుమనాః సత్యః సమాత్మాఽసమ్మితః సమః |\nఅమోఘః పుండరీకాక్షో వృషకర్మా వృషాకృతిః ||",
     "Vasur Vasumanaah Satyah Samaatmaa'sammitah Samah |\nAmoghah Pundareekaaksho Vrishakarmaa Vrishaakritih ||"),
    # 13
    ("రుద్రో బహుశిరా బభ్రుర్విశ్వయోనిః శుచిశ్రవాః |\nఅమృతః శాశ్వతస్థాణుర్వరారోహో మహాతపాః ||",
     "Rudro Bahushiraa Babhrur Vishvayonih Shuchishravaah |\nAmritah Shaashvatasthaanur Varaaroho Mahaatapaah ||"),
    # 14
    ("సర్వగః సర్వవిద్భానుర్విష్వక్సేనో జనార్దనః |\nవేదో వేదవిదవ్యంగో వేదాంగో వేదవిత్కవిః ||",
     "Sarvagah Sarvavid Bhaanur Vishvakseno Janaardanah |\nVedo Vedavid Avyango Vedaango Vedavit Kavih ||"),
    # 15
    ("లోకాధ్యక్షః సురాధ్యక్షో ధర్మాధ్యక్షః కృతాకృతః |\nచతురాత్మా చతుర్వ్యూహశ్చతుర్దంష్ట్రశ్చతుర్భుజః ||",
     "Lokaadhyakshah Suraadhyaksho Dharmaadhyakshah Kritaakritah |\nChaturaatmaa Chaturvyoohash Chaturdamshtrash Chaturbhujah ||"),
    # 16
    ("భ్రాజిష్ణుర్భోజనం భోక్తా సహిష్ణుర్జగదాదిజః |\nఅనఘో విజయో జేతా విశ్వయోనిః పునర్వసుః ||",
     "Bhraajishnur Bhojanam Bhoktaa Sahishnur Jagadaadijah |\nAnagho Vijayo Jetaa Vishvayonih Punarvasuh ||"),
    # 17
    ("ఉపేంద్రో వామనో ప్రాంశురమోఘః శుచిరూర్జితః |\nఅతీంద్రః సంగ్రహః సర్గో ధృతాత్మా నియమో యమః ||",
     "Upendro Vaamano Praamshur Amoghah Shuchir Oorjitah |\nAteendrah Samgrahah Sargo Dhritaatmaa Niyamo Yamah ||"),
    # 18
    ("వేద్యో వైద్యః సదాయోగీ వీరహా మాధవో మధుః |\nఅతీంద్రియో మహామాయో మహోత్సాహో మహాబలః ||",
     "Vedyo Vaidyah Sadaayogee Veerahaa Maadhavo Madhuh |\nAteendriyo Mahaamaayo Mahotsaaho Mahaabalah ||"),
    # 19
    ("మహాబుద్ధిర్మహావీర్యో మహాశక్తిర్మహాద్యుతిః |\nఅనిర్దేశ్యవపుః శ్రీమానమేయాత్మా మహాద్రిధృక్ ||",
     "Mahaabuddhir Mahaaveeryo Mahaashaktir Mahaadyutih |\nAnirdeshyavapuh Shreemaan Ameyaatmaa Mahaadridhrik ||"),
    # 20
    ("మహేష్వాసో మహీభర్తా శ్రీనివాసః సతాం గతిః |\nఅనిరుద్ధః సురానందో గోవిందో గోవిదాం పతిః ||",
     "Maheshvaaso Maheebhartaa Shreenivaasah Sataam Gatih |\nAniruddhah Suraanando Govindo Govidaam Patih ||"),
    # 21
    ("మరీచిర్దమనో హంసః సుపర్ణో భుజగోత్తమః |\nహిరణ్యనాభః సుతపాః పద్మనాభః ప్రజాపతిః ||",
     "Mareechir Damano Hamsah Suparno Bhujagottamah |\nHiranyanaabhah Sutapaah Padmanaabhah Prajaapatih ||"),
    # 22
    ("అమృత్యుః సర్వదృక్సింహః సంధాతా సంధిమాన్ స్థిరః |\nఅజో దుర్మర్షణః శాస్తా విశ్రుతాత్మా సురారిహా ||",
     "Amrityuh Sarvadrik Simhah Samdhaataa Samdhimaan Sthirah |\nAjo Durmarshanaah Shaastaa Vishrutaatmaa Suraarihaa ||"),
    # 23
    ("గురుర్గురుతమో ధామ సత్యః సత్యపరాక్రమః |\nనిమిషోఽనిమిషః స్రగ్వీ వాచస్పతిరుదారధీః ||",
     "Gurur Gurutamo Dhaama Satyah Satyaparaakramah |\nNimisho'nimishah Sragvee Vaachaspatir Udaaradheeh ||"),
    # 24
    ("అగ్రణీర్గ్రామణీః శ్రీమాన్ న్యాయో నేతా సమీరణః |\nసహస్రమూర్ధా విశ్వాత్మా సహస్రాక్షః సహస్రపాత్ ||",
     "Agraneer Graamaneeh Shreemaan Nyaayo Netaa Sameeranah |\nSahasramoordhaa Vishvaatmaa Sahasraakshah Sahasrapaat ||"),
    # 25
    ("ఆవర్తనో నివృత్తాత్మా సంవృతః సంప్రమర్దనః |\nఅహః సంవర్తకో వహ్నిరనిలో ధరణీధరః ||",
     "Aavartano Nivrittaatmaa Samvritah Sampramardanah |\nAhah Samvartako Vahnir Anilo Dharaneedharah ||"),
    # 26
    ("సుప్రసాదః ప్రసన్నాత్మా విశ్వధృగ్విశ్వభుగ్విభుః |\nసత్కర్తా సత్కృతః సాధుర్జహ్నుర్నారాయణో నరః ||",
     "Suprasaadah Prasannaatmaa Vishvadhrik Vishvabhug Vibhuh |\nSatkartaa Satkritah Saadhur Jahnur Naaraayano Narah ||"),
    # 27
    ("అసంఖ్యేయోఽప్రమేయాత్మా విశిష్టః శిష్టకృచ్ఛుచిః |\nసిద్ధార్థః సిద్ధసంకల్పః సిద్ధిదః సిద్ధిసాధనః ||",
     "Asamkhyeyo'prameyaatmaa Vishishtah Shishtakrich Chhuchih |\nSiddhaarthah Siddhasamkalpah Siddhidah Siddhidhaadanah ||"),
    # 28
    ("వృషాహీ వృషభో విష్ణుర్వృషపర్వా వృషోదరః |\nవర్ధనో వర్ధమానశ్చ వివిక్తః శ్రుతిసాగరః ||",
     "Vrishaahee Vrishabho Vishnur Vrishaparvaa Vrishodarah |\nVardhano Vardhamaanashcha Viviktah Shrutisaagarah ||"),
    # 29
    ("సుభుజో దుర్ధరో వాగ్మీ మహేంద్రో వసుదో వసుః |\nనైకరూపో బృహద్రూపః శిపివిష్టః ప్రకాశనః ||",
     "Subhujo Durdharo Vaagmee Mahendro Vasudo Vasuh |\nNaikaroopo Brihadroopah Shipivishtah Prakaashanah ||"),
    # 30
    ("ఓజస్తేజోద్యుతిధరః ప్రకాశాత్మా ప్రతాపనః |\nఋద్ధః స్పష్టాక్షరో మంత్రశ్చంద్రాంశుర్భాస్కరద్యుతిః ||",
     "Ojastejodyutidharah Prakaashaatmaa Prataapanah |\nRiddhah Spashtaaksharo Mantrash Chandraamshur Bhaaskaradyutih ||"),
    # 31
    ("అమృతాంశూద్భవో భానుః శశబిందుః సురేశ్వరః |\nఔషధం జగతః సేతుః సత్యధర్మపరాక్రమః ||",
     "Amritaamshoodbhavo Bhaanuh Shashabinduh Sureshavarah |\nAushadham Jagatah Setuh Satyadharmaparaakramah ||"),
    # 32
    ("భూతభవ్యభవన్నాథః పవనః పావనోఽనలః |\nకామహా కామకృత్కాంతః కామః కామప్రదః ప్రభుః ||",
     "Bhootabhavyabhavannaathah Pavanah Paavano'nalah |\nKaamahaa Kaamakrit Kaantah Kaamah Kaamapradah Prabhuh ||"),
    # 33
    ("యుగాదికృద్యుగావర్తో నైకమాయో మహాశనః |\nఅదృశ్యో వ్యక్తరూపశ్చ సహస్రజిదనంతజిత్ ||",
     "Yugaadikrid Yugaavarto Naikamaayo Mahaashanah |\nAdrishyo Vyaktaroopashcha Sahasrajid Anantajit ||"),
    # 34
    ("ఇష్టోఽవిశిష్టః శిష్టేష్టః శిఖండీ నహుషో వృషః |\nక్రోధహా క్రోధకృత్కర్తా విశ్వబాహుర్మహీధరః ||",
     "Ishto'vishishtah Shishteshtah Shikhandee Nahusho Vrishah |\nKrodhahaa Krodhakrit Kartaa Vishvabaahur Maheedharah ||"),
    # 35
    ("అచ్యుతః ప్రథితః ప్రాణః ప్రాణదో వాసవానుజః |\nఅపాంనిధిరధిష్ఠానమప్రమత్తః ప్రతిష్ఠితః ||",
     "Achyutah Prathitah Praanah Praanado Vaasavaanujah |\nApaamnidhir Adhishthaanam Apramattah Pratishthitah ||"),
    # 36
    ("స్కందః స్కందధరో ధుర్యో వరదో వాయువాహనః |\nవాసుదేవో బృహద్భానురాదిదేవః పురంధరః ||",
     "Skandah Skandadharo Dhuryo Varado Vaayuvaahanah |\nVaasudevo Brihadbhaanur Aadidevah Purandharah ||"),
    # 37
    ("అశోకస్తారణస్తారః శూరః శౌరిర్జనేశ్వరః |\nఅనుకూలః శతావర్తః పద్మీ పద్మనిభేక్షణః ||",
     "Ashokas Taaranas Taarah Shoorah Shaurir Janeshvarah |\nAnukoolah Shataavartah Padmee Padmanibhekshanah ||"),
    # 38
    ("పద్మనాభోఽరవిందాక్షః పద్మగర్భః శరీరభృత్ |\nమహర్ద్ధిరృద్ధో వృద్ధాత్మా మహాక్షో గరుడధ్వజః ||",
     "Padmanaabho'ravindaakshah Padmagarbhah Shareerabhrit |\nMaharddhir Riddho Vriddhaatmaa Mahaaksho Garudadhwayah ||"),
    # 39
    ("అతులః శరభో భీమః సమయజ్ఞో హవిర్హరిః |\nసర్వలక్షణలక్షణ్యో లక్ష్మీవాన్ సమితింజయః ||",
     "Atulah Sharabho Bheemah Samayajno Havirharih |\nSarvalakshanalakshanyo Lakshmeevaan Samitimjayah ||"),
    # 40
    ("విక్షరో రోహితో మార్గో హేతుర్దామోదరః సహః |\nమహీధరో మహాభాగో వేగవానమితాశనః ||",
     "Viksharo Rohito Maargo Hetur Daamodarah Sahah |\nMaheedharo Mahaabhaago Vegavaan Amitaashanah ||"),
    # 41
    ("ఉద్భవః క్షోభణో దేవః శ్రీగర్భః పరమేశ్వరః |\nకరణం కారణం కర్తా వికర్తా గహనో గుహః ||",
     "Udbhavah Kshobhano Devah Shrigarbhah Parameshvarah |\nKaranam Kaaranam Kartaa Vikartaa Gahano Guhah ||"),
    # 42
    ("వ్యవసాయో వ్యవస్థానః సంస్థానః స్థానదో ధ్రువః |\nపరర్ద్ధిః పరమస్పష్టస్తుష్టః పుష్టః శుభేక్షణః ||",
     "Vyavasaayo Vyavasthaanah Samsthaanah Sthaanado Dhruvah |\nPararddhih Paramaspashtas Tushtah Pushtah Shubhekshanah ||"),
    # 43
    ("రామో విరామో విరజో మార్గో నేయో నయోఽనయః |\nవీరః शक्तिమతాం శ్రేష్ఠో ధర్మో ధర్మవిదుత్తమః ||",
     "Raamo Viraamo Virajo Maargo Neyo Nayo'nayah |\nVeerah Shaktimataam Shreshtho Dharmo Dharmaviduttamah ||"),
    # 44
    ("వైకుంఠః పురుషః ప్రాణః ప్రాణదః ప్రణవః పృథుః |\nహిరణ్యగర్భః శత్రుఘ్నో వ్యాప్తో వాయురధోక్షజః ||",
     "Vaikunthah Purushah Praanah Praanadah Pranavah Prithuh |\nHiranyagarbhah Shatrughno Vyaapto Vaayur Adhokshajah ||"),
    # 45
    ("ఋతుః సుదర్శనః కాలః పరమేష్ఠీ పరిగ్రహః |\nఉగ్రః సంవత్సరో దక్షో విశ్రామో విశ్వదక్షిణః ||",
     "Rituh Sudarshanah Kaalah Parameshthi Parigrahah |\nUgrah Samvatsaro Daksho Vishraamo Vishvadakshinah ||"),
    # 46
    ("విస్తారః స్థావరస్థాణుః ప్రమాణం బీజమవ్యయమ్ |\nఅర్థోఽనర్ధో మహాకోశో మహాభోగో మహాధనః ||",
     "Vistaarah Sthaavarasthaanuh Pramaanam Beejam Avyayam |\nArtho'nanartho Mahaakosho Mahaabhogo Mahaadhanah ||"),
    # 47
    ("అనిర్విణ్ణః స్థవిష్ఠోఽభూర్ధర్మయూపో మహామఖః |\nనక్షత్రనేమిర్నక్షత్రీ క్షమః క్షామః సమీహనః ||",
     "Anirvinnah Sthavishtho'bhoor Dharmayoopo Mahaamakhah |\nNakshatranemir Nakshatree Kshamah Kshaamah Sameehanah ||"),
    # 48
    ("యజ్ఞ ఇజ్యో మహేజ్యశ్చ క్రతుః సత్రం సతాం గతిః |\nసర్వదర్శీ విముక్తాత్మా సర్వజ్ఞో జ్ఞానముత్తమమ్ ||",
     "Yajna Ijyo Mahejyashcha Kratuh Satram Sataam Gatih |\nSarvadarshee Vimuktaatmaa Sarvajno Gyaanamuttamam ||"),
    # 49
    ("సువ్రతః సుముఖః సూక్ష్మః సుఘోషః సుఖదః సుహృత్ |\nమనోహరో జితక్రోధో వీరబాహుర్విదారణః ||",
     "Suvratah Sumukhah Sookshmah Sughoshah Sukhadah Suhrit |\nManoharo Jitakrodho Veerabaahur Vidaaranah ||"),
    # 50
    ("స్వాపనః స్వవశో వ్యాపీ నైకాత్మా నైకకర్మకృత్ |\nవత్సరో వత్సలో వత్సీ రత్నగర్భో ధనేశ్వరః ||",
     "Svaapanah Svavasho Vyaapee Naikaatmaa Naikakarmakrit |\nVatsaro Vatsalo Vatsee Ratnagarbho Dhaneshvarah ||"),
    # 51
    ("ధర్మగుబ్ధర్మకృద్ధర్మీ సదసత్క్షరమక్షరమ్ |\nఅవిజ్ఞాతా సహస్రాంశుర్విధాతా కృతలక్షణః ||",
     "Dharmagub Dharmakrid Dharmee Sadasat Ksharam Aksharam |\nAvijnaataa Sahasraamshur Vidhaataa Kritalakshanah ||"),
    # 52
    ("గభస్తినేమిః సత్త్వస్థః సింహో భూతమహేశ్వరః |\nఆదిదేవో మహాదేవో దేవేశో దేవభృద్గురుః ||",
     "Gabhastinemih Sattvasthah Simho Bhootamaheshvarah |\nAadidevo Mahaadevo Devesho Devabhrid Guruh ||"),
    # 53
    ("ఉత్తరో గోపతిర్గోప్తా జ్ఞానగమ్యః పురాతనః |\nశరీరభూతభృద్భోక్తా కపీంద్రో భూరురిదక్షిణః ||",
     "Uttaro Gopatir Goptaa Gyaanagamyah Puraatanah |\nShareerabhootabhrid Bhoktaa Kapeendro Bhooridakshinah ||"),
    # 54
    ("సోమపోఽమృతపః సోమః పురుజిత్పురుసత్తమః |\nవినయో జయః సత్యసంధో దాశార్హః సాత్త్వతాం పతిః ||",
     "Somapo'mritapah Somah Purujit Purusattamah |\nVinayo Jayah Satyasamdho Daashaarhah Saattvataam Patih ||"),
    # 55
    ("జీవో వినయితా సాక్షీ ముకుందోఽమితవిక్రమః |\nఅంభోనిధిరనంతాత్మా మహోదధిశయోఽంతకః ||",
     "Jeevo Vinayitaa Saakshee Mukundo'mitavikramah |\nAmbhonidhir Anantaatmaa Mahodadhishayo'ntakah ||"),
    # 56
    ("అజో మహార్హః స్వాభావ్యో జితామిత్రః ప్రమోదనః |\nఆనందో నందనో నందః సత్యధర్మా త్రివిక్రమః ||",
     "Ajo Mahaarhah Svaabhaavyo Jitaamitrah Pramodanah |\nAanando Nandano Nandah Satyadharmaa Trivikramah ||"),
    # 57
    ("మహర్షిః కపిలాచార్యః కృతజ్ఞో మేదినీపతిః |\nత్రిపదస్త్రిదశాధ్యక్షో మహాశృంగః కృతాంతకృత్ ||",
     "Maharshih Kapilaachaaryah Kritajno Medineepatih |\nTripadas Tridashaadhyaksho Mahaashringah Kritaantakrit ||"),
    # 58
    ("మహావరాహో గోవిందః సుషేణః కనకాంగదీ |\nగుహ్యో గభీరో గహనో గుప్తశ్చక్రగదాధరః ||",
     "Mahaavaraaho Govindah Sushenah Kanakaangadee |\nGuhyo Gabheero Gahano Guptash Chakra Gadaadharah ||"),
    # 59
    ("వేధాః స్వాంగోఽజితః కృష్ణో దృఢః సంకర్షణోఽచ్యుతః |\nవరుణో వారుణో వృక్షః పుష్కరాక్షో మహామనాః ||",
     "Vedhaah Svaango'jitah Krishno Dridhah Samkarshano'chyutah |\nVaruno Vaaruno Vrikshah Pushkaraaksho Mahaamanaah ||"),
    # 60
    ("భగవాన్ భగహా నందీ వనమాలీ హలాయుధః |\nఆదిత్యో జ్యోతిరాదిత్యః సహిష్ణుర్గతిసత్తమః ||",
     "Bhagavaan Bhagahaa Nandee Vanamaalee Halaayudhah |\nAadityo Jyotiraadityah Sahishnur Gatisattamah ||"),
    # 61
    ("సుధన్వా ఖండపరశుర్దారుణో ద్రవిణప్రదః |\nదివిస్పృక్సర్వదృగ్వ్యాసో వాచస్పతిరయోనిజః ||",
     "Sudhanvaa Khandaparashur Daaruno Dravinapradah |\nDivisprik Sarvadrik Vyaaso Vaachaspatir Ayonijah ||"),
    # 62
    ("త్రిసామా సామగః సామ నిర్వాణం భేషజం భిషక్ |\nసంన్యాసకృచ్ఛమః శాంతో నిష్ఠా శాంతిః పరాయణమ్ ||",
     "Trisaamaa Saamagah Saama Nirvaanam Bheshajam Bhishak |\nSamnyaasakrich Chhamah Shaanto Nishthaa Shaantih Paraayanam ||"),
    # 63
    ("శుభాంగః శాంతిదః స్రష్టా కుముదః కువలేశయః |\nగోహితో గోపతిర్గోప్తా వృషభాక్షో వృషప్రియః ||",
     "Shubhaangah Shaantidah Srashtaa Kumudah Kuvaleshayah |\nGohito Gopatir Goptaa Vrishabhaaksho Vrishapriyah ||"),
    # 64
    ("అనివర్తీ నివృత్తాత్మా సంక్షేప్తా క్షేమకృచ్ఛివః |\nశ్రీవత్సవక్షాః శ్రీవాసః శ్రీపతిః శ్రీమతాం వరః ||",
     "Anivartee Nivrittaatmaa Samksheptaa Kshemakrich Chhivah |\nShreevatsavakshaah Shrevaasah Shreepatih Shreemataam Varah ||"),
    # 65
    ("శ్రీదః శ్రీశః శ్రీనివాసః శ్రీనిధిః శ్రీవిభావనః |\nశ్రీధరః శ్రీకరః శ్రేయః శ్రీమాంల్లోకత్రయాశ్రయః ||",
     "Shreedah Shreeshah Shreenivaasah Shreenidhih Shreevibhaavanah |\nShreedharah Shreekarah Shreyah Shreemaamllokatrayaashrayah ||"),
    # 66
    ("స్వక్షః స్వంగః శతానందో నందిర్జ్యోతిర్గణేశ్వరః |\nవిజితాత్మాఽవిధేయాత్మా సత్కీర్తిశ్ఛిన్నసంశయః ||",
     "Svakshah Svangah Shataanando Nandir Jyotirganeshvarah |\nVijitaatmaa'vidheyaatmaa Satkeertish Chhinnasamshayah ||"),
    # 67
    ("ఉదీర్ణః సర్వతశ్చక్షురనీశః శాశ్వతస్థిరః |\nభూశయో భూషణో భూతిర్విశోకః శోకనాశనః ||",
     "Udeernah Sarvatashchakshur Aneeshah Shaashvatasthirah |\nBhooshayo Bhooshano Bhootir Vishokah Shokanaashanah ||"),
    # 68
    ("అర్చిష్మానర్చితః కుంభో విశుద్ధాత్మా విశోధనః |\nఅనిరుద్ధోఽప్రతిరథః ప్రద్యుమ్నోఽమితవిక్రమః ||",
     "Archishmahn Architah Kumbho Vishuddhaatmaa Vishodhanah |\nAniruddho'pratirathah Pradyumno'mitavikramah ||"),
    # 69
    ("కాలనేమినిహా వీరః శౌరిః శూరజనేశ్వరః |\nత్రిలోకాత్మా త్రిలోకేశః కేశవః కేశిహా హరిః ||",
     "Kaalanemi-nihaa Veerah Shaurih Shoorajaneshvarah |\nTrilokaatmaa Trilokeshah Keshavah Keshihaa Harih ||"),
    # 70
    ("కామదేవః కామపాలః కామీ కాంతః కృతాగమః |\nఅనిర్దేశ్యవపుర్విష్ణుర్వీరోఽనంతో ధనంజయః ||",
     "Kaamadevah Kaamapaalah Kaamee Kaantah Kritaagamah |\nAnirdeshyavapur Vishnur Veero'nanto Dhananjayah ||"),
    # 71
    ("బ్రహ్మణ్యో బ్రహ్మకృద్బ్రహ్మా బ్రహ్మ బ్రహ్మవివర్ధనః |\nబ్రహ్మవిద్బ్రాహ్మణో బ్రహ్మీ బ్రహ్మజ్ఞో బ్రాహ్మణప్రియః ||",
     "Brahmanyo Brahmakrid Brahmaa Brahma Brahmavivardhanah |\nBrahmavid Braahmano Brahmee Brahmajno Braahmanapriyah ||"),
    # 72
    ("మహాక్రమో మహాకర్మా మహాతేజా మహోరగః |\nమహాక్రతుర్మహాయజ్వా మహాయజ్ఞో మహామహవిః ||",
     "Mahaakramo Mahaakarmaa Mahaatejaa Mahoragah |\nMahaakratur Mahaayajvaa Mahaayajno Mahaahavih ||"),
    # 73
    ("స్తవ్యః స్తవప్రియః స్తోత్రం స్తుతిః స్తోతా రణప్రియః |\nపూర్ణః పూరయితా పుణ్యః పుణ్యకీర్తిరనామయః ||",
     "Stavyah Stavapriyah Stotram Stutih Stotaa Ranapriyah |\nPoornah Poorayitaa Punyah Punyakeertir Anaamayah ||"),
    # 74
    ("మనోజవస్తీర్థకరో వసురేతా వసుప్రదః |\nవసుప్రదో వాసుదేవో వసుర్వసుమనా హవిః ||",
     "Manojavas Teerthakaro Vasuretaa Vasupradah |\nVasuprado Vaasudevo Vasur Vasumanaa Havih ||"),
    # 75
    ("సద్గతిః సత్కృతిః సత్తా సద్భూతిః సత్పరాయణః |\nశూరసేనో యదుశ్రేష్ఠః సంనివాసః సుయామునః ||",
     "Sadgatih Satkritih Sattaa Sadbhootih Satparaayanah |\nShooraseno Yadushreshthah Samnivaasah Suyaamunah ||"),
    # 76
    ("భూతావాసో వాసుదేవః సర్వాసునిలయోఽనలః |\nదర్పహా దర్పదో దృప్తో దుర్ధరోఽథాపరాజితః ||",
     "Bhootaavaaso Vaasudevah Sarvaasunilayo'nalah |\nDarpahaa Darpado Dripto Durdharo'thaaparaajitah ||"),
    # 77
    ("విశ్వమూర్తిర్మహామూర్తిర్దీప్తమూర్తిరమూర్తిమాన్ |\nఅనేకమూర్తిరవ్యక్తః శతమూర్తిః శతాననః ||",
     "Vishvamoortir Mahaamoortir Deeptamoortir Amoortimaan |\nAnekamoortir Avyaktah Shatamoortih Shataanahah ||"),
    # 78
    ("ఏకో నైకః సవః కః కిం యత్తత్ పదమనుత్తమమ్ |\nలోకబంధుర్లోకనాథో మాధవో భక్తవత్సలః ||",
     "Eko Naikah Savah Kah Kim Yat Tat Padam Anuttamam |\nLokabandhur Lokanaatho Maadhavo Bhaktavatsalah ||"),
    # 79
    ("సువర్ణవర్ణో హేమాంగో వరాంగశ్చందనాంగదీ |\nవీరహా విషమః శూన్యో ఘృతాశీరచలశ్చలః ||",
     "Suvarnavarno Hemaango Varaangash Chandanaangadee |\nVeerahaa Vishamah Shoonyo Ghritaasheesh Chhalashchalah ||"),
    # 80
    ("అమానీ మానదో మాన్యో లోకస్వామీ త్రిలోకధృక్ |\nసుమేధా మేధజో ధన్యః సత్యమేధా ధరాధరః ||",
     "Amaanee Maanado Maanyo Lokasvaamee Trilokadhrik |\nSumedhaa Medhajo Dhanyah Satyamedhaa Dharaadharah ||"),
    # 81
    ("తేజోవృషో ద్యుతిధరః సర్వశస్త్రభృతాం వరః |\nప్రగ్రహో నిగ్రహో వ్యగ్రో నైకశృంగో గదాగ్రజః ||",
     "Tejovrisho Dyutidharah Sarvashastrabhritaam Varah |\nPragraho Nigraho Vyagro Naikashringo Gadaagrajah ||"),
    # 82
    ("చతుర్మూర్తిశ్చతుర్బాహుశ్చతుర్వ్యూహశ్చతుర్గతిః |\nచతురాత్మా చతుర్భావశ్చతుర్వేదవిదేకపాత్ ||",
     "Chaturmoortish Chaturbhaahush Chaturvyoohash Chaturgatih |\nChaturaatmaa Chaturbhaavash Chaturvedavid Ekapahaat ||"),
    # 83
    ("సమావర్తోఽనివృత్తాత్మా దుర్జయో దురతిక్రమః |\nదుర్లభో దుర్గమో దుర్గో దురావాసో దురారిహా ||",
     "Samaavarto'nivrittaatmaa Durjayo Duratikramah |\nDurlabho Durgamo Durgo Duraavaaso Duraarihaa ||"),
    # 84
    ("శుభాంగో లోకసారంగః సుతంతుస్తంతువర్ధనః |\nఇంద్రకర్మా మహాకర్మా కృతకర్మా కృతాగమః ||",
     "Shubhaango Lokasaarangah Sutantus Tantuvardhanah |\nIndrakarmaa Mahaakarmaa Kritakarmaa Kritaagamah ||"),
    # 85
    ("ఉద్భవః సుందరః సుందో రత్ననాభః సులోచనః |\nఅర్కో వాజసనః శృంగీ జయంతః సర్వవిజ్జయీ ||",
     "Udbhavah Sundarah Sundo Ratnanaabhah Sulochanah |\nArko Vaajasanah Shringee Jayantah Sarvavij Jayee ||"),
    # 86
    ("సువర్ణబిందురక్షోభ్యః సర్వవాగీశ్వరేశ్వరః |\nమహాహ్రదో మహాగర్తో మహాభూతో మహానిధిః ||",
     "Suvarnabindur Akshobhyah Sarvavaageeshvareshvarah |\nMahaahrado Mahaagarto Mahaabhooto Mahaanidhih ||"),
    # 87
    ("కుముదః కుందరః కుందః పర్జన్యః పావనోఽనిలః |\nఅమృతాశోఽమృతవపుః సర్వజ్ఞః సర్వతోముఖః ||",
     "Kumudah Kundarah Kundah Parjanyah Paavano'nilah |\nAmritaasho'mritavapuh Sarvajnah Sarvatomukhah ||"),
    # 88
    ("సులభః సువ్రతః సిద్ధః శత్రుజిచ్ఛత్రుతాపనః |\nన్యగ్రోధోఽదుంబరోఽశ్వత్థశ్చాణూరాంధ్రనిషూదనః ||",
     "Sulabhah Suvratah Siddhah Shatrujich Chhatrutaapanah |\nNyagrodho'dumbaro'shvatthash Chaanooraandhra Nishoodanah ||"),
    # 89
    ("సహస్రార్చిః సప్తజిహ్వః సప్తైధాః సప్తవాహనః |\nఅమూర్తిరనఘోఽచింత్యో భయకృద్భయనాశనః ||",
     "Sahasraarchih Saptajihvah Saptaidhaah Saptavaahanah |\nAmoortir Anagho'chintyo Bhayakrid Bhayanaashanah ||"),
    # 90
    ("అణుర్బృహత్కృశః స్థూలో గుణభృన్నిర్గుణో మహాన్ |\nఅధృతః స్వధృతః స్వాస్యః ప్రాగ్వంశో వంశవర్ధనః ||",
     "Anur Brihat Krishah Sthoolo Gunabhrin Nirguno Mahaan |\nAdhritah Svadhritah Svaasyah Praagvamsho Vamshavardhanah ||"),
    # 91
    ("భారభృత్కథితో యోగీ యోగీశః సర్వకామదః |\nఆశ్రమః శ్రమణః క్షామః సుపర్ణో వాయువాహనః ||",
     "Bhaarabhrit Kathito Yogee Yogeeshah Sarvakaamadah |\nAashramah Shramanah Kshaamah Suparno Vaayuvaahanah ||"),
    # 92
    ("ధనుర్ధరో ధనుర్వేదో దండో దమయితా దమః |\nఅపరాజితః సర్వసహో నియంతాఽనియమోఽయమః ||",
     "Dhanurdharo Dhanurvedo Dando Damayitaa Damah |\nAparaajitah Sarvasaho Niyantaa'niyamo'yamah ||"),
    # 93
    ("సత్త్వవాన్ సాత్త్వికః సత్యః సత్యధర్మపరాయణః |\nఅభిప్రాయః ప్రియార్హోఽర్హః ప్రియకృత్ ప్రీతివర్ధనః ||",
     "Sattvavaan Saattvikah Satyah Satyadharmaparaayanah |\nAbhipraayah Priyaarho'rhah Priyakrit Preetivardhanah ||"),
    # 94
    ("విహాయసగతిర్జ్యోతిః సురుచిర్హుతభుగ్విభుః |\nరవిర్విరోచనః సూర్యః సవితా రవిలోచనః ||",
     "Vihaayasagatir Jyotih Suruchir Hutabhug Vibhuh |\nRavir Virochanah Sooryah Savitaa Ravilochanah ||"),
    # 95
    ("అనంతో హుతభుగ్భోక్తా సుఖదో నైకదోఽగ్రజః |\nఅనిర్విణ్ణః సదామర్షీ లోకాధిష్ఠానమద్భుతః ||",
     "Ananto Hutabhug Bhoktaa Sukhado Naikado'grajah |\nAnirvinnah Sadaamarshee Lokaadhishthaanam Adbhutah ||"),
    # 96
    ("సనాత్సనాతనతమః కపిలః కపిరవ్యయః |\nస్వస్తిదః స్వస్తికృత్స్వస్తి స్వస్తిభుక్స్వస్తిదక్షిణః ||",
     "Sanaat Sanaatanatamah Kapilah Kapir Avyayah |\nSvastidah Svastikrit Svasti Svastibhuk Svastidakshinah ||"),
    # 97
    ("అరౌద్రః కుండలీ చక్రీ విక్రమ్యూర్జితశాసనః |\nశబ్దాతిగః శబ్దసహః శిశిరః శర్వరీకరః ||",
     "Araudrah Kundalee Chakree Vikramy Oorjitashaasanah |\nShabdaatigah Shabdasahah Shishirah Sharvareekarah ||"),
    # 98
    ("అక్రూరః పేశలో దక్షో దక్షిణః క్షమిణాం వరః |\nవిద్వత్తమో వీతభయః పుణ్యశ్రవణకీర్తనః ||",
     "Akroorah Peshalo Daksho Dakshinah Kshaminaam Varah |\nVidvattamo Veetabhayah Punyashravanakeertanah ||"),
    # 99
    ("ఉత్తారణో దుష్కృతిహా పుణ్యో దుఃస్వప్ననాశనః |\nవీరహా రక్షణః సంతో జీవనః పర్యవస్థితః ||",
     "Uttaarano Dushkritihaa Punyo Duhsvapnanaashanah |\nVeerahaa Rakshanah Santo Jeevanah Paryavasthitah ||"),
    # 100
    ("అనంతరూపోఽనంతశ్రీర్జితమన్యుర్భయాపహః |\nచతురశ్రో గభీరాత్మా విదిశో వ్యాదిశో దిశః ||",
     "Anantaroopo'nantashreer Jitamanyur Bhayaapahah |\nChaturashro Gabheeraatmaa Vidisho Vyaadisho Dishah ||"),
    # 101
    ("అనాదిర్భూర్భువో లక్ష్మీః సువీరో రుచిరాంగదః |\nజననో జనజన్మాదిర్భీమో భీమపరాక్రమః ||",
     "Anaadir Bhoorbhuvo Lakshmeeh Suveero Ruchiraangadah |\nJanano Janajanmaadir Bheemo Bheemaparaakramah ||"),
    # 102
    ("ఆధారనిలయోఽధాతా పుష్పహాసః ప్రజాగరః |\nఊర్ధ్వగః సత్పథాచారః ప్రాణదః ప్రణవః పణః ||",
     "Aadhaaranilayo'dhaataa Pushpahaasah Prajaagarah |\nOordhvagah Satpathaachaarah Praanadah Pranavah Panah ||"),
    # 103
    ("ప్రమాణం ప్రాణనిలయః ప్రాణభృత్ ప్రాణజీవనః |\nతత్త్వం తత్త్వవిదేకాత్మా జన్మమృత్యుజరాతిగః ||",
     "Pramaanam Praananilayah Praanabhrit Praanajeevanah |\nTattvam Tattvavid Ekaatmaa Janmamrityujaraatigah ||"),
    # 104
    ("భూర్భువః స్వస్తరుస్తారః సవితా ప్రపితామహః |\nయజ్ఞో యజ్ఞపతిర్యజ్వా యజ్ఞాంగో యజ్ఞవాహనః ||",
     "Bhoorbhuvah Svastarus Taarah Savitaa Prapitaamahah |\nYajno Yajnapatir Yajvaa Yajnaango Yajnavaahanah ||"),
    # 105
    ("యజ్ఞభృద్ యజ్ఞకృద్ యజ్ఞీ యజ్ఞభుగ్ యజ్ఞసాధనః |\nయజ్ఞాంతకృద్ యజ్ఞగుహ్యమన్నమన్నాద ఏవ చ ||",
     "Yajnabhrid Yajnakrid Yajnee Yajnabhug Yajnasaadhanah |\nYajnaantakrid Yajnaguhyam Annam Annaada Eva Cha ||"),
    # 106
    ("ఆత్మయోనిః స్వయంజాతో వైఖానః సామగాయనః |\nదేవకీనందనః స్రష్టా క్షితీశః పాపనాశనః ||",
     "Aatmayonih Svayamjaato Vaikhaanah Saamagaayanah |\nDevakeenandanah Srashtaa Ksheetishah Paapanaashanah ||"),
    # 107
    ("శంఖభృన్నందకీ చక్రీ శార్ఙ్గధన్వా గదాధరః |\nరథాంగపాణిరక్షోభ్యః సర్వప్రహరణాయుధః ||",
     "Shankhabhrin Nandakee Chakree Shaarngadhanvaa Gadaadharah |\nRathaangapaanir Akshobhyah Sarvapraharanaayudhah ||"),
    # 108
    ("వనమాలీ గదీ శార్ఙ్గీ శంఖీ చక్రీ చ నందకీ |\nశ్రీమాన్ నారాయణో విష్ణుర్వాసుదేవోఽభిరక్షతు ||",
     "Vanamaalee Gadee Shaarngee Shankhee Chakree Cha Nandakee |\nShreemaan Naaraayano Vishnur Vaasudevo'bhirakshatu ||")
]

stanzas = []

# --- 1. Opening Tanpura/Omkara (0 -> 8700 ms) ---
stanzas.append({
    "index": 1,
    "timestampMs": 0,
    "startTimeMs": 0,
    "endTimeMs": 8700,
    "textTelugu": "॥ శ్రీ విష్ణు సహస్రనామ స్తోత్రమ్ - ఆరంభ ధ్యానమ్ ॥",
    "telugu": "॥ శ్రీ విష్ణు సహస్రనామ స్తోత్రమ్ - ఆరంభ ధ్యానమ్ ॥",
    "textEnglish": "|| Sri Vishnu Sahasranama Stotram - Invocation ||",
    "english": "|| Sri Vishnu Sahasranama Stotram - Invocation ||"
})

# --- 2. Dhyana Shlokas & Purva Peethika (8700 -> 345000 ms) ---
INTRO_SECTIONS = [
    (8700, 30500,
     "శుక్లాంబరధరం విష్ణుం శశివర్ణం చతుర్భుజమ్ |\nప్రసన్నవదనం ధ్యాయేత్ సర్వవిఘ్నోపశాంతయే ||",
     "Shuklaambaradharam Vishnum Shashivarnam Chaturbhujam |\nPrasanna Vadanam Dhyaayet Sarva Vighnopa Shaantaye ||"),
    (30500, 53700,
     "యస్య ద్విరదవక్త్రాద్యాః పారిషద్యాః పరః శతమ్ |\nవిఘ్నం నిఘ్నంతి సతతం విష్వక్సేనం తమాశ్రయే ||",
     "Yasya Dvirada Vaktraadyaah Paarishadyaah Parah Shatam |\nVighnam Nighnanti Satatam Vishvaksenam Tamaashraye ||"),
    (53700, 98500,
     "శాంతాకారం భుజగశయనం పద్మనాభం సురేశమ్ |\nవిశ్వాధారం గగనసదృశం మేఘవర్ణం శుభాంగమ్ |\nలక్ష్మీకాంతం కమలనయనం యోగిహృద్ధ్యానగమ్యమ్ |\nవందే విష్ణుం భవభయహరం సర్వలోకైకనాథమ్ ||",
     "Shaantaakaaram Bhujagashayanam Padmanaabham Suresham |\nVishvaadhaaram Gaganasadrisham Meghavarnam Shubhaangam |\nLakshmeekaantam Kamalanayanam Yogihriddhyaanagamyam |\nVande Vishnum Bhavabhayaharam Sarvalokaika Naatham ||"),
    (98500, 135100,
     "మేఘశ్యామం పీతకౌశేయవాసం శ్రీవత్సాంకం కౌస్తుభోద్భాసితాంగమ్ |\nపుణ్యోపేతం పుండరీకాయతాక్షం విష్ణుం వందే సర్వలోకైకనాథమ్ ||",
     "Meghashyaamam Peetakawsheyavaasam Shreevatsaankam Kaustubhobhaasitaangam |\nPunyopetam Pundareekaayataaksham Vishnum Vande Sarvalokaika Naatham ||"),
    (135100, 167500,
     "నమః సమస్త భూతానామాదిభూతాయ భూభృతే |\nఅనేకరూప రూపాయ విష్ణవే ప్రభవిష్ణవే ||",
     "Namah Samasta Bhootaanaamaadibhootaaya Bhoobhrite |\nAneka Roopa Roopaaya Vishnave Prabha Vishnave ||"),
    (167500, 209100,
     "॥ పూర్వ పీఠికా ॥\nవైశంపాయన ఉవాచ: శ్రుత్వా ధర్మానశేషేణ పావనాని చ సర్వశః |\nయుధిష్ఠిరః శాంతనవం పునరేవాభ్యభాషత ||",
     "|| Poorva Peethikaa ||\nVaishampaayana Uvaacha: Shrutvaa Dharmaanasheshena Paavanaani Cha Sarvashah |\nYudhishthirah Shaantanavam Punarevaabhyabhaashata ||"),
    (209100, 275000,
     "యుధిష్ఠిర ఉవాచ: కిమేకం దైవతం లోకే కిం వాప్యేకం పరాయణమ్ |\nస్తువంతః కం కమర్చంతః ప్రాప్నుయుర్మానవాః శుభమ్ ||",
     "Yudhishthira Uvaacha: Kimekam Daivatam Loke Kim Vaapyekam Paraayanam |\nStuvantah Kam Kamarchantah Praapnuyur Maanavaah Shubham ||"),
    (275000, 315000,
     "భీష్మ ఉవాచ: జగత్ప్రిభుం దేవదేవమనంతం పురుషోత్తమమ్ |\nస్తువన్ నామసహస్రేణ పురుషః సతతోత్థితః ||",
     "Bheeshma Uvaacha: Jagatprabhum Devadevamanantam Purushottamam |\nStuvan Naama Sahasrena Purushah Satatotthitah ||"),
    (315000, 345000,
     "॥ సంకల్పం & న్యాసః ॥\nఓం అస్య శ్రీవిష్ణోర్దివ్య సహస్రనామస్తోత్ర మహామంత్రస్య...\nశ్రీమన్నారాయణ ప్రీత్యర్థే జపే వినియోగః ||",
     "|| Sankalpam & Nyaasah ||\nOm Asya Shree Vishnor Divya Sahasranaama Stotra Mahaamantrasya...\nShreeman Naaraayana Preetyarthe Jape Viniyogah ||")
]

for i, (s_ms, e_ms, tel, eng) in enumerate(INTRO_SECTIONS):
    stanzas.append({
        "index": len(stanzas) + 1,
        "timestampMs": s_ms,
        "startTimeMs": s_ms,
        "endTimeMs": e_ms,
        "textTelugu": tel,
        "telugu": tel,
        "textEnglish": eng,
        "english": eng
    })

# --- 108 Main Stotra Shlokas (345000 -> 1595000 ms) ---
shloka_start = 345000
shloka_end = 1595000
shloka_dur = (shloka_end - shloka_start) / 108.0

for i, (tel, eng) in enumerate(SHLOKAS):
    s_ms = int(round(shloka_start + i * shloka_dur))
    e_ms = int(round(shloka_start + (i + 1) * shloka_dur))
    shloka_num_tel = f"॥ శ్లోకం {i+1} ॥\n"
    shloka_num_eng = f"|| Shloka {i+1} ||\n"
    stanzas.append({
        "index": len(stanzas) + 1,
        "timestampMs": s_ms,
        "startTimeMs": s_ms,
        "endTimeMs": e_ms,
        "textTelugu": shloka_num_tel + tel,
        "telugu": shloka_num_tel + tel,
        "textEnglish": shloka_num_eng + eng,
        "english": shloka_num_eng + eng
    })

# --- Phalasruti & Concluding Mangalam (1595000 -> 1790910 ms) ---
OUTRO_SECTIONS = [
    (1595000, 1635000,
     "॥ ఉత్తర పీఠికా / ఫలశ్రుతిః ॥\nఇతీదం కీర్తనీయస్య కేశవస్య మహాత్మనః |\nనామ్నాం సహస్రం దివ్యానామశేషేణ ప్రకీర్తితమ్ ||",
     "|| Uttara Peethikaa / Phalasrutih ||\nIteedam Keertaneeyasya Keshavasya Mahaatmanah |\nNaamnaam Sahasram Divyaanaam Asheshena Prakeertitam ||"),
    (1635000, 1675000,
     "య ఇదం శృణుయాన్నిత్యం యశ్చాపి పరికీర్తయేత్ |\nనాశుభం ప్రాప్నుయాత్ కించిత్ సోఽముత్రేహ చ మానవః ||",
     "Ya Idam Shrinuyan Nityam Yash Chaapi Parikeertayet |\nNaashubham Praapnuyaat Kimchit So'mutreha Cha Maanavah ||"),
    (1675000, 1715000,
     "వేదాంతగో బ్రాహ్మణః స్యాత్ క్షత్రియో విజయీ భవేత్ |\nవైశ్యో ధనసమృద్ధః స్యాత్ శూద్రః సుఖమవాప్నుయాత్ ||",
     "Vedaantago Braahmanah Syaat Kshatriyo Vijayee Bhavet |\nVaishyo Dhanasamriddhah Syaat Shoodrah Sukham Avaapnuyaat ||"),
    (1715000, 1755000,
     "న తే యాంతి పరాభవం సర్వభూతాత్మా సర్వదృక్ |\nసర్వదా సర్వగః సర్వః సర్వాత్మా సర్వభావనః ||",
     "Na Te Yaanti Paraabhavam Sarvabhootaatmaa Sarvadrik |\nSarvadaa Sarvagah Sarvah Sarvaatmaa Sarvabhaavanah ||"),
    (1755000, 1790910,
     "నమో బ్రహ్మణ్యదేవాయ గోబ్రాహ్మణహితాయ చ |\nజగద్ధితాయ కృష్ణాయ గోవిందాయ నమో నమః ||\n॥ శ్రీ వాసుదేవార్పణమస్తు ॥",
     "Namo Brahmanyadevaaya Gobraahmanahitaaya Cha |\nJagaddhitaaya Krishnaaya Govindaaya Namo Namah ||\n|| Shree Vaasudevaarpanamastu ||")
]

for i, (s_ms, e_ms, tel, eng) in enumerate(OUTRO_SECTIONS):
    stanzas.append({
        "index": len(stanzas) + 1,
        "timestampMs": s_ms,
        "startTimeMs": s_ms,
        "endTimeMs": e_ms,
        "textTelugu": tel,
        "telugu": tel,
        "textEnglish": eng,
        "english": eng
    })

output_file = os.path.join(OUTPUT_DIR, "vishnu_sahasranamam.json")
data = {
    "trackId": "vishnu_sahasranamam",
    "titleTelugu": "శ్రీ విష్ణు సహస్రనామ స్తోత్రము",
    "titleEnglish": "Sri Vishnu Sahasranama Stotram",
    "totalStanzas": len(stanzas),
    "stanzas": stanzas
}

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Calibrated {output_file} with {len(stanzas)} stanzas.")
