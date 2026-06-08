#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 5 Claude business carousels (16-20) - editorial cover style with huge Claude logo."""

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
MAX_WORKERS = int(os.environ.get("CAROUSEL_WORKERS", "40"))
TIMEOUT = 300

# Reference: adarshxdesign surreal editorial - huge Claude logo, provocative business hook
EDITORIAL_STYLE = """
Premium Instagram carousel, 3:4 vertical portrait, surreal editorial graphic design.
Photorealistic cinematic scene: vivid blue sky, lens flare sunbeam upper left, high contrast.
Typography: bold clean sans-serif headlines, one key word hand-underlined in black rough stroke.
Footer small: @piyush.glitch bottom-left. Page number bottom-right.
Ultra sharp, magazine quality, no watermarks, no misspellings, no lorem ipsum.
"""

COVER_HERO = """
COVER SLIDE - REFERENCE AESTHETIC (critical):
- Scene: surreal liminal workspace - e.g. professional at wooden desk in vast green grass field under blue sky,
  OR glass office floating above clouds, OR minimalist white studio with single desk - cinematic daylight.
- CLAUDE LOGO DOMINANT: enormous official Anthropic Claude app icon (terracotta/coral rounded square with
  white sparkle star mark) as floating 3D card on RIGHT side, partially overlapping scene - BIG, hero-sized,
  at least 35% of frame height. Accurate Claude logo, not generic AI icon.
- BOTTOM WATERMARK: giant lowercase word "claude" spanning nearly full width at bottom, semi-transparent,
  sitting in grass or fading into scene - like a brand billboard.
- Top micro-header row: small caps left "MAY 2026" center "PIYUSH.GLITCH" right "AI FOR BUSINESS".
- Headline area: stacked bold provocative business statements (3-5 lines), one punchline underlined.
- Mood: thought-leader, attractive, scroll-stopping, Claude-branded, NOT generic tech template.
"""

INTERIOR_STYLE = """
Interior slide: clean editorial layout, cream grid OR soft blue gradient background.
Include small Claude terracotta logo badge top-right corner on every slide.
Coral #EF5E45 accent tabs, black bold headline, readable body copy.
Business advice tone - operator playbook not hype.
"""

CAROUSELS: list[dict[str, Any]] = [
    {
        "title": "Claude Opus 4.8 Upgrade Guide",
        "slug": "16_Claude_Opus_4_8_Upgrade",
        "angle": "Opus 4.8 shipped May 2026 - what changed from 4.7 for coding, agents and business work.",
        "slides": [
            (
                "Claude 4.7 Was Great. 4.8 Is The Default Now.",
                "Anthropic upgraded Opus May 28, 2026. Same price. Better coding, agents and long-running work.",
                "COVER: surreal man at retro desk in green field, blue sky, sun flare. HUGE floating Claude logo card right. Giant semi-transparent 'claude' at bottom. Headline stack: '4.7 trained you.' '4.8 ships the work.' 'Same price.' Underline '4.8'.",
            ),
            (
                "What Actually Changed",
                "Agentic coding score 64.3% to 69.2%. Knowledge work score 1753 to 1890. Less comment noise, cleaner tool calls.",
                "Split comparison card 4.7 vs 4.8 with benchmark bars, small Claude badge top-right.",
            ),
            (
                "New: Effort Control",
                "claude.ai model selector: high (default), extra, max. More tokens on hard tasks when you choose.",
                "UI mockup effort slider high/extra/max with coral highlights.",
            ),
            (
                "New: Fast Mode",
                "API speed:fast gives 2.5x output speed. Premium pricing but 3x cheaper than old fast mode.",
                "Speed gauge 2.5x with lightning, API code snippet claude-opus-4-8.",
            ),
            (
                "New: Dynamic Workflows",
                "Claude Code research preview - tackle larger engineering problems autonomously.",
                "Workflow nodes diagram branching tasks, Claude Code terminal aesthetic.",
            ),
            (
                "Adaptive Thinking",
                "Reasons only when needed. Saves tokens on simple lookups vs 4.7 at same effort.",
                "Brain icon adaptive on/off toggle illustration.",
            ),
            (
                "Upgrade Checklist",
                "API: claude-opus-4-8. Cache min now 1024 tokens. Test evals before full cutover.",
                "Numbered checklist on cream grid, coral checkmarks.",
            ),
            (
                "Comment AI",
                "Want the 4.7 to 4.8 migration checklist? Comment AI for the PDF.",
                "CTA slide, huge Claude logo corner, coral Comment AI button.",
            ),
        ],
    },
    {
        "title": "GPT Image 2 And Claude Prompts",
        "slug": "17_GPT_Image_2_Claude_Prompts",
        "angle": "Use GPT Image 2 for pixels, Claude for prompt engineering, brand grammar and QC - the operator stack.",
        "slides": [
            (
                "GPT Image 2 Makes Pixels. Claude Makes Prompts That Win.",
                "Most brands fail at AI images because they prompt in the generator. Pros prompt in Claude first.",
                "COVER: surreal creative director at floating glass desk above cloud sea, giant Claude logo card right, giant 'claude' bottom watermark. Headlines: 'GPT Image 2 renders.' 'Claude writes the brief.' 'You approve.' Underline 'Claude'.",
            ),
            (
                "The Two-Tool Stack",
                "Claude drafts shot list, brand rules, negative prompts. GPT Image 2 executes generation.",
                "Two-column Claude brain left, image output right, arrow pipeline.",
            ),
            (
                "Brand Prompt Grammar",
                "Claude outputs: subject, environment, lighting, camera, ratio, NEVER list, reference notes.",
                "Structured prompt template card with coral tabs.",
            ),
            (
                "Reference Pack Workflow",
                "Claude analyzes 5 approved refs, extracts visual DNA, writes generation prompt + QC checklist.",
                "Five thumbnail refs feeding Claude document artifact.",
            ),
            (
                "Iteration Loop",
                "Generate in GPT Image 2, paste fail into Claude, get v2 prompt with specific fixes not vibes.",
                "Circular loop v1 v2 v3 with fix notes.",
            ),
            (
                "Campaign Shot List",
                "Claude builds 8-slide carousel shot list before a single pixel generates.",
                "Shot list table hero product lifestyle detail macro.",
            ),
            (
                "QC In Claude",
                "Upload output back to Claude: hands, logo geometry, text legibility, brand color drift pass/fail.",
                "QC checklist red green coral accents.",
            ),
            (
                "Comment AI",
                "Want 20 Claude prompts for GPT Image 2 campaigns? Comment AI.",
                "CTA editorial cover style smaller Claude logo.",
            ),
        ],
    },
    {
        "title": "Meta Business Meets Claude",
        "slug": "18_Meta_Business_Claude_Connector",
        "angle": "Meta official Ads MCP at mcp.facebook.com/ads connects Claude to your ad account in plain English.",
        "slides": [
            (
                "Run Meta Ads From Claude. Official Connector. Free Beta.",
                "Meta opened MCP April 29, 2026. 29 tools. OAuth once. Ask your ad account questions in chat.",
                "COVER: surreal media buyer at desk in minimalist white room, Meta blue + Claude terracotta accents, MASSIVE Claude logo card right overlapping Meta infinity subtle background, giant 'claude' bottom. Headline: 'Meta Business.' 'Meet Claude.' '29 tools live.' Underline 'Claude'.",
            ),
            (
                "What The Connector Does",
                "Performance reports, campaign diagnostics, catalog checks, signal tracking - conversational.",
                "Hub diagram Claude center Meta Ads Instagram Facebook icons.",
            ),
            (
                "5-Minute Setup",
                "Claude Desktop or claude.ai Settings > Connectors > Add custom > https://mcp.facebook.com/ads",
                "Settings UI mockup with URL field highlighted coral.",
            ),
            (
                "OAuth And Permissions",
                "Sign in with Business Manager admin. Choose ad accounts. ads_read first, writes with approval.",
                "OAuth flow three steps shield icon.",
            ),
            (
                "8 Prompts That Save Hours",
                "Weekly performance digest, creative fatigue scan, budget pacing, audience overlap check.",
                "Eight prompt chips stacked scroll style.",
            ),
            (
                "What It Does NOT Do",
                "Not a replacement for strategy or clean tracking. Bad data in = bad recommendations out.",
                "Warning callout box coral border.",
            ),
            (
                "Safety Pattern",
                "Read-only week 1. Log every tool call. Human approves pauses and budget changes.",
                "Approval gate checklist.",
            ),
            (
                "Comment AI",
                "Want the Meta + Claude setup guide and prompt pack? Comment AI.",
                "CTA Meta blue Claude orange blend.",
            ),
        ],
    },
    {
        "title": "Claude For Daily Business Ops",
        "slug": "19_Claude_Daily_Business_Ops",
        "angle": "Day-to-day Claude workflows for inbox, meetings, reports, decisions - 30 minutes saved daily.",
        "slides": [
            (
                "Claude Is Your Daily Ops Partner Not A Weekend Toy",
                "Morning brief, inbox triage, meeting prep, EOD recap - repeatable Projects not one-off chats.",
                "COVER: surreal operator with laptop on rooftop at sunrise city skyline, golden hour, HUGE Claude logo floating right, giant 'claude' grass-style watermark at bottom. Headlines: 'Before coffee.' 'After Claude.' 'Every day.' Underline 'Every day'.",
            ),
            (
                "Morning Brief Ritual",
                "Paste calendar + Slack highlights + KPI screenshot. Claude returns 5 priorities with owners.",
                "Morning dashboard mockup 5 bullet priorities.",
            ),
            (
                "Inbox Triage Mode",
                "Forward 20 emails. Claude sorts: reply now, delegate, archive, needs data.",
                "Email buckets four columns coral labels.",
            ),
            (
                "Meeting Prep In 3 Min",
                "Upload attendee LinkedIn, last notes, goal. Claude gives agenda + 3 smart questions.",
                "Meeting card agenda questions.",
            ),
            (
                "Decision Memo Template",
                "Options, pros/cons, recommendation, what would change my mind - one page max.",
                "Decision matrix template cream grid.",
            ),
            (
                "End Of Day Recap",
                "What shipped, what blocked, tomorrow top 3. Paste to team Slack.",
                "EOD recap card timestamp.",
            ),
            (
                "Project Not Chat",
                "Save daily ops instructions once in Claude Project. Same format every morning.",
                "Project folder vs scattered chats comparison.",
            ),
            (
                "Comment AI",
                "Want the daily Claude ops prompt pack? Comment AI for the PDF.",
                "CTA sunrise editorial.",
            ),
        ],
    },
    {
        "title": "Claude Business Playbook 2026",
        "slug": "20_Claude_Business_Playbook_2026",
        "angle": "Five Claude investments that pay back: Projects, routing, connectors, artifacts, team SOPs.",
        "slides": [
            (
                "Stop Experimenting. Start Operating Claude Like A Business System.",
                "Random chats burn money. Projects + routing + MCP + artifacts + SOPs compound.",
                "COVER: surreal boardroom table in open desert dunes blue sky, executives silhouettes, monumental Claude logo card dominating right side 40% frame, massive 'claude' etched in sand at bottom. Headlines: 'AI demos die.' 'Claude systems scale.' 'Your move.' Underline 'systems'.",
            ),
            (
                "Investment 1: Team Projects",
                "One shared brain per workflow. Brand, pricing, SOPs loaded every session.",
                "Project stack icon three folders.",
            ),
            (
                "Investment 2: Model Routing",
                "Sonnet for volume. Opus 4.8 for judgment. Haiku for classify. Track edit minutes.",
                "Routing funnel diagram.",
            ),
            (
                "Investment 3: Live Connectors",
                "Meta Ads MCP, GitHub, Postgres read-only - Claude sees truth not exports.",
                "Connector hub MCP icons.",
            ),
            (
                "Investment 4: Artifacts",
                "Deliverables in side panel - calculators, memos, decks - not chat paragraphs.",
                "Artifact window floating.",
            ),
            (
                "Investment 5: Team SOPs",
                "Version starter prompts in git. Weekly review of failures. One AI ops owner.",
                "SOP document version v1 v2.",
            ),
            (
                "ROI Math",
                "10 min saved x 5 days x 10 people = 33 hours/week. Measure it or guess.",
                "Simple ROI calculator graphic.",
            ),
            (
                "Comment AI",
                "Want the full Claude business playbook PDF? Comment AI.",
                "CTA monumental Claude logo.",
            ),
        ],
    },
]


def slugify(text: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "_", text.strip()).strip("_")[:60]


def build_prompt(carousel: dict, slide_index: int, slide: tuple[str, str, str]) -> str:
    headline, body, visual = slide
    page = f"{slide_index}/8"
    if slide_index == 1:
        style_block = f"{EDITORIAL_STYLE}\n{COVER_HERO}"
    else:
        style_block = f"{EDITORIAL_STYLE}\n{INTERIOR_STYLE}"
    return f"""
3:4 vertical Instagram carousel slide.
{style_block}

Topic: {carousel['title']}
Business angle: {carousel['angle']}
Slide: {page}

HEADLINE (render exactly, large bold): {headline}
BODY (smaller supporting text): {body}
Label top-right small: AI FOR BUSINESS - {slide_index + 15:02d}
Footer: @piyush.glitch | {page}

VISUAL DIRECTION (follow closely):
{visual}

Make Claude logo accurate and prominent on cover. Interior slides: small Claude badge top-right.
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
        req = urllib.request.Request(item["url"], headers={"User-Agent": "claude-batch3/1.0"})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            path.write_bytes(r.read())
        return
    b64 = item.get("b64_json", "")
    if "," in b64:
        b64 = b64.split(",", 1)[1]
    path.write_bytes(base64.b64decode(b64))


def job(api_key: str, carousel: dict, idx: int, slide: tuple, force: bool) -> str:
    folder = ROOT / carousel["slug"]
    folder.mkdir(parents=True, exist_ok=True)
    name = f"{idx:02d}_{slugify(slide[0])}.png"
    out = folder / name
    if not force and out.exists() and out.stat().st_size > 100_000:
        return "skipped"
    for attempt in range(3):
        try:
            save_image(
                post_json(
                    API_URL,
                    {"model": MODEL, "prompt": build_prompt(carousel, idx, slide), "response_format": "url"},
                    api_key,
                ),
                out,
            )
            return "ok"
        except Exception as exc:  # noqa: BLE001
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
    jobs = [(c, i, s) for c in CAROUSELS for i, s in enumerate(c["slides"], 1)]
    for c in CAROUSELS:
        (ROOT / c["slug"]).mkdir(parents=True, exist_ok=True)
    print(f"Generating {len(jobs)} slides ({len(CAROUSELS)} carousels, batch 16-20)", flush=True)
    print("After images: ./.venv/bin/python build_pdfs.py", flush=True)
    fails = []
    done = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futs = {ex.submit(job, api_key, c, i, s, force): (c["slug"], i) for c, i, s in jobs}
        for fut in concurrent.futures.as_completed(futs):
            slug, i = futs[fut]
            done += 1
            try:
                st = fut.result()
                print(f"[{done}/{len(jobs)}] {st.upper()} {slug} #{i}", flush=True)
            except Exception as e:  # noqa: BLE001
                fails.append(f"{slug} #{i}: {e}")
                print(f"[{done}/{len(jobs)}] FAIL {slug} #{i}: {e}", flush=True)
    print(f"Done. Failures: {len(fails)}", flush=True)
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
