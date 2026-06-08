# All Carousels Automatically

Automated Instagram carousel pipeline: **content definitions**, **AI image generation**, and **PDF lead magnets**.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env
# Edit .env and set APIYI_API_KEY

# Example: generate 6th June carousels
cd "6th June"
python3 generate.py

# Build PDFs only
python3 build_pdfs.py
```

## Environment

| Variable | Required | Purpose |
|----------|----------|---------|
| `APIYI_API_KEY` | Yes | Image API (api.apiyi.com, model gpt-image-2-all) |

**Never commit real API keys.** This repo ships without generated images or PDFs.

## Project layout

| Folder | Description |
|--------|-------------|
| `AI_Business_Carousels/` | Piyush / @piyush.glitch AI business carousels |
| `Draftly_Carousels/` | Draftly product-vertical carousels + PDF guides |
| `Draftly_Growth/` | Draftly growth/marketing carousels (5 x 8 slides) |
| `6th June/` | Claude operator carousels + dense PDF guides |
| `5th June/` | Full carousel batch + PDF pages |
| `third June/`, `fourth June/` | Earlier batches |
| `Claude2ndJune/` | Claude carousel batch |
| `50_Series_Carousels/` | 50-series content |
| `references/draftly/` | Draftly brand memory (markdown) |
| `fifth June/` | Cover previews + maker.md prompts |

|| `Draftly_3D_Free/` | Draftly 3-slide 4:5 free 3D website carousel |
|| `7th June/` | Gemini Pro FREE carousels + Jio activation PDF guide |
Root scripts: `generate_carousels.py`, `build_pdfs.py`, batch generators.

## Regenerate outputs

Generated `*.png` and `*.pdf` files are **gitignored**. After clone:

1. Set `APIYI_API_KEY`
2. Run the matching `generate.py` in each batch folder
3. Run `build_pdfs.py` for PDF lead magnets

## Draftly screenshots (optional)

```bash
# Start Draftly dev server locally, then:
node capture_draftly_screenshots.mjs
```

---

# Carousel projects (two separate pipelines)

| Folder | Company | Script | Style |
|--------|---------|--------|-------|
| `AI_Business_Carousels/` | **Piyush** (`@piyush.glitch`) | `generate_carousels.py` | Cream grid / coral editorial, Claude/GPT/Gemini AI business topics |
| `Draftly_Carousels/` | **Draftly** (`draftly.space`) | `Draftly_Carousels/generate.py` + `build_pdfs.py` | Cream/coral editorial (Mobile Editing Club style), 15 product carousels, deep prompts, PDF guides |

When you ask for **AI business carousels**, use the Piyush pipeline.  
When you ask for **Draftly carousels**, use the Draftly pipeline only.
