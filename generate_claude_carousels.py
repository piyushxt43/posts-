#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 5 Claude-focused AI Business carousels (11-15) with Claude logo on cover."""

from __future__ import annotations

import base64
import concurrent.futures
import json
import os
import re
import sys
import textwrap
import time
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent / "AI_Business_Carousels"
API_URL = "https://api.apiyi.com/v1/images/generations"
MODEL = "gpt-image-2-all"
MAX_WORKERS = int(os.environ.get("CAROUSEL_WORKERS", "40"))
TIMEOUT = 300

STYLE = """
Create a premium Instagram carousel slide in modern editorial AI-business style.
3:4 vertical portrait first.
Cream grid paper OR blue-sky editorial background, huge confident typography, coral/red highlight tabs,
bold black sans-serif plus one italic serif accent word, footer @piyush.glitch bottom-left, page number bottom-right.
Readable, sharp, correctly spelled. No lorem ipsum, no watermarks, no clutter.
"""

CLAUDE_LOGO_COVER = """
COVER SLIDE ONLY - must include the official Anthropic Claude brand logo prominently:
terracotta/coral-orange rounded square icon with white sparkle/star mark inside (the recognizable Claude app logo),
placed top-left or top-center near headline - clean, accurate, not distorted. Also show wordmark CLAUDE in elegant sans nearby.
Brand colors: warm terracotta #D97757 accent on cover. This is a Claude-by-Anthropic carousel.
"""

CAROUSELS: list[dict[str, Any]] = [
    {
        "title": "Claude Projects For Teams",
        "slug": "11_Claude_Projects_For_Teams",
        "angle": "Claude Projects turn scattered chats into shared business brains with files, instructions and team context.",
        "pdf_title": "Claude Projects: Shared Context For Business Teams",
        "slides": [
            ("Stop Re-Explaining Your Business", "Claude Projects bundle files, custom instructions and chat history so every teammate starts smart.", "Cover with Claude logo terracotta icon, editorial portrait, giant white headline on blue sky."),
            ("What A Project Is", "A persistent workspace: upload PDFs, SOPs, brand guides, spreadsheets. Claude reads them every session.", "Cream grid, project folder UI card with file chips."),
            ("Custom Instructions", "Set tone, format, banned phrases, approval rules once - not in every prompt.", "Instruction panel mockup with coral tab."),
            ("Shared Team Access", "Marketing, ops and founders use the same source of truth instead of duplicate chats.", "Team avatars orbiting one Claude Project card."),
            ("Use Case Stack", "Campaign briefs, board prep, support macros, hiring scorecards, product specs.", "Five stacked workflow cards."),
            ("Project vs Plain Chat", "Chat forgets. Projects remember files, rules and prior decisions.", "Before/after two-column comparison."),
            ("Setup In 10 Minutes", "Create project, upload 5 key docs, write instructions, invite team, pin starter prompts.", "Numbered checklist on cream grid."),
            ("Comment AI", "Want the Claude Projects setup checklist? Comment AI and get the guide.", "Clean CTA slide coral button."),
        ],
        "pdf_sections": [
            ("Why Projects beat chat", "Every business re-explains context daily. Projects store the docs and rules once so Claude answers like an onboarded teammate."),
            ("What to upload first", "Brand voice guide, top 10 FAQs, pricing sheet, last quarter report, and one exemplar deliverable you want cloned."),
        ],
    },
    {
        "title": "Claude Artifacts For Business",
        "slug": "12_Claude_Artifacts_For_Business",
        "angle": "Artifacts let Claude ship live documents, dashboards, mini-apps and decks beside the chat - not just paragraphs.",
        "pdf_title": "Claude Artifacts: From Chat To Deliverables",
        "slides": [
            ("Claude Can Ship Artifacts", "Not just answers - live docs, calculators, landing pages, charts and code your team can use immediately.", "Cover Claude logo, artifact window floating beside chat UI."),
            ("Live Documents", "Rewrite policies, proposals and SOPs in a side panel you edit and export.", "Split chat plus document artifact mockup."),
            ("Mini Apps", "Build ROI calculators, pricing tables and internal tools without a sprint.", "Simple app artifact with coral CTA."),
            ("Data Visuals", "Paste CSV, get charts and narrative analysis in one artifact.", "Chart artifact card on cream grid."),
            ("Iterate Fast", "Ask for v2, v3 in plain English - artifact updates in place.", "Version tabs v1 v2 v3."),
            ("Share With Stakeholders", "Send artifact link or export PDF - no dev deploy needed.", "Share button and export icons."),
            ("Business Use Cases", "Board decks, campaign landing pages, onboarding portals, competitive battlecards.", "Four use-case tiles."),
            ("Comment AI", "Want 20 artifact prompts for operators? Comment AI for the playbook.", "CTA cover with Claude logo small corner."),
        ],
        "pdf_sections": [
            ("What artifacts are", "Side-panel outputs Claude generates alongside chat - documents, code, React components, SVG, HTML you refine iteratively."),
            ("Operator prompts", "Ask for an artifact explicitly: build a one-page ROI calculator, draft a policy doc, create a chart from this CSV."),
        ],
    },
    {
        "title": "Claude MCP Connectors",
        "slug": "13_Claude_MCP_For_Operators",
        "angle": "MCP gives Claude live hands into GitHub, Slack, Notion, Postgres and internal APIs through one connector layer.",
        "pdf_title": "Claude MCP: Live Tools For Business Ops",
        "slides": [
            ("Claude Gets Live Hands", "MCP connectors let Claude read and act across your stack - not copy-paste from tabs.", "Cover Claude logo, hub-and-spoke connector diagram."),
            ("What MCP Is", "Model Context Protocol - USB-C for AI tools. One standard, many apps.", "Simple hub diagram coral center burst."),
            ("Read Actions", "Pull open PRs, query CRM, fetch Notion pages, read support tickets.", "Read-only tool cards with checkmarks."),
            ("Write Actions", "Post Slack updates, create issues, draft emails - with approval gates.", "Write tools behind approval gate icon."),
            ("Starter Connectors", "GitHub, Google Drive, Slack, Postgres, Linear, Figma.", "Six app logo tiles stylized not trademark exact."),
            ("Security Pattern", "Scope tokens, read-only first, log every action, human approve writes.", "Shield checklist on cream grid."),
            ("Ops Workflow", "Morning digest agent: pull metrics, summarize blockers, post to channel.", "Workflow timeline three steps."),
            ("Comment AI", "Want our Claude MCP connector map? Comment AI and get the list.", "CTA slide."),
        ],
        "pdf_sections": [
            ("Why MCP matters", "Without connectors Claude guesses from stale exports. With MCP it pulls live truth and acts where you allow."),
            ("Rollout order", "Start read-only on one system, add logging, then enable writes with approval for one high-value workflow."),
        ],
    },
    {
        "title": "Claude Sonnet vs Opus",
        "slug": "14_Claude_Sonnet_vs_Opus",
        "angle": "Smart teams route fast Sonnet work to volume tasks and reserve Opus for high-stakes reasoning.",
        "pdf_title": "Claude Model Routing: Sonnet vs Opus",
        "slides": [
            ("Route Claude Like A Pro", "Sonnet for speed and volume. Opus for judgment calls. Wrong routing burns budget and time.", "Cover Claude logo, split Sonnet vs Opus typography."),
            ("Claude Sonnet", "Drafts, summaries, rewrites, data cleanup, first-pass research, bulk ops.", "Sonnet card - fast lightning icon coral."),
            ("Claude Opus", "Strategy, architecture, negotiation prep, complex analysis, high-stakes writing.", "Opus card - depth brain icon."),
            ("Cost vs Quality", "Sonnet keeps COGS down. Opus protects revenue on decisions that matter.", "Simple two-axis chart cream grid."),
            ("Team Routing Table", "Support macros Sonnet. Board memo Opus. Code review Sonnet first Opus on risk.", "Routing table UI."),
            ("When To Escalate", "If Sonnet output needs 3+ fixes, escalate to Opus with the thread attached.", "Escalation arrow diagram."),
            ("Measure It", "Track edit rate, time-to-ship and rework by model - tune routing monthly.", "Metrics dashboard mockup."),
            ("Comment AI", "Want our Claude routing cheat sheet? Comment AI.", "CTA slide Claude logo accent."),
        ],
        "pdf_sections": [
            ("Default rule", "Sonnet unless the task needs multi-step judgment, legal/finance precision, or executive-facing quality on first draft."),
            ("Escalation triggers", "Novel strategy, conflicting constraints, high blast radius, or repeated Sonnet failures on same template."),
        ],
    },
    {
        "title": "Claude For Research",
        "slug": "15_Claude_For_Research_And_Writing",
        "angle": "Claude excels at long-form research synthesis, executive writing and evidence-backed briefs when you structure the prompt.",
        "pdf_title": "Claude Research and Writing Workflows",
        "slides": [
            ("Claude Writes And Researches", "Turn raw notes, links and PDFs into exec briefs, memos and content systems - with citations discipline.", "Cover Claude logo, editorial writer desk blue sky."),
            ("Research Stack", "Gather sources, extract claims, cross-check conflicts, synthesize one narrative.", "Four-step research pipeline cards."),
            ("Long Context Edge", "Drop in reports, transcripts, decks - Claude holds the thread.", "Stack of document icons feeding Claude."),
            ("Writing Modes", "Brief, memo, thread, landing copy, talk track - each with format rules in Project instructions.", "Format mode pills."),
            ("Citation Hygiene", "Ask for claim/source pairs, flag weak evidence, separate fact from inference.", "Citation table mockup coral highlights."),
            ("Content Ops Loop", "Research once, repurpose to email, LinkedIn, deck, FAQ via artifact exports.", "Repurpose hub diagram."),
            ("Quality Gate", "Human editor checks numbers, names, dates - Claude does 80% draft.", "Editor checklist green coral."),
            ("Comment AI", "Want 15 Claude research prompts? Comment AI for the pack.", "CTA closing slide."),
        ],
        "pdf_sections": [
            ("Research prompt pattern", "Role, sources provided, output format, citation rules, unknowns to flag, audience and decision to support."),
            ("Writing guardrails", "Ban invented stats, require labeled assumptions, keep executive summary under 200 words."),
        ],
    },
]


def slugify(text: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "_", text.strip()).strip("_")[:60]


def build_prompt(carousel: dict, slide_index: int, slide: tuple[str, str, str]) -> str:
    headline, body, visual = slide
    page = f"{slide_index}/8"
    cover = CLAUDE_LOGO_COVER if slide_index == 1 else "Interior educational slide - clear structure, cream grid or editorial as fits."
    return f"""
3:4 vertical Instagram carousel slide.
{STYLE}
{cover}

Topic: {carousel['title']}
Angle: {carousel['angle']}
Slide: {page}

Headline: {headline}
Body: {body}
Label top: AI FOR BUSINESS - {slide_index:02d}
Footer: @piyush.glitch | {page}

Visual: {visual}
Main headline dominates. Coral highlight tab. Claude terracotta accent on cover only.
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
        req = urllib.request.Request(item["url"], headers={"User-Agent": "claude-carousel/1.0"})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            path.write_bytes(r.read())
        return
    b64 = item.get("b64_json", "")
    if "," in b64:
        b64 = b64.split(",", 1)[1]
    path.write_bytes(base64.b64decode(b64))


def write_pdf(path: Path, title: str, carousel: dict) -> None:
    width, height = 612, 792
    margin, lh = 54, 14
    lines: list[tuple[int, str]] = []
    y = height - margin

    def add(size: int, text: str = "") -> None:
        nonlocal y
        if not text:
            y -= lh
            return
        for part in textwrap.wrap(text, width=max(45, int(95 - size * 2.2))):
            if y < margin + 40:
                lines.append((-1, "PB"))
                y = height - margin
            lines.append((size, part))
            y -= lh + (size - 10) * 0.7

    add(22, title)
    add(11, carousel["angle"])
    for h, b in carousel["pdf_sections"]:
        add(16, h)
        add(11, b)
    pages: list[list[tuple[int, str]]] = [[]]
    for item in lines:
        if item == (-1, "PB"):
            pages.append([])
        else:
            pages[-1].append(item)

    objects = ["<< /Type /Catalog /Pages 2 0 R >>"]
    kids = " ".join(f"{3+i*2} 0 R" for i in range(len(pages)))
    objects.append(f"<< /Type /Pages /Kids [{kids}] /Count {len(pages)} >>")
    for i, pl in enumerate(pages):
        pn, cn = 3 + i * 2, 4 + i * 2
        objects.append(f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {width} {height}] /Resources << /Font << /F1 << /Type /Font /Subtype /Type1 /BaseFont /Helvetica >> /F2 << /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >> >> >> /Contents {cn} 0 R >>")
        stream = ["BT"]
        yp = height - margin
        for fs, tx in pl:
            f = "F2" if fs >= 16 else "F1"
            tx = tx.encode("latin-1", "replace").decode().replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
            stream.append(f"/{f} {fs} Tf {margin} {yp:.1f} Td ({tx}) Tj {-margin} {-lh-(fs-10)*0.7:.1f} Td")
            yp -= lh + (fs - 10) * 0.7
        stream.append("ET")
        s = "\n".join(stream)
        objects.append(f"<< /Length {len(s.encode('latin-1'))} >>\nstream\n{s}\nendstream")

    pdf = ["%PDF-1.4\n"]
    off = [0]
    for i, o in enumerate(objects, 1):
        off.append(sum(len(p.encode("latin-1")) for p in pdf))
        pdf.append(f"{i} 0 obj\n{o}\nendobj\n")
    xs = sum(len(p.encode("latin-1")) for p in pdf)
    pdf.append(f"xref\n0 {len(objects)+1}\n0000000000 65535 f \n")
    pdf += [f"{o:010d} 00000 n \n" for o in off[1:]]
    pdf.append(f"trailer\n<< /Size {len(objects)+1} /Root 1 0 R >>\nstartxref\n{xs}\n%%EOF\n")
    path.write_bytes("".join(pdf).encode("latin-1"))


def job(api_key: str, carousel: dict, idx: int, slide: tuple, force: bool) -> str:
    folder = ROOT / carousel["slug"]
    folder.mkdir(parents=True, exist_ok=True)
    name = f"{idx:02d}_{slugify(slide[0])}.png"
    out = folder / name
    if not force and out.exists() and out.stat().st_size > 100_000:
        return "skipped"
    for attempt in range(3):
        try:
            save_image(post_json(API_URL, {"model": MODEL, "prompt": build_prompt(carousel, idx, slide), "response_format": "url"}, api_key), out)
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
    # Rich PDFs: run ./.venv/bin/python build_pdfs.py after slides are generated.
    print(f"Generating {len(jobs)} slides ({len(CAROUSELS)} Claude carousels)", flush=True)
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
