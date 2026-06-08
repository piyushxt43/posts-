# Draftly Carousels

**Separate from `AI_Business_Carousels/`** (Piyush / Claude / GPT / Gemini).

## Style

Premium editorial like Mobile Editing Club reference carousels:

- Cream grid `#F4EEDE`, coral accent `#EF5E45`, ink `#1B1A17`
- Space Grotesk headlines + italic serif accent
- **DRAFTLY** text wordmark top-right (no icon)
- Cover handles: `draftly.space / piyush.glitch`
- Deep multi-paragraph prompts visible on slides (website, image, video)
- Website screenshot mockups + generated result previews

**Not used:** dark blue AI builder chrome, neon glow, cream-only Piyush `@piyush.glitch` footer on every slide.

## 15 carousels (120 PNGs + 15 PDFs)

| # | Folder | Product |
|---|--------|---------|
| 01 | Premium_Earphones | Apple AirPods Pro |
| 02 | Luxury_Clothing | Maison Aurel |
| 03 | Performance_Sneakers | Velocity Pro |
| 04 | Specialty_Coffee | Origin and Ember |
| 05 | Artisan_Cafe | Hearth and Bloom |
| 06 | Boutique_Hotel | The Vale House |
| 07 | Luxury_Bed_Linen | Somerset and Co |
| 08 | Premium_Watch | Meridian Automatic |
| 09 | Clean_Skincare | Lumen Botanica |
| 10 | Designer_Sunglasses | Optic Atelier |
| 11 | Luxury_Handbags | Maison Valetta |
| 12 | Artisan_Perfume | Nocturne Atelier |
| 13 | Designer_Furniture | Arcform Chair |
| 14 | Premium_Wellness_Studio | Forma Pilates |
| 15 | Luxury_Chocolate | Cacao Meridian |

Each folder: **8 PNG slides** + **`09_prompt_guide.pdf`** (5-6 pages, all prompts in depth).

### Video carousel (experimental)

| Folder | Pipeline |
|--------|----------|
| `16_iPhone_17_Pro_Max` | Hero PNG -> `veo-3.1-fast-generate-preview` image-to-video -> MP4 slides 1-2 + PNG slides 3-8 |

```bash
APIYI_API_KEY="..." python3 Draftly_Carousels/generate_video_carousel.py
```

## Commands

```bash
# Images (parallel)
APIYI_API_KEY="..." python3 Draftly_Carousels/generate.py --workers 80 --force

# PDFs only
./.venv/bin/python Draftly_Carousels/build_pdfs.py
```

Reference screenshots: `references/draftly/` and `references/mobile_editing_club_01.png`
