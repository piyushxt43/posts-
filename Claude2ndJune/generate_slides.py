#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate interior slides 2-10 for Claude2ndJune carousels (PARALLEL).

Slide 2-9: one agent per slide (Meghanify agent-system infographic style).
Slide 10: CTA slide with photo.

Usage:
  APIYI_API_KEY=... python3 generate_slides.py              # all missing slides, 8 parallel
  APIYI_API_KEY=... python3 generate_slides.py --workers 10
  APIYI_API_KEY=... python3 generate_slides.py 02 03        # specific carousels
  APIYI_API_KEY=... python3 generate_slides.py --force      # regenerate even if file exists
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from carousels_content import CAROUSELS

ROOT = Path(__file__).resolve().parent
API_URL = "https://api.apiyi.com/v1/images/generations"
MODEL = "gpt-image-2-all"
TIMEOUT = 360
DEFAULT_WORKERS = 8

INTERIOR_STYLE = """
DESIGN SYSTEM - INTERIOR AGENT SLIDE (match Meghanify agent-system reference exactly):
- Aspect ratio STRICTLY 4:5 vertical portrait, 1080x1350.
- Background: warm off-white cream paper (#F6F1E7) with subtle grain and soft drop shadows.
- TOP LEFT: agent name in HUGE bold black condensed sans-serif (exact text given).
- Under title: one-line description on a hand-marker HIGHLIGHT swipe (color specified below).
- TOP RIGHT: pink sticky note (#F7A8C4) pinned with push-pin, handwritten quote (exact text given).
- TOP RIGHT below sticky: small coral (#D97757) Claude logo rounded-square with white sparkle mark.
- CENTER: clean horizontal workflow diagram - rounded cream tiles with simple flat icons connected by
  hand-drawn arrows. Each tile has an icon + short label. Tiles use soft pastel fills (mint, yellow,
  lavender, sky blue). Below the main flow, optional sub-detail rows (lists, mini tables, sticky clusters).
- BOTTOM RIGHT or bottom bar: lime-green or yellow sticky note labeled "Output:" with the outcome text.
- BOTTOM: horizontal row of small rounded nav tiles for the full system (highlight current agent).
- Footer center: @piyush.glitch in small grey sans.
- NO slide numbers in the art. Crisp spelling, no lorem ipsum, no watermarks, no Instagram UI.
- Mood: premium educational infographic, tactile sticky-note collage, approachable not corporate-boring.
"""

STICKY_QUOTES = {
    "Market Research": "Start with the market.",
    "ICP": "Know who you're for.",
    "Competitor": "Know them. Beat them.",
    "Content Strategy": "Plan it. Ship it.",
    "LinkedIn": "Hooks first.",
    "Email": "Sequences > one-offs.",
    "Ad Copy": "Test angles.",
    "Marketing Ops": "Ship on schedule.",
    "/business-pulse": "Monday in 90 sec.",
    "/invoice-chase": "Collect what's owed.",
    "/lead-triage": "Hot leads first.",
    "/monday-brief": "One page. Done.",
    "/contract-review": "Read before sign.",
    "/job-post-builder": "Hire with clarity.",
    "/receipt-sorter": "Tax season ready.",
    "/client-checkin": "Never go cold.",
    "Client Intelligence": "Context once.",
    "Content Production": "Voice locked in.",
    "Operations": "Draft. Don't send.",
    "Writer Management": "Quality at scale.",
    "Strategy Partner": "Think faster.",
    "Knowledge Base": "Company brain.",
    "Onboarding": "Never drop a ball.",
    "Reporting": "Numbers + story.",
    "Transcript": "One source truth.",
    "Hook Lab": "Earn the swipe.",
    "Carousel": "8 slides. One run.",
    "Thread": "Native, not copy-paste.",
    "Newsletter": "They'll open it.",
    "Repurpose Lead": "No overlap.",
    "Caption": "Engineered saves.",
    "Scheduler": "Set and ship.",
    "Lead Triage": "Work what matters.",
    "Research": "Walk in prepared.",
    "Outreach": "Personal, not spam.",
    "Proposal": "Same-day scope.",
    "Objection": "Never caught flat.",
    "Win-Loss": "Learn from closes.",
    "Pipeline Ops": "CRM stays honest.",
    "Follow-up": "Deals don't die.",
}


def _slugify(name: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "_", name.strip()).strip("_")
    return s[:40]


def sticky_for(name: str) -> str:
    for key, quote in STICKY_QUOTES.items():
        if key.lower() in name.lower():
            return quote
    return "One job. Done well."


def build_agent_prompt(c: dict, slide_num: int, name: str, does: str, fl: str, outp: str,
                       sticky_quote: str) -> str:
    nodes = [n.strip() for n in fl.split("->")]
    flow_labels = " -> ".join(nodes)
    bar = " | ".join(c["bottom_bar"])
    current = name.split()[0] if name.startswith("/") else name.split(" Agent")[0].split()[0]
    return f"""
You are designing slide {slide_num} of 10 for @piyush.glitch Instagram carousel:
"{c['number_word']} {c['headline_main']} {c['system_line']}".

This is an INTERIOR AGENT SLIDE in the Meghanify "Market Research Agent / Content Strategy Agent" style -
information-dense infographic on cream paper, NOT a photo slide.

{INTERIOR_STYLE}

EXACT TEXT TO RENDER:
- Title (top-left, huge bold): "{name}"
- Highlighted sub-line on {c['highlight_color']} swipe: "{does}"
- Pink sticky note (top-right, handwritten): "{sticky_quote}"
- Workflow tiles left-to-right with icons: {flow_labels}
- Output sticky (bottom, labeled "Output:"): "{outp}"
- Bottom nav row highlighting "{current}" among: {bar}
- Footer: @piyush.glitch

VISUAL DETAIL FOR THIS AGENT:
Build a rich, specific infographic layout inspired by the reference agent slides. For "{name}":
- Main flow row: {len(nodes)} connected rounded tiles - {", ".join(nodes)} - each with a distinct simple icon
  (magnifying glass, target, lightbulb, calendar, person, chart, etc. matching the step meaning).
- Add ONE supporting detail block below the flow: a mini list, comparison table, or cluster of colored sticky
  notes that makes the agent feel concrete and useful (not generic placeholder boxes).
- Use hand-drawn curved arrows between tiles. Scatter 1-2 tiny hand-drawn stars or underlines for warmth.
- Keep Claude logo accurate but small (top-right). Pink sticky must feel physically pinned.

Quality bar: this should look like a real designer made it for a 4K-save business Instagram carousel.
4:5 ratio only. Perfect spelling.
""".strip()


def build_cta_prompt(c: dict) -> str:
    comment_word = "AGENT"
    if "SKILLS" in c["caption"]:
        comment_word = "SKILLS"
    elif "OS" in c["caption"][:30]:
        comment_word = "OS"
    elif "ENGINE" in c["caption"]:
        comment_word = "ENGINE"
    elif "SALES" in c["caption"]:
        comment_word = "SALES"

    return f"""
You are designing slide 10 of 10 (FINAL CTA) for @piyush.glitch Instagram carousel:
"{c['number_word']} {c['headline_main']} {c['system_line']}".

LAYOUT - split like the cover reference:
- TOP 55%: cream paper graphic design.
- BOTTOM 45%: real candid editorial photograph (NOT AI-looking).

TOP ZONE:
- Big bold black headline: "Build this system"
- Highlighted line on {c['highlight_color']}: "{c['system_line']}"
- Pink sticky: "Save + comment '{comment_word}'"
- Coral Claude logo card top-right with white sparkle mark.
- Small recap row of tiny agent tiles from the system.
- Pink "You now have the full workflow" handwritten accent.

BOTTOM PHOTO:
{c['scene']}

PHOTOGRAPHY RULES:
- Authentic documentary photo, 35mm feel, natural light, real skin texture, mild grain, shallow DOF.
- Same person/type as cover for continuity. Not waxy, not stock-stiff, not uncanny.

Footer center: @piyush.glitch. No slide number. 4:5 ratio. Perfect spelling.
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
        req = urllib.request.Request(item["url"], headers={"User-Agent": "claude2ndjune-slides/1.0"})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            path.write_bytes(r.read())
        return
    b64 = item.get("b64_json", "")
    if "," in b64:
        b64 = b64.split(",", 1)[1]
    path.write_bytes(base64.b64decode(b64))


def job_path(c: dict, slide_num: int) -> Path:
    folder = ROOT / c["slug"]
    if slide_num == 10:
        return folder / "10_cta.png"
    idx = slide_num - 2
    name = c["agents"][idx][0]
    return folder / f"{slide_num:02d}_{_slugify(name)}.png"


def build_prompt(c: dict, slide_num: int) -> str:
    if slide_num == 10:
        return build_cta_prompt(c)
    idx = slide_num - 2
    name, does, fl, outp = c["agents"][idx]
    return build_agent_prompt(c, slide_num, name, does, fl, outp, sticky_for(name))


def run_job(api_key: str, c: dict, slide_num: int) -> tuple[str, int, Path]:
    out = job_path(c, slide_num)
    out.parent.mkdir(parents=True, exist_ok=True)
    prompt = build_prompt(c, slide_num)
    save_image(
        post_json(API_URL, {"model": MODEL, "prompt": prompt, "response_format": "url"}, api_key),
        out,
    )
    return c["slug"], slide_num, out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("slugs", nargs="*", help="Carousel slug fragments e.g. 02 03")
    parser.add_argument("--workers", type=int, default=DEFAULT_WORKERS)
    parser.add_argument("--force", action="store_true", help="Regenerate even if file exists")
    parser.add_argument("--slides", type=int, nargs="*", help="Only these slide numbers (2-10)")
    args = parser.parse_args()

    api_key = os.environ.get("APIYI_API_KEY")
    if not api_key:
        print("Set APIYI_API_KEY", file=sys.stderr)
        return 2

    carousels = CAROUSELS
    if args.slugs:
        carousels = [c for c in CAROUSELS if any(x in c["slug"] for x in args.slugs)]

    slide_nums = args.slides or list(range(2, 11))
    slide_nums = [n for n in slide_nums if 2 <= n <= 10]

    jobs: list[tuple[dict, int]] = []
    for c in carousels:
        for n in slide_nums:
            out = job_path(c, n)
            if out.exists() and not args.force:
                print(f"SKIP {c['slug']} slide {n:02d} ({out.name})", flush=True)
                continue
            jobs.append((c, n))

    if not jobs:
        print("Nothing to generate.", flush=True)
        return 0

    print(f"Generating {len(jobs)} slides with {args.workers} parallel workers...", flush=True)
    ok = 0
    fail = 0

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {
            pool.submit(run_job, api_key, c, n): (c["slug"], n)
            for c, n in jobs
        }
        for fut in as_completed(futures):
            slug, n = futures[fut]
            try:
                _, slide_num, out = fut.result()
                ok += 1
                print(f"OK {slug} slide {slide_num:02d} -> {out.name}", flush=True)
            except Exception as e:
                fail += 1
                print(f"FAIL {slug} slide {n:02d}: {e}", flush=True)

    print(f"Done. {ok} ok, {fail} failed.", flush=True)
    return 1 if fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
