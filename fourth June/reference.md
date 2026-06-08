# Carousel reference library

Use this file whenever building new Instagram carousels. Match layout, typography, and information density from these references � do not copy text verbatim; adapt for **@piyush.glitch** branding.

**Brand swap:** `CHASE AI` ? `PIYUSH.GLITCH` � `chase.h.ai` style ? your terracotta plugin deck style.

---

## Active style: Chase H AI � Claude Code Plugins (June 2026)

**Source account:** [@chase.h.ai](https://www.instagram.com/chase.h.ai/)  
**Format:** 4:5 vertical � 7�8 slides � Comment keyword lead magnet (`agent` ? PDF/guides)  
**Saved:** 4 June 2026

### Reference images (use these paths in prompts / design briefs)

| # | Role | File path |
|---|------|-----------|
| 1 | **Landing / cover** � hero hook, gradient title, statue + floating app icons | `/Users/piyush/.cursor/projects/Users-piyush-Downloads-All-carousels-automatically/assets/Screenshot_2026-06-04_at_12.47.17_PM-67264cce-2311-44a3-861b-0924aa9c3199.png` |
| 2 | **Plugin 01** � Impeccable, black pill tag, GitHub repo card with tape | `/Users/piyush/.cursor/projects/Users-piyush-Downloads-All-carousels-automatically/assets/Screenshot_2026-06-04_at_12.47.18_PM-dec6d6fc-4d1d-4ee0-a004-c15aa931beed.png` |
| 3 | **Plugin 02** � Caveman mode, 3D rock card, token savings copy | `/Users/piyush/.cursor/projects/Users-piyush-Downloads-All-carousels-automatically/assets/Screenshot_2026-06-04_at_12.47.19_PM-e1667733-353b-49fd-af01-6c183e72628d.png` |
| 4 | **Plugin 03** � Codex ? GPT-5 handoff, Rust repo card | `/Users/piyush/.cursor/projects/Users-piyush-Downloads-All-carousels-automatically/assets/Screenshot_2026-06-04_at_12.47.19_PM_1-1506f0e4-0b2f-4602-96eb-4f3d4435473f.png` |
| 5 | **Plugin 04** � notebooklm-py, terminal-driven NotebookLM | `/Users/piyush/.cursor/projects/Users-piyush-Downloads-All-carousels-automatically/assets/Screenshot_2026-06-04_at_12.47.20_PM-1e5e7928-192c-4531-9139-013266facd6c.png` |
| 6 | **Bonus 06** � Obsidian vault as Claude memory | `/Users/piyush/.cursor/projects/Users-piyush-Downloads-All-carousels-automatically/assets/Screenshot_2026-06-04_at_12.47.21_PM-4585a9bb-93c2-4ccc-8c46-68c2cf92c5ac.png` |

**Workspace copies (for @ attachments):**

| # | Local copy |
|---|------------|
| 1-6 | `fourth June/references/Screenshot_2026-06-04_*.png` (6 files) |

Use these paths when attaching references to image generation prompts.

---

### Visual DNA (apply to every slide)

| Element | Spec |
|---------|------|
| Background | Warm terracotta / burnt orange `#C45E3B`�`#D4623C`, subtle paper grain |
| Header row | Small caps: `JUN @2026` � `PIYUSH.GLITCH` � `0N / 08` (slide counter) |
| Tag pill | Black rounded pill, white text: `PLUGIN 01 / NAME` or `BONUS / OBSIDIAN` |
| Headline | Large bold lowercase sans; emphasis words in **black**, rest in **white** |
| Body | Short paragraph, white; key terms bold black |
| Repo card | White rectangle, slight tilt, **translucent tape** corners, GitHub path + stars + language dot |
| Footer | `0N / 08` left � dot progress � `SWIPE ->` right |
| Ratio | 4:5 (1080�1350) |

### Information pattern (per plugin slide)

1. One-line outcome hook (what it kills / saves / enables)  
2. Two-sentence explanation with **bold** technical terms  
3. Repo card: `owner / repo` + one-line description + language + star count  
4. No lorem ipsum; real repo names and accurate one-liners  

### Landing slide pattern

- Big title: **Top N** + gradient or split-color product name + **for Month**  
- Hero visual (statue, bust, or editorial object) + 2 floating 3D app icons (GitHub, Claude)  
- No plugin pill on slide 1 � save pills for slides 2�8  

### PDF companion (not a plain text dump)

- 12+ pages, cream/terracotta accent, monospace install blocks  
- Per plugin: what it does ? install ? config ? example command ? failure modes  
- Final page: comment keyword + file checklist  

---

## Secondary references (beauty / Visual AI Club)

Used for carousels `06`�`12` in `third June/`. See `third June/reference.md` if added, or screenshots in `third June/` assets.

| Style | Folder |
|-------|--------|
| Hyper-real beauty macros + sky hero | `third June/06_*` � `12_*` |
| Cream educational cards | `third June/08_*` � `12_*` |

---

## How agents should use this file

1. Read **Visual DNA** before writing image prompts.  
2. Attach the matching reference image path from the table for the slide type being generated.  
3. Create carousel under dated folder (`fourth June/`, `third June/`, etc.).  
4. Build PDF from `pdf_content.py` / `build_pdfs.py` in that folder � minimum **10 filled pages**.  
5. Export: `01_cover.png` � `08_*.png`, `caption.txt`, `*.pdf`.

---

## Changelog

| Date | Added |
|------|--------|
| 2026-06-04 | Chase H AI Claude Code Plugins � 6 reference screenshots + DNA |
