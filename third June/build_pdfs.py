#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build 5-6 page deep-knowledge PDFs for Third June carousels."""

from __future__ import annotations

from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, PageBreak,
)

from content import CAROUSELS
from pdf_beauty_guides import BEAUTY_PDF_PAGES
from pdf_beauty_rich import BEAUTY_SLUGS, build_beauty_pdf

ROOT = Path(__file__).resolve().parent
CREAM = HexColor("#F4EEDE")
INK = HexColor("#1B1A17")
CORAL = HexColor("#EF5E45")
GREY = HexColor("#6E6657")
MARGIN = 0.72 * inch


def _styles():
    ss = getSampleStyleSheet()
    return {
        "kicker": ParagraphStyle("k", parent=ss["Normal"], fontName="Helvetica-Bold", fontSize=10,
                                 textColor=CORAL, spaceAfter=6),
        "h1": ParagraphStyle("h1", parent=ss["Title"], fontName="Helvetica-Bold", fontSize=26,
                             textColor=INK, leading=30, spaceAfter=10),
        "h2": ParagraphStyle("h2", parent=ss["Heading2"], fontName="Helvetica-Bold", fontSize=14,
                             textColor=INK, leading=18, spaceBefore=14, spaceAfter=6),
        "body": ParagraphStyle("b", parent=ss["Normal"], fontSize=10.5, leading=15, textColor=INK, spaceAfter=6),
        "mono": ParagraphStyle("m", parent=ss["Normal"], fontName="Courier", fontSize=8.5, leading=12,
                               textColor=INK, backColor=HexColor("#EDE8DC"), borderPadding=8, spaceAfter=10),
    }


def _bg(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(CREAM)
    canvas.rect(0, 0, letter[0], letter[1], fill=1, stroke=0)
    canvas.setFillColor(CORAL)
    canvas.rect(0, letter[1] - 6, letter[0], 6, fill=1, stroke=0)
    canvas.setFillColor(GREY)
    canvas.setFont("Helvetica", 8)
    canvas.drawString(MARGIN, 0.5 * inch, "@piyush.glitch")
    canvas.drawRightString(letter[0] - MARGIN, 0.5 * inch, f"page {doc.page}")
    canvas.restoreState()


PDF_PAGES = {
    "01_Claude_Skills_Slash_Commands": [
        ("Overview", "Anthropic shipped 31 pre-built Claude Skills for small businesses in 2025, with connectors for QuickBooks, Stripe, HubSpot, Gmail, Google Calendar, Square, Canva, Slack, Microsoft 365, Block, PayPal, and Google Drive. Skills are folders with a SKILL.md file - not MCP servers, not tools. They define workflow: what to do, in what order, with what guardrails."),
        ("Top slash commands to run this week", "<b>/business-pulse</b> - QuickBooks + Stripe + HubSpot into a 90-second dashboard: cash, revenue, pipeline, 3 to-dos.<br/><b>/invoice-chase</b> - scans overdue invoices, drafts tone-matched reminders. Most SMBs recover $2K-$10K on day one.<br/><b>/lead-triage</b> - scores HubSpot leads by fit and engagement, drafts follow-ups.<br/><b>/monday-brief</b> - one page: cash, sales, pipeline, owners.<br/><b>/contract-review</b> - red flags in plain English before you sign."),
        ("SKILL.md template", """<pre>
---
name: invoice-chase
description: Scan overdue invoices and draft reminders. Use when user mentions AR or collections.
---

## Steps
1. Pull open invoices via QuickBooks connector
2. Match tone to client history
3. Draft reminder - never send, flag [REVIEW]
4. Queue subject line variants
</pre>Install at ~/.claude/skills/invoice-chase/SKILL.md"""),
        ("GitHub repos", "<b>github.com/anthropics/skills</b> - official Anthropic skill examples and format spec.<br/><b>github.com/ComposioHQ/awesome-claude-skills</b> - 78 SaaS workflow skills via Composio Rube MCP.<br/><b>github.com/MichaelGong/mcp-to-skills</b> - discovers MCP servers in Claude Code and writes SKILL.md per server.<br/><b>github.com/CyPack/ai-tooling-sync</b> - syncs MCP, skills, rules across Claude Code, Codex, OpenCode, Cursor."),
        ("Hidden CLI commands", "<b>/compact focus</b> - shrink context to current task only.<br/><b>/btw</b> - append side note without polluting main thread.<br/><b>/init</b> - regenerate CLAUDE.md from codebase scan.<br/><b>/effort high|medium|low</b> - control token spend per reply.<br/>In Claude Cowork: <b>/schedule</b> for timed runs (e.g. Monday brief at 6am)."),
        ("Setup checklist", "1. Enable connectors in Claude Settings. 2. Run /business-pulse once to verify data pull. 3. Copy SKILL.md template for your top 3 workflows. 4. Run mcp-to-skills sync if you use MCP. 5. Gate all sends with [REVIEW] in custom instructions. 6. Cancel redundant SaaS after 30-day trial."),
    ],
    "02_Claude_MCP_Connectors": [
        ("What MCP is", "Model Context Protocol (MCP) is the open standard for connecting AI agents to external tools - Postgres, GitHub, Slack, Notion, Google Drive, and custom APIs. MCP servers handle auth and tool discovery; Claude Code and Cursor act as MCP hosts. Skills define behavior; MCP defines access."),
        ("Install servers", """<pre>
claude mcp add github -- npx -y @modelcontextprotocol/server-github
claude mcp add postgres -- npx -y @modelcontextprotocol/server-postgres $DATABASE_URL
claude mcp add slack -- npx -y @modelcontextprotocol/server-slack
claude mcp list
</pre>Project-level: create .mcp.json in repo root. Global: ~/.claude.json under mcpServers."""),
        ("7-server ops stack", "1. <b>Postgres</b> - live metrics, read-only default. 2. <b>GitHub</b> - PRs, issues, CI. 3. <b>Slack</b> - read channels, draft posts. 4. <b>Notion</b> - SOPs and client docs. 5. <b>Google Drive</b> - deliverable handoff. 6. <b>Meta Ads MCP</b> - spend and ROAS. 7. <b>Internal REST</b> - your API via openapi-mcp generator."),
        ("Sync tools", "<b>zweiklang/mcp-sync</b> - bidirectional sync between Claude Code (~/.claude.json) and Codex CLI (~/.codex/config.toml). Commands: mcp-sync status, diff, claude-to-codex.<br/><b>CyPack/ai-tooling-sync</b> - syncs MCP + skills + rules + agents across Claude, Codex, OpenCode, Cursor in one pass."),
        ("Security pattern", "Read-first by default: allow SELECT on Postgres, read on GitHub/Slack. Block writes unless human approves. Add to CLAUDE.md: 'Never execute write MCP tools. Draft output. Tag [REVIEW].' Never commit tokens - use env vars and .env.local in .gitignore."),
        ("Troubleshooting", "Server won't connect: run claude mcp list and check npx path. Auth errors: verify env vars in mcpServers entry. Duplicate configs: run mcp-sync diff. Cursor out of sync: copy .mcp.json from Claude project or run ai-tooling-sync."),
    ],
    "03_GPT_Custom_GPTs_API": [
        ("Custom GPT architecture", "Custom GPTs = Instructions + Knowledge files + Capabilities (web, DALL-E, code) + optional Actions (OpenAPI). Instructions should define ROLE, CONTEXT, RULES, OUTPUT FORMAT - not a vague persona. Upload pricing PDFs, SOPs, FAQs to Knowledge. Test in Preview before Publish."),
        ("GPT-4o image API", """<pre>
POST https://api.openai.com/v1/images/generations
{
  "model": "gpt-image-1",
  "prompt": "[detailed 2-paragraph prompt]",
  "size": "1024x1536",
  "quality": "high"
}
</pre>1024x1536 = 3:4 Instagram portrait. Store url or b64_json from response."""),
        ("Chat vs Assistants", "<b>Chat Completions</b> - stateless, fast, cheap. Use for one-shot tasks, classification, rewrites. Model: gpt-4o-mini for volume.<br/><b>Assistants API</b> - threads, file search, code interpreter. Use when you need persistent memory, vector store knowledge, or multi-step tool use across sessions."),
        ("Stored prompts preset", "Create prompts in OpenAI Dashboard > Prompts. Reference by ID in API calls for version-controlled system behavior without redeploying your app. Share preset ID across team for consistent outputs."),
        ("GPT Actions", "Import OpenAPI 3.0 schema in GPT Builder > Actions. Define operationId per endpoint. Set API Key auth header. GPT can call your CRM, calendar, or internal API. Test in Preview. Never expose write endpoints without confirmation step in your API."),
        ("OpenAI cookbook", "Bookmark github.com/openai/openai-cookbook for RAG, agents, structured outputs, function calling, and batch API patterns. Official Python SDK: github.com/openai/openai-python."),
    ],
    "04_Gemini_Gems_Workspace": [
        ("What Gems are", "Gemini Gems are persistent custom assistants in Google AI Studio - Google's equivalent of Custom GPTs. Each Gem has system instructions, optional Knowledge files, and capability toggles (Google Search, Workspace extensions). Share Gem links with your team for consistent behavior."),
        ("Create a business Gem", "Go to aistudio.google.com > Create Gem. Paste system instructions: role, output format, [REVIEW] gate for sends, Drive search behavior. Upload Knowledge: pricing sheets, SOPs, CSV exports. Enable Google Search for market research tasks."),
        ("Workspace integration", "Admin enables Gemini for Workspace. Connect Gmail, Drive, Docs, Sheets, Calendar. Gem can read inbox threads, summarize Docs, draft replies, analyze Sheet data. Default: draft only, no auto-send. Best for operators already in Google stack."),
        ("API preset", """<pre>
POST .../models/gemini-2.0-flash:generateContent
{
  "systemInstruction": {"parts":[{"text":"You are..."}]},
  "contents": [{"role":"user","parts":[{"text":"..."}]}],
  "tools": [{"googleSearch": {}}],
  "generationConfig": {"temperature": 0.4}
}
</pre>Add googleSearch tool for grounded answers with citations."""),
        ("Gemini vs GPT vs Claude", "<b>Gemini wins:</b> native Workspace, Google Search grounding, generous free tier.<br/><b>GPT wins:</b> Custom GPT marketplace, mature image API, plugin ecosystem.<br/><b>Claude wins:</b> code/agents, MCP, Claude Code, long-context projects.<br/>Operator stack: use all three for what each does best."),
        ("Hidden tips", "1. Upload CSV to Knowledge - ask pivot questions in plain English. 2. Force Drive retrieval with explicit doc names in prompt. 3. Export Gem instructions to API systemInstruction for production. 4. Combine with Apps Script for Sheet-triggered workflows."),
    ],
    "05_Cursor_Agent_Secrets": [
        ("Cursor as agent runtime", "Cursor is not just autocomplete. With .cursor/rules, MCP servers, Composer agent mode, and background agents, it is a full agent runtime for shipping code. Configure it like an operator: rules for standards, MCP for external tools, Composer for multi-file edits."),
        (".cursor/rules", """<pre>
# .cursor/rules/project.mdc
---
description: Project standards
globs: ["**/*.ts", "**/*.tsx"]
alwaysApply: true
---
- Match existing patterns in src/
- Never commit .env or secrets
- Run tests before merge suggestions
</pre>Rules auto-apply when matching files are open."""),
        ("MCP in Cursor", "Create .cursor/mcp.json with same structure as Claude .mcp.json. Enable in Cursor Settings > MCP. Agent in Composer can call GitHub, Postgres, etc. Use ai-tooling-sync to keep Cursor and Claude Code configs identical."),
        (".cursorignore", "Add .env, credentials, node_modules, dist, .git to .cursorignore (same syntax as .gitignore). Prevents agent from reading secrets into context. Pair with rule: never print environment variables."),
        ("Composer workflow", "Cmd+I opens Composer. Use @codebase for full repo, @docs for library docs. Agent mode runs multi-file edits autonomously - review diff per file before accept. Pattern: ask for plan first, then implement in same session."),
        ("Repos and background agents", "<b>PatrickJS/awesome-cursorrules</b>, <b>cursor.directory</b>, <b>getcursor/cursor</b>. Enable Background Agents in Beta settings for cloud sandbox runs on long tasks. Always review diff before merge - agent is not autopilot."),
    ],
}

PDF_PAGES.update(BEAUTY_PDF_PAGES)


def build_one(carousel: dict) -> Path:
    if carousel["slug"] in BEAUTY_SLUGS:
        return build_beauty_pdf(carousel)

    st = _styles()
    folder = ROOT / carousel["slug"]
    folder.mkdir(parents=True, exist_ok=True)
    out = folder / carousel["pdf_name"]
    pages = PDF_PAGES[carousel["slug"]]

    doc = BaseDocTemplate(str(out), pagesize=letter, leftMargin=MARGIN, rightMargin=MARGIN,
                          topMargin=MARGIN, bottomMargin=MARGIN)
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=_bg)])

    flow = []
    flow.append(Paragraph("PIYUSH.GLITCH  /  DEEP GUIDE", st["kicker"]))
    flow.append(Paragraph(carousel["slug"].replace("_", " "), st["h1"]))
    flow.append(Paragraph("Companion PDF for the Instagram carousel. Save and implement - not generic advice.", st["body"]))
    flow.append(Spacer(1, 12))

    for title, body in pages:
        flow.append(Paragraph(title, st["h2"]))
        if body.strip().startswith("<"):
            flow.append(Paragraph(body, st["body"]))
        elif "<pre>" in body:
            flow.append(Paragraph(body.replace("<pre>", "").replace("</pre>", ""), st["mono"]))
        else:
            flow.append(Paragraph(body, st["body"]))
        flow.append(Spacer(1, 8))
        if title != pages[-1][0]:
            flow.append(PageBreak())

    doc.build(flow)
    return out


def main() -> int:
    import sys
    only_beauty = "--beauty" in sys.argv
    for c in CAROUSELS:
        if only_beauty and c["slug"] not in BEAUTY_SLUGS:
            continue
        out = build_one(c)
        size = out.stat().st_size
        print(f"OK {out} ({size:,} bytes)", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
