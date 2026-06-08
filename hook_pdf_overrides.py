# -*- coding: utf-8 -*-
"""Hook-aligned title/subtitle/intro + custom PDF filenames for 7 high-save carousels."""

HOOK_PDF_OVERRIDES = {
    "27_Claude_Skills_To_Steal": {
        "pdf_filename": "steal-claude-carousel-skill.pdf",
        "title": "Steal This Claude Carousel Skill",
        "subtitle": "One SKILL.md turns any topic into hook + 8 slides + CTA - copy the exact file.",
        "kicker": "CLAUDE TACTICS - STEAL THIS",
        "intro": (
            "The highest-save post format on business Instagram is an 8-slide carousel with a brutal hook. "
            "Most creators re-prompt from scratch every time. Operators package the whole workflow as a Claude "
            "Skill: YAML frontmatter + steps that output hook, eight slide headlines, body copy, visual direction "
            "and a CTA in one run. This guide is the copy-paste carousel-factory skill - including the description "
            "that triggers it, the progressive-disclosure layout, and the quality bar that stops generic output."
        ),
        "callout": {
            "title": "Save-driver move",
            "text": "Name the skill carousel-factory and front-load the description: 'Build an 8-slide Instagram "
                    "carousel from one topic - hook, headlines, body, visual notes, CTA.' Test five topics; "
                    "iterate the NEVER list until slide 1 stops sounding like a blog post.",
        },
    },
    "08_Agent_Evals_As_Release_Gates": {
        "pdf_filename": "12-agents-3-survived.pdf",
        "title": "12 AI Agents. 30 Days. 3 Survived.",
        "subtitle": "A field scorecard - what actually held up in real business work.",
        "kicker": "AI FOR BUSINESS - FIELD TEST",
        "intro": (
            "I deployed twelve AI agents against the same real business tasks for thirty days: research, inbox "
            "triage, reporting, light ops, drafting. Nine died - loops, hallucinated tool calls, ignored "
            "constraints, or cost more supervision than doing the work myself. Three survived: a narrow "
            "source-grounded researcher, a read-mostly ops runner with write approval, and a drafter that "
            "never had final say. This guide is the scorecard, the failure modes, and the eval gates that "
            "would have killed the nine before they burned a month."
        ),
        "callout": {
            "title": "Survival pattern",
            "text": "Every survivor had narrow scope, checkable output (citations, diffs, drafts you review), "
                    "and a human gate on writes. Every agent that died was wide, autonomous, and unsupervised. "
                    "Build your eval set from those three traits - not leaderboard trivia.",
        },
    },
    "13_Claude_MCP_For_Operators": {
        "pdf_filename": "7-mcp-connectors-ops-stack.pdf",
        "title": "7 MCP Connectors That Replace a 5-Person Ops Stack",
        "subtitle": "Live hands into Postgres, GitHub, Slack, Notion, Drive, Meta Ads and your API.",
        "kicker": "AI FOR BUSINESS - CLAUDE MCP",
        "intro": (
            "A five-person ops team spends its week on reporting, ticket triage, doc search, CRM lookups, "
            "ad diagnostics and status updates - mostly moving data between systems. Seven MCP connectors "
            "wired into Claude replace that glue work when scoped read-first and gated on writes: Postgres "
            "(metrics), GitHub (PR/issue context), Slack (summaries), Notion (runbooks), Google Drive "
            "(contracts), Meta Ads MCP (campaign diagnostics), and a thin internal REST MCP for your CRM. "
            "This is the operator wiring diagram - not 'connect everything day one.'"
        ),
        "callout": {
            "title": "Stack math",
            "text": "Enable three read-only MCPs first (Postgres replica, GitHub read, Drive search). Prove one "
                    "daily report before adding Slack write or Meta Ads. Keep enabled servers under ten or your "
                    "200K context shrinks toward seventy thousand usable tokens.",
        },
    },
    "30_Claude_md_Mastery": {
        "pdf_filename": "claude-md-half-your-tokens.pdf",
        "title": "The CLAUDE.md Mistake Wasting Half Your Tokens",
        "subtitle": "Bloat, cold starts, and re-discovery - the silent tax on every Claude Code session.",
        "kicker": "CLAUDE TACTICS - CLAUDE.md",
        "intro": (
            "Most repos either have no CLAUDE.md - so every session cold-starts and re-discovers your stack - "
            "or a two-thousand-line monster that loads into context every time and silently eats half your "
            "token budget before you ask a question. The fix is not 'write more instructions.' It is a lean "
            "root file under five hundred lines, scoped rules in .claude/rules/, and conditional triggers that "
            "load deep docs only when you touch auth or billing. CLAUDE.md is the only context that survives "
            "/compact - this guide shows the mistake patterns and the lean architecture that stops the bleed."
        ),
        "callout": {
            "title": "Silent bleed",
            "text": "Run /context after session start. If CLAUDE.md + always-on rules eat more than fifteen "
                    "percent of the window before your first prompt, you are paying a tax on every message. "
                    "Move domain depth behind 'Before editing X, read docs/X.md' triggers.",
        },
    },
    "12_Claude_Artifacts_For_Business": {
        "pdf_filename": "80-percent-content-cut.pdf",
        "title": "I Cut Content Time 80% With One Claude Skill",
        "subtitle": "Artifact + Project + carousel-factory skill - the repeatable content pipeline.",
        "kicker": "AI FOR BUSINESS - ARTIFACTS",
        "intro": (
            "Content used to mean: brief, draft in chat, copy to Docs, reformat for carousel, design in Canva, "
            "rewrite for newsletter - five tools, three hours. One Claude Skill inside a Content Project forces "
            "deliverables into Artifacts: long-form in an editable doc Artifact, carousel structure in a second "
            "Artifact, hooks in a third. Iteration is v2/v3 in place, not re-prompting from zero. After two "
            "weeks the skill + exemplar library in project knowledge cut production time roughly eighty percent "
            "on a real weekly content cadence. This guide is the skill file, the Project instructions, and the "
            "Artifact prompts - not generic 'use AI for content' advice."
        ),
        "callout": {
            "title": "The 80% lever",
            "text": "Force Artifact-only mode: 'Put each deliverable in its own Artifact; chat only for "
                    "questions.' Save approved Artifacts back to project knowledge as EXAMPLE- files. The skill "
                    "loads structure; the exemplars load taste.",
        },
    },
    "19_Claude_Daily_Business_Ops": {
        "pdf_filename": "claude-won-business-ops.pdf",
        "title": "Everyone's Chasing GPT. Claude Won Business Ops.",
        "subtitle": "Projects, Artifacts, MCP and daily modes - why operators standardised on Claude.",
        "kicker": "AI FOR BUSINESS - DAILY OPS",
        "intro": (
            "The timeline is full of GPT agent demos and benchmark wars. Meanwhile operators quietly moved "
            "daily business infrastructure to Claude: one Daily Ops Project with MORNING / INBOX / MEETING / EOD "
            "modes, Artifacts for decision memos, MCP for live metrics, and Sonnet-for-volume / Opus-for-judgment "
            "routing. Not because Claude wins trivia - because Projects persist instructions, Artifacts ship "
            "deliverables, MCP reads truth, and the eval story is checkable. This guide is the daily ops stack "
            "that survived a thirty-day field test while nine generic agents died."
        ),
        "callout": {
            "title": "Why ops, not hype",
            "text": "GPT Agent mode excels at one-off web tasks. Claude excels at repeatable internal workflows "
                    "with memory, structured output and live connectors. Pick the tool for the job - ops teams "
                    "picked Claude because the output lands in Artifacts and Projects, not chat paragraphs.",
        },
    },
    "26_Claude_Hidden_Commands": {
        "pdf_filename": "5-commands-not-in-docs.pdf",
        "title": "5 Claude Commands Not in the Docs",
        "subtitle": "/compact focus, /btw, /init, /effort, /loop - the CLI shipped faster than the manual.",
        "kicker": "CLAUDE TACTICS - INSIDER",
        "intro": (
            "Anthropic's Claude Code docs lag the CLI - power users bookmark cheat sheets because the product "
            "shipped faster than the reference. Five commands change output quality and cost more than any "
            "prompt tweak: /compact focus on X (keeps the constraint plain /compact loses), /btw (side questions "
            "without burning main context), /init (drafts CLAUDE.md from your repo), /effort (dials reasoning "
            "low/med/high per task), and /loop (recurring work that can bill for hours if you walk away). "
            "This guide is the insider card - plus the prompt prefixes (ULTRATHINK, /skeptic, L99) that stack "
            "on top."
        ),
        "callout": {
            "title": "Gated-access feel",
            "text": "Stack /skeptic + ULTRATHINK on architecture decisions - it challenges your premise before "
                    "going deep. Most users never stack prefixes; that alone separates operator output from "
                    "default chat quality.",
        },
    },
}


def apply_hook_overrides(content: dict) -> dict:
    """Merge hook overrides into CONTENT entries."""
    for slug, overrides in HOOK_PDF_OVERRIDES.items():
        if slug not in content:
            continue
        content[slug].update(overrides)
    return content
