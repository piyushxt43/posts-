#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regenerate cover slide 01 for 7 hook carousels with dominant Claude logo."""

from __future__ import annotations

import base64
import json
import os
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent / "AI_Business_Carousels"
API_URL = "https://api.apiyi.com/v1/images/generations"
MODEL = "gpt-image-2-all"
TIMEOUT = 300

COVER_STYLE = """
Premium Instagram carousel COVER ONLY. STRICT 3:4 vertical portrait (1080x1440).
Surreal editorial photoreal - cinematic daylight, lens flare, high contrast, magazine quality.
CLAUDE LOGO DOMINANT: enormous official Anthropic Claude app icon (terracotta/coral rounded square,
white sparkle star mark) floating 3D card on RIGHT - at least 35% of frame height. Accurate logo.
BOTTOM WATERMARK: giant semi-transparent lowercase "claude" spanning nearly full width.
Top micro-row: left "PIYUSH.GLITCH" center hook category tag right "AI FOR BUSINESS".
Bold stacked headline (render EXACT text). One key phrase hand-underlined in rough black stroke.
Footer: @piyush.glitch bottom-left. NO slide numbers on this cover.
Ultra sharp, correct spelling, no lorem ipsum, no watermarks.
"""

HOOKS = [
    {
        "slug": "27_Claude_Skills_To_Steal",
        "category": "STEAL THIS",
        "headline": "Steal the Claude skill that turns one topic into a 8-slide carousel",
        "underline": "8-slide carousel",
        "sub": "Package once. Run forever. Highest-save format on business Instagram.",
        "visual": (
            "COVER: surreal floating archive of glowing SKILL.md folders in warm library light, "
            "professional reaching for a folder labeled carousel-factory. HUGE Claude logo card right. "
            "Faded 'skills' watermark bottom. Headline exact as given. Underline '8-slide carousel'. "
            "Coral accent on the number 8."
        ),
        "out_name": "01_Steal_The_Claude_Carousel_Skill.png",
    },
    {
        "slug": "08_Agent_Evals_As_Release_Gates",
        "category": "I TESTED IT",
        "headline": "I ran 12 AI agents for 30 days. 3 survived.",
        "underline": "3 survived",
        "sub": "Nine looped, hallucinated tools, or cost more to babysit than doing it yourself.",
        "visual": (
            "COVER: surreal scoreboard arena - 12 agent pods, only 3 glowing green, 9 dim red X marks. "
            "Operator with clipboard reviewing results. HUGE Claude logo card right. "
            "Faded 'eval' watermark bottom. Render headline EXACT. Underline '3 survived'. "
            "Big numbers 12 and 3 in coral."
        ),
        "out_name": "01_12_Agents_30_Days_3_Survived.png",
    },
    {
        "slug": "13_Claude_MCP_For_Operators",
        "category": "NUMBER + OUTCOME",
        "headline": "7 MCP connectors that replace a 5-person ops stack",
        "underline": "5-person ops stack",
        "sub": "Postgres, GitHub, Slack, Notion, Drive, Meta Ads, internal API - read-first, write gated.",
        "visual": (
            "COVER: surreal command center - seven connector cables plug into central Claude terracotta hub, "
            "replacing five empty operator desks fading into background. HUGE Claude logo card right. "
            "Faded 'mcp' watermark bottom. Headline EXACT. Underline '5-person ops stack'. "
            "Coral badge with number 7 on connector hub."
        ),
        "out_name": "01_7_MCP_Connectors_5_Person_Ops_Stack.png",
    },
    {
        "slug": "30_Claude_md_Mastery",
        "category": "SILENTLY KILLING",
        "headline": "The CLAUDE.md mistake silently wasting half your tokens",
        "underline": "half your tokens",
        "sub": "Bloat or no file - both tax every Claude Code session before you type a word.",
        "visual": (
            "COVER: surreal scene - giant CLAUDE.md document leaking glowing token particles into void, "
            "developer alarmed at context meter showing 50% gone. HUGE Claude logo card right. "
            "Faded 'CLAUDE.md' watermark bottom. Headline EXACT. Underline 'half your tokens'. "
            "Context meter at 50% in coral warning."
        ),
        "out_name": "01_CLAUDE_md_Mistake_Half_Your_Tokens.png",
    },
    {
        "slug": "12_Claude_Artifacts_For_Business",
        "category": "BOLD CLAIM",
        "headline": "I cut content time 80% with one Claude skill",
        "underline": "80%",
        "sub": "Artifact + Project + carousel skill - long-form, carousel, newsletter from one pipeline.",
        "visual": (
            "COVER: surreal split - left side cluttered content chaos (many tabs), right side clean Claude "
            "Artifact panels with 80% time-saved gauge. Creator relieved. HUGE Claude logo card right. "
            "Faded 'artifact' watermark bottom. Headline EXACT. Underline '80%'. "
            "Big coral 80% stat prominent."
        ),
        "out_name": "01_80_Percent_Content_Cut_One_Claude_Skill.png",
    },
    {
        "slug": "19_Claude_Daily_Business_Ops",
        "category": "EVERYONE'S WRONG",
        "headline": "Everyone's chasing GPT. Claude quietly won business ops.",
        "underline": "won business ops",
        "sub": "Projects, Artifacts, MCP, daily modes - operators picked infrastructure over demos.",
        "visual": (
            "COVER: surreal race scene - crowd chasing glowing GPT logo billboards, lone operator at calm "
            "Claude desk shipping daily ops checklist while others sprint past. HUGE Claude logo card right "
            "dominant. Faded 'claude' watermark bottom. Headline EXACT. Underline 'won business ops'. "
            "Muted GPT signs in background blur."
        ),
        "out_name": "01_Everyone_Chasing_GPT_Claude_Won_Ops.png",
    },
    {
        "slug": "26_Claude_Hidden_Commands",
        "category": "HIDDEN / INSIDER",
        "headline": "5 Claude commands Anthropic doesn't put in the docs",
        "underline": "doesn't put in the docs",
        "sub": "/compact focus, /btw, /init, /effort, /loop - CLI shipped faster than the manual.",
        "visual": (
            "COVER: surreal dark terminal room - glowing command list floating, official docs booklet "
            "missing pages, insider glow on five commands highlighted in coral. Hoodie operator. "
            "HUGE Claude logo card right. Faded 'commands' watermark bottom. Headline EXACT. "
            "Underline 'doesn't put in the docs'. Number 5 in coral circle."
        ),
        "out_name": "01_5_Claude_Commands_Not_In_The_Docs.png",
    },
]


def build_prompt(h: dict) -> str:
    return f"""
3:4 vertical Instagram carousel COVER slide (portrait only).
{COVER_STYLE}

Category tag: {h['category']}

HEADLINE (render exactly, large bold stacked):
{h['headline']}

Underline phrase with rough black stroke: {h['underline']}

Supporting line (smaller): {h['sub']}

Footer: @piyush.glitch

VISUAL:
{h['visual']}

Claude terracotta logo must be accurate, hero-sized, major visual attraction on the right.
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
        req = urllib.request.Request(item["url"], headers={"User-Agent": "hook-covers/1.0"})
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
    hooks = HOOKS
    if only:
        hooks = [h for h in HOOKS if any(h["slug"].startswith(x) or x in h["slug"] for x in only)]
    for h in hooks:
        folder = ROOT / h["slug"]
        folder.mkdir(parents=True, exist_ok=True)
        for old in folder.glob("01_*.png"):
            old.unlink()
        out = folder / h["out_name"]
        print(f"Generating {h['slug']} -> {out.name}", flush=True)
        save_image(
            post_json(
                API_URL,
                {"model": MODEL, "prompt": build_prompt(h), "response_format": "url"},
                api_key,
            ),
            out,
        )
        print(f"OK {out}", flush=True)
    print("Done. Run: ./.venv/bin/python build_pdfs.py", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
