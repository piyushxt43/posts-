# Draftly UI reference screenshots

Captured from local Draftly dev server (`draftly-yc-main 3`) on port 3456.

| File | What it shows |
|------|----------------|
| `01_home_chat_ui.png` | Landing page hero + animated AI chat composer (website / image / video model pickers) |
| `02_3d_builder_website_prompt.png` | `/3d-builder` — main chat with "Describe the website you want to build..." |
| `03_3d_builder_mobile.png` | Mobile view of the 3D cinematic builder |
| `04_presets_gallery.png` | `/presets` gallery — preset shortcut path |

## Draftly prompt flow (3D builder)

1. **Website prompt** — chat at `idle` step ? drives final HTML site
2. **Image prompt** — chat at `describe` step ? hero still (`bgImageUrl`)
3. **First / last frame** — right rail keyframes ? optional end still for first?last motion
4. **Video prompt** — chat at `confirm-image` ? MP4 / scroll frames
5. **Website build** — frames extracted ? scroll-synced site shipped

Regenerate screenshots:

```bash
cd "/Users/piyush/Downloads/draftly-yc-main 3" && npm run dev -- -p 3456
cd "/Users/piyush/Downloads/All carousels automatically" && node capture_draftly_screenshots.mjs
```
