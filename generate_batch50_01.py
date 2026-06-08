#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate only batch 50 carousel 01 images (10 slides)."""

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

ROOT = Path(__file__).resolve().parent / "AI_Business_Carousels"
SLUG = "50_Series_Carousels/01_50_Claude_Agent_Secrets"
API_URL = "https://api.apiyi.com/v1/images/generations"
MODEL = "gpt-image-2-all"
MAX_WORKERS = int(os.environ.get("CAROUSEL_WORKERS", "8"))
TIMEOUT = 300

BASE_STYLE = """
Premium Instagram carousel slide in 3:4 vertical portrait ratio (1080x1440 feel).
Strong editorial layout matching @piyush.glitch AI_Business_Carousels posts 01-15.
Allowed look: cream paper grid OR blue-sky editorial portrait.
Typography: bold black sans headline + one coral accent. Spell everything correctly.
Required footer: @piyush.glitch at bottom-left.
Required page marker: bottom-right exactly as x/10.
Required branding every slide: accurate Anthropic Claude terracotta logo badge.
No watermark, no lorem ipsum, no random gibberish.
"""

COVER_STYLE = """
Cover must be scroll-stopping with high-contrast hook headline.
Top row micro label: AI FOR BUSINESS.
Claude terracotta logo visible prominently.
"""

INTERIOR_STYLE = """
Interior slides: clean grid structure, 5 concrete secrets as concise bullets.
Claude terracotta logo badge top-right on every slide.
"""

SLIDES = [
    (
        "I tested 50 Claude agent tricks. These 12 actually ship work.",
        "5 truths: Scope beats prompts; Subagents protect context; Hooks enforce rules; MCP beats copy-paste; /compact needs focus.",
        "Blue-sky editorial founder portrait at desk with floating terminal cards. Huge bold headline stack. Terracotta Claude logo card near top. Strong coral underline under 'ship work'.",
    ),
    (
        "Subagents: 5 secrets that cut chaos",
        "1) .claude/agents is reusable team infra 2) Use Haiku for explore 3) tools allowlist per agent 4) isolation worktree for parallel edits 5) maxTurns to prevent wandering",
        "Cream grid, architecture cards showing orchestrator -> explore/build/review agents, terracotta Claude badge top-right.",
    ),
    (
        "Hooks: 5 secrets most teams skip",
        "1) PreToolUse can block danger 2) PostToolUse auto-fixes format 3) Stop hooks run final checks 4) matcher regex narrows scope 5) exit code 2 blocks risky calls",
        "Terminal + settings.json visual, coral danger shield, Claude terracotta logo badge.",
    ),
    (
        "MCP: 5 connector secrets for real ops",
        "1) Start read-only tools first 2) Split read/write connectors 3) Keep schemas narrow 4) Track identity on every call 5) Test servers with MCP Inspector",
        "Connector hub with GitHub/Postgres/Slack icons and one central Claude logo tile; cream editorial grid.",
    ),
    (
        "Skills: 5 SKILL.md secrets",
        "1) Description drives auto-invoke 2) Keep SKILL.md short 3) Put depth in references/ 4) Add deterministic scripts/ 5) Golden examples beat vibes",
        "Folder anatomy illustration .claude/skills with SKILL.md highlighted and terracotta Claude badge.",
    ),
    (
        "/compact: 5 context-saving secrets",
        "1) Compact at task boundaries 2) Use '/compact focus on X' 3) Keep CLAUDE.md stable 4) Avoid compact loops 5) Re-verify constraints after compact",
        "Context meter UI dropping from high to low, coral focus chip, blue-sky editorial lighting.",
    ),
    (
        "Effort + model: 5 routing secrets",
        "1) High effort for architecture 2) Medium for daily edits 3) Cheap model for search 4) Escalate only on risk 5) Track cost per successful run",
        "Dial controls for effort and model routing funnel, premium cream grid and Claude logo badge.",
    ),
    (
        "Hidden workflows: 5 operator loops",
        "1) Plan -> Explore -> Build -> Review 2) Parallel worktrees 3) Hook-driven test-fix loop 4) Night cloud run + local verify 5) Incident -> eval case",
        "Workflow timeline cards, dev-ops editorial style, terracotta accents, Claude logo top-right.",
    ),
    (
        "GitHub refs: 5 repos worth cloning",
        "1) modelcontextprotocol/servers 2) modelcontextprotocol/inspector 3) anthropics/claude-code 4) punkpeye/awesome-mcp-servers 5) promptfoo/promptfoo",
        "GitHub repo cards with readable names, clean editorial board, Claude terracotta logo badge and coral tabs.",
    ),
    (
        "5 final secrets + full pack",
        "1) Guardrails before autonomy 2) Eval gates before writes 3) Project memory beats chat memory 4) Narrow tools increase reliability 5) Review logs weekly. Comment AI.",
        "Strong CTA design, coral 'Comment AI' button, cream grid background, clear 10/10 marker, Claude logo visible.",
    ),
]


def slugify(text: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "_", text.strip()).strip("_")[:64]


def build_prompt(idx: int, slide: tuple[str, str, str]) -> str:
    headline, body, visual = slide
    page = f"{idx}/10"
    style = f"{BASE_STYLE}\n{COVER_STYLE}" if idx == 1 else f"{BASE_STYLE}\n{INTERIOR_STYLE}"
    return f"""
3:4 vertical Instagram carousel slide.
{style}

HEADLINE (render exactly): {headline}
BODY (render exactly): {body}
Footer left exactly: @piyush.glitch
Footer right exactly: {page}
Slide number must be visible as {page}.

VISUAL:
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
        req = urllib.request.Request(item["url"], headers={"User-Agent": "batch50-01/1.0"})
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
    if not force and out.exists() and out.stat().st_size > 80_000:
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
        print("Missing API key", file=sys.stderr)
        return 2

    force = "--force" in sys.argv
    slides = list(enumerate(SLIDES, 1))
    print(f"Generating {len(slides)} slides for {SLUG}", flush=True)
    failures: list[str] = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(job, api_key, idx, slide, force): idx for idx, slide in slides}
        done = 0
        for fut in concurrent.futures.as_completed(futures):
            idx = futures[fut]
            done += 1
            try:
                status = fut.result()
                print(f"[{done}/{len(slides)}] {status.upper()} slide #{idx}", flush=True)
            except Exception as exc:  # noqa: BLE001
                failures.append(f"slide #{idx}: {exc}")
                print(f"[{done}/{len(slides)}] FAIL slide #{idx}: {exc}", flush=True)

    print(f"Done. Failures: {len(failures)}", flush=True)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
