# -*- coding: utf-8 -*-
"""Extended PDF blocks for Claude carousels 11-15. Merged into expand_pdf_content at import."""

BATCH2_EXTENDED = {
    "11_Claude_Projects_For_Teams": {
        "carousel_slides": [
            ("1", "Stop Re-Uploading Context", "Projects persist instructions and knowledge."),
            ("2", "Instructions = System Prompt", "WHO, RULES, FORMAT, ESCALATE blocks."),
            ("3", "Knowledge On Demand", "Files are retrieved, not dumped into every chat."),
            ("4", "Team Sharing", "Can use vs Can edit permissions on Team plans."),
            ("5", "Starter Prompts", "Pin examples so teammates clone, not guess."),
            ("6", "Two-Tier Architecture", "Shared team Projects + personal Projects."),
            ("7", "Weekly Owner Ritual", "Refresh files, log instruction changes."),
            ("8", "Comment AI", "Get the full project templates."),
        ],
        "extra_sections": [
            {
                "tab": "04",
                "title": "Setup walkthrough (claude.ai)",
                "body": [
                    "Anthropic's official flow (support.claude.com): Projects > Create project > Set project "
                    "instructions > Add content to project knowledge > Start chat inside the project boundary.",
                    "Critical detail most users miss: chat history inside a project does NOT automatically "
                    "become shared context for other chats. Only instructions + uploaded knowledge persist. "
                    "Decisions made in chat must be exported to a knowledge file if teammates need them.",
                ],
                "bullets": [
                    ("Create", "Projects sidebar > + New project. Name by outcome not date."),
                    ("Instructions", "Project settings > Set project instructions > Save."),
                    ("Knowledge", "Add content > upload PDF, MD, CSV, code. ~30MB per file."),
                    ("Share", "Team plan: invite with Can use or Can edit per member."),
                ],
                "code": {
                    "caption": "Project instructions template (paste in Set project instructions)",
                    "lines": "WHO: You are the [Company] [role] assistant.\n\nRULES:\n- Always cite uploaded files by filename.\n- Never invent pricing, legal claims, or customer names.\n- If info missing, write UNKNOWN and list what file would resolve it.\n\nFORMAT:\n1. Exec summary (3 bullets)\n2. Detail with citations\n3. Next actions (owner + deadline)\n\nESCALATE: Say 'Needs human review' for legal, HR, or pricing exceptions.",
                },
            },
            {
                "tab": "05",
                "title": "Knowledge architecture that scales",
                "body": [
                    "Claude Lab's team pattern: shared Projects hold official docs only; personal Projects hold "
                    "individual preferences. Filename convention: spec-auth-flow.md, brand-voice.md, pricing-current.csv.",
                    "Header each file with author + last-updated date. One knowledge owner approves uploads.",
                ],
                "bullets": [
                    ("Official only", "No drafts in shared knowledge - stale drafts poison retrieval."),
                    ("Chunk by topic", "Five focused files beat one 200-page dump."),
                    ("Exemplars", "EXAMPLE-good-email.md teaches format better than adjectives."),
                ],
                "pro_tip": {
                    "title": "Retrieval trick",
                    "text": "Ask 'Which knowledge files did you use for each claim?' in test chats. If Claude "
                            "cites wrong files, rename or split knowledge until retrieval stabilizes.",
                },
            },
            {
                "tab": "06",
                "title": "Three Projects every team should clone",
                "body": [
                    "1) Brand & Comms - brand-voice.md, banned-phrases.md, EXAMPLE posts. 2) Product & Pricing - "
                    "pricing.csv, feature-matrix.md, competitor-notes.md. 3) Ops & Support - macro library, "
                    "escalation tree, SLA doc.",
                    "Each Project gets 3 pinned starter prompts in the description field teammates copy-paste.",
                ],
                "code": {
                    "caption": "Starter prompt: weekly exec update from project knowledge",
                    "lines": "Using ONLY files in this project:\n1. Summarize product changes from changelog.md\n2. Pull open risks from risks-register.md\n3. Draft 150-word exec update for Slack #leadership\nCite each bullet with [filename]. Mark UNKNOWN if not in files.",
                },
            },
            {
                "tab": "07",
                "title": "Team permissions playbook",
                "body": [
                    "Can use: ICs who chat but must not edit instructions (prevents drift). Can edit: project "
                    "owner + delegate who versions instruction changes in a CHANGELOG.md uploaded to knowledge.",
                    "Org-wide visibility (Enterprise): use for brand Projects; keep HR/legal Projects restricted.",
                ],
            },
            {
                "tab": "08",
                "title": "Projects + Claude Code bridge",
                "body": [
                    "Claude.ai Projects are no-code team memory. Claude Code uses CLAUDE.md + .claude/ for the "
                    "same role in repos. Mature teams mirror: export approved Project instructions to CLAUDE.md "
                    "sections and sync pricing/brand files into repo docs/ for developers.",
                    "GitHub: macanhhuy/claude-code-development-kit ships starter CLAUDE.md and project templates "
                    "you can adapt from web Project instructions.",
                ],
                "code": {
                    "caption": "Sync ritual (weekly, 15 min)",
                    "lines": "1. Export best Project answer to knowledge/exemplars/\n2. If engineering-relevant, copy rules to CLAUDE.md\n3. Delete superseded pricing/policy files\n4. Log change in project-CHANGELOG.md\n5. Re-run 5 golden test prompts",
                },
            },
            {
                "tab": "09",
                "title": "GitHub repos for Project operators",
                "body": [
                    "These community repos complement Anthropic docs - not official, but battle-tested:",
                ],
                "bullets": [
                    ("AlexandrG539/claude-code-setup-guide", "Step-by-step Claude Code + MCP setup; port patterns to Project instructions."),
                    ("affaan-m/everything-claude-code", "Hooks, skills, MCP configs - translate SOPs into Project instruction blocks."),
                    ("arosenkranz/claude-code-config", "Example .claude.json and permission patterns for team governance."),
                ],
            },
        ],
        "hidden_tricks": [
            "Knowledge files are searched on demand - you can upload hundreds of pages; Claude pulls sections when needed, not all at once.",
            "Put starter prompts in the project description field - teammates see them before first message.",
            "Use EXAMPLE- prefix on gold outputs in knowledge - Claude matches structure faster than tone paragraphs.",
            "Split 'Can edit' to one owner - everyone else 'Can use' stops instruction drift.",
            "Export great chat answers to .md and re-upload - chat context does not auto-share across threads.",
            "Test with 'list every file you referenced' before inviting the team.",
            "Create personal Project for experiments; promote to team Project only after 10 stable test runs.",
            "Filename dates in headers (Updated: 2026-05-01) help Claude prefer current policy over old uploads.",
        ],
    },
    "12_Claude_Artifacts_For_Business": {
        "carousel_slides": [
            ("1", "Deliverables Beside Chat", "Artifacts are editable output panels."),
            ("2", "Force Artifact Mode", "Tell Claude: chat minimal, deliverable in Artifact."),
            ("3", "React and HTML", "Mini apps without a dev sprint."),
            ("4", "Project + Artifact", "Brand tokens from knowledge drive CSS."),
            ("5", "Version In Place", "v2/v3 updates same panel - no duplicate mess."),
            ("6", "Export and Archive", "Save finals to project knowledge."),
            ("7", "Client Snapshot", "PDF v-final before experimental v3."),
            ("8", "Comment AI", "Get Artifact prompt pack."),
        ],
        "extra_sections": [
            {
                "tab": "04",
                "title": "When and how Artifacts spawn",
                "body": [
                    "Claude opens an Artifact for self-contained outputs: long docs, code, SVG, interactive HTML. "
                    "Force it explicitly: 'Put the complete deliverable in an Artifact. Use chat only for clarifying "
                    "questions.' Settings > Capabilities > Artifacts should be enabled (default on Pro).",
                ],
                "bullets": [
                    ("Documents", "SOPs, proposals, policies - side panel editing."),
                    ("Interactive", "Calculators, configurators, data viz in React/HTML sandbox."),
                    ("Diagrams", "Mermaid, SVG flowcharts for ops documentation."),
                ],
            },
            {
                "tab": "05",
                "title": "Brand-locked Artifact prompt",
                "body": [
                    "Upload brand-tokens.css or brand section in instructions with hex values. Reference in Artifact "
                    "prompt so interactive outputs match marketing site without manual CSS fixes.",
                ],
                "code": {
                    "caption": "ROI calculator Artifact prompt",
                    "lines": "Create an Artifact-only interactive ROI calculator.\nInputs: monthly ad spend, conversion rate, AOV, CAC.\nOutputs: ROAS, payback months, LTV:CAC ratio.\nUse CSS variables from brand-tokens.md in project knowledge.\nNo external CDN libraries. Mobile-friendly layout.\nChat: ask max 1 clarifying question if inputs ambiguous.",
                },
            },
            {
                "tab": "06",
                "title": "Artifact types for business teams",
                "body": [
                    "Sales: mutual action plan table, battlecard HTML, pricing scenario calculator. Marketing: "
                    "campaign brief doc, landing page wireframe HTML. Ops: runbook checklist, escalation flow "
                    "Mermaid diagram. Product: PRD skeleton, user story table.",
                ],
                "code": {
                    "caption": "Mutual action plan Artifact prompt",
                    "lines": "Artifact: mutual action plan for enterprise deal.\nColumns: Milestone, Owner, Due date, Status, Blocker.\nPre-fill from deal-notes.md in project knowledge.\nHighlight overdue items in coral #EF5E45.\nExport-friendly markdown table at bottom.",
                },
            },
            {
                "tab": "07",
                "title": "Iteration protocol (v2/v3)",
                "body": [
                    "Never accept v1 for client-facing work. Use numbered change lists: 'Artifact v2: shorten exec "
                    "summary, add risk table, keep v1 layout.' Claude updates the same Artifact.",
                    "Before risky v3 experiments, copy v-final text to a knowledge file as snapshot.",
                ],
                "pro_tip": {
                    "title": "Hidden command pattern",
                    "text": "Say 'Do not create a new Artifact - edit the existing one' when Claude spawns "
                            "duplicates during long threads.",
                },
            },
            {
                "tab": "08",
                "title": "Artifacts in Projects workflow",
                "body": [
                    "Run Artifacts inside a Project so instructions enforce brand, legal disclaimers from policy.pdf, "
                    "and data columns from pricing.csv. After approval, download Artifact source and upload to "
                    "project knowledge as templates/ for reuse.",
                ],
            },
            {
                "tab": "09",
                "title": "React Artifact constraints that ship",
                "body": [
                    "Claude Artifacts run in a sandbox. Avoid external npm imports unless documented. Prefer "
                    "inline React with useState, plain CSS, no fetch to private APIs (use static data from knowledge).",
                ],
                "code": {
                    "caption": "Safe interactive Artifact spec",
                    "lines": "Stack: single-file React component, inline styles only.\nData: embed from uploaded CSV pasted as const DATA = [...]\nNo network calls. No localStorage secrets.\nInclude 'Reset' button and input validation messages.",
                },
            },
        ],
        "hidden_tricks": [
            "Prefix prompts with 'Artifact-only mode' to stop Claude narrating in chat.",
            "Upload brand hex values as brand-tokens.md - Artifacts reference variables, not guessed colors.",
            "Use Mermaid Artifacts for ops docs - exports clean to Notion and Confluence.",
            "Say 'edit existing Artifact' to prevent duplicate panels in long sessions.",
            "Snapshot v-final to knowledge before asking experimental redesigns.",
            "Combine Project citation rules with Artifact tables - audit trail for research deliverables.",
            "For client PDFs: copy Artifact to Google Doc, then export PDF - preserves formatting better than chat copy.",
            "Template library: save approved Artifact markdown in knowledge/templates/ with version numbers.",
        ],
    },
    "13_Claude_MCP_For_Operators": {
        "carousel_slides": [
            ("1", "Live Data Not Stale CSVs", "MCP connects Claude to real systems."),
            ("2", "claude mcp add", "CLI setup in under 10 minutes."),
            ("3", "Three Scopes", "local, project (.mcp.json), user global."),
            ("4", "Read-First Rollout", "SELECT before INSERT."),
            ("5", "Context Tax", "Under 10 MCPs, ~80 tools active."),
            ("6", "/mcp Auth", "OAuth inside Claude Code session."),
            ("7", "Hooks + MCP", "PreToolUse blocks dangerous writes."),
            ("8", "Comment AI", "Get MCP starter .mcp.json."),
        ],
        "extra_sections": [
            {
                "tab": "04",
                "title": "Official setup (Claude Code docs)",
                "body": [
                    "Anthropic documents four transport types: HTTP (remote), SSE (legacy remote), stdio (local "
                    "npx process), WebSocket. Most operators start with HTTP remote servers (GitHub, Sentry, Linear) "
                    "because no local Node install debugging.",
                ],
                "code": {
                    "caption": "GitHub MCP (official remote HTTP)",
                    "lines": "# Fine-grained PAT from github.com/settings/tokens\nclaude mcp add --transport http github \\\n  https://api.githubcopilot.com/mcp/ \\\n  --header \"Authorization: Bearer YOUR_GITHUB_PAT\"\n\n# Inside Claude Code session:\n/mcp\n# Select Authenticate for github",
                },
            },
            {
                "tab": "05",
                "title": "Project-scoped .mcp.json for teams",
                "body": [
                    "Use --scope project so .mcp.json commits to git. Teammates inherit same connectors. Never "
                    "commit secrets - use env vars and ${GITHUB_TOKEN} patterns.",
                ],
                "code": {
                    "caption": ".mcp.json team starter (commit this, not tokens)",
                    "lines": "{\n  \"mcpServers\": {\n    \"github\": {\n      \"type\": \"http\",\n      \"url\": \"https://api.githubcopilot.com/mcp/\"\n    },\n    \"sentry\": {\n      \"type\": \"http\",\n      \"url\": \"https://mcp.sentry.dev/mcp\"\n    },\n    \"db-readonly\": {\n      \"command\": \"npx\",\n      \"args\": [\"-y\", \"@bytebase/dbhub\", \"--dsn\", \"${DATABASE_URL_READONLY}\"]\n    }\n  }\n}",
                },
                "pro_tip": {
                    "title": "Flag order matters",
                    "text": "claude mcp add requires --scope and --transport BEFORE the server name. "
                            "Wrong order silently fails on some CLI versions.",
                },
            },
            {
                "tab": "06",
                "title": "Postgres read-only pattern",
                "body": [
                    "Create a DB user with SELECT only on views you expose. Point dbhub MCP at read replica, "
                    "not primary. Split write tools into a separate MCP server disabled by default in "
                    "disabledMcpServers project config.",
                ],
                "code": {
                    "caption": "Read-only Postgres MCP",
                    "lines": "claude mcp add --scope project db-readonly -- \\\n  npx -y @bytebase/dbhub \\\n  --dsn \"postgresql://readonly:PASS@replica:5432/analytics\"\n\n# Verify:\nclaude mcp list",
                },
            },
            {
                "tab": "07",
                "title": "Context budget management",
                "body": [
                    "affaan-m/everything-claude-code documents disabledMcpServers in project settings to turn off "
                    "unused servers per workflow. 20+ configured MCPs can shrink usable context from ~200K toward "
                    "~70K tokens because tool schemas load at session start.",
                ],
                "bullets": [
                    ("Cap enabled MCPs", "Fewer than 10 active per project."),
                    ("Cap tools", "Aim for ~80 total tool definitions active."),
                    ("Workflow-specific", "Sales project: CRM read only. Eng project: GitHub + Sentry."),
                ],
            },
            {
                "tab": "08",
                "title": "Hooks that gate MCP writes",
                "body": [
                    "PreToolUse hooks on MCP tool calls can require confirmation for INSERT, UPDATE, post_message, "
                    "create_issue with write scope. robinbril/claude-harness shows hook patterns for team safety.",
                ],
                "code": {
                    "caption": "Concept: block write tools until APPROVE=1 env set",
                    "lines": "# PreToolUse hook (stdin JSON includes tool_name)\nif echo \"$tool\" | grep -E 'write|create|delete|merge'; then\n  if [ \"$MCP_WRITES_APPROVED\" != \"1\" ]; then\n    echo '{\"decision\":\"block\",\"reason\":\"Set MCP_WRITES_APPROVED=1 after human review\"}'\n    exit 2\n  fi\nfi",
                },
            },
            {
                "tab": "09",
                "title": "GitHub repos and install scripts",
                "body": [
                    "Community references worth bookmarking:",
                ],
                "bullets": [
                    ("modelcontextprotocol/servers", "Official MCP server implementations (GitHub, filesystem, postgres)."),
                    ("justinwlin/claude-mcp-guide", "CLI reference for scopes, transports, env vars."),
                    ("undeadpickle/claude-code-mcpinstall", "One-script bulk install for filesystem, fetch, puppeteer MCPs."),
                    ("robinbril/claude-harness", "Hooks + MCP governance patterns for production teams."),
                ],
            },
        ],
        "hidden_tricks": [
            "Run claude mcp list after every add - silent failures happen when npx path wrong.",
            "Use --scope project for team repos; --scope user only for personal experiments.",
            "Authenticate inside session with /mcp - tokens refresh; don't paste PATs into prompts.",
            "disabledMcpServers in project settings turns off MCPs without deleting config.",
            "HTTP MCP beats stdio on laptops with strict corporate npm proxy policies.",
            "Name tools narrowly in custom MCP servers - 'run_read_query' not 'run_query'.",
            "Log tool inputs on write failures - schema mismatches are the #1 MCP debug issue.",
            "Start with GitHub read + filesystem before Postgres - proves value in one afternoon.",
        ],
    },
    "14_Claude_Sonnet_vs_Opus": {
        "carousel_slides": [
            ("1", "Route Like Headcount", "Sonnet volume, Opus judgment."),
            ("2", "Risk Tags", "Tag tasks 1-3 before picking model."),
            ("3", "Escalation Rule", "3 failed Sonnet rounds -> Opus thread."),
            ("4", "Subagent Models", "Haiku explore, Sonnet build, Opus review."),
            ("5", "Cost Per Success", "Measure edit minutes not API cents."),
            ("6", "Project Defaults", "Sonnet default, Opus keyword triggers."),
            ("7", "API model param", "Explicit per request in production."),
            ("8", "Comment AI", "Get routing cheat sheet PDF."),
        ],
        "extra_sections": [
            {
                "tab": "04",
                "title": "Routing table with examples",
                "body": [
                    "Sonnet: rewrite email, summarize meeting, CSV cleanup, first-pass blog, support macro, "
                    "internal Slack post, bulk unit test generation. Opus: board memo, contract summary, architecture "
                    "decision record, multi-doc M&A brief, security threat model, investor narrative.",
                ],
                "bullets": [
                    ("Sonnet", "Template exists, facts provided, human edit under 15 minutes."),
                    ("Opus", "High blast radius, conflicting constraints, executive audience."),
                    ("Haiku", "Classify ticket urgency, grep-scale explore, routing decisions."),
                ],
            },
            {
                "tab": "05",
                "title": "Claude Code subagent routing",
                "body": [
                    "Define model in .claude/agents/*.md YAML frontmatter. Explore on Haiku saves 40-60% context "
                    "cost vs Opus reading entire repos in main thread.",
                ],
                "code": {
                    "caption": ".claude/agents/architect.md (Opus review)",
                    "lines": "---\nname: architect\ndescription: Architecture and security review\nmodel: opus\ntools: Read, Grep, Glob\ndisallowedTools: Write, Edit, Bash\n---\n\nReview proposed changes for:\n1. Security regressions\n2. Data model integrity\n3. Breaking API changes\nReturn PASS/FAIL with file:line references.",
                },
            },
            {
                "tab": "06",
                "title": "Project instruction routing keywords",
                "body": [
                    "In shared Projects, add instruction block: 'Default: thorough but efficient responses. "
                    "If message contains BOARD, LEGAL, PRICING EXCEPTION, or ARCHITECTURE - switch to maximum "
                    "reasoning depth and double-check citations.'",
                    "This nudges Claude toward Opus-tier care on trigger topics even when UI model is Sonnet.",
                ],
                "code": {
                    "caption": "Paste into Project instructions",
                    "lines": "MODEL BEHAVIOR:\n- Standard tasks: concise, structured, fast.\n- TRIGGER KEYWORDS (BOARD, LEGAL, ARCHITECTURE, INVESTOR):\n  * Slow down. List assumptions.\n  * Cite sources for every factual claim.\n  * Add 'Risks and unknowns' section.\n  * Never guess numbers.",
                },
            },
            {
                "tab": "07",
                "title": "API routing for production apps",
                "body": [
                    "Pass model explicitly per request. Router pattern: Haiku classifies intent -> Sonnet or Opus "
                    "handles body. Log model + human_edit_minutes + rework_flag for monthly review.",
                ],
                "code": {
                    "caption": "Python router sketch",
                    "lines": "ROUTING = {\n  \"classify\": \"claude-haiku-4-5\",\n  \"draft\": \"claude-sonnet-4-6\",\n  \"executive\": \"claude-opus-4-6\",\n}\n\ntier = classify_task(user_input)  # haiku\nmodel = ROUTING[\"executive\"] if tier == 3 else ROUTING[\"draft\"]\nresponse = client.messages.create(model=model, ...)",
                },
            },
            {
                "tab": "08",
                "title": "When Sonnet fails silently",
                "body": [
                    "Sonnet errors are subtle: wrong tone in executive comms, missed edge case in policy interpretation, "
                    "overconfident recommendation without caveats. Escalation heuristic: if human rewrites more than "
                    "30% of output twice on same task type, move task class to Opus permanently.",
                ],
            },
            {
                "tab": "09",
                "title": "Team routing cheat sheet (printable)",
                "body": [
                    "Publish one page internally:",
                ],
                "bullets": [
                    ("Tier 1 Sonnet", "Drafts, summaries, transforms, internal comms, codegen with tests."),
                    ("Tier 2 Sonnet + review", "Customer-facing copy with human sign-off."),
                    ("Tier 3 Opus", "Legal, finance, board, architecture, novel multi-stakeholder decisions."),
                    ("Escalate", "3 correction rounds on same thread -> new Opus thread with context attached."),
                ],
            },
        ],
        "hidden_tricks": [
            "Explore subagent on Haiku before Opus architecture review - cheaper context map.",
            "Add TRIGGER KEYWORDS to Project instructions for automatic depth bump.",
            "Track human_edit_minutes per model - proves Opus ROI on tier-3 tasks.",
            "Never use Opus for 'make shorter' - use Sonnet with max_tokens cap.",
            "API: separate API keys per tier for finance chargeback to departments.",
            "Claude Code /cost shows session spend - compare Explore+Haiku vs monolithic Opus thread.",
            "For batch jobs: Sonnet parallel workers + single Opus aggregator pass.",
            "Re-benchmark routing quarterly when Anthropic releases new model IDs.",
        ],
    },
    "15_Claude_For_Research_And_Writing": {
        "carousel_slides": [
            ("1", "Source Packets Beat Vague Prompts", "Label inputs A/B/C."),
            ("2", "Claim Tables", "Fact | Citation | Confidence."),
            ("3", "Non-Goals", "Stop scope creep cold."),
            ("4", "Writing Modes", "Separate Projects per output type."),
            ("5", "UNKNOWN > Guessing", "Ban invented statistics."),
            ("6", "Artifact Export", "Final brief in side panel."),
            ("7", "Human Verify Pass", "Numbers and names checked."),
            ("8", "Comment AI", "Get research prompt pack."),
        ],
        "extra_sections": [
            {
                "tab": "04",
                "title": "Research packet (copy-paste template)",
                "body": [
                    "Professional research with Claude starts before the first question. Assemble labeled sources, "
                    "decision statement, and format contract.",
                ],
                "code": {
                    "caption": "Master research prompt",
                    "lines": "ROLE: Research lead for [Company].\nDECISION: Should we [X] by [date]?\nSOURCES (ONLY): A=market-report.pdf B=internal-metrics.csv C=competitor-notes.md\nNON-GOALS: No product roadmap, no hiring plan.\nOUTPUT:\n1. Exec summary (max 150 words)\n2. Claim table: Claim | Source | Confidence (H/M/L)\n3. Recommendation with risks\n4. Open questions (what file would resolve each)\nRULES: Write UNKNOWN instead of guessing. Separate INFERENCE section.",
                },
            },
            {
                "tab": "05",
                "title": "Exec memo mode vs blog mode",
                "body": [
                    "Exec memo Project: max 400 words, no adjectives without data, mandatory risks section. Blog "
                    "Project: narrative hook, subheads, SEO keywords from keywords.md, longer examples allowed.",
                ],
                "code": {
                    "caption": "Exec memo instructions block",
                    "lines": "VOICE: Direct, no hype, no 'revolutionary' or 'game-changing'.\nSTRUCTURE: Bottom line up front. Max 3 recommendations.\nEVERY stat needs [Source: file, section].\nEND with 'What would change this recommendation'.",
                },
            },
            {
                "tab": "06",
                "title": "Multi-doc synthesis without hallucination",
                "body": [
                    "Upload sources to Project knowledge. In prompt, forbid web browsing unless explicitly enabled. "
                    "Ask Claude to flag conflicts between sources in a dedicated CONFLICTS section instead of "
                    "smoothing them over.",
                ],
                "bullets": [
                    ("Conflicts", "Source A says X, Source B says Y - do not merge silently."),
                    ("Gaps", "List missing data that would upgrade confidence from M to H."),
                    ("Inference", "Quarantine model reasoning from sourced facts."),
                ],
            },
            {
                "tab": "07",
                "title": "Investor update workflow",
                "body": [
                    "Weekly rhythm: upload metrics.csv + changelog.md + wins-losses.md. Run fixed prompt. Human "
                    "verifies every number against CSV before send. Save approved output to knowledge/investor/YYYY-MM-DD.md.",
                ],
                "code": {
                    "caption": "Investor update prompt",
                    "lines": "Using ONLY this week's uploaded files:\nDraft investor update email.\nSections: Highlights, Metrics (table), Product, Asks, Risks.\nMetrics must match metrics.csv exactly - quote row numbers.\nTone: confident, precise, no superlatives without data.",
                },
            },
            {
                "tab": "08",
                "title": "Longform content system",
                "body": [
                    "Outline-first: 'Artifact v1: outline only, no prose.' Then section-by-section expansion "
                    "with word counts per section. Prevents 3,000-word ramble and makes human edit tractable.",
                ],
                "code": {
                    "caption": "Longform two-pass prompt",
                    "lines": "PASS 1 - Artifact outline only:\n- H2 sections with 1-sentence thesis each\n- Target word count per section\n- CTA placement\n\nPASS 2 (after I approve outline):\nExpand section 2 only. Max 400 words.\nCite examples from case-studies.md only.",
                },
            },
            {
                "tab": "09",
                "title": "Verification checklist before send",
                "body": [
                    "Human operator runs this on every external-facing doc:",
                ],
                "bullets": [
                    ("Numbers", "Spot-check 100% against source CSV/PDF."),
                    ("Names", "Company and people names match sources exactly."),
                    ("Dates", "Timeline claims have citation or marked UNKNOWN."),
                    ("Tone", "No banned phrases from brand-voice.md."),
                    ("Scope", "Non-goals section respected - delete stray sections."),
                ],
            },
        ],
        "hidden_tricks": [
            "Require row numbers when citing CSV metrics - catches transposition errors fast.",
            "CONFLICTS section forces Claude to surface disagreement instead of false consensus.",
            "Two-pass longform (outline then sections) cuts edit time 50%+ vs one-shot drafts.",
            "Save approved outputs dated in knowledge - next week's prompt says 'match tone of 2026-05-01 update'.",
            "Ban superlatives in Project instructions - Claude defaults to hype without this.",
            "Use Artifact for final brief; chat for Q&A only - cleaner export to PDF.",
            "Ask 'what would change this recommendation' - surfaces hidden assumptions executives want.",
            "Web research: require URL + access date in claim table or mark source as UNVERIFIED.",
        ],
    },
}

BATCH2_FAQS = {
    "11_Claude_Projects_For_Teams": [
        ("Do chat histories share across project chats?", "No. Anthropic docs: context is not shared across chats unless exported to project knowledge."),
        ("How much can I upload?", "Roughly 200K tokens total across knowledge files; ~30MB per file typical."),
        ("Can use vs Can edit?", "Can use: chat only. Can edit: modify instructions, knowledge, and member settings."),
        ("Free tier Projects?", "Projects exist on paid tiers; limits scale with Pro/Team/Enterprise."),
        ("One project or many?", "Split by outcome - Brand, Product, Support - not one mega-project."),
        ("How to stop instruction drift?", "One Can edit owner; CHANGELOG in knowledge; others Can use only."),
        ("Projects vs Claude Code memory?", "Projects = claude.ai no-code. CLAUDE.md = repo agent memory. Mirror critical rules in both."),
        ("How to test before team rollout?", "Run 10 golden prompts; ask which files were cited each time."),
    ],
    "12_Claude_Artifacts_For_Business": [
        ("How do I force an Artifact?", "Say: put complete deliverable in Artifact; chat only for clarifying questions."),
        ("Can Artifacts call my API?", "Sandbox limits apply - embed static data from knowledge instead of private API calls."),
        ("React in Artifacts?", "Yes - inline React with useState; avoid undeclared external libraries."),
        ("Duplicate Artifacts in one chat?", "Say 'edit existing Artifact, do not create new panel'."),
        ("Export to PDF?", "Copy from Artifact panel or paste into Google Docs then export."),
        ("Artifacts + Projects?", "Run inside Project so brand/legal rules from instructions apply."),
        ("Client approval workflow?", "Snapshot v-final to knowledge before v3 experiments."),
        ("Best business Artifact types?", "Calculators, MAP tables, runbook checklists, Mermaid flows."),
    ],
    "13_Claude_MCP_For_Operators": [
        ("Where is config stored?", "Local: ~/.claude.json. Project: .mcp.json in repo root. User: ~/.claude.json global."),
        ("HTTP vs stdio MCP?", "HTTP for GitHub/Sentry/Linear remote. stdio for npx local servers like dbhub."),
        ("How to authenticate?", "Run /mcp inside Claude Code session after claude mcp add."),
        ("How many MCPs is too many?", "Keep under 10 enabled; ~80 tools active to preserve context window."),
        ("Read-only DB first?", "Yes - SELECT-only user on replica before any write MCP."),
        ("Commit .mcp.json?", "Yes with --scope project; never commit tokens - use env vars."),
        ("Official server list?", "github.com/modelcontextprotocol/servers and Anthropic MCP directory."),
        ("Block dangerous writes?", "PreToolUse hooks on MCP tool names containing write/create/delete."),
    ],
    "14_Claude_Sonnet_vs_Opus": [
        ("Default for most work?", "Sonnet for volume drafts, summaries, transforms, internal comms."),
        ("When Opus?", "Board, legal, architecture, investor narrative, novel multi-constraint problems."),
        ("How to escalate?", "After 3 correction rounds on Sonnet, open Opus thread with same context attached."),
        ("Claude Code subagents?", "Haiku explore, Sonnet build, Opus architect/review in agent frontmatter."),
        ("Measure what?", "Cost per successful approved output including human edit minutes."),
        ("Opus for short emails?", "No - Sonnet with length constraint is faster and equally good."),
        ("Project keyword triggers?", "Add BOARD, LEGAL, ARCHITECTURE triggers in instructions for depth bump."),
        ("API production?", "Explicit model param per request; router classifies tier first."),
    ],
    "15_Claude_For_Research_And_Writing": [
        ("Research without sources?", "Avoid - provide labeled files or accept UNKNOWN-heavy output."),
        ("Stop hallucinated stats?", "Instruct: write UNKNOWN; require claim table with citations."),
        ("Separate writing modes?", "Different Projects for exec memo vs blog vs support macro."),
        ("Multi-doc conflicts?", "Require CONFLICTS section - do not merge contradictory sources silently."),
        ("Longform without ramble?", "Outline Artifact first; expand one section per message."),
        ("Verify before send?", "Human checks 100% of numbers and proper nouns against sources."),
        ("Investor updates?", "Fixed prompt + metrics.csv; archive approved dated markdown in knowledge."),
        ("Web sources?", "Require URL + access date in claim table or mark UNVERIFIED."),
    ],
}

BATCH2_CASE_STUDIES = {
    "11_Claude_Projects_For_Teams": (
        "A 12-person B2B SaaS marketing team replaced five scattered Claude chats with three Projects: "
        "Brand Voice, Campaign Copy, and Competitive Intel. They uploaded EXAMPLE-winners/ files, set "
        "Can edit to one lead, and pinned starter prompts in descriptions. Onboarding time for new writers "
        "dropped from 2 weeks of tone corrections to 3 days - not because Claude got smarter, but because "
        "instructions and exemplars loaded every session. They mirrored pricing rules into engineering's "
        "CLAUDE.md monthly."
    ),
    "12_Claude_Artifacts_For_Business": (
        "A sales ops lead built a mutual-action-plan Artifact inside a Deal Desk Project with brand CSS from "
        "knowledge. Reps cloned the starter prompt per enterprise opportunity; v2/v3 iterations stayed in one "
        "panel. Win: legal-approved disclaimer text from policy.pdf auto-inserted. They archived v-final "
        "Artifacts to knowledge/templates/ - next quarter's reps started from proven structure, not blank chat."
    ),
    "13_Claude_MCP_For_Operators": (
        "An analytics team connected read-only Postgres MCP (replica + SELECT user) and GitHub HTTP MCP with "
        "project-scoped .mcp.json in git. Week 1: 'show me signup funnel last 7 days' matched Metabase. Week 3: "
        "added PreToolUse hook blocking write tools unless MCP_WRITES_APPROVED=1. Incident rate from bad queries "
        "went to zero because writes never reached production DB."
    ),
    "14_Claude_Sonnet_vs_Opus": (
        "A fintech ops team tagged 200 recurring tasks by risk. Sonnet handled 85% (macros, summaries, CSV "
        "transforms). Opus locked to tier-3: regulatory memos, board prep, architecture reviews. They tracked "
        "human_edit_minutes and cut API spend 38% while board memo quality scores (internal rubric) went up - "
        "because Opus time went to work that actually needed it."
    ),
    "15_Claude_For_Research_And_Writing": (
        "A founder ran weekly investor updates through a Research Project with metrics.csv, changelog.md, and "
        "fixed claim-table prompt. First month: caught two metric transposition errors in verification pass. "
        "Second month: saved approved updates to knowledge/investor/ - Claude matched tone and structure without "
        "re-explaining format. Partners commented updates got ' tighter and more honest about unknowns.'"
    ),
}

BATCH2_REFERENCE_APPENDIX = {
    "11_Claude_Projects_For_Teams": {
        "title": "Reference: setup checklist and repos",
        "body": [
            "Official: support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects",
            "Use this checklist when standing up a team Project from scratch.",
        ],
        "bullets": [
            ("Step 1", "Create project named [Team] - [Outcome]."),
            ("Step 2", "Paste WHO/RULES/FORMAT/ESCALATE instructions template."),
            ("Step 3", "Upload 5-8 curated files with dated headers."),
            ("Step 4", "Pin 3 starter prompts in project description."),
            ("Step 5", "Run 10 golden tests; fix retrieval before sharing."),
            ("Step 6", "Share: owner Can edit, team Can use."),
            ("AlexandrG539/claude-code-setup-guide", "Claude Code setup - mirror rules to CLAUDE.md."),
            ("macanhhuy/claude-code-development-kit", "Starter kit for repo-side agent memory."),
        ],
        "code": {
            "caption": "Golden test prompt (run before team invite)",
            "lines": "Answer using ONLY project knowledge:\n1. What is our refund policy for enterprise?\n2. Cite filename for each claim.\n3. List any UNKNOWNs.\n4. Which files did you search but not use?",
        },
    },
    "12_Claude_Artifacts_For_Business": {
        "title": "Reference: Artifact prompt library",
        "body": [
            "Copy these starters into Projects with matching knowledge files.",
        ],
        "bullets": [
            ("ROI calculator", "Interactive React; inputs spend, CVR, AOV; brand CSS vars."),
            ("Mutual action plan", "Table from deal-notes.md; overdue highlighted."),
            ("Runbook checklist", "Mermaid flow + checkbox HTML for ops."),
            ("Policy summary", "Doc Artifact with mandatory legal footer from policy.pdf."),
        ],
        "code": {
            "caption": "Universal Artifact opener",
            "lines": "ARTIFACT-ONLY MODE:\nDeliverable: [type]\nChat: max 1 clarifying question\nVersion: start v1; I will request v2 with numbered changes\nBrand: use variables from brand-tokens.md",
        },
    },
    "13_Claude_MCP_For_Operators": {
        "title": "Reference: commands and repos",
        "body": [
            "Docs: code.claude.com/docs/en/mcp. Verify claude mcp list after every change.",
        ],
        "bullets": [
            ("claude mcp add", "Add server with --transport http or stdio."),
            ("--scope project", "Writes .mcp.json for team git share."),
            ("/mcp", "Authenticate OAuth inside session."),
            ("claude mcp list", "Verify connected servers."),
            ("modelcontextprotocol/servers", "Official reference implementations."),
            ("justinwlin/claude-mcp-guide", "Scope and transport quick reference."),
            ("affaan-m/everything-claude-code", "Context budget and disabledMcpServers patterns."),
        ],
        "code": {
            "caption": "Week-1 operator MCP stack",
            "lines": "claude mcp add --scope project --transport http github https://api.githubcopilot.com/mcp/\nclaude mcp add --scope project db-readonly -- npx -y @bytebase/dbhub --dsn \"$DATABASE_URL_READONLY\"\n# In session: /mcp -> authenticate\n# In CLAUDE.md: list allowed MCP tools and read-only policy",
        },
    },
    "14_Claude_Sonnet_vs_Opus": {
        "title": "Reference: routing matrix",
        "body": [
            "Print this matrix for team Slack pin or Notion.",
        ],
        "bullets": [
            ("Tier 1 Sonnet", "Email edits, summaries, CSV cleanup, internal Slack, test codegen."),
            ("Tier 2 Sonnet + human", "Customer copy, help articles, social posts."),
            ("Tier 3 Opus", "Board, legal, finance precision, architecture, M&A synthesis."),
            ("Haiku", "Explore, classify, route, ticket tagging."),
            ("Escalation", "3 Sonnet correction rounds -> Opus new thread."),
            ("Metric", "human_edit_minutes + rework_incidents per tier monthly."),
        ],
        "code": {
            "caption": "Subagent model lines (Claude Code)",
            "lines": "# explore.md\nmodel: haiku\n\n# builder.md\nmodel: sonnet\n\n# architect.md\nmodel: opus\ndisallowedTools: Write, Edit",
        },
    },
    "15_Claude_For_Research_And_Writing": {
        "title": "Reference: prompt pack and verification",
        "body": [
            "Store these prompts as starter pins in Research Project description.",
        ],
        "bullets": [
            ("Research packet", "Decision + sources A/B/C + claim table + UNKNOWN rule."),
            ("Exec memo", "BLUF, max 400 words, risks section, no hype words."),
            ("Investor update", "Metrics from CSV with row citations."),
            ("Longform", "Outline Artifact pass 1; section expand pass 2."),
            ("Verification", "100% numbers, all names, non-goals respected."),
        ],
        "code": {
            "caption": "Pre-send verification prompt",
            "lines": "Audit the draft above against sources A/B/C only.\nOutput:\n1. Claims without citation\n2. Numbers that differ from sources\n3. Names spelled differently from sources\n4. Sections violating non-goals\nDo NOT rewrite - audit only.",
        },
    },
}

BATCH2_TROUBLESHOOTING = {
    "11_Claude_Projects_For_Teams": {
        "title": "Troubleshooting Projects",
        "body": [
            "Claude ignores brand voice: add EXAMPLE- files not adjectives; shorten instructions under 1,500 words.",
            "Wrong file cited: rename/split knowledge files; run golden test with 'which files referenced'.",
            "Teammates get inconsistent answers: someone edited instructions without CHANGELOG - restore version.",
            "Outdated pricing in outputs: delete old pricing files from knowledge; only one current pricing.csv.",
            "Chat decision lost: export to .md and upload to knowledge - chats do not auto-share.",
        ],
    },
    "12_Claude_Artifacts_For_Business": {
        "title": "Troubleshooting Artifacts",
        "body": [
            "Output stays in chat: say 'Artifact-only mode' explicitly; check Artifacts enabled in settings.",
            "Duplicate panels: 'edit existing Artifact, do not create new'.",
            "Off-brand colors: upload brand-tokens.md with hex; reference in prompt.",
            "Interactive broken: remove external CDN deps; use inline React + static data.",
            "Lost good version: snapshot v-final to knowledge before experimental edits.",
        ],
    },
    "13_Claude_MCP_For_Operators": {
        "title": "Troubleshooting MCP",
        "body": [
            "Tools missing: claude mcp list; restart session; verify .mcp.json JSON valid.",
            "Auth failures: run /mcp in session; refresh OAuth; check PAT scopes for GitHub.",
            "Context feels tiny: disable unused MCPs via disabledMcpServers; reduce enabled count under 10.",
            "Wrong DB results: confirm read replica DSN; verify SELECT-only grants.",
            "Silent write damage: add PreToolUse hook before enabling any write MCP.",
        ],
    },
    "14_Claude_Sonnet_vs_Opus": {
        "title": "Troubleshooting model routing",
        "body": [
            "Board memo feels shallow: task is tier-3; move to Opus with same sources attached.",
            "Budget blown: audit Opus usage on tier-1 tasks like shortening emails.",
            "Sonnet keeps failing: escalate after 3 rounds; update routing table permanently.",
            "Inconsistent depth in Project: add TRIGGER KEYWORDS block to instructions.",
            "API wrong model: log model param per request; fix router classifier training set.",
        ],
    },
    "15_Claude_For_Research_And_Writing": {
        "title": "Troubleshooting research workflows",
        "body": [
            "Hallucinated stats: no sources provided; add UNKNOWN rule and claim table requirement.",
            "Tone too hype: add banned-words list to Project instructions.",
            "Rambling longform: enforce outline-first two-pass workflow.",
            "Conflicting sources merged: require CONFLICTS section in prompt.",
            "Numbers wrong after send: human verification skipped - enforce row-level CSV check.",
        ],
    },
}

BATCH2_MASTERY_PATH = {
    "11_Claude_Projects_For_Teams": [
        "Week 1: One personal Project with WHO/RULES/FORMAT/ESCALATE instructions and 3 knowledge files.",
        "Week 2: 10 golden test prompts; fix retrieval and citations.",
        "Week 3: Promote to team Project; Can edit owner only; pin starter prompts.",
        "Week 4: Second Project for adjacent workflow (Support or Product).",
        "Month 2: Weekly knowledge refresh ritual; exemplar library growing.",
        "Month 3: Mirror critical rules to CLAUDE.md for engineering; measure onboarding time saved.",
    ],
    "12_Claude_Artifacts_For_Business": [
        "Week 1: One simple doc Artifact inside a Project with brand instructions.",
        "Week 2: Interactive calculator Artifact with brand CSS vars from knowledge.",
        "Week 3: v2/v3 iteration protocol; snapshot v-final to knowledge.",
        "Week 4: Template library folder in project knowledge.",
        "Month 2: Sales or ops team adopts MAP/runbook Artifacts.",
        "Month 3: 50%+ deliverables start from templates not blank chat.",
    ],
    "13_Claude_MCP_For_Operators": [
        "Week 1: GitHub HTTP MCP read-only; validate against known PR list.",
        "Week 2: Postgres read replica MCP; validate 5 known SQL answers.",
        "Week 3: Project-scoped .mcp.json in git; document allowed tools in CLAUDE.md.",
        "Week 4: PreToolUse hook blocking writes.",
        "Month 2: Second MCP only if first is daily-use proven.",
        "Month 3: Audit log review; remove unused servers from enabled list.",
    ],
    "14_Claude_Sonnet_vs_Opus": [
        "Week 1: Tag 50 recent tasks risk 1-3.",
        "Week 2: Publish routing matrix; Sonnet default in Projects.",
        "Week 3: Claude Code subagents: Haiku explore, Sonnet build, Opus review.",
        "Week 4: Track human_edit_minutes per tier.",
        "Month 2: API router or keyword triggers for tier 3.",
        "Month 3: Quarterly re-benchmark; report cost per success to leadership.",
    ],
    "15_Claude_For_Research_And_Writing": [
        "Week 1: Research Project with citation rules and 3 source files.",
        "Week 2: Run master research prompt; human verify claim table.",
        "Week 3: Separate exec memo Project with tone constraints.",
        "Week 4: Investor or board update rhythm with archived approvals.",
        "Month 2: Longform outline-first workflow live.",
        "Month 3: Zero external sends without verification checklist signed.",
    ],
}

BATCH2_EXPERT_DEPTH = {
    "11_Claude_Projects_For_Teams": {
        "title": "What elite teams do differently",
        "body": [
            "They treat Projects as versioned products: instruction CHANGELOG, dated knowledge files, golden tests "
            "before every invite, and two-tier architecture (shared official + personal sandbox). They never "
            "expect chat memory to train teammates - they export decisions to knowledge within 24 hours.",
            "They connect web Projects to repo CLAUDE.md so marketing rules and engineering rules do not diverge.",
        ],
    },
    "12_Claude_Artifacts_For_Business": {
        "title": "What elite teams do differently",
        "body": [
            "They mandate Artifact-only mode for deliverables, maintain templates/ in project knowledge, and "
            "run v-final snapshots before client-facing iterations. Interactive Artifacts use static embedded "
            "data from knowledge - not live API calls that break in sandbox.",
        ],
    },
    "13_Claude_MCP_For_Operators": {
        "title": "What elite teams do differently",
        "body": [
            "They cap enabled MCPs, split read/write at server level, commit .mcp.json without secrets, and "
            "treat PreToolUse hooks as mandatory before any write connector. They log tool calls monthly and "
            "delete servers that nobody used in 30 days.",
        ],
    },
    "14_Claude_Sonnet_vs_Opus": {
        "title": "What elite teams do differently",
        "body": [
            "They optimize cost per approved output, not cheapest API call. They publish routing matrices, "
            "use Haiku for explore, and escalate with data (edit minutes, rework count) not gut feel.",
        ],
    },
    "15_Claude_For_Research_And_Writing": {
        "title": "What elite teams do differently",
        "body": [
            "They never research without labeled source packets. They separate inference from fact, require "
            "CONFLICTS sections, run verification prompts before external send, and archive approved writing "
            "so tone compounds instead of resetting every week.",
        ],
    },
}

BATCH2_CLOSING_NOTES = {
    "11_Claude_Projects_For_Teams": [
        "Projects are team memory - not chat folders. Instructions + knowledge + starter prompts are the product.",
        "Today: create one Project with the WHO/RULES/FORMAT/ESCALATE template from this guide.",
        "Upload five curated files, not your entire Drive.",
        "Run the golden test prompt before inviting anyone.",
        "Assign one Can edit owner. Everyone else Can use.",
        "Export great answers to knowledge within 24 hours.",
        "Comment AI on the post for the next Claude operator guide.",
        "Follow @piyush.glitch for AI systems content that ships.",
    ],
    "12_Claude_Artifacts_For_Business": [
        "Artifacts turn Claude from chat into a deliverable surface - if you force Artifact-only mode.",
        "This week: build one interactive Artifact with brand tokens from project knowledge.",
        "Use v2/v3 numbered changes, not 'try again'.",
        "Snapshot v-final before risky redesigns.",
        "Archive templates to knowledge so next campaign starts warm.",
        "Comment AI on the post for the Artifact prompt pack.",
        "Follow @piyush.glitch for operator-level breakdowns.",
    ],
    "13_Claude_MCP_For_Operators": [
        "MCP is how Claude touches live systems - read-first, hooks-gated, context-budgeted.",
        "This week: one read-only MCP (GitHub or Postgres replica) with project scope.",
        "Run claude mcp list and /mcp auth before declaring victory.",
        "Add PreToolUse before any write connector.",
        "Keep enabled MCPs under ten.",
        "Comment AI on the post for the .mcp.json starter.",
        "Follow @piyush.glitch for MCP ops without hype.",
    ],
    "14_Claude_Sonnet_vs_Opus": [
        "Model routing is an operating policy - Sonnet for volume, Opus for judgment.",
        "Tag your last 20 tasks by risk this week.",
        "Publish the routing matrix where your team actually works.",
        "Track human edit minutes, not just API spend.",
        "Escalate after three Sonnet correction rounds.",
        "Comment AI on the post for the printable cheat sheet.",
        "Follow @piyush.glitch for cost-aware AI ops.",
    ],
    "15_Claude_For_Research_And_Writing": [
        "Research quality is input quality - source packets, claim tables, UNKNOWN over guessing.",
        "Create a Research Project with citation rules today.",
        "Run the master research prompt on one real decision.",
        "Human-verify every number before external send.",
        "Archive approved writing dated in knowledge.",
        "Comment AI on the post for the full prompt pack.",
        "Follow @piyush.glitch for research workflows that audit.",
    ],
}
