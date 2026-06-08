#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate carousel 32 (8 slides) in AI_Business_Carousels."""

from __future__ import annotations

import base64
import concurrent.futures
import json
import os
import re
import sys
import time
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent / "AI_Business_Carousels"
API_URL = "https://api.apiyi.com/v1/images/generations"
MODEL = "gpt-image-2-all"
MAX_WORKERS = int(os.environ.get("CAROUSEL_WORKERS", "16"))
TIMEOUT = 300

BASE_STYLE = """
Premium Instagram carousel slide. STRICT 3:4 vertical portrait aspect ratio.
Reference style: @piyush.glitch posts 01-15.
Cream grid paper or editorial blue-sky portrait background, huge confident typography,
bold black sans-serif with one elegant italic serif accent word, coral highlight tabs
and clean card layout. Crisp readable text only, no lorem ipsum.
No watermarks. No Instagram UI.
Footer text: @piyush.glitch bottom-left and page marker bottom-right (x/8).
"""

COVER_STYLE = """
COVER SLIDE:
- Scroll-stopping hook, high contrast, big 3-5 line headline.
- Include both Claude and GPT branding tastefully (logos/cards/badges).
- Top micro label: AI FOR BUSINESS.
- Visual should feel premium, operator-focused, and urgent.
"""

INTERIOR_STYLE = """
INTERIOR SLIDES:
- Cream grid background, clean content hierarchy.
- Top-left small label: AI FOR BUSINESS.
- Claude or GPT badge top-right depending on context.
- Support copy in concise, readable lines.
"""


def slugify(text: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "_", text.strip()).strip("_")[:64]


CAROUSEL: dict[str, Any] = {
    "title": "50 Hidden Prompts That Actually Ship (Claude + GPT)",
    "slug": "32_50_Hidden_Prompts_That_Ship",
    "angle": "50 non-generic prompts with XML tags, format contracts, prefill patterns and non-goals.",
    "slides": [
        (
            "50 Hidden Prompts That Actually Ship",
            "Claude + GPT prompt stack operators use to ship real work, not generic outputs.",
            "COVER: editorial portrait of business operator at desk with holographic prompt cards, "
            "Claude terracotta badge and GPT black-white badge visible. Bold giant headline with 'Ship' in "
            "italic serif coral highlight box. Trendy, high-contrast, premium."
        ),
        (
            "Ops Prompt That Replaces Daily Chaos",
            "Exec dashboard prompt with hard schema: KPI table, risks, opportunities, and one clear summary.",
            "Show KPI cards and structured output template panel, with Claude/GPT co-brand cue."
        ),
        (
            "Content Prompt For Scroll-Stopping Hooks",
            "Generate 12 hooks with pattern labels and select top 3 with rationale. No generic fluff.",
            "Show hook matrix UI with coral tags: Contrarian, Data, Warning, Status."
        ),
        (
            "Code Prompt With Rollback Contract",
            "Refactor plan that includes risk map, tests, rollback triggers and done criteria.",
            "Show code editor + risk panel + rollback checklist cards."
        ),
        (
            "Sales Prompt For Account Strategy",
            "Turn CRM notes into stakeholder map, objection forecast and next 3 actions.",
            "Show CRM-style cards and action timeline."
        ),
        (
            "Research Prompt With Evidence Confidence",
            "Source-graded memo: findings, contradictions, decision options and assumptions.",
            "Show research board with confidence labels High/Med/Low."
        ),
        (
            "The Prompt Contract That Makes It Reliable",
            "Use XML tags + output contract + prefill + non-goals to reduce intervention rate.",
            "Show skeleton blocks: context, rules, output_contract, non_goals."
        ),
        (
            "Comment AI For All 50 Copy-Paste Prompts",
            "Drop 'AI' in comments and get the full categorized prompt PDF.",
            "Premium CTA slide with clean coral Comment AI button and subtle Claude/GPT branding."
        ),
    ],
}


def build_prompt(idx: int, slide: tuple[str, str, str]) -> str:
    headline, body, visual = slide
    page = f"{idx}/8"
    style = f"{BASE_STYLE}\n{COVER_STYLE}" if idx == 1 else f"{BASE_STYLE}\n{INTERIOR_STYLE}"
    return f"""
3:4 vertical Instagram carousel slide.
{style}

Topic: {CAROUSEL['title']}
Angle: {CAROUSEL['angle']}
Slide: {page}

Headline (render exactly): {headline}
Body text (render exactly): {body}
Footer left: @piyush.glitch
Footer right: {page}

Visual direction:
{visual}
""".strip()


def post_json(payload: dict, api_key: str) -> dict:
    req = urllib.request.Request(
        API_URL,
        json.dumps(payload).encode(),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return json.loads(resp.read())


def save_image(result: dict, path: Path) -> None:
    item = result["data"][0]
    if item.get("url"):
        req = urllib.request.Request(item["url"], headers={"User-Agent": "carousel-32/1.0"})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            path.write_bytes(r.read())
        return
    b64 = item.get("b64_json", "")
    if "," in b64:
        b64 = b64.split(",", 1)[1]
    path.write_bytes(base64.b64decode(b64))


def job(api_key: str, idx: int, slide: tuple[str, str, str], force: bool) -> str:
    folder = ROOT / CAROUSEL["slug"]
    folder.mkdir(parents=True, exist_ok=True)
    name = f"{idx:02d}_{slugify(slide[0])}.png"
    out = folder / name
    if not force and out.exists() and out.stat().st_size > 100_000:
        return "skipped"
    for attempt in range(3):
        try:
            result = post_json(
                {"model": MODEL, "prompt": build_prompt(idx, slide), "response_format": "url"},
                api_key,
            )
            save_image(result, out)
            return "ok"
        except Exception:
            if attempt == 2:
                raise
            time.sleep(5 * (attempt + 1))
    return "ok"


def main() -> int:
    api_key = os.environ.get("APIYI_API_KEY")
    if not api_key:
        print("Set APIYI_API_KEY", file=sys.stderr)
        return 2

    force = "--force" in sys.argv
    slides = list(enumerate(CAROUSEL["slides"], 1))
    print(f"Generating {len(slides)} slides for {CAROUSEL['slug']}", flush=True)
    failures: list[str] = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(job, api_key, idx, slide, force): idx for idx, slide in slides}
        done = 0
        for fut in concurrent.futures.as_completed(futures):
            idx = futures[fut]
            done += 1
            try:
                st = fut.result()
                print(f"[{done}/{len(slides)}] {st.upper()} slide #{idx}", flush=True)
            except Exception as exc:
                failures.append(f"slide #{idx}: {exc}")
                print(f"[{done}/{len(slides)}] FAIL slide #{idx}: {exc}", flush=True)

    print(f"Done. Failures: {len(failures)}", flush=True)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
