"""Zet een patroonconcept om naar het skelet van een kennisbank-handleiding.

Het levert een README met de juiste frontmatter en de vaste koppen, gevuld met de inhoud uit het
patroon. Het is een **skelet**: de aanspreekvorm, de barriere-zin en het bewijs schrijf je daarna met de
hand na, want een catalogus beschrijft en een handleiding spreekt de lezer aan.

Gebruik:
    python tools/naar_handleiding.py <slug> <mapnaam> <barrieres,komma> <rol>

Voorbeeld:
    python tools/naar_handleiding.py pim-jit just-in-time-beheerrechten jit fundering
"""
from __future__ import annotations

import json
import pathlib
import re
import sys

HIER = pathlib.Path(__file__).resolve().parent.parent
WERKMAP = HIER.parent
KENNISBANK = WERKMAP / "kennisbank"
PADEN = WERKMAP / "aanvalspaden" / "paden.json"
SITE = "https://security-commons-nl.github.io/kennisbank/security"


def barrieres() -> dict[str, dict]:
    data = json.loads(PADEN.read_text(encoding="utf-8"))
    uit: dict[str, dict] = {}
    for blad in data["bladeren"]:
        for cp in blad["chokepoints"]:
            uit.setdefault(cp["vraag_id"], cp)
    for rv in data.get("randvoorwaarden", []):
        uit.setdefault(rv["vraag_id"], rv)
    return uit


def sectie(tekst: str, kop: str) -> str:
    m = re.search(rf"^## {re.escape(kop)}\n(.*?)(?=\n## |\Z)", tekst, re.S | re.M)
    return m.group(1).strip() if m else ""


def bouw(slug: str, mapnaam: str, bar_ids: list[str], rol: str) -> pathlib.Path:
    concept = (HIER / "_dump" / f"{slug}.md").read_text(encoding="utf-8")
    naam = concept.split("\n")[0].lstrip("# ").strip()
    alle = barrieres()
    onbekend = [b for b in bar_ids if b not in alle]
    if onbekend:
        sys.exit(f"onbekende barriere(s): {onbekend}")

    titels = [alle[b]["titel"] for b in bar_ids]
    bewijs_bron = next((alle[b].get("bewijs", "") for b in bar_ids if alle[b].get("bewijs")), "")

    def lijst(kop: str) -> str:
        blok = sectie(concept, kop)
        return blok if blok and blok != "(geen)" else ""

    uitleg = sectie(concept, "Zo leg je het uit")
    regels = [
        "---",
        f"titel: {naam}",
        "vakgebied: security",
        "type: handleiding",
        "normen: [BIO2]",
        "versie: 2026-09",
        "herkomst: patroon uit de security-shop-catalogus van security-commons-nl, herschreven als handleiding",
        "status: concept",
        f"samenvatting: TODO {sectie(concept, 'In een zin')}",
        f"barrieres: [{', '.join(bar_ids)}]",
        f"rol: {rol}",
        "---",
        "",
        f"# {naam}",
        "",
        f"> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/{mapnaam}]({SITE}/{mapnaam}/)",
        "",
        f"> **Barriere:** {'; '.join(t[0].lower() + t[1:] for t in titels)}. "
        f"{sectie(concept, 'In een zin')}",
        "",
        sectie(concept, "De gap"),
        "",
        "## Wanneer wel, wanneer niet",
        "",
        sectie(concept, "Wanneer wel, wanneer niet"),
        "",
        "## Zo richt je het in",
        "",
        sectie(concept, "Hoe het werkt"),
        "",
        lijst("Stappen"),
        "",
        "## Wat het kost en wat het oplevert",
        "",
        f"Kosten: {sectie(concept, 'Kosten') or 'onbekend'}.",
        "",
        "**Wat het oplevert**",
        "",
        lijst("Voordelen"),
        "",
        "**Waar je op moet letten**",
        "",
        lijst("Nadelen"),
        "",
        "## Bewijs",
        "",
        bewijs_bron or "TODO: wat kun je aan het eind laten zien?",
        "",
        "TODO: maak concreet welke export, rapportage of configuratie dat is.",
        "",
        "## Zo leg je het uit",
        "",
        uitleg,
        "",
        "## Hoe dit samenhangt",
        "",
        f"Deze handleiding hoort bij {'barriere' if len(bar_ids) == 1 else 'de barrieres'} "
        f"{', '.join('`' + b + '`' for b in bar_ids)} uit de "
        "[zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/). Wat je hiermee "
        "aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op "
        "[Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).",
        "",
        "## Licentie",
        "",
        "[EUPL-1.2](../../LICENSE).",
        "",
    ]
    doel = KENNISBANK / "security" / mapnaam
    doel.mkdir(parents=True, exist_ok=True)
    pad = doel / "README.md"
    pad.write_text(re.sub(r"\n{3,}", "\n\n", "\n".join(regels)), encoding="utf-8")
    return pad


if __name__ == "__main__":
    if len(sys.argv) < 5:
        sys.exit(__doc__)
    p = bouw(sys.argv[1], sys.argv[2], sys.argv[3].split(","), sys.argv[4])
    print(f"{p} geschreven; werk de TODO's bij en draai daarna leesversie.py en build.py")
