"""Zet de patronen uit de mockup om naar markdown-concepten, een bestand per patroon, in _dump/.

De catalogus leeft als JavaScript-objecten in mockup/index.html. Dat is prima om een mockup mee te
tonen, maar niet om uit te schrijven. Dit script haalt de velden eruit zodat je per patroon een leesbaar
concept hebt.

De concepten zijn **grondstof**, geen kennisbank-items. Elke handleiding wordt daaruit met de hand
geschreven volgens de vaste koppen (zie kennisbank/CONTRIBUTING.md): een catalogus beschrijft
("dit patroon..."), een handleiding spreekt de lezer aan ("je richt in...").

Gebruik:
    python tools/dump.py
"""
from __future__ import annotations

import pathlib
import re

HIER = pathlib.Path(__file__).resolve().parent.parent
UIT = HIER / "_dump"


def blok() -> str:
    tekst = (HIER / "mockup" / "index.html").read_text(encoding="utf-8")
    start = tekst.find("const PATTERNS")
    if start < 0:
        raise SystemExit("PATTERNS niet gevonden in mockup/index.html")
    return tekst[start:tekst.find("];", start)]


def veld(naam: str, bron: str) -> str:
    m = re.search(naam + r':\s*"((?:[^"\\]|\\.)*)"', bron)
    return m.group(1).replace('\\"', '"') if m else ""


def lijst(naam: str, bron: str) -> list[str]:
    m = re.search(naam + r":\s*\[(.*?)\]", bron, re.S)
    return [s.replace('\\"', '"') for s in re.findall(r'"((?:[^"\\]|\\.)*)"', m.group(1))] if m else []


def concept(p: str) -> tuple[str, str]:
    slug = veld("slug", p)
    comm = re.search(r"comm:\s*\{(.*?)\n\s*\}", p, re.S)
    comm = comm.group(1) if comm else ""

    regels = [
        f"# {veld('naam', p)}",
        "",
        f"- slug: `{slug}`",
        f"- rol in de catalogus: {veld('role', p)}",
        f"- BIO 2.0: {', '.join(lijst('bio', p)) or 'geen'}",
        f"- NIS2: {', '.join(lijst('nis2', p)) or 'geen'}",
        f"- AVG: {', '.join(lijst('avg', p)) or 'geen'}",
        "",
        "## In een zin",
        veld("one", p),
        "",
        "## De gap",
        veld("gap", p),
        "",
        "## Wanneer wel, wanneer niet",
        veld("wanneer", p),
        "",
        "## Hoe het werkt",
        veld("hoe", p),
        "",
        "## Stappen",
    ]
    regels += [f"{i}. {s}" for i, s in enumerate(lijst("stappen", p), 1)] or ["(geen)"]
    regels += ["", "## Voordelen"] + ([f"- {s}" for s in lijst("voordelen", p)] or ["(geen)"])
    regels += ["", "## Nadelen"] + ([f"- {s}" for s in lijst("nadelen", p)] or ["(geen)"])
    regels += ["", "## Kosten", veld("kosten", p)]
    regels += ["", "## Zo leg je het uit",
               f"**Aan de directie.** {veld('directie', comm)}", "",
               f"**Aan de informatiemanager.** {veld('im', comm)}", "",
               f"**Aan het MT.** {veld('mt', comm)}", ""]
    return slug, "\n".join(regels)


if __name__ == "__main__":
    UIT.mkdir(exist_ok=True)
    aantal = 0
    for stuk in re.split(r"\n\s*\{\s*\n", blok()):
        if "slug:" not in stuk:
            continue
        slug, tekst = concept(stuk)
        (UIT / f"{slug}.md").write_text(tekst, encoding="utf-8")
        aantal += 1
    print(f"{aantal} patronen naar {UIT}")
