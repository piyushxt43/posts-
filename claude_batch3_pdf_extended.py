# -*- coding: utf-8 -*-
"""Extended PDF blocks for Claude business carousels 16-20."""

BATCH3_EXTENDED = {
    "16_Claude_Opus_4_8_Upgrade": {
        "carousel_slides": [
            ("1", "4.7 Was Great. 4.8 Is Default.", "May 28 2026 upgrade same price."),
            ("2", "Benchmark Gains", "Coding, knowledge work, financial analysis up."),
            ("3", "Effort Control", "high, extra, max on claude.ai."),
            ("4", "Fast Mode", "2.5x speed API research preview."),
            ("5", "Dynamic Workflows", "Claude Code large autonomous tasks."),
            ("6", "Adaptive Thinking", "Reason when needed save tokens."),
            ("7", "Migration Checklist", "claude-opus-4-8 eval first."),
            ("8", "Comment AI", "Get migration PDF."),
        ],
        "extra_sections": [
            {
                "tab": "04",
                "title": "Benchmark table (Anthropic published)",
                "body": [
                    "Use these to justify migration testing to engineering and finance - not as gospel, "
                    "as directional signal that 4.8 fixes 4.7 pain points in agentic workloads.",
                ],
                "bullets": [
                    ("Agentic coding", "64.3% (4.7) -> 69.2% (4.8)."),
                    ("Multidisciplinary reasoning + tools", "54.7% -> 57.9%."),
                    ("Agentic computer use", "82.8% -> 83.4%."),
                    ("Knowledge work score", "1753 -> 1890."),
                    ("Agentic financial analysis", "51.5% -> 53.9%."),
                ],
            },
            {
                "tab": "05",
                "title": "Effort levels explained",
                "body": [
                    "Opus 4.8 defaults to high effort - Anthropic says similar token spend to 4.7 default on "
                    "coding with better results. extra/xhigh for difficult refactors. max for long async jobs "
                    "with increased rate limits.",
                ],
                "code": {
                    "caption": "When to bump effort (internal policy)",
                    "lines": "STANDARD: high (default)\nTRIGGER extra: cross-module refactor, security review, legal precision\nTRIGGER max: overnight async agent job with human review gate\nNEVER max: email shorten, summary, CSV cleanup",
                },
            },
            {
                "tab": "06",
                "title": "Fast mode API",
                "body": [
                    "Set speed:fast on Messages API for up to 2.5x output tokens/sec. Premium: $10/M input, "
                    "$50/M output vs standard $5/$25. Use for user-facing latency SLAs after cost model proves ROI.",
                ],
                "code": {
                    "caption": "API fast mode (research preview)",
                    "lines": "{\n  \"model\": \"claude-opus-4-8\",\n  \"speed\": \"fast\",\n  \"max_tokens\": 4096,\n  \"messages\": [...]\n}",
                },
            },
            {
                "tab": "07",
                "title": "Adaptive thinking migration",
                "body": [
                    "Enable thinking: {type: adaptive} explicitly - off by default like 4.7. Bimodal workloads "
                    "(simple lookups + hard reasoning in one agent) waste fewer thinking tokens.",
                ],
            },
            {
                "tab": "08",
                "title": "Production cutover checklist",
                "body": [
                    "Official docs: platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8",
                ],
                "bullets": [
                    ("Day 1", "Shadow traffic 10% on claude-opus-4-8."),
                    ("Day 3", "Compare eval pass rate and edit minutes."),
                    ("Day 5", "Enable prompt cache - verify 1024 min applies."),
                    ("Day 7", "Full cutover if evals green; rollback ID documented."),
                ],
            },
        ],
        "hidden_tricks": [
            "1024-token cache minimum on 4.8 - re-test caching on short prompts that failed on 4.7.",
            "4.7 API ID claude-opus-4-7 still supported during migration - no forced Friday switch.",
            "Adaptive thinking off unless you set it - same as 4.7, avoids surprise token bills.",
            "Fast mode is opt-in premium - do not enable globally without latency SLA justification.",
            "Devin quote in Anthropic launch: 4.8 fixes 4.7 tool-calling verbosity - retest agent evals.",
            "Dynamic workflows Claude Code preview - pilot one repo not org-wide day one.",
            "Effort max gets higher rate limits - use for async batch not interactive chat.",
        ],
    },
    "17_GPT_Image_2_Claude_Prompts": {
        "carousel_slides": [
            ("1", "Claude Briefs. GPT Image 2 Renders.", "Two-tool brand stack."),
            ("2", "Brand Grammar", "SUBJECT ENV LIGHT CAMERA NEVER."),
            ("3", "Visual DNA", "Extract from 5 approved refs."),
            ("4", "Shot List First", "8 slides planned before pixels."),
            ("5", "v2 From Failures", "Surgical prompt fixes not reroll."),
            ("6", "Sidecar JSON", "Reproduce every hero shot."),
            ("7", "QC In Claude", "Hands logo text pass/fail."),
            ("8", "Comment AI", "Get prompt pack PDF."),
        ],
        "extra_sections": [
            {
                "tab": "04",
                "title": "Visual DNA extraction prompt",
                "body": [
                    "Run once per campaign before any GPT Image 2 call.",
                ],
                "code": {
                    "caption": "Claude visual DNA prompt",
                    "lines": "Analyze attached 5 approved brand images.\nOutput visual-dna.md with:\n- Palette (hex)\n- Lighting (direction, softness, color temp)\n- Camera (lens feel, depth of field)\n- Materials and textures\n- Composition patterns\n- NEVER list (3+ concrete failures to avoid)\nNo generation yet - analysis only.",
                },
            },
            {
                "tab": "05",
                "title": "GPT Image 2 prompt template from Claude",
                "body": [
                    "Claude outputs copy-paste block for image API - ratio first line.",
                ],
                "code": {
                    "caption": "Generation prompt structure",
                    "lines": "RATIO: 9:16 vertical\nSUBJECT: [product] on marble surface, 45-degree hero angle\nENVIRONMENT: minimal studio, soft gradient backdrop #F4EEDE\nLIGHTING: key light camera-left, soft fill, subtle rim\nCAMERA: 85mm equivalent, shallow DOF, product sharp\nMATERIALS: brushed aluminum, matte packaging\nNEVER: extra fingers, warped logo, readable fake text, off-brand orange\nREFERENCE NOTES: match lighting density of ref-03.png",
                },
            },
            {
                "tab": "06",
                "title": "Failure iteration prompt",
                "body": [
                    "Upload failed output + original prompt. Claude returns v2 with numbered fixes only.",
                ],
                "code": {
                    "caption": "Prompt v2 from QC fail",
                    "lines": "Original prompt: [paste]\nFailure: logo geometry warped, hands have 6 fingers, background too saturated\nRefs: ref-01 ref-03 unchanged\nOutput: prompt v2 with CHANGES numbered\nDo not regenerate from scratch - minimal delta only.",
                },
            },
            {
                "tab": "07",
                "title": "Carousel shot list prompt",
                "body": [
                    "Plan 8 Instagram slides before generating any image.",
                ],
                "code": {
                    "caption": "8-slide shot list",
                    "lines": "Product: premium wireless earphones\nBrand: cream #F4EEDE coral #EF5E45\nOutput table: Slide | Shot type | Environment | Prompt skeleton | Ratio\nCover must include product hero + lifestyle + macro detail + CTA slide spec",
                },
            },
            {
                "tab": "08",
                "title": "QC checklist prompt",
                "body": [
                    "Final gate before publishing any AI image.",
                ],
                "code": {
                    "caption": "QC pass/fail",
                    "lines": "Compare output to brand-world.md and refs.\nCheck: hands, logo geometry, product shape, hex drift, text legibility, ratio crop.\nOutput: PASS or FAIL per category with fix instruction for FAIL items.",
                },
            },
        ],
        "hidden_tricks": [
            "Compress reference uploads ~1.5MB each - better API success rate.",
            "Ratio phrase first line - '9:16 vertical' beats '4K' or 'square' on adaptive models.",
            "Sidecar JSON next to PNG: prompt, model, refs, ratio, approver name.",
            "NEVER list in every prompt - cuts hand/logo failures 40%+ in practice.",
            "Claude Project with brand-world.md - do not prompt cold each session.",
            "Batch variants share grammar; one-by-one when QC needs per-image approval.",
            "Upload fail image back to Claude - describe breakages specifically not 'make better'.",
        ],
    },
    "18_Meta_Business_Claude_Connector": {
        "carousel_slides": [
            ("1", "Meta Ads In Claude", "Official MCP free beta."),
            ("2", "29 Tools", "Report diagnose manage catalog."),
            ("3", "5-Min Setup", "mcp.facebook.com/ads URL."),
            ("4", "OAuth Scopes", "ads_read first writes gated."),
            ("5", "8 Prompts", "Weekly digest fatigue pacing."),
            ("6", "Limits", "Admin BM rollout gradual."),
            ("7", "Safety", "Log calls human approve writes."),
            ("8", "Comment AI", "Get setup PDF."),
        ],
        "extra_sections": [
            {
                "tab": "04",
                "title": "Step-by-step setup (Claude Desktop)",
                "body": [
                    "Meta launched April 29, 2026. Official endpoint: https://mcp.facebook.com/ads",
                ],
                "bullets": [
                    ("1", "Claude Desktop > Settings > Connectors > Add custom connector."),
                    ("2", "Name: Meta Ads. URL: https://mcp.facebook.com/ads"),
                    ("3", "Click Connect - Meta OAuth opens."),
                    ("4", "Sign in with Business Manager admin account."),
                    ("5", "Select ad accounts and scopes - ads_read first."),
                    ("6", "Restart Claude Desktop. Verify connector Active."),
                ],
                "code": {
                    "caption": "claude.ai web path",
                    "lines": "claude.ai > Avatar > Settings > Connectors > Add Custom Connector\nRemote URL: https://mcp.facebook.com/ads\nOAuth > select accounts > approve",
                },
            },
            {
                "tab": "05",
                "title": "8 prompts that save agency hours",
                "body": [
                    "Read-only week 1. Validate against Ads Manager exports.",
                ],
                "code": {
                    "caption": "Prompt pack (read-only)",
                    "lines": "1. Last 7d performance by campaign - table with spend, CTR, CPA\n2. Ad sets with CTR down 20%+ WoW and spend > $500\n3. Creative fatigue: frequency >3 and CTR declining\n4. Budget pacing vs monthly target\n5. Audience overlap between ad sets A and B\n6. Catalog product feed errors last 24h\n7. Pixel/event signal health summary\n8. Top 5 recommendations - NO pauses or budget changes",
                },
            },
            {
                "tab": "06",
                "title": "CLI alternative for developers",
                "body": [
                    "npm install -g @meta/ads-cli for Claude Code terminal workflows. Marketers use MCP URL in Desktop.",
                ],
            },
            {
                "tab": "07",
                "title": "Rollout errors",
                "body": [
                    "is_ads_mcp_enabled: false means account not in rollout yet. Advertiser/Analyst roles may "
                    "insufficient - need Admin on Business Manager. Free tier limited to one custom connector.",
                ],
            },
            {
                "tab": "08",
                "title": "Post-connect training (critical)",
                "body": [
                    "Connector gives access not judgment. After OAuth: upload account naming doc, KPI "
                    "definitions, creative testing rules to Claude Project. Two things after connect: clean data "
                    "structure and guardrail instructions - or AI spends your budget confidently wrong.",
                ],
            },
        ],
        "hidden_tricks": [
            "Official MCP free in open beta - budget line item is Claude subscription only.",
            "ads_read scope week 1 - prove reporting accuracy before ads_management writes.",
            "Team plan: org Owner must add connector before members use it.",
            "Revoke access anytime: Business Suite > Business Integrations.",
            "Name campaigns consistently - AI summarizes messy accounts with false confidence.",
            "Log tool calls weekly - catch wrong account ID selections early.",
            "Cross-platform Google+Meta needs third-party MCP or manual export - official Meta MCP is Meta only.",
        ],
    },
    "19_Claude_Daily_Business_Ops": {
        "carousel_slides": [
            ("1", "Daily Ops Partner", "Not a weekend toy."),
            ("2", "Morning Brief", "5 priorities before coffee."),
            ("3", "Inbox Triage", "Reply delegate archive."),
            ("4", "Meeting Prep", "Agenda plus 3 questions."),
            ("5", "Decision Memo", "Options recommendation caveats."),
            ("6", "EOD Recap", "Slack-ready team update."),
            ("7", "One Project", "Four MODE blocks."),
            ("8", "Comment AI", "Get daily prompt PDF."),
        ],
        "extra_sections": [
            {
                "tab": "04",
                "title": "Daily Ops Project instructions",
                "body": [
                    "Paste this as project instructions for repeatable daily rituals.",
                ],
                "code": {
                    "caption": "Project instructions skeleton",
                    "lines": "MODES (trigger with MODE: keyword):\nMORNING - priorities from calendar+slack+KPI\nINBOX - sort emails, draft only never send\nMEETING - agenda + 3 questions from attendee context\nEOD - shipped, blocked, tomorrow top 3 for Slack\nFORMAT: bullets, owners, deadlines\nNEVER: invent metrics, send external comms, legal advice",
                },
            },
            {
                "tab": "05",
                "title": "Meeting prep prompt",
                "body": [
                    "Run 3 minutes before any external call.",
                ],
                "code": {
                    "caption": "MODE: MEETING",
                    "lines": "MODE: MEETING\nAttendees: [paste LinkedIn or notes]\nGoal: [one sentence]\nLast notes: [paste]\nOutput:\n- 5-item agenda timed\n- 3 smart questions to ask\n- 2 risks to probe\n- Desired outcome statement",
                },
            },
            {
                "tab": "06",
                "title": "Decision memo prompt",
                "body": [
                    "One page max for leadership decisions.",
                ],
                "code": {
                    "caption": "Decision memo template",
                    "lines": "Decision needed: [X]\nOptions: A / B / C\nPros/cons table\nRecommendation with confidence H/M/L\nWhat would change my mind\nNon-goals: what this memo does not decide",
                },
            },
            {
                "tab": "07",
                "title": "Weekly time audit",
                "body": [
                    "Track minutes saved per ritual for 2 weeks. Typical operators report 25-40 min/day when "
                    "Projects are stable vs ad-hoc chats.",
                ],
            },
        ],
        "hidden_tricks": [
            "Pin MODE: MORNING starter in project description - zero thinking before coffee.",
            "Redact client names in inbox triage pastes if policy requires.",
            "EOD format locked - team learns to scan consistent Slack updates.",
            "Archive best EOD to knowledge - Claude matches tone next week.",
            "Decision memos separate from casual project chat - no tone drift.",
            "Calendar paste + Slack paste only - do not ask Claude to guess priorities.",
            "Friday EOD includes next week top 3 - Monday morning brief is faster.",
        ],
    },
    "20_Claude_Business_Playbook_2026": {
        "carousel_slides": [
            ("1", "Operate Not Experiment", "Systems beat demos."),
            ("2", "Projects", "Shared memory per workflow."),
            ("3", "Routing", "Sonnet volume Opus judgment."),
            ("4", "Connectors", "Live truth not CSVs."),
            ("5", "Artifacts", "Deliverables not paragraphs."),
            ("6", "SOPs", "Versioned starter prompts."),
            ("7", "ROI Math", "33 hours/week example."),
            ("8", "Comment AI", "Get full playbook PDF."),
        ],
        "extra_sections": [
            {
                "tab": "04",
                "title": "Six-layer scorecard (quick audit)",
                "body": [
                    "Rate each 1-5 for your top workflow. Anything below 3 on control blocks scale.",
                ],
                "bullets": [
                    ("Context", "Project instructions + knowledge current?"),
                    ("Tools", "MCP read-only proven?"),
                    ("Workflows", "Starter prompts pinned?"),
                    ("Control", "Human approval on writes?"),
                    ("Evals", "15+ golden cases?"),
                    ("Library", "Approved outputs archived?"),
                ],
            },
            {
                "tab": "05",
                "title": "90-day rollout",
                "body": [
                    "Month 1: one workflow all five investments thin. Month 2: clone to second workflow. "
                    "Month 3: leadership dashboard with hours saved and intervention rate.",
                ],
            },
            {
                "tab": "06",
                "title": "Board slide prompt",
                "body": [
                    "Generate internal board one-pager from your metrics.",
                ],
                "code": {
                    "caption": "CEO summary prompt",
                    "lines": "Workflows live: [list]\nHours saved last month: [N]\nConnectors: [read/write list]\nIncidents: [N]\nLibrary assets: [N]\nIntervention rate: [%]\nNext quarter: [one workflow]\nOutput: 300-word board slide narrative, no hype",
                },
            },
            {
                "tab": "07",
                "title": "Series map (carousels 11-20)",
                "body": [
                    "This series connects: Projects (11), Artifacts (12), MCP (13), Routing (14), Research (15), "
                    "Opus 4.8 (16), Image prompts (17), Meta connector (18), Daily ops (19), Playbook (20).",
                ],
            },
        ],
        "hidden_tricks": [
            "Name AI ops owner in writing - even 20% FTE beats 'everyone owns it'.",
            "Kill workflow if intervention rate >25% for 4 weeks despite context fixes.",
            "Library KPI: count archived approved outputs monthly - compounds like code reuse.",
            "Present ROI as hours saved AND incidents - finance and legal both satisfied.",
            "Clone first win - do not design unique stack per department.",
            "Quarterly delete unused MCP servers and stale Project files.",
            "Connect Opus 4.8 upgrade testing to eval suite from carousel 16.",
        ],
    },
}

BATCH3_FAQS = {
    "16_Claude_Opus_4_8_Upgrade": [
        ("When did 4.8 launch?", "May 28, 2026 - about six weeks after Opus 4.7 (April 16, 2026)."),
        ("Same price as 4.7?", "Yes - $5/M input, $25/M output standard. Fast mode is premium."),
        ("API model ID?", "claude-opus-4-8 via Claude API, Bedrock, Vertex, Foundry."),
        ("Must I upgrade immediately?", "No - test evals first. 4.7 remains supported during migration."),
        ("What is adaptive thinking?", "Reasons only when turn needs it - set thinking: {type: adaptive}."),
        ("Fast mode cost?", "$10/M input, $50/M output - 2.5x speed research preview on API."),
        ("Dynamic workflows?", "Claude Code research preview for larger autonomous engineering tasks."),
        ("Biggest 4.7 pain fixed?", "Tool-calling verbosity and comment noise per partner feedback."),
    ],
    "17_GPT_Image_2_Claude_Prompts": [
        ("Why Claude before image gen?", "Brand grammar, shot lists, QC - image models optimize pixels not strategy."),
        ("What is visual DNA?", "Extracted palette, lighting, camera, materials from approved refs."),
        ("Sidecar JSON?", "Prompt + model + refs + ratio saved beside each file for reproduction."),
        ("NEVER list?", "Concrete failures to avoid - hands, logo warp, off-brand hex."),
        ("Iteration protocol?", "Upload fail, describe breakages, get prompt v2 delta not reroll."),
        ("Ratio first?", "Yes - '9:16 vertical' first line beats vague size words."),
        ("QC in Claude?", "Pass/fail checklist on hands, logo, text, color drift."),
        ("Compress refs?", "~1.5MB per reference improves API success."),
    ],
    "18_Meta_Business_Claude_Connector": [
        ("Official URL?", "https://mcp.facebook.com/ads - Meta launched April 29, 2026."),
        ("Free?", "Open beta free for eligible advertisers; Claude subscription separate."),
        ("How many tools?", "29 across reporting, campaigns, catalog, signals."),
        ("Setup time?", "~5 minutes OAuth in Claude Desktop or claude.ai Connectors."),
        ("Permissions needed?", "Typically Business Manager Admin; gradual rollout applies."),
        ("Read-only first?", "Yes - ads_read week 1, validate against Ads Manager."),
        ("Free tier limit?", "One custom connector on Claude free plan."),
        ("CLI option?", "npm install -g @meta/ads-cli for Claude Code developers."),
    ],
    "19_Claude_Daily_Business_Ops": [
        ("One Project or many chats?", "One Daily Ops Project with MODE blocks."),
        ("Morning brief inputs?", "Calendar, Slack highlights, KPI snippet."),
        ("Inbox mode?", "Sort and draft - never auto-send external email."),
        ("Meeting prep time?", "~3 minutes with attendee context pasted."),
        ("EOD format?", "Shipped, blocked, tomorrow top 3 - Slack ready."),
        ("Time saved?", "Operators report 25-40 min/day when rituals stable."),
        ("PII policy?", "Redact client names if required before paste."),
        ("Decision memo length?", "One page max with what would change my mind section."),
    ],
    "20_Claude_Business_Playbook_2026": [
        ("Five investments?", "Projects, routing, connectors, artifacts, SOPs."),
        ("ROI example?", "10 min x 5 days x 10 people = 33 hours/week saved."),
        ("AI ops owner?", "Named person maintaining Projects, connectors, evals, library."),
        ("When to kill workflow?", "Intervention rate >25% for 4 weeks despite fixes."),
        ("Start where?", "One high-volume weekly task, all layers thin-but-complete."),
        ("Leadership metric?", "Hours saved + incidents + library asset count."),
        ("Relation to carousel series?", "11-20 build one Claude operating system."),
        ("Thin-but-complete?", "All six layers present minimally before scaling scope."),
    ],
}

BATCH3_CASE_STUDIES = {
    "16_Claude_Opus_4_8_Upgrade": (
        "A devtools startup ran 40 agent eval cases on 4.7 vs 4.8 over one week. Pass rate rose 6 points; "
        "median human edit minutes on PR summaries dropped 18%. They cut over on API with claude-opus-4-8 "
        "after enabling adaptive thinking on bimodal support triage - simple tickets stopped burning thinking "
        "tokens. Fast mode reserved for customer-facing status pages with SLA under 3 seconds."
    ),
    "17_GPT_Image_2_Claude_Prompts": (
        "A D2C brand stopped prompting GPT Image 2 directly. Claude Project with brand-world.md produced shot "
        "lists and sidecar JSON for 8-slide launch. QC pass rate went from 40% to 78% first generation because "
        "NEVER lists and ref DNA were enforced before pixels. Hero shot reproduced 3 campaigns from library "
        "without creative director re-briefing."
    ),
    "18_Meta_Business_Claude_Connector": (
        "A 6-person performance agency connected Meta MCP read-only Monday, validated weekly digest prompt "
        "against Ads Manager exports by Wednesday, added write approval gate Friday. Account managers saved "
        "~6 hours/week on reporting; zero unauthorized pauses because Project instructions banned write "
        "tools until human typed APPROVE."
    ),
    "19_Claude_Daily_Business_Ops": (
        "A COO built Daily Ops Project with four MODE blocks. Morning brief before 8am standup, EOD to Slack "
        "at 5:30pm. After 3 weeks the exec team adopted EOD format company-wide. COO tracked 32 min/day saved "
        "vs manual priority setting and inbox sorting in spreadsheets."
    ),
    "20_Claude_Business_Playbook_2026": (
        "A 40-person startup presented one slide after 90 days: 2 workflows live (investor update + pipeline "
        "digest), 41 hours saved/month measured, 2 MCP connectors read-only, 23 library assets, 1 incident "
        "(bad paste fixed with redaction SOP). CEO approved Opus 4.8 Max seats for tier-3 workflows only."
    ),
}

BATCH3_REFERENCE_APPENDIX = {
    "16_Claude_Opus_4_8_Upgrade": {
        "title": "Reference: migration commands and links",
        "body": ["Official: anthropic.com/news/claude-opus-4-8 and platform.claude.com docs."],
        "bullets": [
            ("API ID", "claude-opus-4-8"),
            ("Previous", "claude-opus-4-7 still supported"),
            ("Cache min", "1024 tokens on 4.8"),
            ("Fast mode", "speed: fast in API body"),
            ("Effort", "high default on claude.ai selector"),
        ],
        "code": {
            "caption": "Shadow test curl pattern",
            "lines": "curl https://api.anthropic.com/v1/messages \\\n  -H \"x-api-key: $KEY\" \\\n  -d '{\"model\":\"claude-opus-4-8\",\"max_tokens\":1024,\"messages\":[...]}'",
        },
    },
    "17_GPT_Image_2_Claude_Prompts": {
        "title": "Reference: two-tool pipeline checklist",
        "body": ["Claude Project -> shot list -> GPT Image 2 -> Claude QC -> library archive."],
        "bullets": [
            ("brand-world.md", "Hex, lighting, NEVER list"),
            ("visual-dna.md", "From 5 approved refs"),
            ("sidecar.json", "Beside every approved PNG"),
            ("QC prompt", "Pass/fail per category"),
        ],
        "code": {
            "caption": "sidecar.json example",
            "lines": "{\n  \"prompt\": \"RATIO: 9:16...\",\n  \"model\": \"gpt-image-2-all\",\n  \"refs\": [\"ref-01.png\", \"ref-03.png\"],\n  \"ratio\": \"9:16\",\n  \"approver\": \"name\",\n  \"date\": \"2026-05-31\"\n}",
        },
    },
    "18_Meta_Business_Claude_Connector": {
        "title": "Reference: Meta MCP setup card",
        "body": ["Endpoint: https://mcp.facebook.com/ads | Launch: April 29, 2026 | Tools: 29"],
        "bullets": [
            ("Claude Desktop", "Settings > Connectors > Add custom"),
            ("claude.ai", "Settings > Connectors"),
            ("Scopes", "ads_read first; writes gated"),
            ("CLI", "npm i -g @meta/ads-cli"),
            ("Revoke", "Business Suite > Integrations"),
        ],
        "code": {
            "caption": "Read-only weekly digest",
            "lines": "Using Meta Ads connector READ ONLY:\nLast 7 days by campaign: spend, impressions, CTR, CPA.\nFlag CTR down 20%+ WoW with spend > $500.\nTable format. NO budget or pause changes.",
        },
    },
    "19_Claude_Daily_Business_Ops": {
        "title": "Reference: daily ritual schedule",
        "body": ["Pin these times internally for habit formation."],
        "bullets": [
            ("8:00", "MODE: MORNING - 5 priorities"),
            ("8:30", "MODE: INBOX - triage batch"),
            ("Before calls", "MODE: MEETING - 3 min prep"),
            ("17:30", "MODE: EOD - Slack recap"),
        ],
        "code": {
            "caption": "EOD Slack format",
            "lines": "SHIPPED: [bullets]\nBLOCKED: [bullets + owners]\nTOMORROW TOP 3: [numbered]\nASKS: [one line if any]",
        },
    },
    "20_Claude_Business_Playbook_2026": {
        "title": "Reference: leadership dashboard fields",
        "body": ["Track monthly for board or exec review."],
        "bullets": [
            ("Workflows live", "Count with owners"),
            ("Hours saved", "Measured not estimated"),
            ("Intervention rate", "Major rewrite %"),
            ("Connectors", "Read vs write list"),
            ("Library assets", "Approved outputs count"),
            ("Incidents", "With root cause"),
        ],
        "code": {
            "caption": "Quarterly audit prompt",
            "lines": "Audit our Claude OS:\nList stale Projects, unused MCPs, workflows with intervention >25%.\nRecommend kill, fix, or scale per item.",
        },
    },
}

BATCH3_TROUBLESHOOTING = {
    "16_Claude_Opus_4_8_Upgrade": {
        "title": "Troubleshooting 4.8 migration",
        "body": [
            "Eval pass rate dropped: roll back to claude-opus-4-7 shadow; diff failing cases.",
            "Token bill spiked: check if max effort enabled globally; reset to high default.",
            "Fast mode cost surprise: speed:fast is opt-in premium - audit API logs.",
            "Cache not hitting: verify prompt length >= 1024 tokens on 4.8.",
            "Agent still verbose: re-run evals - 4.8 should improve tool calls vs 4.7.",
        ],
    },
    "17_GPT_Image_2_Claude_Prompts": {
        "title": "Troubleshooting image pipeline",
        "body": [
            "Random outputs: no brand-world.md or NEVER list in Claude Project.",
            "Cannot reproduce hero: missing sidecar JSON.",
            "QC always fails hands: add NEVER extra fingers; shorten on-image text.",
            "Refs ignored: compress to ~1.5MB; name refs explicitly in prompt.",
            "v2 worse than v1: ask Claude for minimal delta not full rewrite.",
        ],
    },
    "18_Meta_Business_Claude_Connector": {
        "title": "Troubleshooting Meta MCP",
        "body": [
            "Connector fails: is_ads_mcp_enabled false - wait rollout or check Admin role.",
            "Wrong account data: verify OAuth selected correct ad account IDs.",
            "Free tier blocked: one connector limit - remove unused connector first.",
            "Bad recommendations: clean account naming and KPI docs in Project first.",
            "Unauthorized pause: remove write scopes until read-only validated 1 week.",
        ],
    },
    "19_Claude_Daily_Business_Ops": {
        "title": "Troubleshooting daily ops",
        "body": [
            "Inconsistent morning output: missing MODE: keyword or Project instructions.",
            "Too long briefs: add max 200 words to instructions.",
            "Hallucinated priorities: paste calendar and Slack only - do not ask Claude to guess.",
            "EOD not adopted: lock format in instructions; archive exemplars.",
            "PII leak: add redaction rule to Project NEVER section.",
        ],
    },
    "20_Claude_Business_Playbook_2026": {
        "title": "Troubleshooting playbook rollout",
        "body": [
            "No ROI proof: pick one workflow metric and measure 4 weeks before scaling.",
            "Tool sprawl: delete unused MCPs; one owner approves new connectors.",
            "Demos not ops: build all five investments on one workflow first.",
            "Leadership skepticism: report incidents alongside hours saved.",
            "Stalled adoption: pin starter prompts; train one ritual not ten.",
        ],
    },
}

BATCH3_MASTERY_PATH = {
    "16_Claude_Opus_4_8_Upgrade": [
        "Day 1: Run 20 eval cases on claude-opus-4-8 shadow traffic.",
        "Day 3: Compare edit minutes vs claude-opus-4-7.",
        "Day 5: Enable adaptive thinking on bimodal agent.",
        "Week 2: Pilot fast mode on one latency-sensitive job.",
        "Week 3: Full API cutover if evals green.",
        "Week 4: Document effort policy for team on claude.ai.",
    ],
    "17_GPT_Image_2_Claude_Prompts": [
        "Week 1: brand-world.md + 10 refs in Claude Project.",
        "Week 2: Visual DNA extraction + 8-slide shot list.",
        "Week 3: GPT Image 2 generation with sidecar JSON.",
        "Week 4: Claude QC gate enforced; library folder live.",
        "Month 2: 30% prompts reused from library.",
        "Month 3: Train designer on QC taxonomy.",
    ],
    "18_Meta_Business_Claude_Connector": [
        "Day 1: Add mcp.facebook.com/ads connector OAuth.",
        "Day 2: Run 5 read-only golden prompts vs Ads Manager.",
        "Week 1: Weekly digest prompt in Project instructions.",
        "Week 2: Document KPI definitions and naming conventions.",
        "Week 3: Write approval gate before any write scope.",
        "Month 2: Expand to second ad account if stable.",
    ],
    "19_Claude_Daily_Business_Ops": [
        "Day 1: Create Daily Ops Project with four MODE blocks.",
        "Week 1: Morning brief daily before standup.",
        "Week 2: Add EOD Slack recap habit.",
        "Week 3: Meeting prep before external calls.",
        "Week 4: Measure minutes saved vs baseline.",
        "Month 2: Team adopts EOD format.",
    ],
    "20_Claude_Business_Playbook_2026": [
        "Week 1: Pick workflow; name AI ops owner.",
        "Week 2: Projects + routing on one task.",
        "Week 3: Read-only MCP + Artifact deliverable.",
        "Week 4: 15 eval cases + first library assets.",
        "Month 2: Clone to workflow #2; leadership slide.",
        "Month 3: Quarterly audit kill/fix/scale.",
    ],
}

BATCH3_EXPERT_DEPTH = {
    "16_Claude_Opus_4_8_Upgrade": {
        "title": "What upgrade leaders do differently",
        "body": [
            "They shadow-test 4.8 on eval suites before cutover, exploit 1024-token cache win immediately, "
            "and document effort policy so max is not default. They treat 4.8 as agent reliability upgrade "
            "not benchmark bragging rights.",
        ],
    },
    "17_GPT_Image_2_Claude_Prompts": {
        "title": "What production brands do differently",
        "body": [
            "They never prompt image APIs cold. Claude owns grammar, shot lists, iteration and QC. Sidecar "
            "JSON on every approve. Library compounds like code reuse.",
        ],
    },
    "18_Meta_Business_Claude_Connector": {
        "title": "What agencies do differently",
        "body": [
            "They connect read-only, validate reporting prompts against Ads Manager, upload account structure "
            "docs, and ban write tools until APPROVE keyword. Connector access without guardrails spends "
            "client budget confidently wrong.",
        ],
    },
    "19_Claude_Daily_Business_Ops": {
        "title": "What executives do differently",
        "body": [
            "They use one Project with MODE blocks at fixed times - not random chats. They measure minutes "
            "saved and archive exemplar EOD formats so the system compounds.",
        ],
    },
    "20_Claude_Business_Playbook_2026": {
        "title": "What scaling teams do differently",
        "body": [
            "They clone thin-but-complete workflows, name an owner, kill high-intervention workflows, and "
            "report hours saved plus incidents to leadership in one slide.",
        ],
    },
}

BATCH3_CLOSING_NOTES = {
    "16_Claude_Opus_4_8_Upgrade": [
        "Opus 4.8 is same price, better agents - test before you cut over.",
        "Run evals on claude-opus-4-8 this week.",
        "Exploit 1024-token cache minimum immediately.",
        "Document effort policy - max is not default.",
        "Comment AI on the post for the migration checklist PDF.",
        "Follow @piyush.glitch for operator-level Claude updates.",
    ],
    "17_GPT_Image_2_Claude_Prompts": [
        "Claude writes the brief. GPT Image 2 renders. You QC.",
        "Build brand-world.md today even if half a page.",
        "Never generate without shot list and NEVER list.",
        "Sidecar JSON on every approved image.",
        "Comment AI for the 20-prompt pack.",
        "Follow @piyush.glitch for brand AI ops.",
    ],
    "18_Meta_Business_Claude_Connector": [
        "Meta official MCP is live at mcp.facebook.com/ads.",
        "Connect read-only this week. Validate against Ads Manager.",
        "Train Claude with clean KPI docs after OAuth.",
        "Human approve every write action.",
        "Comment AI for the 8-prompt pack.",
        "Follow @piyush.glitch for Meta + Claude ops.",
    ],
    "19_Claude_Daily_Business_Ops": [
        "Daily Claude beats random chats - Projects and MODE blocks.",
        "Start tomorrow with MODE: MORNING before standup.",
        "Lock EOD format for Slack by end of week.",
        "Measure minutes saved - do not guess ROI.",
        "Comment AI for the daily prompt PDF.",
        "Follow @piyush.glitch for business AI rituals.",
    ],
    "20_Claude_Business_Playbook_2026": [
        "Five investments: Projects, routing, connectors, artifacts, SOPs.",
        "Pick one workflow and go thin-but-complete.",
        "Name an AI ops owner this week.",
        "Present hours saved to leadership in 30 days.",
        "Comment AI for the full playbook PDF.",
        "Follow @piyush.glitch - carousels 11-20 are one operating system.",
    ],
}
