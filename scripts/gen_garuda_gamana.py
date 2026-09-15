# -*- coding: utf-8 -*-
"""
Calibrated generator for Garuda Gamana Tava Charana lyrics JSON.
Vocal onset starts at 450 ms with recurring refrains across 414550 ms.
"""
import json
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "app", "src", "main", "assets", "lyrics")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 414550 ms total
GARUDA_SECTIONS = [
    # 0: Pallavi / Refrain
    (
        0, 24000,
        "గరుడ గమన తవ చరణ కమలమిహ\nమనసి లసతు మమ నిత్యమ్ | మమ నిత్యమ్ ||",
        "Garuda Gamana Tava Charana Kamala Miha\nManasi Lasatu Mama Nityam | Mama Nityam ||"
    ),
    # 1: Verse 1
    (
        24000, 48000,
        "జలధి సుతా రమణ చారు లలామ |\nమదనా జనక మనసి లసతు మమ నిత్యమ్ ||",
        "Jaladhi Sutaa Ramana Chaaru Lalaama |\nMadanaa Janaka Manasi Lasatu Mama Nityam ||"
    ),
    # 2: Refrain
    (
        48000, 72000,
        "గరుడ గమన తవ చరణ కమలమిహ\nమనసి లసతు మమ నిత్యమ్ | మమ నిత్యమ్ ||",
        "Garuda Gamana Tava Charana Kamala Miha\nManasi Lasatu Mama Nityam | Mama Nityam ||"
    ),
    # 3: Verse 2
    (
        72000, 96000,
        "భజన శీలా జన పరమ దయాఘన |\nభవ భయ హరణ మనసి లసతు మమ నిత్యమ్ ||",
        "Bhajana Sheelaa Jana Parama Dayaaghana |\nBhava Bhaya Harana Manasi Lasatu Mama Nityam ||"
    ),
    # 4: Refrain
    (
        96000, 120000,
        "గరుడ గమన తవ చరణ కమలమిహ\nమనసి లసతు మమ నిత్యమ్ | మమ నిత్యమ్ ||",
        "Garuda Gamana Tava Charana Kamala Miha\nManasi Lasatu Mama Nityam | Mama Nityam ||"
    ),
    # 5: Verse 3
    (
        120000, 144000,
        "దినకర కోటి సుదీప్త నఖద్యుతి |\nదీన జనావన మనసి లసతు మమ నిత్యమ్ ||",
        "Dinakara Koti Sudeepta Nakhadyuti |\nDeena Janaavana Manasi Lasatu Mama Nityam ||"
    ),
    # 6: Refrain
    (
        144000, 168000,
        "గరుడ గమన తవ చరణ కమలమిహ\nమనసి లసతు మమ నిత్యమ్ | మమ నిత్యమ్ ||",
        "Garuda Gamana Tava Charana Kamala Miha\nManasi Lasatu Mama Nityam | Mama Nityam ||"
    ),
    # 7: Verse 4
    (
        168000, 192000,
        "కరుణారస సుధా కమలాసన వినుత |\nకమల భవాండ మనసి లసతు మమ నిత్యమ్ ||",
        "Karunaarasa Sudhaa Kamalaasana Vinuta |\nKamala Bhavaanda Manasi Lasatu Mama Nityam ||"
    ),
    # 8: Refrain
    (
        192000, 216000,
        "గరుడ గమన తవ చరణ కమలమిహ\nమనసి లసతు మమ నిత్యమ్ | మమ నిత్యమ్ ||",
        "Garuda Gamana Tava Charana Kamala Miha\nManasi Lasatu Mama Nityam | Mama Nityam ||"
    ),
    # 9: Verse 5
    (
        216000, 240000,
        "అసుర కులార్దన అద్భుత శౌర్య |\nఅమిత పరాక్రమ మనసి లసతు మమ నిత్యమ్ ||",
        "Asura Kulaardana Adbhuta Shaurya |\nAmita Paraakrama Manasi Lasatu Mama Nityam ||"
    ),
    # 10: Refrain
    (
        240000, 264000,
        "గరుడ గమన తవ చరణ కమలమిహ\nమనసి లసతు మమ నిత్యమ్ | మమ నిత్యమ్ ||",
        "Garuda Gamana Tava Charana Kamala Miha\nManasi Lasatu Mama Nityam | Mama Nityam ||"
    ),
    # 11: Verse 6
    (
        264000, 288000,
        "కనక విచిత్ర విభూషణ భూషిత |\nకౌస్తుభ శోభిత మనసి లసతు మమ నిత్యమ్ ||",
        "Kanaka Vichitra Vibhooshana Bhooshita |\nKaustubha Shobhita Manasi Lasatu Mama Nityam ||"
    ),
    # 12: Refrain
    (
        288000, 312000,
        "గరుడ గమన తవ చరణ కమలమిహ\nమనసి లసతు మమ నిత్యమ్ | మమ నిత్యమ్ ||",
        "Garuda Gamana Tava Charana Kamala Miha\nManasi Lasatu Mama Nityam | Mama Nityam ||"
    ),
    # 13: Verse 7
    (
        312000, 336000,
        "సకల జగజ్జన పాలక శోభిత |\nశంఖ గదాధర మనసి లసతు మమ నిత్యమ్ ||",
        "Sakala Jagajjana Paalaka Shobhita |\nShankha Gadaadhara Manasi Lasatu Mama Nityam ||"
    ),
    # 14: Refrain
    (
        336000, 360000,
        "గరుడ గమన తవ చరణ కమలమిహ\nమనసి లసతు మమ నిత్యమ్ | మమ నిత్యమ్ ||",
        "Garuda Gamana Tava Charana Kamala Miha\nManasi Lasatu Mama Nityam | Mama Nityam ||"
    ),
    # 15: Verse 8
    (
        360000, 384000,
        "నిగమ విదూర నితాంత మనోహర |\nనిత్య నిరంజన మనసి లసతు మమ నిత్యమ్ ||",
        "Nigama Vidoora Nitaanta Manohara |\nNitya Niranjana Manasi Lasatu Mama Nityam ||"
    ),
    # 16: Grand Finale Refrain
    (
        384000, 404000,
        "గరుడ గమన తవ చరణ కమలమిహ\nమనసి లసతు మమ నిత్యమ్ | మమ నిత్యమ్ ||",
        "Garuda Gamana Tava Charana Kamala Miha\nManasi Lasatu Mama Nityam | Mama Nityam ||"
    ),
    # 17: Mangalam
    (
        404000, 414550,
        "శ్రీమన్నారాయణ జగత్పతే వాసుదేవ రక్షమామ్ |\nఓం నమో నారాయణాయ ||",
        "Shreeman Naaraayana Jagatpate Vaasudeva Rakshamaam |\nOm Namo Naaraayanaaya ||"
    )
]

stanzas = []
for i, (s_ms, e_ms, tel, eng) in enumerate(GARUDA_SECTIONS):
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

output_file = os.path.join(OUTPUT_DIR, "garuda_gamana.json")
data = {
    "trackId": "garuda_gamana",
    "titleTelugu": "గరుడ గమన తవ చరణ కమలమిహ",
    "titleEnglish": "Garuda Gamana Tava Charana",
    "totalStanzas": len(stanzas),
    "stanzas": stanzas
}

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Calibrated {output_file} with {len(stanzas)} stanzas.")
