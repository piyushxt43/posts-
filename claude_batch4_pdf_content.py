# -*- coding: utf-8 -*-
"""Base PDF content for carousels 21-30 (5 tool spotlights + 5 Claude tactics)."""

BATCH4_CONTENT = {
    # ===================== 21 GPT =====================
    "21_GPT_Power_Moves": {
        "title": "GPT Power Moves For Operators",
        "subtitle": "GPT-5.2, Agent mode, Codex and Atlas - stop chatting, start delegating.",
        "kicker": "AI FOR BUSINESS - GPT",
        "intro": (
            "Most people still treat ChatGPT as a smarter search box. The 2026 stack is bigger: GPT-5.2 (Instant "
            "and Thinking), Agent mode that browses and takes actions, Codex for shipping code across terminal/IDE/"
            "cloud, and the Atlas AI browser. The leverage is not better prompts - it is delegating multi-step work "
            "with permission gates and scheduling it to repeat. This guide is the operator playbook for turning "
            "ChatGPT from a chatbot into a worker."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "GPT-5.2: Instant vs Thinking",
                "body": [
                    "GPT-5.2 is the current GPT-5 series upgrade. Instant is the fast workhorse for everyday work, "
                    "how-tos, technical writing and translation. Thinking handles harder tasks - spreadsheet "
                    "formatting, financial modeling, long-document summarizing, step-by-step math and logic.",
                    "Free and Go users default to Instant; pick Thinking from the composer when the task needs depth. "
                    "Automatic reasoning routing was removed so you choose deliberately.",
                ],
                "bullets": [
                    ("Instant", "Drafts, lookups, walkthroughs, translation - warm and fast."),
                    ("Thinking", "Modeling, complex logic, file Q&A, planning with structure."),
                    ("Pick manually", "Select Thinking in the tools menu for high-stakes work."),
                ],
            },
            {
                "tab": "02",
                "title": "Agent mode does the work",
                "body": [
                    "Type /agent or select Agent mode from the tools dropdown. ChatGPT uses its own remote browser to "
                    "navigate sites, fill forms, analyze data and build docs/slides/sheets - narrating progress so you "
                    "can pause, take over, or steer mid-task. It asks permission before consequential actions like "
                    "sending email or submitting forms.",
                ],
                "bullets": [
                    ("Where", "Paid plans: Plus, Pro, Business, Enterprise, Edu. Web, mobile, desktop."),
                    ("Limits", "Pro ~400 messages/month; other paid ~40/month (credit options exist)."),
                    ("Control", "On-screen narration; you confirm important actions."),
                ],
            },
            {
                "tab": "03",
                "title": "Codex and Atlas",
                "body": [
                    "Codex ships code from your terminal, IDE and the cloud - delegate real engineering tasks, not "
                    "snippets. Atlas is OpenAI's AI browser that summarizes pages, compares products and takes action "
                    "across the web. Together with Agent, ChatGPT moves from advice to execution.",
                ],
            },
        ],
        "playbook": [
            "Set Thinking as your default for modeling and analysis; Instant for everyday drafts.",
            "Run one real task in Agent mode (expense entry, itinerary, competitor brief) with approvals on.",
            "Schedule the winning task to repeat (clock icon -> daily/weekly) at chatgpt.com/schedules.",
            "Connect email/calendar/docs as data sources - read-only first.",
            "Use Codex for a contained engineering task before trusting larger refactors.",
            "Document which actions require human confirmation in your team SOP.",
        ],
        "mistakes": [
            "Using Instant for financial modeling then blaming the model for sloppiness.",
            "Letting Agent submit forms or send email without reviewing the narration.",
            "Connecting every data source on day one instead of read-only first.",
            "Treating Agent like a chat - give it a task with a clear done-state.",
        ],
        "glossary": [
            ("GPT-5.2 Instant", "Fast everyday model in the GPT-5 series."),
            ("GPT-5.2 Thinking", "Reasoning model for complex, high-polish tasks."),
            ("Agent mode", "ChatGPT browses and acts with permission gates (/agent)."),
            ("Codex", "OpenAI coding tool across terminal, IDE and cloud."),
            ("Atlas", "OpenAI's AI browser for summarizing and acting on the web."),
        ],
        "callout": {
            "title": "Operator move",
            "text": "Turn a weekly report into an Agent task, approve it once, then schedule it to repeat. You just "
                    "converted a 45-minute Monday ritual into a reviewed 5-minute approval.",
        },
    },
    # ===================== 22 CLAUDE =====================
    "22_Claude_Power_Moves": {
        "title": "Claude Power Moves",
        "subtitle": "Opus 4.8, Projects, Artifacts, Skills and MCP - an operating layer, not a chatbot.",
        "kicker": "AI FOR BUSINESS - CLAUDE",
        "intro": (
            "Claude in 2026 is a business operating layer. Opus 4.8 (May 2026) brings effort control and stronger "
            "agents at the same price as 4.7. Projects give shared team memory. Artifacts ship deliverables beside "
            "chat. Skills package SOPs that load on demand. MCP connects live systems. Most teams use 10% of this. "
            "This guide is the other 90% - the operator stack that turns Claude into infrastructure."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "Opus 4.8 + effort control",
                "body": [
                    "Opus 4.8 defaults to high effort; choose extra (xhigh) or max for harder tasks. Same pricing as "
                    "4.7, better agentic coding and knowledge work, cleaner tool calls, and adaptive thinking that "
                    "saves tokens on simple turns.",
                ],
                "bullets": [
                    ("high", "Default - best balance for most work."),
                    ("extra/xhigh", "Difficult refactors, security review, legal precision."),
                    ("max", "Long async jobs with increased rate limits."),
                ],
            },
            {
                "tab": "02",
                "title": "Projects, Artifacts, Skills",
                "body": [
                    "Projects: persistent instructions + knowledge files load every session - stop re-uploading. "
                    "Artifacts: docs, calculators, charts and mini-apps in an editable side panel. Skills: SKILL.md "
                    "folders that load only when relevant, keeping context clean and output repeatable.",
                ],
                "bullets": [
                    ("Projects", "Shared team memory per workflow."),
                    ("Artifacts", "Deliverables you edit and export, not chat paragraphs."),
                    ("Skills", "Reusable SOPs invoked on demand."),
                ],
            },
            {
                "tab": "03",
                "title": "MCP and model routing",
                "body": [
                    "MCP connects GitHub, Postgres, Slack and even Meta Ads so Claude reads live truth and acts. "
                    "Route models like headcount: Sonnet for volume, Opus for judgment, Haiku to classify. Measure "
                    "human edit minutes, not API cents.",
                ],
            },
        ],
        "playbook": [
            "Create one Project for your highest-value workflow with instructions + 5 knowledge files.",
            "Force deliverables into Artifacts: 'put the full output in an Artifact'.",
            "Package one repeated prompt as a SKILL.md.",
            "Connect one read-only MCP server and validate answers.",
            "Set Sonnet default; reserve Opus 4.8 for tier-3 tasks.",
            "Track edit minutes per task to prove ROI.",
        ],
        "mistakes": [
            "Re-pasting the same docs into new chats instead of using Projects.",
            "Letting long deliverables live in the chat stream.",
            "Using Opus for everything and burning budget.",
            "Enabling 20 MCP servers and shrinking your context window.",
        ],
        "glossary": [
            ("Opus 4.8", "Anthropic's most capable model (May 2026), effort-controlled."),
            ("Project", "Persistent workspace: instructions + knowledge."),
            ("Artifact", "Editable side-panel deliverable."),
            ("Skill", "SKILL.md SOP loaded on demand."),
            ("MCP", "Model Context Protocol - live tool connectors."),
        ],
        "callout": {
            "title": "The 90% move",
            "text": "Combine all four: a Project (memory) + Skills (SOPs) + MCP (live data) + Artifacts (deliverables) "
                    "around one workflow. That is the difference between a chat toy and an operating layer.",
        },
    },
    # ===================== 23 GEMINI =====================
    "23_Gemini_Power_Moves": {
        "title": "Gemini Power Moves",
        "subtitle": "Gemini 3 Pro, 1M context, thinking levels and Deep Think - a reasoning engine, not search.",
        "kicker": "AI FOR BUSINESS - GEMINI",
        "intro": (
            "Gemini quietly became a frontier reasoning model and most people still use it like search. Gemini 3 "
            "Pro carries a 1M-token context window, native multimodality, and a thinking_level control. Deep Think "
            "delivers olympiad-level results in math, physics and chemistry. For operators, the edge is long-context "
            "synthesis, grounded research with citations, and explicit reasoning control. This is the playbook."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "1M context + multimodal",
                "body": [
                    "Gemini 3 Pro comprehends text, audio, images, video, PDFs and entire code repositories within a "
                    "1M-token context window. Drop full contract sets, transcript archives or codebases and ask for "
                    "synthesis without chunking.",
                ],
                "bullets": [
                    ("Long docs", "Entire repos, long contracts, transcript archives."),
                    ("Multimodal", "Text, image, audio, video, PDF, code in one window."),
                    ("Function calling", "Streaming args and multimodal function responses."),
                ],
            },
            {
                "tab": "02",
                "title": "thinking_level and Deep Think",
                "body": [
                    "Set thinking_level (low or high) to balance reasoning depth, latency and cost - it replaced "
                    "thinking_budget for Gemini 3. Deep Think is the specialized reasoning mode for science, math and "
                    "engineering, with gold-medal-level benchmark results; available in the Gemini app for Ultra and "
                    "via API early access.",
                ],
                "bullets": [
                    ("thinking_level: low", "Fast, cheaper, everyday tasks."),
                    ("thinking_level: high", "Complex reasoning, more tokens and latency."),
                    ("Deep Think", "Frontier science/math/engineering reasoning mode."),
                ],
            },
            {
                "tab": "03",
                "title": "Grounding and tiers",
                "body": [
                    "Enable grounding with Google Search for fresh, cited facts - ask for sources and recent-only "
                    "results. A generous personal free tier via Google auth lets you experiment; production runs on "
                    "Vertex AI or API keys.",
                ],
            },
        ],
        "playbook": [
            "Use Gemini 3 Pro for one long-document synthesis you would normally chunk.",
            "Set thinking_level high only when a task genuinely needs depth.",
            "Request grounded citations with a recency constraint on factual queries.",
            "For science/math/engineering, try Deep Think (Ultra app or API early access).",
            "Stream responses on Deep Think to avoid timeouts; raise max_output_tokens.",
            "Prototype on the free tier; move production to Vertex/API.",
        ],
        "mistakes": [
            "Chunking a document that fits in 1M context for no reason.",
            "Leaving thinking_level high on simple tasks - wasted latency and cost.",
            "Expecting Deep Think behavior from a non-Deep-Think model name.",
            "Trusting factual claims without grounding and citations.",
        ],
        "glossary": [
            ("Gemini 3 Pro", "Frontier reasoning model with 1M-token context."),
            ("thinking_level", "low/high control replacing thinking_budget."),
            ("Deep Think", "Specialized science/math/engineering reasoning mode."),
            ("Grounding", "Fresh web facts with citations via Google Search."),
        ],
        "callout": {
            "title": "Reasoning tip",
            "text": "For Deep Think on the API, set temperature 1.0, raise max_output_tokens to 16,384, and stream - "
                    "the thinking portion can dwarf the output and default timeouts will cut it off.",
        },
    },
    # ===================== 24 CURSOR =====================
    "24_Cursor_Power_Moves": {
        "title": "Cursor Power Moves",
        "subtitle": "Cursor 3, Composer 2, parallel agents, Plan Mode, rules, skills and hooks.",
        "kicker": "AI FOR BUSINESS - CURSOR",
        "intro": (
            "Cursor 3 (April 2026) rebuilt the IDE so the agent is the IDE: an Agents Window where each run is a "
            "first-class tab with its own context, model and execution environment. Composer 2 is Cursor's in-house "
            "frontier coding model. Add Plan Mode, the .cursor/rules system, Agent Skills and hooks, and you have a "
            "harness for parallel autonomous work - most users still drive it like autocomplete. This is the upgrade."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "Composer 2 and the Agents Window",
                "body": [
                    "Composer 2 is Cursor's proprietary coding model - fast and cheap, tuned with codebase-wide "
                    "semantic search. The Agents Window treats each agent run as a tab with its own model and "
                    "environment; the model picker lives in the agent tab header (composer-2, auto, or your own keys).",
                ],
                "bullets": [
                    ("composer-2", "In-house model, very fast, large-codebase aware."),
                    ("auto", "Let Cursor route to the best model."),
                    ("Per-tab env", "local, /worktree, cloud sandbox, or remote SSH."),
                ],
            },
            {
                "tab": "02",
                "title": "Parallel agents + Plan Mode",
                "body": [
                    "Run many agents at once; each operates in an isolated git worktree via /worktree so concurrent "
                    "edits never collide. Plan Mode researches your codebase, asks clarifying questions and writes a "
                    "reviewable plan before any code - it saves you from watching the agent build the wrong thing.",
                ],
                "bullets": [
                    ("/worktree", "Isolated branch per agent - no collisions."),
                    ("Plan Mode", "Reviewable plan before writing code."),
                    ("Cloud handoff", "Start in cloud, finish/review locally with screenshots."),
                ],
            },
            {
                "tab": "03",
                "title": "Rules, Skills and hooks",
                "body": [
                    "Use .cursor/rules/*.mdc (Always, Apply Intelligently, glob-scoped, or manual @-mention) instead "
                    "of legacy .cursorrules. Agent Skills are SKILL.md files in .cursor/skills/ with custom slash "
                    "commands and hooks. .cursor/hooks.json runs scripts before/after actions - build loops that "
                    "grind until tests pass. (Skills are in the nightly channel as of early 2026.)",
                ],
            },
        ],
        "playbook": [
            "Switch from .cursorrules to .cursor/rules/*.mdc with clear application modes.",
            "Use Plan Mode for any change touching multiple files.",
            "Run two agents in parallel on separate worktrees for independent features.",
            "Add a .cursor/hooks.json test-fix loop for autonomous grinding.",
            "Author one Agent Skill for a repeated workflow (nightly channel).",
            "Use cloud agents for long refactors; review the diff locally.",
        ],
        "mistakes": [
            "Living in autocomplete while ignoring the Agents Window.",
            "Skipping Plan Mode and letting the agent code the wrong architecture.",
            "Editing the same files with parallel agents without worktrees.",
            "Putting everything in always-on rules and bloating context.",
        ],
        "glossary": [
            ("Cursor 3", "Agent-centric IDE release (April 2026)."),
            ("Composer 2", "Cursor's in-house frontier coding model."),
            ("/worktree", "Isolated git worktree per parallel agent."),
            ("Plan Mode", "Reviewable plan before code."),
            ("Rules", ".cursor/rules/*.mdc project context."),
        ],
        "callout": {
            "title": "Power pattern",
            "text": "Plan Mode -> parallel agents on worktrees -> a hooks.json grind loop until tests pass -> cloud "
                    "handoff for the long refactor. That is Cursor 3 as a harness, not autocomplete.",
        },
    },
    # ===================== 25 DRAFTLY =====================
    "25_Draftly_Power_Moves": {
        "title": "Draftly Power Moves",
        "subtitle": "One deep prompt to a scroll-synced cinematic product site plus matching visuals.",
        "kicker": "AI FOR BUSINESS - DRAFTLY",
        "intro": (
            "Static product pages lose because they look like everyone else's - one hero photo, a stock grid, no "
            "motion, no story. Draftly turns a detailed brief into a launch-ready experience: scroll-synced website "
            "sections, photoreal hero stills, and short product videos in one brand world. No code, no agency. This "
            "guide is the prompt-pipeline playbook for DTC brands where design IS the product."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "One prompt, full experience",
                "body": [
                    "Brief the whole page in one structured prompt: floating nav, hero headline and subcopy, scroll "
                    "sections (feature cards, comparison strip, spec table, testimonial slider), palette, typography "
                    "and motion behavior. Draftly assembles the launch page instead of a flat template.",
                ],
                "bullets": [
                    ("Website prompt", "Nav, hero, sections, palette, motion in one brief."),
                    ("Image prompt", "Lighting, camera, materials, 16:9 frames for scroll."),
                    ("Video prompt", "Short cinematic product reveal in the same world."),
                ],
            },
            {
                "tab": "02",
                "title": "Cinematic scroll motion",
                "body": [
                    "The hero scrubs through extracted frames as the user scrolls, giving hardware-grade motion that "
                    "static banners cannot. This is what proves premium build quality before a customer reads a "
                    "single spec - the same rhythm flagship brands use on launch pages.",
                ],
            },
            {
                "tab": "03",
                "title": "Brand world, locked",
                "body": [
                    "Define palette (hex), typography, lighting, camera feel and a NEVER list once. Every generated "
                    "asset - stills, video, sections - stays on-brand, so you reuse prompts across campaigns instead "
                    "of rebuilding from scratch each season.",
                ],
            },
        ],
        "playbook": [
            "Write a brand-world brief: palette, type, lighting, NEVER list.",
            "Draft the website prompt: nav, hero copy, scroll sections, motion.",
            "Generate hero stills (16:9) for scroll scrubbing.",
            "Add a short product video in the same brand world.",
            "Assemble the scroll-synced page and review on mobile.",
            "Save the prompt set to reuse across the next campaign.",
        ],
        "mistakes": [
            "Shipping a static one-hero page for a premium SKU.",
            "Prompting without a brand-world doc - inconsistent assets.",
            "Skipping mobile review where most traffic lands.",
            "Rebuilding every campaign from scratch instead of reusing prompts.",
        ],
        "glossary": [
            ("Scroll-synced hero", "Background scrubs through frames as you scroll."),
            ("Brand world", "Locked palette, type, lighting, NEVER list."),
            ("Prompt pipeline", "Website + image + video prompts that share a world."),
        ],
        "callout": {
            "title": "Free trial",
            "text": "Comment DRAFTLY on the post to get free trial access on draftly.space and build your first "
                    "scroll-synced product site from one prompt.",
        },
    },
    # ===================== 26 HIDDEN COMMANDS =====================
    "26_Claude_Hidden_Commands": {
        "title": "Claude Code Hidden Commands",
        "subtitle": "70+ slash commands and prompt prefixes most users never discover.",
        "kicker": "CLAUDE TACTICS - COMMANDS",
        "intro": (
            "Claude Code shipped faster than its documentation. Most users know `claude` and five slash commands. "
            "Power users running 10x output know the other 80%: context commands that protect your window, prompt "
            "prefixes that change response behavior, and the three commands that can quietly burn credits for hours. "
            "This is the field guide to the commands and prefixes that actually move the needle."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "Context commands",
                "body": [
                    "/clear wipes the conversation (CLAUDE.md and skills survive). /compact compresses history - add a "
                    "focus so it keeps the constraint you cannot lose. /btw asks a side question without spending main "
                    "context. /context shows a visual grid of usage; /cost shows spend.",
                ],
                "bullets": [
                    ("/compact focus on X", "Lossy summary that preserves what matters."),
                    ("/btw <q>", "Side question, no main-context burn."),
                    ("/clear", "Fresh slate; project memory survives."),
                ],
            },
            {
                "tab": "02",
                "title": "Prompt prefixes",
                "body": [
                    "Prefixes are model-level conventions you type at the start of a prompt. ULTRATHINK forces maximum "
                    "depth; /skeptic challenges your premise; L99 gives a committed, less-hedged answer. Stack 2-3 - "
                    "/skeptic + ULTRATHINK for high-stakes architecture is a common combo.",
                ],
                "bullets": [
                    ("ULTRATHINK", "Maximum reasoning depth."),
                    ("/skeptic", "Challenge the question before answering."),
                    ("L99", "Committed, less-hedged tone."),
                ],
            },
            {
                "tab": "03",
                "title": "Cost and control",
                "body": [
                    "/effort sets reasoning level (low/med/high); /model switches model per task. Beware the burners: "
                    "/loop, /goal + /loop and /schedule can run for hours and bill while you are away. Know which is "
                    "which before you walk off.",
                ],
            },
        ],
        "playbook": [
            "Run /init in any unfamiliar repo to draft CLAUDE.md.",
            "Use /compact focus on <constraint> instead of plain /compact.",
            "Park side questions in /btw to protect context.",
            "Stack /skeptic + ULTRATHINK on architecture decisions.",
            "Set /effort low for bulk work, high for hard reasoning.",
            "Never walk away from /loop or /schedule without a cost cap in mind.",
        ],
        "mistakes": [
            "Using plain /compact and losing the one constraint that mattered.",
            "Never using /btw and bloating the main thread with asides.",
            "Leaving /loop running unattended and getting a surprise bill.",
            "Ignoring prompt prefixes that change output quality for free.",
        ],
        "glossary": [
            ("/compact focus", "Compress context while preserving a stated focus."),
            ("/btw", "Side question without spending main context."),
            ("ULTRATHINK", "Prompt prefix for maximum reasoning depth."),
            ("/loop", "Recurring/long-running task that bills accordingly."),
        ],
        "callout": {
            "title": "Hidden combo",
            "text": "/skeptic + ULTRATHINK on a high-stakes decision: it challenges your framing first, then goes "
                    "maximum depth on the corrected question. Most people never stack prefixes.",
        },
    },
    # ===================== 27 SKILLS =====================
    "27_Claude_Skills_To_Steal": {
        "title": "Claude Skills You Can Steal",
        "subtitle": "SKILL.md folders that package SOPs and load only when relevant.",
        "kicker": "CLAUDE TACTICS - SKILLS",
        "intro": (
            "Skills are the cheat code most teams never set up. A Skill is a folder with a SKILL.md file: YAML "
            "frontmatter (name + description) plus markdown instructions. Claude reads only the metadata at startup "
            "and loads the full skill when the description matches your request - clean context, repeatable output. "
            "They work the same in Claude Code, the API and claude.ai. This guide shows how to author skills worth stealing."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "Anatomy of a Skill",
                "body": [
                    "Create a directory whose name matches the frontmatter `name` (lowercase, numbers, hyphens, max 64 "
                    "chars, no XML tags, no reserved words anthropic/claude). Add SKILL.md with YAML frontmatter then "
                    "markdown instructions. Keep the body under ~500 lines; move depth to references/.",
                ],
                "bullets": [
                    ("name", "Matches directory; lowercase-kebab-case."),
                    ("description", "Up to ~1024 chars; the primary trigger - front-load the use case."),
                    ("body", "Steps, examples, templates, edge cases."),
                ],
            },
            {
                "tab": "02",
                "title": "Progressive disclosure",
                "body": [
                    "Three loading levels: (1) metadata always loaded so Claude can decide relevance; (2) SKILL.md "
                    "body loaded on trigger; (3) bundled references/, assets/ and scripts/ loaded only when needed. "
                    "Scripts run via bash so only their output consumes context.",
                ],
                "bullets": [
                    ("Metadata", "name + description, always pre-loaded."),
                    ("Body", "Loaded when the skill triggers."),
                    ("Resources", "references/, assets/, scripts/ on demand."),
                ],
            },
            {
                "tab": "03",
                "title": "Control invocation",
                "body": [
                    "Frontmatter flags control behavior: disable-model-invocation: true for side-effect commands like "
                    "/deploy, /commit, /send-slack-message (only you can fire them); user-invocable: false for "
                    "background knowledge; allowed-tools to skip per-use approval; model and effort per skill.",
                ],
            },
        ],
        "playbook": [
            "Convert your most-repeated prompt into a SKILL.md with a sharp description.",
            "Add two examples and one counter-example in the body.",
            "Move long reference material into references/ files.",
            "Set disable-model-invocation on anything with side effects.",
            "Test 5 trigger prompts; check Claude's thinking loads the skill.",
            "Store project skills in .claude/skills/ and version them in git.",
        ],
        "mistakes": [
            "Vague description - the skill never triggers.",
            "A 1,000-line SKILL.md that bloats context once loaded.",
            "Letting Claude auto-invoke a /deploy skill with side effects.",
            "XML tags or reserved words in name/description (invalid).",
        ],
        "glossary": [
            ("SKILL.md", "Skill definition: frontmatter + markdown body."),
            ("description", "Trigger field Claude uses to load the skill."),
            ("progressive disclosure", "Metadata -> body -> resources loading."),
            ("disable-model-invocation", "Only the user can fire the skill."),
        ],
        "callout": {
            "title": "Author trick",
            "text": "Ask Claude to write the skill for you: 'Create a SKILL.md for <workflow> with a description that "
                    "triggers on <phrases>.' It formats the frontmatter correctly and you refine the body.",
        },
    },
    # ===================== 28 HOOKS =====================
    "28_Claude_Hooks_Automation": {
        "title": "Claude Hooks And Automation",
        "subtitle": "Scripts that always run on lifecycle events - guardrails the agent cannot skip.",
        "kicker": "CLAUDE TACTICS - HOOKS",
        "intro": (
            "A prompt is a request; a hook is a rule. Hooks are scripts that fire on lifecycle events - before/after "
            "a tool call, on session start, on stop. Unlike 'please remember to lint', a hook always runs. That is "
            "how you block secrets, auto-format diffs, gate writes and build loops that grind until tests pass. This "
            "guide turns soft instructions into deterministic guardrails."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "PreToolUse and PostToolUse",
                "body": [
                    "Hooks live in settings.json under hooks.PreToolUse and hooks.PostToolUse. A PreToolUse hook on Bash "
                    "can regex-scan for sk_live, AKIA or PRIVATE KEY and return a block before the command runs. A "
                    "PostToolUse hook on Write/Edit can auto-run prettier or eslint --fix so the agent never leaves "
                    "messy diffs.",
                ],
                "bullets": [
                    ("PreToolUse", "Inspect and block a tool call before it runs."),
                    ("PostToolUse", "Run formatters/tests after edits."),
                    ("Scope", "user, project or managed settings."),
                ],
            },
            {
                "tab": "02",
                "title": "Deny rules and exit codes",
                "body": [
                    "Deny rules in settings.json beat prompts: block rm -rf, curl | bash and git push --force globally. "
                    "Hooks receive JSON on stdin and signal decisions with exit codes - exit 2 blocks the tool call. "
                    "Parse the JSON to decide per-command.",
                ],
                "bullets": [
                    ("Deny list", "Hard-block dangerous commands everywhere."),
                    ("Exit 2", "Block the tool call from a PreToolUse hook."),
                    ("stdin JSON", "Tool name and args for your logic."),
                ],
            },
            {
                "tab": "03",
                "title": "Grind loops",
                "body": [
                    "A hook that returns a follow-up message can keep the agent iterating until a condition is met - "
                    "for example, run tests and, if they fail, feed the failures back and continue until green. This "
                    "is how teams build autonomous test-fix loops that do not require babysitting.",
                ],
            },
        ],
        "playbook": [
            "Add a PreToolUse hook that blocks secrets in shell commands.",
            "Add a PostToolUse hook that runs your formatter after edits.",
            "Add deny rules for rm -rf, curl | bash, git push --force.",
            "Build a test-fix grind loop hook for one repo.",
            "Log blocked actions so you can audit what the agent tried.",
            "Keep hooks in project scope and version them in git.",
        ],
        "mistakes": [
            "Trusting a prompt to enforce linting instead of a hook.",
            "Wrong event name (PreToolUse vs PostToolUse) so the hook never fires.",
            "Forgetting exit 2 - the tool call is not actually blocked.",
            "No logging - you cannot audit what the agent attempted.",
        ],
        "glossary": [
            ("Hook", "Script that runs on a lifecycle event."),
            ("PreToolUse", "Runs before a tool call; can block it."),
            ("PostToolUse", "Runs after a tool call; auto-fix/format."),
            ("Deny rule", "Global hard-block for dangerous commands."),
        ],
        "callout": {
            "title": "Guarantee, not request",
            "text": "If a rule matters - no secrets, always lint, never force-push - make it a hook or deny rule. "
                    "Prompts get forgotten under pressure; hooks run every single time.",
        },
    },
    # ===================== 29 PROMPTING =====================
    "29_Claude_Prompting_Secrets": {
        "title": "Claude Prompting Secrets",
        "subtitle": "XML tags, gold examples, format contracts and thinking - structure beats wording.",
        "kicker": "CLAUDE TACTICS - PROMPTS",
        "intro": (
            "Claude does not read your mind - it reads your structure. The gap between a vague chat and a reliable "
            "deliverable is not clever wording; it is XML-tagged inputs, two-good-one-bad examples, explicit format "
            "contracts, requested reasoning, and non-goals that stop scope creep. This guide is the structured "
            "prompting playbook that makes Claude output the same quality every time."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "XML tags and examples",
                "body": [
                    "Wrap inputs in tags like <context>, <example>, <rules> so Claude parses sections cleanly instead "
                    "of guessing boundaries. Show two strong examples and one counter-example - this teaches the "
                    "shape and the failure mode better than paragraphs of adjectives.",
                ],
                "bullets": [
                    ("<context>", "Background the model must use."),
                    ("<example>", "Two good, one bad - teach the shape."),
                    ("<rules>", "Always/never constraints, clearly delimited."),
                ],
            },
            {
                "tab": "02",
                "title": "Format contracts and thinking",
                "body": [
                    "State the exact output shape - headings, length, table columns. Ban invented statistics and "
                    "require UNKNOWN when data is missing. On hard tasks, ask for step-by-step reasoning before the "
                    "answer, or enable adaptive thinking on the API so the model reasons only when needed.",
                ],
                "bullets": [
                    ("Schema", "Define headings, length, columns up front."),
                    ("UNKNOWN", "Forbid guessing; require honest gaps."),
                    ("Thinking", "Reason first on complex tasks."),
                ],
            },
            {
                "tab": "03",
                "title": "Non-goals and system prompts",
                "body": [
                    "List what the output must NOT include - the fastest fix for scope creep. Put persona, rules and "
                    "format in Project instructions once so every chat inherits your system prompt instead of "
                    "re-explaining it each time.",
                ],
            },
        ],
        "playbook": [
            "Tag every prompt's inputs with <context>, <example>, <rules>.",
            "Add two gold examples and one counter-example.",
            "Write a format contract: headings, length, columns.",
            "Add a non-goals list to high-stakes prompts.",
            "Request reasoning before the answer on complex tasks.",
            "Move standing rules into Project instructions.",
        ],
        "mistakes": [
            "Pasting unstructured walls of text and hoping.",
            "Adjectives ('professional') instead of examples.",
            "No format contract - inconsistent output shape.",
            "No non-goals - the answer expands every time.",
        ],
        "glossary": [
            ("XML tags", "Delimit prompt sections for clean parsing."),
            ("Format contract", "Explicit output shape and limits."),
            ("Non-goals", "What the output must not include."),
            ("Adaptive thinking", "API reasoning only when the turn needs it."),
        ],
        "callout": {
            "title": "Skeleton that wins",
            "text": "<context> ... </context> <rules> always/never </rules> <example> good/good/bad </example> then: "
                    "'Output: <schema>. Mark UNKNOWN if missing. Non-goals: <list>.' Reuse it everywhere.",
        },
    },
    # ===================== 30 CLAUDE.md =====================
    "30_Claude_md_Mastery": {
        "title": "CLAUDE.md Mastery",
        "subtitle": "The only context that survives /compact - your repo's control plane.",
        "kicker": "CLAUDE TACTICS - MEMORY",
        "intro": (
            "CLAUDE.md is the single highest-leverage file you can add to a repo that uses Claude Code. It loads at "
            "every session start and is the only context that survives /compact. Most repos do not have one, which "
            "is why every session starts cold. This guide shows what to put in it, how to keep it lean, and how to "
            "pair it with output styles and memory so Claude stops re-discovering your project every time."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "What to put in it",
                "body": [
                    "Treat CLAUDE.md as persistent system instructions for the repo: stack, exact commands (test, "
                    "lint, build, deploy), a one-paragraph architecture snapshot so the agent does not guess, and an "
                    "explicit NEVER list (no secrets in commits, no force-push main, no editing generated/).",
                ],
                "bullets": [
                    ("Commands", "Exact test/lint/build/deploy lines."),
                    ("Architecture", "One paragraph on how data flows."),
                    ("NEVER", "Hard boundaries spelled out."),
                ],
            },
            {
                "tab": "02",
                "title": "Keep it lean, load on demand",
                "body": [
                    "Keep the root under ~500 lines. Push domain detail into linked docs in .claude/rules/ and add "
                    "conditional triggers like 'Before editing auth, read docs/auth-flow.md' so the agent fetches "
                    "deep context only when relevant instead of bloating every session.",
                ],
                "bullets": [
                    ("Root < 500 lines", "Short, high-signal."),
                    (".claude/rules/", "Scoped docs loaded as needed."),
                    ("Conditional read", "Trigger deep context only when relevant."),
                ],
            },
            {
                "tab": "03",
                "title": "Output styles and memory",
                "body": [
                    "Use /output-style to switch to Explanatory or Learning modes, or write a custom style file to "
                    "enforce a format. Teach memory once - 'remember our API uses snake_case JSON' - and Claude "
                    "persists the convention so it stops asking. Run /init to generate a starter CLAUDE.md fast.",
                ],
            },
        ],
        "playbook": [
            "Run /init to draft CLAUDE.md, then edit - the draft is a starting point.",
            "Add exact commands and a one-paragraph architecture note.",
            "Write a hard NEVER list.",
            "Move domain depth into .claude/rules/ with conditional triggers.",
            "Set an output style for consistent formatting.",
            "Teach one durable convention to memory this week.",
        ],
        "mistakes": [
            "No CLAUDE.md - every session starts cold.",
            "A 2,000-line file that bloats every session.",
            "Vague 'be helpful' instead of commands and boundaries.",
            "Relying on chat memory that /compact will erase.",
        ],
        "glossary": [
            ("CLAUDE.md", "Repo-root persistent instructions; survives /compact."),
            (".claude/rules/", "Scoped rule docs loaded on demand."),
            ("/output-style", "Switch or customize response format."),
            ("/init", "Auto-generate a starter CLAUDE.md."),
        ],
        "callout": {
            "title": "The leverage line",
            "text": "Add one line: 'Before editing auth, read docs/auth-flow.md.' The agent loads deep context only "
                    "when relevant - lean sessions, no cold starts, fewer wrong guesses.",
        },
    },
}
