#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate ONLY the cover (slide 1) for each Claude2ndJune carousel.

- 4:5 vertical portrait.
- Reference 'Claude agents that run my X system' editorial look (Meghanify-style):
  bold black headline, highlighter sub-line, pink sticky note, Claude logo card,
  'Swipe to see the workflow ->' line, and a REAL-looking photo in the bottom half.
- Long, multi-paragraph prompts (style block + layout + scene + exact text).

Usage:
  APIYI_API_KEY=... python3 generate_covers.py            # all 5 covers
  APIYI_API_KEY=... python3 generate_covers.py 01 03       # only matching slugs
"""

from __future__ import annotations

import base64
import json
import os
import sys
import urllib.request
from pathlib import Path

from carousels_content import CAROUSELS, STYLE_BLOCK, PHOTO_RULES

ROOT = Path(__file__).resolve().parent
API_URL = "https://api.apiyi.com/v1/images/generations"
MODEL = "gpt-image-2-all"
TIMEOUT = 360


def build_cover_prompt(c: dict) -> str:
    bar = "  |  ".join(c["bottom_bar"])
    sticky = c["sticky"].replace("\n", " / ")
    words = c["headline_main"].split()
    line1 = f"{c['number_word']} {words[0]}"
    line2 = " ".join(words[1:]) if len(words) > 1 else ""
    headline_lines = f'line 1 = "{line1}"' + (f'\n  line 2 = "{line2}"' if line2 else "")
    return f"""
You are designing the COVER (slide 1 of 10) of a premium Instagram carousel for the creator @piyush.glitch.
The series concept is "{c['number_word']} {c['headline_main']} {c['system_line']}". This single image must be
so good that someone stops scrolling and swipes. It must look like the work of a high-end design studio paired
with a real documentary photographer - NOT a generic AI tech template and NOT an obviously AI-generated picture.

{STYLE_BLOCK}

LAYOUT FOR THIS COVER (top design zone, ~upper 55% of the 4:5 frame):
- Top-left, very large, bold, stacked headline rendered in near-black ink, EXACTLY this text:
  {headline_lines}
  Make the number "{c['number_word']}" oversized and confident, tight leading, condensed bold sans.
- Directly under the headline, the sub-line rendered with a hand-marker HIGHLIGHT in {c['highlight_color']}:
  "{c['system_line']}" in a casual handwritten-script or italic style sitting on the highlight swipe.
- Top-right: a PINK sticky note (tilted, push-pin, soft shadow) with the handwritten phrase: "{sticky}".
- Near the sticky note OR just under it: the CLAUDE LOGO card - a terracotta/coral (#D97757) rounded square
  with the accurate white Anthropic Claude sparkle/star mark, as a small floating 3D sticker. It should read
  instantly as "this is about Claude".
- Just above the photo: a small pink marker line "Swipe to see the workflow ->" with a quick hand-drawn arrow.

LAYOUT FOR THIS COVER (bottom photo zone, ~lower 45% of the 4:5 frame):
{c['scene']}

{PHOTO_RULES}

FOOTER: center the small grey text "@piyush.glitch" near the very bottom edge, below the photo or as a clean
caption strip. Do NOT add a slide number anywhere on this cover.

OPTIONAL micro-detail: you may faintly suggest a horizontal workflow row of tiny rounded app-tiles
(like: {bar}) as a subtle hint of the system, but keep it secondary - the headline + sticky + Claude logo +
real photo are the heroes. Keep everything perfectly spelled, crisp, and balanced. 4:5 ratio only.
""".strip()


def post_json(url: str, payload: dict, api_key: str) -> dict:
    req = urllib.request.Request(
        url,
        json.dumps(payload).encode(),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return json.loads(r.read())


def save_image(result: dict, path: Path) -> None:
    item = result["data"][0]
    if item.get("url"):
        req = urllib.request.Request(item["url"], headers={"User-Agent": "claude2ndjune/1.0"})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            path.write_bytes(r.read())
        return
    b64 = item.get("b64_json", "")
    if "," in b64:
        b64 = b64.split(",", 1)[1]
    path.write_bytes(base64.b64decode(b64))


def main() -> int:
    api_key = os.environ.get("APIYI_API_KEY")
    if not api_key:
        print("Set APIYI_API_KEY", file=sys.stderr)
        return 2
    only = sys.argv[1:] if len(sys.argv) > 1 else None
    items = CAROUSELS
    if only:
        items = [c for c in CAROUSELS if any(x in c["slug"] for x in only)]
    for c in items:
        folder = ROOT / c["slug"]
        folder.mkdir(parents=True, exist_ok=True)
        out = folder / "01_cover.png"
        print(f"Generating cover: {c['slug']} -> {out.name}", flush=True)
        save_image(
            post_json(
                API_URL,
                {
                    "model": MODEL,
                    "prompt": build_cover_prompt(c),
                    "response_format": "url",
                },
                api_key,
            ),
            out,
        )
        print(f"OK {out}", flush=True)
    print("All covers done.", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
