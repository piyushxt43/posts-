# Draftly reference hub (persistent memory)

Use this folder before generating any Draftly carousel, PDF, or ad.

## Memory files

| File | Purpose |
|------|---------|
| [BRAND_REFERENCE.md](./BRAND_REFERENCE.md) | Product, pricing, pipeline, messaging, visual rules, source paths |
| [PRESET_CATALOG.md](./PRESET_CATALOG.md) | All 47 preset slugs + carousel favorites |
| [../../Draftly_Carousels/scripts/5_GROWTH_CAROUSELS.md](../../Draftly_Carousels/scripts/5_GROWTH_CAROUSELS.md) | 5 growth carousel scripts (June 2026) |
| [../../Draftly_Growth/](../../Draftly_Growth/) | **Built** 5 growth carousels (8 PNGs + PDF each) |

## UI screenshots

Captured from local Draftly dev server (`draftly-yc-main 3`) on port 3456.

| File | What it shows |
|------|----------------|
| `01_home_chat_ui.png` | Landing page hero + animated AI chat composer |
| `02_3d_builder_website_prompt.png` | `/3d-builder` — "Describe the website you want to build..." |
| `03_3d_builder_mobile.png` | Mobile view of the 3D cinematic builder |
| `04_presets_gallery.png` | `/presets` gallery |

Regenerate:

```bash
cd "/Users/piyush/Downloads/draftly-yc-main 3" && npm run dev -- -p 3456
cd "/Users/piyush/Downloads/All carousels automatically" && node capture_draftly_screenshots.mjs
```

## 3D builder prompt flow

1. **Website prompt** — idle step → final HTML
2. **Image prompt** — describe step → hero still
3. **First / last frame** — keyframes for motion arc
4. **Video prompt** — confirm-image → MP4
5. **Website build** — frames → scroll-synced site

## Repo layout

| Path | Content |
|------|---------|
| `Draftly_Carousels/` | 15 product-vertical carousels + generators |
| `Draftly_Carousels/scripts/` | Growth carousel scripts |
| `references/draftly/` | This memory hub |
| `draftly-yc-main 3/` | Product source (external) |
