# -*- coding: utf-8 -*-
"""Rich PDF content for Claude carousels 11-15. Merged into pdf_content + expand_pdf_content."""

BATCH2_CONTENT = {
    "11_Claude_Projects_For_Teams": {
        "title": "Claude Projects as Team Memory",
        "subtitle": "Stop re-uploading context. Build one shared brain per workflow.",
        "kicker": "AI FOR BUSINESS - 11",
        "intro": (
            "Claude Projects (claude.ai, Pro/Team/Enterprise) are persistent workspaces: custom instructions "
            "plus uploaded knowledge files (~200K tokens total) that load automatically in every chat inside "
            "the project. Most teams use Projects like folders. Operators use them like onboarded teammates - "
            "with role-specific instructions, curated file sets, starter prompts, and shared access so marketing, "
            "ops and founders stop pasting the same PDFs into new chats every Monday."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "What Projects actually store",
                "body": [
                    "Three layers persist: (1) Project instructions - your standing system prompt for tone, format, "
                    "forbidden actions and output templates. (2) Project knowledge - PDFs, CSVs, MD, code files "
                    "Claude retrieves without re-upload. (3) Conversation history within the project - searchable "
                    "continuity for decisions already made.",
                    "Unlike API system prompts, Projects are no-code and survive session restarts. Unlike plain "
                    "chat, they enforce the same rules for every teammate who joins the project.",
                ],
                "bullets": [
                    ("Instructions", "Persona, voice, citation rules, approval language, output schemas."),
                    ("Knowledge", "Brand guide, pricing CSV, PRD, FAQ, exemplar outputs, glossary."),
                    ("Sharing", "Team/Enterprise: invite colleagues; everyone inherits same context."),
                ],
            },
            {
                "tab": "02",
                "title": "Instructions that work on first deploy",
                "body": [
                    "Structure instructions in four blocks: WHO (role), RULES (always/never), FORMAT (headings, "
                    "length, tables), ESCALATE (when to say 'needs human review'). Keep under 1,500 words - "
                    "longer instructions get partially ignored under pressure.",
                ],
                "bullets": [
                    ("Always", "Cite which uploaded file each claim comes from when using knowledge."),
                    ("Never", "Invent pricing, legal claims, or customer names not in knowledge files."),
                    ("Format", "Exec summary first, then detail, then next actions with owners."),
                ],
            },
            {
                "tab": "03",
                "title": "Knowledge file strategy",
                "body": [
                    "Upload fewer, better files. One messy 400-page dump confuses retrieval. Prefer: brand-voice.md, "
                    "product-faq.md, pricing.csv, competitor-notes.md, approved-email-examples.md.",
                    "Refresh cadence: pricing monthly, brand quarterly, exemplars when you ship something great.",
                ],
            },
        ],
        "playbook": [
            "Create project named by outcome ('Q2 Launch Copy') not tool ('Claude').",
            "Write instructions using WHO/RULES/FORMAT/ESCALATE template.",
            "Upload 5-8 curated files; delete outdated versions from project.",
            "Pin 3 starter prompts in project description for teammates.",
            "Run 10 test queries; fix instructions when Claude drifts twice on same failure.",
            "Invite team; assign one 'project owner' to approve instruction changes.",
            "Weekly: export one great answer to exemplars/ folder in knowledge.",
        ],
        "mistakes": [
            "Dumping entire Google Drive into knowledge - retrieval quality collapses.",
            "Instructions that say 'be helpful' with no format or boundaries.",
            "One mega-project for unrelated workflows - split by outcome.",
            "Never updating files after pricing or policy changes.",
            "Letting every teammate edit instructions without version notes.",
        ],
        "glossary": [
            ("Project instructions", "Persistent system prompt for all chats in a Project."),
            ("Project knowledge", "Uploaded files Claude can reference across sessions."),
            ("200K token budget", "Approximate total knowledge capacity across all project files."),
            ("Starter prompt", "Pinned example query teammates clone instead of writing from scratch."),
        ],
        "callout": {
            "title": "Hidden power move",
            "text": "Upload three 'gold standard' outputs as knowledge with filenames EXAMPLE-good-email.md "
                    "- instruct Claude to match structure and density, not wording. This beats paragraphs "
                    "of style advice.",
        },
    },
    "12_Claude_Artifacts_For_Business": {
        "title": "Claude Artifacts for Deliverables",
        "subtitle": "Side-panel outputs you can edit, share and ship - not just chat paragraphs.",
        "kicker": "AI FOR BUSINESS - 12",
        "intro": (
            "Artifacts are Claude's dedicated output window for substantial content: documents, React components, "
            "SVG diagrams, HTML pages, Mermaid charts and interactive tools. They appear beside chat, update "
            "in place when you iterate, and export without copy-paste hell. For business teams, Artifacts turn "
            "Claude from a drafting chatbot into a lightweight production surface for internal tools, client "
            "deliverables and campaign assets."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "When Claude creates an Artifact",
                "body": [
                    "Claude opens an Artifact when output is self-contained and useful outside the chat - "
                    "typically >15 lines, structured, or interactive. You can force it: 'Put the full deliverable "
                    "in an Artifact; chat only for questions.'",
                    "Enable in Settings > Capabilities > Artifacts (on by default for Pro). Artifacts support "
                    "live preview for HTML/React and export for docs.",
                ],
                "bullets": [
                    ("Documents", "Policies, proposals, SOPs - editable side panel."),
                    ("Mini apps", "ROI calculators, configurators, dashboards in React/HTML."),
                    ("Visuals", "Diagrams, flowcharts, SVG infographics."),
                ],
            },
            {
                "tab": "02",
                "title": "Artifact + Project combo",
                "body": [
                    "Run Artifacts inside a Project so instructions and knowledge shape the Artifact: brand colors "
                    "in CSS variables, legal disclaimers from uploaded policy, data columns from pricing.csv.",
                    "Save final Artifacts to project knowledge as new exemplars - your library compounds.",
                ],
            },
            {
                "tab": "03",
                "title": "Iteration protocol",
                "body": [
                    "Never accept v1. Use versioned requests: 'Artifact v2: tighten intro, add table, keep layout.' "
                    "Claude updates the same Artifact instead of spawning duplicates.",
                    "For client work, snapshot v-final to PDF before asking experimental v3 changes.",
                ],
            },
        ],
        "playbook": [
            "Open Project with brand instructions + CSS token file in knowledge.",
            "Prompt: 'Build [deliverable] as Artifact; chat stays minimal.'",
            "Review preview; request v2/v3 with numbered change list.",
            "Export or copy Artifact source to repo / Notion / Google Docs.",
            "Archive approved Artifact in project knowledge as template.",
        ],
        "mistakes": [
            "Letting long deliverables stay in chat stream - hard to edit and export.",
            "No Project instructions - Artifacts ignore brand system.",
            "Asking for Artifact + 10 pages in chat simultaneously - split tasks.",
            "Shipping v1 because 'AI wrote it' - always one structured revision pass.",
        ],
        "glossary": [
            ("Artifact", "Dedicated Claude output panel for substantial or interactive content."),
            ("Live preview", "Runs HTML/React in sandbox beside chat."),
            ("Artifact v2", "In-place iteration language that prevents duplicate panels."),
        ],
        "callout": {
            "title": "Operator prompt",
            "text": "Create an Artifact-only ROI calculator: inputs ARR, churn, CAC; outputs LTV:CAC and payback "
                    "months; use our brand CSS variables from knowledge; no external libraries; mobile-friendly.",
        },
    },
    "13_Claude_MCP_For_Operators": {
        "title": "Claude MCP for Business Ops",
        "subtitle": "Live connectors so Claude reads and acts on real systems - not stale exports.",
        "kicker": "AI FOR BUSINESS - 13",
        "intro": (
            "Model Context Protocol (MCP) is Anthropic's open standard for connecting AI to tools - databases, "
            "GitHub, Slack, Notion, Postgres, Google Drive and internal APIs through one interface. Claude Code "
            "and Claude Desktop load MCP servers at session start. The hidden cost: every enabled server consumes "
            "context and tool slots. Elite teams enable fewer than 10 MCPs per project and scope tokens read-only "
            "until workflows prove stable."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "MCP vs copy-paste",
                "body": [
                    "Without MCP, operators export CSVs, paste into chat, and get answers stale by morning. With MCP, "
                    "Claude queries live Postgres, pulls open GitHub PRs, or searches Notion with citations.",
                    "MCP servers run as local or remote processes; Claude discovers tools via JSON schema.",
                ],
                "bullets": [
                    ("Read-first", "Postgres SELECT, GitHub issues read, Drive search - low risk rollout."),
                    ("Write gated", "Slack post, Jira create, GitHub merge - require approval hooks."),
                    ("Context tax", "20+ MCPs can shrink effective context ~40% - curate aggressively."),
                ],
            },
            {
                "tab": "02",
                "title": "Claude Code MCP setup",
                "body": [
                    "Add servers via CLI: claude mcp add <name> or edit .mcp.json in project root. Project-level "
                    "config travels with repo; user-level lives in ~/.claude.json.",
                    "Official docs: modelcontextprotocol.io. Reference configs: github.com/modelcontextprotocol/servers.",
                ],
            },
            {
                "tab": "03",
                "title": "Starter stack for operators",
                "body": [
                    "Week 1: GitHub (read) + filesystem. Week 2: Postgres read-only replica. Week 3: Slack read. "
                    "Week 4: one write action with human approval in loop.",
                ],
            },
        ],
        "playbook": [
            "Inventory top 5 systems you manually export from weekly.",
            "Install one read-only MCP; validate answers against known queries.",
            "Document allowed tools in CLAUDE.md or Project instructions.",
            "Add PreToolUse hook to block writes until eval set passes.",
            "Log MCP tool calls monthly; remove unused servers.",
        ],
        "mistakes": [
            "Enabling every MCP from a blog post on day one.",
            "Production DB write access without read replica first.",
            "No logging of tool calls - impossible to audit mistakes.",
            "Sharing API keys in committed .mcp.json files.",
        ],
        "glossary": [
            ("MCP", "Model Context Protocol - standard connector layer for AI tools."),
            ("Tool schema", "JSON description Claude uses to call MCP functions."),
            ("disabledMcpServers", "Project config to turn off unused servers and save context."),
        ],
        "callout": {
            "title": "Context warning",
            "text": "everything-claude-code repo warns: 20-30 MCPs configured but keep under 10 enabled and "
                    "80 tools active or your 200K window shrinks toward 70K usable tokens.",
        },
    },
    "14_Claude_Sonnet_vs_Opus": {
        "title": "Claude Model Routing",
        "subtitle": "Sonnet for volume. Opus for judgment. Route like you route headcount.",
        "kicker": "AI FOR BUSINESS - 14",
        "intro": (
            "Anthropic's Claude 4.x family splits into fast, cost-efficient Sonnet and deeper Opus tiers. Teams "
            "that use Opus for everything burn budget. Teams that use Sonnet for everything ship subtle errors in "
            "executive memos, contracts and architecture. Routing is an operating policy: classify task by risk, "
            "reversibility, and edit cost - then assign model explicitly in Projects, Claude Code subagents, or API."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "Default routing table",
                "body": [
                    "Sonnet: drafts, summaries, rewrites, data cleanup, first-pass research, bulk codegen, "
                    "support macros, internal notes. Opus: strategy, negotiation, legal/finance precision, "
                    "architecture, novel problems, executive-facing first drafts, complex multi-doc synthesis.",
                ],
                "bullets": [
                    ("Sonnet signals", "Template exists, facts provided, human edits <15 min."),
                    ("Opus signals", "High blast radius, conflicting constraints, audience is board/investor."),
                    ("Escalate", "Sonnet needed 3+ correction rounds - switch thread to Opus with context attached."),
                ],
            },
            {
                "tab": "02",
                "title": "Claude Code subagent routing",
                "body": [
                    "Explore/search subagents on Haiku or Sonnet; builder on Sonnet; security/architecture review "
                    "on Opus. Define model in .claude/agents/*.md YAML frontmatter.",
                ],
            },
            {
                "tab": "03",
                "title": "Measure cost per success",
                "body": [
                    "Track: model, task type, human edit minutes, rework incidents. Optimize for cost per approved "
                    "output, not cheapest API call.",
                ],
            },
        ],
        "playbook": [
            "Tag last 20 tasks with risk level 1-3.",
            "Set Sonnet default in Project; Opus only for level 3 prompts.",
            "Configure explore subagent on fast model in Claude Code.",
            "Weekly review: tasks that escalated - update routing table.",
            "Publish one-page routing cheat sheet for team.",
        ],
        "mistakes": [
            "Opus for 'make this email shorter' - 100x cost for zero quality gain.",
            "Sonnet for investor deck narrative - subtle tone errors cost deals.",
            "No escalation rule - people fight the model instead of switching.",
            "Routing policy in someone's head - not in Project instructions.",
        ],
        "glossary": [
            ("Sonnet", "Balanced Claude tier - speed and cost for volume work."),
            ("Opus", "Highest reasoning tier for complex or high-stakes tasks."),
            ("Haiku", "Fastest/cheapest - explore and classify subtasks."),
        ],
        "callout": {
            "title": "API tip",
            "text": "Use model parameter per request in API; in Claude Code set model per subagent. Never rely "
                    "on default model for mixed-risk workflows.",
        },
    },
    "15_Claude_For_Research_And_Writing": {
        "title": "Claude Research and Writing Ops",
        "subtitle": "Long-context synthesis, citation discipline and exec-ready prose.",
        "kicker": "AI FOR BUSINESS - 15",
        "intro": (
            "Claude's long context window and careful prose make it the default research associate for operators "
            "who produce briefs, memos, board updates and content systems. The gap between amateur and pro use "
            "is structure: source packets, claim/evidence tables, non-goals, and format contracts. This guide "
            "covers web + Projects + Artifacts workflows teams use to ship research faster without hallucination debt."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "Research packet template",
                "body": [
                    "Before asking for synthesis, assemble: (1) question and decision needed, (2) sources provided "
                    "labeled A/B/C, (3) non-goals, (4) output format, (5) citation rules, (6) confidence labels "
                    "for weak evidence.",
                ],
                "bullets": [
                    ("Decision", "What choice this brief supports - one sentence."),
                    ("Sources", "Only use provided docs; flag gaps explicitly."),
                    ("Format", "Exec summary 150 words, then evidence table, then recommendation."),
                ],
            },
            {
                "tab": "02",
                "title": "Writing modes in Projects",
                "body": [
                    "Create separate Projects or instruction blocks for: exec memo, investor update, blog longform, "
                    "support macro, talk track. Each mode has different length, tone and taboo phrases.",
                ],
            },
            {
                "tab": "03",
                "title": "Citation hygiene",
                "body": [
                    "Require [Source: filename, section] after factual claims from uploads. Separate 'Inference' "
                    "section for model reasoning. Ban invented statistics - instruct Claude to write UNKNOWN rather "
                    "than guess.",
                ],
            },
        ],
        "playbook": [
            "Create Research Project with citation rules in instructions.",
            "Upload source PDFs; label filenames descriptively.",
            "Run synthesis prompt with decision + format contract.",
            "Human verifies numbers and names against sources.",
            "Export final as Artifact; archive in project knowledge.",
        ],
        "mistakes": [
            "Asking for 'research X' without providing sources - hallucination bait.",
            "One Project mixing casual chat and board memos - tone drift.",
            "Skipping human verification on numbers and proper nouns.",
            "No non-goals - Claude expands scope every time.",
        ],
        "glossary": [
            ("Source packet", "Labeled inputs Claude must not exceed."),
            ("Claim table", "Two-column facts vs citations for audit."),
            ("Non-goals", "Explicit list of what the output must not cover."),
        ],
        "callout": {
            "title": "Power prompt skeleton",
            "text": "Role: research lead. Decision: [X]. Sources: A/B/C only. Output: exec summary + claim table + "
                    "recommendation. Mark UNKNOWN if not in sources. Non-goals: [list].",
        },
    },
}
