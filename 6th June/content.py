# -*- coding: utf-8 -*-
"""6th June - 5 Claude carousels x 10 slides, Visual AI Club + cream educational."""

BASE = """
3:4 vertical portrait ONLY (1080x1440). Premium Instagram carousel slide.
Crisp readable text, perfect spelling, no lorem ipsum, no watermarks, no slide numbers on image.
Footer bottom-left: @piyush.glitch in small grey sans. NO progress dots. NO SWIPE arrow.
"""

SKY_COVER = BASE + """
SLIDE TYPE: Visual AI Club sky hero cover - EXACT reference style.
Full-bleed editorial fashion photo outdoors against clear bright blue sky with soft white clouds.
Low-angle shot looking slightly upward. Caucasian woman late 20s, wavy dirty-blonde hair, light freckles,
terracotta-rust flowing linen outfit, calm confident expression, natural wind in hair, 24-35mm cinematic grade.
Top center tiny white caps: PIYUSH.GLITCH. Upper-right frosted pill: VISUAL AI CLUB with small star icon.
Lower third huge white bold geometric sans headline + white elegant italic serif second line as specified.
White pill CTA bottom center black uppercase text as specified. Sky dominates - NO dark studio background.
"""

SKY_CTA = BASE + """
SLIDE TYPE: Visual AI Club sky hero finale - same blue sky reference as cover.
Side profile or three-quarter, terracotta outfit, bright blue sky background.
Lower third white headline stack as specified. White pill: COMMENT AI FOR THE PDF.
PIYUSH.GLITCH top center. @piyush.glitch bottom-left on photo.
"""

INTERIOR = BASE + """
SLIDE TYPE: Educational cream grid #F4EEDE - AI_Business style interior.
Top small caps: AI FOR BUSINESS. Huge bold black sans headline; ONE phrase italic serif or coral #EF5E45 underline.
2-3 cream cards with thin border - render ALL specified text EXACTLY, legible monospace for code/repos.
Small Claude terracotta sparkle logo badge top-right. Strong whitespace. Footer @piyush.glitch bottom-left.
"""

EDITORIAL = BASE + """
SLIDE TYPE: Editorial photo slide with text overlay - NOT cream grid.
Full-bleed or 80% photo: professional model or product hero as specified. Clean white or black text overlay lower third.
PIYUSH.GLITCH top center small white caps. @piyush.glitch bottom-left. Cinematic lighting, magazine quality.
"""


def slide(filename, prompt):
    return (filename, prompt.strip())


def C(slug, pdf_name, caption, slides):
    return {"slug": slug, "pdf_name": pdf_name, "caption": caption, "slides": slides}


CAROUSELS = [
    C(
        "01_Top_10_Claude_Plugins_June",
        "top-10-claude-plugins-june.pdf",
        """Comment AI and I'll send the full 12-page install PDF - every plugin, repo link, and config block.

Most devs run Claude Code vanilla. These 10 plugins are what operators actually install in June 2026 - from anti-AI-slop UI audits to token savers and orchestration.

Swipe for: Impeccable, Caveman, Codex, Compound Engineering, Claude HUD, Superpowers, and 4 more with GitHub paths.

Save this. Follow @piyush.glitch for Claude operator stacks.

#ClaudeCode #ClaudePlugins #DevTools #AIagents #PIYUSHGLITCH""",
        [
            slide("01_cover.png", SKY_COVER + """
Headline: "Top 10" bold white sans + "Claude Plugins" white italic serif + "for June" white sans below.
White pill CTA: COMMENT AI FOR THE PDF. Optional frosted badge "10" upper-right.
"""),
            slide("02_plugin_01_impeccable.png", INTERIOR + """
Pill tag black: PLUGIN 01 / IMPECCABLE. Headline: impeccable kills ai slop in your ui.
Body: Audits frontend for 24 design tells before merge. Repo card taped bottom:
pbakaus / impeccable | Anti-AI-slop design skill | JavaScript | 1.2k stars.
"""),
            slide("03_plugin_02_caveman.png", INTERIOR + """
Pill: PLUGIN 02 / CAVEMAN. Headline: caveman mode cuts ~75% of your tokens.
Body: Drops filler, keeps full technical accuracy. Toggle lite / full / ultra in Claude Code.
3D rock card labeled caveman with tape corners aesthetic.
"""),
            slide("04_plugin_03_codex.png", INTERIOR + """
Pill: PLUGIN 03 / CODEX. Headline: codex hands stuck tasks to gpt-5.
Repo card: openai / codex | GPT-5 rescue bridge | Rust | 30k stars.
Body: When Claude stalls, fresh diagnosis without losing thread.
"""),
            slide("05_plugin_04_compound.png", INTERIOR + """
Pill: PLUGIN 04 / COMPOUND. Headline: compound engineering plugin ships faster.
Repo: EveryInc / compound-engineering-plugin | Claude Code + Cursor | 19k stars.
Body: Official compound workflow - plan, build, review loop.
"""),
            slide("06_plugin_05_hud.png", INTERIOR + """
Pill: PLUGIN 05 / CLAUDE HUD. Headline: claude hud shows what is happening.
Repo: jarrodwatts / claude-hud | Context %, tools, agents, todos | 24k stars.
Body: See context usage and running subagents live in terminal UI.
"""),
            slide("07_plugin_06_superpowers.png", INTERIOR + """
Pill: PLUGIN 06 / SUPERPOWERS. Headline: superpowers adds 20+ dev workflows.
Repo: obra / superpowers | Brainstorm, TDD, debug, review skills | highly starred.
Body: Install via plugin marketplace - skills auto-load.
"""),
            slide("08_plugin_07_notebooklm.png", INTERIOR + """
Pill: PLUGIN 07 / NOTEBOOKLM. Headline: notebooklm from your terminal.
Repo: teng-lin / notebooklm-py | Programmatic NotebookLM | Python | 15k stars.
Body: Spin notebooks, add sources, generate podcasts from Claude Code.
"""),
            slide("09_plugin_08_to_10.png", INTERIOR + """
Pill: PLUGINS 08-10. Three repo cards stacked:
anthropics / claude-plugins-official | Official directory | 29k stars
linny006 / claude-code-plugin-tracker | Live index every 15min
quemsah / awesome-claude-plugins | 20k repos indexed
Headline: track the ecosystem - do not install random repos.
"""),
            slide("10_sky_cta.png", SKY_CTA + """
Headline: "comment" white sans + "AI" coral highlight box + "for all 10 install guides" white italic serif.
Recap tiny white text: Impeccable, Caveman, Codex, Compound, HUD, Superpowers, NotebookLM, Official, Tracker, Awesome.
"""),
        ],
    ),
    C(
        "02_10_Claude_Agents_You_Dont_Know",
        "10-claude-agents-you-dont-know.pdf",
        """Comment AI for the subagent playbook PDF - install paths, .claude/agents/ templates, and hidden built-ins.

Everyone knows @codebase. Almost nobody uses Verification Agent, Fork subagents, or the VoltAgent catalog of 154 specialists.

Swipe for 10 agents that isolate context and stop polluting your main thread.

Follow @piyush.glitch

#ClaudeCode #Subagents #AIagents #DevTools #PIYUSHGLITCH""",
        [
            slide("01_cover.png", SKY_COVER + """
Headline: "10 Claude" white sans + "Agents" white italic serif + "you don't know" white sans.
White pill: COMMENT AI FOR THE PDF. Frosted badge "10".
"""),
            slide("02_explore_agent.png", INTERIOR + """
Pill: AGENT 01 / EXPLORE. Headline: explore agent - read-only codebase search.
Body: Built-in. Haiku model. Searches repo without flooding main context. Returns summary only.
Use when: find files, grep patterns, map architecture.
"""),
            slide("03_plan_agent.png", INTERIOR + """
Pill: AGENT 02 / PLAN. Headline: plan agent before you write code.
Body: Built-in Plan subagent. Read-only. Outputs implementation plan + acceptance criteria.
Use when: large refactors, new features, migration planning.
"""),
            slide("04_verification_agent.png", INTERIOR + """
Pill: AGENT 03 / VERIFICATION. Headline: verification agent catches fake done.
Body: Leaked source shows auto-trigger if you close 3+ tasks without verify step.
Adversarial pass - did the work actually ship?
"""),
            slide("05_fork_subagent.png", INTERIOR + """
Pill: AGENT 04 / FORK. Headline: fork inherits full context - side task without re-explaining.
Body: Subagent sees same history as parent. Tool calls stay isolated. Final result only returns.
Use when: parallel approaches from same starting point.
"""),
            slide("06_coordinator_mode.png", INTERIOR + """
Pill: AGENT 05 / COORDINATOR. Headline: coordinator mode - agent swarms (feature flag).
Body: COORDINATOR_MODE spawns parallel workers via XML task protocol + shared scratch dir.
Experimental - enable via feature flag. Multi-phase workflows.
"""),
            slide("07_security_sentinel.png", INTERIOR + """
Pill: AGENT 06 / SECURITY. Headline: security-sentinel from voltagent catalog.
Body: VoltAgent/awesome-claude-code-subagents - 154 agents, 20k stars.
Install: .claude/agents/security-sentinel.md | OWASP checks, secret scan.
"""),
            slide("08_code_reviewer.png", INTERIOR + """
Pill: AGENT 07 / REVIEWER. Headline: code-reviewer subagent before merge.
Body: Separate context window. Checks tests, breaking changes, security smells.
Never auto-merges - outputs structured review comment.
"""),
            slide("09_context_manager.png", INTERIOR + """
Pill: AGENTS 08-10. Three cards:
context-manager | compacts long threads intelligently
debugger | repro steps + root cause isolation
architect-review | system design adversarial pass
Repo: VoltAgent/awesome-claude-code-subagents | /subagent-catalog:search to browse
"""),
            slide("10_sky_cta.png", SKY_CTA + """
Headline: "comment AI" + "for subagent templates + install paths".
White text recap: Explore, Plan, Verify, Fork, Coordinator, Security, Reviewer, Context, Debugger, Architect.
"""),
        ],
    ),
    C(
        "03_Claude_vs_GPT_Different_Angles",
        "claude-vs-gpt-different-angles.pdf",
        """Comment AI for the multi-model operator PDF - when to use Claude vs GPT vs Gemini, with API presets.

Stop picking one AI religion. This carousel shows different angles - coding, images, business ops, cost - with the models holding the products that matter.

Swipe for the decision matrix. Save for your team stack meeting.

#ClaudeAI #ChatGPT #AIcomparison #PIYUSHGLITCH""",
        [
            slide("01_cover.png", SKY_COVER + """
Model holding TWO phones at chest level - left screen Claude orange sunburst app, right screen ChatGPT swirl logo.
Low-angle blue sky behind. Headline: "Claude" white sans + "vs" small + "GPT" white italic serif.
White pill: COMMENT AI FOR THE PDF.
"""),
            slide("02_angle_coding.png", EDITORIAL + """
Over-shoulder low angle: developer hands on laptop, split screen Claude Code terminal left, ChatGPT window right.
Overlay lower third black semi-transparent card: "Coding angle" bold + "Claude wins agents + MCP" white subline.
"""),
            slide("03_claude_wins.png", INTERIOR + """
Headline: when claude wins. Coral checklist:
Claude Code + subagents in terminal
MCP connectors (GitHub, HubSpot, filesystem)
Long-running agentic coding sessions
Cowork SMB workflows with approve gate
Skills + CLAUDE.md project memory
"""),
            slide("04_gpt_wins.png", INTERIOR + """
Headline: when gpt wins. Coral checklist:
Custom GPT marketplace + sharing
GPT Actions OpenAPI webhooks
Workspace Agents scheduled team runs
Image API maturity (gpt-image-1)
Voice + consumer app reach
"""),
            slide("05_angle_images.png", EDITORIAL + """
Model three-quarter portrait holding phone showing AI-generated product shot on screen.
Warm golden hour side light, different angle from slide 01. Overlay: "Image angle" + "GPT API vs Claude artifacts".
"""),
            slide("06_angle_business.png", INTERIOR + """
Headline: business ops angle. Split table:
Claude: Cowork, invoice chase, contract review
GPT: Workspace Agents, Salesforce connector
Gemini: Gmail/Drive native (see carousel 04)
Operator stack: use all three - route by job
"""),
            slide("07_angle_cost.png", INTERIOR + """
Headline: cost angle. Cream card:
Claude Opus - hard bugs, architecture, review
Claude Sonnet - daily coding default
GPT-4o mini - bulk classification cheap
Gemini Flash - 1M context free tier ops
Rule: expensive model for plan/review only
"""),
            slide("08_product_in_hand.png", EDITORIAL + """
Close-up hands holding physical product (sleek skincare bottle or tech gadget) with phone beside showing Claude-generated ad mockup.
Macro product photography angle - commerce creator vibe. Text overlay: "UGC angle - Claude drafts, GPT images, you approve".
"""),
            slide("09_stack_all_three.png", INTERIOR + """
Headline: the operator stack. Flow diagram cream card:
Job -> Router picks model -> Worker executes -> Reviewer gates
Coding: Claude Code | Google-native: Gemini | Team GPTs: OpenAI
One SKILL.md across tools (agentskills.io)
"""),
            slide("10_sky_cta.png", SKY_CTA + """
Headline: "comment AI" for decision matrix PDF.
Model silhouette against sky, terracotta scarf. Recap: Coding, Images, Business, Cost, Stack.
"""),
        ],
    ),
    C(
        "04_Google_Omni_Claude_Bridge",
        "google-omni-claude-bridge.pdf",
        """Comment AI for the Omni MCP setup PDF - Gemini Veo, 1M context, Deep Research inside Claude Code.

Google Omni is not a replacement for Claude - it is a tool layer. omni-ai-mcp lets Claude orchestrate Gemini's video, TTS, RAG, and 1M token context.

Swipe for pip install, MCP config, and slash commands.

#Gemini #ClaudeCode #MCP #GoogleAI #PIYUSHGLITCH""",
        [
            slide("01_cover.png", SKY_COVER + """
Headline: "Google Omni" white sans + "+ Claude" white italic serif + "one bridge" white sans.
Floating 3D icons: Gemini sparkle + Claude sunburst connected by thin line. White pill: COMMENT AI FOR THE PDF.
"""),
            slide("02_what_is_omni_mcp.png", INTERIOR + """
Pill: OVERVIEW / OMNI-AI-MCP. Headline: claude orchestrates - gemini executes.
Body: marmyx77/omni-ai-mcp on GitHub. Claude stays in control. Gemini tools: Veo 3.1 video, Imagen 4K, Deep Research, 1M context, TTS 30 voices.
PyPI: pip install omni-ai-mcp
"""),
            slide("03_install.png", INTERIOR + """
Pill: SETUP / 5 MIN. Monospace card legible:
pip install omni-ai-mcp
export GEMINI_API_KEY=your_key
# Optional: OPENROUTER_API_KEY for 400+ models

Claude Code: add MCP server in settings
Verify: gemini_list_models tool call
"""),
            slide("04_veo_video.png", INTERIOR + """
Pill: TOOL / VEO 3.1. Headline: generate video with audio from claude chat.
Body: Prompt Claude: "Use Gemini Veo to create 9:16 product demo, 8 seconds, upbeat."
Output returns to Claude thread - no tab switching.
"""),
            slide("05_million_context.png", INTERIOR + """
Pill: TOOL / 1M CONTEXT. Headline: dump entire repo - gemini reads, claude decides.
Body: /gemini-analyze slash command. Claude sends summary request - Gemini processes 1M tokens - returns compressed insight.
~2000x token savings vs pasting into Claude.
"""),
            slide("06_deep_research.png", INTERIOR + """
Pill: TOOL / DEEP RESEARCH. Headline: gemini deep research as claude sub-tool.
Body: Market scans, competitor briefs, cited reports. Claude frames question - Gemini researches - Claude synthesizes action items.
"""),
            slide("07_openrouter_fallback.png", INTERIOR + """
Pill: BONUS / OPENROUTER. Headline: 400+ models via ask_model tool.
Body: GPT-4o, Llama, Mistral from same MCP. Routing: explicit Gemini key -> native API fastest.
Fallback: OpenRouter google/ prefix.
"""),
            slide("08_vs_gemini_cli_bridge.png", INTERIOR + """
Pill: ALT / GEMINI CLI. Headline: two bridges compared.
Table: omni-ai-mcp (full Gemini API tools) vs ankitdotgg/making-gemini-useful-with-claude (free CLI delegation) vs claude-gemini-bridge (large codebase analysis).
Pick omni for video/TTS/RAG. Pick CLI bridge for free Flash reads.
"""),
            slide("09_workflow_example.png", INTERIOR + """
Pill: WORKFLOW / MONDAY BRIEF. Headline: end-to-end example.
Steps numbered:
1. Claude plans brief sections
2. Gemini pulls 1M context from Drive via MCP
3. Veo generates 15s recap video for Slack
4. Claude drafts email - [REVIEW] before send
"""),
            slide("10_sky_cta.png", SKY_CTA + """
Headline: "comment AI" for omni-ai-mcp config + slash commands PDF.
Gemini + Claude icons small in corner. Recap: Install, Veo, 1M context, Research, OpenRouter.
"""),
        ],
    ),
    C(
        "05_Is_Higgsfield_MCP_Worth_It",
        "is-higgsfield-mcp-worth-it.pdf",
        """Comment AI for the honest Higgsfield MCP review PDF - setup, credits, model picks, and when NOT to use it.

Is Higgsfield MCP good or overhyped? Short answer: yes if you generate video + ad creative from Claude daily. No if you only write code.

Swipe for the 60-second OAuth setup and which of 30+ models actually earn your credits.

#Higgsfield #MCP #ClaudeAI #AIVideo #PIYUSHGLITCH""",
        [
            slide("01_cover.png", SKY_COVER + """
Headline: "Is Higgsfield" white sans + "MCP worth it?" white italic serif with question mark.
Dramatic clickbait energy but premium editorial - not cheesy. White pill: COMMENT AI FOR THE PDF.
Small text under headline: honest 2026 operator review
"""),
            slide("02_the_verdict.png", INTERIOR + """
Pill: VERDICT / 2026. Headline: yes - if you ship creative from claude.
Big coral callout card: WORTH IT: UGC ads, product shots, 4K video from chat | SKIP IF: code-only workflow
Body: Official hosted MCP at mcp.higgsfield.ai/mcp - launched April 30 2026. OAuth - no API keys.
"""),
            slide("03_setup_60_sec.png", INTERIOR + """
Pill: SETUP / 60 SEC. Monospace:
Claude Settings -> Connectors -> Add custom
Name: Higgsfield
URL: https://mcp.higgsfield.ai/mcp
Click Connect -> OAuth sign-in -> done

Claude Code CLI:
claude mcp add --transport http --scope user higgsfield https://mcp.higgsfield.ai/mcp
"""),
            slide("04_models_image.png", INTERIOR + """
Pill: MODELS / IMAGE. Headline: pick the right image model.
Table: Soul 2.0 (faces) | Nano Banana Pro (speed) | GPT Image 2 (text in image) | FLUX (photoreal) | Seedream 4.0 (fashion)
Body: Claude selects model - you specify use case in prompt.
"""),
            slide("05_models_video.png", INTERIOR + """
Pill: MODELS / VIDEO. Headline: 16+ video models one connector.
Table: Sora 2 (cinematic) | Veo 3.1 (Google) | Kling 3.0 (UGC) | Seedance 2.0 (dance/product) | MiniMax Hailuo (fast)
9 preset formats: UGC, unboxing, product review, TV spot.
"""),
            slide("06_credits_pricing.png", INTERIOR + """
Pill: COST / CREDITS. Headline: know your burn rate.
Body: Free tier ~150 credits/month (May 2026). Paid: ~$1 = 16 credits. List models + balance via Claude prompt.
Pro tip: batch 10 variants in one thread - Claude picks cheapest model per shot.
"""),
            slide("07_workflow_ugc.png", INTERIOR + """
Pill: WORKFLOW / UGC ADS. Headline: claude writes hooks - higgsfield renders.
Steps:
1. Claude drafts 5 hook scripts from brand SKILL.md
2. Higgsfield MCP generates 9:16 variants per hook
3. You [REVIEW] selects - export to Meta Ads folder
Pairs with carousel 07 Meta UGC OS from 5th June.
"""),
            slide("08_when_not_to_use.png", INTERIOR + """
Pill: SKIP IF. Headline: when higgsfield mcp is wrong tool.
Bullets: pure backend coding | sensitive IP without review | budget under $20/mo heavy video | need local-only generation
Use instead: Claude Code only, or local ComfyUI for privacy.
"""),
            slide("09_vs_other_mcp.png", INTERIOR + """
Pill: COMPARE. Headline: higgsfield vs omni vs meta mcp.
Table row: Higgsfield = creative gen | omni-ai-mcp = Gemini tools | Meta MCP = ad account data
Stack: Meta MCP for performance data + Higgsfield for creative volume + Claude orchestrates both.
"""),
            slide("10_sky_cta.png", SKY_CTA + """
Headline: "comment AI" for full higgsfield mcp review PDF.
Verdict recap white text: Worth it for creative operators. 60-sec setup. 30+ models. Credit math inside.
"""),
        ],
    ),
]

CAROUSEL_MAP = {f"{i:02d}": CAROUSELS[i - 1] for i in range(1, len(CAROUSELS) + 1)}
