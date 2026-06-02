# security-shop MVP — Implementatieplan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Een werkende `security-shop` MVP opleveren: een MkDocs-site met repo-skelet, templates, 8 pillar-pagina's en 5 patronen rond detectie/SOC-sourcing.

**Architecture:** Markdown is de enige bron; een gegenereerde statische site (MkDocs Material) is de presentatie. Site-content staat onder `docs/` (MkDocs-conventie — dit verfijnt §10 van de spec, dat `patterns/` e.d. op root plaatste). `templates/` en de planningsdocumenten (ontwerp + plan, in de projectroot) vallen buiten de site-build. Verificatie per taak is `mkdocs build --strict` (faalt bij kapotte links of pagina's buiten de nav) plus visuele controle via `mkdocs serve`.

**Tech Stack:** Markdown + YAML-frontmatter, MkDocs + mkdocs-material (Python), git. Windows/PowerShell omgeving.

**Spec:** `2026-05-20-security-shop-design.md` (projectroot) — leidend. Bij twijfel: de spec wint, dit plan verfijnt alleen de fysieke MkDocs-layout.

**Aard van dit plan:** dit is een content-project, geen code-project. Voor configuratiebestanden staat de exacte inhoud in het plan. Voor proza-documenten (patronen, pillar-pagina's, prompts) geeft het plan een **inhoudsbrief**: verplichte secties, te dekken kernpunten, mappings en acceptatiecriteria. De uitvoerder schrijft het proza op basis van de brief en `STIJL.md`.

**Vooraf (buiten dit plan, door de projecteigenaar):** de werkmap heet nog `security-architecture`; hernoemen naar `security-shop` mag op elk moment — een git-repo en bestanden verhuizen mee. Het plan werkt in de huidige map.

---

## Bestandsstructuur

```
security-shop/                         (nu: security-architecture/)
├── docs/                              # MkDocs-content root — uitsluitend site-content
│   ├── index.md                       # winkel-voorpagina
│   ├── pillars/                       # 8 beschrijvingspagina's
│   │   ├── identity.md
│   │   ├── devices.md
│   │   ├── networks.md
│   │   ├── applications.md
│   │   ├── data.md
│   │   ├── visibility-analytics.md
│   │   ├── automation-orchestration.md
│   │   └── governance.md
│   ├── patterns/                      # de patronen (plat, ID-geprefixt)
│   │   ├── visibility-centrale-logverzameling.md
│   │   ├── visibility-co-managed-siem.md
│   │   ├── visibility-uitbestede-soc-mssp.md
│   │   ├── visibility-mdr-dienst.md
│   │   └── visibility-regionaal-soc.md
│   └── mappings/
│       ├── nis2.md
│       └── avg.md
├── templates/
│   ├── patroon-template.md
│   └── prompts/
│       ├── prompt-directie.md
│       ├── prompt-informatiemanager.md
│       └── prompt-mt.md
├── mkdocs.yml
├── requirements.txt
├── .gitignore
├── README.md
├── CONTRIBUTING.md
├── STIJL.md
├── LICENSE
├── 2026-05-20-security-shop-design.md  # dit ontwerp (planningsdoc, niet in de site)
└── 2026-05-22-security-shop-mvp.md     # dit implementatieplan (planningsdoc)
```

Verantwoordelijkheden:
- `mkdocs.yml` — site-config: thema, navigatie, uitsluiting van `superpowers/`.
- `templates/` — bronmateriaal voor bijdragers; geen site-content.
- `docs/pillars/` — het frame; korte uitleg per ZTMM-pillar/capability.
- `docs/patterns/` — de patronen; volgen het schema uit spec §11.
- `docs/mappings/` — NIS2- en AVG-mappingtabellen (BIO zit in de frontmatter van patronen).

---

## Task 1: Repo-skelet en MkDocs-basis

**Files:**
- Create: `.gitignore`, `requirements.txt`, `mkdocs.yml`, `docs/index.md`
- Create (mappen): `docs/pillars/`, `docs/patterns/`, `docs/mappings/`, `templates/prompts/`

- [ ] **Step 1: Git-repo initialiseren**

In de werkmap (`X:\SECURITY-COMMONS-NL\security-architecture`):

```
git init
git branch -m main
```

- [ ] **Step 2: Mappen aanmaken**

```
mkdir docs\pillars
mkdir docs\patterns
mkdir docs\mappings
mkdir templates\prompts
```

- [ ] **Step 3: `.gitignore` schrijven**

```
site/
.venv/
__pycache__/
*.pyc
.DS_Store
```

- [ ] **Step 4: `requirements.txt` schrijven**

```
mkdocs-material>=9.5
```

- [ ] **Step 5: `mkdocs.yml` schrijven**

```yaml
site_name: security-shop
site_description: Catalogus van security-patronen voor de Nederlandse publieke sector
docs_dir: docs

theme:
  name: material
  language: nl
  palette:
    - scheme: default
      primary: indigo
      accent: indigo
  features:
    - navigation.sections
    - navigation.indexes
    - navigation.top
    - content.code.copy
    - search.suggest

plugins:
  - search:
      lang: nl
  - tags

markdown_extensions:
  - admonition
  - pymdownx.details
  - attr_list
  - tables
  - toc:
      permalink: true

nav:
  - Home: index.md
```

- [ ] **Step 6: `docs/index.md` schrijven (voorlopige voorpagina)**

```markdown
# security-shop

Catalogus van security-patronen voor de Nederlandse publieke sector.

Je weet welke gap je hebt — dit project laat zien welke realistische manieren
er zijn om die te dichten, met trade-offs en een verwijzing naar de norm.

Geen leveranciers, geen prijzen — patronen waarmee je kunt kiezen.

*De winkel-voorpagina wordt afgerond in Task 12.*
```

- [ ] **Step 7: MkDocs installeren en strict build draaien**

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
mkdocs build --strict
```

Expected: build slaagt, map `site/` verschijnt, geen warnings/errors.

- [ ] **Step 8: Commit**

```
git add .gitignore requirements.txt mkdocs.yml docs/index.md
git commit -m "chore: repo-skelet en MkDocs-basis"
```

---

## Task 2: Projectdocumentatie — README, CONTRIBUTING, STIJL

**Files:**
- Create: `README.md`, `CONTRIBUTING.md`, `STIJL.md`, `LICENSE`

- [ ] **Step 1: `README.md` schrijven**

Inhoudsbrief — dek deze punten:
- Eén-alinea pitch: catalogus van security-patronen; je komt met een gap, je vertrekt met een shortlist van oplossingsrichtingen + trade-offs + norm-verwijzing.
- Voor wie: CISO/ISO bij Nederlandse gemeenten.
- Onderscheid met zusterprojecten (tabel uit spec §4: grc-platform / security-posture-tool / security-shop / hosting-bouwblokken).
- Hoe het werkt: frame = CISA ZTMM 2.0 (5 pillars + 3 cross-cutting); patronen getagd met BIO 2.0; statische site via MkDocs.
- Lokaal draaien: `pip install -r requirements.txt` + `mkdocs serve`.
- Verwijzing naar `CONTRIBUTING.md` en de licentie.
- Acceptatie: een nieuwe lezer snapt in 2 minuten wat het project is en hoe de site lokaal te draaien.

- [ ] **Step 2: `CONTRIBUTING.md` schrijven**

Inhoudsbrief — dek deze punten:
- Het gelaagde-status-model (spec §13): voorstellen is vrij; een patroon komt binnen als `status: concept`; een maintainer promoveert via `review` naar `stabiel`.
- Hoe een patroon voorstellen: kopieer `templates/patroon-template.md` naar `docs/patterns/`, vul in, open een PR.
- **Review-checklist concept → stabiel** (expliciete lijst):
  1. Frontmatter volledig en geldig YAML, alle velden uit spec §11.1 aanwezig.
  2. Alle 9 body-secties uit spec §11.2 ingevuld, niets leeg.
  3. Substantie: het patroon zegt iets specifieks; geen open deuren.
  4. Productneutraal: geen leverancier aangeprezen; voorbeelden mogen, vergelijking niet.
  5. Toon voldoet aan `STIJL.md`.
  6. `mapping.bio` gecontroleerd; NIS2/AVG indien van toepassing.
  7. `verwant`-verwijzingen kloppen (bestaande pattern-ID's).
  8. `mkdocs build --strict` slaagt.
- Verwijzing naar `STIJL.md`.
- Acceptatie: iemand zonder Git-ervaring snapt hoe bij te dragen; een reviewer heeft een afvinkbare checklist.

- [ ] **Step 3: `STIJL.md` schrijven**

Inhoudsbrief — de schrijfwijzer (spec §12). Dek:
- Doel: één gedeelde, neutrale, professionele toon — niemands persoonlijke stem.
- Regels: concreet boven abstract; stellig boven omfloerst; geen vulwoorden; elke claim onderbouwd of weggelaten; korte zinnen; Nederlands; vakterm uitleggen bij eerste gebruik.
- Expliciet: geen marketingtaal, geen leveranciersjargon, geen "AI-slop" (generieke alineas die niets toevoegen).
- Eén goed en één fout voorbeeld ter illustratie.
- Acceptatie: een reviewer kan met `STIJL.md` in de hand een tekst objectief toetsen.

- [ ] **Step 4: `LICENSE` aanmaken**

De spec (§15) noemt EUPL-1.2 als waarschijnlijke keuze. Bevestig dit met de projecteigenaar. Plaats vervolgens de officiële canonieke EUPL-1.2-tekst (Engelse versie) als `LICENSE`, opgehaald van de officiële EU-bron. Niet zelf parafraseren.

- [ ] **Step 5: Strict build en commit**

```
mkdocs build --strict
git add README.md CONTRIBUTING.md STIJL.md LICENSE
git commit -m "docs: README, CONTRIBUTING, STIJL en licentie"
```

Expected: build slaagt (deze bestanden staan op root, buiten `docs/`, dus niet in de site — geen nav-warning).

---

## Task 3: Patroon-template

**Files:**
- Create: `templates/patroon-template.md`

- [ ] **Step 1: `templates/patroon-template.md` schrijven**

Exacte inhoud — de invulbare template volgens spec §11. Frontmatter met lege/voorbeeldwaarden, body met de 9 vaste secties als koppen plus een korte invul-instructie per sectie:

```markdown
---
id: PILLAR-KORTE-NAAM
naam: 
pillar: []                       # identity / devices / networks / applications / data
cross-cutting: []                # visibility-analytics / automation-orchestration / governance
maturity:                        # traditional / initial / advanced / optimal
context:
  hosting: []                    # cloud / hybride / on-prem
  omvang: []                     # klein / middel / groot
  budget:                        # laag / midden / hoog
mapping:
  bio: []                        # BIO 2.0-maatregelen (ISO 27002:2022-nummering)
  nis2: []                       # optioneel
  avg: []                        # optioneel
verwant:
  alternatief-voor: []
  vereist: []
  vult-aan: []
prompt-aandachtspunten: ""
status: concept
herzien: JJJJ-MM-DD
---

# {naam}

## In één zin
<!-- De pitch: wat lost dit patroon op, in één zin. -->

## De gap
<!-- Welk concreet, herkenbaar probleem. -->

## Wanneer dit past — en wanneer niet
<!-- Eerlijk over de anti-context: in welke situatie juist niet. -->

## Hoe het werkt
<!-- Het mechanisme op architectuur-niveau. Geen implementatiestappen. -->

## Implementatie-richting
<!-- Stappenplan op hoofdlijnen, ~5-10 genummerde stappen, productneutraal. -->

## Voordelen

## Nadelen & risico's

## Inspanning & kosten
<!-- Eenmalig én doorlopend beheer. Grove indicatie, kwalitatief. Geen prijzen. -->

## Communicatie & draagvlak
<!-- Drie kernboodschappen van 2-3 zinnen, plak- én spreekbaar. -->

### Voor directie/college
### Voor de informatiemanager
### Voor het MT
```

- [ ] **Step 2: Commit**

```
git add templates/patroon-template.md
git commit -m "docs: patroon-template volgens schema"
```

---

## Task 4: Communicatie-prompts

**Files:**
- Create: `templates/prompts/prompt-directie.md`, `templates/prompts/prompt-informatiemanager.md`, `templates/prompts/prompt-mt.md`

- [ ] **Step 1: `prompt-directie.md` schrijven**

Inhoudsbrief — een generieke prompt-template die een taalmodel instrueert om van een kernboodschap een afgerond directie/college-stuk te maken. Dek:
- Rol/doel: maak een collegevoorstel of raadsbrief-paragraaf voor directie/college — die bezitten besluit + budget.
- Placeholders die de CISO invult: `{kernboodschap}`, `{patroon-naam}`, `{lokale context}` (huidige situatie, budget-realiteit, politieke gevoeligheid).
- Instructie: focus op risico, kosten-orde en het te nemen besluit; bestuurlijke taal; kort.
- Verplichte "maak het van jou"-stap: vraag de CISO expliciet om lokale context in te voegen; lever geen kant-en-klare generieke tekst.
- Neutrale toon conform `STIJL.md` — geen persoonlijke huisstijl.

- [ ] **Step 2: `prompt-informatiemanager.md` schrijven**

Zelfde structuur, andere doelgroep: de informatiemanager bezit inpassing in landschap & roadmap. Output = architectuurnotitie/impactanalyse. Focus: wat verandert er in het landschap, afhankelijkheden, impact op andere systemen, roadmap-gevolg.

- [ ] **Step 3: `prompt-mt.md` schrijven**

Zelfde structuur, doelgroep MT: bezit uitvoering in de lijn. Output = MT-stuk. Focus: gevolgen voor mensen en processen, wat is nodig van het team, planning.

- [ ] **Step 4: Commit**

```
git add templates/prompts/
git commit -m "docs: drie communicatie-prompt-templates"
```

---

## Task 5: Pillar-beschrijvingspagina's

**Files:**
- Create: `docs/pillars/identity.md`, `devices.md`, `networks.md`, `applications.md`, `data.md`, `visibility-analytics.md`, `automation-orchestration.md`, `governance.md`
- Modify: `mkdocs.yml` (nav)

- [ ] **Step 1: De 8 pillar-pagina's schrijven**

Inhoudsbrief per pagina — kort (½ tot 1 scherm). Elke pagina dekt:
- Wat deze pillar/capability is, in gewone taal (gebruik de één-zin-omschrijvingen uit spec §7).
- 2–4 typische gemeentelijke gaps die hier thuishoren.
- Of het een pillar of een cross-cutting capability is (en bij cross-cutting: dat het door alle pillars heen loopt).
- Voor `visibility-analytics.md`: vermeld dat hier de eerste 5 MVP-patronen liggen en link ernaar.
- Voor de overige 7: een eerlijke "nog geen patronen — dit groeit"-notitie.

Gebruik de tabellen uit spec §7 als bron. Toon conform `STIJL.md`.

- [ ] **Step 2: `mkdocs.yml` nav uitbreiden**

Voeg onder `nav:` toe:

```yaml
  - Pillars:
      - pillars/identity.md
      - pillars/devices.md
      - pillars/networks.md
      - pillars/applications.md
      - pillars/data.md
      - pillars/visibility-analytics.md
      - pillars/automation-orchestration.md
      - pillars/governance.md
```

- [ ] **Step 3: Strict build en commit**

```
mkdocs build --strict
git add docs/pillars/ mkdocs.yml
git commit -m "docs: 8 pillar-beschrijvingspagina's"
```

Expected: build slaagt, alle 8 pagina's in de nav, geen "not in nav"-warning.

---

## Task 6: Mapping-tabellen NIS2 en AVG

**Files:**
- Create: `docs/mappings/nis2.md`, `docs/mappings/avg.md`
- Modify: `mkdocs.yml` (nav)

- [ ] **Step 1: `docs/mappings/nis2.md` schrijven**

Inhoudsbrief:
- Korte uitleg: NIS2 art. 21 lid 2 somt beveiligingsmaatregelen op; deze tabel koppelt die aan patronen.
- Tabel: NIS2-maatregel (art. 21.2 a–j) → relevante patronen (vooralsnog de detectie/SOC-patronen, m.n. onder 21.2(b) incidentafhandeling).
- Disclaimer: indicatief, geen formele NIS2-conformiteitsverklaring.

- [ ] **Step 2: `docs/mappings/avg.md` schrijven**

Inhoudsbrief:
- Korte uitleg: AVG art. 32 (beveiliging van verwerking) en art. 33 (meldplicht datalekken) zijn de relevante haakjes; detectie maakt tijdig melden mogelijk.
- Tabel: AVG-artikel → relevante patronen.
- Zelfde disclaimer.

- [ ] **Step 3: `mkdocs.yml` nav uitbreiden**

```yaml
  - Normen:
      - mappings/nis2.md
      - mappings/avg.md
```

- [ ] **Step 4: Strict build en commit**

```
mkdocs build --strict
git add docs/mappings/ mkdocs.yml
git commit -m "docs: NIS2- en AVG-mappingtabellen"
```

---

## Task 7: Patroon — Centrale logverzameling

**Files:**
- Create: `docs/patterns/visibility-centrale-logverzameling.md`
- Modify: `mkdocs.yml` (nav)

- [ ] **Step 1: Het patroon schrijven**

Volg `templates/patroon-template.md` en spec §11. Frontmatter:
- `id: VIS-CENTRALE-LOGVERZAMELING`, `naam: Centrale logverzameling`
- `pillar: []`, `cross-cutting: [visibility-analytics]`, `maturity: initial`
- `context: hosting: [cloud, hybride, on-prem]`, `omvang: [klein, middel, groot]`, `budget: laag`
- `mapping: bio: [8.15, 8.16, 8.17]` (Logging, Monitoring, Kloksynchronisatie), `nis2: [21.2b]`, `avg: [32, 33]`
- `verwant: vereist: []`, `vult-aan: [VIS-CO-MANAGED-SIEM, VIS-UITBESTEDE-SOC-MSSP, VIS-MDR-DIENST, VIS-REGIONAAL-SOC]`
- `status: concept`

Body — inhoudsbrief per sectie:
- **In één zin:** logs van systemen, applicaties en netwerk centraal verzamelen en bewaren — de fundering onder elke vorm van detectie.
- **De gap:** logs staan verspreid, lokaal, kort bewaard; bij een incident is er niets te reconstrueren.
- **Wanneer wel/niet:** altijd zinvol; dit is een randvoorwaarde voor patronen 2–5. "Niet": als losse stap zonder vervolg blijft het een datakerkhof.
- **Hoe het werkt:** logbronnen → log-forwarders/agents → centrale opslag (logserver/log-store); normalisatie en retentie; kloksynchronisatie zodat tijdlijnen kloppen.
- **Implementatie-richting:** ~6–8 stappen — inventariseer logbronnen; bepaal retentietermijn (mede o.b.v. AVG); kies centrale opslag (open-source mogelijk); richt forwarders in; standaardiseer tijd (NTP); test reconstructie; beleg beheer.
- **Voordelen:** randvoorwaarde voor detectie; bewijs bij incidenten; relatief lage drempel; leverancier-onafhankelijk.
- **Nadelen & risico's:** logopslag bevat gevoelige data (zelf te beschermen); zonder analyse (SIEM/SOC) nog geen detectie; opslagkosten groeien.
- **Inspanning & kosten:** budget laag — vooral inrichtings- en beheerinspanning; open-source houdt licentiekosten laag. Doorlopend: beheer, retentiebewaking.
- **Communicatie & draagvlak:** drie kernboodschappen — directie (zonder dit geen zicht en geen bewijs bij incidenten; beperkte investering), informatiemanager (raakt elk systeem dat logs levert; standaardiseren loont), MT (lijnteams moeten logbronnen aanleveren en aangesloten houden).

- [ ] **Step 2: `mkdocs.yml` nav uitbreiden**

Voeg een sectie `Patronen` toe met dit bestand:

```yaml
  - Patronen:
      - patterns/visibility-centrale-logverzameling.md
```

- [ ] **Step 3: Strict build en commit**

```
mkdocs build --strict
git add docs/patterns/visibility-centrale-logverzameling.md mkdocs.yml
git commit -m "feat: patroon Centrale logverzameling"
```

Acceptatie: alle 9 body-secties ingevuld; frontmatter geldig; build slaagt.

---

## Task 8: Patroon — Co-managed SIEM

**Files:**
- Create: `docs/patterns/visibility-co-managed-siem.md`
- Modify: `mkdocs.yml` (nav)

- [ ] **Step 1: Het patroon schrijven**

Frontmatter:
- `id: VIS-CO-MANAGED-SIEM`, `naam: Co-managed SIEM`
- `pillar: []`, `cross-cutting: [visibility-analytics]`, `maturity: advanced`
- `context: hosting: [cloud, hybride]`, `omvang: [middel, groot]`, `budget: hoog`
- `mapping: bio: [8.15, 8.16, 5.25, 5.26]`, `nis2: [21.2b]`, `avg: [32, 33]`
- `verwant: vereist: [VIS-CENTRALE-LOGVERZAMELING]`, `alternatief-voor: [VIS-UITBESTEDE-SOC-MSSP, VIS-MDR-DIENST, VIS-REGIONAAL-SOC]`
- `status: concept`

Body — inhoudsbrief:
- **In één zin:** een SIEM die de gemeente zelf bezit, maar samen met een partij beheert — de gemeente houdt regie, de partij brengt schaal en kennis.
- **De gap:** logs zijn er wel (patroon 1), maar niemand analyseert ze; aanvallen worden niet gezien.
- **Wanneer wel/niet:** past bij middel/grote gemeenten die regie willen houden en eigen analisten (deels) hebben. Niet voor kleine gemeenten zonder eigen securitycapaciteit.
- **Hoe het werkt:** SIEM-platform verzamelt en correleert logs; detectieregels genereren alerts; gedeeld bedienmodel — gemeente doet een deel, partner een deel (vaak buiten kantooruren).
- **Implementatie-richting:** ~6–8 stappen — patroon 1 als basis; kies SIEM-platform; bepaal taakverdeling gemeente/partner; stel use-cases/detectieregels op; richt alert-afhandeling in; oefen; evalueer use-cases periodiek.
- **Voordelen:** eigen regie en eigendom van data en regels; opbouw van eigen kennis; flexibel.
- **Nadelen & risico's:** vereist eigen capaciteit en volwassenheid; SIEM-kosten en -tuning zijn fors; "alert moeheid" bij slechte tuning.
- **Inspanning & kosten:** budget hoog — platform/licenties plus eigen analisten. Doorlopend: tuning, use-case-beheer, 24/7-dekking regelen.
- **Communicatie & draagvlak:** directie (hoogste grip, maar ook hoogste eigen investering en afhankelijkheid van personeel), informatiemanager (zwaar platform in het landschap; integraties met logbronnen), MT (vraagt structureel capaciteit en roosters van het securityteam).

- [ ] **Step 2: `mkdocs.yml` nav uitbreiden** — voeg het bestand toe onder `Patronen`.

- [ ] **Step 3: Strict build en commit**

```
mkdocs build --strict
git add docs/patterns/visibility-co-managed-siem.md mkdocs.yml
git commit -m "feat: patroon Co-managed SIEM"
```

---

## Task 9: Patroon — Uitbestede SOC (MSSP)

**Files:**
- Create: `docs/patterns/visibility-uitbestede-soc-mssp.md`
- Modify: `mkdocs.yml` (nav)

- [ ] **Step 1: Het patroon schrijven**

Frontmatter:
- `id: VIS-UITBESTEDE-SOC-MSSP`, `naam: Uitbestede SOC (MSSP)`
- `pillar: []`, `cross-cutting: [visibility-analytics]`, `maturity: advanced`
- `context: hosting: [cloud, hybride, on-prem]`, `omvang: [klein, middel, groot]`, `budget: midden`
- `mapping: bio: [8.15, 8.16, 5.25, 5.26]`, `nis2: [21.2b]`, `avg: [32, 33]`
- `verwant: vereist: [VIS-CENTRALE-LOGVERZAMELING]`, `alternatief-voor: [VIS-CO-MANAGED-SIEM, VIS-MDR-DIENST, VIS-REGIONAAL-SOC]`
- `status: concept`

Body — inhoudsbrief:
- **In één zin:** monitoring en detectie volledig uitbesteed aan een Managed Security Service Provider.
- **De gap:** geen eigen securityteam, en dat is er ook niet snel — toch is detectie nodig.
- **Wanneer wel/niet:** past als de gemeente geen eigen SOC kan/wil opbouwen. Niet als de gemeente juist eigen kennis wil opbouwen of maximale regie eist.
- **Hoe het werkt:** de MSSP neemt logs af, draait detectie op eigen platform, levert alerts/rapportages; de gemeente handelt incidenten af of belegt ook dat bij de provider.
- **Implementatie-richting:** ~6–8 stappen — patroon 1 als basis; eisen en scope opstellen; aanbesteden/contracteren; logkoppeling inrichten; afspraken over escalatie en responstijden (SLA); rollen aan gemeentekant beleggen; periodiek de dienst evalueren.
- **Voordelen:** snel operationeel; geen eigen 24/7-team nodig; voorspelbare dienstkosten.
- **Nadelen & risico's:** afhankelijkheid van leverancier; minder eigen kennisopbouw; MSSP kent de lokale context beperkt; exit/overstap is lastig.
- **Inspanning & kosten:** budget midden — dienstcontract i.p.v. eigen team. Doorlopend: contract- en leveranciersmanagement, kwaliteit bewaken.
- **Communicatie & draagvlak:** directie (snelste weg naar detectie zonder eigen team; afhankelijkheid is de prijs), informatiemanager (logkoppeling en dataverwerkersafspraken met de MSSP), MT (lichtere belasting eigen team, wel iemand nodig voor regie op het contract).

- [ ] **Step 2: `mkdocs.yml` nav uitbreiden** — voeg het bestand toe onder `Patronen`.

- [ ] **Step 3: Strict build en commit**

```
mkdocs build --strict
git add docs/patterns/visibility-uitbestede-soc-mssp.md mkdocs.yml
git commit -m "feat: patroon Uitbestede SOC (MSSP)"
```

---

## Task 10: Patroon — MDR-dienst

**Files:**
- Create: `docs/patterns/visibility-mdr-dienst.md`
- Modify: `mkdocs.yml` (nav)

- [ ] **Step 1: Het patroon schrijven**

Frontmatter:
- `id: VIS-MDR-DIENST`, `naam: MDR-dienst (Managed Detection & Response)`
- `pillar: []`, `cross-cutting: [visibility-analytics]`, `maturity: advanced`
- `context: hosting: [cloud, hybride]`, `omvang: [klein, middel, groot]`, `budget: hoog`
- `mapping: bio: [8.15, 8.16, 5.7, 5.25, 5.26]`, `nis2: [21.2b]`, `avg: [32, 33]`
- `verwant: vereist: [VIS-CENTRALE-LOGVERZAMELING]`, `alternatief-voor: [VIS-CO-MANAGED-SIEM, VIS-UITBESTEDE-SOC-MSSP, VIS-REGIONAAL-SOC]`
- `status: concept`

Body — inhoudsbrief:
- **In één zin:** een dienst die niet alleen detecteert maar ook actief reageert — inclusief ingrijpen bij een aanval.
- **De gap:** alleen alerts krijgen is niet genoeg; er is niemand die 's nachts daadwerkelijk ingrijpt.
- **Wanneer wel/niet:** past als snelle, actieve respons nodig is en de gemeente bereid is mandaat voor ingrijpen te geven. Niet als de gemeente elke actie zelf wil houden, of als het budget krap is.
- **Hoe het werkt:** MDR combineert detectie (vaak endpoint-gericht) met een responsteam dat namens de gemeente containment-acties uitvoert, binnen vooraf afgesproken mandaat.
- **Implementatie-richting:** ~6–8 stappen — patroon 1 als basis; bepaal welk mandaat de dienst krijgt (wat mag automatisch worden afgesloten/geïsoleerd); contracteren; endpoint-/log-koppeling; afspraken over communicatie tijdens incidenten; oefenen met een scenario; evalueren.
- **Voordelen:** snelste daadwerkelijke respons; 24/7 zonder eigen team; beperkt de schade van een aanval actief.
- **Nadelen & risico's:** premium-kosten; je geeft handelingsmandaat uit handen; afhankelijkheid; vereist heldere afspraken over wat de dienst wél/niet mag.
- **Inspanning & kosten:** budget hoog — premium dienst. Doorlopend: mandaat- en contractbeheer, afstemming bij incidenten.
- **Communicatie & draagvlak:** directie (kortste tijd-tot-respons, maar duur en je geeft ingrijp-mandaat weg — dat is een bestuurlijk besluit), informatiemanager (endpoint-dekking en koppelingen; afspraken over geautomatiseerde acties), MT (team hoeft niet 's nachts te draaien, wel oefenen en bereikbaar zijn voor opschaling).

- [ ] **Step 2: `mkdocs.yml` nav uitbreiden** — voeg het bestand toe onder `Patronen`.

- [ ] **Step 3: Strict build en commit**

```
mkdocs build --strict
git add docs/patterns/visibility-mdr-dienst.md mkdocs.yml
git commit -m "feat: patroon MDR-dienst"
```

---

## Task 11: Patroon — Regionaal/gedeeld SOC

**Files:**
- Create: `docs/patterns/visibility-regionaal-soc.md`
- Modify: `mkdocs.yml` (nav)

- [ ] **Step 1: Het patroon schrijven**

Frontmatter:
- `id: VIS-REGIONAAL-SOC`, `naam: Regionaal/gedeeld SOC-samenwerkingsverband`
- `pillar: []`, `cross-cutting: [visibility-analytics]`, `maturity: advanced`
- `context: hosting: [cloud, hybride, on-prem]`, `omvang: [klein, middel]`, `budget: midden`
- `mapping: bio: [8.15, 8.16, 5.25, 5.26]`, `nis2: [21.2b]`, `avg: [32, 33]`
- `verwant: vereist: [VIS-CENTRALE-LOGVERZAMELING]`, `alternatief-voor: [VIS-CO-MANAGED-SIEM, VIS-UITBESTEDE-SOC-MSSP, VIS-MDR-DIENST]`
- `status: concept`

Body — inhoudsbrief:
- **In één zin:** meerdere gemeenten delen samen één SOC — gedeelde kosten, gedeelde kennis.
- **De gap:** een eigen SOC is te duur voor één (kleine) gemeente, en volledig uitbesteden voelt te ver van huis.
- **Wanneer wel/niet:** past bij kleine/middelgrote gemeenten in een bestaand samenwerkingsverband. Niet als er geen samenwerkingspartners zijn of de governance-bereidheid ontbreekt.
- **Hoe het werkt:** deelnemende gemeenten brengen logs/middelen samen; één gedeelde SOC-functie (eigen personeel, gedeelde dienst, of gehost bij een gastorganisatie); governance via een samenwerkingsovereenkomst.
- **Implementatie-richting:** ~6–8 stappen — patroon 1 als basis; partners en samenwerkingsvorm bepalen; governance en kostenverdeling afspreken; gezamenlijke scope en use-cases; dataverwerkers-/uitwisselingsafspraken (AVG); inrichten; gezamenlijk evalueren.
- **Voordelen:** kosten en schaarse expertise gedeeld; behoud van publieke regie; kennisdeling tussen gemeenten; past bij de SC-NL-gedachte.
- **Nadelen & risico's:** governance-overhead; trager besluitvormen met meerdere partijen; afhankelijk van de zwakste schakel; opstarten kost tijd.
- **Inspanning & kosten:** budget midden — gedeelde kosten, maar governance-inspanning komt erbij. Doorlopend: samenwerking onderhouden, gezamenlijk bijsturen.
- **Communicatie & draagvlak:** directie (kosten en expertise delen met behoud van publieke regie; vraagt bestuurlijke commitment aan de samenwerking), informatiemanager (gedeelde logkoppelingen en gegevensuitwisseling tussen gemeenten), MT (samenwerken met andere gemeenten in de uitvoering; gedeelde processen).

- [ ] **Step 2: `mkdocs.yml` nav uitbreiden** — voeg het bestand toe onder `Patronen`.

- [ ] **Step 3: Strict build en commit**

```
mkdocs build --strict
git add docs/patterns/visibility-regionaal-soc.md mkdocs.yml
git commit -m "feat: patroon Regionaal/gedeeld SOC"
```

---

## Task 12: Winkel-voorpagina en eindcontrole

**Files:**
- Modify: `docs/index.md`, `mkdocs.yml`

- [ ] **Step 1: `docs/index.md` afronden**

Inhoudsbrief — de winkel-voorpagina. Dek:
- De pitch (uit Task 1, behouden/aanscherpen).
- Hoe het werkt in 3 stappen: kies je pillar/afdeling → vergelijk de patronen voor jouw gap → gebruik trade-offs, norm-verwijzing en communicatie-bouwstenen.
- Een uitgelicht blok: "Eerste cluster — detectie & SOC-sourcing" met links naar de 5 patronen en de regel dat patroon 1 de fundering is.
- Korte uitleg van het `concept`-label (gelaagde status, spec §13).
- Link naar de pillars-overzichtspagina's en `CONTRIBUTING.md`.

- [ ] **Step 2: Nav-controle in `mkdocs.yml`**

Controleer dat de volledige `nav` klopt: Home, Pillars (8), Patronen (5), Normen (2). Volgorde van de patronen: centrale-logverzameling eerst (de fundering).

- [ ] **Step 3: Strict build en visuele controle**

```
mkdocs build --strict
mkdocs serve
```

Open `http://127.0.0.1:8000`. Controleer:
- Alle 8 pillar-pagina's, 5 patronen en 2 mappingpagina's zijn bereikbaar via de nav.
- De voorpagina-links werken.
- Search werkt (Nederlands).
- De planningsdocumenten in de projectroot verschijnen **niet** in de site (ze staan buiten `docs/`).

- [ ] **Step 4: Commit**

```
git add docs/index.md mkdocs.yml
git commit -m "feat: winkel-voorpagina en nav afgerond"
```

- [ ] **Step 5: Afrondende controle tegen de spec**

Loop spec §14 na: 5 patronen aanwezig, geconcentreerd in Visibility & Analytics, patroon 1 als fundering met `verwant`-koppelingen naar 2–5. Loop §11 na: elk patroon heeft volledige frontmatter en 9 body-secties.

---

## Self-Review (uitgevoerd bij het schrijven van dit plan)

**Spec-dekking:** §16 van de spec is de scope. Punt 1 (m-rename) is een handmatige pre-stap, genoteerd. Punt 2 (git-init) = Task 1. Punt 3 (skelet/config/README/CONTRIBUTING/STIJL/LICENSE) = Task 1–2. Punt 4 (prompts) = Task 4. Punt 5 (patroon-template) = Task 3. Punt 6 (8 pillar-pagina's) = Task 5. Punt 7 (5 MVP-patronen) = Task 7–11. Punt 8 (NIS2/AVG-mappings) = Task 6. Alle punten gedekt.

**Placeholder-scan:** configuratiebestanden hebben exacte inhoud; proza-documenten hebben een concrete inhoudsbrief met verplichte secties en kernpunten — geen "TBD". De EUPL-tekst wordt bewust niet geparafraseerd maar opgehaald van de officiële bron.

**Type-consistentie:** pattern-ID's consistent (`VIS-CENTRALE-LOGVERZAMELING`, `VIS-CO-MANAGED-SIEM`, `VIS-UITBESTEDE-SOC-MSSP`, `VIS-MDR-DIENST`, `VIS-REGIONAAL-SOC`); `verwant`-verwijzingen tussen patronen verwijzen alleen naar deze vijf ID's; bestandsnamen `visibility-*` consistent; frontmatter-velden volgen spec §11.1.

**Aandachtspunt voor de uitvoerder:** de spec §10 is bijgewerkt naar de MkDocs-layout (site-content onder `docs/`); plan en spec zijn consistent.
