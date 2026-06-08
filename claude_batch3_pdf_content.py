# -*- coding: utf-8 -*-
"""Rich PDF content for Claude business carousels 16-20."""

BATCH3_CONTENT = {
    "16_Claude_Opus_4_8_Upgrade": {
        "title": "Claude Opus 4.8 Upgrade Guide",
        "subtitle": "What changed from 4.7 - and what to switch today without breaking production.",
        "kicker": "AI FOR BUSINESS - 16",
        "intro": (
            "Anthropic released Claude Opus 4.8 on May 28, 2026 - six weeks after Opus 4.7. Same API pricing "
            "($5/M input, $25/M output) but measurable gains in agentic coding, knowledge work and long-running "
            "autonomy. For business operators, the upgrade is not hype: cleaner tool calls, adaptive thinking "
            "that saves tokens on easy turns, effort controls on claude.ai, fast mode on API, and dynamic "
            "workflows in Claude Code. This guide is the migration checklist teams actually need."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "4.7 vs 4.8 at a glance",
                "body": [
                    "Opus 4.7 (April 16, 2026) brought stronger coding, vision and multi-step consistency. "
                    "Opus 4.8 builds on that with better agent reliability and less wasted output (Anthropic noted "
                    "fixes to comment verbosity and tool-calling issues seen in 4.7).",
                ],
                "bullets": [
                    ("Agentic coding", "64.3% to 69.2% on Anthropic internal benchmark."),
                    ("Knowledge work", "Score 1753 to 1890."),
                    ("Agentic financial analysis", "51.5% to 53.9%."),
                    ("Pricing", "Unchanged from 4.7 - no budget excuse to delay testing."),
                ],
            },
            {
                "tab": "02",
                "title": "New features that matter for ops",
                "body": [
                    "Effort control (claude.ai): high default, extra/xhigh and max for harder tasks. Fast mode "
                    "(API research preview): speed:fast for 2.5x output tokens/sec at premium rate - now 3x "
                    "cheaper than previous fast mode. Dynamic workflows (Claude Code preview): larger autonomous "
                    "engineering tasks. Adaptive thinking: reasons only when turn needs it.",
                ],
            },
            {
                "tab": "03",
                "title": "API migration",
                "body": [
                    "Change model ID from claude-opus-4-7 to claude-opus-4-8. Prompt cache minimum drops to "
                    "1024 tokens (was higher on 4.7) - more prompts qualify for caching with zero code change. "
                    "Constraints unchanged from 4.7 - code running on 4.7 needs no structural changes.",
                ],
            },
        ],
        "playbook": [
            "Run eval suite on 4.8 with claude-opus-4-8 before full traffic cutover.",
            "Compare human_edit_minutes on 20 golden tasks 4.7 vs 4.8.",
            "Enable adaptive thinking for bimodal workloads (simple + complex in one agent).",
            "Test fast mode on latency-sensitive async jobs only after cost modeling.",
            "Update internal docs: default effort high; escalate to extra for board/legal/architecture.",
            "Claude Code teams: pilot dynamic workflows on one repo before org-wide.",
        ],
        "mistakes": [
            "Switching production without re-running agent evals.",
            "Using max effort on every request - burns tokens on easy tasks.",
            "Ignoring 4.7 support window - migrate deliberately, not panic Friday night.",
            "Assuming fast mode is default - it is opt-in with premium pricing.",
        ],
        "glossary": [
            ("claude-opus-4-8", "API model ID for Opus 4.8."),
            ("Adaptive thinking", "Model reasons only when turn complexity warrants it."),
            ("Effort levels", "high, extra/xhigh, max - user-controlled depth on claude.ai."),
            ("Fast mode", "API speed:fast for 2.5x output speed at premium rate."),
        ],
        "callout": {
            "title": "Hidden upgrade win",
            "text": "1024-token cache minimum means short system prompts + few-shot examples now cache on 4.8 "
                    "when they did not on 4.7 - instant cost drop for some production apps.",
        },
    },
    "17_GPT_Image_2_Claude_Prompts": {
        "title": "GPT Image 2 + Claude Prompt Ops",
        "subtitle": "Claude writes the brief. GPT Image 2 renders pixels. You own QC.",
        "kicker": "AI FOR BUSINESS - 17",
        "intro": (
            "GPT Image 2 (gpt-image-2-all class models) excels at generation and edit. It does not excel at "
            "brand strategy, shot planning or fixing failed QC passes. Elite brand teams use Claude first: "
            "extract visual DNA from references, write structured prompt grammar, build shot lists, iterate "
            "prompts from failure analysis, and run final QC checklists. This is the two-tool production stack "
            "that turns random AI images into campaign assets."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "Why prompt in Claude first",
                "body": [
                    "Image models optimize pixels not brand consistency. Claude holds brand rules, competitor "
                    "constraints, legal NEVER lists and reference analysis in one thread. Output: a generation "
                    "prompt + negative constraints + QC checklist - not a paragraph of vibes.",
                ],
            },
            {
                "tab": "02",
                "title": "Brand prompt grammar",
                "body": [
                    "Structure every generation prompt: SUBJECT, ENVIRONMENT, LIGHTING, CAMERA/LENS, RATIO, "
                    "MATERIALS, NEVER list, REFERENCE NOTES. Claude enforces this from brand-world.md in a Project.",
                ],
                "bullets": [
                    ("SUBJECT", "Product hero, model pose, scale vs environment."),
                    ("NEVER", "Wrong logo, extra fingers, off-brand hex, readable gibberish text."),
                    ("RATIO", "9:16, 4:5, 1:1 - stated first line not buried."),
                ],
            },
            {
                "tab": "03",
                "title": "Iteration loop",
                "body": [
                    "Generate in GPT Image 2. Upload fail to Claude with: what broke, which ref was ignored, "
                    "target fix. Claude returns prompt v2 with surgical changes - not regenerate from scratch.",
                ],
            },
        ],
        "playbook": [
            "Create Claude Project with brand-world.md and 10 approved reference images.",
            "Claude extracts visual DNA doc from refs before any generation.",
            "Claude outputs 8-slide shot list for carousel campaign.",
            "Generate each shot in GPT Image 2 with sidecar JSON (prompt, refs, ratio).",
            "Upload outputs to Claude for QC pass/fail per checklist.",
            "Archive approved prompt + refs in library for reuse.",
        ],
        "mistakes": [
            "Typing prompts directly in image API with no brand grammar.",
            "No NEVER list - hands and logos fail repeatedly.",
            "Skipping sidecar JSON - cannot reproduce hero shots.",
            "One-shot generation without v2 iteration protocol.",
        ],
        "glossary": [
            ("Visual DNA", "Extracted lighting, palette, camera, materials from approved refs."),
            ("Sidecar JSON", "Prompt + model + refs + ratio saved beside each PNG."),
            ("Shot list", "Planned frames before generation - hero, detail, lifestyle, macro."),
        ],
        "callout": {
            "title": "Power Claude prompt",
            "text": "Analyze these 5 approved refs. Extract visual DNA. Write GPT Image 2 prompt for slide 3 "
                    "lifestyle shot: product in use, 9:16, coral accent lighting, NEVER readable text on product.",
        },
    },
    "18_Meta_Business_Claude_Connector": {
        "title": "Meta Business + Claude Connector",
        "subtitle": "Official Meta Ads MCP - 29 tools, OAuth setup, prompts that save agency hours.",
        "kicker": "AI FOR BUSINESS - 18",
        "intro": (
            "On April 29, 2026 Meta launched official Ads AI Connectors: MCP server at https://mcp.facebook.com/ads "
            "and CLI @meta/ads-cli. Claude Desktop and claude.ai can connect via Settings > Connectors, OAuth "
            "with Business Manager, and call 29 Marketing API tools in natural language. Open beta is free for "
            "eligible advertisers. This is not a replacement for media buying strategy - it is a speed layer "
            "for reporting, diagnostics and guarded operations when your data and guardrails are clean."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "What the connector exposes",
                "body": [
                    "29 tools across performance reporting, campaign management, catalog management and signal "
                    "diagnostics - same Marketing API underneath as Ads Manager, conversational interface on top.",
                ],
                "bullets": [
                    ("Read-first", "Weekly performance digest, creative fatigue scan, pacing checks."),
                    ("Write gated", "Pause ad sets, budget changes - human approval required."),
                    ("Limits", "Admin-level Business Manager access typically required for MCP rollout."),
                ],
            },
            {
                "tab": "02",
                "title": "Setup in Claude Desktop / claude.ai",
                "body": [
                    "Settings > Connectors (or Features > MCP) > Add custom connector > Remote URL: "
                    "https://mcp.facebook.com/ads > Connect > Meta OAuth > select ad accounts and scopes.",
                    "Free tier: one custom connector. Pro/Max: multiple. Team/Enterprise: org owner adds first.",
                ],
            },
            {
                "tab": "03",
                "title": "Safety before speed",
                "body": [
                    "Week 1 read-only: ads_read scope, log every tool call, validate answers against Ads Manager. "
                    "Week 2+: add write scopes with approval hooks. Train AI with clean naming conventions and "
                    "documented KPI definitions - garbage account structure produces garbage recommendations.",
                ],
            },
        ],
        "playbook": [
            "Verify is_ads_mcp_enabled on your account (gradual rollout).",
            "Add connector URL in Claude Settings.",
            "OAuth with admin Business Manager account.",
            "Run 5 read-only golden prompts; compare to Ads Manager exports.",
            "Document allowed write actions in Project instructions.",
            "Weekly audit: tool calls log vs human approvals.",
        ],
        "mistakes": [
            "Write access on day one without read validation.",
            "Analyst-level permissions - MCP may fail or scope limited.",
            "Trusting AI budget pauses without human sign-off.",
            "Messy ad account naming - AI summarizes chaos confidently.",
        ],
        "glossary": [
            ("Meta Ads MCP", "Official connector at mcp.facebook.com/ads."),
            ("ads_read", "Read-only scope for reporting and diagnostics."),
            ("Business Manager", "Meta container for ad accounts, pages, permissions."),
        ],
        "callout": {
            "title": "8-hour-saving prompt",
            "text": "Pull last 7 days performance by campaign. Flag ad sets with CTR down 20%+ WoW and spend "
                    "above $500. Rank by severity. Do NOT pause anything - recommend only.",
        },
    },
    "19_Claude_Daily_Business_Ops": {
        "title": "Claude Daily Business Operations",
        "subtitle": "Morning brief to EOD recap - repeatable Projects that save 30+ minutes daily.",
        "kicker": "AI FOR BUSINESS - 19",
        "intro": (
            "Most professionals use Claude reactively - paste a problem, get an answer, lose the thread. "
            "Operators use Claude as daily infrastructure: same Project, same instruction blocks, same output "
            "formats every morning and evening. Inbox triage, meeting prep, decision memos and team recaps "
            "become 5-minute rituals instead of 45-minute context rebuilds."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "Daily ops Project structure",
                "body": [
                    "One Claude Project: Daily Ops. Instructions define four modes - MORNING, INBOX, MEETING, EOD. "
                    "Upload: team roster.md, KPI definitions, decision template.md, banned-phrases for external comms.",
                ],
            },
            {
                "tab": "02",
                "title": "Morning brief (5 min)",
                "body": [
                    "Paste: today's calendar, yesterday Slack highlights, one KPI screenshot or metrics snippet. "
                    "Output: top 5 priorities with owner, one blocker, one ask for leadership.",
                ],
                "code": {
                    "caption": "Morning brief prompt",
                    "lines": "MODE: MORNING\nInput attached: calendar, slack, KPIs.\nOutput:\n1. Top 5 priorities (owner + deadline)\n2. One blocker needing escalation\n3. One decision I must make today\nMax 200 words. No fluff.",
                },
            },
            {
                "tab": "03",
                "title": "End of day recap",
                "body": [
                    "Paste: what you completed, open threads, tomorrow calendar preview. Output: Slack-ready EOD "
                    "for team channel - shipped, blocked, tomorrow top 3.",
                ],
            },
        ],
        "playbook": [
            "Create Daily Ops Project with four mode blocks in instructions.",
            "Pin morning and EOD starter prompts in project description.",
            "Run morning brief before first meeting daily for 2 weeks.",
            "Track minutes saved vs old manual process.",
            "Add meeting prep mode when morning brief is stable.",
            "Archive great EOD formats to knowledge/exemplars/.",
        ],
        "mistakes": [
            "New chat every morning - no accumulated instructions.",
            "Pasting sensitive PII without redaction policy.",
            "Using Claude for final external send without human read.",
            "No fixed output format - inconsistent team comms.",
        ],
        "glossary": [
            ("Mode block", "Instruction section triggered by MODE: keyword in prompt."),
            ("EOD recap", "End-of-day team update in fixed format."),
            ("Decision memo", "Options, recommendation, what would change my mind."),
        ],
        "callout": {
            "title": "Inbox triage prompt",
            "text": "MODE: INBOX. Sort these 20 emails into: REPLY NOW (draft reply), DELEGATE (who + one line), "
                    "ARCHIVE, NEEDS DATA (what missing). Do not send - draft only.",
        },
    },
    "20_Claude_Business_Playbook_2026": {
        "title": "Claude Business Playbook 2026",
        "subtitle": "Five investments that compound - stop treating Claude like a chat toy.",
        "kicker": "AI FOR BUSINESS - 20",
        "intro": (
            "Random Claude chats do not scale. Business ROI comes from five investments: Team Projects (shared "
            "memory), model routing (Sonnet volume / Opus 4.8 judgment), live MCP connectors (Meta, GitHub, DB), "
            "Artifacts (deliverables not paragraphs), and versioned team SOPs (starter prompts in git with an "
            "AI ops owner). This playbook ties the carousel series into one operating system you can present "
            "to leadership with hours saved, not demo videos."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "The five investments",
                "body": [
                    "Each investment is thin-but-complete before adding the next. Clone the first workflow template "
                    "across departments instead of reinventing.",
                ],
                "bullets": [
                    ("Projects", "Shared instructions + knowledge per outcome."),
                    ("Routing", "Sonnet default, Opus 4.8 for tier-3, Haiku classify."),
                    ("Connectors", "Read-first MCP; Meta Ads, GitHub, Postgres replica."),
                    ("Artifacts", "Calculators, memos, decks in side panel."),
                    ("SOPs", "Starter prompts versioned; weekly failure review."),
                ],
            },
            {
                "tab": "02",
                "title": "ROI math leadership understands",
                "body": [
                    "10 minutes saved x 5 days x 10 people = 500 minutes/week = 33 hours/week. Track one workflow "
                    "metric for 4 weeks before scaling spend. Report intervention rate and incidents alongside hours.",
                ],
            },
            {
                "tab": "03",
                "title": "AI ops owner",
                "body": [
                    "Name one person (even 20% role) who owns: Project instruction changes, connector approvals, "
                    "eval suites, starter prompt library. Without ownership, tools sprawl and quality drifts.",
                ],
            },
        ],
        "playbook": [
            "Pick highest-volume weekly task (e.g. pipeline digest).",
            "Build all five investments thin around that one task.",
            "Measure hours saved + human edit rate for 4 weeks.",
            "Present one slide to leadership with numbers.",
            "Clone template to second workflow.",
            "Quarterly audit: kill workflows with >25% intervention rate.",
        ],
        "mistakes": [
            "Connecting ten tools with no Projects or SOPs.",
            "No named owner - everyone edits instructions.",
            "Demos without metrics - budget gets cut.",
            "Skipping read-only connector phase.",
        ],
        "glossary": [
            ("AI ops owner", "Named maintainer of Projects, connectors, SOPs, evals."),
            ("Intervention rate", "Percent of AI outputs requiring major human rewrite."),
            ("Thin-but-complete", "All layers present minimally before scaling scope."),
        ],
        "callout": {
            "title": "Leadership one-pager prompt",
            "text": "Summarize our Claude operating system in 300 words for CEO: workflows live, hours saved "
                    "last month, connectors (read vs write), incidents, library assets count, next quarter plan.",
        },
    },
}
