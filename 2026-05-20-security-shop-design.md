# security-shop — ontwerp

**Status:** Ontwerp compleet — klaar voor review, daarna een implementatieplan.
**Gestart:** 2026-05-20 · **Laatst bijgewerkt:** 2026-05-22
**Auteur:** Bas Stevens (sparring met Claude)
**Project:** `X:\SECURITY-COMMONS-NL\security-shop\` → toekomstige repo `github.com/security-commons-nl/security-shop`

> Let op: de werkmap heet nog `security-architecture`; de hernoeming naar `security-shop` staat open (zie §16).

---

## 1. Doel

`security-shop` is een **catalogus van security-patronen** voor de Nederlandse publieke sector. Per concrete gap presenteert het een **shortlist van realistische oplossingsrichtingen** met trade-offs, mapping naar normen, een stappenplan op hoofdlijnen, en herbruikbare communicatie-bouwstenen.

Het project bedient één hoofdscenario:

> De CISO/ISO weet dat hij/zij een gap heeft — bijvoorbeeld geen fatsoenlijk SIEM, of MFA dekt admins niet, of logging is niet centraal — en wil zien welke realistische manieren er zijn om die gap te dichten: inkopen, bestaande dienst uitbreiden, open-source erin, of zelf bouwen. Met voor- en nadelen, een norm-verwijzing, en tekst die direct in een memo past.

## 2. Primaire gebruiker

**CISO of ISO bij een Nederlandse gemeente.** Zij/hij heeft BIO 2.0, AVG en NIS2 in portefeuille en moet keuzes maken én verantwoorden richting directie, college, auditor en architecten.

Secundaire gebruikers (geen ontwerpfocus, maar moeten niet uitgesloten worden):
- Externe adviseurs/consultants die meerdere gemeenten ondersteunen
- Architecten/infra-engineers die op een gap stuiten en willen weten welke richtingen passen

## 3. Tastbare uitkomst

De CISO/ISO loopt weg met:

1. **Een shortlist van 2–5 patronen** die de gap kunnen dichten — elk met voor/nadelen, kosten-indicatie, context-passendheid (cloud/on-prem, schaal, volwassenheid) en norm-verwijzing.
2. **Communicatie-bouwstenen per patroon** — drie korte kernboodschappen (directie / informatiemanager / MT), plus generieke prompt-templates die met de lokale context van de CISO een afgerond stuk produceren (collegevoorstel, architectuurnotitie, MT-stuk).

Geen losse "memo-generator" en geen interactieve beslisboom — dat is bewust uitgesloten in MVP (zie §5).

## 4. Plek t.o.v. zusterprojecten

| Project | Doet wat |
|---|---|
| `grc-platform` | Beheer van het ISMS — wélke controls zijn er, hoe staat het ervoor |
| `security-posture-tool` | Meten — wáár zitten de gaps |
| **`security-shop`** | **Oplossen — welke realistische opties zijn er om déze gap te dichten** |
| `hosting-bouwblokken` | Hosten van de SC-NL applicaties zélf (anonimizer, beleid-assistent, grc-platform) — IaC, Docker, Azure |

Let op de afbakening met `hosting-bouwblokken`: dat project gaat over het *hosten van de SC-NL applicaties*, niet over het implementeren van willekeurige security-patronen. Een patroon in security-shop draagt daarom z'n **eigen** implementatie-richting (stappenplan op hoofdlijnen). Alleen een patroon dat écht over het hosten van een SC-NL tool gaat, verwijst naar `hosting-bouwblokken`.

## 5. Wat het project **niet** is (non-doelen)

- **Geen GRC-platform** — controls-beheer, evidence en compliance-status horen in `grc-platform`.
- **Geen gap-detectie** — meten waar de gaps zitten, doet `security-posture-tool`.
- **Geen IaC-bibliotheek.** De implementatie-sectie van een patroon is een stappenplan op hoofdlijnen — géén Terraform, Compose of scripts. Diepe IaC valt buiten dit project.
- **Geen interactieve beslisboom of applicatie.** De presentatie is een *gegenereerde statische site* — geen server, geen app-logica. Een beslisboom-laag kan later bovenop dezelfde frontmatter-data.
- **Geen losse memo-generator.** Communicatie-bouwstenen leven *binnen* patronen; de prompt-templates zijn een hulpmiddel, geen aparte applicatie.
- **Geen leveranciersvergelijking of marktreview.** Een patroon noemt voorbeelden van implementaties (proprietary én open-source), maar dit project beoordeelt geen leveranciers.
- **Geen normen-encyclopedie.** BIO/ISO/NIS2/AVG worden via mapping gekoppeld, niet uitgelegd.

## 6. Metafoor en terminologie

Eén metafoor, één vakterm — niet stapelen.

- **Metafoor = de winkel.** Het project heet `security-shop`. De winkel doet het metafoor-werk: je loopt een afdeling in, vergelijkt wat er ligt, pakt wat bij je past. Afdelingen = de ZTMM-pillars.
- **Vakterm voor één item = "patroon".** Geen metafoor maar de internationaal erkende architectuurterm: een benoemde, herbruikbare oplossing voor een terugkerend probleem, mét context, trade-offs en verwante patronen.

De eerder geopperde **"puzzelstuk"-metafoor is verworpen**. Reden: een legpuzzel heeft één stukje per plek en één eindplaatje, terwijl de kernwaarde van security-shop juist *kiezen uit 2–5 alternatieven per gap* is — en security nooit "af" is. Bovendien botst "puzzel" met de winkel-metafoor (twee metaforen door elkaar = ruis). "Patroon" draagt het kiezen-tussen-alternatieven van nature in zich.

## 7. Frame (architectuur-spine)

**CISA Zero Trust Maturity Model 2.0** — 5 pillars + 3 cross-cutting capabilities.

Een **pillar** is een "ding" dat je beveiligt. De keten die doorlopen wordt als iemand bij data wil: *iemand* (Identity) werkt op een *apparaat* (Devices), gaat over het *netwerk* (Networks) naar een *applicatie* (Applications), om bij de *gegevens* (Data) te komen.

| Pillar | In één zin | Voorbeeld-gap |
|---|---|---|
| Identity | Wie mag erin — mensen en accounts | Beheerders loggen in zonder MFA |
| Devices | Waarmee loggen ze in — laptops, telefoons, servers | Privé-laptops krijgen toegang tot gemeentedata |
| Networks | Waar het verkeer overheen gaat | Netwerk is één plat vlak — één ingang = overal bij |
| Applications & Workloads | De programma's en systemen zelf | Vakapplicatie zonder veilige inlog-koppeling |
| Data | Het spul dat je beschermt — de gegevens | Niemand weet welke data gevoelig is |

Een **cross-cutting capability** is geen "plek" maar een vermogen dat door alle vijf pillars heen loopt:

| Cross-cutting | In één zin | Voorbeeld-gap |
|---|---|---|
| Visibility & Analytics | Zie je wat er gebeurt — logging, SIEM, SOC | Geen centrale logging, geen SIEM |
| Automation & Orchestration | Handwerk of automatisch — IaC, auto-respons | Elke wijziging is foutgevoelig handwerk |
| Governance | De afspraken erboven — beleid, rollen, risico | Geen vastgesteld IB-beleid |

Reden voor dit frame: internationaal erkend, architectuur-georiënteerd (i.t.t. NIST CSF's management-functies), klein aantal categorieën, bestaande mappings naar andere frameworks, en aansluitend op de Zero Trust richting van BIO 2.0, NIS2 en NCSC-NL. Maturity-niveaus (Traditional → Initial → Advanced → Optimal) zijn ingebakken in ZTMM en dekken de "klein beginnen → opschalen"-as.

## 8. Normen-mapping — BIO 2.0 primair

BIO 2.0 is de **primaire bril**, geen afgeleide. Reden: BIO is de norm waarop de gemeente geauditeerd wordt (ENSIA-verantwoording); de gebruiker denkt in BIO-maatregelen.

- **BIO 2.0** is een eerste-klas frontmatter-veld (`mapping.bio`). De patroon-auteur tagt BIO-maatregelen direct.
- **ISO 27001/27002:2022** komt vrijwel 1-op-1 mee — BIO 2.0 is uitgelijnd op de ISO 27002:2022 control-structuur. Hoeft niet apart getagd.
- **NIS2** (art. 21) en **AVG** (m.n. art. 32) worden kleine, losse mappingtabellen in `mappings/`.
- **SCF (Secure Controls Framework) is bewust niet gebruikt.** SCF optimaliseert voor breedte (200+ frameworks) terwijl de doelgroep er 3–4 nodig heeft; het is een voorhamer voor dit probleem. Kan later terugkomen als optionele "internationale brug" via de ISO-uitlijning, als daar vraag naar ontstaat.

**Disclaimer (zichtbaar op elke norm-view):** de BIO-mapping is indicatief en gecureerd door de community — geen officiële BIO-conformiteitsverklaring.

## 9. Format en opslag

- **Bron = markdown.** Eén bestand per patroon (frontmatter + body). Versiebeheerd in git, bewerkbaar door bijdragers. Dit is de enige bron van waarheid.
- **Presentatie = een gegenereerde statische site met MkDocs Material**: hiërarchische navigatie per pillar, ingebouwde full-text search, tag-indexen. Statische HTML, geen server.
- **Faceted filtering** (meerdere filters tegelijk — cloud én budget én norm) is bewust uitgesteld. Het is een schaal-feature, niet nodig op MVP-omvang. Wordt het knellend bij groei, dan migreert de site (bijv. naar Astro); de patronen blijven ongemoeid omdat de markdown-bron generator-onafhankelijk is.
- Handgeschreven HTML als bron is verworpen: dat verliest de gestructureerde frontmatter en schaalt niet.

## 10. Repo-layout

```
security-shop/
├── docs/                              # MkDocs-content root (docs_dir) — uitsluitend site-content
│   ├── index.md                       # winkel-voorpagina
│   ├── patterns/                      # alle patronen, plat; ID-geprefixte bestandsnamen
│   ├── pillars/                       # 8 beschrijvingspagina's (5 pillars + 3 cross-cutting)
│   └── mappings/                      # NIS2- en AVG-mappingtabellen (BIO zit in de frontmatter)
├── templates/
│   ├── patroon-template.md
│   └── prompts/                       # prompt-directie.md, prompt-informatiemanager.md, prompt-mt.md
├── mkdocs.yml                         # site-generator config
├── requirements.txt
├── README.md
├── CONTRIBUTING.md                    # incl. review-checklist concept → stabiel
├── STIJL.md                           # schrijfwijzer
├── LICENSE
├── 2026-05-20-security-shop-design.md # dit ontwerp (planningsdoc)
└── 2026-05-22-security-shop-mvp.md    # implementatieplan (planningsdoc)
```

- **Site-content staat onder `docs/`** — dat is de MkDocs `docs_dir`, uitsluitend site-content. Het ontwerp en het implementatieplan staan als planningsdocumenten in de projectroot, buiten de site-build. `templates/` valt eveneens buiten de site.
- **Patronen plat** in `docs/patterns/`: een patroon heeft precies één thuis. Multi-pillar = meerdere pillars in de frontmatter. Herclassificeren = frontmatter wijzigen, geen bestand verplaatsen.
- Bestandsnaam = ID, met primaire-pillar-prefix als zachte groepering (bijv. `visibility-centrale-logverzameling.md`).
- Alle pillar-, overlay- en filter-views worden door MkDocs gegenereerd uit de frontmatter.

## 11. Patroon-schema

Elk patroon is één markdown-bestand: YAML-frontmatter (gestructureerd, machine-leesbaar) plus een body (proza).

### 11.1 Frontmatter — gestructureerd

```yaml
id: IDENT-MFA-PHISHING-RESISTANT
naam: Phishing-bestendige MFA voor beheerders
pillar: [identity]                 # ZTMM-pillar(s)
cross-cutting: []                  # visibility-analytics / automation-orchestration / governance
maturity: initial                  # ZTMM-niveau: traditional / initial / advanced / optimal
context:
  hosting: [cloud, hybride]        # cloud / hybride / on-prem
  omvang: [klein, middel, groot]   # gemeentegrootte
  budget: midden                   # laag / midden / hoog
mapping:
  bio: [5.17, 8.5]                 # BIO 2.0-maatregelen — primaire bril (ISO 27002:2022 komt 1:1 mee)
  nis2: [21.2d]                    # optioneel — NIS2 art. 21
  avg: [32]                        # optioneel — AVG-artikel(en)
verwant:
  alternatief-voor: [IDENT-MFA-APP]      # i.p.v. dit
  vereist: [IDENT-IDP-CENTRAAL]          # eerst dit
  vult-aan: [IDENT-PAM]                  # samen met dit
prompt-aandachtspunten: ""         # optioneel: patroon-specifieke nuance voor de communicatie-prompts
status: concept                    # concept / review / stabiel
herzien: 2026-05-22
```

Een `implementatie`-verwijzing naar `hosting-bouwblokken` zit bewust *niet* in het schema (zie §4) — een patroon draagt z'n eigen implementatie-richting.

### 11.2 Body — vaste secties (proza)

1. **In één zin** — de pitch
2. **De gap** — welk probleem, concreet en herkenbaar
3. **Wanneer dit past — en wanneer niet** — eerlijk over de anti-context
4. **Hoe het werkt** — mechanisme op architectuur-niveau
5. **Implementatie-richting** — stappenplan op hoofdlijnen (~5–10 stappen), productneutraal, briefbaar aan een architect/leverancier
6. **Voordelen**
7. **Nadelen & risico's**
8. **Inspanning & kosten** — eenmalig én doorlopend beheer, grove indicatie
9. **Communicatie & draagvlak** — drie korte kernboodschappen van elk 2–3 zinnen, plak- én spreekbaar:
   - voor directie/college — bezit het besluit + budget
   - voor de informatiemanager — bezit inpassing in landschap & roadmap
   - voor het MT — bezit uitvoering in de lijn

### 11.3 Communicatie-prompts (globaal, DRY)

In `templates/prompts/` staan drie generieke prompt-templates — `prompt-directie.md`, `prompt-informatiemanager.md`, `prompt-mt.md`. Ze nemen `{kernboodschap}` + `{patroon}` + `{lokale context van de CISO}` en produceren een afgerond stuk: collegevoorstel/raadsbrief, architectuurnotitie, MT-stuk.

Reden voor de DRY-opzet: een prompt is ~90% generiek per doelgroep; alleen de kernboodschap verschilt per patroon. Drie templates centraal onderhouden i.p.v. drie volledige prompts per patroon. De gegenereerde site kan een prompt voorvullen met de kernboodschap ("werk uit voor directie").

De prompts leveren een **neutrale basistoon** plus een verplichte "maak het van jou"-stap (zie §12) — geen persoonlijke huisstijl.

### 11.4 Waarom de frontmatter/body-split

- **Overlays komen gratis**: BIO/NIS2/AVG-views worden gegenereerd uit `mapping` + `pillar` — geen losse handmatige tabellen die uit sync lopen.
- **Filters werken zonder app**: zelfs een simpel script kan op `context:` filteren.
- **`verwant:` voedt de shortlist-ervaring**: open één patroon, zie meteen de alternatieven.
- Een latere **beslisboom-laag leest puur de frontmatter** — geen herschrijven.

## 12. Toon en kwaliteitsbewaking

AI-slop — generieke tekst die niets zegt — wordt op drie linies tegengehouden:

1. **Substantie** — een patroon moet iets specifieks zeggen om opgenomen te worden; dat regelt de review-gate (§13).
2. **Lokaal-specifieke output** — de communicatie-prompts dwingen de CISO eigen gemeente-context in te voeren; de output is daardoor nooit generiek.
3. **Toon** — geregeld in dit hoofdstuk.

- **`STIJL.md`** is een korte schrijfwijzer: concreet, stellig, geen vulwoorden, elke claim onderbouwd. Neutraal en professioneel — niemands persoonlijke stem. Reviewers toetsen hieraan.
- De prompt-templates leveren diezelfde neutrale basistoon plus een verplichte "maak het van jou"-stap waarin de CISO lokale context en eigen stem inbrengt.
- `schrijfstijl-bas` en `ciso-memo` zijn persoonlijke skills van de auteur en horen **niet** in deze landelijke open-source repo. De output-types (collegevoorstel, raadsbrief) zijn generieke overheidsdocumenten — daar verwijzen de prompts naar zonder een persoonlijke skill mee te leveren.

## 13. Contributie-model — gelaagde status

- **Voorstellen is vrij.** Iedereen mag een patroon indienen via PR of een issue-template. Lage drempel.
- Een ingediend patroon komt binnen als **`status: concept`** — het staat in de repo en op de site, maar zichtbaar gelabeld "nog niet gereviewd".
- Een **maintainer** tilt het via `review` naar **`stabiel`** na toetsing aan een checklist in `CONTRIBUTING.md` (volledig schema, substantie, productneutraliteit, STIJL.md, mapping-correctheid).
- De gegenereerde site **scheidt concept en stabiel visueel** — stabiele patronen prominent, concepten met een waarschuwingslabel.
- De gate zit op *promotie*, niet op *binnenkomst* — geen merge-bottleneck, en de groei van de catalogus is ontkoppeld van de vrije uren van één reviewer.
- Promotierechten kunnen groeien naar meerdere vertrouwde SC-NL-mensen. Concepten die te lang ongereviewd blijven hangen, worden periodiek herzien of verwijderd.

## 14. MVP-scope — de eerste 5 patronen

De eerste patronen zijn **geconcentreerd in één gap-cluster** — niet gespreid over pillars. Reden: alleen concentratie maakt de kern-mechaniek "2–5 alternatieven per gap" zichtbaar; 1 patroon per pillar verbergt juist de belangrijkste waardepropositie.

**Cluster:** detectie & response / SOC-sourcing — capability **Visibility & Analytics**. Dit sluit aan op de voorbeeld-gaps van de doelgroep ("geen fatsoenlijk SIEM", "logging niet centraal") en is juist waar de catalogus het meest onderscheidend is: sourcing-beslissingen met een echte NL-context (regionale samenwerkingsverbanden), waar bestaande NCSC/CIS-guidance zwak is.

**De gap:** "we hebben geen volwassen detectie- en response-capaciteit."

| # | Patroon | Rol |
|---|---|---|
| 1 | Centrale logverzameling | fundering — `vereist` voor 2–5 |
| 2 | Co-managed SIEM | alternatief |
| 3 | Uitbestede SOC (MSSP) | alternatief |
| 4 | MDR-dienst (Managed Detection & Response) | alternatief |
| 5 | Regionaal / gedeeld SOC-samenwerkingsverband | alternatief |

Eén fundering plus vier alternatieven die sterk verschillen in kosten, mate van controle en benodigde eigen expertise — ideaal om de trade-off-vergelijking te demonstreren.

De overige pillars/capabilities blijven in de MVP leeg; de `pillars/`-beschrijvingspagina's geven wel alvast het volledige frame, zodat een bezoeker ziet waar het project naartoe groeit.

## 15. Werkafspraken

- Taal: Nederlands voor alle inhoud en documentatie.
- Open source vanaf dag één onder een Europese licentie (waarschijnlijk EUPL-1.2, conform `hosting-bouwblokken` overweging).
- Geen klantspecifieke gegevens (gemeente, IP-ranges, persoonsnamen) in patronen — geanonimiseerd vanaf publicatie.
- Patronen blijven productneutraal en cloud-agnostisch; de implementatie-sectie is een stappenplan op hoofdlijnen, geen leverancier-specifieke handleiding.

## 16. Nog te doen vóór implementatie

Alle ontwerpkeuzes zijn gemaakt. Wat resteert is uitvoerings-voorbereiding — input voor het implementatieplan:

1. **Werkmap hernoemen** `security-architecture` → `security-shop` (plus de bijbehorende memory-map). Gebeurt buiten Claude om, want de map is in gebruik door de actieve sessie.
2. **Git-repo initialiseren** (lokaal; later publiceren op `github.com/security-commons-nl/security-shop`).
3. **Skelet opzetten**: repo-layout uit §10, `mkdocs.yml`, `README.md`, `CONTRIBUTING.md` (met review-checklist), `STIJL.md`, `LICENSE`.
4. **De 3 prompt-templates** schrijven (`templates/prompts/`).
5. **`patroon-template.md`** schrijven volgens §11.
6. **De 8 `pillars/`-beschrijvingspagina's** schrijven.
7. **De 5 MVP-patronen** uitwerken (§14).
8. **NIS2- en AVG-mappingtabellen** opzetten in `mappings/`.
