#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 10 carousels (21-30): 5 tool spotlights + 5 Claude tactics.

Image-only. 3:4 ratio. NO slide numbers rendered on images (post in any order).
Strong editorial hook covers. Footer @piyush.glitch only - no page number.
"""

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

BASE_STYLE = """
Premium Instagram carousel slide. STRICT 3:4 vertical portrait aspect ratio (1080x1440 feel).
Editorial design-magazine quality. Ultra sharp, correct spelling, no lorem ipsum, no watermarks.
IMPORTANT: do NOT render any slide numbers, page numbers, or counters like 1/8 anywhere on the image.
Footer text only: lowercase @piyush.glitch small at bottom-left. No page index anywhere.
"""

COVER_HOOK = """
COVER SLIDE - scroll-stopping editorial hook:
- Surreal cinematic photoreal scene matching the topic (see VISUAL).
- HUGE provocative headline stack (3-5 short lines), one punchline word hand-underlined in rough black stroke.
- Big confident typography, high contrast, lens-flare daylight or moody studio per topic.
- Brand mark of the tool shown as a clean floating card (accurate logo) where specified.
- Small top row micro-caps: left brand tag, right "AI FOR BUSINESS" (NO numbers).
- Mood: thought-leader, premium, makes people stop scrolling. Not a generic tech template.
"""

INTERIOR_STYLE = """
Interior slide: clean editorial layout, cream grid #F4EEDE OR soft gradient per topic.
Coral #EF5E45 accent tab/underline, bold black headline, readable supporting copy.
Small accurate tool logo badge top-right. Operator/playbook tone. NO page numbers anywhere.
"""


def C(title, slug, angle, slides):
    return {"title": title, "slug": slug, "angle": angle, "slides": slides}


CAROUSELS: list[dict[str, Any]] = [
    # ---------------- BATCH A: TOOL SPOTLIGHTS ----------------
    C(
        "GPT Power Moves", "21_GPT_Power_Moves",
        "GPT-5.2 plus Agent mode, Codex and Atlas turn ChatGPT from chatbot into a worker that takes action.",
        [
            ("Everyone Types Prompts. Almost No One Uses GPT Like This.",
             "GPT-5.2 + Agent mode + Codex + Atlas browser. The 1% run tasks, not chats.",
             "COVER: surreal office worker at desk floating in clouds, bright sky, sun flare. Floating ChatGPT logo card (black/white spiral) right side. Giant faded 'GPT' watermark across bottom. Headline stack: 'Stop chatting.' 'Start delegating.' 'GPT works now.' Underline 'works'."),
            ("GPT-5.2: Instant vs Thinking",
             "Instant for fast everyday work. Thinking for spreadsheets, financial modeling, hard logic. Pick from the composer.",
             "Split card Instant lightning vs Thinking brain, coral divider, ChatGPT badge top-right."),
            ("Agent Mode Does The Work",
             "Type /agent or pick Agent mode. It browses, fills forms, builds slides and sheets - you approve key actions.",
             "Browser window with agent narration steps, approval checkmark, coral highlights."),
            ("Schedule It To Repeat",
             "Finish a task, hit the clock icon - run it daily, weekly, monthly. Manage all at chatgpt.com/schedules.",
             "Calendar with recurring task chips, clock icon, cream grid."),
            ("Codex Ships Code",
             "Codex runs in terminal, IDE and cloud - delegate real engineering, not snippets.",
             "Terminal + IDE split with code diff, coral cursor."),
            ("Atlas Browser",
             "OpenAI's AI browser summarizes pages, compares products and acts across the web.",
             "Minimal browser UI summarizing a page, sidebar insights."),
            ("Connect Your World",
             "Link email, calendar and docs so GPT pulls the right context before it acts - with permission gates.",
             "Hub of connector icons around ChatGPT core, shield badge."),
            ("Comment AI",
             "Want the GPT power-user prompt pack and Agent playbook? Comment AI.",
             "CTA editorial, ChatGPT logo corner, coral Comment AI button."),
        ],
    ),
    C(
        "Claude Power Moves", "22_Claude_Power_Moves",
        "Claude Opus 4.8 plus Projects, Artifacts, Skills and MCP is a business operating layer, not a chatbot.",
        [
            ("You Are Using 10% Of Claude. Here Is The Other 90%.",
             "Opus 4.8, Projects, Artifacts, Skills, MCP. Operators build systems - not single chats.",
             "COVER: surreal professional at retro desk in vast green field, blue sky, sun flare. HUGE Claude logo card (terracotta sparkle) floating right. Giant faded 'claude' watermark bottom. Headline: 'It is not a chatbot.' 'It is an operating layer.' Underline 'operating layer'."),
            ("Opus 4.8 + Effort Control",
             "Choose high, extra or max effort on hard tasks. Same price as 4.7, better agents and coding.",
             "Effort selector high/extra/max slider, Claude badge top-right, coral accents."),
            ("Projects = Team Memory",
             "Instructions + knowledge files load every session. Stop re-uploading your brand guide.",
             "Project card with file chips and instruction panel, cream grid."),
            ("Artifacts Ship Deliverables",
             "Docs, calculators, charts and mini-apps in a side panel you edit and export.",
             "Artifact window beside chat, coral export button."),
            ("Skills: Teach Once",
             "SKILL.md folders package SOPs Claude loads only when relevant - clean context, repeatable output.",
             "Folder with SKILL.md icon, slash command chip."),
            ("MCP: Live Hands",
             "Connect GitHub, Postgres, Slack and Meta Ads. Claude reads truth and acts, not stale exports.",
             "Connector hub diagram, terracotta center."),
            ("Route Sonnet vs Opus",
             "Sonnet for volume, Opus for judgment, Haiku to classify. Track edit minutes not API cents.",
             "Routing funnel three tiers, coral labels."),
            ("Comment AI",
             "Want the full Claude operator stack PDF? Comment AI.",
             "CTA editorial, big Claude logo corner."),
        ],
    ),
    C(
        "Gemini Power Moves", "23_Gemini_Power_Moves",
        "Gemini 3 Pro and Deep Think bring 1M context, thinking levels and frontier science reasoning to operators.",
        [
            ("Gemini Quietly Became A Reasoning Monster. Most People Missed It.",
             "Gemini 3 Pro: 1M token context. Deep Think: gold-medal math and science. You are still using it like search.",
             "COVER: surreal scientist at glass desk on a cliff above cloud sea, aurora sky. Floating Gemini logo card (blue-purple spark) right. Giant faded 'gemini' watermark bottom. Headline: 'Not autocomplete.' 'A reasoning engine.' Underline 'reasoning'."),
            ("1M Token Context",
             "Drop entire codebases, long contracts, full transcript archives - Gemini 3 Pro holds the thread.",
             "Stack of huge documents feeding Gemini core, scale meter, badge top-right."),
            ("Thinking Level Control",
             "Set thinking_level low or high to balance depth, latency and cost. It replaced thinking_budget.",
             "Toggle low/high with cost vs depth axes, cream grid coral."),
            ("Deep Think Mode",
             "Specialized reasoning for science, math and engineering - olympiad-level on hard benchmarks.",
             "Brain with branching proof tree, equations faint background."),
            ("Multimodal Native",
             "Text, images, audio, video, PDFs and code in one window with strong long-context understanding.",
             "Five input type tiles converging, coral arrows."),
            ("Grounding With Search",
             "Pull fresh web facts with citations - ask for sources and recent-only results.",
             "Search grounding panel with cited links."),
            ("Free Tier Edge",
             "Generous personal free tier via Google auth; Vertex and API keys for production scale.",
             "Tier comparison free vs Vertex, simple chart."),
            ("Comment AI",
             "Want the Gemini long-context and Deep Think prompt pack? Comment AI.",
             "CTA editorial, Gemini logo corner."),
        ],
    ),
    C(
        "Cursor Power Moves", "24_Cursor_Power_Moves",
        "Cursor 3 makes the agent the IDE - parallel agents, Composer 2, Plan Mode, rules, skills and hooks.",
        [
            ("In Cursor 3, The Agent IS The IDE. You Are Still Autocompleting.",
             "Agents Window, parallel agents, Composer 2, Plan Mode. The editor changed - most users did not.",
             "COVER: surreal developer in a glass control room floating in space, monitors of code, neon-cool light. Floating Cursor logo card right. Giant faded 'cursor' watermark bottom. Headline: 'Not autocomplete.' 'An agent IDE.' Underline 'agent'."),
            ("Composer 2 Is Cursor's Model",
             "In-house frontier coding model, fast and cheap, tuned for codebase-wide semantic search.",
             "Model picker in agent tab header, speed gauge, badge top-right."),
            ("Run Agents In Parallel",
             "Each agent gets its own tab, context and git worktree via /worktree - concurrent edits never collide.",
             "Multiple agent tabs each with worktree branch, cream grid coral."),
            ("Plan Mode First",
             "It researches your codebase, asks questions, and writes a reviewable plan before any code.",
             "Plan document with checkboxes, edit-before-build flow."),
            ("Rules Over .cursorrules",
             "Use .cursor/rules/*.mdc: Always, Apply Intelligently, glob-scoped, or manual @-mention.",
             "Rules folder with mdc files, application-mode chips."),
            ("Agent Skills + Hooks",
             "SKILL.md + .cursor/hooks.json run scripts before/after actions - build loops that grind until tests pass.",
             "hooks.json snippet with test-fix loop arrow."),
            ("Cloud To Local Handoff",
             "Start a long refactor in the cloud, hand the diff to a local agent to finish and review.",
             "Cloud to laptop handoff diagram, screenshots chip."),
            ("Comment AI",
             "Want the Cursor 3 rules, skills and hooks starter pack? Comment AI.",
             "CTA editorial, Cursor logo corner."),
        ],
    ),
    C(
        "Draftly Power Moves", "25_Draftly_Power_Moves",
        "Draftly turns one deep prompt into scroll-synced cinematic product websites and matching visuals - no code.",
        [
            ("Your Product Page Looks Like Everyone Else's. That Is Why It Loses.",
             "Draftly prompts a scroll-synced cinematic site plus matching hero visuals from one brief. No code, no agency.",
             "COVER: surreal founder at desk on a beach with a giant glowing website screen rising from sand, golden hour. Floating Draftly wordmark card right. Giant faded 'draftly' watermark bottom. Headline: 'Static pages die.' 'Cinematic sites sell.' Underline 'sell'."),
            ("One Prompt, Full Experience",
             "Brief the nav, hero copy, scroll sections, palette and motion - Draftly builds the launch page.",
             "Prompt panel turning into a layered website mockup, coral accents, Draftly mark top-right."),
            ("Cinematic Scroll Motion",
             "Hero scrubs through extracted frames as users scroll - hardware-grade feel, not a static banner.",
             "Phone showing scroll-scrubbed hero frames sequence."),
            ("Image + Video Pipeline",
             "Generate photoreal hero stills and short product videos in the same brand world.",
             "Image and video tiles sharing one palette, pipeline arrows."),
            ("Brand World Locked",
             "Set palette, typography, lighting and a NEVER list once - every asset stays on-brand.",
             "Brand tokens card hex swatches, typography sample."),
            ("Built For DTC Verticals",
             "Earphones, fashion, coffee, sneakers, skincare, hotels - lookbook pacing, not catalog grids.",
             "Six vertical thumbnails in editorial grid."),
            ("Ship In An Afternoon",
             "What used to be a $20K agency build becomes a prompt pipeline you reuse across campaigns.",
             "Before/after agency invoice vs prompt pipeline, coral check."),
            ("Comment Draftly",
             "Want free trial access? Comment DRAFTLY and we send the link.",
             "CTA editorial, Draftly wordmark, coral Comment DRAFTLY button."),
        ],
    ),
    # ---------------- BATCH B: CLAUDE TACTICS ----------------
    C(
        "Claude Hidden Commands", "26_Claude_Hidden_Commands",
        "Claude Code ships faster than its docs - power users run slash commands and prompt prefixes most never see.",
        [
            ("Claude Code Has 70+ Commands. You Probably Use 5.",
             "Hidden slash commands and prompt prefixes that 10x output. The CLI shipped faster than its docs.",
             "COVER: surreal hacker desk in a dark room with a single terminal glowing, floating Claude logo card right, faded 'claude' watermark bottom. Headline: 'You use 5 commands.' 'Power users know 70.' Underline '70'."),
            ("/compact focus",
             "Plain /compact is lossy. Add 'focus on X' so the summary keeps the constraint you cannot lose.",
             "Terminal showing /compact focus on auth, context bar preserved, coral highlight, Claude badge top-right."),
            ("/btw Saves Context",
             "Ask a side question with /btw without burning your main thread's context budget.",
             "Side question bubble outside main thread, context meter steady."),
            ("/init Writes CLAUDE.md",
             "Run /init in a repo - Claude scans conventions and drafts a starter CLAUDE.md in minutes.",
             "Repo scan generating CLAUDE.md file, cream grid."),
            ("Prompt Prefixes",
             "ULTRATHINK for depth, /skeptic to challenge your premise, L99 for committed less-hedged answers. Stack 2-3.",
             "Prefix chips stacked on a prompt, coral underline."),
            ("/effort + /model",
             "Dial reasoning effort low/med/high and switch model per task - control cost and depth on the fly.",
             "Effort and model dials, token cost readout."),
            ("Watch The Cost Burners",
             "/loop, /goal+/loop and /schedule can run for hours and bill while you are away. Know which is which.",
             "Warning panel three long-running commands, coral border."),
            ("Comment AI",
             "Want the full Claude Code command cheat sheet? Comment AI.",
             "CTA editorial, Claude logo corner, terminal aesthetic."),
        ],
    ),
    C(
        "Claude Skills You Can Steal", "27_Claude_Skills_To_Steal",
        "Claude Skills are SKILL.md folders that package SOPs - load on demand, keep context clean, ship consistent output.",
        [
            ("Skills Are The Cheat Code Nobody Set Up. Steal These.",
             "A SKILL.md folder teaches Claude an SOP once. It loads only when relevant - clean context, repeatable output.",
             "COVER: surreal librarian in a floating archive of glowing folders, warm light, floating Claude logo card right, faded 'skills' watermark bottom. Headline: 'Stop re-prompting.' 'Package it once.' Underline 'once'."),
            ("Anatomy Of A Skill",
             "A folder with SKILL.md: YAML frontmatter (name + description) then markdown instructions. Keep under 500 lines.",
             "SKILL.md file split frontmatter vs body, coral tabs, Claude badge top-right."),
            ("Description Is The Trigger",
             "Claude reads every skill's description to decide when to load it. Front-load the use case, max ~1024 chars.",
             "Description field highlighted as a trigger key, cream grid."),
            ("Progressive Disclosure",
             "Metadata always loaded, SKILL.md on trigger, references/ and scripts/ only when needed - saves tokens.",
             "Three-level loading pyramid, coral levels."),
            ("Control Invocation",
             "disable-model-invocation for /deploy side effects; user-invocable false for background knowledge.",
             "Frontmatter flags table, lock icons."),
            ("Bundle Scripts",
             "Add scripts/ in Python, JS or Bash - Claude runs them via bash; only output uses context.",
             "scripts folder with code files, output chip."),
            ("Where Skills Live",
             "Project .claude/skills/ or global ~/.claude/skills/. Same pattern in Claude Code, API and claude.ai.",
             "Folder paths project vs global, slash command chip."),
            ("Comment AI",
             "Want 7 ready-to-paste Claude Skills? Comment AI.",
             "CTA editorial, Claude logo corner."),
        ],
    ),
    C(
        "Claude Hooks And Automation", "28_Claude_Hooks_Automation",
        "Hooks are scripts that always run on lifecycle events - deterministic guardrails the agent cannot skip.",
        [
            ("Prompts Beg. Hooks Enforce. This Is The Difference.",
             "Hooks run on every tool call - block secrets, auto-lint, gate writes. The agent cannot skip them.",
             "COVER: surreal security gate in a server room, glowing barrier, floating Claude logo card right, faded 'hooks' watermark bottom. Headline: 'Please remember to lint.' 'No. Make it a rule.' Underline 'rule'."),
            ("PreToolUse Blocks Danger",
             "Scan Bash commands for sk_live, AKIA or PRIVATE KEY and return block - the call never runs.",
             "Hook intercepting a shell command, red stop, coral, Claude badge top-right."),
            ("PostToolUse Auto-Fixes",
             "Run prettier or eslint --fix after every Write/Edit so the agent never leaves messy diffs.",
             "Auto-format running after edit, green check, cream grid."),
            ("Configure In settings.json",
             "Hooks live under hooks.PreToolUse and hooks.PostToolUse - user, project or managed scope.",
             "settings.json snippet with hook blocks, coral keys."),
            ("Deny Rules Beat Prompts",
             "Block rm -rf, curl | bash and git push --force globally - safer than asking nicely.",
             "Deny list panel with blocked commands, shield."),
            ("Build Grind Loops",
             "A hook returning a follow-up message keeps the agent iterating until all tests pass.",
             "Loop diagram run tests, fix, repeat until green."),
            ("Exit Codes Matter",
             "Hook exits 2 to block a tool call; stdin carries JSON context you can parse and decide on.",
             "Exit code 2 = block flow chart, JSON stdin."),
            ("Comment AI",
             "Want copy-paste hook scripts for safety and auto-fix? Comment AI.",
             "CTA editorial, Claude logo corner, terminal aesthetic."),
        ],
    ),
    C(
        "Claude Prompting Secrets", "29_Claude_Prompting_Secrets",
        "Claude rewards structure - XML tags, examples, prefilled format and thinking turn vague chats into reliable output.",
        [
            ("Claude Is Not Mind-Reading. It Is Reading Your Structure.",
             "XML tags, gold examples, format contracts and thinking - the difference between a guess and a deliverable.",
             "COVER: surreal architect at a drafting table building a glowing structured document, blueprint sky, floating Claude logo card right, faded 'prompt' watermark bottom. Headline: 'Vague in, vague out.' 'Structure wins.' Underline 'Structure'."),
            ("Wrap Inputs In XML Tags",
             "Use <context>, <example>, <rules> tags - Claude parses sections cleanly instead of guessing boundaries.",
             "Prompt with XML tag sections color-coded, coral, Claude badge top-right."),
            ("Two Good, One Bad",
             "Show two strong examples and one counter-example - beats paragraphs of adjectives every time.",
             "Three example cards good/good/bad, cream grid."),
            ("Format Contracts",
             "State the exact output shape: headings, length, table columns. Ban invented stats and require UNKNOWN.",
             "Output schema card with sections and limits."),
            ("Ask For Thinking",
             "On hard tasks, request step-by-step reasoning before the answer - or set adaptive thinking on the API.",
             "Reasoning steps then answer, toggle adaptive."),
            ("Non-Goals Stop Drift",
             "List what the output must NOT include - the fastest fix for scope creep.",
             "Non-goals checklist with crossed items, coral."),
            ("Project Instructions = System Prompt",
             "Put persona, rules and format in Project instructions once - every chat inherits it.",
             "Instruction block feeding many chats, badge."),
            ("Comment AI",
             "Want the structured Claude prompt templates? Comment AI.",
             "CTA editorial, Claude logo corner."),
        ],
    ),
    C(
        "CLAUDE.md Mastery", "30_Claude_md_Mastery",
        "CLAUDE.md is the only context that survives /compact - the highest-leverage file in any Claude Code repo.",
        [
            ("One File Controls Every Claude Session. Most Repos Don't Have It.",
             "CLAUDE.md loads every session and survives /compact. It is the single highest-leverage thing you can add.",
             "COVER: surreal control tower overseeing a city of code at dawn, single glowing document beam, floating Claude logo card right, faded 'CLAUDE.md' watermark bottom. Headline: 'No memory? Cold start.' 'CLAUDE.md fixes it.' Underline 'fixes'."),
            ("What To Put In It",
             "Stack, exact test/lint/build commands, architecture in one paragraph, and a hard NEVER list.",
             "CLAUDE.md sections labeled, coral tabs, Claude badge top-right."),
            ("Keep It Under 500 Lines",
             "Short root file plus linked docs in .claude/rules/ - load only what the task needs.",
             "Root file linking scoped rule files, cream grid."),
            ("It Survives /compact",
             "Conversation gets summarized; CLAUDE.md does not. That is why cold starts disappear.",
             "Context wiped but CLAUDE.md persists, anchor icon."),
            ("Conditional Loading",
             "'Before editing auth, read docs/auth-flow.md' - fetch deep context only when relevant.",
             "Trigger line pulling a doc on demand, coral arrow."),
            ("Output Styles",
             "Switch /output-style to Explanatory or Learning, or write a custom style to enforce format.",
             "Output style selector with custom file."),
            ("Memory You Teach Once",
             "'Remember our API uses snake_case JSON' - Claude writes it to memory and stops asking.",
             "Memory note saved, recurring convention chip."),
            ("Comment AI",
             "Want a battle-tested CLAUDE.md template? Comment AI.",
             "CTA editorial, Claude logo corner, terminal aesthetic."),
        ],
    ),
]


def slugify(text: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "_", text.strip()).strip("_")[:60]


def build_prompt(carousel: dict, idx: int, slide: tuple[str, str, str]) -> str:
    headline, body, visual = slide
    style = f"{BASE_STYLE}\n{COVER_HOOK}" if idx == 1 else f"{BASE_STYLE}\n{INTERIOR_STYLE}"
    return f"""
3:4 vertical Instagram carousel slide (portrait).
{style}

Topic: {carousel['title']}
Angle: {carousel['angle']}

HEADLINE (render exactly, large bold): {headline}
SUPPORTING TEXT (smaller, readable): {body}
Footer: @piyush.glitch  (NO page number, NO slide counter)

VISUAL DIRECTION (follow closely):
{visual}

Reminder: absolutely no numbers, page counts, or 'x/8' indicators anywhere on the image.
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
        req = urllib.request.Request(item["url"], headers={"User-Agent": "batch4/1.0"})
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
        except Exception:  # noqa: BLE001
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
    only = [a for a in sys.argv[1:] if a.isdigit()]
    carousels = CAROUSELS
    if only:
        carousels = [c for c in CAROUSELS if c["slug"][:2] in only]
    jobs = [(c, i, s) for c in carousels for i, s in enumerate(c["slides"], 1)]
    for c in carousels:
        (ROOT / c["slug"]).mkdir(parents=True, exist_ok=True)
    print(f"Generating {len(jobs)} slides ({len(carousels)} carousels, batch 21-30)", flush=True)
    print("After images: ./.venv/bin/python build_pdfs.py", flush=True)
    fails, done = [], 0
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
