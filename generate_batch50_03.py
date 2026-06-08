#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate carousel 03 (10 slides) for the 50-series set."""

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
SLUG = "50_Series_Carousels/03_50_Hidden_Prompts_That_Ship"
API_URL = "https://api.apiyi.com/v1/images/generations"
MODEL = "gpt-image-2-all"
MAX_WORKERS = int(os.environ.get("CAROUSEL_WORKERS", "16"))
TIMEOUT = 300

BASE_STYLE = """
Premium Instagram carousel slide. STRICT 3:4 vertical portrait aspect ratio.
Match visual language of AI_Business_Carousels 01-15:
cream grid-paper background, coral accent blocks/tabs, bold black sans-serif,
one elegant italic serif accent word, premium editorial composition.
Crisp readable text only, no lorem ipsum. No watermark.
Footer left must read: @piyush.glitch
Footer right must read page marker in the exact format x/10.
"""

COVER_STYLE = """
COVER SLIDE:
- Strong hook based on trending AI business content in 2026.
- High-contrast, urgent, operator-focused, premium business aesthetic.
- Top micro label: AI FOR BUSINESS.
- Include subtle Claude + GPT + Cursor badges/cards in layout.
"""

INTERIOR_STYLE = """
INTERIOR SLIDES:
- Cream grid background and clean card hierarchy.
- Top-left label: AI FOR BUSINESS.
- Keep text dense but readable with clear numbered blocks.
- Use coral callout tabs for each prompt item.
"""


def slugify(text: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "_", text.strip()).strip("_")[:72]


CAROUSEL: dict[str, Any] = {
    "title": "50 Hidden Prompts That Ship (Claude + GPT + Cursor)",
    "angle": (
        "50 copy-paste hidden prompts operators use for XML tags, format contracts, prefill patterns, "
        "reasoning controls, non-goals, and inbox/ops/content workflows."
    ),
    "slides": [
        (
            "50 Hidden Prompts That Ship in 2026",
            "The exact Claude/GPT/Cursor prompt stack serious operators use for revenue, ops, and shipping velocity.",
            "Hook cover with huge headline and italic serif on 'Ship'. Add subtle badges for Claude, GPT, Cursor. "
            "Modern business desk scene with prompt cards floating in depth.",
        ),
        (
            "5 XML Tag Prompts Most People Never Use",
            "1) <role><task><constraints> framework\n2) <context><input_data><goal> splitter\n3) <rules><priority_order> guardrails\n4) <quality_checks><failure_mode> checker\n5) <sources><evidence_level> verifier",
            "Structured prompt cards showing XML snippets and compliance ticks. Make each item clearly numbered.",
        ),
        (
            "5 Format Contracts That Force Reliable Output",
            "1) Return EXACTLY these sections\n2) JSON schema with required keys\n3) Table contract: cols + order fixed\n4) Word caps per section\n5) If missing data write UNKNOWN",
            "Design like an output API contract board with schema blocks and red/green validation markers.",
        ),
        (
            "5 Prefill Patterns For Faster High-Quality Prompts",
            "1) {{audience}} {{goal}} {{deadline}}\n2) {{brand_voice}} {{forbidden_words}}\n3) {{risk_level}} {{approval_path}}\n4) {{tools_allowed}} {{data_sources}}\n5) {{done_criteria}} {{rollback_trigger}}",
            "Template-driven slide with fillable variables highlighted in coral chips and clean examples.",
        ),
        (
            "5 Non-Goal Blocks That Kill Prompt Drift",
            "1) No invented metrics\n2) No motivational filler\n3) No irreversible actions\n4) No legal claims without source\n5) No scope beyond requested output",
            "Risk-control layout with red non-goal badges and a drift-warning visual.",
        ),
        (
            "5 Inbox Operator Prompts (Email + DM + Follow-up)",
            "1) Priority triage with SLA\n2) Reply draft with risk flags\n3) Thread summarizer + next action\n4) Escalation detector\n5) Follow-up sequence generator",
            "Inbox dashboard visual with message queues, urgency labels, and operator action cards.",
        ),
        (
            "5 Ops Operator Prompts (Meetings, KPI, Incident, SOP)",
            "1) KPI daily digest contract\n2) Incident timeline + root cause\n3) SOP gap finder\n4) Weekly blocker memo\n5) Decision log formatter",
            "Operations command-center visual with KPI cards, incident timeline, and structured memo output.",
        ),
        (
            "5 Content Operator Prompts (Hooks, Scripts, Carousels)",
            "1) 12 hooks + top 3 rationale\n2) Carousel page map 1-10\n3) Reels script with beat timestamps\n4) Objection-first post angle\n5) Repurpose longform -> shortform pack",
            "Content pipeline visual with hook matrix, script panels, carousel thumbnails, and trend tags.",
        ),
        (
            "5 Reasoning Control Prompts That Replace 'Think Hard'",
            "1) Assumptions first, answer second\n2) Confidence label per claim\n3) Two alternatives + tradeoff\n4) Self-check before final\n5) Show unknowns and needed data",
            "Reasoning QA layout with checklist, confidence meter, and decision-branch cards.",
        ),
        (
            "Comment AI For All 50 Copy-Paste Prompts",
            "Comment AI and I will send the full 10+ page PDF with all 50 prompts, templates, and rollout checklist.",
            "Premium CTA slide with coral comment button, clean white space, and trustworthy business branding.",
        ),
    ],
}


def build_prompt(idx: int, slide: tuple[str, str, str]) -> str:
    headline, body, visual = slide
    page = f"{idx}/10"
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
        req = urllib.request.Request(item["url"], headers={"User-Agent": "batch50-03/1.0"})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            path.write_bytes(r.read())
        return
    b64 = item.get("b64_json", "")
    if "," in b64:
        b64 = b64.split(",", 1)[1]
    path.write_bytes(base64.b64decode(b64))


def job(api_key: str, idx: int, slide: tuple[str, str, str], force: bool) -> str:
    folder = ROOT / SLUG
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
    print(f"Generating {len(slides)} slides in {ROOT / SLUG}", flush=True)
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
