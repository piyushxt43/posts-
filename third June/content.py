# -*- coding: utf-8 -*-
"""Third June Visual AI Club carousels - deep technical content, 3:4 slides."""

BASE = """
3:4 vertical portrait aspect ratio ONLY (1080x1440). Premium Instagram carousel slide.
Crisp readable text, perfect spelling, no lorem ipsum, no watermarks, no slide numbers on image.
Footer bottom-left: @piyush.glitch in small grey sans.
"""

COVER = BASE + """
SLIDE TYPE: COVER ONLY - Visual AI Club editorial hero (like visualaiclub Instagram grid).
Full-bleed hyper-real editorial photograph fills ENTIRE 3:4 frame edge to edge.
Real human model hero - natural skin texture, pores, cinematic lighting, shot on 35mm or 85mm, NOT AI-waxy.
Top center tiny white caps: PIYUSH.GLITCH.
Lower third white typography overlaid on photo: line1 bold geometric sans, line2 large italic serif.
White pill CTA bottom center with black uppercase text. Optional frosted badge upper-right with number.
NO cream grid on cover. NO infographic cards on cover. Photo + bold type only.
"""

INTERIOR = BASE + """
SLIDE TYPE: INTERIOR educational slide - match AI_Business_Carousels project style exactly.
Cream grid-paper background #F4EEDE with subtle grid lines (NOT full-bleed photo background).
Top small caps label: AI FOR BUSINESS
Huge bold black sans-serif headline dominating slide; ONE key word in elegant italic serif accent.
Coral #EF5E45 highlight tab or rough underline on the most important phrase.
2-3 large readable UI cards, checklist blocks, repo tiles, or flow diagram - Figma-like polished layout.
Technical content (slash commands, JSON, repos, CLI) inside cream cards with thin border and LEGIBLE monospace -
render ALL specified text EXACTLY, large enough to read on mobile. Max 3 compact supporting points per slide.
Small accurate tool logo badge top-right (Claude coral sparkle / OpenAI / Google / Cursor as specified).
Strong whitespace, operator playbook tone. No generic robot art. No tiny unreadable text blocks.
"""

CTA = BASE + """
SLIDE TYPE: CTA closing slide - cream grid #F4EEDE like AI_Business_Carousels final slide.
NOT a photo cover. Cream grid background with bold black headline.
Huge CTA: Comment [KEYWORD] for the full PDF guide.
Coral accent on keyword. 3 small recap bullet cards of what the PDF contains.
Small tool logo top-right. Footer @piyush.glitch bottom-left.
"""

BEAUTY_MODEL = """
SAME MODEL EVERY SLIDE: Caucasian woman late 20s, fair skin with natural light freckles across nose and cheeks,
light green-hazel eyes, voluminous wavy dirty-blonde hair, refined editorial bone structure, minimal makeup.
Hyper-real skin: visible pores, peach fuzz, natural sebum sheen - NEVER plastic smoothing or waxy AI skin.
"""

BEAUTY_COVER = BASE + BEAUTY_MODEL + """
SLIDE TYPE: Visual AI Club beauty cover - full-bleed emotional portrait on dark soft background.
Shot on 85mm f/2, soft window key light camera-left. One realistic tear on cheek catching light.
Top center tiny white caps PIYUSH.GLITCH. Lower third white text on photo. White pill CTA bottom center black text.
"""

BEAUTY_TYPO = BASE + BEAUTY_MODEL + """
SLIDE TYPE: Visual AI Club typography slide - warm off-white paper #FAF8F4 with subtle grain, NOT full-bleed photo.
Left: huge headline in dark espresso brown bold serif + tan italic serif second line.
Right: two overlapping rounded-corner portrait inset cards of the SAME model with soft drop shadows.
Thin hand-drawn black arrow from headline with handwritten script annotation Hyper Realistic.
Top right PIYUSH.GLITCH small caps. Footer @piyush.glitch bottom center light grey.
"""

BEAUTY_MACRO = BASE + BEAUTY_MODEL + """
SLIDE TYPE: Visual AI Club macro beauty slide - full-bleed extreme close-up photo edge to edge.
Three thin white handwritten-style labels with delicate arrows pointing to skin details (Visual AI Club annotation style).
Top right on photo: PIYUSH.GLITCH in small white sans. Bottom center @piyush.glitch in small white sans.
Clinical beauty editorial precision - Phase One macro quality, not CGI, not horror.
"""

BEAUTY_SPLIT = BASE + BEAUTY_MODEL + """
SLIDE TYPE: Visual AI Club split macro slide - one frame split into two macro panels (left eye area, right cheek area).
Same model, consistent skin tone and freckle pattern. White handwritten callouts with arrows on photo.
Top right PIYUSH.GLITCH. Bottom visualaiclub-style footer @piyush.glitch.
"""

BEAUTY_INFO = BASE + BEAUTY_MODEL + """
SLIDE TYPE: Educational beauty operator slide - cream grid #F4EEDE with subtle grid lines (NOT full-bleed photo).
Top label: AI BEAUTY SYSTEM in small coral #EF5E45 caps.
Huge bold black sans headline; ONE key phrase in elegant italic serif accent.
One large cream card with thin border - render ALL specified text EXACTLY, large enough to read on mobile.
Use clean sans for bullets or monospace for prompt blocks - max 7 lines in card, perfect spelling.
Coral rough underline or tab on the most important line. Optional small rounded macro inset in corner - text is hero.
Footer @piyush.glitch bottom-left. No generic robots. No tiny unreadable text.
"""

BEAUTY_SKY_HERO = BASE + BEAUTY_MODEL + """
SLIDE TYPE: Visual AI Club sky hero finale - EXACTLY like Claude Skills cover reference.
Full-bleed 3:4 editorial fashion photograph outdoors against clear bright blue sky with soft white clouds.
Low-angle shot looking slightly upward. Model in flowing terracotta-rust or cream linen outfit optional.
Side profile or three-quarter profile - face turned slightly toward camera, calm confident expression.
Natural wind in hair, real fabric weave, shot on 24-35mm, warm cinematic grade.
Top center PIYUSH.GLITCH tiny white caps. Lower third huge white bold geometric sans + white italic serif line.
White pill CTA bottom center black uppercase text. Optional frosted badge upper-right.
NO dark background on this slide - sky must dominate frame.
"""


def slide(filename, prompt):
    return (filename, prompt.strip())


def C(slug, pdf_name, caption, slides):
    return {"slug": slug, "pdf_name": pdf_name, "caption": caption, "slides": slides}


CAROUSELS = [
    C(
        "01_Claude_Skills_Slash_Commands",
        "claude-skills-slash-commands.pdf",
        """Comment SKILLS and I'll send the full PDF with every slash command, connector map, and SKILL.md template.

Anthropic shipped 31 pre-built Claude Skills for SMBs - 382K downloads day one. Most people never run them because they don't know which connector each one needs.

This carousel is the cheat sheet: /business-pulse, /invoice-chase, /lead-triage, /monday-brief, /contract-review - plus the SKILL.md format from github.com/anthropics/skills and the Composio awesome-claude-skills repo.

Swipe for: the exact YAML frontmatter, hidden CLI commands (/compact, /btw, /init), and how mcp-to-skills turns your MCP servers into loadable skills.

Save this before your next Claude renewal. Follow @piyush.glitch for operator-level Claude systems.

#ClaudeAI #ClaudeSkills #AIforBusiness #Automation #SmallBusiness""",
        [
            slide("01_cover.png", COVER + """
Full-bleed 3:4 editorial. South Asian woman late 20s in terracotta rust pantsuit outdoors against bright blue sky with soft clouds.
She holds large matte terracotta box toward camera reading "Claude Skills" with Anthropic white sparkle logo.
Low angle 24mm, real skin pores, fabric weave visible. Overlay: PIYUSH.GLITCH top. Frosted badge upper-right "31".
Lower third: "Claude" huge white bold sans + "Skills" white italic serif. Pill: GET ALL 31 CLAUDE SKILLS. Footer @piyush.glitch.
"""),
            slide("02_business_pulse.png", INTERIOR + """
Headline: "Slash Commands" bold dark serif + "that replace SaaS" italic coral accent.
Large cream UI card showing EXACT readable text:
/business-pulse
Connectors: QuickBooks + Stripe + HubSpot
Output: cash position, revenue, pipeline, 3 to-dos
Run every Monday before standup

/binvoice-chase
Scans overdue invoices, drafts tone-matched reminders
Most SMBs recover $2K-$10K on day one

/monday-brief
One page: cash, sales, pipeline, owners
Below card small sans: "Anthropic SMB Skills - June 2025 ship". Coral Claude logo badge top-right.
"""),
            slide("03_skill_md.png", INTERIOR + """
Headline: "SKILL.md" bold + "copy this file" italic.
Large cream UI card EXACT text:
---
name: invoice-chase
description: Scan overdue invoices and draft reminders. Use when user mentions unpaid, AR, or collections.
---

## Steps
1. Pull open invoices from QuickBooks connector
2. Match tone to client history (formal vs casual)
3. Draft reminder - never send, flag [REVIEW]
4. Queue subject lines A/B for operator

Footer note: "Install: ~/.claude/skills/invoice-chase/SKILL.md"
GitHub: anthropics/skills
"""),
            slide("04_github_repos.png", INTERIOR + """
Headline: "GitHub repos" bold + "operators bookmark" italic.
White slide with four rounded dark tiles each showing repo + one line:
github.com/anthropics/skills - official skill examples
github.com/ComposioHQ/awesome-claude-skills - 78 SaaS workflow skills
github.com/MichaelGong/mcp-to-skills - MCP to SKILL.md converter
github.com/CyPack/ai-tooling-sync - sync skills across Claude/Codex/Cursor

Small inset photo: developer at laptop, rounded corner top-right. Highlight swipe under "bookmark".
"""),
            slide("05_connectors.png", INTERIOR + """
Headline: "12 Connectors" bold + "Anthropic ships" italic.
Clean table-style layout on white - dark header row, readable rows:
QuickBooks - cash, invoices, expenses
Stripe - payments, MRR, refunds
HubSpot - CRM, leads, pipeline
Gmail - inbox triage, follow-ups
Google Calendar - scheduling blocks
Square - POS, retail receipts
Canva - asset export
Slack - team notifications (read-first)
Microsoft 365 - docs, email
Block - payments alt
PayPal - invoice matching
Google Drive - file handoff

Note: "Enable in Claude Settings > Connectors before running skills"
"""),
            slide("06_hidden_cli.png", INTERIOR + """
Headline: "Hidden CLI" bold + "not in the docs" italic.
Cream monospace card EXACT commands:
/compact focus - shrink context to task only
/btw - append side note without polluting thread
/init - regenerate CLAUDE.md from codebase
/effort high|medium|low - token budget per reply
/clear - hard reset (use between clients)

Side note box: "/loop 5m run /monday-brief - schedule in Cowork"
Claude Code terminal aesthetic, green prompt char.
"""),
            slide("07_mcp_to_skills.png", INTERIOR + """
Headline: "mcp-to-skills" bold + "one command" italic.
Large cream UI card with legible monospace:
npm i -g @mgong/mcp-to-skills
mcp-to-skills list        # probe all MCP servers
mcp-to-skills sync        # write SKILL.md per server
mcp-to-skills install     # copy to ~/.claude/skills/

Reads: ~/.claude.json mcpServers
Writes: ./skills/{server-name}/SKILL.md + tools/*.json
GitHub: github.com/MichaelGong/mcp-to-skills
"""),
            slide("08_cta.png", CTA + """
Headline: "Want the full guide?" bold black sans + "Comment SKILLS" coral italic.
Three cream recap cards: (1) All 31 slash commands + connectors (2) SKILL.md template (3) Hidden CLI + mcp-to-skills repo setup.
Claude coral logo badge top-right. Footer @piyush.glitch.
"""),
        ],
    ),
    C(
        "02_Claude_MCP_Connectors",
        "claude-mcp-connectors.pdf",
        """Comment MCP and I'll send the connector setup PDF - server configs, sync tools, and the read-first security pattern.

MCP is how Claude talks to Postgres, GitHub, Slack, Notion, and your internal APIs without copy-paste. Most operators configure it once wrong and never fix it.

This carousel: claude mcp add syntax, project .mcp.json, zweiklang/mcp-sync for Codex parity, CyPack/ai-tooling-sync for Claude+Cursor+OpenCode, and the 7 connectors that replace a 5-person ops stack.

Swipe for exact JSON configs and the repos that keep MCP in sync across every tool you use.

Save this. Follow @piyush.glitch for Claude ops infrastructure.

#ClaudeAI #MCP #ModelContextProtocol #AIagents #DevTools""",
        [
            slide("01_cover.png", COVER + """
Full-bleed editorial. Indian male operator early 30s black turtleneck in moody dark studio, dramatic rim light,
looking at camera with calm focus. Upper right frosted badge "7". Lower third: "Claude" bold white sans +
"MCP" italic serif + "Connectors" bold sans. Pill: BUILD YOUR OPS STACK. PIYUSH.GLITCH top. @piyush.glitch.
"""),
            slide("02_mcp_add.png", INTERIOR + """
Headline: "claude mcp add" bold + "exact syntax" italic.
Large cream UI card with legible monospace:
claude mcp add github -- npx -y @modelcontextprotocol/server-github
claude mcp add postgres -- npx -y @modelcontextprotocol/server-postgres $DATABASE_URL
claude mcp add slack -- npx -y @modelcontextprotocol/server-slack
claude mcp list
claude mcp remove github

Env vars go in ~/.claude.json under mcpServers.{name}.env
Never commit secrets - use .env.local + [REVIEW] gate on writes
"""),
            slide("03_mcp_json.png", INTERIOR + """
Headline: "Project" bold + ".mcp.json" italic.
Large cream UI card showing project root file:
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_TOKEN": "${GITHUB_TOKEN}" }
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "${DATABASE_URL}"]
    }
  }
}

Note: "Commit .mcp.json - never commit tokens"
"""),
            slide("04_seven_connectors.png", INTERIOR + """
Headline: "7 MCP servers" bold + "ops stack" italic.
Seven rounded tiles with icon + label + one line each:
Postgres - live metrics, read-only default
GitHub - PRs, issues, CI status
Slack - post summaries, read channels
Notion - SOPs, client docs
Google Drive - deliverable handoff
Meta Ads - spend + ROAS pull
Internal REST - your API via openapi-mcp

Footer: "Read-first. Write actions need human [REVIEW]"
"""),
            slide("05_mcp_sync.png", INTERIOR + """
Headline: "mcp-sync" bold + "Claude to Codex" italic.
Large cream UI card with legible monospace:
npm i -g mcp-sync
mcp-sync status
mcp-sync diff
mcp-sync claude-to-codex --dry-run
mcp-sync claude-to-codex

Reads ~/.claude.json + ~/.codex/config.toml
Creates .bak before every write
GitHub: github.com/zweiklang/mcp-sync
"""),
            slide("06_ai_tooling_sync.png", INTERIOR + """
Headline: "ai-tooling-sync" bold + "all clients" italic.
Large cream UI card with legible monospace:
One config -> Claude Code + Codex + OpenCode
Syncs: MCP servers, skills, rules, agents, memory

Claude: ~/.claude.json + ~/.claude/skills/
Codex: ~/.codex/config.toml + ~/.codex/skills/
Cursor: .cursor/mcp.json + .cursor/rules/
OpenCode: ~/.config/opencode/

GitHub: github.com/CyPack/ai-tooling-sync
"""),
            slide("07_read_first.png", INTERIOR + """
Headline: "Read-first" bold + "write gated" italic.
Split layout: left checklist on white:
[OK] SELECT queries on Postgres MCP
[OK] Read GitHub issues + PR comments
[OK] Read Slack channel history
[BLOCK] INSERT/UPDATE without [REVIEW]
[BLOCK] Send Slack message auto
[BLOCK] Merge PR without human

Right: dark card CLAUDE.md rule:
"Never execute write MCP tools. Draft output. Tag [REVIEW]."
"""),
            slide("08_cta.png", CTA + """
Headline: "Want the MCP setup?" + "Comment MCP" coral highlight.
Three recap cards: claude mcp add syntax, .mcp.json template, mcp-sync + ai-tooling-sync repos.
Claude logo top-right. Footer @piyush.glitch.
"""),
        ],
    ),
    C(
        "03_GPT_Custom_GPTs_API",
        "gpt-custom-gpts-api.pdf",
        """Comment GPT and I'll send the Custom GPT + API preset PDF - instructions template, GPT-4o image API, and Actions setup.

Custom GPTs are free distribution. The API is production. Most creators use neither correctly - they paste a system prompt and wonder why it drifts.

This carousel: Custom GPT instruction architecture, OpenAI stored prompts preset, GPT-4o image generations API body, Assistants vs Chat Completions decision tree, and GPT Actions webhook pattern from the OpenAI cookbook.

Swipe for copy-paste configs. Save before you build your next GPT.

Follow @piyush.glitch for multi-model operator playbooks.

#ChatGPT #OpenAI #CustomGPT #GPT4o #AIforBusiness""",
        [
            slide("01_cover.png", COVER + """
Full-bleed editorial. Woman holding vibrant orange smartphone toward camera, dark gradient background,
face visible upper frame, cinematic product-lifestyle shot. Lower third: "Custom" bold sans + "GPTs" italic serif.
Pill: BUILD YOUR GPT STACK. Badge "5" frosted upper-right. PIYUSH.GLITCH top.
"""),
            slide("02_instructions.png", INTERIOR + """
Headline: "Custom GPT" bold + "instruction stack" italic. OpenAI green accent dot top-right.
Large cream UI card with legible monospace - Instructions field structure:
ROLE: You are a [specific role] for [audience].
CONTEXT: We sell [product]. Tone: [adjectives].
RULES: Never invent pricing. Cite sources. Ask before assumptions.
OUTPUT: Always return [format].
KNOWLEDGE: Upload PDFs here - pricing, SOPs, FAQs.
CAPABILITIES: Web browsing ON. Code interpreter OFF unless needed.

Footer: "Test in Preview before Publish"
"""),
            slide("03_gpt4o_image.png", INTERIOR + """
Headline: "GPT-4o" bold + "image API" italic.
Large cream UI card with legible monospace:
POST https://api.openai.com/v1/images/generations
{
  "model": "gpt-image-1",
  "prompt": "[your 2-paragraph editorial prompt]",
  "size": "1024x1536",
  "quality": "high",
  "n": 1
}

Size for 3:4 Instagram: 1024x1536
Store response.url or b64_json
Rate limit: check tier dashboard
"""),
            slide("04_assistants_vs_chat.png", INTERIOR + """
Headline: "When to use" bold + "which API" italic.
Two column comparison on white:
CHAT COMPLETIONS - stateless, cheap, fast
Best: one-shot, classification, rewrite
Model: gpt-4o-mini for volume

ASSISTANTS API - threads, files, tools
Best: multi-step agent, file search, code
Use: vector store for knowledge base

DECISION: If it needs memory across sessions -> Assistants
If it needs one response -> Chat Completions
"""),
            slide("05_stored_prompts.png", INTERIOR + """
Headline: "Stored prompts" bold + "API preset" italic.
Large cream UI card with legible monospace:
POST /v1/chat/completions
{
  "model": "gpt-4o",
  "prompt": {
    "id": "pmpt_abc123",
    "version": "1"
  },
  "input": [{"role":"user","content":"..."}]
}

Create presets in OpenAI Dashboard > Prompts
Version control prompt changes without redeploying app
Share preset ID across team - single source of truth
"""),
            slide("06_openai_cookbook.png", INTERIOR + """
Headline: "OpenAI" bold + "cookbook repos" italic.
Four repo tiles:
github.com/openai/openai-cookbook - RAG, agents, evals
github.com/openai/openai-python - official SDK
Examples: structured outputs, function calling, batch API
GPT Actions: openapi schema -> Custom GPT external API

Bookmark: cookbook/examples/agents for agent patterns
"""),
            slide("07_gpt_actions.png", INTERIOR + """
Headline: "GPT Actions" bold + "webhook pattern" italic.
Large cream UI card with legible monospace - OpenAPI snippet:
openapi: 3.0.0
info: { title: My CRM, version: 1.0.0 }
paths:
  /leads:
    get:
      operationId: listLeads
      summary: Fetch open leads

Authentication: API Key header X-API-Key
Paste schema in GPT Builder > Actions > Import
Test with Preview before sharing link
"""),
            slide("08_cta.png", CTA + """
Headline: "Want the GPT stack?" + "Comment GPT" coral highlight.
Recap cards: Custom GPT instructions, gpt-image-1 API preset, GPT Actions OpenAPI template.
OpenAI badge top-right. Footer @piyush.glitch.
"""),
        ],
    ),
    C(
        "04_Gemini_Gems_Workspace",
        "gemini-gems-workspace.pdf",
        """Comment GEMINI and I'll send the Gems + Workspace PDF - system instructions, grounding, and API presets for business ops.

Gemini Gems are Google's Custom GPT equivalent - but with native Google Workspace access most people never enable.

This carousel: Gem creation in aistudio.google.com, Workspace extension setup, Gemini 2.0 Flash API preset, grounded search with Google, and the system instruction template for business operators.

Swipe for copy-paste configs. Save if you live in Gmail, Drive, and Sheets.

Follow @piyush.glitch for multi-model stacks.

#GeminiAI #GoogleAI #AIforBusiness #Workspace #GeminiGems""",
        [
            slide("01_cover.png", COVER + """
Full-bleed editorial. Professional woman in camel blazer, glass office, city skyline blurred,
confident three-quarter portrait. Google blue accent subtle in background light. Lower third:
"Gemini" bold white sans + "Gems" italic serif. Pill: BUILD YOUR GEM STACK. PIYUSH.GLITCH top.
"""),
            slide("02_create_gem.png", INTERIOR + """
Headline: "Create a Gem" bold + "aistudio.google.com" italic. Google four-color dot accent.
Large cream UI card with legible monospace - System instructions template:
You are a [role] assistant for [company].
Always search Google Drive when user asks about docs.
Format outputs as: Summary / Actions / Draft.
Never send email - draft only with [REVIEW].
Use Google Search grounding for market data.

Steps: AI Studio > Create Gem > paste instructions > add Knowledge files
"""),
            slide("03_workspace.png", INTERIOR + """
Headline: "Workspace" bold + "extension" italic.
Checklist on white with Google icons:
Enable Gemini in Google Admin console
Connect: Gmail, Drive, Docs, Sheets, Calendar
Gem can: read inbox, summarize threads, draft replies
Gem cannot: send without confirmation (by default)

Business use: /monday-brief equivalent in Gmail + Sheets
Personal: gemini.google.com > Settings > Extensions
"""),
            slide("04_api_preset.png", INTERIOR + """
Headline: "Gemini API" bold + "preset" italic.
Large cream UI card with legible monospace:
POST generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent
{
  "systemInstruction": { "parts": [{"text": "You are..."}] },
  "contents": [{"role":"user","parts":[{"text":"..."}]}],
  "tools": [{"googleSearch": {}}],
  "generationConfig": { "temperature": 0.4, "maxOutputTokens": 8192 }
}

Grounding: add googleSearch tool for live web
Flash = fast + cheap for ops workflows
"""),
            slide("05_grounding.png", INTERIOR + """
Headline: "Grounded" bold + "search" italic.
Explain visually: User question -> Gemini -> Google Search -> cited answer
Cream card example output:
"Competitor X raised prices 12% in Q1 [1]"
Sources: [1] techcrunch.com/... [2] company blog

Enable in API: tools: [{ googleSearch: {} }]
In Gems: toggle "Google Search" in capabilities
Reduces hallucination on market/competitor tasks
"""),
            slide("06_gems_vs_gpt.png", INTERIOR + """
Headline: "Gemini vs GPT" bold + "when to use" italic.
Split comparison:
GEMINI WINS: Google Workspace native, Gmail/Drive/Sheets, free tier generous, Google Search grounding
GPT WINS: Custom GPT marketplace, plugin ecosystem, Codex/Cursor integration, image API maturity

OPERATOR STACK: Claude for code/agents, GPT for custom tools, Gemini for Google-native ops
Run all three - don't pick one religion
"""),
            slide("07_hidden_gem_tips.png", INTERIOR + """
Headline: "Hidden" bold + "Gem tips" italic.
Cream card numbered list:
1. Upload CSV to Knowledge - ask pivot questions in plain English
2. @Google Drive in prompt - force doc retrieval
3. Export Gem as API - same instructions in production
4. Share Gem link internally - team consistent behavior
5. Combine with Apps Script - trigger from Sheet button

AI Studio > My Gems > Share > Copy link
"""),
            slide("08_cta.png", CTA + """
Headline: "Want the Gem setup?" + "Comment GEMINI" coral highlight.
Recap cards: Gem system instructions, Workspace extension, Gemini 2.0 Flash API preset with googleSearch.
Google badge top-right. Footer @piyush.glitch.
"""),
        ],
    ),
    C(
        "05_Cursor_Agent_Secrets",
        "cursor-agent-secrets.pdf",
        """Comment CURSOR and I'll send the full Cursor operator PDF - rules, MCP, Composer agents, and the GitHub repos worth bookmarking.

Cursor is not autocomplete. It is an agent runtime with .cursor/rules, MCP servers, background agents, and Composer multi-file edits - if you configure it like an operator instead of a chatbot.

This carousel: .cursor/rules structure, .cursor/mcp.json setup, .cursorignore for secrets, Composer agent mode, background agents, and repos like awesome-cursorrules and cursor.directory.

Swipe for copy-paste configs. Save if you ship code with AI daily.

Follow @piyush.glitch for dev operator stacks.

#CursorAI #AIcoding #MCP #DevTools #BuildInPublic""",
        [
            slide("01_cover.png", COVER + """
Full-bleed editorial. Young Indian male developer late 20s at creator desk, headphones around neck,
laptop with code blurred on screen, warm practical lighting, authentic studio. Lower third:
"Cursor" bold sans + "Secrets" italic serif. Pill: BUILD YOUR DEV STACK. PIYUSH.GLITCH top.
"""),
            slide("02_cursor_rules.png", INTERIOR + """
Headline: ".cursor/rules" bold + "copy this" italic. Cursor logo badge top-right.
Large cream UI card with legible monospace - .cursor/rules/project.mdc:
---
description: Project standards for this repo
globs: ["**/*.ts", "**/*.tsx"]
alwaysApply: true
---
- Use existing patterns in src/components
- Never commit .env or API keys
- Run tests before suggesting merge
- Prefer edit over rewrite

Rules auto-load when globs match open files
"""),
            slide("03_mcp_cursor.png", INTERIOR + """
Headline: "Cursor" bold + "MCP setup" italic.
Large cream UI card with legible monospace - .cursor/mcp.json:
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_TOKEN": "${GITHUB_TOKEN}" }
    }
  }
}

Cursor Settings > MCP > Enable
Same servers as Claude Code - use ai-tooling-sync to keep in sync
Agent can call tools from Composer chat
"""),
            slide("04_composer.png", INTERIOR + """
Headline: "Composer" bold + "agent mode" italic.
White slide workflow tiles:
1. Cmd+I - open Composer
2. @codebase - full repo context
3. @docs - pull library docs
4. Agent mode - multi-file edits autonomously
5. Review diff - accept per file

Pro tip: "Plan first, then implement" in one Composer session
Max context: enable codebase indexing in Settings
"""),
            slide("05_cursorignore.png", INTERIOR + """
Headline: ".cursorignore" bold + "protect secrets" italic.
Large cream UI card with legible monospace:
.env
.env.*
**/secrets/**
**/*.pem
**/credentials.json
node_modules/
dist/
.git/

Same syntax as .gitignore
Prevents agent reading keys into context or logs
Pair with rule: "Never print env vars"
"""),
            slide("06_github_repos.png", INTERIOR + """
Headline: "Cursor" bold + "repos to bookmark" italic.
Four tiles:
github.com/PatrickJS/awesome-cursorrules - community rules
cursor.directory - searchable rule templates
github.com/getcursor/cursor - official docs + issues
github.com/CyPack/ai-tooling-sync - sync with Claude/Codex

Also: dotcursorrules.com for language-specific presets
"""),
            slide("07_background_agents.png", INTERIOR + """
Headline: "Background" bold + "agents" italic.
Cream card:
Cursor Settings > Beta > Background Agents ON
Agent runs in cloud sandbox while you keep coding
Use for: test runs, long refactors, doc generation
Hand off: "@agent fix failing CI" from PR comment

Limits: check plan tier for agent minutes
Always review diff before merge - agent is not autopilot
"""),
            slide("08_cta.png", CTA + """
Headline: "Want the Cursor ops guide?" + "Comment CURSOR" coral highlight.
Recap cards: .cursor/rules template, .cursor/mcp.json, Composer agent workflow + background agents.
Cursor badge top-right. Footer @piyush.glitch.
"""),
        ],
    ),
    C(
        "06_Build_Realistic_AI_Character_Shoots",
        "build-realistic-ai-character-shoots.pdf",
        """Comment SHOOTS and I'll send the full workflow guide + prompt system PDF for hyper-realistic AI beauty campaigns.

Most AI portraits look plastic. Operators run a macro system: identity lock, pore-level skin, editorial lighting, and campaign-ready crops.

Swipe for the exact Visual AI Club-style workflow - detailed models, eye macro, skin texture, lips, and the sky hero shot that stops the scroll.

Save this before your next beauty campaign. Follow @piyush.glitch for editorial AI shoots.

#AIShoots #AIBeauty #AIPortraits #PromptEngineering #VisualAI""",
        [
            slide("01_cover.png", BEAUTY_COVER + """
Full-bleed portrait: model with voluminous wavy blonde hair, serious editorial expression, one finger gently touching lower lip,
single clear tear on cheek, dark soft out-of-focus background. 85mm beauty editorial sorrow campaign still.
Overlay lower third: "This is" medium white serif + "AI Shoots" large bold white italic serif.
White pill: GENERATE SHOOTS WITH AI. PIYUSH.GLITCH top center.
"""),
            slide("02_detailed_models.png", BEAUTY_TYPO + """
Headline left: "Detailed" dark brown bold serif + "models" tan italic serif below.
Right: two overlapping rounded portrait cards - front card tight face crop same model eyes closed freckles visible;
back card peeking macro green-hazel eye with tear bead. Arrow handwritten Hyper Realistic.
"""),
            slide("03_eye_macro.png", BEAUTY_MACRO + """
Extreme macro left eye green-hazel iris fiber detail, wet lower lash line, one clear tear bead, capillaries in sclera,
individual lash strands with mascara micro-clumps. Pat McGrath editorial macro lighting.
Labels with arrows: Realistic Eye, Realistic Tears, Realistic Eyelashes.
"""),
            slide("04_skin_macro.png", BEAUTY_MACRO + """
Extreme macro bridge of nose and upper cheeks - visible pores, natural sebum sheen, scattered light freckles,
one small realistic mole, peach fuzz in sidelight. Warm honest color grade.
Labels with arrows: Realistic Pores, Realistic Texture, Realistic Moles.
"""),
            slide("05_lip_macro.png", BEAUTY_MACRO + """
Macro lower face: lips slightly parted, natural pink tone, gloss on lower lip, index fingertip touching lip corner -
finger skin shows ridges not airbrushed. Dark soft background shallow DOF.
Labels with arrows: Realistic Lips, Realistic Features.
"""),
            slide("06_texture_split.png", BEAUTY_SPLIT + """
Split frame: left panel eye with dark lashes and clear droplet on cheek; right panel extreme cheek freckles pores
and glistening water droplet. Labels: Realistic Texture, Realistic shadows.
"""),
            slide("07_sky_hero_cta.png", BEAUTY_SKY_HERO + """
Side profile three-quarter view, blonde hair catching sunlight, terracotta rust flowing top or dress,
bright blue sky fills background. Lower third: "This is" white serif + "AI Shoots" bold white italic serif.
Pill: COMMENT SHOOTS FOR THE PDF. Frosted badge upper-right optional "7".
"""),
        ],
    ),
    C(
        "07_Generate_AI_Beauty_Campaigns",
        "generate-ai-beauty-campaigns.pdf",
        """Comment BEAUTY and I'll send the macro prompt system PDF - eyes, lips, pores, sweat, freckles, and sky hero setups.

Build realistic AI character shoots without plastic skin or fake CGI texture. This carousel is the proof deck:
typography intro, macro callouts, moisture detail, shadow truth, and a blue-sky campaign closer.

Swipe all 7. Save for your next beauty editorial. Follow @piyush.glitch.

#AIBeauty #AIModels #Skin #AIPortraits #PromptEngineering""",
        [
            slide("01_cover.png", BEAUTY_COVER + """
Full-bleed close portrait same blonde model, hand near face, emotional editorial gaze, dark moody background.
Overlay: "Build Realistic" white bold sans + "AI Character Shoots" white italic serif stacked in lower third.
White pill: GENERATE BEAUTY WITH AI. PIYUSH.GLITCH top.
"""),
            slide("02_detailed_models.png", BEAUTY_TYPO + """
Headline: "Detailed" bold serif + "models" italic serif. Insets: main rounded portrait model neutral expression tear on cheek;
overlapping square macro inset of same model's eye with tear. Handwritten Hyper Realistic arrow from title.
Left edge optional blurred skin strip with water droplets for detail tease.
"""),
            slide("03_eye_macro.png", BEAUTY_MACRO + """
Same eye macro as character shoots carousel - green-hazel iris, tear, lashes. Labels: Realistic Eye, Realistic Tears,
Realistic Eyelashes. Footer @piyush.glitch on photo.
"""),
            slide("04_pores_macro.png", BEAUTY_MACRO + """
Macro cheek and nose side angle - single clear sweat or water droplet running down cheek, pores and fine facial hair sharp.
Bright natural side lighting accentuating moisture. Label with arrow: Realistic Pores.
Optional second label Realistic Shadow near philtrum shadow.
"""),
            slide("05_lip_macro.png", BEAUTY_MACRO + """
Lip and nose macro with finger on lower lip - same Visual AI Club composition. Labels Realistic Lips and Realistic Features.
Sliver of adjacent macro panel at far left edge optional for collage feel.
"""),
            slide("06_shadow_texture.png", BEAUTY_MACRO + """
Macro side of nose cheek corner of mouth - individual pores fine facial hair small freckles, glistening moisture droplet.
Hand-drawn arrow to cheek labeled Realistic Pores. Bright natural side light NOT dark studio.
"""),
            slide("07_sky_hero_cta.png", BEAUTY_SKY_HERO + """
EXACT Claude Prompts cover energy: low-angle blonde woman against vivid blue sky with wispy clouds,
side profile face visible, wearing terracotta rust long-sleeve dress or holding rust matte board at chest optional.
Lower third: "Generate" huge white bold sans + "AI Shoots" white italic serif.
Pill: COMMENT BEAUTY FOR THE PDF. PIYUSH.GLITCH top. Sky dominates - bright daylight NOT dark bg.
"""),
        ],
    ),
    C(
        "08_Identity_Lock_Character_DNA",
        "identity-lock-character-dna.pdf",
        """Comment IDENTITY for the 12-page Identity Lock PDF  -  Character DNA template, 3-angle rule, reference workflow, and QA checklist.

Face drift kills AI campaigns. This carousel teaches the lock system operators use before any macro or sky slide.

Swipe: copy-paste DNA block, same-face test, freckle map, seed discipline. Save before your next character series.

Follow @piyush.glitch

#AIBeauty #AIPortraits #CharacterDesign #PromptEngineering #IdentityLock""",
        [
            slide("01_cover.png", BEAUTY_COVER + """
Overlay: "Identity" huge white bold sans + "Lock" white italic serif. Pill: LOCK YOUR CHARACTER DNA.
Dark editorial portrait same blonde model, tear optional, PIYUSH.GLITCH top.
"""),
            slide("02_character_dna.png", BEAUTY_INFO + """
Headline: "Character" bold + "DNA" italic coral underline.
Large cream card EXACT text:
CHARACTER DNA (LOCKED):
Caucasian woman, 27, fair skin, light freckles
nose + cheeks, green-hazel eyes
wavy dirty-blonde hair, editorial bone structure
minimal makeup, visible pores, no plastic skin
Paste at top of EVERY prompt in the shoot.
"""),
            slide("03_three_angles.png", BEAUTY_TYPO + """
Headline left: "Same face." bold serif + "Three shots." italic.
Right: three small rounded portraits in a row - front, three-quarter, profile - SAME model identical freckles and eyes.
Handwritten arrow: Identity Locked.
"""),
            slide("04_reference_workflow.png", BEAUTY_INFO + """
Headline: "Reference" bold + "workflow" italic.
Numbered cream card:
1. Generate cover x4 - pick winner
2. Upload as character reference
3. Macros use reference + DNA text
4. If face drifts - fix DNA wording, not random re-rolls
Coral tab: NEVER CHANGE EYE COLOR MID-SERIES
"""),
            slide("05_freckle_map.png", BEAUTY_INFO + """
Headline: "Freckle" bold + "map" italic.
Cream card EXACT:
Freckles dense on nose bridge
Sparse on forehead
One mole 2mm left cheek
Copy this phrase into every macro prompt.
Models anchor on permanent marks.
"""),
            slide("06_seed_discipline.png", BEAUTY_INFO + """
Headline: "Seed" bold + "discipline" italic.
Cream card:
Midjourney: save --seed from hero
GPT Image: keep prompt prefix identical
Change only shot clause per slide
Session rule: one sitting = one DNA version
"""),
            slide("07_qa_checklist.png", BEAUTY_INFO + """
Headline: "Identity" bold + "QA" italic.
Checklist card with checkboxes:
Same eye color all slides
Freckle pattern matches
Skin undertone not drifting
Hair part consistent
PASS at 150px thumbnail width
"""),
            slide("08_sky_cta.png", BEAUTY_SKY_HERO + """
Blue sky side profile, terracotta dress. Lower third: "Lock" bold sans + "Identity" italic serif.
Pill: COMMENT IDENTITY FOR THE PDF.
"""),
        ],
    ),
    C(
        "09_Macro_Prompt_Library",
        "macro-prompt-library.pdf",
        """Comment MACRO for the 12-page macro library  -  eye, skin, lip, tear, and annotation prompts you paste into GPT Image or Midjourney.

Macros are proof slides. This deck gives the exact blocks + batch order so your carousel does not look generic.

Follow @piyush.glitch

#MacroPhotography #AIBeauty #PromptLibrary #AIPortraits #SkinTexture""",
        [
            slide("01_cover.png", BEAUTY_COVER + """
Overlay: "Macro" bold white sans + "Prompt Library" italic serif. Pill: GET ALL MACRO BLOCKS.
Dark portrait, PIYUSH.GLITCH top.
"""),
            slide("02_macro_blocks.png", BEAUTY_INFO + """
Headline: "Macro" bold + "blocks" italic.
Cream monospace card:
EYE: extreme macro [DNA]
iris fibers, tear bead, capillaries
labels: Realistic Eye, Tears, Lashes
SKIN: nose bridge + cheeks, pores
freckles, mole, sebum sheen
LIPS: parted, gloss, finger at corner
"""),
            slide("03_eye_macro.png", BEAUTY_MACRO + """
Eye macro full bleed. Labels Realistic Eye, Realistic Tears, Realistic Eyelashes.
"""),
            slide("04_skin_macro.png", BEAUTY_MACRO + """
Skin macro. Labels Realistic Pores, Realistic Texture, Realistic Moles.
"""),
            slide("05_lip_macro.png", BEAUTY_MACRO + """
Lip macro. Labels Realistic Lips, Realistic Features.
"""),
            slide("06_tear_system.png", BEAUTY_INFO + """
Headline: "Tear" bold + "system" italic.
Cream card:
One fluid per image only
tear OR sweat OR lip gloss
Prompt: single clear droplet
surface tension highlight
not gel blob
"""),
            slide("07_batch_order.png", BEAUTY_INFO + """
Headline: "Batch" bold + "order" italic.
Cream card numbered:
1. Cover  2. Eye  3. Skin
4. Lips  5. Split texture
6. Typography  7. Sky hero
Reduces face drift between gens
"""),
            slide("08_sky_cta.png", BEAUTY_SKY_HERO + """
Sky hero. "Macro" sans + "Library" italic. Pill: COMMENT MACRO FOR THE PDF.
"""),
        ],
    ),
    C(
        "10_Lighting_Camera_Beauty_Setups",
        "lighting-camera-beauty-setups.pdf",
        """Comment LIGHT for the 12-page lighting guide  -  window editorial, raking macro, and outdoor sky setups with copy-paste clauses.

Lighting language is 60% of realism. Swipe for key/fill/rim, focal lengths, and grade tokens.

Follow @piyush.glitch

#LightingSetup #AIBeauty #EditorialPhotography #PromptEngineering""",
        [
            slide("01_cover.png", BEAUTY_COVER + """
Overlay: "Light" bold sans + "Direction" italic serif. Pill: MASTER BEAUTY LIGHTING.
"""),
            slide("02_window_setup.png", BEAUTY_INFO + """
Headline: "Window" bold + "editorial" italic.
Cream card:
KEY: soft 45 deg camera-left
FILL: white bounce right -1.5 stops
RIM: narrow strip behind hair
Use: cover + 3-angle row
"""),
            slide("03_raking_macro.png", BEAUTY_INFO + """
Headline: "Raking" bold + "macro" italic.
Cream card:
KEY: side 30 deg hard-ish
FILL: minimal
GOAL: pores, freckles, peach fuzz
AVOID: flat front flash look
"""),
            slide("04_camera_clauses.png", BEAUTY_INFO + """
Headline: "Camera" bold + "clauses" italic.
Cream card:
Cover: 85mm f/2 shallow DOF
Macro: 100mm f/5.6-8 sharp plane
Sky: 35mm deep DOF on face
Never use macro language on sky slide
"""),
            slide("05_light_diagram.png", BEAUTY_INFO + """
Headline: "Light" bold serif + "Direction" italic on cream.
Bullets on card: Key 45 left, Fill bounce right, Rim hair.
Simple hand-drawn overhead diagram circle with light arrows.
Small rounded inset of lit face result labeled Match this.
"""),
            slide("06_skin_macro.png", BEAUTY_MACRO + """
Skin macro raking light. Labels Realistic Pores, Realistic Shadow.
"""),
            slide("07_grade_tokens.png", BEAUTY_INFO + """
Headline: "Color" bold + "grade" italic.
Cream card:
Editorial: slightly desaturated warm skin
Macro: no orange skin preserve undertone
Sky: warm skin vs cool blue separation
"""),
            slide("08_sky_cta.png", BEAUTY_SKY_HERO + """
Outdoor sky Setup C. "Light" + "Masterclass" italic. Pill: COMMENT LIGHT FOR THE PDF.
"""),
        ],
    ),
    C(
        "11_Quality_Gates_Negative_Prompts",
        "quality-gates-negative-prompts.pdf",
        """Comment QUALITY for the 12-page QC guide  -  master negative block, pass/fail tests, and recovery prompts for plastic skin and glass eyes.

Stop posting porcelain AI faces. Swipe the gate system operators use before publish.

Follow @piyush.glitch

#AIQuality #NegativePrompts #AIBeauty #AIPortraits""",
        [
            slide("01_cover.png", BEAUTY_COVER + """
Overlay: "Quality" bold sans + "Gates" italic serif. Pill: STOP PLASTIC SKIN.
"""),
            slide("02_negative_block.png", BEAUTY_INFO + """
Headline: "Negative" bold + "block" italic coral.
Cream monospace card EXACT:
plastic skin, wax doll, beauty filter
poreless, uncanny eyes, extra fingers
CGI gloss lips, painted tears
warped text, watermark
Append to EVERY generation
"""),
            slide("03_pass_fail.png", BEAUTY_INFO + """
Headline: "Pass" bold + "or fail" italic.
Two column cream layout:
PASS: texture at 150px thumb
FAIL: porcelain cheek no pores
PASS: iris fibers + moisture physics
FAIL: repeating freckle pattern
"""),
            slide("04_plastic_recovery.png", BEAUTY_INFO + """
Headline: "Plastic" bold + "recovery" italic.
Cream card ADD:
visible pores, peach fuzz, sebum
REMOVE: flawless porcelain 8k beauty
Lower stylize on Midjourney
"""),
            slide("05_eye_recovery.png", BEAUTY_INFO + """
Headline: "Eye" bold + "recovery" italic.
Cream card ADD:
capillaries sclera, iris fibers
asymmetric catchlights
REMOVE: glowing crystal doll eyes
"""),
            slide("06_skin_macro.png", BEAUTY_MACRO + """
Skin macro proof after recovery. Labels Realistic Texture, Realistic Pores.
"""),
            slide("07_pre_publish.png", BEAUTY_INFO + """
Headline: "Pre-publish" bold + "checklist" italic.
Seven checkboxes on cream card:
DNA on every gen
Negative appended
Lighting consistent
3-angle pass
Single fluid type
Sky skin not clipped
CTA keyword correct
"""),
            slide("08_sky_cta.png", BEAUTY_SKY_HERO + """
Sky finale. "Quality" + "System" italic. Pill: COMMENT QUALITY FOR THE PDF.
"""),
        ],
    ),
    C(
        "12_Campaign_Contact_Sheet_Export",
        "campaign-contact-sheet-export.pdf",
        """Comment CAMPAIGN for the 12-page export guide  -  6 deliverables from one character, contact sheet layout, Figma assembly, and pricing the system not the image.

Productize AI beauty. Swipe the campaign board, scene swaps, and automation outline.

Follow @piyush.glitch

#AICampaign #ContactSheet #AIBeauty #CreativeWorkflow""",
        [
            slide("01_cover.png", BEAUTY_COVER + """
Overlay: "Campaign" bold sans + "Contact Sheet" italic serif. Pill: BUILD THE FULL BOARD.
"""),
            slide("02_six_deliverables.png", BEAUTY_INFO + """
Headline: "Six" bold + "deliverables" italic.
Cream card numbered:
1. Hero cover 4:5
2. Eye macro ad
3. Skin macro ad
4. 3-angle strip
5. Sky poster
6. 1080 square crop
One DNA - no reshoot
"""),
            slide("03_scene_swap.png", BEAUTY_INFO + """
Headline: "Scene" bold + "swap" italic.
Cream card:
Change BACKGROUND clause only
dark studio -> blue sky -> warm interior
NEVER remove DNA block
Face locked before scene change
"""),
            slide("04_contact_sheet.png", BEAUTY_INFO + """
Headline: "Contact" bold + "sheet" italic.
Describe visually: flat lay desk six printed cards same face
soft daylight, pen, sticky note Hero Macro Sky
arrow label Campaign Board
"""),
            slide("05_pricing.png", BEAUTY_INFO + """
Headline: "Price" bold + "the system" italic coral.
Cream card:
Package = 7 slides + 6 exports
+ DNA.txt + negative.txt + PDF
Do NOT price per image
"""),
            slide("06_figma_assembly.png", BEAUTY_INFO + """
Headline: "Figma" bold + "assembly" italic.
Cream card:
Import PNGs 1080x1350
Typography in vectors for slides 2 5 8
Photo gens for faces only
Fixes warped AI text
"""),
            slide("07_grid_slide.png", BEAUTY_TYPO + """
Headline: "Campaign" serif + "board" italic.
2x3 grid of six rounded crops same model varied shots.
Handwritten: Ready for campaign use.
"""),
            slide("08_sky_cta.png", BEAUTY_SKY_HERO + """
Sky hero. "Campaign" sans + "Ready" italic. Pill: COMMENT CAMPAIGN FOR THE PDF.
"""),
        ],
    ),
]

CAROUSEL_MAP = {f"{i:02d}": c for i, c in enumerate(CAROUSELS, start=1)}
