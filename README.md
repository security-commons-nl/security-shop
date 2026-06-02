# security-shop

> **Catalogus van security-patronen voor de Nederlandse publieke sector.**

Per concrete security-gap presenteert deze catalogus een **shortlist van 2–5
realistische oplossingsrichtingen** met trade-offs, mapping naar normen
(BIO 2.0, NIS2, AVG) en herbruikbare communicatie-bouwstenen voor directie,
informatiemanager en MT.

**Voor wie:** CISO/ISO bij Nederlandse gemeenten.

## Live preview

→ **<https://security-commons-nl.github.io/security-shop/>**

De live preview is een **mockup** — één self-contained HTML-bestand dat toont
hoe de toekomstige MkDocs Material-site eruit komt te zien. Bevat alle
patronen, normen-mapping, focusdreigingen-as en een keuzehulp.

## Inhoud van deze repo

| Pad | Wat |
|---|---|
| `mockup/index.html` | De live mockup (single-file, geen build) |
| `2026-05-20-security-shop-design.md` | Ontwerp van het project |
| `2026-05-22-security-shop-mvp.md` | Implementatieplan voor de MkDocs-MVP |

## Status

Mockup-fase. De productie-implementatie (MkDocs Material vanuit markdown-
bestanden onder `docs/`) volgt het plan in
[`2026-05-22-security-shop-mvp.md`](./2026-05-22-security-shop-mvp.md).

## Lokaal bekijken

```sh
cd mockup
python -m http.server 8080
# open http://localhost:8080
```

## Frame

De ruggengraat is het **CISA Zero Trust Maturity Model 2.0** (5 pillars +
3 cross-cutting capabilities). Patronen zitten in clusters onder een pillar of
capability; elk patroon vermeldt welke focusdreigingen (AP-01..05) het mitigeert.

## Licentie

EUPL-1.2 — Europese open-source-licentie. Het canonieke LICENSE-bestand volgt
(zie Task 2 van het implementatieplan).

## Bijdragen

Iedereen mag een patroon voorstellen via een pull request. Een patroon komt
binnen als `status: concept` en wordt na review door een maintainer
gepromoveerd naar `status: stabiel`. Volledige bijdrage-instructies komen
in `CONTRIBUTING.md` (volgt).

## Zusterprojecten

| Project | Doet wat |
|---|---|
| `grc-platform` | Beheer van het ISMS — controls-administratie |
| `security-posture-tool` | Meten — waar zitten de gaps |
| **`security-shop`** | **Oplossen — welke realistische opties dichten déze gap** |
| `kill-chain-analysis` | Per-CTI chokepoint-coverage-analyse (operationeel) |
| `hosting-bouwblokken` | Veilig hosten van de SC-NL-applicaties zelf |
