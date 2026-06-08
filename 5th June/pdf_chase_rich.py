# -*- coding: utf-8 -*-
"""Dense Chase-style PDFs: guide pages + embedded carousel images."""

from __future__ import annotations

import re
from pathlib import Path

from reportlab.lib.units import inch

from pdf_builder_rich import build_pdf

ROOT = Path(__file__).resolve().parent

SKIP = (
    "3:4 vertical", "Chase H AI", "Perfect spelling", "Graphic editorial",
    "Premium Instagram", "header JUN", "NOT beauty",
)


def _clean_prompt(raw: str) -> str:
    lines = []
    for line in raw.replace("\r", "").split("\n"):
        s = line.strip()
        if not s:
            continue
        if any(s.startswith(p) for p in SKIP):
            continue
        lines.append(s)
    text = "\n".join(lines).strip()
    return text[:1800] + "..." if len(text) > 1800 else text


def _title(filename: str) -> str:
    base = filename.replace(".png", "").replace("_", " ")
    return base[3:].title() if len(base) > 3 else base.title()


DEEP = {
    "01_Claude_Small_Business_Cowork": {
        "title": "Claude for Small Business (Cowork)",
        "cta": "COWORK",
        "tagline": "Connectors + 15 workflows + approve-before-send",
        "overview": (
            "Anthropic's Claude for Small Business packages Cowork (shared ops workspace), OAuth connectors "
            "(QuickBooks, PayPal, HubSpot, Canva, Gmail, Slack), and 15 ready workflows for finance, sales, "
            "and HR. This is not generic chat - it is staged automation where every external write pauses at "
            "<b>[REVIEW]</b> until a human approves."
        ),
        "workflow": [
            "Enable Claude for Small Business on team plan",
            "OAuth connect QuickBooks + HubSpot (read-first week)",
            "Activate Finance / Invoice chase workflow",
            "Set [REVIEW] gate on all send/pay/post actions",
            "Dry-run Monday brief before live connectors",
        ],
        "table": ["Workflow", "Trigger", "Output"],
        "rows": [
            ["Invoice chase", "Monday 9am", "QB pull + 3 draft emails"],
            ["Pipeline nudge", "Stale 14d deals", "HubSpot drafts"],
            ["Onboarding pack", "New hire event", "Canva deck + calendar"],
            ["Monday brief", "Weekly", "One-page exec summary"],
        ],
        "code": (
            "## Cowork safety block (paste in team instructions)\n"
            "Never send email, post to social, or initiate payment without explicit APPROVE.\n"
            "All drafts end with [REVIEW] + diff summary + risk tag (low/med/high).\n"
            "Week 1: read-only connector scopes only."
        ),
        "failures": [
            ["Auto-sent email", "Enable [REVIEW] gate; disable write scopes"],
            ["Wrong client tone", "Add tone examples to workflow skill"],
            ["Connector auth expired", "Re-OAuth; keep read-only until proof prompt passes"],
            ["Duplicate invoices chased", "Dedupe by invoice_id in workflow step 1"],
        ],
        "insights": {
            "01_Landing_Cover.png": "Cover sells ops desk positioning - connectors + workflows in subline.",
            "02_What_Is_Cowork.png": "Define Cowork vs chat - multi-step + approve is the differentiator.",
            "03_Connector_Map.png": "Show six connectors - reduces tab-hopping objection.",
            "04_Workflow_Finance.png": "Invoice chase is highest ROI workflow for SMB - lead with money.",
            "05_Workflow_Sales_HR.png": "Two workflows one slide - density without overwhelm.",
            "06_Approve_Before_Send.png": "Trust slide - [REVIEW] diff view is the product.",
            "07_15_Workflows_Setup.png": "Checklist slide drives PDF comment COWORK.",
            "08_CTA.png": "Recap six concepts + PDF filename on taped card.",
        },
    },
    "02_Skills_MCP_Two_Layer_Stack": {
        "title": "Skills + MCP Two-Layer Stack",
        "cta": "STACK",
        "tagline": "USB access vs playbook procedure",
        "overview": (
            "MCP (Model Context Protocol) standardizes <b>access</b> to tools and data. Agent Skills (SKILL.md) "
            "standardize <b>procedure</b> - tone, steps, guardrails. Confusion ends when you stack them: "
            "MCP connects, Skills instruct. agentskills.io is the open standard adopted across Claude, Cursor, Codex."
        ),
        "workflow": [
            "Pick one job (invoice chase, UI audit, Monday brief)",
            "Install MCP servers for data access only",
            "Add matching Skill folder with SKILL.md",
            "Test read-only proof prompt per server",
            "Add [REVIEW] before any write tool",
        ],
        "table": ["Job", "MCP", "Skill"],
        "rows": [
            ["Invoice chase", "HubSpot", "collections-chase"],
            ["UI audit", "filesystem + GitHub", "impeccable"],
            ["Monday brief", "GSC + GA4", "ops-brief"],
        ],
        "code": (
            "Mental model:\n"
            "  Layer 1 MCP  = USB (plug in GitHub, GSC, HubSpot)\n"
            "  Layer 2 Skill = Playbook (how to use USB well)\n"
            "Never put OAuth secrets inside SKILL.md - MCP handles auth."
        ),
        "failures": [
            ["Skill without MCP", "Agent hallucinates data - add MCP read first"],
            ["MCP without Skill", "Inconsistent outputs - add SKILL.md procedure"],
            ["Duplicate logic in CLAUDE.md and Skill", "Move procedure to Skill only"],
        ],
        "insights": {
            "01_Landing_Cover.png": "USB vs playbook visual on bust split - memorable metaphor.",
            "02_USB_Vs_Playbook.png": "Diagram slide - most saved slide in deck.",
            "03_MCP_Layer.png": "Registry repo card lends credibility.",
            "04_Skills_Layer.png": "Progressive disclosure is key teaching point.",
            "05_Workflow_Invoice.png": "First concrete job recipe.",
            "06_Workflow_UI_Audit.png": "Dev audience hook - impeccable + MCP.",
            "07_Workflow_Monday_Brief.png": "Ops audience hook - GSC + GA4.",
            "08_CTA.png": "Comment STACK for diagram PDF.",
        },
    },
    "03_Agent_Skills_Write_Once": {
        "title": "Agent Skills: Write Once, Run Everywhere",
        "cta": "SKILLS",
        "tagline": "SKILL.md portable standard",
        "overview": (
            "Maintain one SKILL.md per workflow instead of duplicating across .cursor/rules, CLAUDE.md, Codex "
            "instructions, and Gemini GEMs. Agent Skills uses YAML frontmatter + markdown body + optional "
            "scripts/ and references/. Tools load summary first, full skill on demand."
        ),
        "workflow": [
            "Audit top 3 repeated workflows across tools",
            "Write SKILL.md with frontmatter name + description",
            "Add references/ for tone and policy docs",
            "Install path per tool (Claude, Cursor, Codex, Gemini CLI)",
            "Delete duplicated rules after 7-day parity test",
        ],
        "table": ["Template", "Use when"],
        "rows": [
            ["pr-review", "Every PR before merge"],
            ["invoice-draft", "Finance ops drafts"],
            ["caption-qa", "UGC / Meta caption batches"],
        ],
        "code": (
            "---\n"
            "name: pr-review\n"
            "description: Review PR diffs for tests, security, breaking changes.\n"
            "---\n\n"
            "## When to use\n"
            "User mentions PR, merge request, or code review.\n\n"
            "## Steps\n"
            "1. Summarize diff scope\n"
            "2. Check tests + breaking changes\n"
            "3. Output structured review - never auto-merge"
        ),
        "failures": [
            ["Skill too long", "Split into references/ files"],
            ["Tool ignores skill", "Check install path + frontmatter description"],
            ["Drift across tools", "Single git repo for all skills"],
        ],
        "insights": {
            "01_Landing_Cover.png": "Write once run everywhere - gradient on middle phrase.",
            "02_The_Problem.png": "Four configs pain point - developers share this.",
            "03_SKILL_MD_Anatomy.png": "Code card must be legible - test mobile zoom.",
            "04_Where_It_Runs.png": "Four tool icons = portability proof.",
            "05_Skill_PR_Review.png": "First template - dev audience.",
            "06_Skill_Invoice_Draft.png": "Second template - SMB crossover.",
            "07_Skill_Caption_QA.png": "Third template - UGC crossover.",
            "08_CTA.png": "SKILLS keyword for PDF.",
        },
    },
    "04_Cursor_Cloud_Agents": {
        "title": "Cursor Cloud Agents",
        "cta": "CLOUD",
        "tagline": "Isolated VMs + merge-ready PRs",
        "overview": (
            "Cloud Agents (evolution of Background Agents) run in isolated cloud VMs with browser testing, "
            "parallel execution, and merge-ready PR output. Use local Composer for tight pairing; use Cloud "
            "when the task has clear acceptance criteria and can run unattended."
        ),
        "workflow": [
            "Write acceptance criteria in Linear/GitHub issue",
            "Add environment.json (Node, test cmd, start cmd)",
            "Set spend limit per agent run",
            "Require green CI + screenshots in PR template",
            "Human review before merge - agent never merges alone",
        ],
        "table": ["Use Cloud when", "Use Local when"],
        "rows": [
            ["Clear issue + tests", "Exploratory spike"],
            ["UI needs browser verify", "Architecture debate"],
            ["Parallel dependency bumps", "Pairing on hard bug"],
        ],
        "code": (
            "{\n"
            '  "snapshot": "POPULAR",\n'
            '  "install": "npm ci",\n'
            '  "start": "npm run dev",\n'
            '  "test": "npm test"\n'
            "}"
        ),
        "failures": [
            ["PR missing tests", "Add test command to environment.json"],
            ["Wrong Node version", "Pin snapshot in environment.json"],
            ["Agent scope creep", "Router issue - acceptance criteria only"],
        ],
        "insights": {
            "01_Landing_Cover.png": "Open PRs headline - dev share trigger.",
            "02_Cloud_Vs_Local.png": "Split diagram prevents misuse.",
            "03_Isolated_VM.png": "Clean environment story.",
            "04_Merge_Ready_PR.png": "Definition of done on mock PR card.",
            "05_Triggers.png": "Slack/Linear triggers = team adoption.",
            "06_Environment_JSON.png": "Copy-paste config slide.",
            "07_Spend_And_DOD.png": "Checklist reduces bad merges.",
            "08_CTA.png": "CLOUD keyword.",
        },
    },
    "05_OpenAI_Workspace_Agents": {
        "title": "OpenAI Workspace Agents",
        "cta": "AGENTS",
        "tagline": "Shared scheduled agents for Business teams",
        "overview": (
            "Workspace Agents replace solo Custom GPTs for team infrastructure: shared ownership, scheduled "
            "cloud runs, connectors (Slack, Salesforce, Google), and admin controls. Use when output goes to "
            "clients or runs on a cron. Keep personal GPTs for drafts only."
        ),
        "workflow": [
            "List workflows that are shared + recurring",
            "Create Workspace Agent with connector read-first",
            "Define output template (Slack, email draft, doc)",
            "Add human review step before external send",
            "Migrate Custom GPT when schedule + connectors needed",
        ],
        "table": ["Custom GPT", "Workspace Agent"],
        "rows": [
            ["Solo user", "Team shared"],
            ["Manual run", "Scheduled cloud"],
            ["No connectors", "Slack, SF, Google"],
            ["No audit", "Admin + Compliance API"],
        ],
        "code": (
            "Migration rule:\n"
            "IF output goes to client OR runs on schedule\n"
            "  THEN Workspace Agent + HITL\n"
            "ELSE keep Custom GPT for personal drafts"
        ),
        "failures": [
            ["Agent sent without review", "Enable review step in flow"],
            ["Stale connector data", "Re-auth; test proof prompt"],
            ["Team forked GPT versions", "Consolidate to one Workspace Agent"],
        ],
        "insights": {
            "01_Landing_Cover.png": "For teams subline targets Business buyers.",
            "02_Beyond_Custom_GPTs.png": "Comparison table slide.",
            "03_Shared_Scheduled.png": "Weekly report example concrete.",
            "04_Connectors.png": "Live data vs copy-paste.",
            "05_Human_In_Loop.png": "[REVIEW] on email mock.",
            "06_When_To_Migrate.png": "Decision flowchart.",
            "07_Build_First_Agent.png": "Five-step build list.",
            "08_CTA.png": "AGENTS keyword.",
        },
    },
    "06_Google_Workspace_Studio_Gems": {
        "title": "Google Workspace Studio + Gems",
        "cta": "STUDIO",
        "tagline": "No-code agentic flows with your Gems inside",
        "overview": (
            "Workspace Studio builds agentic flows across Gmail, Drive, Sheets without code. The 2026 "
            "<b>Ask a Gem</b> step places your trained Gem (brand voice, policy) inside the automation - "
            "not just the chat sidebar. Huge SMB segment already on Workspace."
        ),
        "workflow": [
            "Admin: enable Gemini for Workspace",
            "Create 2 Gems: brand voice + policy rubric",
            "Build urgent email triage flow (read-first)",
            "Add human approval before send step",
            "Expand to form-to-Sheet and meeting actions",
        ],
        "table": ["Flow", "Steps"],
        "rows": [
            ["Urgent triage", "Label -> Gem classify -> draft -> approve"],
            ["Form lead", "Submit -> Gem score -> Sheet -> Gmail draft"],
            ["Meeting actions", "Calendar end -> extract -> Sheet tab"],
            ["Attachment file", "Gmail attach -> Drive folder by client"],
        ],
        "code": (
            "Flow pattern:\n"
            "Trigger -> [Optional filter] -> Ask a Gem -> Action -> Human approve\n"
            "Never skip approve on external Gmail send."
        ),
        "failures": [
            ["Gemini not enabled", "Admin console prerequisite"],
            ["Gem wrong tone", "Retrain Gem with 10 gold examples"],
            ["Flow sent without approve", "Add explicit human step"],
        ],
        "insights": {
            "01_Landing_Cover.png": "Google gradient on Workspace Studio.",
            "02_Studio_Basics.png": "No-code positioning.",
            "03_Ask_A_Gem.png": "Key 2026 differentiator slide.",
            "04_Flow_Email_Triage.png": "First flow - universal pain.",
            "05_Flow_Form_Gem.png": "Lead gen angle.",
            "06_Flow_Meeting_Actions.png": "Two flows density.",
            "07_Admin_Prereqs.png": "Admin checklist prevents support DMs.",
            "08_CTA.png": "STUDIO keyword.",
        },
    },
    "07_Meta_UGC_Creative_OS": {
        "title": "Meta UGC Creative Operating System",
        "cta": "UGC",
        "tagline": "Creative-first Advantage+ at scale",
        "overview": (
            "Meta's auction is creative-first: roughly 70-80% of performance comes from assets, not audiences. "
            "Advantage+ Shopping Campaigns want 30-50+ variants refreshed every 2-3 weeks with hook-level "
            "testing. This OS covers hook bible, variant matrix, tagging, and AI volume + hero creators."
        ),
        "workflow": [
            "Build hook bible (6 patterns, 0-3s focus)",
            "Create variant matrix: hook x format x CTA",
            "Tag every asset: hook_type, format, angle, week_live",
            "Produce AI variants for long tail; 2-4 hero creators/quarter",
            "Kill losers weekly; refresh batch every 14 days",
        ],
        "table": ["Hook pattern", "0-3s open"],
        "rows": [
            ["Question", "Did you know...?"],
            ["Negative", "Stop doing X"],
            ["POV", "POV: you finally..."],
            ["Demo-first", "Watch this transform"],
            ["Before/after", "Split screen reveal"],
        ],
        "code": (
            "Tag schema (Sheet columns):\n"
            "asset_id | hook_type | format | cta | angle | week_live | spend | roas\n"
            "Refresh rule: new batch every 14d; postmortem at 21d"
        ),
        "failures": [
            ["One hero ad fatigue", "Increase variant volume"],
            ["Hooks not isolated", "Test 0-3s clips separately"],
            ["No tagging", "Cannot learn what won - add schema"],
        ],
        "insights": {
            "01_Landing_Cover.png": "Hybrid ad grid - UGC audience signal.",
            "02_Creative_First.png": "70-80% stat slide.",
            "03_Variant_Volume.png": "30-50 variants expectation set.",
            "04_Hook_Bible.png": "Most referenced page in PDF.",
            "05_Variant_Matrix.png": "Test grid for media buyers.",
            "06_AI_UGC_Identity.png": "Bridges to beauty identity work.",
            "07_Tagging_And_Refresh.png": "Ops calendar slide.",
            "08_CTA.png": "UGC keyword.",
        },
    },
    "08_MCP_Servers_By_Job": {
        "title": "MCP Servers by Job",
        "cta": "MCP",
        "tagline": "Connect for work, not for lists",
        "overview": (
            "Practitioners converge on a small high-leverage MCP set: filesystem, GitHub, Google Search Console, "
            "GA4, HubSpot, Obsidian/Notion, n8n for schedules. This guide maps <b>jobs</b> to server stacks with "
            "auth gotchas and proof prompts - not another giant server list."
        ),
        "workflow": [
            "Pick one recurring job (SEO weekly, pipeline, content alert)",
            "Install minimum MCP stack for that job only",
            "OAuth read-only scopes first",
            "Run proof prompt that verifies real data returned",
            "Add [REVIEW] before any write tool",
        ],
        "table": ["Job", "MCP stack", "Proof prompt"],
        "rows": [
            ["SEO weekly", "GSC + GA4 + fs", "Top 10 query drops WoW"],
            ["Pipeline", "HubSpot + Gmail", "Deals idle 14+ days"],
            ["Content alert", "GSC + Obsidian", "Pages down 20% clicks"],
        ],
        "code": (
            "Core five: filesystem, GitHub, GSC, GA4, HubSpot\n"
            "Add: Obsidian (memory), n8n (schedule)\n"
            "Week 1: list and fetch only - no create/update/delete"
        ),
        "failures": [
            ["Too many servers day 1", "Pick one job stack"],
            ["Write scope too early", "Read-first week"],
            ["Proof prompt hallucination", "Require tool trace in output"],
        ],
        "insights": {
            "01_Landing_Cover.png": "Not a list - job framing on cover.",
            "02_Stop_Installing_Random.png": "Mindset slide.",
            "03_Job_SEO_Report.png": "SEO job - broad audience.",
            "04_Job_Pipeline.png": "Sales job.",
            "05_Job_Content_Alert.png": "Content ops job.",
            "06_Core_Servers.png": "High-leverage five.",
            "07_Auth_Gotchas.png": "Auth checklist.",
            "08_CTA.png": "MCP keyword.",
        },
    },
    "09_Router_Worker_Reviewer": {
        "title": "Router, Worker, Reviewer",
        "cta": "WORKFLOW",
        "tagline": "Plan, execute, gate",
        "overview": (
            "Multi-agent pattern used everywhere: Router scopes and plans (no tools), Worker executes with "
            "MCP + Skills, Reviewer gates output with [REVIEW] or [SHIP]. Cuts drift, unsafe writes, and "
            "runaway token spend. Copy roles into CLAUDE.md or project rules."
        ),
        "workflow": [
            "Define Router output schema: tasks, tools, acceptance, out-of-scope",
            "Worker reads plan only - no replanning",
            "Reviewer checks facts, tone, PII, policy",
            "Bounce to Worker with diffs if fail",
            "End-to-end test: client weekly report job",
        ],
        "table": ["Role", "Can use tools?", "Output"],
        "rows": [
            ["Router", "No", "Plan + criteria"],
            ["Worker", "Yes", "Draft artifact"],
            ["Reviewer", "Read-only", "[REVIEW] or [SHIP]"],
        ],
        "code": (
            "Router: You plan only. Never call tools.\n"
            "Worker: Execute Router plan. No external send.\n"
            "Reviewer: Verify acceptance criteria. Tag [REVIEW] or [SHIP]."
        ),
        "failures": [
            ["Router calls tools", "Re-prompt - plan only"],
            ["Worker replans", "Freeze to Router output"],
            ["Reviewer always approves", "Require explicit checklist"],
        ],
        "insights": {
            "01_Landing_Cover.png": "Three-word stacked headline.",
            "02_The_Pattern.png": "Flow diagram - core teaching.",
            "03_Router_Role.png": "Boundaries for Router.",
            "04_Worker_Role.png": "Execution role.",
            "05_Reviewer_Role.png": "[REVIEW] vs [SHIP] tags.",
            "06_Example_Weekly_Report.png": "Concrete business example.",
            "07_Copy_Paste_Roles.png": "Highest save rate slide.",
            "08_CTA.png": "WORKFLOW keyword.",
        },
    },
    "10_Agent_Governance_SAFE": {
        "title": "Human-in-the-Loop Governance",
        "cta": "SAFE",
        "tagline": "Trust layer before agents act",
        "overview": (
            "Cowork, Workspace Agents, and MCP can take real actions. Governance is not optional: "
            "<b>[REVIEW]</b> protocol, read-first MCP, hard-blocked tool classes, audit logs, and a "
            "one-page team policy. This is what lets SMB owners say yes to agents."
        ),
        "workflow": [
            "Default all external writes to [REVIEW]",
            "Week 1 MCP: read-only scopes only",
            "Hard-block payments, bulk email, social publish",
            "Log: prompt, tools, output, approver, timestamp",
            "Print one-page policy for team",
        ],
        "table": ["Action", "Policy"],
        "rows": [
            ["Single email draft", "[REVIEW] required"],
            ["Bulk email", "Blocked auto"],
            ["Payment", "Two-person rule"],
            ["Social post", "[REVIEW] + brand check"],
            ["CRM mass update", "Blocked auto"],
        ],
        "code": (
            "[REVIEW] block template:\n"
            "Risk: low|med|high\n"
            "Diff: <what changes>\n"
            "Rollback: <how to undo>\n"
            "Awaiting: APPROVE or edits"
        ),
        "failures": [
            ["Silent send", "Hard-block at tool config"],
            ["No audit trail", "Add logging middleware"],
            ["Read+write day 1", "Read-first week policy"],
        ],
        "insights": {
            "01_Landing_Cover.png": "Before send - fear + solution.",
            "02_Why_Governance_Now.png": "2026 urgency.",
            "03_REVIEW_Protocol.png": "Protocol template slide.",
            "04_Read_First_MCP.png": "Read-first week.",
            "05_Write_Blocked_Tools.png": "Never auto list.",
            "06_What_To_Log.png": "Audit minimum.",
            "07_One_Page_Policy.png": "Printable policy.",
            "08_CTA.png": "SAFE keyword.",
        },
    },
}


def _guide_pages(carousel: dict, meta: dict) -> list:
    slug = carousel["slug"]
    n = len(carousel["slides"])
    return [
        [
            {"type": "heading", "text": meta["title"]},
            {"type": "subhead", "text": f"@piyush.glitch  |  {meta['tagline']}"},
            {"type": "prose", "text": meta["overview"]},
            {"type": "callout", "title": "Instagram CTA", "text": (
                f"Comment <b>{meta['cta']}</b> on the carousel post for this PDF. "
                f"Carousel folder: <b>{slug}</b> ({n} slides, 3:4 ratio)."
            )},
            {"type": "table", "headers": meta["table"], "rows": meta["rows"]},
            {"type": "prose", "text": (
                "<b>Prerequisites:</b> Team admin access where noted. Read-first MCP week recommended. "
                "Nothing in this guide auto-sends, auto-pays, or auto-posts - human approval required."
            )},
        ],
        [
            {"type": "heading", "text": "Operator workflow"},
            {"type": "bullets", "title": "Setup order", "items": meta["workflow"]},
            {"type": "code", "text": meta["code"]},
            {"type": "table", "headers": ["Failure", "Fix"], "rows": meta["failures"]},
            {"type": "prose", "text": (
                "<b>Next pages:</b> one page per Instagram slide with the actual generated image, "
                "on-slide intent, and the production prompt used with GPT Image."
            )},
        ],
        [
            {"type": "heading", "text": "Slide index"},
            {"type": "table", "headers": ["#", "File", "Topic"], "rows": [
                [str(i), fn, _title(fn)] for i, (fn, _) in enumerate(carousel["slides"], 1)
            ]},
            {"type": "callout", "title": "Visual DNA", "text": (
                "Terracotta #C45E3B grain background. Header: JUN @2026 PIYUSH.GLITCH. "
                "Black pill tags on info slides. Taped GitHub/repo cards at bottom. "
                "Cover: marble bust + glitch stroke + floating 3D icons."
            )},
            {"type": "prose", "text": (
                "<b>Regenerate tip:</b> Generate slide 01 first for style lock, then 02-08 in the same session. "
                "If typography warps, rebuild text in Figma using exported PNG background only."
            )},
        ],
    ]


def _slide_page(folder: Path, filename: str, prompt: str, meta: dict, index: int) -> list:
    insight = meta["insights"].get(filename, "Match on-slide copy and layout from carousel image.")
    return [[
        {"type": "subhead", "text": f"Slide {index} - {_title(filename)}"},
        {"type": "image", "path": str(folder / filename), "caption": filename, "max_height": 3.5 * inch},
        {"type": "h3", "text": "What this slide teaches"},
        {"type": "prose", "text": insight},
        {"type": "h3", "text": "Production prompt"},
        {"type": "code", "text": _clean_prompt(prompt)},
    ]]


def _closing(meta: dict) -> list:
    return [[
        {"type": "heading", "text": "Stay updated"},
        {"type": "callout", "title": f"Comment {meta['cta']}", "text": (
            f"Follow @piyush.glitch for operator-level AI stacks. "
            f"Comment <b>{meta['cta']}</b> on the matching carousel for PDF updates."
        )},
        {"type": "table", "headers": ["Check", "Pass?"], "rows": [
            ["All 8 slides generated 3:4", ""],
            ["Header/footer spelling correct", ""],
            ["Repo names accurate on cards", ""],
            ["CTA slide has no SWIPE arrow", ""],
            ["PDF matches carousel folder", ""],
        ]},
    ]]


def build_pages(carousel: dict) -> list:
    meta = DEEP[carousel["slug"]]
    folder = ROOT / carousel["slug"]
    pages = []
    pages.extend(_guide_pages(carousel, meta))
    for i, (fn, pr) in enumerate(carousel["slides"], 1):
        pages.extend(_slide_page(folder, fn, pr, meta, i))
    pages.extend(_closing(meta))
    return pages


def build_carousel_pdf(carousel: dict) -> Path:
    folder = ROOT / carousel["slug"]
    folder.mkdir(parents=True, exist_ok=True)
    out = folder / carousel["pdf_name"]
    build_pdf(out, build_pages(carousel))
    return out
