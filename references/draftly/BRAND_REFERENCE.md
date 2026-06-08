# Draftly Brand Reference (persistent memory)

> Source of truth: `/Users/piyush/Downloads/draftly-yc-main 3`  
> Live: [draftly.space](https://draftly.space)  
> Last updated: June 2026

Use this file for all future Draftly carousels, PDFs, ads, and scripts.

---

## One-liner

**Draftly** is an AI-native 3D website builder: one prompt ? cinematic video ? 400+ scroll frames ? production HTML. No WebGL at runtime. Ship to `*.draftly.space` or export ZIP.

---

## Primary headlines (from product)

| Context | Copy |
|---------|------|
| Hero | Build cinematic 3D websites from a single prompt |
| Sub | AI-generated motion, frame extraction, production-ready HTML — ~10× faster |
| Pipeline | From prompt to production |
| Scroll | Your video becomes a scroll experience |
| Zero code | No WebGL, no Three.js, no code |
| CTA primary | Start building for free / 3D Website Builder |
| CTA secondary | Build from Preset / Browse Presets |
| Stats | 400+ frames per site · ~8s video · 10–40 FPS · ZIP ready |

---

## Two product paths (always mention both)

1. **3D Builder** (`/3d-builder`) — blank canvas, full image ? video ? frames ? HTML pipeline  
2. **Presets** (`/presets`) — 47 production-ready sites, click-to-edit, chat customize, publish

---

## 5-step / 6-step pipeline (builder UI labels)

1. **Prompt Input** / Describe — "Describe the website you want to build..."
2. **Visual Draft** — AI still (Nano Banana Pro class)
3. **Motion Pass** — ~8s video (Veo 3.1 class)
4. **Website Build** — frame extraction (FFmpeg WASM, 36–2000 frames)
5. **Website Ready** — scroll-synced HTML

Preset path adds **Pick a preset** before Describe.

---

## Builder UI tabs (exact labels)

- **Preview** · **Ship** · **Pipeline** / **Log**
- **Image** · **Video** · **Frames** · **History**
- **Business OS** (Premium)
- Preset editor: **Customize** · **Ship** · **Design**
- Quick tools: **Add page** · **Text** · **Edit** · **Media** · **Design** · **Ship**
- **Apply changes** · **Publish** · **Publish & custom domain**

---

## Target audiences

| Segment | Hook angle |
|---------|------------|
| Founders | Investor-ready hero in minutes, not weeks |
| Agencies | Pitch $40k motion quality at $60/mo |
| Designers | Cinematic scroll without Three.js |
| Developers | Own HTML/Tailwind/JS, ZIP export |
| Marketers | Landing pages + chat iteration |
| D2C / SaaS / Web3 | Presets for every vertical |

---

## Pricing (June 2026 — verify in `lib/pricing-config.ts`)

| Plan | Price | Notes |
|------|-------|-------|
| Free Trial | $0 | 7-day, ~100 credits, 1 site |
| Basic | $25/mo | 1,500 credits, 2 sites |
| Basic Plus | $40/mo | 2,500 credits, 4 sites |
| Pro | $60/mo | **Most Popular**, 6k credits, ZIP export |
| Premium | $200/mo | 25k credits, cloud save, Business OS |
| Enterprise | Custom | Done-for-you |

Credit examples: image ~20cr · video 8s ~128cr · site gen ~600cr

---

## vs Competitors (from features page)

| | Draftly | Framer | Webflow | Spline |
|--|---------|--------|---------|--------|
| AI prompt-to-full-site | Full pipeline | Partial | No | No |
| Scroll without WebGL | Yes | Partial | No | 3D runtime |
| Code export | HTML ZIP | Limited | Yes | No |
| Preset gallery | 47+ | Templates | Templates | No |
| Entry | $0 trial | Higher | Higher | N/A |

---

## Example prompt chips (landing)

- A luxury car brand landing page
- A DeFi crypto staking platform
- A wellness & yoga studio site

---

## Tech / credibility stack

- Next.js 14 · Firebase · Claude Opus / Gemini for HTML
- Veo 3.1 · Nano Banana Pro · FFmpeg WASM
- Payments: Dodo · Affiliate: 10%

---

## Brand visual (carousels)

- Cream grid `#F4EEDE`, coral `#EF5E45`, ink `#1B1A17`
- **DRAFTLY** wordmark top-right (text, no icon)
- Handles: `draftly.space` · optional `piyush.glitch`
- Space Grotesk headlines + italic serif accent
- Show deep multi-paragraph prompts on slides (website / image / video)
- **Not:** dark neon AI-builder chrome, generic purple gradients

---

## Growth CTAs for carousels

| Goal | CTA |
|------|-----|
| Trial | draftly.space — Start building for free |
| Presets | draftly.space/presets |
| Builder | draftly.space/3d-builder |
| Pricing | draftly.space/pricing |
| Lead magnet | Comment **DRAFTLY** / **BUILD** / **PRESET** for PDF |

---

## Key source files (re-read before new batch)

```
draftly-yc-main 3/README.md
draftly-yc-main 3/messages/en/landing.json
draftly-yc-main 3/messages/en/features.json
draftly-yc-main 3/messages/en/pricing.json
draftly-yc-main 3/messages/en/presets.json
draftly-yc-main 3/app/3d-builder/page.tsx
draftly-yc-main 3/app/presets/page.tsx
draftly-yc-main 3/lib/website-presets/index.ts
draftly-yc-main 3/lib/subscription-plans.ts
draftly-yc-main 3/design-system/README.md
draftly-yc-main 3/handoff.md
draftly-yc-main 3/handoff2.md
```

## Screenshots

Regenerate UI refs:

```bash
cd "/Users/piyush/Downloads/draftly-yc-main 3" && npm run dev -- -p 3456
cd "/Users/piyush/Downloads/All carousels automatically" && node capture_draftly_screenshots.mjs
```

Files: `references/draftly/01_home_chat_ui.png` etc.

---

## Existing carousel work in this repo

| Folder | What |
|--------|------|
| `Draftly_Carousels/` | 15 product-vertical carousels (earphones, fashion, etc.) + prompt PDFs |
| `AI_Business_Carousels/25_Draftly_Power_Moves/` | Power moves bonus PDF |
| `Draftly_Carousels/scripts/` | Growth carousel scripts (5) |

---

## Founder / origin

- Built in India · Piyush Singh
- Positioning: agentic creative workflows, cinematic AI builder (not YC-branded in product)
