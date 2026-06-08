# -*- coding: utf-8 -*-
"""Extended PDF blocks for carousels 21-30. Code-rich, non-generic, 10+ page output."""

BATCH4_EXTENDED = {
    # ===================== 21 GPT =====================
    "21_GPT_Power_Moves": {
        "carousel_slides": [
            ("", "Stop Chatting, Start Delegating", "GPT-5.2 + Agent + Codex + Atlas."),
            ("", "Instant vs Thinking", "Fast workhorse vs deep reasoning."),
            ("", "Agent Mode", "Browses, fills forms, builds docs."),
            ("", "Schedule To Repeat", "Clock icon -> daily/weekly."),
            ("", "Codex Ships Code", "Terminal, IDE and cloud."),
            ("", "Atlas Browser", "Summarize and act on the web."),
            ("", "Connect Your World", "Email, calendar, docs with gates."),
            ("", "Comment AI", "Get the prompt pack."),
        ],
        "extra_sections": [
            {
                "tab": "04", "title": "Agent mode in practice",
                "body": [
                    "Agent runs in its own remote browser and narrates each step. You can interrupt, take over the "
                    "browser (it does not see what you type while you drive), and it asks before consequential "
                    "actions. Deep research lives inside Agent; pick 'deep research' from the composer for longer, "
                    "more detailed runs.",
                ],
                "bullets": [
                    ("Start", "Tools dropdown -> Agent mode, or type /agent."),
                    ("Steer", "Add instructions mid-task; it resumes with new info."),
                    ("Confirm", "Email/forms require your explicit approval."),
                ],
                "code": {
                    "caption": "Agent task brief (paste in Agent mode)",
                    "lines": "TASK: Build a 1-page competitor brief.\nSTEPS:\n1. Visit these 3 sites\n2. Extract pricing + positioning\n3. Compare to us in a table\nOUTPUT: Google Doc, exec summary first.\nDO NOT: submit any forms or sign in anywhere.\nASK ME before any action that leaves a trace.",
                },
            },
            {
                "tab": "05", "title": "Scheduling recurring work",
                "body": [
                    "After a task finishes, click the clock icon to repeat it daily, weekly or monthly. Manage all "
                    "recurring tasks at chatgpt.com/schedules. This turns a reviewed one-off into an ongoing "
                    "automation with a human approval step.",
                ],
                "pro_tip": {
                    "title": "Approval-first automation",
                    "text": "Schedule the task but keep consequential actions gated - you get a draft to approve "
                            "instead of an unsupervised action.",
                },
            },
            {
                "tab": "06", "title": "Model picking discipline",
                "body": [
                    "Free/Go users default to GPT-5.2 Instant; choose Thinking from the tools menu for modeling, long "
                    "documents and step-by-step logic. Automatic reasoning routing was removed, so the choice is "
                    "yours - make it deliberately per task class.",
                ],
            },
            {
                "tab": "07", "title": "Connectors and governance",
                "body": [
                    "Link email, calendar and document repositories as data sources so Agent pulls real context. "
                    "Roll out read-only first, then add write/draft actions with approval. For teams, document which "
                    "actions require confirmation and who owns each scheduled agent.",
                ],
                "code": {
                    "caption": "Team rule of thumb",
                    "lines": "Phase 1: read-only connectors, drafts only\nPhase 2: draft + create doc/email (no send)\nPhase 3: send/submit with human approval\nOwner: named per scheduled agent\nAudit: review chatgpt.com/schedules weekly",
                },
            },
        ],
        "hidden_tricks": [
            "Type /agent to enter Agent mode instantly instead of hunting the tools dropdown.",
            "Pick 'deep research' from the composer when you want a longer, more detailed run than Agent's default.",
            "When Agent takes over the browser, anything you type yourself stays private to you.",
            "Schedule a finished task with the clock icon; manage them all at chatgpt.com/schedules.",
            "Default to Thinking for spreadsheets and financial modeling - Instant cuts corners there.",
            "Give Agent a clear done-state and a DO NOT list, like an SOP - not a chatty request.",
            "Use Codex for contained engineering tasks in terminal/IDE/cloud before trusting big refactors.",
        ],
    },
    # ===================== 22 CLAUDE =====================
    "22_Claude_Power_Moves": {
        "carousel_slides": [
            ("", "The Other 90% Of Claude", "Operating layer, not chatbot."),
            ("", "Opus 4.8 + Effort", "high / extra / max."),
            ("", "Projects = Memory", "Instructions + knowledge persist."),
            ("", "Artifacts", "Deliverables you edit and export."),
            ("", "Skills", "SKILL.md SOPs on demand."),
            ("", "MCP", "Live hands into your stack."),
            ("", "Route Models", "Sonnet / Opus / Haiku."),
            ("", "Comment AI", "Get the operator stack."),
        ],
        "extra_sections": [
            {
                "tab": "04", "title": "Effort control on Opus 4.8",
                "body": [
                    "Opus 4.8 defaults to high effort. Bump to extra (xhigh in Claude Code) for difficult refactors "
                    "and reviews; use max for long async jobs with higher rate limits. On the API, enable adaptive "
                    "thinking so simple turns do not burn reasoning tokens.",
                ],
                "code": {
                    "caption": "Effort policy (team SOP)",
                    "lines": "STANDARD: high (default)\nextra/xhigh: cross-module refactor, security/legal review\nmax: overnight async agent with human review gate\nAPI: thinking { type: adaptive } for bimodal workloads",
                },
            },
            {
                "tab": "05", "title": "Projects as team memory",
                "body": [
                    "Projects store instructions (a persistent system prompt) and knowledge files (~200K tokens) that "
                    "load every session. Chat history inside a project does NOT auto-share across chats - export "
                    "decisions to a knowledge file. On Team/Enterprise, share with Can use vs Can edit.",
                ],
                "code": {
                    "caption": "Project instructions skeleton",
                    "lines": "WHO: [Company] [role] assistant.\nRULES: cite uploaded files; never invent pricing/names.\nFORMAT: exec summary -> detail -> next actions (owner+date).\nESCALATE: say 'Needs human review' for legal/HR/pricing.",
                },
            },
            {
                "tab": "06", "title": "Artifacts and Skills",
                "body": [
                    "Force deliverables into Artifacts: 'put the full output in an Artifact; chat only for questions.' "
                    "Iterate with v2/v3 in place. Package repeated SOPs as SKILL.md folders that load only when their "
                    "description matches - clean context, repeatable output.",
                ],
                "pro_tip": {
                    "title": "Compounding library",
                    "text": "Save approved Artifacts back into project knowledge as templates/. Your library compounds "
                            "like code reuse instead of starting from a blank chat every time.",
                },
            },
            {
                "tab": "07", "title": "MCP and routing",
                "body": [
                    "Connect read-only MCP first (GitHub, Postgres replica, even Meta Ads at mcp.facebook.com/ads). "
                    "Keep enabled servers under ~10 to protect context. Route Sonnet for volume, Opus 4.8 for "
                    "judgment, Haiku to classify; track human edit minutes per task, not API cents.",
                ],
            },
        ],
        "hidden_tricks": [
            "Force Artifact-only mode so deliverables are editable/exportable, not buried in chat.",
            "Upload EXAMPLE- gold outputs to knowledge; Claude matches structure faster than tone paragraphs.",
            "Chat does not auto-share across project chats - export decisions to a knowledge .md within 24h.",
            "Set Sonnet as default; reserve Opus 4.8 for tier-3 with TRIGGER KEYWORDS in instructions.",
            "Enable adaptive thinking on the API to stop burning reasoning tokens on simple turns.",
            "Keep enabled MCP servers under 10 or your 200K window shrinks toward ~70K usable.",
            "One 'Can edit' owner per Project; everyone else 'Can use' to stop instruction drift.",
        ],
    },
    # ===================== 23 GEMINI =====================
    "23_Gemini_Power_Moves": {
        "carousel_slides": [
            ("", "A Reasoning Engine", "Not autocomplete."),
            ("", "1M Token Context", "Repos, contracts, transcripts."),
            ("", "thinking_level", "low / high control."),
            ("", "Deep Think", "Science, math, engineering."),
            ("", "Multimodal Native", "Text, image, audio, video, PDF."),
            ("", "Grounding", "Fresh facts with citations."),
            ("", "Free Tier Edge", "Experiment then scale on Vertex."),
            ("", "Comment AI", "Get the prompt pack."),
        ],
        "extra_sections": [
            {
                "tab": "04", "title": "Using the 1M window well",
                "body": [
                    "Gemini 3 Pro handles entire repos, long contracts and transcript archives in one context. Do not "
                    "chunk what fits. Ask it to flag conflicts between sources rather than smoothing them, and to "
                    "cite which document each claim came from.",
                ],
                "code": {
                    "caption": "Long-context synthesis prompt",
                    "lines": "You have the full repo/contract set below.\nTASK: summarize decisions + open risks.\nCITE the file/section for each claim.\nFLAG conflicts between sources in a CONFLICTS section.\nMark UNKNOWN if not present. Do not chunk.",
                },
            },
            {
                "tab": "05", "title": "thinking_level and Deep Think (API)",
                "body": [
                    "thinking_level (low/high) replaced thinking_budget for Gemini 3 - it balances depth, latency and "
                    "cost. Deep Think is the specialized reasoning mode; use a Deep Think-capable model name, set "
                    "temperature 1.0, raise max_output_tokens, and stream to avoid timeouts.",
                ],
                "code": {
                    "caption": "Deep Think config (google-generativeai)",
                    "lines": "model = genai.GenerativeModel('gemini-3-0-deep-think')\nresp = model.generate_content(\n  prompt,\n  generation_config=GenerationConfig(\n    max_output_tokens=16384,\n    temperature=1.0))\n# stream to avoid 30-60s client timeouts",
                },
            },
            {
                "tab": "06", "title": "Grounding with Search",
                "body": [
                    "Turn on grounding for fresh, cited facts. Always ask for sources and constrain recency ('only "
                    "sources from the last 12 months'). Separate grounded facts from the model's inference so you can "
                    "verify the numbers that matter.",
                ],
            },
            {
                "tab": "07", "title": "Tiers and production",
                "body": [
                    "A generous personal free tier (Google auth) is great for prototyping. Production scales on Vertex "
                    "AI or API keys. Monitor usage_metadata to track thinking-token consumption - on complex tasks "
                    "the thinking portion can dwarf the visible output.",
                ],
                "code": {
                    "caption": "Watch token spend",
                    "lines": "resp = model.generate_content(prompt, stream=True)\nfor chunk in resp:\n    handle(chunk)\nprint(resp.usage_metadata)  # thinking + output tokens",
                },
            },
        ],
        "hidden_tricks": [
            "Stop chunking documents that fit in the 1M window - paste the whole thing and ask for synthesis.",
            "thinking_level replaced thinking_budget on Gemini 3 - use low for everyday, high only when needed.",
            "Deep Think needs temperature=1.0; other values degrade its reasoning quality.",
            "Raise max_output_tokens to 8k-16k for Deep Think or the reasoning gets truncated mid-thought.",
            "Stream Deep Think responses - default 30-60s HTTP timeouts will otherwise cut it off.",
            "Ask for citations with a recency filter to keep grounded facts trustworthy.",
            "Monitor usage_metadata - thinking tokens can dwarf output and drive the bill on hard tasks.",
        ],
    },
    # ===================== 24 CURSOR =====================
    "24_Cursor_Power_Moves": {
        "carousel_slides": [
            ("", "The Agent Is The IDE", "Cursor 3 Agents Window."),
            ("", "Composer 2", "Cursor's in-house model."),
            ("", "Parallel Agents", "Each in its own /worktree."),
            ("", "Plan Mode First", "Reviewable plan before code."),
            ("", "Rules > .cursorrules", ".cursor/rules/*.mdc."),
            ("", "Skills + Hooks", "Grind until tests pass."),
            ("", "Cloud Handoff", "Refactor in cloud, finish local."),
            ("", "Comment AI", "Get the starter pack."),
        ],
        "extra_sections": [
            {
                "tab": "04", "title": "Rules the modern way",
                "body": [
                    "Use .cursor/rules/*.mdc instead of legacy .cursorrules. Each rule has an application mode: Always "
                    "Apply, Apply Intelligently (agent reads the description and decides), Apply to Specific Files "
                    "(glob), or Apply Manually (@-mention). User Rules apply globally across projects.",
                ],
                "code": {
                    "caption": ".cursor/rules/api.mdc",
                    "lines": "---\ndescription: API conventions for /server\nglobs: server/**/*.ts\nalwaysApply: false\n---\n- snake_case JSON keys\n- All routes validated with zod\n- Never log request bodies with PII",
                },
            },
            {
                "tab": "05", "title": "Agent Skills + hooks",
                "body": [
                    "Agent Skills are SKILL.md files in .cursor/skills/ with custom slash commands and hooks (nightly "
                    "channel as of early 2026). Hooks live in .cursor/hooks.json and run scripts before/after agent "
                    "actions - the basis for loops that iterate until a goal is met.",
                ],
                "code": {
                    "caption": ".cursor/hooks.json (grind-until-green)",
                    "lines": "{\n  \"afterEdit\": [\n    { \"command\": \"node .cursor/hooks/grind.ts\" }\n  ]\n}\n// grind.ts reads stdin, runs tests,\n// returns { followup_message } if tests fail",
                },
            },
            {
                "tab": "06", "title": "Parallel agents on worktrees",
                "body": [
                    "Run multiple agents at once; /worktree gives each an isolated git worktree so concurrent edits "
                    "never collide. Use this to build two independent features in parallel, then review each diff "
                    "separately in the Reviews tab.",
                ],
            },
            {
                "tab": "07", "title": "Plan Mode and cloud handoff",
                "body": [
                    "Plan Mode researches the codebase, asks clarifying questions and produces a reviewable, editable "
                    "plan before any code - the fix for agents confidently building the wrong architecture. Start a "
                    "long refactor on a cloud agent (it produces screenshots/demos) and hand the diff to a local "
                    "agent to finish and review.",
                ],
            },
        ],
        "hidden_tricks": [
            "Migrate .cursorrules to .cursor/rules/*.mdc - it is what Cursor documents and builds against now.",
            "The model picker is in the agent tab header in Cursor 3, not the global chat panel.",
            "Give each parallel agent its own /worktree so edits never collide.",
            "Plan Mode before multi-file changes saves you from 10 minutes of wrong-architecture code.",
            "Agent Skills + hooks live in the nightly channel - set update channel to Nightly to try them.",
            "Cloud agents emit screenshots and demo videos so you verify work without running it yourself.",
            "Composer 2 is tuned for codebase-wide semantic search - lean on it for large-repo navigation.",
        ],
    },
    # ===================== 25 DRAFTLY =====================
    "25_Draftly_Power_Moves": {
        "carousel_slides": [
            ("", "Static Pages Lose", "Cinematic sites sell."),
            ("", "One Prompt, Full Site", "Nav, hero, sections, motion."),
            ("", "Scroll Motion", "Hero scrubs through frames."),
            ("", "Image + Video", "Same brand world."),
            ("", "Brand World Locked", "Palette, type, NEVER list."),
            ("", "Built For DTC", "Lookbook pacing not grids."),
            ("", "Ship In An Afternoon", "Reuse prompts across campaigns."),
            ("", "Comment DRAFTLY", "Free trial access."),
        ],
        "extra_sections": [
            {
                "tab": "04", "title": "The three-prompt pipeline",
                "body": [
                    "Draftly works best as three aligned prompts sharing one brand world: a website prompt (structure "
                    "and motion), an image prompt (photoreal hero frames), and a video prompt (short cinematic "
                    "reveal). Write the brand world once and every asset inherits it.",
                ],
                "code": {
                    "caption": "Website prompt skeleton",
                    "lines": "Floating nav pill: Features, Specs, Pre-order.\nHero headline + subcopy (state both).\nScroll sections: 3 feature cards, comparison strip,\n spec table, testimonial slider, sticky CTA.\nPalette: <hex>. Type: <grotesque>. Motion: hero\n scrubs extracted frames on scroll. No catalog grid.",
                },
            },
            {
                "tab": "05", "title": "Image prompt grammar",
                "body": [
                    "State ratio first, then subject, environment, lighting, camera, materials, and a NEVER list. "
                    "16:9 hero stills give you frames to scroll-scrub; keep negative space for headline overlay.",
                ],
                "code": {
                    "caption": "Hero image prompt",
                    "lines": "RATIO: 16:9 (frames for scroll scrubbing)\nSUBJECT: product hero, 3/4 angle\nENVIRONMENT: charcoal gradient, negative space left\nLIGHTING: soft key upper-left, cool rim right\nMATERIALS: brushed aluminum, matte finish\nNEVER: text, logos, warped geometry, neon blue",
                },
            },
            {
                "tab": "06", "title": "Brand world doc",
                "body": [
                    "Lock palette (hex), typography, lighting, camera feel and a NEVER list in one short doc. Reuse it "
                    "as the header of every prompt so stills, video and sections stay consistent across a campaign.",
                ],
                "pro_tip": {
                    "title": "Reuse beats redo",
                    "text": "Save the winning prompt set per vertical. Next launch starts from a proven world, not a "
                            "blank brief - the same reason agencies keep brand bibles.",
                },
            },
            {
                "tab": "07", "title": "Why scroll motion converts",
                "body": [
                    "Premium buyers judge build quality in seconds. A hero that scrubs through frames on scroll feels "
                    "like hardware, not a banner - it earns the price before the spec table loads. Static one-hero "
                    "pages flatten flagship products into generic listings.",
                ],
            },
        ],
        "hidden_tricks": [
            "Write the brand-world doc first; paste it as the header of every website/image/video prompt.",
            "Put the aspect ratio on the first line of image prompts - it sticks better than 'high-res'.",
            "Leave negative space in hero stills for the headline overlay you add later.",
            "Generate 16:9 hero frames specifically so the site can scroll-scrub them.",
            "Keep a NEVER list (no text-on-product, no warped logos) to cut QC failures.",
            "Review every build on mobile first - that is where most DTC traffic lands.",
            "Save and reuse the prompt set per vertical instead of rebuilding each campaign.",
        ],
    },
    # ===================== 26 HIDDEN COMMANDS =====================
    "26_Claude_Hidden_Commands": {
        "carousel_slides": [
            ("", "70+ Commands, You Use 5", "Shipped faster than its docs."),
            ("", "/compact focus", "Keep the constraint you need."),
            ("", "/btw", "Side question, no context burn."),
            ("", "/init", "Auto-draft CLAUDE.md."),
            ("", "Prompt Prefixes", "ULTRATHINK, /skeptic, L99."),
            ("", "/effort + /model", "Dial cost and depth."),
            ("", "Cost Burners", "/loop, /goal+/loop, /schedule."),
            ("", "Comment AI", "Get the cheat sheet."),
        ],
        "extra_sections": [
            {
                "tab": "04", "title": "Context commands that save money",
                "body": [
                    "/context shows a visual grid of what is filling your window; /cost shows spend. /clear is a clean "
                    "slate (CLAUDE.md and skills survive). /compact summarizes - always add a focus so the summary "
                    "keeps the decision or constraint you cannot lose.",
                ],
                "code": {
                    "caption": "Context hygiene",
                    "lines": "/context              # see what fills the window\n/compact focus on the auth refactor plan\n/btw what does this regex do?   # no main-context burn\n/clear                # fresh slate; memory survives",
                },
            },
            {
                "tab": "05", "title": "Prompt prefixes (stackable)",
                "body": [
                    "Prefixes are model-level conventions typed at the start of a prompt. Common combos: PERSONA + L99 "
                    "(expert + committed) for technical decisions; /skeptic + ULTRATHINK for high-stakes architecture; "
                    "/ghost + /punch to humanize and sharpen text. Most power users stack 2-3.",
                ],
                "code": {
                    "caption": "Stacking prefixes",
                    "lines": "/skeptic ULTRATHINK\nShould we migrate from REST to gRPC for the\ninternal services? Consider blast radius and rollback.",
                },
            },
            {
                "tab": "06", "title": "Cost and model control",
                "body": [
                    "/effort sets reasoning low/med/high; /model switches model per task; /fast favors speed. Use low "
                    "effort for bulk transforms and high only when reasoning matters - this is the cheapest quality "
                    "lever you have.",
                ],
            },
            {
                "tab": "07", "title": "Custom commands and skills",
                "body": [
                    "Any markdown file in .claude/commands/ becomes a slash command (deploy-check.md -> /deploy-check). "
                    "The recommended path now is skills: a folder with SKILL.md and frontmatter that can auto-load by "
                    "description or stay manual-only for side effects.",
                ],
                "code": {
                    "caption": ".claude/commands/pr-review.md",
                    "lines": "Review the pending diff.\nOrder: security risks, then tests, then style.\nList file:line for each issue.\nNever nitpick formatting alone.",
                },
            },
        ],
        "hidden_tricks": [
            "/compact focus on X keeps your key constraint; plain /compact is lossy and forgets it.",
            "/btw lets you ask an aside without spending main-thread context.",
            "/init scans a repo and drafts CLAUDE.md - a far better start than a blank file.",
            "Stack prefixes: /skeptic + ULTRATHINK for architecture; PERSONA + L99 for committed expert takes.",
            "/effort low on bulk work, /effort high on hard reasoning - cheapest quality lever there is.",
            "Drop a .md in .claude/commands/ and it becomes a slash command next session.",
            "/loop, /goal+/loop and /schedule can run for hours and bill - never walk away unaware.",
        ],
    },
    # ===================== 27 SKILLS =====================
    "27_Claude_Skills_To_Steal": {
        "carousel_slides": [
            ("", "The Cheat Code", "Package an SOP once."),
            ("", "Anatomy", "Frontmatter + markdown body."),
            ("", "Description = Trigger", "Front-load the use case."),
            ("", "Progressive Disclosure", "Metadata -> body -> resources."),
            ("", "Control Invocation", "Side-effect skills stay manual."),
            ("", "Bundle Scripts", "Only output uses context."),
            ("", "Where Skills Live", ".claude/skills/ or global."),
            ("", "Comment AI", "Get 7 ready skills."),
        ],
        "extra_sections": [
            {
                "tab": "04", "title": "A complete SKILL.md",
                "body": [
                    "The directory name must match the frontmatter name (lowercase, numbers, hyphens, max 64 chars, "
                    "no XML tags, no reserved words anthropic/claude). description is the trigger - up to ~1024 chars, "
                    "front-loaded. Keep the body under ~500 lines.",
                ],
                "code": {
                    "caption": ".claude/skills/pr-review/SKILL.md",
                    "lines": "---\nname: pr-review\ndescription: Review a pull request diff for security,\n  tests, and style. Use when asked to review code or a PR.\nallowed-tools: Read, Grep, Bash\n---\n## Steps\n1. Summarize the diff in 3 bullets\n2. Security risks first (file:line)\n3. Test coverage gaps\n4. Style last - never nitpick alone\n## Example\nInput: diff. Output: ordered risk list.",
                },
            },
            {
                "tab": "05", "title": "Invocation flags",
                "body": [
                    "disable-model-invocation: true means only you can fire it - use for /deploy, /commit, "
                    "/send-slack-message. user-invocable: false hides it from users for background knowledge. "
                    "allowed-tools skips per-use approval; model and effort can be set per skill.",
                ],
                "code": {
                    "caption": "Side-effect skill frontmatter",
                    "lines": "---\nname: deploy\ndescription: Ship to production. Manual only.\ndisable-model-invocation: true\nallowed-tools: Bash\n---",
                },
            },
            {
                "tab": "06", "title": "Progressive disclosure",
                "body": [
                    "Only metadata (name + description) is pre-loaded at startup. Claude reads SKILL.md via bash when "
                    "the description matches, and reads references/ or runs scripts/ only as needed. Move long detail "
                    "out of SKILL.md into references/ to keep loaded context lean.",
                ],
                "pro_tip": {
                    "title": "Budget tip",
                    "text": "If descriptions get truncated and skills mismatch, raise SLASH_COMMAND_TOOL_CHAR_BUDGET "
                            "(default ~1% of context, 8,000-char fallback).",
                },
            },
            {
                "tab": "07", "title": "Bundling scripts and assets",
                "body": [
                    "Add scripts/ (Python, JS, Bash), references/ (docs) and assets/ (templates, schemas). Scripts run "
                    "via bash so only their output consumes context. Declare runtime dependencies in frontmatter for "
                    "claude.ai and Claude Code; pre-install for API containers.",
                ],
            },
        ],
        "hidden_tricks": [
            "The description is the single most important field - it is how Claude decides to load the skill.",
            "Directory name must exactly match the frontmatter name or the skill will not register.",
            "Set disable-model-invocation on anything with side effects (/deploy, /commit, /send-*).",
            "Move long reference material into references/ so SKILL.md stays under 500 lines.",
            "Scripts run via bash - only their output costs tokens, not the whole file.",
            "Ask Claude to author the SKILL.md for you; it gets the frontmatter format right.",
            "Raise SLASH_COMMAND_TOOL_CHAR_BUDGET if many skills cause truncated descriptions and misfires.",
        ],
    },
    # ===================== 28 HOOKS =====================
    "28_Claude_Hooks_Automation": {
        "carousel_slides": [
            ("", "Prompts Beg, Hooks Enforce", "Run every time."),
            ("", "PreToolUse", "Block before it runs."),
            ("", "PostToolUse", "Auto-lint after edits."),
            ("", "settings.json", "user/project/managed scope."),
            ("", "Deny Rules", "rm -rf, curl|bash, force-push."),
            ("", "Grind Loops", "Iterate until tests pass."),
            ("", "Exit Codes", "Exit 2 blocks the call."),
            ("", "Comment AI", "Get hook scripts."),
        ],
        "extra_sections": [
            {
                "tab": "04", "title": "Block secrets (PreToolUse)",
                "body": [
                    "A PreToolUse hook on Bash receives the command as JSON on stdin. Regex-scan for credential "
                    "patterns and exit 2 to block the call entirely - this is a guarantee, not a polite request in a "
                    "prompt the agent can forget.",
                ],
                "code": {
                    "caption": "PreToolUse secret guard",
                    "lines": "# reads JSON on stdin; cmd = .tool_input.command\nif echo \"$cmd\" | grep -Eq 'sk_live|AKIA|PRIVATE KEY'; then\n  echo '{\"decision\":\"block\",\"reason\":\"secret detected\"}'\n  exit 2   # exit 2 = block the tool call\nfi",
                },
            },
            {
                "tab": "05", "title": "Auto-format (PostToolUse)",
                "body": [
                    "A PostToolUse hook on Write/Edit runs your formatter so the agent never leaves messy diffs. This "
                    "removes a whole class of review nits and keeps the codebase consistent automatically.",
                ],
                "code": {
                    "caption": "settings.json PostToolUse",
                    "lines": "{\n  \"hooks\": {\n    \"PostToolUse\": [{\n      \"matcher\": \"Write|Edit\",\n      \"command\": \"npx prettier --write $FILE\"\n    }]\n  }\n}",
                },
            },
            {
                "tab": "06", "title": "Deny rules",
                "body": [
                    "Deny rules hard-block dangerous commands globally - safer than asking nicely every time. Pair them "
                    "with logging so you can audit what the agent attempted and tighten rules over time.",
                ],
                "code": {
                    "caption": "settings.json deny list",
                    "lines": "{\n  \"permissions\": {\n    \"deny\": [\n      \"Bash(rm -rf*)\",\n      \"Bash(*curl*| *sh)\",\n      \"Bash(git push*--force*)\"\n    ]\n  }\n}",
                },
            },
            {
                "tab": "07", "title": "Grind-until-green loop",
                "body": [
                    "A Stop or PostToolUse hook that returns a follow-up message can keep the agent working until a "
                    "condition holds - run tests, and if they fail, feed failures back and continue. This is how teams "
                    "get autonomous test-fix loops without babysitting.",
                ],
            },
        ],
        "hidden_tricks": [
            "Exit code 2 from a PreToolUse hook blocks the tool call; other codes do not.",
            "Hooks receive JSON on stdin - parse tool_name and args to decide per command.",
            "PostToolUse with matcher Write|Edit auto-formats so the agent never leaves messy diffs.",
            "Deny rules beat prompts for rm -rf, curl | bash and git push --force.",
            "Wrong event name (PreToolUse vs PostToolUse) is the #1 reason a hook silently never fires.",
            "Return a followup_message from a Stop hook to build a grind-until-green loop.",
            "Log blocked actions - you cannot audit or tighten rules on what you do not record.",
        ],
    },
    # ===================== 29 PROMPTING =====================
    "29_Claude_Prompting_Secrets": {
        "carousel_slides": [
            ("", "It Reads Structure", "Not your mind."),
            ("", "XML Tags", "<context> <example> <rules>."),
            ("", "Two Good One Bad", "Examples beat adjectives."),
            ("", "Format Contracts", "Define the output shape."),
            ("", "Ask For Thinking", "Reason before answering."),
            ("", "Non-Goals", "Stop scope creep."),
            ("", "Project Instructions", "System prompt once."),
            ("", "Comment AI", "Get the templates."),
        ],
        "extra_sections": [
            {
                "tab": "04", "title": "Tag your inputs",
                "body": [
                    "Claude parses delimited sections far more reliably than a wall of text. Wrap background, rules "
                    "and examples in tags so the model knows what each chunk is for and where it ends.",
                ],
                "code": {
                    "caption": "XML-structured prompt",
                    "lines": "<context>\nWe are a B2B SaaS; audience is CFOs.\n</context>\n<rules>\nNo hype words. Cite any stat. Mark UNKNOWN if missing.\n</rules>\n<example>\nGOOD: ... GOOD: ... BAD: ...\n</example>\nTask: draft the exec summary.",
                },
            },
            {
                "tab": "05", "title": "Format contracts",
                "body": [
                    "State the exact output shape and limits. Forbid invented statistics and require UNKNOWN for gaps. "
                    "This is what makes output consistent across runs and reviewers.",
                ],
                "code": {
                    "caption": "Output schema",
                    "lines": "OUTPUT:\n1. Exec summary (<=150 words)\n2. Claim table: Claim | Source | Confidence\n3. Recommendation + risks\nRULES: no invented numbers; write UNKNOWN if absent.",
                },
            },
            {
                "tab": "06", "title": "Thinking and reasoning",
                "body": [
                    "On hard problems, ask for step-by-step reasoning before the answer, or enable adaptive thinking "
                    "on the API so the model reasons only when the turn needs it. Keep the reasoning separate from the "
                    "final deliverable so you can audit it.",
                ],
            },
            {
                "tab": "07", "title": "Non-goals and system prompts",
                "body": [
                    "A non-goals list is the fastest cure for scope creep. Put persona, rules and format in Project "
                    "instructions once so every chat inherits your system prompt - you stop re-explaining and outputs "
                    "stay on-spec.",
                ],
                "pro_tip": {
                    "title": "Reusable skeleton",
                    "text": "<context>/<rules>/<example> + an explicit OUTPUT schema + a NON-GOALS list. Save it as a "
                            "snippet and paste it on every high-stakes prompt.",
                },
            },
        ],
        "hidden_tricks": [
            "Delimit inputs with XML-style tags - Claude parses sections far better than one long blob.",
            "Two good examples plus one counter-example teaches shape and failure mode at once.",
            "Require UNKNOWN instead of guesses to kill hallucinated statistics.",
            "Define the output schema explicitly - headings, length, columns - for consistent runs.",
            "Add a non-goals list; it is the fastest fix for scope creep.",
            "Ask for reasoning before the answer on hard tasks; keep it separate from the deliverable.",
            "Move standing persona/rules/format into Project instructions so every chat inherits them.",
        ],
    },
    # ===================== 30 CLAUDE.md =====================
    "30_Claude_md_Mastery": {
        "carousel_slides": [
            ("", "One File, Every Session", "Most repos don't have it."),
            ("", "What Goes In It", "Commands, architecture, NEVER."),
            ("", "Keep It Under 500 Lines", "Link scoped rules."),
            ("", "Survives /compact", "No more cold starts."),
            ("", "Conditional Loading", "Deep context only when relevant."),
            ("", "Output Styles", "Explanatory, Learning, custom."),
            ("", "Memory", "Teach a convention once."),
            ("", "Comment AI", "Get the template."),
        ],
        "extra_sections": [
            {
                "tab": "04", "title": "A minimal CLAUDE.md",
                "body": [
                    "Keep it high-signal: stack, exact commands, a one-paragraph architecture note, and a hard NEVER "
                    "list. This is loaded every session and is the only context that survives /compact, so it earns "
                    "its place.",
                ],
                "code": {
                    "caption": "CLAUDE.md skeleton",
                    "lines": "# Project\nStack: Next.js 15, Postgres, Stripe\n\n## Commands\n- test: npm test\n- lint: npm run lint\n- build: npm run build\n\n## Architecture\nAuth -> API routes -> service layer -> DB\n\n## NEVER\n- Commit .env files\n- Force-push main\n- Edit generated/ folder",
                },
            },
            {
                "tab": "05", "title": "Scoped rules + conditional loading",
                "body": [
                    "Keep the root under ~500 lines and push domain detail into .claude/rules/. Add conditional "
                    "triggers so deep context loads only when relevant - the agent fetches the auth doc when it "
                    "touches auth, not on every session.",
                ],
                "code": {
                    "caption": "Conditional context line",
                    "lines": "## Context triggers\n- Before editing auth, read docs/auth-flow.md\n- Before DB migrations, read docs/migrations.md\n- For billing, read docs/stripe-webhooks.md",
                },
            },
            {
                "tab": "06", "title": "Output styles",
                "body": [
                    "Switch /output-style to Explanatory or Learning, or write a custom style file that modifies the "
                    "system prompt to enforce your format (e.g., always lead with a one-line summary, then code, then "
                    "caveats). Styles persist so output stays consistent.",
                ],
            },
            {
                "tab": "07", "title": "Memory you teach once",
                "body": [
                    "Tell Claude a durable convention once - 'remember our API uses snake_case JSON' - and it persists "
                    "to memory so it stops asking. Project-level memory reloads each session; user-level memory "
                    "persists across sessions by design. Run /init to bootstrap CLAUDE.md fast.",
                ],
            },
        ],
        "hidden_tricks": [
            "CLAUDE.md is the only context that survives /compact - that is why it kills cold starts.",
            "Run /init to draft it from your repo, then edit; the generated file is a starting point.",
            "Keep root under ~500 lines; push depth into .claude/rules/ loaded on demand.",
            "Add 'Before editing X, read docs/X.md' so deep context loads only when relevant.",
            "Project memory reloads each session; user-level memory persists across all sessions.",
            "Write a custom /output-style to enforce a house format for every response.",
            "Teach one durable convention to memory and Claude stops re-asking it forever.",
        ],
    },
}

# ----------------------------- FAQS -----------------------------
BATCH4_FAQS = {
    "21_GPT_Power_Moves": [
        ("Which plans have Agent mode?", "Plus, Pro, Business, Enterprise, Edu - not Free. Web, mobile, desktop."),
        ("How do I start Agent mode?", "Tools dropdown -> Agent mode, or type /agent in the composer."),
        ("Instant or Thinking?", "Instant for everyday work; Thinking for modeling, long docs, hard logic."),
        ("Can it send email on its own?", "It asks permission before consequential actions like sending or submitting."),
        ("Message limits?", "Pro ~400/month; other paid ~40/month, with credit-based options."),
        ("What is Codex?", "OpenAI's coding tool across terminal, IDE and cloud for shipping real code."),
        ("What is Atlas?", "OpenAI's AI browser that summarizes pages and acts across the web."),
        ("Can tasks repeat?", "Yes - clock icon to schedule daily/weekly/monthly; manage at chatgpt.com/schedules."),
    ],
    "22_Claude_Power_Moves": [
        ("What changed in Opus 4.8?", "Better agents/coding, effort control, same price as 4.7 (May 2026)."),
        ("Effort levels?", "high default, extra/xhigh for hard tasks, max for long async with higher limits."),
        ("Do Projects share chat history?", "No - only instructions + knowledge persist; export decisions to knowledge."),
        ("How force an Artifact?", "Say 'put the full deliverable in an Artifact; chat only for questions.'"),
        ("What is a Skill?", "A SKILL.md folder Claude loads when its description matches your request."),
        ("How many MCP servers?", "Keep under ~10 enabled to protect your context window."),
        ("Sonnet or Opus?", "Sonnet for volume, Opus 4.8 for judgment, Haiku to classify."),
        ("How to prove ROI?", "Track human edit minutes per task, not API cents."),
    ],
    "23_Gemini_Power_Moves": [
        ("How big is the context?", "Gemini 3 Pro carries a 1M-token context window."),
        ("What is thinking_level?", "low/high control of reasoning depth; it replaced thinking_budget on Gemini 3."),
        ("What is Deep Think?", "Specialized reasoning mode for science, math and engineering."),
        ("Deep Think temperature?", "Set 1.0 - other values degrade reasoning quality."),
        ("Why does it time out?", "Stream responses; default 30-60s client timeouts cut long reasoning off."),
        ("max_output_tokens?", "Raise to 8k-16k for Deep Think or reasoning gets truncated."),
        ("Is there a free tier?", "Yes - generous personal tier via Google auth; production on Vertex/API."),
        ("How to keep facts honest?", "Enable grounding and ask for cited, recent-only sources."),
    ],
    "24_Cursor_Power_Moves": [
        ("What is Composer 2?", "Cursor's in-house frontier coding model, fast and large-codebase aware."),
        ("What changed in Cursor 3?", "Agents Window - each run is a tab with its own context, model, environment."),
        ("How to run agents in parallel?", "Use /worktree so each agent edits an isolated git worktree."),
        ("Rules vs .cursorrules?", "Use .cursor/rules/*.mdc; legacy .cursorrules may still work but is deprecated."),
        ("Rule application modes?", "Always, Apply Intelligently, glob-scoped, or manual @-mention."),
        ("Where are Skills/hooks?", ".cursor/skills/ (SKILL.md) and .cursor/hooks.json - nightly channel early 2026."),
        ("What is Plan Mode?", "Researches the codebase and writes a reviewable plan before any code."),
        ("Cloud handoff?", "Start a refactor in cloud, hand the diff to a local agent to finish and review."),
    ],
    "25_Draftly_Power_Moves": [
        ("What does Draftly do?", "Turns one deep brief into a scroll-synced site plus matching stills and video."),
        ("Do I need to code?", "No - you write structured prompts; Draftly assembles the experience."),
        ("What is scroll-sync?", "The hero scrubs through extracted frames as the user scrolls."),
        ("How to stay on-brand?", "Lock a brand-world doc (palette, type, lighting, NEVER list) and reuse it."),
        ("Which verticals?", "DTC - earphones, fashion, coffee, sneakers, skincare, hotels and more."),
        ("Can I reuse prompts?", "Yes - save the prompt set per vertical and start the next campaign warm."),
        ("Image ratio?", "Generate 16:9 hero stills so the site can scroll-scrub them."),
        ("How do I get a free trial?", "Comment DRAFTLY on the post for free trial access on draftly.space."),
    ],
    "26_Claude_Hidden_Commands": [
        ("How many commands exist?", "70+ built-in slash commands; most users know about five."),
        ("Difference /clear vs /compact?", "/clear wipes the chat; /compact summarizes - add a focus to keep key context."),
        ("What does /btw do?", "Asks a side question without spending main-thread context."),
        ("What is /init?", "Scans the repo and drafts a starter CLAUDE.md."),
        ("What are prompt prefixes?", "Typed conventions like ULTRATHINK, /skeptic, L99 that change response behavior."),
        ("Can I stack prefixes?", "Yes - 2-3 is common, e.g. /skeptic + ULTRATHINK."),
        ("Which commands cost money?", "/loop, /goal + /loop and /schedule can run for hours and bill."),
        ("Custom commands?", "Any .md in .claude/commands/ becomes a slash command; skills are the newer path."),
    ],
    "27_Claude_Skills_To_Steal": [
        ("What is a Skill?", "A folder with SKILL.md: YAML frontmatter + markdown instructions."),
        ("Required fields?", "name and description; name must match the directory."),
        ("name rules?", "Lowercase/numbers/hyphens, max 64 chars, no XML tags, no anthropic/claude."),
        ("Why does my skill not trigger?", "The description is the trigger - front-load the use case and key phrases."),
        ("How does loading work?", "Metadata always; SKILL.md on trigger; references/scripts on demand."),
        ("Stop auto-invoking /deploy?", "Set disable-model-invocation: true so only you can fire it."),
        ("Can skills run code?", "Yes - scripts/ in Python/JS/Bash run via bash; only output uses context."),
        ("Where do skills live?", ".claude/skills/ (project) or ~/.claude/skills/ (global)."),
    ],
    "28_Claude_Hooks_Automation": [
        ("What is a hook?", "A script that runs on a lifecycle event - it always runs, unlike a prompt."),
        ("PreToolUse vs PostToolUse?", "Pre runs before a tool call (can block); Post runs after (auto-fix)."),
        ("How do I block a call?", "Exit 2 from a PreToolUse hook blocks the tool call."),
        ("Where are hooks defined?", "settings.json under hooks.PreToolUse / hooks.PostToolUse."),
        ("What are deny rules?", "Global hard-blocks for commands like rm -rf, curl | bash, git push --force."),
        ("How do hooks get context?", "JSON on stdin with tool name and arguments to parse."),
        ("Can hooks build loops?", "Yes - return a follow-up message to grind until tests pass."),
        ("Why did my hook not fire?", "Usually a wrong event name or scope (user/project/managed)."),
    ],
    "29_Claude_Prompting_Secrets": [
        ("Why structure over wording?", "Claude parses delimited sections reliably; vague text invites guessing."),
        ("Should I use XML tags?", "Yes - <context>, <rules>, <example> delimit inputs cleanly."),
        ("How many examples?", "Two good plus one counter-example beats paragraphs of adjectives."),
        ("How to stop hallucinated stats?", "Require UNKNOWN for gaps and a claim/source table."),
        ("What is a format contract?", "An explicit output shape - headings, length, columns - stated up front."),
        ("How to stop scope creep?", "Add a non-goals list of what the output must not include."),
        ("Where do standing rules go?", "Project instructions - every chat inherits them as a system prompt."),
        ("When to ask for thinking?", "On hard tasks; or enable adaptive thinking on the API."),
    ],
    "30_Claude_md_Mastery": [
        ("What is CLAUDE.md?", "Repo-root file loaded every session; the only context that survives /compact."),
        ("What goes in it?", "Stack, exact commands, one-paragraph architecture, and a NEVER list."),
        ("How long should it be?", "Under ~500 lines; push detail into .claude/rules/."),
        ("How to generate one?", "Run /init - it scans the repo and drafts a starter file."),
        ("Conditional loading?", "Add 'Before editing X, read docs/X.md' to fetch deep context only when relevant."),
        ("What are output styles?", "/output-style switches Explanatory/Learning or a custom format file."),
        ("How does memory work?", "Teach a convention once; project memory reloads, user memory persists."),
        ("Why no cold starts?", "CLAUDE.md reloads every session so Claude never re-discovers your project."),
    ],
}

# ----------------------------- CASE STUDIES -----------------------------
BATCH4_CASE_STUDIES = {
    "21_GPT_Power_Moves": (
        "A 5-person marketing team replaced a manual Monday ritual with one Agent task: visit three competitor "
        "sites, extract pricing and positioning, and produce a comparison doc with exec summary first. They kept "
        "form-submission and sign-in actions gated, approved the run once, then scheduled it weekly. A 45-minute "
        "task became a reviewed 5-minute approval, and Thinking handled the modeling that Instant used to fumble."
    ),
    "22_Claude_Power_Moves": (
        "A B2B SaaS ops lead combined all four primitives on one workflow: a Project (brand + pricing knowledge), "
        "a SKILL.md for the weekly update, a read-only Postgres MCP for live metrics, and Artifacts for the final "
        "deliverable. Sonnet drafted, Opus 4.8 polished the exec narrative. Onboarding new writers dropped from "
        "two weeks of tone corrections to three days because instructions and exemplars loaded every session."
    ),
    "23_Gemini_Power_Moves": (
        "A research analyst stopped chunking a 600-page contract set and pasted it into Gemini 3 Pro's 1M window, "
        "asking for a decisions+risks synthesis with per-file citations and a CONFLICTS section. Deep Think (temp "
        "1.0, 16k max tokens, streamed) cracked a modeling problem that standard generation kept truncating. "
        "Grounding with a recency filter kept the market figures cited and current."
    ),
    "24_Cursor_Power_Moves": (
        "A two-person team shipped two features in parallel using /worktree so the agents never collided. Each "
        "started in Plan Mode - reviewable plans caught a wrong data-model assumption before any code. A "
        ".cursor/hooks.json grind loop iterated until tests passed, and a long migration ran on a cloud agent that "
        "handed the diff back locally for review. Composer 2 kept the large-repo navigation fast and cheap."
    ),
    "25_Draftly_Power_Moves": (
        "A DTC earphone brand replaced a static one-hero page with a Draftly scroll-synced site: one website prompt "
        "for structure and motion, 16:9 hero stills for scrubbing, and a short cinematic reveal - all sharing a "
        "locked brand world. They reused the prompt set for the next colorway launch instead of rebuilding, turning "
        "what used to be an agency line item into an afternoon."
    ),
    "26_Claude_Hidden_Commands": (
        "A developer cut surprise context loss by switching from plain /compact to '/compact focus on the migration "
        "plan', parked asides in /btw, and stacked /skeptic + ULTRATHINK on an architecture call that surfaced a "
        "rollback risk nobody had raised. /effort low on bulk transforms and high on the hard reasoning kept the "
        "monthly bill flat while output quality rose."
    ),
    "27_Claude_Skills_To_Steal": (
        "A team turned their five most-repeated prompts into SKILL.md folders. The PR-review skill auto-loaded on "
        "the right requests; the /deploy skill was locked with disable-model-invocation so Claude never fired it. "
        "Moving detail into references/ kept loaded context lean, and raising SLASH_COMMAND_TOOL_CHAR_BUDGET fixed "
        "truncated descriptions that had caused misfires."
    ),
    "28_Claude_Hooks_Automation": (
        "An agency hard-blocked secrets with a PreToolUse hook (exit 2), auto-formatted every edit with a PostToolUse "
        "prettier hook, and added deny rules for rm -rf, curl | bash and force-push. A Stop hook that returned a "
        "follow-up message built a grind-until-green loop so the agent fixed failing tests unattended. Logged blocks "
        "let them tighten rules over time - incident rate from bad commands went to zero."
    ),
    "29_Claude_Prompting_Secrets": (
        "A content lead replaced vague briefs with an XML-tagged skeleton: <context>/<rules>/<example> plus an "
        "explicit OUTPUT schema and a NON-GOALS list. Requiring UNKNOWN for gaps killed invented statistics, and "
        "two-good-one-bad examples locked the format. The same prompt now produces board-ready output across "
        "different writers because the structure - not the wording - carries the quality."
    ),
    "30_Claude_md_Mastery": (
        "A repo with no CLAUDE.md started every session cold. After running /init and trimming to a lean root file "
        "(commands, one-paragraph architecture, NEVER list) with .claude/rules/ for depth and conditional triggers "
        "for auth/migrations, cold starts disappeared. A custom output style enforced 'summary first, then code, "
        "then caveats', and a taught snake_case-JSON memory stopped the repeated questions."
    ),
}

# ----------------------------- REFERENCE APPENDIX -----------------------------
BATCH4_REFERENCE_APPENDIX = {
    "21_GPT_Power_Moves": {
        "title": "Reference: Agent and model quick card",
        "body": ["Keep this beside you when delegating to ChatGPT."],
        "bullets": [
            ("Start Agent", "Tools -> Agent mode, or /agent"),
            ("Deep research", "Pick 'deep research' in composer for longer runs"),
            ("Schedules", "chatgpt.com/schedules"),
            ("Instant", "everyday drafts, lookups, translation"),
            ("Thinking", "modeling, long docs, step-by-step logic"),
            ("Codex", "terminal / IDE / cloud code"),
        ],
        "code": {
            "caption": "Agent SOP template",
            "lines": "ROLE: <one line>\nINPUTS: <connectors, read-only>\nSTEPS: 1.. 2.. 3..\nOUTPUT: <format, exec summary first>\nNEVER: submit/sign-in without approval\nASK before any action that leaves a trace",
        },
    },
    "22_Claude_Power_Moves": {
        "title": "Reference: operator stack card",
        "body": ["The four primitives and how to wire them together."],
        "bullets": [
            ("Project", "instructions + knowledge per workflow"),
            ("Artifact", "put full deliverable in Artifact"),
            ("Skill", ".claude/skills/<name>/SKILL.md"),
            ("MCP", "read-only first; under 10 enabled"),
            ("Routing", "Sonnet volume / Opus 4.8 judgment / Haiku classify"),
            ("Effort", "high default; extra/xhigh; max for async"),
        ],
        "code": {
            "caption": "One-workflow setup",
            "lines": "1. Project + instructions + 5 knowledge files\n2. SKILL.md for the repeated task\n3. read-only MCP (e.g. Postgres replica)\n4. 'put deliverable in an Artifact'\n5. Sonnet draft -> Opus polish for tier-3",
        },
    },
    "23_Gemini_Power_Moves": {
        "title": "Reference: Gemini config card",
        "body": ["Docs: Gemini API / Vertex AI generative docs."],
        "bullets": [
            ("Model", "gemini-3-pro-preview / deep-think variant"),
            ("thinking_level", "low or high (replaces thinking_budget)"),
            ("Deep Think", "temperature 1.0, stream, raise max tokens"),
            ("Context", "1M tokens - do not chunk what fits"),
            ("Grounding", "Search + cited, recent-only sources"),
            ("Monitor", "usage_metadata for thinking tokens"),
        ],
        "code": {
            "caption": "Deep Think call",
            "lines": "model = genai.GenerativeModel('gemini-3-0-deep-think')\nresp = model.generate_content(prompt,\n  generation_config=GenerationConfig(\n    max_output_tokens=16384, temperature=1.0),\n  stream=True)",
        },
    },
    "24_Cursor_Power_Moves": {
        "title": "Reference: Cursor 3 quick card",
        "body": ["Docs: cursor.com agent best practices."],
        "bullets": [
            ("Model", "composer-2 or auto in agent tab header"),
            ("Parallel", "/worktree per agent"),
            ("Plan", "Plan Mode before multi-file work"),
            ("Rules", ".cursor/rules/*.mdc"),
            ("Skills", ".cursor/skills/ SKILL.md (nightly)"),
            ("Hooks", ".cursor/hooks.json before/after actions"),
        ],
        "code": {
            "caption": ".cursor/hooks.json grind loop",
            "lines": "{\n  \"afterEdit\": [\n    { \"command\": \"node .cursor/hooks/grind.ts\" }\n  ]\n}",
        },
    },
    "25_Draftly_Power_Moves": {
        "title": "Reference: three-prompt pipeline",
        "body": ["Write the brand world once; reuse on every prompt."],
        "bullets": [
            ("Brand world", "palette hex, type, lighting, NEVER list"),
            ("Website prompt", "nav, hero, scroll sections, motion"),
            ("Image prompt", "ratio first, subject, lighting, camera"),
            ("Video prompt", "short cinematic reveal, same world"),
            ("Review", "mobile first"),
            ("Reuse", "save prompt set per vertical"),
        ],
        "code": {
            "caption": "Brand world header",
            "lines": "BRAND WORLD\nPalette: #F4EEDE cream, #EF5E45 coral, #1B1A17 ink\nType: Space Grotesk headers\nLighting: soft key, cool rim\nNEVER: text-on-product, warped logos, neon blue",
        },
    },
    "26_Claude_Hidden_Commands": {
        "title": "Reference: command cheat sheet",
        "body": ["Most-used commands and prefixes in one place."],
        "bullets": [
            ("/init", "draft CLAUDE.md"),
            ("/compact focus on X", "lossy summary, keep X"),
            ("/btw", "side question, no context burn"),
            ("/effort + /model", "dial cost and depth"),
            ("ULTRATHINK / /skeptic / L99", "stackable prefixes"),
            ("Burners", "/loop, /goal+/loop, /schedule"),
        ],
        "code": {
            "caption": "Daily combo",
            "lines": "/init                     # new repo\n/compact focus on plan    # before long work\n/skeptic ULTRATHINK ...   # hard decisions\n/effort low ...           # bulk transforms",
        },
    },
    "27_Claude_Skills_To_Steal": {
        "title": "Reference: SKILL.md checklist",
        "body": ["Validation rules and structure."],
        "bullets": [
            ("name", "lowercase/numbers/hyphens, <=64, no XML/reserved"),
            ("description", "<=1024 chars, front-load use case"),
            ("body", "<=500 lines; steps + examples"),
            ("references/", "depth loaded on demand"),
            ("scripts/", "run via bash; only output costs tokens"),
            ("flags", "disable-model-invocation, allowed-tools"),
        ],
        "code": {
            "caption": "Minimal SKILL.md",
            "lines": "---\nname: release-notes\ndescription: Turn merged PRs into a changelog. Use when\n  asked for release notes or a changelog.\n---\n## Steps\n1. Group commits: feat/fix/breaking\n2. Customer-facing tone\n3. Breaking section first",
        },
    },
    "28_Claude_Hooks_Automation": {
        "title": "Reference: hooks recipes",
        "body": ["Drop these into settings.json (project scope)."],
        "bullets": [
            ("PreToolUse", "scan + exit 2 to block"),
            ("PostToolUse", "matcher Write|Edit -> format"),
            ("deny", "rm -rf, curl|bash, force-push"),
            ("stdin", "JSON with tool name + args"),
            ("Stop hook", "followup_message for loops"),
            ("scope", "user / project / managed"),
        ],
        "code": {
            "caption": "PreToolUse secret guard",
            "lines": "if echo \"$cmd\" | grep -Eq 'sk_live|AKIA|PRIVATE KEY'; then\n  echo '{\"decision\":\"block\",\"reason\":\"secret\"}'\n  exit 2\nfi",
        },
    },
    "29_Claude_Prompting_Secrets": {
        "title": "Reference: prompt skeleton",
        "body": ["Paste and fill for any high-stakes prompt."],
        "bullets": [
            ("<context>", "background the model must use"),
            ("<rules>", "always/never"),
            ("<example>", "good / good / bad"),
            ("OUTPUT", "schema + limits"),
            ("UNKNOWN", "forbid guessing"),
            ("NON-GOALS", "what to exclude"),
        ],
        "code": {
            "caption": "Reusable skeleton",
            "lines": "<context>...</context>\n<rules>always X; never Y</rules>\n<example>GOOD.. GOOD.. BAD..</example>\nOUTPUT: <schema, <=N words>\nMark UNKNOWN if missing.\nNON-GOALS: <list>",
        },
    },
    "30_Claude_md_Mastery": {
        "title": "Reference: CLAUDE.md template",
        "body": ["Run /init then trim to this shape."],
        "bullets": [
            ("Stack", "frameworks + services"),
            ("Commands", "test / lint / build / deploy"),
            ("Architecture", "one paragraph"),
            ("NEVER", "hard boundaries"),
            (".claude/rules/", "scoped docs"),
            ("triggers", "read deep docs on demand"),
        ],
        "code": {
            "caption": "Template",
            "lines": "# Project\nStack: ...\n## Commands\n- test: ...\n## Architecture\n...\n## NEVER\n- ...\n## Context triggers\n- Before editing auth, read docs/auth-flow.md",
        },
    },
}

# ----------------------------- TROUBLESHOOTING -----------------------------
BATCH4_TROUBLESHOOTING = {
    "21_GPT_Power_Moves": {
        "title": "Troubleshooting GPT workflows",
        "body": [
            "Agent stalls on a site: take over the browser, complete the step, hand control back.",
            "Sloppy modeling: you used Instant - switch to Thinking for spreadsheets and finance.",
            "Unwanted action taken: tighten the DO NOT list and require approval before traces.",
            "Hit message cap: Pro has ~400/month; batch tasks or use credit options.",
            "Scheduled task drifted: review it at chatgpt.com/schedules and re-confirm gates.",
        ],
    },
    "22_Claude_Power_Moves": {
        "title": "Troubleshooting Claude stack",
        "body": [
            "Context feels small: too many MCP servers - disable unused, keep under ~10.",
            "Teammates get different answers: someone edited instructions - one Can edit owner.",
            "Deliverable stuck in chat: say 'put the full output in an Artifact'.",
            "Budget high: Opus on tier-1 tasks - default Sonnet, reserve Opus for judgment.",
            "Skill never loads: weak description - front-load the use case and trigger phrases.",
        ],
    },
    "23_Gemini_Power_Moves": {
        "title": "Troubleshooting Gemini",
        "body": [
            "No Deep Think behavior: you used a non-Deep-Think model name.",
            "Truncated reasoning: raise max_output_tokens to 8k-16k.",
            "Timeouts: stream the response; default client timeout is 30-60s.",
            "Degraded reasoning: set temperature 1.0 for Deep Think.",
            "Surprise bill: monitor usage_metadata - thinking tokens can dwarf output.",
        ],
    },
    "24_Cursor_Power_Moves": {
        "title": "Troubleshooting Cursor 3",
        "body": [
            "Agents collide on files: give each its own /worktree.",
            "Wrong architecture built: use Plan Mode and review the plan before code.",
            "Rules ignored: use .cursor/rules/*.mdc with correct application mode.",
            "Skills/hooks missing: they are nightly-channel early 2026 - switch update channel.",
            "Context bloated: do not put everything in always-on rules; scope by glob.",
        ],
    },
    "25_Draftly_Power_Moves": {
        "title": "Troubleshooting Draftly builds",
        "body": [
            "Off-brand assets: you skipped the brand-world header on prompts.",
            "Flat hero: generate 16:9 frames and enable scroll scrubbing.",
            "Text on product: add it to the NEVER list and regenerate.",
            "Looks generic: replace catalog grid with lookbook pacing and motion.",
            "Breaks on mobile: review mobile-first before publishing.",
        ],
    },
    "26_Claude_Hidden_Commands": {
        "title": "Troubleshooting commands",
        "body": [
            "Lost a key constraint: use /compact focus on X, not plain /compact.",
            "Context bloated by asides: route them through /btw.",
            "Surprise bill: a burner ran unattended (/loop, /goal+/loop, /schedule).",
            "Prefix did nothing: type it at the start of the prompt; stack 2-3.",
            "CLAUDE.md missing: run /init to draft one fast.",
        ],
    },
    "27_Claude_Skills_To_Steal": {
        "title": "Troubleshooting Skills",
        "body": [
            "Skill not triggering: weak/late description - front-load the use case.",
            "Name error: directory must match name; lowercase/hyphens; no reserved words.",
            "Context bloated: move detail into references/ and keep body under 500 lines.",
            "Claude auto-fires /deploy: set disable-model-invocation: true.",
            "Descriptions truncated: raise SLASH_COMMAND_TOOL_CHAR_BUDGET.",
        ],
    },
    "28_Claude_Hooks_Automation": {
        "title": "Troubleshooting hooks",
        "body": [
            "Hook never fires: wrong event name (PreToolUse vs PostToolUse) or scope.",
            "Call not blocked: you must exit 2 from a PreToolUse hook.",
            "Formatter not running: check matcher Write|Edit and the command path.",
            "Cannot audit: add logging of blocked actions.",
            "Loop never ends: bound the grind loop with a max-iteration guard.",
        ],
    },
    "29_Claude_Prompting_Secrets": {
        "title": "Troubleshooting prompts",
        "body": [
            "Model ignores rules: delimit them in <rules> and add a counter-example.",
            "Invented numbers: require UNKNOWN and a claim/source table.",
            "Inconsistent shape: add an explicit OUTPUT schema.",
            "Scope creep: add a non-goals list.",
            "Re-explaining every time: move standing rules to Project instructions.",
        ],
    },
    "30_Claude_md_Mastery": {
        "title": "Troubleshooting CLAUDE.md",
        "body": [
            "Cold starts: no CLAUDE.md - add one (it survives /compact).",
            "Session bloat: file too long - trim to <500 lines, link .claude/rules/.",
            "Agent guesses: add exact commands and a one-paragraph architecture note.",
            "Deep context every session: use conditional 'before editing X read docs/X.md'.",
            "Inconsistent format: set an output style.",
        ],
    },
}

# ----------------------------- MASTERY PATH -----------------------------
BATCH4_MASTERY_PATH = {
    "21_GPT_Power_Moves": [
        "Day 1: Set Thinking as default for analysis; run one Agent task with approvals on.",
        "Day 3: Add a DO NOT list and a clear done-state to your Agent brief.",
        "Week 1: Schedule the winning task; manage at chatgpt.com/schedules.",
        "Week 2: Connect one read-only data source; keep writes gated.",
        "Week 3: Delegate one contained engineering task to Codex.",
        "Month 2: Document which actions need confirmation; name an owner per scheduled agent.",
    ],
    "22_Claude_Power_Moves": [
        "Day 1: Create one Project with instructions + 5 knowledge files.",
        "Week 1: Force one deliverable into an Artifact; iterate v2/v3.",
        "Week 2: Package a repeated prompt as a SKILL.md.",
        "Week 3: Connect one read-only MCP and validate answers.",
        "Week 4: Set Sonnet default; reserve Opus 4.8 for tier-3.",
        "Month 2: Track edit minutes per task; archive approved Artifacts as templates.",
    ],
    "23_Gemini_Power_Moves": [
        "Day 1: Run one long-document synthesis in the 1M window (no chunking).",
        "Week 1: Use thinking_level high only where depth is needed.",
        "Week 2: Try Deep Think (temp 1.0, stream, raise max tokens).",
        "Week 3: Add grounding with cited, recent-only sources.",
        "Week 4: Move a production call to Vertex/API; monitor usage_metadata.",
        "Month 2: Standardize a long-context synthesis prompt for your team.",
    ],
    "24_Cursor_Power_Moves": [
        "Day 1: Migrate .cursorrules to .cursor/rules/*.mdc.",
        "Week 1: Use Plan Mode on a multi-file change.",
        "Week 2: Run two agents in parallel on separate worktrees.",
        "Week 3: Add a .cursor/hooks.json grind-until-green loop.",
        "Week 4: Author one Agent Skill (nightly channel).",
        "Month 2: Use cloud agents for long refactors; review diffs locally.",
    ],
    "25_Draftly_Power_Moves": [
        "Day 1: Write the brand-world doc (palette, type, lighting, NEVER).",
        "Week 1: Draft the website prompt with scroll sections and motion.",
        "Week 2: Generate 16:9 hero stills for scrubbing.",
        "Week 3: Add a short product video in the same world.",
        "Week 4: Ship the scroll-synced page; review mobile-first.",
        "Month 2: Reuse the prompt set on the next campaign.",
    ],
    "26_Claude_Hidden_Commands": [
        "Day 1: Run /init; start using /compact focus on X.",
        "Week 1: Route asides through /btw to protect context.",
        "Week 2: Stack /skeptic + ULTRATHINK on a real decision.",
        "Week 3: Tune /effort by task class; switch /model deliberately.",
        "Week 4: Add one custom command in .claude/commands/.",
        "Month 2: Audit burner usage (/loop, /schedule) for cost.",
    ],
    "27_Claude_Skills_To_Steal": [
        "Day 1: Convert your most-repeated prompt into a SKILL.md.",
        "Week 1: Add two examples + one counter-example; sharpen the description.",
        "Week 2: Move depth into references/; keep body under 500 lines.",
        "Week 3: Lock side-effect skills with disable-model-invocation.",
        "Week 4: Bundle a script and test 5 trigger prompts.",
        "Month 2: Version the skills folder in git; review monthly.",
    ],
    "28_Claude_Hooks_Automation": [
        "Day 1: Add a PreToolUse secret guard (exit 2).",
        "Week 1: Add a PostToolUse formatter on Write|Edit.",
        "Week 2: Add deny rules for rm -rf, curl|bash, force-push.",
        "Week 3: Build a grind-until-green loop with a Stop hook.",
        "Week 4: Add logging for blocked actions.",
        "Month 2: Version hooks in project scope; tighten from logs.",
    ],
    "29_Claude_Prompting_Secrets": [
        "Day 1: Adopt the <context>/<rules>/<example> skeleton.",
        "Week 1: Add gold + counter examples to your top prompt.",
        "Week 2: Write explicit OUTPUT schemas with UNKNOWN rule.",
        "Week 3: Add non-goals to high-stakes prompts.",
        "Week 4: Move standing rules into Project instructions.",
        "Month 2: Make the skeleton a team snippet.",
    ],
    "30_Claude_md_Mastery": [
        "Day 1: Run /init and trim to a lean root file.",
        "Week 1: Add exact commands + one-paragraph architecture.",
        "Week 2: Move depth into .claude/rules/ with triggers.",
        "Week 3: Set a custom output style.",
        "Week 4: Teach one durable memory convention.",
        "Month 2: Review CLAUDE.md after any stack or rebrand change.",
    ],
}

# ----------------------------- EXPERT DEPTH -----------------------------
BATCH4_EXPERT_DEPTH = {
    "21_GPT_Power_Moves": {
        "title": "What power users do differently",
        "body": [
            "They give Agent an SOP with a done-state and a DO NOT list, keep consequential actions gated, and "
            "schedule the reviewed task to repeat. They pick Instant vs Thinking deliberately by task class and "
            "delegate contained engineering to Codex rather than pasting snippets back and forth.",
        ],
    },
    "22_Claude_Power_Moves": {
        "title": "What power users do differently",
        "body": [
            "They wire Projects + Skills + MCP + Artifacts around one workflow before scaling, route Sonnet/Opus/"
            "Haiku by risk, and measure edit minutes not API cents. They export decisions to knowledge within 24h "
            "and keep enabled MCP servers under ten to protect context.",
        ],
    },
    "23_Gemini_Power_Moves": {
        "title": "What power users do differently",
        "body": [
            "They exploit the 1M window instead of chunking, set thinking_level deliberately, and treat Deep Think "
            "as a configured tool (temp 1.0, streamed, high max tokens). They ground factual claims with citations "
            "and watch usage_metadata so thinking tokens never blow the budget unnoticed.",
        ],
    },
    "24_Cursor_Power_Moves": {
        "title": "What power users do differently",
        "body": [
            "They treat Cursor 3 as a harness: Plan Mode first, parallel agents on worktrees, hooks for grind loops, "
            "and cloud handoff for long refactors. They keep rules scoped (not always-on) and lean on Composer 2 for "
            "fast large-codebase navigation.",
        ],
    },
    "25_Draftly_Power_Moves": {
        "title": "What power brands do differently",
        "body": [
            "They write the brand world once and reuse it across website, image and video prompts. They generate "
            "16:9 frames specifically for scroll-scrubbing, review mobile-first, and keep a prompt library per "
            "vertical so each launch starts from a proven world, not a blank brief.",
        ],
    },
    "26_Claude_Hidden_Commands": {
        "title": "What power users do differently",
        "body": [
            "They protect context religiously (/compact focus, /btw), stack prompt prefixes for high-stakes work, "
            "tune /effort by task class, and know exactly which commands can bill for hours before walking away. "
            "They turn repeated prompts into custom commands and skills.",
        ],
    },
    "27_Claude_Skills_To_Steal": {
        "title": "What power users do differently",
        "body": [
            "They obsess over the description because it is the trigger, keep SKILL.md lean with references/ for "
            "depth, lock side-effect skills, and let scripts run via bash so only output costs tokens. They version "
            "skills in git and review them monthly.",
        ],
    },
    "28_Claude_Hooks_Automation": {
        "title": "What power users do differently",
        "body": [
            "They convert every must-do rule into a hook or deny rule, use exit 2 to truly block, log blocked "
            "actions to tighten policy, and build bounded grind loops. They treat hooks like production guardrails, "
            "not suggestions.",
        ],
    },
    "29_Claude_Prompting_Secrets": {
        "title": "What power users do differently",
        "body": [
            "They carry one reusable skeleton (tags + schema + non-goals + UNKNOWN rule) and let structure carry "
            "quality across writers. They use two-good-one-bad examples, request reasoning on hard tasks, and push "
            "standing rules into Project instructions so they never re-explain.",
        ],
    },
    "30_Claude_md_Mastery": {
        "title": "What power users do differently",
        "body": [
            "They keep CLAUDE.md lean and conditional, link scoped rules, set output styles, and teach durable "
            "conventions to memory. They know it is the only context that survives /compact and treat it as the "
            "repo's control plane, refreshed after stack changes.",
        ],
    },
}

# ----------------------------- CLOSING NOTES -----------------------------
BATCH4_CLOSING_NOTES = {
    "21_GPT_Power_Moves": [
        "GPT is a worker now - delegate tasks with approvals, do not just chat.",
        "Pick Thinking for analysis; Instant for everyday drafts.",
        "Run one Agent task this week and schedule the winner.",
        "Keep consequential actions gated until you trust the flow.",
        "Comment AI for the GPT prompt and Agent playbook.",
        "Follow @piyush.glitch for operator-level AI breakdowns.",
    ],
    "22_Claude_Power_Moves": [
        "Claude is an operating layer - Projects + Skills + MCP + Artifacts.",
        "Wire all four around one workflow before scaling.",
        "Route Sonnet/Opus/Haiku by risk; measure edit minutes.",
        "Force deliverables into Artifacts and archive templates.",
        "Comment AI for the full operator stack PDF.",
        "Follow @piyush.glitch for Claude ops that ship.",
    ],
    "23_Gemini_Power_Moves": [
        "Gemini is a reasoning engine - stop using it like search.",
        "Use the 1M window; do not chunk what fits.",
        "Set thinking_level deliberately; configure Deep Think correctly.",
        "Ground facts with citations and a recency filter.",
        "Comment AI for the Gemini prompt pack.",
        "Follow @piyush.glitch for frontier-model ops.",
    ],
    "24_Cursor_Power_Moves": [
        "In Cursor 3 the agent is the IDE - stop autocompleting.",
        "Plan Mode first; parallel agents on worktrees.",
        "Use .cursor/rules/*.mdc and a hooks.json grind loop.",
        "Hand long refactors to cloud agents; review locally.",
        "Comment AI for the rules, skills and hooks starter pack.",
        "Follow @piyush.glitch for agent-IDE workflows.",
    ],
    "25_Draftly_Power_Moves": [
        "Static pages lose; cinematic scroll-synced sites sell.",
        "Write the brand world once; reuse on every prompt.",
        "Generate 16:9 frames for scrubbing; review mobile-first.",
        "Reuse the prompt set per vertical instead of rebuilding.",
        "Comment DRAFTLY for free trial access on draftly.space.",
        "Follow @piyush.glitch for prompt-to-website workflows.",
    ],
    "26_Claude_Hidden_Commands": [
        "You use 5 commands; power users know 70+.",
        "Protect context with /compact focus and /btw.",
        "Stack prompt prefixes for high-stakes work.",
        "Know the burners before you walk away.",
        "Comment AI for the full command cheat sheet.",
        "Follow @piyush.glitch for Claude Code tactics.",
    ],
    "27_Claude_Skills_To_Steal": [
        "Skills package an SOP once and load on demand.",
        "The description is the trigger - make it sharp.",
        "Keep SKILL.md lean; push depth to references/.",
        "Lock side-effect skills with disable-model-invocation.",
        "Comment AI for 7 ready-to-paste skills.",
        "Follow @piyush.glitch for Claude skill engineering.",
    ],
    "28_Claude_Hooks_Automation": [
        "Prompts beg; hooks enforce - make rules run every time.",
        "Block secrets with a PreToolUse hook (exit 2).",
        "Auto-format with PostToolUse; deny dangerous commands.",
        "Build a grind-until-green loop and log blocks.",
        "Comment AI for copy-paste hook scripts.",
        "Follow @piyush.glitch for safe agent automation.",
    ],
    "29_Claude_Prompting_Secrets": [
        "Claude reads your structure, not your mind.",
        "Tag inputs; show two good and one bad example.",
        "Define the output schema; require UNKNOWN.",
        "Add non-goals to stop scope creep.",
        "Comment AI for the structured prompt templates.",
        "Follow @piyush.glitch for prompting that audits.",
    ],
    "30_Claude_md_Mastery": [
        "One CLAUDE.md controls every session and survives /compact.",
        "Run /init, then trim to a lean root file.",
        "Link scoped rules; load deep context only when relevant.",
        "Set an output style and teach durable memory.",
        "Comment AI for a battle-tested CLAUDE.md template.",
        "Follow @piyush.glitch for Claude Code mastery.",
    ],
}
