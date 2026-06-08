#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 50 Series carousel 02 (10 slides, Claude Skills theme)."""

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

ROOT = Path(__file__).resolve().parent / "50_Series_Carousels" / "02_50_Claude_Skills_Nobody_Set_Up"
API_URL = "https://api.apiyi.com/v1/images/generations"
MODEL = "gpt-image-2-all"
MAX_WORKERS = int(os.environ.get("CAROUSEL_WORKERS", "12"))
TIMEOUT = 300

BASE_STYLE = """
Premium Instagram carousel slide. STRICT 3:4 vertical portrait aspect ratio.
Match posts 01-15 visual language: editorial cream grid (#F4EEDE), bold black sans-serif,
coral accent (#EF5E45), sharp hierarchy, minimal clutter, premium creator aesthetic.
Use exact readable text. No gibberish. No watermark. No slide/page counters.
Footer only: @piyush.glitch bottom-left (small).
"""

COVER_STYLE = """
COVER HOOK SLIDE:
- Scroll-stopping, high-contrast headline stack (3-5 lines).
- Include official Claude logo as a clean badge/card (terracotta app icon style).
- Add small micro label top: AI FOR BUSINESS.
- Visual mood: founder/operator urgency, premium editorial, business consequences.
"""

INTERIOR_STYLE = """
INTERIOR SLIDE:
- Cream grid or subtle editorial paper background.
- Strong headline + short operator body copy.
- Small Claude logo badge top-right.
- Visual aids: cards, folders, code snippets, process diagrams.
"""

SLIDES = [
    (
        "50 Claude skills exist. You set up zero.",
        "Steal 5 copy-paste workflows today and make Claude work like an operator.",
        "Cover with dramatic editorial founder desk, floating Claude logo card, big coral underline under 'zero'.",
    ),
    (
        "SKILL.md Anatomy In 20 Seconds",
        "Frontmatter controls routing. Body controls output quality. References keep context lean.",
        "Document split view with YAML frontmatter panel and markdown instructions panel.",
    ),
    (
        "Progressive Disclosure = Lower Token Burn",
        "Description loads first. Full skill loads on trigger. references/ and scripts/ load only when needed.",
        "Three-layer funnel diagram: metadata -> SKILL.md -> references/scripts.",
    ),
    (
        "Invocation Flags Teams Misconfigure",
        "disable-model-invocation and user-invocable decide who can trigger what and when.",
        "Frontmatter table card with lock icons and operator warning callout.",
    ),
    (
        "Skill 1: PR Security Sentinel",
        "Review diffs risk-first, map blast radius, and force test-gap reporting before merge.",
        "Git diff card with risk badges and security checklist.",
    ),
    (
        "Skill 2: Incident Timeline Builder",
        "Correlate logs, deploys, and tickets into a minute-by-minute postmortem timeline.",
        "Timeline cards with timestamps and incident markers.",
    ),
    (
        "Skill 3: GTM Message Calibrator",
        "Rewrite by persona with forbidden claims list so messaging stays sharp and compliant.",
        "Persona cards and message rewrite matrix.",
    ),
    (
        "Skill 4: Eval Gatekeeper",
        "Block prompt or model changes when safety or task pass-rate drops.",
        "Release gate dashboard with red/green status panels.",
    ),
    (
        "Skill 5: Prompt Regression Tracker",
        "Run golden prompts weekly and flag behavior drift before customers notice.",
        "Regression chart and golden prompts folder UI.",
    ),
    (
        "Comment AI For 7 Full Skill Files",
        "Get all 7 copy-paste SKILL.md workflows with frontmatter and examples.",
        "Clean CTA slide with Claude badge and bold coral 'Comment AI' button.",
    ),
]


def slugify(text: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "_", text.strip()).strip("_")[:70]


def build_prompt(index: int, slide: tuple[str, str, str]) -> str:
    headline, body, visual = slide
    style = COVER_STYLE if index == 1 else INTERIOR_STYLE
    return f"""
3:4 vertical Instagram carousel slide.
{BASE_STYLE}
{style}

HEADLINE (render exactly): {headline}
BODY (render exactly): {body}
Footer text: @piyush.glitch

VISUAL DIRECTION:
{visual}
""".strip()


def post_json(url: str, payload: dict, api_key: str) -> dict:
    request = urllib.request.Request(
        url,
        json.dumps(payload).encode(),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
        return json.loads(response.read())


def save_image(result: dict, path: Path) -> None:
    item = result["data"][0]
    if item.get("url"):
        req = urllib.request.Request(item["url"], headers={"User-Agent": "batch50-02/1.0"})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
            path.write_bytes(response.read())
        return
    b64 = item.get("b64_json", "")
    if "," in b64:
        b64 = b64.split(",", 1)[1]
    path.write_bytes(base64.b64decode(b64))


def job(api_key: str, index: int, slide: tuple[str, str, str], force: bool) -> str:
    ROOT.mkdir(parents=True, exist_ok=True)
    filename = f"{index:02d}_{slugify(slide[0])}.png"
    output = ROOT / filename
    if not force and output.exists() and output.stat().st_size > 120_000:
        return "skipped"

    for attempt in range(3):
        try:
            result = post_json(
                API_URL,
                {"model": MODEL, "prompt": build_prompt(index, slide), "response_format": "url"},
                api_key,
            )
            save_image(result, output)
            return "ok"
        except Exception:  # noqa: BLE001
            if attempt == 2:
                raise
            time.sleep(4 * (attempt + 1))
    return "ok"


def main() -> int:
    api_key = os.environ.get("APIYI_API_KEY")
    if not api_key:
        print("ERROR: Set APIYI_API_KEY environment variable.", file=sys.stderr)
        return 2
    force = "--force" in sys.argv
    print(f"Generating {len(SLIDES)} slides into {ROOT}", flush=True)

    failures: list[str] = []
    done = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {
            executor.submit(job, api_key, index, slide, force): index
            for index, slide in enumerate(SLIDES, start=1)
        }
        for future in concurrent.futures.as_completed(futures):
            index = futures[future]
            done += 1
            try:
                status = future.result()
                print(f"[{done}/{len(SLIDES)}] {status.upper()} slide #{index}", flush=True)
            except Exception as exc:  # noqa: BLE001
                failures.append(f"slide #{index}: {exc}")
                print(f"[{done}/{len(SLIDES)}] FAIL slide #{index}: {exc}", flush=True)

    print(f"Done. Failures: {len(failures)}", flush=True)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
