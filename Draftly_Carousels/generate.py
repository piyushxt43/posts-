#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Draftly premium editorial carousels (separate from AI_Business_Carousels)."""

from __future__ import annotations

import argparse
import base64
import concurrent.futures
import os
import re
import sys
import time
import urllib.request
from pathlib import Path
from typing import Any

_ROOT = Path(__file__).resolve().parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from content import CAROUSELS, SLIDE_TEMPLATES

API_URL = "https://api.apiyi.com/v1/images/generations"
MODEL = "gpt-image-2-all"
ROOT = _ROOT
TIMEOUT_SECONDS = 300

EDITORIAL_STYLE = """
3:4 vertical Instagram carousel slide.

REFERENCE AESTHETIC: Mobile Editing Club premium Instagram carousels - editorial photography, cream grid-paper educational slides, bold grotesque typography, luxury brand campaign quality. Match the warm premium creator look - NOT dark blue AI SaaS UI, NOT neon glow, NOT generic AI slop.

COLORS (premium only - same family as high-end AI business carousels):
- Cream grid paper #F4EEDE on educational / prompt slides
- Warm card panels #FCFAF3
- Coral accent #EF5E45 for tabs, arrows, numbered steps, highlight pills
- Ink black #1B1A17 for headlines
- Muted brown-gray #6E6657 for body text
- Cover and CTA slides: full-bleed editorial product photography with white text overlay

TYPOGRAPHY:
- Space Grotesk bold grotesque for main headlines (premium website feel)
- One elegant italic serif accent word where natural
- Inter for readable body copy on cream slides
- TOP RIGHT on every slide: text wordmark "DRAFTLY" in small bold Space Grotesk uppercase - text only, NO icon logo

LAYOUT:
- Prompt slides must show MULTI-PARAGRAPH prompt text in readable blocks (2-3 paragraphs) - people must see these are deep production briefs, not one-liners
- Include realistic draftly.space website screenshot mockups on cream/light UI panels where relevant
- Show generated result preview thumbnail beside prompt where relevant
- Subtle hand-drawn arrow annotations optional
- Feel like actual website workflow documentation taken from draftly.space, not AI concept art

COVER SLIDE:
- Photoreal premium product hero
- Bold headline
- DRAFTLY text top-right
- Footer: draftly.space / piyush.glitch

CTA SLIDE:
- White pill button on editorial photo like "START PROMPTING ->"
- DRAFTLY top-right

Interior slides: slide number X/8 bottom-right.
NO lorem ipsum. NO spelling mistakes. NO blue builder chrome.
"""

COVER_HANDLES = "draftly.space / piyush.glitch"


def slugify(text: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "_", text.strip().lower())
    return text.strip("_") or "slide"


def build_slide_spec(carousel: dict[str, Any], slide_index: int) -> dict[str, str]:
    kind = SLIDE_TEMPLATES[slide_index - 1]
    n = slide_index
    product = carousel["product_label"]
    title = carousel["title"]

    if kind == "cover":
        return {
            "filename": f"{n:02d}_cover_{slugify(title)[:40]}.png",
            "headline": f"Prompt A Cinematic Site For {product}",
            "body": carousel["cover_hook"],
            "visual": (
                f"Premium Mobile Editing Club style cover. Full-bleed editorial photoreal {product} hero. "
                f"Large white Space Grotesk headline with one italic serif accent word. "
                f"Small text logo DRAFTLY top-right. Footer {COVER_HANDLES}. Slide {n}/8. "
                f"No icon logo. No blue UI."
            ),
            "extra": "",
        }

    if kind == "website_prompt":
        return {
            "filename": f"{n:02d}_website_prompt.png",
            "headline": "Website Prompt",
            "body": (
                "Step 1 at /3d-builder. Paste a full production brief - layout, copy, sections, palette, CTAs. "
                "This is what ships your scroll-synced site."
            ),
            "visual": (
                "Cream grid-paper slide. Left: coral step tab 01, headline, short explanation. "
                "Right: light draftly.space website screenshot mockup with textarea showing THREE PARAGRAPHS of website prompt text fully readable. "
                "Hand-drawn arrow to prompt area. DRAFTLY text top-right."
            ),
            "extra": f"RENDER THIS FULL WEBSITE PROMPT (3 paragraphs, readable):\n{carousel['website_prompt']}",
        }

    if kind == "image_prompt":
        return {
            "filename": f"{n:02d}_hero_image_prompt.png",
            "headline": "Hero Image Prompt",
            "body": (
                "Step 2 generates your scroll-synced background still. "
                "Write scene, lens, light, mood - minimum three paragraphs of art direction."
            ),
            "visual": (
                "Cream grid slide. Left column: long prompt card with THREE FULL PARAGRAPHS of image prompt in readable type inside a warm card panel. "
                "Right column: photoreal preview of generated hero still for this product. "
                "Coral step tab 02. DRAFTLY top-right. Editorial not AI-blue."
            ),
            "extra": f"RENDER THIS FULL IMAGE PROMPT (3 paragraphs, must be readable on slide):\n{carousel['image_prompt']}",
        }

    if kind == "keyframes":
        return {
            "filename": f"{n:02d}_first_last_frames.png",
            "headline": "First and Last Frame",
            "body": (
                "Right rail in Draftly: first frame from hero still. Last frame from its own prompt for first-to-last motion. "
                "Media to frames to UI."
            ),
            "visual": (
                "Cream grid slide with website screenshot strip showing keyframe rail UI on light panel. "
                "Two large photoreal thumbnails FIRST FRAME and LAST FRAME with full prompt text below each. "
                "Coral step tab 03. DRAFTLY top-right."
            ),
            "extra": (
                f"FIRST FRAME PROMPT:\n{carousel['first_frame_prompt']}\n\n"
                f"LAST FRAME PROMPT:\n{carousel['last_frame_prompt']}"
            ),
        }

    if kind == "video_prompt":
        return {
            "filename": f"{n:02d}_video_motion_prompt.png",
            "headline": "Video Motion Prompt",
            "body": (
                "Step 4 optional camera motion. One focused paragraph - dolly, pan, parallax, loop length."
            ),
            "visual": (
                "Cream grid slide. Website screenshot mockup with motion prompt paragraph visible in chat composer. "
                "Small filmstrip between first and last frame. Coral step tab 04. DRAFTLY top-right."
            ),
            "extra": f"RENDER FULL VIDEO PROMPT:\n{carousel['video_prompt']}",
        }

    if kind == "why_website":
        return {
            "filename": f"{n:02d}_why_cinematic_website.png",
            "headline": "Why A Cinematic Website",
            "body": carousel["why_website"],
            "visual": (
                "Cream grid editorial slide. Large headline, two full paragraphs body copy visible, three coral-accent pillar chips: Trust, Story, Conversion. "
                "Typography-led, no product photo. DRAFTLY top-right."
            ),
            "extra": "",
        }

    if kind == "result_website":
        return {
            "filename": f"{n:02d}_finished_website.png",
            "headline": carousel["result_headline"],
            "body": carousel["result_notes"],
            "visual": (
                f"Split slide: left cream panel explains output, right shows realistic draftly.space shipped website screenshot mockup for {product} "
                f"over cinematic generated background - nav, hero, sections, CTA visible. "
                f"Feels like actual site capture. DRAFTLY top-right."
            ),
            "extra": "",
        }

    return {
        "filename": f"{n:02d}_start_prompting.png",
        "headline": "Prompt. Generate. Ship.",
        "body": (
            f"Build a scroll-synced site for {product}: website brief, hero still, motion, frames, live site. "
            "Deep prompts in, cinematic site out."
        ),
        "visual": (
            f"Full-bleed editorial product photo background. White pill CTA button START PROMPTING with arrow. "
            f"Four coral step pills. Footer {COVER_HANDLES}. DRAFTLY top-right."
        ),
        "extra": "",
    }


def build_api_prompt(carousel: dict[str, Any], slide_index: int) -> str:
    spec = build_slide_spec(carousel, slide_index)
    page = f"{slide_index}/8"
    extra = f"\n\nAdditional content to render on slide:\n{spec['extra']}" if spec["extra"] else ""
    return f"""
{EDITORIAL_STYLE}

Carousel: {carousel['title']} ({carousel['product_label']})
Slide: {page}
Type: {SLIDE_TEMPLATES[slide_index - 1]}

Headline: {spec['headline']}
Body copy (include fully, readable): {spec['body']}

Visual direction:
{spec['visual']}
{extra}
""".strip()


def post_json(url: str, payload: dict[str, Any], api_key: str) -> dict[str, Any]:
    body = __import__("json").dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
        return __import__("json").loads(resp.read().decode("utf-8"))


def download_url(url: str, path: Path) -> None:
    req = urllib.request.Request(url, headers={"User-Agent": "draftly-carousel/3.0"})
    with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
        path.write_bytes(resp.read())


def save_generation(result: dict[str, Any], path: Path) -> None:
    item = result["data"][0]
    if item.get("url"):
        download_url(item["url"], path)
        return
    value = item.get("b64_json", "")
    if "," in value and value.startswith("data:"):
        value = value.split(",", 1)[1]
    if value:
        path.write_bytes(base64.b64decode(value))
        return
    raise RuntimeError(f"No image data: {result}")


def generate_job(api_key: str, carousel: dict[str, Any], slide_index: int, force: bool) -> dict[str, Any]:
    folder = ROOT / carousel["slug"]
    folder.mkdir(parents=True, exist_ok=True)
    spec = build_slide_spec(carousel, slide_index)
    out_path = folder / spec["filename"]
    if not force and out_path.exists() and out_path.stat().st_size > 100_000:
        return {"status": "skipped", "slug": carousel["slug"], "slide": slide_index}
    payload = {"model": MODEL, "prompt": build_api_prompt(carousel, slide_index), "response_format": "url"}
    last_error: Exception | None = None
    for attempt in range(1, 4):
        try:
            save_generation(post_json(API_URL, payload, api_key), out_path)
            return {"status": "ok", "slug": carousel["slug"], "slide": slide_index}
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            time.sleep(min(60, 5 * attempt))
    raise RuntimeError(f"{carousel['slug']} slide {slide_index}: {last_error}")


def cleanup_sidecars() -> int:
    removed = 0
    for folder in ROOT.iterdir():
        if not folder.is_dir() or not folder.name[:1].isdigit():
            continue
        for path in folder.iterdir():
            if path.suffix.lower() in {".txt", ".json"}:
                path.unlink()
                removed += 1
    return removed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=int(os.environ.get("DRAFTLY_WORKERS", "80")))
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--no-clean", action="store_true")
    args = parser.parse_args()
    api_key = os.environ.get("APIYI_API_KEY")
    if not api_key:
        print("ERROR: set APIYI_API_KEY", file=sys.stderr)
        return 2
    jobs = [(c, i) for c in CAROUSELS for i in range(1, 9)]
    print(f"Generating {len(jobs)} slides ({len(CAROUSELS)} carousels), {args.workers} workers", flush=True)
    failures: list[str] = []
    done = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futs = {pool.submit(generate_job, api_key, c, i, args.force): (c["slug"], i) for c, i in jobs}
        for fut in concurrent.futures.as_completed(futs):
            slug, idx = futs[fut]
            done += 1
            try:
                r = fut.result()
                print(f"[{done:03d}/{len(jobs)}] {r['status'].upper()} {slug} #{idx}", flush=True)
            except Exception as exc:  # noqa: BLE001
                msg = f"{slug} #{idx}: {exc}"
                failures.append(msg)
                print(f"[{done:03d}/{len(jobs)}] FAILED {msg}", flush=True)
    if not args.no_clean:
        print(f"Cleaned {cleanup_sidecars()} sidecar files", flush=True)
    print(f"Done. Failures: {len(failures)}", flush=True)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
