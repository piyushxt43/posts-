# -*- coding: utf-8 -*-
"""10-page operator PDFs - unique depth per carousel."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent

META = {
    "01_Claude_Small_Business_Cowork": {
        "title": "Claude for Small Business (Cowork)",
        "cta": "COWORK",
        "pdf": "claude-small-business-cowork.pdf",
        "tag": "SMB ops | connectors | approve-before-send",
    },
    "02_Skills_MCP_Two_Layer_Stack": {
        "title": "Skills + MCP Two-Layer Stack",
        "cta": "STACK",
        "pdf": "skills-mcp-two-layer-stack.pdf",
        "tag": "USB access vs playbook procedure",
    },
    "03_Agent_Skills_Write_Once": {
        "title": "Agent Skills: Write Once, Run Everywhere",
        "cta": "SKILLS",
        "pdf": "agent-skills-write-once.pdf",
        "tag": "SKILL.md portable standard",
    },
    "04_Cursor_Cloud_Agents": {
        "title": "Cursor Cloud Agents",
        "cta": "CLOUD",
        "pdf": "cursor-cloud-agents.pdf",
        "tag": "VMs, browser tests, merge-ready PRs",
    },
    "05_OpenAI_Workspace_Agents": {
        "title": "OpenAI Workspace Agents",
        "cta": "AGENTS",
        "pdf": "openai-workspace-agents.pdf",
        "tag": "shared scheduled team agents",
    },
    "06_Google_Workspace_Studio_Gems": {
        "title": "Google Workspace Studio + Gems",
        "cta": "STUDIO",
        "pdf": "google-workspace-studio-gems.pdf",
        "tag": "Ask a Gem inside no-code flows",
    },
    "07_Meta_UGC_Creative_OS": {
        "title": "Meta UGC Creative Operating System",
        "cta": "UGC",
        "pdf": "meta-ugc-creative-os.pdf",
        "tag": "Advantage+ variant factory",
    },
    "08_MCP_Servers_By_Job": {
        "title": "MCP Servers by Job",
        "cta": "MCP",
        "pdf": "mcp-servers-by-job.pdf",
        "tag": "job stacks, not server lists",
    },
    "09_Router_Worker_Reviewer": {
        "title": "Router, Worker, Reviewer",
        "cta": "WORKFLOW",
        "pdf": "router-worker-reviewer.pdf",
        "tag": "plan, execute, gate",
    },
    "10_Agent_Governance_SAFE": {
        "title": "Human-in-the-Loop Governance",
        "cta": "SAFE",
        "pdf": "agent-governance-safe.pdf",
        "tag": "trust layer before agents act",
    },
}


def _img(slug: str, fn: str = "01_Landing_Cover.png", cap: str = "") -> dict:
    return {"type": "image", "path": str(ROOT / slug / fn), "caption": cap or fn, "max_height": 3.2}


def pages_for(slug: str) -> list:
    m = META[slug]
    builders = {
        "01_Claude_Small_Business_Cowork": _pages_01,
        "02_Skills_MCP_Two_Layer_Stack": _pages_02,
        "03_Agent_Skills_Write_Once": _pages_03,
        "04_Cursor_Cloud_Agents": _pages_04,
        "05_OpenAI_Workspace_Agents": _pages_05,
        "06_Google_Workspace_Studio_Gems": _pages_06,
        "07_Meta_UGC_Creative_OS": _pages_07,
        "08_MCP_Servers_By_Job": _pages_08,
        "09_Router_Worker_Reviewer": _pages_09,
        "10_Agent_Governance_SAFE": _pages_10,
    }
    return builders[slug](slug, m)


def _pages_01(slug: str, m: dict) -> list:
    return [
        [
            {"type": "heading", "text": m["title"]},
            {"type": "subhead", "text": f"@piyush.glitch Operator Guide  |  {m['tag']}"},
            {"type": "prose", "text": (
                "Anthropic's <b>Claude for Small Business</b> (May 2026) is a one-toggle plugin inside "
                "<b>Claude Cowork</b> (desktop). It bundles 15 agentic workflows + 15 skills across finance, "
                "sales, marketing, HR, and customer service. Connectors: QuickBooks, PayPal, HubSpot, Canva, "
                "DocuSign, Google Workspace, Microsoft 365, Slack. Claude reads, drafts, stages - you approve "
                "before anything sends, posts, or pays."
            )},
            {"type": "callout", "title": "Comment keyword", "text": (
                f"Comment <b>{m['cta']}</b> on the Instagram carousel for this PDF + slide pack."
            )},
            {"type": "table", "headers": ["Page", "You will learn"], "rows": [
                ["2", "Decision tree: which workflow first"],
                ["3", "Cowork install + connector OAuth"],
                ["4", "Finance: invoice chase + cash pulse"],
                ["5", "Sales/HR workflows + slash commands"],
                ["6", "Hidden repos + productivity hacks"],
                ["7", "CLAUDE.md business brain file"],
                ["8", "4-week rollout plan"],
                ["9", "Failure modes"],
                ["10", "Checklist + cover slide"],
            ]},
        ],
        [
            {"type": "heading", "text": "Why Cowork beats chat for SMB"},
            {"type": "prose", "text": (
                "Chat answers questions. Cowork runs <b>end-to-end jobs</b> across your stack: pull QuickBooks "
                "invoices, draft reminders in your tone, stage HubSpot follow-ups, build Canva onboarding decks. "
                "The moat is <b>context hygiene + approval gates</b> - not another prompt library."
            )},
            {"type": "table", "headers": ["If your pain is...", "Start here", "Risk level"], "rows": [
                ["Cash flow visibility", "/business-pulse + Invoice chase", "Low (read-heavy)"],
                ["Stale pipeline", "Lead triage + Pipeline nudge", "Medium (draft emails)"],
                ["Month-end chaos", "Month-end close packet", "Medium"],
                ["Contract risk", "Contract review (read-only)", "Low"],
                ["New hire admin", "Onboarding pack", "High (calendar + email)"],
            ]},
            {"type": "callout", "title": "Trust boundary", "text": (
                "Week 1: read-only connector scopes. Week 2: draft-only writes. Week 3+: explicit APPROVE "
                "on payments, bulk email, social publish. Skills draft - they never auto-fire."
            )},
        ],
        [
            {"type": "heading", "text": "Setup: first 60 minutes"},
            {"type": "bullets", "title": "Install sequence", "items": [
                "Download Claude desktop app (Cowork is desktop-only)",
                "Sidebar: Customize -> Plugins -> + -> Install Small Business",
                "Customize plugin: tell Claude your industry, team size, top 3 pains",
                "Connectors: OAuth QuickBooks + HubSpot first (read scopes)",
                "Run: 'get me started' - Claude walks first workflow",
                "Paste safety block into team instructions (page 4)",
            ]},
            {"type": "code", "text": (
                "# Cowork slash commands (copy-paste)\n"
                "/business-pulse     # cash + pipeline + 3 to-dos\n"
                "/invoice-chase      # overdue AR drafts\n"
                "/lead-triage        # HubSpot score + follow-ups\n"
                "/monday-brief       # one-page exec summary\n"
                "/contract-review    # red flags before sign"
            )},
            {"type": "prose", "text": (
                "<b>Official tutorial:</b> claude.com/resources/tutorials/how-to-install-the-claude-for-small-business-plugin"
            )},
        ],
        [
            {"type": "heading", "text": "Workflow deep dive: Finance"},
            {"type": "subhead", "text": "Invoice chase - highest ROI for most SMBs"},
            {"type": "prose", "text": (
                "Trigger: Monday 9am or on-demand. Steps: (1) Pull open invoices from QuickBooks. "
                "(2) Rank by amount + days overdue. (3) Draft 3 tone variants per client tier. "
                "(4) Output [REVIEW] block with diff. (5) You APPROVE -> send via Gmail connector."
            )},
            {"type": "code", "text": (
                "Prompt (invoice chase):\n"
                "Pull all QuickBooks invoices overdue 7+ days. Group by client tier.\n"
                "Draft reminder emails matching our tone guide in references/tone.md.\n"
                "End each draft with [REVIEW] - never send.\n"
                "Flag any invoice over $5k as risk:high."
            )},
            {"type": "table", "headers": ["Metric", "Target week 4"], "rows": [
                ["AR recovered", "$2k-$10k from first chase batch"],
                ["Draft accuracy", "90%+ need only minor edits"],
                ["Auto-send incidents", "0"],
            ]},
        ],
        [
            {"type": "heading", "text": "Sales + HR workflows"},
            {"type": "subhead", "text": "Pipeline nudge + onboarding pack"},
            {"type": "prose", "text": (
                "<b>Pipeline nudge:</b> HubSpot deals idle 14+ days -> personalized nudge drafts -> [REVIEW]. "
                "<b>Onboarding pack:</b> new hire trigger -> checklist -> Canva welcome deck -> calendar holds "
                "-> staged invites (nothing sends until OK)."
            )},
            {"type": "bullets", "title": "Marketing workflows in plugin", "items": [
                "Campaign from HubSpot analysis to Canva assets",
                "Customer pulse digest from CRM + support",
                "Margin analysis on product lines",
                "Tax season prep packet from QuickBooks",
            ]},
            {"type": "callout", "title": "Pro move", "text": (
                "Customize the plugin once: Claude rewrites default skills for your industry. "
                "From then on skills carry your context - team size, tone, priorities."
            )},
        ],
        [
            {"type": "heading", "text": "GitHub gems + productivity hacks"},
            {"type": "table", "headers": ["Repo", "Why it matters"], "rows": [
                ["anthropics/skills", "Official SKILL.md examples + format spec"],
                ["ComposioHQ/awesome-claude-skills", "78 SaaS workflow skills via Rube MCP"],
                ["MichaelGong/mcp-to-skills", "Auto-write SKILL.md per MCP server"],
                ["CyPack/ai-tooling-sync", "Sync skills/rules across Claude, Cursor, Codex"],
            ]},
            {"type": "bullets", "title": "Hidden productivity moves", "items": [
                "/compact focus - shrink context to current task only",
                "/btw - side note without polluting main thread",
                "/effort medium - default for ops (save Opus for contract review)",
                "Pair Cowork finance read with mcp-to-skills for custom connectors",
                "Free AI Fluency course (Anthropic + PayPal) for team onboarding",
            ]},
            {"type": "code", "text": (
                "mcp-to-skills quickstart:\n"
                "npm i -g @mgong/mcp-to-skills\n"
                "mcp-to-skills list    # probe MCP servers\n"
                "mcp-to-skills sync    # write SKILL.md each\n"
                "mcp-to-skills install # copy to ~/.claude/skills/"
            )},
        ],
        [
            {"type": "heading", "text": "CLAUDE.md business brain"},
            {"type": "prose", "text": (
                "Create <b>business-brain.md</b> at repo root or Cowork project folder. Include: "
                "company one-liner, ICP, tone rules, approval policy, connector map, escalation contacts. "
                "Cowork skills reference this file - stops re-explaining context every session."
            )},
            {"type": "code", "text": (
                "# business-brain.md skeleton\n"
                "## Company\n"
                "What we sell | ICP | avg deal size\n\n"
                "## Tone\n"
                "Friendly-professional | never slang | sign-off rules\n\n"
                "## Approval policy\n"
                "[REVIEW] on all external writes | $1k+ needs manager\n\n"
                "## Connectors\n"
                "QB: read+write invoices | HubSpot: read deals, draft only\n\n"
                "## Escalation\n"
                "Finance: name@ | Sales: name@"
            )},
        ],
        [
            {"type": "heading", "text": "4-week rollout plan"},
            {"type": "table", "headers": ["Week", "Focus", "Pass criteria"], "rows": [
                ["1", "Install + read-only connectors", "/business-pulse returns real numbers"],
                ["2", "Invoice chase dry-run", "3 drafts match tone, 0 auto-sends"],
                ["3", "Pipeline nudge live", "5 deals touched, human approved"],
                ["4", "Monday brief on cron", "Team uses brief in standup"],
            ]},
            {"type": "bullets", "title": "Admin checklist", "items": [
                "Document which connectors each role may use",
                "Log every APPROVE with timestamp + user",
                "Monthly: audit skill outputs for tone drift",
                "Cancel redundant SaaS if Cowork replaces manual exports",
            ]},
        ],
        [
            {"type": "heading", "text": "Failure modes"},
            {"type": "table", "headers": ["Symptom", "Fix"], "rows": [
                ["Wrong client tone", "Add 5 gold email examples to tone.md"],
                ["Connector auth expired", "Re-OAuth; test /business-pulse"],
                ["Duplicate invoice chases", "Dedupe by invoice_id in step 1"],
                ["Team skips [REVIEW]", "Disable write scopes at connector level"],
                ["Plugin feels generic", "Re-run Customize with industry detail"],
            ]},
        ],
        [
            {"type": "heading", "text": "Final checklist"},
            {"type": "table", "headers": ["Done?", "Item"], "rows": [
                ["", "Small Business plugin installed in Cowork"],
                ["", "QuickBooks + HubSpot connected read-first"],
                ["", "[REVIEW] policy in team instructions"],
                ["", "First workflow: invoice chase dry-run"],
                ["", "business-brain.md committed"],
                ["", "mcp-to-skills sync for custom MCP"],
            ]},
            _img(slug, cap="Carousel cover - Claude for Small Business Cowork"),
            {"type": "callout", "title": f"Comment {m['cta']}", "text": (
                f"Follow @piyush.glitch. Comment <b>{m['cta']}</b> on Instagram for updates. "
                f"File: {m['pdf']}"
            )},
        ],
    ]


def _pages_02(slug: str, m: dict) -> list:
    return [
        [
            {"type": "heading", "text": m["title"]},
            {"type": "subhead", "text": f"@piyush.glitch  |  {m['tag']}"},
            {"type": "prose", "text": (
                "<b>MCP</b> = standardized access (files, APIs, SaaS). <b>Skills</b> = procedure "
                "(tone, steps, guardrails). Stack them: MCP connects, Skill instructs. "
                "Open standard at <b>agentskills.io</b> (~20k GitHub stars)."
            )},
            {"type": "callout", "title": f"Comment {m['cta']}", "text": "Instagram carousel companion PDF."},
            {"type": "table", "headers": ["Layer", "Analogy", "Example"], "rows": [
                ["MCP", "USB port", "HubSpot, GSC, filesystem"],
                ["Skill", "Playbook", "collections-chase SKILL.md"],
                ["Host", "Computer", "Claude Code, Cursor, Codex"],
            ]},
        ],
        [
            {"type": "heading", "text": "Mental model: USB vs playbook"},
            {"type": "prose", "text": (
                "Without MCP, agents hallucinate CRM data. Without Skills, outputs drift run-to-run. "
                "Together: MCP pulls stale deals, Skill defines chase tone + escalation + [REVIEW] gate."
            )},
            {"type": "code", "text": (
                "Stack diagram:\n"
                "  [User task]\n"
                "       |\n"
                "  [Skill activates] -> loads SKILL.md procedure\n"
                "       |\n"
                "  [MCP tools] -> hubspot.list_deals, gmail.draft\n"
                "       |\n"
                "  [Reviewer] -> [REVIEW] before send"
            )},
        ],
        [
            {"type": "heading", "text": "MCP layer setup"},
            {"type": "bullets", "title": "Install order", "items": [
                "Pick ONE job first (invoice chase, UI audit, Monday brief)",
                "Add MCP servers to ~/.claude/claude_desktop_config.json or Cursor MCP settings",
                "Week 1: list/fetch tools only - no create/update/delete",
                "Run proof prompt that shows real tool trace in output",
            ]},
            {"type": "table", "headers": ["Server", "Package / URL"], "rows": [
                ["HubSpot", "mcp.hubspot.com (OAuth) or @hubspot/mcp-server"],
                ["GSC + GA4", "kairos-company/google-mcp or official Google MCP"],
                ["Filesystem", "@modelcontextprotocol/server-filesystem"],
                ["GitHub", "github.com/github/github-mcp-server"],
            ]},
        ],
        [
            {"type": "heading", "text": "Skills layer setup"},
            {"type": "prose", "text": (
                "Skill folder: SKILL.md + optional scripts/ + references/. Progressive disclosure: "
                "agent loads name+description at startup (~100 tokens each), full body on activation."
            )},
            {"type": "code", "text": (
                "---\n"
                "name: collections-chase\n"
                "description: Chase stale deals and draft nudges. Use for AR, pipeline, collections.\n"
                "---\n\n"
                "## Steps\n"
                "1. MCP: hubspot deals idle 14+ days\n"
                "2. Draft per tone guide in references/tone.md\n"
                "3. Escalation: 14d friendly, 21d firm, 30d final\n"
                "4. [REVIEW] block - never send"
            )},
        ],
        [
            {"type": "heading", "text": "Job recipe: Invoice chase"},
            {"type": "table", "headers": ["Component", "Spec"], "rows": [
                ["MCP", "HubSpot read deals + contacts"],
                ["Skill", "collections-chase"],
                ["Output", "3 draft emails per tier"],
                ["Gate", "[REVIEW] mandatory"],
            ]},
            {"type": "code", "text": (
                "Proof prompt:\n"
                "List HubSpot deals with no activity 14+ days. Show deal_id, amount, last_touch.\n"
                "If empty, say 'no stale deals' with query timestamp."
            )},
        ],
        [
            {"type": "heading", "text": "Job recipe: UI audit + Monday brief"},
            {"type": "subhead", "text": "Dev + ops audiences"},
            {"type": "prose", "text": (
                "<b>UI audit:</b> filesystem + GitHub MCP + impeccable skill (pbakaus/impeccable) - "
                "24-point anti-AI-slop checklist before merge.<br/>"
                "<b>Monday brief:</b> GSC + GA4 MCP + ops-brief skill - executive one-pager with anomalies flagged."
            )},
            {"type": "code", "text": (
                "Monday brief proof prompt:\n"
                "Pull GSC top 10 query drops WoW and GA4 landing pages down 20%+ clicks.\n"
                "Format: 1-page exec summary with 3 recommended actions."
            )},
        ],
        [
            {"type": "heading", "text": "GitHub gems"},
            {"type": "table", "headers": ["Repo", "Stars", "Use"], "rows": [
                ["agentskills/agentskills", "20k+", "Spec + skills-ref validator"],
                ["modelcontextprotocol/servers", "8k+", "Official server registry"],
                ["anthropics/skills", "-", "Example skills from Anthropic"],
                ["MichaelGong/mcp-to-skills", "-", "MCP -> SKILL.md generator"],
                ["matthiastjong/awesome-mcp", "daily", "Curated MCP discovery"],
                ["robotic-pixels/marketing-skills", "-", "GA4+HubSpot MCP configs"],
            ]},
            {"type": "bullets", "title": "Productivity hacks", "items": [
                "Never put OAuth secrets in SKILL.md - MCP handles auth",
                "One skill per job - not one mega-skill for everything",
                "Validate skills: npx skills-ref validate ./my-skill",
                "SkillsMP.com for semantic search across 400k+ community skills",
            ]},
        ],
        [
            {"type": "heading", "text": "Install paths per tool"},
            {"type": "table", "headers": ["Tool", "Skill path"], "rows": [
                ["Claude Code", "~/.claude/skills/ or .claude/skills/"],
                ["Cursor", ".cursor/skills/ or ~/.cursor/skills/"],
                ["Codex CLI", "AGENTS.md references skill folder"],
                ["GitHub Copilot", ".github/skills/"],
            ]},
            {"type": "callout", "title": "CyPack/ai-tooling-sync", "text": (
                "Single git repo for skills - sync to Claude, Cursor, Codex in one command. "
                "Stops the four-config drift problem."
            )},
        ],
        [
            {"type": "heading", "text": "Failure modes"},
            {"type": "table", "headers": ["Problem", "Fix"], "rows": [
                ["Skill without MCP", "Agent hallucinates - add MCP read first"],
                ["MCP without Skill", "Inconsistent output - add SKILL.md"],
                ["Token bloat", "Split long skills into references/ files"],
                ["Wrong skill triggers", "Rewrite description field - it's the trigger"],
            ]},
        ],
        [
            {"type": "heading", "text": "Stack checklist"},
            {"type": "bullets", "title": "Done when", "items": [
                "One job picked and proof prompt passes",
                "MCP read-only week completed",
                "Matching SKILL.md installed",
                "[REVIEW] on all writes",
                "Diagram saved for team onboarding",
            ]},
            _img(slug),
            {"type": "callout", "title": f"Comment {m['cta']}", "text": f"@piyush.glitch | {m['pdf']}"},
        ],
    ]


def _pages_03(slug: str, m: dict) -> list:
    return [
        [
            {"type": "heading", "text": m["title"]},
            {"type": "subhead", "text": f"@piyush.glitch  |  {m['tag']}"},
            {"type": "prose", "text": (
                "One <b>SKILL.md</b> folder works in Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot. "
                "Replace duplicated .cursor/rules + CLAUDE.md + GEM instructions with portable skills. "
                "Spec: agentskills.io (Apache-2.0, 20k+ stars)."
            )},
            {"type": "callout", "title": f"Comment {m['cta']}", "text": "Portable skill templates inside."},
        ],
        [
            {"type": "heading", "text": "The four-config problem"},
            {"type": "prose", "text": (
                "Teams maintain PR review logic in four places - drift guaranteed. Agent Skills "
                "packages procedure once: frontmatter trigger + markdown body + scripts/ + references/."
            )},
            {"type": "table", "headers": ["Old", "New"], "rows": [
                [".cursor/rules", "skills/pr-review/SKILL.md"],
                ["CLAUDE.md walls of text", "skills/ + thin CLAUDE.md pointer"],
                ["Codex instructions", "Same skill folder"],
                ["Gemini GEM", "Same skill folder"],
            ]},
        ],
        [
            {"type": "heading", "text": "SKILL.md anatomy"},
            {"type": "table", "headers": ["Field", "Rule"], "rows": [
                ["name", "max 64 chars, lowercase-hyphen"],
                ["description", "max 1024 - THIS is the trigger"],
                ["body", "under 5000 tokens recommended"],
                ["scripts/", "optional executable helpers"],
                ["references/", "tone, policy, examples on demand"],
            ]},
            {"type": "code", "text": (
                "Validate:\n"
                "git clone https://github.com/agentskills/agentskills\n"
                "cd agentskills/skills-ref && pip install -e .\n"
                "skills-ref validate ./my-skill"
            )},
        ],
        [
            {"type": "heading", "text": "Template: PR review"},
            {"type": "code", "text": (
                "---\n"
                "name: pr-review\n"
                "description: Review PR diffs for tests, security, breaking changes. Use on PR or merge request.\n"
                "---\n\n"
                "## Output format\n"
                "- Scope summary\n"
                "- Breaking changes (yes/no + detail)\n"
                "- Test coverage mention\n"
                "- Security smells\n"
                "- Verdict: approve | request changes\n"
                "NEVER auto-merge."
            )},
            {"type": "prose", "text": "Install: copy folder to ~/.claude/skills/pr-review and .cursor/skills/pr-review"},
        ],
        [
            {"type": "heading", "text": "Template: Invoice draft"},
            {"type": "code", "text": (
                "---\n"
                "name: invoice-draft\n"
                "description: Draft QuickBooks-ready invoices from CSV or email. Finance ops only.\n"
                "---\n\n"
                "## Steps\n"
                "1. Parse line items from references/line-item-format.md\n"
                "2. Apply tax rules from references/tax-rules.md\n"
                "3. Output QB-ready JSON draft\n"
                "4. Tag [REVIEW] - never sync to QuickBooks without APPROVE"
            )},
        ],
        [
            {"type": "heading", "text": "Template: Caption QA (UGC)"},
            {"type": "code", "text": (
                "---\n"
                "name: caption-qa\n"
                "description: QA Meta ad captions for hook, CTA, compliance. Use on UGC batches.\n"
                "---\n\n"
                "## Score 0-100\n"
                "- Hook under 125 chars\n"
                "- CTA clarity\n"
                "- No unsubstantiated claims\n"
                "- Hashtag cap <= 5\n"
                "Output: score + fix list per caption"
            )},
        ],
        [
            {"type": "heading", "text": "GitHub gems + marketplaces"},
            {"type": "table", "headers": ["Source", "What"], "rows": [
                ["agentskills/agentskills", "Canonical spec + validator"],
                ["anthropics/skills", "PowerPoint, Excel, PDF skills + examples"],
                ["skills.sh", "Curated install CLI"],
                ["SkillsMP", "400k+ skills, semantic search"],
                ["ComposioHQ/awesome-claude-skills", "78 SaaS workflows"],
            ]},
            {"type": "bullets", "title": "Pro moves", "items": [
                "Git repo for all skills - version like code",
                "description field A/B test - it's your trigger",
                "Progressive disclosure: keep SKILL.md under 200 lines",
                "allowed-tools field (experimental) for pre-approved MCP tools",
            ]},
        ],
        [
            {"type": "heading", "text": "7-day portability test"},
            {"type": "table", "headers": ["Day", "Action"], "rows": [
                ["1", "Pick top repeated workflow"],
                ["2", "Write SKILL.md + references/"],
                ["3", "Install Claude Code path"],
                ["4", "Install Cursor path"],
                ["5", "Run same prompt both tools - compare"],
                ["6", "Delete duplicate rules if parity holds"],
                ["7", "Document in team wiki"],
            ]},
        ],
        [
            {"type": "heading", "text": "Failure modes"},
            {"type": "table", "headers": ["Issue", "Fix"], "rows": [
                ["Skill too long", "Move detail to references/"],
                ["Never triggers", "Rewrite description - be specific"],
                ["Tool ignores skill", "Check install path per product docs"],
                ["Secrets in skill", "Move to MCP env, not markdown"],
            ]},
        ],
        [
            {"type": "heading", "text": "Skills checklist"},
            {"type": "bullets", "items": [
                "3 templates copied and customized",
                "skills-ref validate passes",
                "Installed in 2+ tools with parity test",
                "Old duplicate configs removed",
            ]},
            _img(slug),
            {"type": "callout", "title": f"Comment {m['cta']}", "text": f"@piyush.glitch | {m['pdf']}"},
        ],
    ]


def _pages_04(slug: str, m: dict) -> list:
    return [
        [
            {"type": "heading", "text": m["title"]},
            {"type": "subhead", "text": f"@piyush.glitch  |  {m['tag']}"},
            {"type": "prose", "text": (
                "Cloud Agents (formerly Background Agents) run in isolated VMs with browser testing, "
                "parallel execution, and merge-ready PRs. Local Composer = pair. Cloud = ship unattended."
            )},
            {"type": "callout", "title": f"Comment {m['cta']}", "text": "environment.json templates inside."},
        ],
        [
            {"type": "heading", "text": "When Cloud vs Local"},
            {"type": "table", "headers": ["Use Cloud", "Use Local Composer"], "rows": [
                ["Clear issue + acceptance criteria", "Exploratory spike"],
                ["UI needs browser verification", "Architecture debate"],
                ["Parallel dep bumps overnight", "Pairing on hard bug"],
                ["Slack/Linear triggered fix", "Tight feedback loop"],
            ]},
        ],
        [
            {"type": "heading", "text": "environment.json setup"},
            {"type": "prose", "text": (
                "Commit <b>.cursor/environment.json</b> to repo - highest priority over UI wizard snapshots. "
                "Resolution: repo config > personal > team. Schema: cursor.com/schemas/environment.schema.json"
            )},
            {"type": "code", "text": (
                "// .cursor/environment.json (snapshot-based)\n"
                "{\n"
                '  "snapshot": "snapshot-20260212-00000000-0000-0000-0000-000000000000",\n'
                '  "install": "npm ci",\n'
                '  "start": "npm run dev",\n'
                '  "test": "npm test"\n'
                "}"
            )},
        ],
        [
            {"type": "heading", "text": "Dockerfile path"},
            {"type": "code", "text": (
                "// .cursor/environment.json (Dockerfile)\n"
                "{\n"
                '  "dockerfile": "Dockerfile",\n'
                '  "install": "./custom_script.sh",\n'
                '  "terminals": [\n'
                '    {"name": "dev", "command": "npm run dev", "ports": [3000]}\n'
                "  ]\n"
                "}"
            )},
            {"type": "prose", "text": (
                "Do NOT COPY full project in Dockerfile - Cursor checks out commit. "
                "Use Secrets tab in Cursor Settings for env vars (encrypted KMS), not .env.local in snapshots."
            )},
        ],
        [
            {"type": "heading", "text": "Definition of done (PR template)"},
            {"type": "bullets", "items": [
                "Linked issue with acceptance criteria",
                "Test output green in PR description",
                "Screenshots for UI changes",
                "No merge by agent - human review required",
                "Branch named by agent, you squash-merge",
            ]},
            {"type": "code", "text": (
                "Acceptance criteria template:\n"
                "- [ ] Unit tests pass\n"
                "- [ ] E2E: login flow works in browser\n"
                "- [ ] No new eslint errors\n"
                "- [ ] Screenshot attached for /checkout change"
            )},
        ],
        [
            {"type": "heading", "text": "Triggers: Slack + Linear"},
            {"type": "prose", "text": (
                "Mention @cursor on Slack thread with issue link. Assign Linear issue to Cloud Agent. "
                "Schedule nightly cron for dependency bumps. Parallel runs for independent tasks."
            )},
            {"type": "bullets", "title": "Spend controls", "items": [
                "Set per-run spend limit in dashboard",
                "Require green CI before merge",
                "Cap parallel agents per repo",
                "Review agent-created branches weekly",
            ]},
        ],
        [
            {"type": "heading", "text": "Cloud Agents API (beta)"},
            {"type": "prose", "text": (
                "Programmatic launch via cursor.com/docs/cloud-agent/api. envVars (max 50) injected "
                "encrypted per session. Use for CI-triggered fixes from failed builds."
            )},
            {"type": "code", "text": (
                "# Trigger from CI (conceptual)\n"
                "curl -X POST https://api.cursor.com/v0/agents \\\n"
                '  -d \'{"prompt":"Fix flaky test in auth.spec.ts", "repo":"org/repo"}\''
            )},
        ],
        [
            {"type": "heading", "text": "Launch checklist"},
            {"type": "table", "headers": ["Step", "Done?"], "rows": [
                ["Write acceptance criteria in issue", ""],
                ["Add .cursor/environment.json", ""],
                ["Set spend limit", ""],
                ["Test dry-run on small issue", ""],
                ["Human review before merge", ""],
            ]},
        ],
        [
            {"type": "heading", "text": "Failure modes"},
            {"type": "table", "headers": ["Issue", "Fix"], "rows": [
                ["PR missing tests", "Add test cmd to environment.json"],
                ["Wrong Node version", "Pin snapshot or Dockerfile base"],
                ["Scope creep", "Router issue - criteria only"],
                ["Privacy mode blocks cloud", "Enable limited retention for cloud features"],
            ]},
        ],
        [
            {"type": "heading", "text": "Cloud checklist"},
            _img(slug),
            {"type": "callout", "title": f"Comment {m['cta']}", "text": f"@piyush.glitch | {m['pdf']}"},
        ],
    ]


def _pages_05(slug: str, m: dict) -> list:
    return [
        [
            {"type": "heading", "text": m["title"]},
            {"type": "subhead", "text": f"@piyush.glitch  |  {m['tag']}"},
            {"type": "prose", "text": (
                "Workspace Agents evolve Custom GPTs into <b>team infrastructure</b>: shared ownership, "
                "scheduled cloud runs, connectors (Slack, Salesforce, Google), admin controls, Compliance API."
            )},
            {"type": "callout", "title": f"Comment {m['cta']}", "text": "Migration matrix inside."},
        ],
        [
            {"type": "heading", "text": "GPT vs Workspace Agent"},
            {"type": "table", "headers": ["Custom GPT", "Workspace Agent"], "rows": [
                ["Solo user", "Team shared"],
                ["Manual run", "Scheduled cron"],
                ["No connectors", "Slack, SF, Drive live data"],
                ["No audit", "Admin + Compliance API"],
            ]},
            {"type": "prose", "text": (
                "<b>Migrate when:</b> output goes to clients OR runs on schedule. "
                "<b>Keep GPT when:</b> personal drafts only."
            )},
        ],
        [
            {"type": "heading", "text": "Build: weekly client report agent"},
            {"type": "bullets", "title": "Steps", "items": [
                "Define data sources (Salesforce + Drive)",
                "Write output template (Slack block format)",
                "Set schedule Monday 8am",
                "Enable human review before Slack post",
                "Dry-run with last week's data",
            ]},
            {"type": "code", "text": (
                "Output template:\n"
                "## Weekly Client Report - {client}\n"
                "Pipeline delta | Risks | 3 actions\n"
                "Sources: SF opportunities + Drive contract folder"
            )},
        ],
        [
            {"type": "heading", "text": "Connectors setup"},
            {"type": "table", "headers": ["Connector", "Read-first use"], "rows": [
                ["Slack", "Post digest to #channel after review"],
                ["Salesforce", "Pull pipeline + activity"],
                ["Google Drive", "Read client folders"],
                ["SharePoint", "Policy docs for agent context"],
            ]},
            {"type": "callout", "title": "HITL rule", "text": "Draft emails and CRM updates pause for reviewer. Enterprise: audit log + Compliance API."},
        ],
        [
            {"type": "heading", "text": "Admin controls"},
            {"type": "bullets", "items": [
                "Role-based: who can create vs run agents",
                "Tool allowlist per agent (not org-wide)",
                "Approval step for external sends",
                "Log: user, prompt, tool call, output",
            ]},
        ],
        [
            {"type": "heading", "text": "Dev path: Responses API + Agents SDK"},
            {"type": "prose", "text": (
                "Business teams use Workspace UI. Developers use Responses API + Agents SDK for custom "
                "orchestration. Assistants API is fading - migrate to Agents SDK for new builds."
            )},
        ],
        [
            {"type": "heading", "text": "High-value team workflows"},
            {"type": "table", "headers": ["Workflow", "ROI"], "rows": [
                ["Weekly pipeline report", "Saves 2h/week per AE"],
                ["Customer-risk digest", "CSM early churn signal"],
                ["PR triage summary", "Eng manager morning scan"],
                ["Support macro audit", "QA consistency"],
            ]},
        ],
        [
            {"type": "heading", "text": "4-week migration"},
            {"type": "table", "headers": ["Week", "Task"], "rows": [
                ["1", "Inventory Custom GPTs used by 2+ people"],
                ["2", "Promote top GPT to Workspace Agent read-only"],
                ["3", "Add schedule + Slack delivery"],
                ["4", "Enable review gate + audit logging"],
            ]},
        ],
        [
            {"type": "heading", "text": "Failure modes"},
            {"type": "table", "headers": ["Issue", "Fix"], "rows": [
                ["Agent sent without review", "Enable review step"],
                ["Stale connector", "Re-auth + proof prompt"],
                ["Team forked GPT versions", "Consolidate to one agent"],
            ]},
        ],
        [
            {"type": "heading", "text": "Agents checklist"},
            _img(slug),
            {"type": "callout", "title": f"Comment {m['cta']}", "text": f"@piyush.glitch | {m['pdf']}"},
        ],
    ]


def _pages_06(slug: str, m: dict) -> list:
    return [
        [
            {"type": "heading", "text": m["title"]},
            {"type": "subhead", "text": f"@piyush.glitch  |  {m['tag']}"},
            {"type": "prose", "text": (
                "Workspace Studio (GA 2026) builds agentic flows across Gmail, Drive, Sheets - no code. "
                "<b>Ask a Gem</b> step (April 2026) puts your trained Gems inside flows - brand voice, "
                "policy rubrics - not just chat sidebar."
            )},
            {"type": "callout", "title": f"Comment {m['cta']}", "text": "5 flow walkthroughs inside."},
        ],
        [
            {"type": "heading", "text": "Prerequisites"},
            {"type": "bullets", "items": [
                "Admin: Gemini for Google Workspace enabled",
                "Gmail smart features on",
                "Gems must use Drive files in knowledge base (not Photos-only)",
                "Promo: higher Studio limits through June 1, 2026",
            ]},
        ],
        [
            {"type": "heading", "text": "Flow 1: Urgent email triage"},
            {"type": "prose", "text": "Trigger: urgent label applied -> Gem classifies severity -> draft reply -> route to owner"},
            {"type": "code", "text": (
                "Ask a Gem prompt:\n"
                "Classify this email: P0 (respond 1h), P1 (today), P2 (this week).\n"
                "Draft reply using support-voice Gem. Do not send - save draft only."
            )},
        ],
        [
            {"type": "heading", "text": "Flow 2: Form lead to sales"},
            {"type": "prose", "text": "Google Form submit -> Gem scores fit 0-100 -> Sheets row -> Gmail draft for sales"},
            {"type": "bullets", "items": [
                "Gem: lead-scoring (trained on 20 gold leads)",
                "Sheet columns: score, fit_reason, draft_subject",
                "Human approves send from Gmail draft",
            ]},
        ],
        [
            {"type": "heading", "text": "Flow 3-4: Meetings + attachments"},
            {"type": "prose", "text": (
                "<b>Meeting actions:</b> calendar end -> extract action items -> Sheet tab.<br/>"
                "<b>Attachments:</b> Gmail watch folder -> auto-file to Drive by client name."
            )},
        ],
        [
            {"type": "heading", "text": "Flow 5: Policy review"},
            {"type": "prose", "text": (
                "New doc in Drive folder -> Ask policy Gem -> flag compliance issues -> "
                "Chat alert to legal channel. Gem trained on policy PDFs in Drive."
            )},
        ],
        [
            {"type": "heading", "text": "Gem design tips"},
            {"type": "bullets", "items": [
                "10 gold examples in Gem instructions",
                "Knowledge: Drive PDFs/Docs only for Studio compatibility",
                "Test with Test run before Turn on",
                "Add human approval step before any Gmail send",
            ]},
        ],
        [
            {"type": "heading", "text": "Admin rollout"},
            {"type": "table", "headers": ["Week", "Flow"], "rows": [
                ["1", "Urgent triage read-only"],
                ["2", "Form lead scoring"],
                ["3", "Meeting actions"],
                ["4", "Attachment filing + policy review"],
            ]},
        ],
        [
            {"type": "heading", "text": "Failure modes"},
            {"type": "table", "headers": ["Issue", "Fix"], "rows": [
                ["Gem not in Studio", "Add Drive files to knowledge base"],
                ["Flow sent without approve", "Insert explicit human step"],
                ["Wrong tone", "Retrain Gem with 10 examples"],
            ]},
        ],
        [
            {"type": "heading", "text": "Studio checklist"},
            _img(slug),
            {"type": "callout", "title": f"Comment {m['cta']}", "text": f"@piyush.glitch | {m['pdf']}"},
        ],
    ]


def _pages_07(slug: str, m: dict) -> list:
    return [
        [
            {"type": "heading", "text": m["title"]},
            {"type": "subhead", "text": f"@piyush.glitch  |  {m['tag']}"},
            {"type": "prose", "text": (
                "Meta's 2026 auction is <b>creative-first</b> (Andromeda retrieval). Advantage+ rewards "
                "30-200 active variants, 2-3 week refresh, hook-level testing. 70-90% of variant volume "
                "can be AI UGC; 2-4 hero creator spots per quarter anchor trust."
            )},
            {"type": "callout", "title": f"Comment {m['cta']}", "text": "Hook bible + matrix inside."},
        ],
        [
            {"type": "heading", "text": "Variant volume by spend"},
            {"type": "table", "headers": ["Monthly spend", "Active variants"], "rows": [
                ["$10k-$50k", "15-30"],
                ["$50k-$250k", "40-80"],
                ["$250k+", "100-250"],
            ]},
            {"type": "prose", "text": "Minimum rotation: 20-30 distinct assets, refreshed every 2-3 weeks."},
        ],
        [
            {"type": "heading", "text": "Hook bible (0-3 seconds)"},
            {"type": "table", "headers": ["Pattern", "Open"], "rows": [
                ["Question", "Did you know...?"],
                ["Negative", "Stop doing X"],
                ["POV", "POV: you finally..."],
                ["Demo-first", "Watch this transform"],
                ["Before/after", "Split reveal"],
                ["Founder rant", "I need to tell you..."],
            ]},
            {"type": "callout", "title": "Primary metric", "text": "Hook rate (% past 3s). Pause below 25% within 72h."},
        ],
        [
            {"type": "heading", "text": "Variant matrix"},
            {"type": "prose", "text": "Test grid: hook x format x CTA. True diversity = different claims, messengers, formats - not same ad with different backgrounds."},
            {"type": "table", "headers": ["Axis", "Options"], "rows": [
                ["Hook", "6 patterns above"],
                ["Format", "Reels 9:16, static 1:1, carousel"],
                ["CTA", "Shop now, Learn more, Get offer"],
                ["Messenger", "Founder, creator, AI character, customer"],
            ]},
        ],
        [
            {"type": "heading", "text": "Three creative tiers"},
            {"type": "table", "headers": ["Tier", "Role", "Volume"], "rows": [
                ["1 Hero", "Brand anthem, founder story", "2-4/quarter"],
                ["2 Mid UGC", "Creator partnerships", "20% of library"],
                ["3 AI long tail", "Identity-locked variants", "70-90%"],
            ]},
        ],
        [
            {"type": "heading", "text": "Tagging schema (Sheet)"},
            {"type": "code", "text": (
                "Columns:\n"
                "asset_id | hook_type | format | cta | angle | messenger | week_live | spend | roas | hook_rate\n\n"
                "Refresh: new batch every 14d | postmortem at 21d\n"
                "Add 3-5 variants every few days - avoid learning phase shock"
            )},
        ],
        [
            {"type": "heading", "text": "ASC bundle strategy"},
            {"type": "bullets", "items": [
                "Bundle 30-50 variants in one ASC campaign",
                "Use DCO inside ASC for hook x voiceover assembly",
                "Upload all aspect ratios: 9:16, 1:1, 16:9",
                "Cull bottom quartile weekly, scale top quartile",
                "Brand kit in Advantage+ Creative for AI variant consistency",
            ]},
        ],
        [
            {"type": "heading", "text": "Production calendar"},
            {"type": "table", "headers": ["Day", "Task"], "rows": [
                ["Mon", "Review hook rates, kill <25%"],
                ["Wed", "Ship 5 new variants"],
                ["Fri", "Tag + upload to ASC"],
                ["Biweekly", "Full pool refresh"],
            ]},
        ],
        [
            {"type": "heading", "text": "Failure modes"},
            {"type": "table", "headers": ["Issue", "Fix"], "rows": [
                ["One hero ad fatigue", "Increase variant volume"],
                ["Fake diversity", "Test different claims not colors"],
                ["No tagging", "Cannot learn winners - add schema"],
            ]},
        ],
        [
            {"type": "heading", "text": "UGC OS checklist"},
            _img(slug),
            {"type": "callout", "title": f"Comment {m['cta']}", "text": f"@piyush.glitch | {m['pdf']}"},
        ],
    ]


def _pages_08(slug: str, m: dict) -> list:
    return [
        [
            {"type": "heading", "text": m["title"]},
            {"type": "subhead", "text": f"@piyush.glitch  |  {m['tag']}"},
            {"type": "prose", "text": (
                "Connect MCP for a <b>job</b> - not a readme binge. Core five: filesystem, GitHub, GSC, "
                "GA4, HubSpot. Add Obsidian (memory) + n8n (schedule)."
            )},
            {"type": "callout", "title": f"Comment {m['cta']}", "text": "Proof prompts per job inside."},
        ],
        [
            {"type": "heading", "text": "Job 1: SEO weekly report"},
            {"type": "table", "headers": ["MCP", "Role"], "rows": [
                ["GSC", "Query/page performance"],
                ["GA4", "Landing page traffic"],
                ["filesystem", "Draft report output"],
            ]},
            {"type": "code", "text": (
                "Proof prompt:\n"
                "List top 10 GSC queries down 20%+ clicks WoW.\n"
                "Cross-reference GA4 landing pages for same URLs.\n"
                "Output markdown report in ./reports/seo-weekly.md"
            )},
        ],
        [
            {"type": "heading", "text": "Job 2: Pipeline follow-up"},
            {"type": "table", "headers": ["MCP", "Role"], "rows": [
                ["HubSpot mcp.hubspot.com", "Stale deals"],
                ["Gmail MCP", "Draft nudges"],
            ]},
            {"type": "code", "text": (
                "Proof prompt:\n"
                "HubSpot: deals no activity 14+ days, amount > $500.\n"
                "Draft 3 email variants per deal. [REVIEW] only."
            )},
        ],
        [
            {"type": "heading", "text": "Job 3: Content refresh alert"},
            {"type": "prose", "text": "GSC declining pages -> Obsidian refresh brief template -> n8n Monday trigger"},
            {"type": "code", "text": (
                "n8n cron: Monday 7am -> trigger Claude with GSC+Obsidian MCP\n"
                "Output: pages to refresh ranked by click loss"
            )},
        ],
        [
            {"type": "heading", "text": "Auth gotchas"},
            {"type": "bullets", "items": [
                "OAuth minimum scopes - read before write",
                "HubSpot: mcp.hubspot.com OAuth OR @hubspot/mcp-server private app token",
                "Never log tokens in repo",
                "Separate read credentials from write credentials",
                "One proof prompt per server before production",
            ]},
        ],
        [
            {"type": "heading", "text": "GitHub discovery"},
            {"type": "table", "headers": ["Repo", "Use"], "rows": [
                ["matthiastjong/awesome-mcp", "Daily-ranked server list"],
                ["modelcontextprotocol/servers", "Official reference servers"],
                ["baryhuang/mcp-hubspot", "Community HubSpot (122 stars)"],
                ["robotic-pixels/marketing-skills", "GA4+HubSpot morning briefing"],
                ["github/github-mcp-server", "PR, issues, code search"],
            ]},
        ],
        [
            {"type": "heading", "text": "Claude Desktop config snippet"},
            {"type": "code", "text": (
                '{\n'
                '  "mcpServers": {\n'
                '    "filesystem": {\n'
                '      "command": "npx",\n'
                '      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed"]\n'
                "    },\n"
                '    "hubspot": { "url": "https://mcp.hubspot.com" }\n'
                "  }\n"
                "}"
            )},
        ],
        [
            {"type": "heading", "text": "Read-first week plan"},
            {"type": "table", "headers": ["Day", "Server", "Proof"], "rows": [
                ["1", "filesystem", "List project files"],
                ["2", "GitHub", "List open PRs"],
                ["3", "GSC", "Top queries last 7d"],
                ["4", "GA4", "Sessions by landing page"],
                ["5", "HubSpot", "Deal count by stage"],
            ]},
        ],
        [
            {"type": "heading", "text": "Failure modes"},
            {"type": "table", "headers": ["Issue", "Fix"], "rows": [
                ["Too many servers day 1", "One job stack only"],
                ["Hallucinated data", "Require tool trace in output"],
                ["Write too early", "Read-first week policy"],
            ]},
        ],
        [
            {"type": "heading", "text": "MCP checklist"},
            _img(slug),
            {"type": "callout", "title": f"Comment {m['cta']}", "text": f"@piyush.glitch | {m['pdf']}"},
        ],
    ]


def _pages_09(slug: str, m: dict) -> list:
    return [
        [
            {"type": "heading", "text": m["title"]},
            {"type": "subhead", "text": f"@piyush.glitch  |  {m['tag']}"},
            {"type": "prose", "text": (
                "Router plans (no tools). Worker executes (MCP + Skills). Reviewer gates ([REVIEW] or [SHIP]). "
                "Same pattern in Claude subagents, OpenAI handoffs, Cursor parallel agents."
            )},
            {"type": "callout", "title": f"Comment {m['cta']}", "text": "Copy-paste roles inside."},
        ],
        [
            {"type": "heading", "text": "Role boundaries"},
            {"type": "table", "headers": ["Role", "Tools?", "Output"], "rows": [
                ["Router", "No", "Plan + acceptance criteria"],
                ["Worker", "Yes", "Draft artifact"],
                ["Reviewer", "Read-only", "[REVIEW] or [SHIP]"],
            ]},
        ],
        [
            {"type": "heading", "text": "Router system prompt"},
            {"type": "code", "text": (
                "You are Router. You PLAN only - never call tools.\n"
                "Output JSON:\n"
                "  tasks: []\n"
                "  tools_needed: []\n"
                "  acceptance_criteria: []\n"
                "  out_of_scope: []\n"
                "Stop scope creep before tokens burn."
            )},
        ],
        [
            {"type": "heading", "text": "Worker system prompt"},
            {"type": "code", "text": (
                "You are Worker. Execute Router plan exactly.\n"
                "Use MCP + Skills. Produce draft artifact.\n"
                "NEVER send externally. NEVER replan.\n"
                "If blocked, return BLOCKED: reason"
            )},
        ],
        [
            {"type": "heading", "text": "Reviewer system prompt"},
            {"type": "code", "text": (
                "You are Reviewer. Check facts, tone, PII, policy.\n"
                "Verify acceptance_criteria from Router.\n"
                "Tag [REVIEW] with risk:low|med|high OR [SHIP].\n"
                "Bounce to Worker with diffs if fail."
            )},
        ],
        [
            {"type": "heading", "text": "Example: client weekly report"},
            {"type": "prose", "text": (
                "Router: define sections + GA4/GSC sources. Worker: MCP pull + draft PDF. "
                "Reviewer: verify numbers match source, client-safe tone -> [SHIP]."
            )},
            {"type": "bullets", "items": [
                "Router output saved as plan.json",
                "Worker attaches tool traces",
                "Reviewer checklist: 8 items",
            ]},
        ],
        [
            {"type": "heading", "text": "Paste into CLAUDE.md"},
            {"type": "code", "text": (
                "## Multi-agent protocol\n"
                "1. User request -> Router only\n"
                "2. Router plan -> Worker only\n"
                "3. Worker draft -> Reviewer only\n"
                "4. [SHIP] -> user delivery\n"
                "Roles must not bleed."
            )},
        ],
        [
            {"type": "heading", "text": "Productivity gains"},
            {"type": "bullets", "items": [
                "Cuts drift - Worker cannot expand scope",
                "Safer writes - Reviewer always gates",
                "Cheaper - Router uses smaller model ok",
                "Parallel Workers for independent subtasks",
                "Audit trail: plan -> draft -> decision",
            ]},
        ],
        [
            {"type": "heading", "text": "Failure modes"},
            {"type": "table", "headers": ["Bleed", "Fix"], "rows": [
                ["Router calls tools", "Re-prompt: plan only"],
                ["Worker replans", "Freeze to Router JSON"],
                ["Reviewer rubber-stamps", "Mandatory checklist"],
            ]},
        ],
        [
            {"type": "heading", "text": "Workflow checklist"},
            _img(slug),
            {"type": "callout", "title": f"Comment {m['cta']}", "text": f"@piyush.glitch | {m['pdf']}"},
        ],
    ]


def _pages_10(slug: str, m: dict) -> list:
    return [
        [
            {"type": "heading", "text": m["title"]},
            {"type": "subhead", "text": f"@piyush.glitch  |  {m['tag']}"},
            {"type": "prose", "text": (
                "Agents can email, pay, post. Governance = trust infrastructure: [REVIEW] protocol, "
                "read-first MCP, hard-blocked tools, audit logs, printable 1-page team policy."
            )},
            {"type": "callout", "title": f"Comment {m['cta']}", "text": "Printable policy on page 7."},
        ],
        [
            {"type": "heading", "text": "Why governance now"},
            {"type": "prose", "text": (
                "Cowork, Workspace Agents, MCP writes are powerful. SMB owners need approval, audit, "
                "Compliance API - not fear-driven bans on AI."
            )},
            {"type": "table", "headers": ["Action", "Default policy"], "rows": [
                ["Single email draft", "[REVIEW] required"],
                ["Bulk email", "Hard-block auto"],
                ["Payment", "Two-person rule"],
                ["Social post", "[REVIEW] + brand check"],
                ["CRM mass update", "Hard-block auto"],
            ]},
        ],
        [
            {"type": "heading", "text": "[REVIEW] protocol"},
            {"type": "code", "text": (
                "[REVIEW] block (required on external writes):\n"
                "Risk: low | med | high\n"
                "Diff: <what changes>\n"
                "Rollback: <how to undo>\n"
                "Awaiting: APPROVE or edits\n"
                "No implicit consent."
            )},
        ],
        [
            {"type": "heading", "text": "Read-first MCP week"},
            {"type": "bullets", "items": [
                "Day 1-7: list and fetch only",
                "Proof prompt per server before write scopes",
                "Log every tool call during week 1",
                "Week 2: draft-only writes",
                "Week 3+: explicit APPROVE on sends",
            ]},
        ],
        [
            {"type": "heading", "text": "Hard-blocked tool classes"},
            {"type": "bullets", "items": [
                "Payments and refunds",
                "Bulk email (>5 recipients)",
                "Social publish APIs",
                "CRM mass update/delete",
                "DNS / infra production changes",
            ]},
            {"type": "callout", "title": "Config level", "text": "Block at MCP tool config - not prompt-only."},
        ],
        [
            {"type": "heading", "text": "Audit log minimum"},
            {"type": "table", "headers": ["Field", "Required"], "rows": [
                ["timestamp", "yes"],
                ["user / approver", "yes"],
                ["prompt hash", "yes"],
                ["tools called", "yes"],
                ["output summary", "yes"],
                ["decision APPROVE/REJECT", "yes"],
            ]},
        ],
        [
            {"type": "heading", "text": "One-page team policy (print)"},
            {"type": "code", "text": (
                "AGENT POLICY - @piyush.glitch template\n"
                "1. Default [REVIEW] on all external writes\n"
                "2. Week 1 MCP read-only for new servers\n"
                "3. BLOCKED: payments, bulk email, social auto-post\n"
                "4. $1000+ needs second human approver\n"
                "5. Log: prompt, tools, output, approver, time\n"
                "6. Monthly sample audit (10 random actions)"
            )},
        ],
        [
            {"type": "heading", "text": "Enterprise additions"},
            {"type": "bullets", "items": [
                "OpenAI Compliance API for regulated teams",
                "SOC2-aligned retention on audit logs",
                "Role-based connector scopes per department",
                "Quarterly red-team on agent write paths",
            ]},
        ],
        [
            {"type": "heading", "text": "Failure modes"},
            {"type": "table", "headers": ["Incident", "Response"], "rows": [
                ["Silent send", "Revoke write scope + postmortem"],
                ["No audit trail", "Add logging middleware immediately"],
                ["Read+write day 1", "Reset to read-first week"],
            ]},
        ],
        [
            {"type": "heading", "text": "SAFE checklist"},
            {"type": "bullets", "items": [
                "[REVIEW] in all agent instructions",
                "Blocked tools configured",
                "Audit log live",
                "1-page policy signed by team",
                "Read-first week completed for new MCP",
            ]},
            _img(slug),
            {"type": "callout", "title": f"Comment {m['cta']}", "text": f"@piyush.glitch | {m['pdf']}"},
        ],
    ]
