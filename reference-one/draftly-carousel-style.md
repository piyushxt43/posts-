# Draftly Carousel Style

## Layout types

### Sky hero (covers)

- Bright blue sky OR editorial desk flat-lay
- **DRAFTLY** top center, frosted pill `3D WEBSITE BUILDER`
- White/dark headline stack + pill CTA
- Footer: `draftly.space`

### Cream grid (educational)

- Background `#F4EEDE`
- Coral `#EF5E45` step pills and accents
- Numbered cards, split layouts for two-path flows
- Monospace prompt text in warm cards

### Prompt dense (how-to slides)

- Four stacked cards: website / image / first+last frame / video
- All prompt text readable at phone size
- Chat iteration banner at bottom

## Specs

| Setting | Value |
|---------|-------|
| Ratio | 4:5 (1080×1350) preferred |
| Wordmark | DRAFTLY top-right, text only |
| Footer | draftly.space bottom-left |
| No | slide numbers, SWIPE arrows, watermarks |

## content.py pattern

```python
BASE = """4:5 vertical (1080x1350)..."""
SKY_HOOK = BASE + """..."""
INTERIOR = BASE + """..."""
PROMPT_DENSE = BASE + """..."""

CAROUSELS = [{
    "slug": "01_Example",
    "caption": "...",
    "slides": [
        ("01_cover.png", SKY_HOOK + "..."),
        ("02_how.png", INTERIOR + "..."),
        ("03_prompts.png", PROMPT_DENSE + "..."),
    ],
}]
```

See `Draftly_3D_Free/content.py` for the latest 3-slide example.
