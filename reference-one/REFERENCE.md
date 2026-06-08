# Reference One — Carousel Pipeline Guide

Public documentation for this repo. **No API keys, no local paths, no private assets.**

> **Note:** Full local reference assets (`references/draftly/`, screenshots, `fourth June/reference.md`) stay on your machine but are **gitignored** — not pushed to GitHub.

Start here if you cloned [posts-](https://github.com/piyushxt43/posts-) and want to understand how everything fits together.

---

## What this repo does

Automated Instagram carousel pipeline in three layers:

1. **Content** — `content.py` in each batch folder defines slides + image prompts + captions
2. **Images** — `generate.py` calls the image API (you supply `APIYI_API_KEY`)
3. **PDFs** — `build_pdfs.py` builds lead-magnet PDFs from the same content

Generated `*.png` and `*.pdf` are gitignored. Clone ? set API key ? run scripts ? get outputs.

---

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
# Add your APIYI_API_KEY to .env

cd "Draftly_3D_Free"
python3 generate.py        # images
```

---

## Two brands

| Brand | Handle / URL | Style doc | Main folders |
|-------|--------------|-----------|--------------|
| **Piyush** | @piyush.glitch | [piyush-style.md](piyush-style.md) | `AI_Business_Carousels/`, `6th June/`, `7th June/` |
| **Draftly** | draftly.space | [draftly-brand.md](draftly-brand.md) | `Draftly_Carousels/`, `Draftly_Growth/`, `Draftly_3D_Free/` |

---

## Folder map (batches)

| Folder | Slides | Topic |
|--------|--------|-------|
| `Draftly_3D_Free/` | 3 | Free 3D websites hook, 4:5 ratio |
| `Draftly_Growth/` | 5×8 | Draftly growth marketing |
| `Draftly_Carousels/` | 15 verticals | Product carousels + PDF guides |
| `6th June/` | 5×8 | Claude operator carousels |
| `7th June/` | 2 carousels | Gemini Pro FREE + Jio PDF |
| `5th June/` | 10×8 | Full AI business batch |
| `third June/` | 12 | Skills, MCP, beauty prompts |
| `fourth June/` | 1 | Claude plugins June |
| `AI_Business_Carousels/` | 20+ | Piyush AI business posts |
| `50_Series_Carousels/` | 50-series | Long-form list carousels |

Date-named folders are **batch snapshots** — same pattern everywhere: `content.py` + `generate.py` + `build_pdfs.py`.

---

## Image API

| Setting | Value |
|---------|-------|
| Endpoint | `https://api.apiyi.com/v1/images/generations` |
| Model | `gpt-image-2-all` |
| Env var | `APIYI_API_KEY` (required — never commit) |

See [api-setup.md](api-setup.md).

---

## Draftly pipeline (prompt fields)

Every Draftly 3D site uses four prompt types:

1. **Website prompt** — full site brief (nav, sections, copy, motion)
2. **Image prompt** — hero still (16:9, 400+ frames)
3. **First + last frame prompts** — animation bookends for continuity
4. **Video prompt** — 8s motion loop

Then **chat** to iterate. See [draftly-brand.md](draftly-brand.md) and [draftly-presets.md](draftly-presets.md).

---

## Files in this folder

| File | Purpose |
|------|---------|
| `REFERENCE.md` | This index |
| `api-setup.md` | API key setup (placeholder only) |
| `piyush-style.md` | @piyush.glitch visual + caption rules |
| `draftly-brand.md` | Draftly product copy, pipeline, pricing |
| `draftly-presets.md` | 47 preset names for carousel credibility |
| `draftly-carousel-style.md` | Draftly slide layout specs |
| `pipeline.md` | content.py ? generate.py ? build_pdfs.py pattern |

---

## Security

- Never commit `.env` or real API keys
- No generated images/PDFs in git
- No local machine paths in public docs
- Comment keywords (`BUILD`, `DRAFTLY`, `FREE`) are lead magnets — PDFs ship separately
