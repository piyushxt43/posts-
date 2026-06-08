# -*- coding: utf-8 -*-
"""14-page dense PDF for Claude vs GPT operator routing."""

PAGES = [
    [
        {"type": "heading", "text": "Claude vs GPT - Multi-Model Operator Manual"},
        {"type": "subhead", "text": "Job routing, API presets, cost math  |  @piyush.glitch"},
        {"type": "prose", "text": (
            "The carousel shows angles - coding, images, business, cost. "
            "This PDF is the <b>decision engine</b>: routing tables, API configs, "
            "monthly cost models, migration runbooks, and the three-model stack your team actually runs."
        )},
        {"type": "callout", "title": "Not a fanboy guide", "text": (
            "You will use Claude, GPT, and Gemini. Single-vendor teams lose on cost AND capability by Q3 2026."
        )},
        {"type": "table", "headers": ["Page", "Topic"], "rows": [
            ["2", "Routing decision tree (flowchart logic)"],
            ["3", "Claude deep: when it wins + config"],
            ["4", "GPT deep: when it wins + config"],
            ["5", "Gemini layer (Omni bridge preview)"],
            ["6", "Coding job matrix with $/task"],
            ["7", "Image + video generation routing"],
            ["8", "Business ops: Cowork vs Workspace Agents"],
            ["9", "Cost model spreadsheet logic"],
            ["10", "Router-Worker-Reviewer implementation"],
            ["11", "SKILL.md sync across vendors"],
            ["12", "4-week team migration"],
            ["13", "Anti-patterns + vendor lock-in traps"],
            ["14", "Stack checklist + API quick reference"],
        ]},
    ],
    [
        {"type": "heading", "text": "Routing decision tree"},
        {"type": "prose", "text": "Answer in order. First match wins."},
        {"type": "code", "text": (
            "START\n"
            "|-- Need terminal agent + MCP + subagents? --> CLAUDE CODE\n"
            "|-- Need scheduled team agent in ChatGPT UI? --> WORKSPACE AGENT\n"
            "|-- Need Gmail/Drive native automation? --> GEMINI GEM + STUDIO\n"
            "|-- Need 1M token doc read cheap? --> GEMINI FLASH via omni-ai-mcp\n"
            "|-- Need image API at scale? --> GPT IMAGE or HIGGSFIELD MCP\n"
            "|-- Need custom GPT marketplace for non-devs? --> CUSTOM GPT\n"
            "|-- Need contract/architecture adversarial review? --> CLAUDE OPUS\n"
            "|-- Need bulk classification 10k rows? --> GPT-4o MINI\n"
            "END -> always REVIEWER gate on external output"
        )},
        {"type": "table", "headers": ["Question", "If YES", "Tool"], "rows": [
            ["Touches production code?", "Yes", "Claude Code default"],
            ["Non-dev runs weekly?", "Yes", "Workspace Agent or Gem"],
            ["Reads Google-native only?", "Yes", "Gemini"],
            ["Needs approve-before-send?", "Yes", "Claude Cowork"],
            ["Consumer voice app?", "Yes", "ChatGPT app"],
        ]},
    ],
    [
        {"type": "heading", "text": "Claude - when it wins + config"},
        {"type": "table", "headers": ["Capability", "Why Claude", "Config"], "rows": [
            ["Agentic coding", "Subagents + CLAUDE.md memory", "Claude Code CLI"],
            ["MCP ecosystem", "GitHub, HubSpot, filesystem", "claude_desktop_config.json"],
            ["SMB workflows", "Cowork approve gate", "Small Business plugin"],
            ["Long sessions", "Compact + skills", "caveman + HUD"],
            ["Skills standard", "agentskills.io portable", "~/.claude/skills/"],
        ]},
        {"type": "code", "text": (
            "# Claude Code default stack\n"
            "Model: sonnet (daily) | opus (architect-review only)\n"
            "CLAUDE.md: project rules + agent routing\n"
            "MCP: github, filesystem, project-specific\n"
            "Plugins: per Plugins PDF stack"
        )},
        {"type": "prose", "text": (
            "<b>Claude loses when:</b> you need ChatGPT consumer reach, Custom GPT sharing with non-technical "
            "users, or mature GPT Actions webhook ecosystem for no-code automations."
        )},
    ],
    [
        {"type": "heading", "text": "GPT - when it wins + config"},
        {"type": "table", "headers": ["Capability", "Why GPT", "Config"], "rows": [
            ["Custom GPTs", "Shareable, no CLI", "chatgpt.com/gpts"],
            ["GPT Actions", "OpenAPI -> webhooks", "GPT builder Actions tab"],
            ["Workspace Agents", "Scheduled team runs", "ChatGPT Team/Enterprise"],
            ["Image API", "gpt-image-1 production", "platform.openai.com API"],
            ["Bulk cheap tasks", "4o mini at scale", "Batch API"],
        ]},
        {"type": "code", "text": (
            "# Workspace Agent example (weekly client report)\n"
            "Trigger: Monday 8am\n"
            "Sources: Salesforce connector (read)\n"
            "Output: Slack #client-updates draft\n"
            "Gate: human posts manually\n\n"
            "# GPT Action skeleton (OpenAPI)\n"
            "POST /webhook/report -> your-backend generates PDF"
        )},
        {"type": "prose", "text": (
            "<b>GPT loses when:</b> you need deep terminal coding with MCP, subagent isolation, "
            "or Anthropic's Cowork connector bundle for QuickBooks/HubSpot native SMB flows."
        )},
    ],
    [
        {"type": "heading", "text": "Gemini layer"},
        {"type": "subhead", "text": "Third leg of operator stack"},
        {"type": "prose", "text": (
            "Gemini wins Google-native: Gmail triage, Drive docs, Sheets, 1M context reads. "
            "Do not force Claude to paste 500-page PDFs - route reads through omni-ai-mcp (see Omni PDF)."
        )},
        {"type": "table", "headers": ["Job", "Gemini tool", "Claude role"], "rows": [
            ["Read entire contract corpus", "gemini-analyze 1M", "Synthesize actions"],
            ["UGC video with audio", "Veo 3.1 via MCP", "Brief + approve"],
            ["Gmail auto-triage", "Gem + Workspace Studio", "Policy in SKILL.md"],
            ["Deep Research report", "Gemini Deep Research", "Executive summary"],
        ]},
        {"type": "callout", "title": "Bridge pattern", "text": (
            "Claude = router/orchestrator. Gemini = heavy read + video worker. "
            "GPT = team scheduling + image API. All three share one SKILL.md repo."
        )},
    ],
    [
        {"type": "heading", "text": "Coding job matrix"},
        {"type": "table", "headers": ["Job", "Primary", "Fallback", "$/task est."], "rows": [
            ["Feature implementation", "Claude Sonnet", "Cursor Cloud Agent", "$0.50-2"],
            ["Hard bug 20m+", "Claude + Codex", "GPT-5 via codex", "$1-3"],
            ["Architecture review", "Claude Opus", "architect-review agent", "$2-5"],
            ["Bulk codemod 100 files", "Claude + Explore", "Batch script", "$3-8"],
            ["PR review only", "code-reviewer agent", "Human", "$0.20"],
            ["Codegen for non-dev", "Custom GPT", "Cowork", "$0.10"],
        ]},
        {"type": "prose", "text": (
            "Estimates assume ~50k tokens/task. Track actuals in spreadsheet week 1. "
            "Opus-only teams spend 3-5x without quality gain on routine tasks."
        )},
    ],
    [
        {"type": "heading", "text": "Image + video routing"},
        {"type": "table", "headers": ["Output", "Tool", "When"], "rows": [
            ["UI mock in IDE", "Claude Artifacts", "Fast iteration"],
            ["Production ad image", "GPT Image API", "API pipeline"],
            ["Multi-model UGC batch", "Higgsfield MCP", "Claude orchestrates"],
            ["4K video + audio", "Gemini Veo via omni", "Long-form"],
            ["Product photoreal", "FLUX via Higgsfield", "E-commerce"],
        ]},
        {"type": "code", "text": (
            "# UGC operator chain\n"
            "1. Claude drafts hooks from brand SKILL.md\n"
            "2. Higgsfield MCP: Kling 9:16 per hook\n"
            "3. Claude scores thumbnails\n"
            "4. Human [REVIEW] -> Meta upload\n"
            "5. Meta MCP reads performance -> next batch"
        )},
        {"type": "callout", "title": "Never auto-publish", "text": (
            "Generated assets always pass human [REVIEW]. Required for brand + platform policy."
        )},
    ],
    [
        {"type": "heading", "text": "Business ops routing"},
        {"type": "table", "headers": ["Workflow", "Claude Cowork", "GPT Workspace", "Gemini"], "rows": [
            ["Invoice chase", "QB connector native", "Via Action webhook", "Sheets only"],
            ["CRM pipeline nudge", "HubSpot Cowork", "Salesforce Agent", "Limited"],
            ["Contract review", "Cowork read-only", "Upload GPT", "Drive native"],
            ["Weekly exec brief", "Cowork /monday-brief", "Scheduled Agent", "Gem flow"],
            ["SEO report", "Claude + GSC MCP", "Custom GPT", "Search Console Gem"],
        ]},
        {"type": "prose", "text": (
            "<b>Decision rule:</b> If connector is Anthropic-native (QB, HubSpot, Canva) -> Cowork first. "
            "If team lives in ChatGPT Enterprise -> Workspace Agent. "
            "If Google Workspace only shop -> Gemini Gems + Studio."
        )},
    ],
    [
        {"type": "heading", "text": "Cost model logic"},
        {"type": "table", "headers": ["Tier", "Model", "$/1M in", "Use for"], "rows": [
            ["$$$", "Claude Opus", "~$15", "Architecture, contracts"],
            ["$$", "Claude Sonnet", "~$3", "Daily coding"],
            ["$", "GPT-4o mini", "~$0.15", "Bulk classify"],
            ["$", "Gemini Flash", "Free tier ops", "1M reads via MCP"],
            ["$$", "GPT-4o", "~$2.50", "General team chat"],
        ]},
        {"type": "code", "text": (
            "# Monthly budget formula\n"
            "coding_tasks * sonnet_cost\n"
            "+ review_tasks * opus_cost\n"
            "+ bulk_rows * mini_cost\n"
            "+ gemini_reads * flash_cost\n"
            "+ image_gens * gpt_image_cost\n"
            "= total  (target: plan/review on expensive, execute on cheap)"
        )},
        {"type": "callout", "title": "Cost trap", "text": (
            "Using Opus for grep and search. Route to Haiku Explore agent or Gemini Flash read instead."
        )},
    ],
    [
        {"type": "heading", "text": "Router-Worker-Reviewer"},
        {"type": "prose", "text": (
            "Implement the stack as three roles - can be one human + three model calls."
        )},
        {"type": "table", "headers": ["Role", "Model", "Output"], "rows": [
            ["Router", "Claude Sonnet", "Job ticket: tool + acceptance criteria"],
            ["Worker", "Per routing table", "Draft artifact"],
            ["Reviewer", "Human or Opus", "APPROVE / REJECT"],
        ]},
        {"type": "code", "text": (
            "# Router prompt template\n"
            "Job: {description}\n"
            "Pick worker: claude-code | workspace-agent | gemini-mcp | gpt-image\n"
            "Output JSON: {tool, model, steps, acceptance_criteria, estimated_cost}\n"
            "Do not execute - wait for APPROVE."
        )},
    ],
    [
        {"type": "heading", "text": "SKILL.md sync across vendors"},
        {"type": "subhead", "text": "CyPack/ai-tooling-sync pattern"},
        {"type": "code", "text": (
            "# One repo: company-skills/\n"
            "skills/brand-voice/SKILL.md\n"
            "skills/seo-report/SKILL.md\n"
            "skills/pr-review/SKILL.md\n\n"
            "# Sync to:\n"
            "~/.claude/skills/     (Claude Code)\n"
            ".cursor/rules/        (Cursor)\n"
            "Custom GPT instructions (paste)\n"
            "Gem system prompt (paste)\n\n"
            "# Tool: github.com/CyPack/ai-tooling-sync"
        )},
        {"type": "prose", "text": (
            "Skills are the portability layer. MCP is the connector layer. "
            "Do not rewrite brand voice four times - sync weekly."
        )},
    ],
    [
        {"type": "heading", "text": "4-week team migration"},
        {"type": "table", "headers": ["Week", "Action", "Pass"], "rows": [
            ["1", "Document current single-vendor spend", "Baseline spreadsheet"],
            ["2", "Add Claude Code for eng only", "1 shipped PR with MCP"],
            ["3", "Add one Workspace Agent OR Cowork workflow", "1 scheduled run"],
            ["4", "Add Gemini bridge for 1M reads", "1 doc analyze success"],
            ["5", "Publish routing wiki + SKILL sync", "Team quiz pass"],
        ]},
        {"type": "bullets", "title": "Change management", "items": [
            "No big-bang vendor switch - parallel run 30 days",
            "Name model router owner (staff engineer or ops lead)",
            "Monthly routing table review in eng meeting",
        ]},
    ],
    [
        {"type": "heading", "text": "Anti-patterns"},
        {"type": "table", "headers": ["Trap", "Cost", "Fix"], "rows": [
            ["One model for everything", "3-5x overspend", "Routing table"],
            ["No REVIEW gate", "Brand/reputation risk", "Mandatory human approve"],
            ["Duplicate skills per tool", "Drift", "ai-tooling-sync"],
            ["Gemini for terminal coding", "Wrong tool", "Claude Code"],
            ["Claude for Custom GPT sharing", "Friction", "GPT marketplace"],
            ["Ignoring free Gemini reads", "Waste", "omni-ai-mcp bridge"],
        ]},
    ],
    [
        {"type": "heading", "text": "Stack checklist + API reference"},
        {"type": "table", "headers": ["Done?", "Item"], "rows": [
            ["", "Routing decision tree posted in wiki"],
            ["", "Cost spreadsheet with actuals"],
            ["", "SKILL.md sync repo created"],
            ["", "Router-Worker-Reviewer in CLAUDE.md"],
            ["", "Each vendor API key in secrets manager"],
            ["", "[REVIEW] policy signed by leadership"],
        ]},
        {"type": "table", "headers": ["API", "Console"], "rows": [
            ["Claude", "console.anthropic.com"],
            ["OpenAI", "platform.openai.com"],
            ["Gemini", "aistudio.google.com"],
        ]},
        {"type": "callout", "title": "@piyush.glitch", "text": "Comment <b>AI</b> | June 2026 v2 dense manual."},
    ],
]
