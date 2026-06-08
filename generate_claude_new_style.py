#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regenerate claude new carousels in AI_Business_Carousels 01-15 style + Claude logo."""

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

ROOT = Path(__file__).resolve().parent / "claude new"
API_URL = "https://api.apiyi.com/v1/images/generations"
MODEL = "gpt-image-2-all"
MAX_WORKERS = int(os.environ.get("CAROUSEL_WORKERS", "40"))
TIMEOUT = 300

# Matches generate_carousels.py posts 01-15
STYLE = """
Create a premium Instagram carousel slide in modern editorial AI-business style.
3:4 vertical portrait first.
Reference: luxury tech creator carousel like @piyush.glitch posts 01-15 -
cream grid paper background #F4EEDE OR blue-sky editorial portrait background,
huge confident typography, clean spacing, high-end startup/design-studio feel,
bold black sans-serif mixed with one elegant italic serif accent word,
coral/red #EF5E45 highlight tabs and brush underlines,
subtle UI cards and diagrams, thin black rules,
polished Figma-like composition. Readable, sharp, correctly spelled.
No lorem ipsum, no watermarks, no clutter, no Instagram UI.
Footer @piyush.glitch bottom-left, page number bottom-right like 1/8 2/8.
"""

CLAUDE_BRAND = """
CLAUDE LOGO (required on every slide):
Official Anthropic Claude app icon - terracotta/coral-orange rounded square with white sparkle star mark.
Cover slide: logo prominent top-left or top-center near AI FOR BUSINESS pill, accurate not distorted.
Interior slides: small Claude logo badge top-right corner on every slide.
Terracotta accent #D97757 / coral #EF5E45 for Claude branding.
"""

COVER_STYLE = """
COVER SLIDE style (match posts 01-15):
Either (A) blue-sky editorial portrait - close crop professional, giant white or black headline overlay,
one key word in italic serif OR inside coral highlight box, Claude logo visible;
OR (B) cream grid paper - bold black headline, one italic serif word with coral box highlight,
clean 3D object or UI illustration, Claude logo on card.
Label pill top: AI FOR BUSINESS - XX with small Claude icon in pill.
"""

INTERIOR_STYLE = """
Interior slide (match posts 02-07 style):
Cream grid paper background. Pill label top-left AI FOR BUSINESS - XX.
Large bold black headline with coral brush-stroke underline.
Small coral arrow icon beside body text. Clean UI cards or diagram center.
Small Claude terracotta logo badge top-right. Footer @piyush.glitch and page X/8.
"""


def C(title, slug, num, angle, slides):
    return {"title": title, "slug": slug, "num": num, "angle": angle, "slides": slides}


CAROUSELS: list[dict[str, Any]] = [
    C(
        "Steal This Claude Carousel Skill", "27_Claude_Skills_To_Steal", "27",
        "SKILL.md packages an 8-slide carousel workflow - load on demand, highest-save format.",
        [
            ("Steal the Claude skill that turns one topic into a 8-slide carousel",
             "Package once. Run forever. A SKILL.md folder outputs hook, 8 headlines, body and CTA.",
             "Cream grid cover like post 05: 3D expanding folder tabs labeled carousel-factory, RESEARCH, CONTENT. Bold black headline, italic serif word carousel in coral box. Claude logo on folder label."),
            ("Anatomy Of A Skill",
             "Folder with SKILL.md: YAML frontmatter name + description, then markdown steps under 500 lines.",
             "SKILL.md card split frontmatter vs body, coral tabs, cream grid diagram."),
            ("Description Is The Trigger",
             "Claude reads every skill description to decide when to load it. Front-load the use case.",
             "Description field highlighted as trigger key with coral arrow, UI mockup."),
            ("Progressive Disclosure",
             "Metadata always loaded, SKILL.md on trigger, references/ and scripts/ only when needed.",
             "Three-level pyramid diagram coral numbered levels on cream grid."),
            ("Control Invocation",
             "disable-model-invocation for side effects; user-invocable false for background knowledge.",
             "Frontmatter flags table with lock icons, clean cards."),
            ("Bundle Scripts",
             "Python, JS or Bash in scripts/ - Claude runs via bash, only output uses context.",
             "scripts folder UI card with code snippet chip."),
            ("Where Skills Live",
             "Project .claude/skills/ or global ~/.claude/skills/. Same in Code, API and claude.ai.",
             "Two path cards project vs global with slash command chip."),
            ("Comment AI",
             "Want 7 ready-to-paste Claude Skills? Comment AI for the pack.",
             "Clean CTA slide coral Comment AI pill button, cream or dark footer."),
        ],
    ),
    C(
        "12 Agents 3 Survived", "08_Agent_Evals_As_Release_Gates", "08",
        "30-day field test: 12 agents, 3 survived - eval gates for production automation.",
        [
            ("I ran 12 AI agents for 30 days. 3 survived.",
             "Nine looped, hallucinated tools, or cost more to babysit than doing it yourself.",
             "Blue-sky editorial cover like post 07: professional portrait, white bold headline, numbers 12 and 3 in coral. Claude logo in top pill. Underline survived in coral box."),
            ("Not Trivia Benchmarks",
             "Useful evals are your workflows: refund policy, CRM mapping, on-call runbook, PR standards.",
             "Four business workflow test cards on cream grid with coral headers."),
            ("Three Eval Types",
             "Task success. Safety boundaries. Operational behavior - loops, retries, latency, cost.",
             "Three-column comparison cards with icons pass/fail."),
            ("Golden Scenarios",
             "Save real edge cases and expected outputs. Run before prompt, model or tool changes.",
             "Golden dataset folder UI with star chips on cream grid."),
            ("Tool-Use Tests",
             "Check whether the agent calls the right tool, with the right inputs, at the right time.",
             "Tool-call timeline with green pass red fail markers."),
            ("Regression Gate",
             "If a new prompt improves style but breaks compliance, it should not ship.",
             "Release gate UI red stop green go with coral accent."),
            ("Metrics That Matter",
             "Success rate, intervention rate, tool error rate, cost per task, hallucinated action rate.",
             "Analytics dashboard cards five KPIs on cream grid."),
            ("Comment AI",
             "Want the agent-eval checklist? Comment AI and get the scorecard.",
             "Final CTA coral button, test card icons, clean footer."),
        ],
    ),
    C(
        "7 MCP Connectors Ops Stack", "13_Claude_MCP_For_Operators", "13",
        "Seven MCP connectors replace a 5-person ops glue-work stack when scoped read-first.",
        [
            ("7 MCP connectors that replace a 5-person ops stack",
             "Postgres, GitHub, Slack, Notion, Drive, Meta Ads, internal API - read-first, write gated.",
             "Cream grid cover like post 04: hub-and-spoke diagram, 7 connector cards, coral center Claude hub with logo. Bold black headline, number 7 in coral tab."),
            ("What MCP Is",
             "Model Context Protocol - USB-C for AI tools. One standard, many apps.",
             "Simple hub diagram coral center burst, cream grid."),
            ("Read Actions",
             "Pull open PRs, query CRM, fetch Notion pages, read support tickets.",
             "Read-only tool cards with green checkmarks."),
            ("Write Actions",
             "Post Slack updates, create issues, draft emails - with approval gates.",
             "Write tools behind approval gate shield icon."),
            ("Starter Connectors",
             "GitHub, Google Drive, Slack, Postgres, Linear, Meta Ads MCP.",
             "Six stylized app tiles in circle on cream grid."),
            ("Security Pattern",
             "Scope tokens, read-only first, log every action, human approve writes.",
             "Shield checklist four items coral checkmarks."),
            ("Ops Workflow",
             "Morning digest: pull metrics, summarize blockers, post to channel.",
             "Three-step workflow timeline cards."),
            ("Comment AI",
             "Want the Claude MCP connector map? Comment AI and get the list.",
             "CTA slide coral button clean layout."),
        ],
    ),
    C(
        "CLAUDE.md Token Mistake", "30_Claude_md_Mastery", "30",
        "Lean CLAUDE.md stops silent token bleed - the only context that survives /compact.",
        [
            ("The CLAUDE.md mistake silently wasting half your tokens",
             "Bloat or no file - both tax every Claude Code session before you type a word.",
             "Cream grid cover: CLAUDE.md document UI with context meter at 50% coral warning. Bold headline, half your tokens in italic serif coral box. Claude logo on doc tab."),
            ("What To Put In It",
             "Stack, exact test/lint/build commands, one-paragraph architecture, hard NEVER list.",
             "CLAUDE.md section cards labeled Commands Architecture NEVER coral tabs."),
            ("Keep It Under 500 Lines",
             "Short root file plus linked docs in .claude/rules/ - load only what the task needs.",
             "Root file linking scoped rule files diagram on cream grid."),
            ("It Survives /compact",
             "Conversation gets summarized; CLAUDE.md does not. Cold starts disappear.",
             "Before after context wiped vs CLAUDE.md persists anchor icon."),
            ("Conditional Loading",
             "Before editing auth, read docs/auth-flow.md - deep context only when relevant.",
             "Trigger line pulling doc on demand coral arrow flow."),
            ("Output Styles",
             "Switch /output-style to Explanatory or Learning, or write custom format file.",
             "Output style selector UI three modes."),
            ("Memory You Teach Once",
             "Remember our API uses snake_case JSON - Claude persists and stops asking.",
             "Memory note saved chip recurring convention."),
            ("Comment AI",
             "Want a battle-tested CLAUDE.md template? Comment AI.",
             "CTA slide coral button terminal aesthetic clean."),
        ],
    ),
    C(
        "80 Percent Content Cut", "12_Claude_Artifacts_For_Business", "12",
        "Artifact + Project + one skill cuts content production time ~80%.",
        [
            ("I cut content time 80% with one Claude skill",
             "Artifact + Project + carousel skill - long-form, carousel, newsletter from one pipeline.",
             "Blue-sky editorial cover like post 01: creator portrait, white bold headline, 80% in coral box italic. Claude logo in pill header. Before/after time chips subtle."),
            ("Live Documents",
             "Rewrite policies, proposals and SOPs in a side panel you edit and export.",
             "Split chat plus document artifact mockup cream grid."),
            ("Mini Apps",
             "Build ROI calculators, pricing tables and internal tools without a sprint.",
             "Simple app artifact with coral CTA button."),
            ("Data Visuals",
             "Paste CSV, get charts and narrative analysis in one artifact.",
             "Chart artifact card on cream grid."),
            ("Iterate Fast",
             "Ask for v2, v3 in plain English - artifact updates in place.",
             "Version tabs v1 v2 v3 coral active tab."),
            ("Share With Stakeholders",
             "Send artifact link or export PDF - no dev deploy needed.",
             "Share and export icon row clean UI."),
            ("Business Use Cases",
             "Board decks, landing pages, onboarding portals, competitive battlecards.",
             "Four use-case tiles 2x2 grid coral labels."),
            ("Comment AI",
             "Want the 80% content skill file? Comment AI for the playbook.",
             "CTA slide Claude logo corner coral button."),
        ],
    ),
    C(
        "Claude Won Business Ops", "19_Claude_Daily_Business_Ops", "19",
        "Daily ops infrastructure: Projects, Artifacts, MCP, MORNING/INBOX/EOD modes.",
        [
            ("Everyone's chasing GPT. Claude quietly won business ops.",
             "Projects, Artifacts, MCP, daily modes - operators picked infrastructure over demos.",
             "Blue-sky editorial cover like post 02: professional calm at desk, bold white headline, won business ops in coral italic box. Claude logo prominent. Subtle GPT blur in background optional muted."),
            ("Morning Brief Ritual",
             "Paste calendar + Slack highlights + KPI screenshot. Claude returns 5 priorities with owners.",
             "Morning dashboard mockup 5 bullet priorities coral numbers cream grid."),
            ("Inbox Triage Mode",
             "Forward 20 emails. Claude sorts: reply now, delegate, archive, needs data.",
             "Four column email buckets coral labels clean cards."),
            ("Meeting Prep In 3 Min",
             "Upload attendee context, last notes, goal. Claude gives agenda + 3 smart questions.",
             "Meeting card agenda and questions UI."),
            ("Decision Memo Template",
             "Options, pros/cons, recommendation, what would change my mind - one page max.",
             "Decision matrix template cream grid coral headers."),
            ("End Of Day Recap",
             "What shipped, what blocked, tomorrow top 3. Paste to team Slack.",
             "EOD recap card with timestamp coral accent."),
            ("Project Not Chat",
             "Save daily ops instructions once in Claude Project. Same format every morning.",
             "Project card vs scattered chat comparison two columns."),
            ("Comment AI",
             "Want the Daily Ops Project template? Comment AI.",
             "CTA slide coral button clean footer."),
        ],
    ),
    C(
        "5 Commands Not In Docs", "26_Claude_Hidden_Commands", "26",
        "Five Claude Code commands the docs underplay - /compact focus, /btw, /init, /effort, /loop.",
        [
            ("5 Claude commands Anthropic doesn't put in the docs",
             "/compact focus, /btw, /init, /effort, /loop - CLI shipped faster than the manual.",
             "Cream grid cover like post 01 interior terminal aesthetic: clean terminal card listing 5 commands highlighted coral. Bold black headline, doesn't put in the docs in italic coral box. Claude logo on terminal window."),
            ("/compact focus",
             "Plain /compact is lossy. Add focus on X so the summary keeps the constraint you cannot lose.",
             "Terminal UI /compact focus on auth context bar preserved coral highlight."),
            ("/btw Saves Context",
             "Ask a side question with /btw without burning your main thread context budget.",
             "Side question bubble outside main thread context meter steady UI."),
            ("/init Writes CLAUDE.md",
             "Run /init in a repo - Claude scans conventions and drafts starter CLAUDE.md in minutes.",
             "Repo scan generating CLAUDE.md file animation style UI card."),
            ("Prompt Prefixes",
             "ULTRATHINK, /skeptic, L99 - stack 2-3 for high-stakes work.",
             "Prefix chips stacked on prompt coral underline cream grid."),
            ("/effort + /model",
             "Dial reasoning effort low/med/high and switch model per task.",
             "Effort and model dial UI token cost readout."),
            ("Watch The Cost Burners",
             "/loop, /goal+/loop and /schedule can run for hours and bill while you are away.",
             "Warning panel three commands coral border alert icons."),
            ("Comment AI",
             "Want the full Claude Code command cheat sheet? Comment AI.",
             "CTA slide coral button terminal clean footer."),
        ],
    ),
]


def slugify(text: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "_", text.strip()).strip("_")[:60]


def build_prompt(carousel: dict, idx: int, slide: tuple[str, str, str]) -> str:
    headline, body, visual = slide
    num = carousel["num"]
    page = f"{idx}/8"
    block = f"{STYLE}\n{CLAUDE_BRAND}\n{COVER_STYLE}" if idx == 1 else f"{STYLE}\n{CLAUDE_BRAND}\n{INTERIOR_STYLE}"
    return f"""
3:4 vertical Instagram carousel slide.
{block}

Topic: {carousel['title']}
Angle: {carousel['angle']}
Slide: {page}

Headline (render exactly, large bold hierarchy): {headline}
Body (smaller supporting text): {body}
Label pill top-left: AI FOR BUSINESS - {num}
Footer: @piyush.glitch bottom-left | page {page} bottom-right

Visual direction:
{visual}

Match posts 01-15 typography and layout exactly. Claude logo required.
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
        req = urllib.request.Request(item["url"], headers={"User-Agent": "claude-new-style/1.0"})
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
    jobs = [(c, i, s) for c in CAROUSELS for i, s in enumerate(c["slides"], 1)]
    print(f"Regenerating {len(jobs)} slides in {ROOT} (posts 01-15 style + Claude logo)", flush=True)
    fails, done = [], 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futs = {ex.submit(job, api_key, c, i, s, force): (c["slug"], i) for c, i, s in jobs}
        for fut in concurrent.futures.as_completed(futs):
            slug, i = futs[fut]
            done += 1
            try:
                st = fut.result()
                print(f"[{done}/{len(jobs)}] {st.upper()} {slug} #{i}", flush=True)
            except Exception as e:
                fails.append(f"{slug} #{i}: {e}")
                print(f"[{done}/{len(jobs)}] FAIL {slug} #{i}: {e}", flush=True)
    print(f"Done. Failures: {len(fails)}", flush=True)
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
