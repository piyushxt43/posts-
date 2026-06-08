# Posts — Carousel Pipeline

Automated Instagram carousel generator: **prompt definitions → AI images → PDF lead magnets**.

> **Start here:** [reference-one/REFERENCE.md](reference-one/REFERENCE.md) — full guide, styles, API setup. No secrets in that folder.

## Quick start

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # add APIYI_API_KEY

cd Draftly_3D_Free && python3 generate.py
```

## What you get after clone

| Included | Not included (gitignored) |
|----------|---------------------------|
| `content.py` prompts | Generated `*.png` |
| `generate.py` scripts | Generated `*.pdf` |
| `caption.txt` templates | API keys |
| `reference-one/` docs | Local machine paths |

## Main folders

| Folder | What |
|--------|------|
| `reference-one/` | **Public docs** — styles, Draftly brand, pipeline |
| `Draftly_3D_Free/` | 3-slide 4:5 free 3D website carousel |
| `Draftly_Growth/` | 5 growth carousels × 8 slides |
| `Draftly_Carousels/` | 15 product-vertical carousels |
| `6th June/` | Claude operator carousels |
| `7th June/` | Gemini Pro FREE carousels |
| `5th June/` | Full AI business batch |
| `AI_Business_Carousels/` | @piyush.glitch AI posts |

Date-named folders are batch snapshots — same `content.py` + `generate.py` + `build_pdfs.py` pattern everywhere.

## API

Set `APIYI_API_KEY` in `.env`. See [reference-one/api-setup.md](reference-one/api-setup.md).

**Never commit real keys.**
