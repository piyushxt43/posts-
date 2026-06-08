# -*- coding: utf-8 -*-
"""16-page dense PDF for Top 10 Claude Plugins - advanced operator depth."""

PAGES = [
    [
        {"type": "heading", "text": "Top 10 Claude Plugins - Advanced Operator Guide"},
        {"type": "subhead", "text": "June 2026  |  @piyush.glitch  |  Beyond the carousel"},
        {"type": "prose", "text": (
            "The Instagram carousel names ten plugins. <b>This PDF does not repeat those one-liners.</b> "
            "It is the install manual, security audit framework, CLAUDE.md templates, hook configs, "
            "token economics, and weekly operator rituals that turn a plugin list into a measurable stack."
        )},
        {"type": "callout", "title": "Who this is for", "text": (
            "Senior devs and tech leads running Claude Code 8+ hours/day. You already know what Impeccable "
            "and Caveman are - you need the <b>exact folder paths</b>, <b>when each plugin fires</b>, "
            "<b>how to vet unaudited repos</b>, and <b>ROI metrics</b> to justify the stack to your team."
        )},
        {"type": "table", "headers": ["Page", "Advanced topic"], "rows": [
            ["2", "Skills vs plugins vs MCP vs hooks - architecture"],
            ["3-4", "Impeccable: 24 tells, pre-commit, SKILL.md fork"],
            ["5", "Caveman + HUD: token math + compact triggers"],
            ["6", "Codex handoff protocol + cost guardrails"],
            ["7", "Compound Engineering: phase gates + templates"],
            ["8", "Superpowers: which 6 skills to enable first"],
            ["9", "notebooklm-py automation + headless CI"],
            ["10", "Plugin security audit (15-point checklist)"],
            ["11", "Ecosystem discovery weekly ritual"],
            ["12", "Master CLAUDE.md + settings.json hooks"],
            ["13", "Role-based stacks (frontend/backend/PM)"],
            ["14", "4-week rollout + KPI dashboard"],
            ["15", "Extended troubleshooting matrix"],
            ["16", "FAQ + version changelog"],
        ]},
        {"type": "prose", "text": (
            "<b>Prerequisites:</b> Claude Code CLI 1.0+, Node 18+, Python 3.10+, git. "
            "Create project CLAUDE.md with /init before installing plugins. "
            "Comment <b>AI</b> on the carousel for PDF updates."
        )},
    ],
    [
        {"type": "heading", "text": "Plugin architecture (read before installing)"},
        {"type": "prose", "text": (
            "Claude Code loads four layers. Confusing them causes \"plugin not working\" support threads."
        )},
        {"type": "table", "headers": ["Layer", "Location", "What it does"], "rows": [
            ["Skills", "~/.claude/skills/<name>/SKILL.md", "Procedure playbook Claude reads on invoke"],
            ["Plugins", "Marketplace / Customize UI", "Bundled skills + slash commands + connectors"],
            ["MCP servers", "claude_desktop_config.json", "External tool APIs (GitHub, DB, etc.)"],
            ["Hooks", ".claude/settings.json", "Pre/post tool events - auto-run checks"],
        ]},
        {"type": "prose", "text": (
            "<b>Load order:</b> CLAUDE.md (project rules) -> skills (on invoke) -> plugins (session) -> "
            "MCP (tool calls). Hooks fire around Bash/Edit/Write - use for Impeccable pre-merge gates."
        )},
        {"type": "code", "text": (
            "# Verify what loaded in current session\n"
            "/help              # plugin slash commands\n"
            "/skills            # skill folders visible\n"
            "/mcp               # MCP servers connected\n"
            "/status            # model, context %, session info\n\n"
            "# Plugin install paths (June 2026)\n"
            "Marketplace: Claude Code -> /plugin -> search\n"
            "Manual skill:  ~/.claude/skills/<repo-name>/SKILL.md\n"
            "Project agent: .claude/agents/<name>.md"
        )},
        {"type": "callout", "title": "Anti-pattern", "text": (
            "Installing 10 plugins day one. Cap at 3 for week 1. Measure: tokens/PR, UI intervention rate, "
            "time-to-green-tests. Add plugin #4 only when a metric is stuck."
        )},
        {"type": "bullets", "title": "Files you will edit this week", "items": [
            "CLAUDE.md - communication, plugin invoke rules, safety",
            ".claude/settings.json - hooks, permissions, effort level",
            "~/.claude/skills/ - manual skill installs (Impeccable fallback)",
            "references/tone.md - optional brand voice for UI audits",
        ]},
    ],
    [
        {"type": "heading", "text": "Impeccable - mechanism and 24 tells"},
        {"type": "subhead", "text": "pbakaus/impeccable  |  github.com/pbakaus/impeccable"},
        {"type": "prose", "text": (
            "Impeccable is a <b>skill</b>, not a linter. It encodes design judgment Claude applies when you invoke it. "
            "The carousel says \"24 tells\" - below is the operator subset. The skill file has the authoritative list; "
            "fork it if your design system bans specific patterns (e.g. dark mode only, no gradients ever)."
        )},
        {"type": "table", "headers": ["Tell #", "AI pattern", "Human fix"], "rows": [
            ["1-4", "Purple/pink gradient heroes, gradient text", "One brand accent on solid surface"],
            ["5-7", "bounce/elastic easing, parallax on static pages", "ease-out 150-200ms or none"],
            ["8-10", "4px/6px random padding, inconsistent gaps", "8px base scale: 8/16/24/32/48"],
            ["11-13", "Inter + generic sans stack only", "Brand font + system fallback"],
            ["14-16", "Glassmorphism on cards + nav + modal", "One elevation level per view"],
            ["17-19", "Three equal CTAs, vague Get Started", "One primary verb per screen"],
            ["20-22", "Stock illustration placeholders", "Product shot or remove asset"],
            ["23-24", "Missing focus rings, tiny tap targets", "WCAG 44px min, visible :focus-visible"],
        ]},
        {"type": "prose", "text": (
            "<b>When NOT to run:</b> backend-only PRs, design token source files (unless refreshing tokens), "
            "generated Storybook snapshots. <b>When ALWAYS run:</b> marketing pages, checkout, onboarding, "
            "any component a non-dev stakeholder will screenshot."
        )},
        {"type": "callout", "title": "Advanced: fork the skill", "text": (
            "Copy SKILL.md to ~/.claude/skills/impeccable-brand/. Add your Figma token export as "
            "references/design-tokens.json. Impeccable then enforces YOUR system, not generic human design."
        )},
    ],
    [
        {"type": "heading", "text": "Impeccable - install, hooks, PR workflow"},
        {"type": "code", "text": (
            "# Install (pick one)\n"
            "npx skills add pbakaus/impeccable\n"
            "# OR manual:\n"
            "git clone https://github.com/pbakaus/impeccable.git /tmp/impeccable\n"
            "mkdir -p ~/.claude/skills/impeccable\n"
            "cp -r /tmp/impeccable/* ~/.claude/skills/impeccable/\n\n"
            "# Verify\n"
            "/skills   # impeccable listed"
        )},
        {"type": "code", "text": (
            "# .claude/settings.json - PostToolUse hook (optional)\n"
            "{\n"
            '  "hooks": {\n'
            '    "PostToolUse": [{\n'
            '      "matcher": "Write|Edit",\n'
            '      "hooks": [{\n'
            '        "type": "command",\n'
            '        "command": "echo UI file changed - run impeccable"\n'
            "      }]\n"
            "    }]\n"
            "  }\n"
            "}\n"
            "# Then in CLAUDE.md: after any .tsx Write, run impeccable on that path"
        )},
        {"type": "prose", "text": (
            "<b>PR workflow (team):</b> (1) Dev finishes UI diff. (2) Thread: \"Use skill impeccable on changed "
            "components only.\" (3) Impeccable returns second diff. (4) Human review both diffs. (5) PR template "
            "checkbox: \"Impeccable pass\" required for frontend label."
        )},
        {"type": "bullets", "title": "Pass criteria (merge gate)", "items": [
            "One primary CTA per view - secondary actions visually subdued",
            "Spacing on 8px grid - spot-check with browser devtools",
            "No gradient text on white unless brand doc requires",
            "Focus states visible - tab through interactive elements",
            "Motion under 300ms - no infinite bounce loaders",
        ]},
        {"type": "table", "headers": ["Failure", "Root cause", "Fix"], "rows": [
            ["Skill missing", "Wrong path", "~/.claude/skills/impeccable/SKILL.md"],
            ["Over-stripped UI", "Prompt too broad", "List specific tells to fix only"],
            ["Never triggers", "No invoke phrase", "Start thread: Use skill impeccable"],
            ["Conflicts with linter", "Both rewrite", "Run ESLint after Impeccable, not before"],
        ]},
    ],
    [
        {"type": "heading", "text": "Caveman + Claude HUD - token economics"},
        {"type": "subhead", "text": "Compression + visibility (pair always)"},
        {"type": "prose", "text": (
            "Caveman strips filler per message. HUD shows <b>context %</b> so you know when compression is lying "
            "(accuracy drops before bar hits red). Together they solve the #1 power-user complaint: sessions that "
            "die at 80% context mid-refactor."
        )},
        {"type": "table", "headers": ["Mode", "Token reduction", "Use when", "Stop when"], "rows": [
            ["lite", "~30%", "Single-file fixes, pairing", "Stakeholder-facing summaries"],
            ["full", "~55%", "Multi-hour refactors", "Accuracy drops on edge cases"],
            ["ultra", "~75%", "Log dumps, grep tasks", "You need prose for docs"],
        ]},
        {"type": "code", "text": (
            "# Session\n"
            "/caveman full\n\n"
            "# CLAUDE.md permanent block\n"
            "## Communication\n"
            "- Implementation threads: caveman full - no filler, no apologies\n"
            "- Client comms in /docs/external/: normal professional tone\n"
            "- Always include: paths, exit codes, test names, security notes\n"
            "- Never remove: breaking change warnings\n\n"
            "# HUD install: jarrodwatts/claude-hud via plugin market\n"
            "# Watch: context bar > 70% -> /compact focus on [next task]\n"
            "# Watch: context bar > 85% -> new thread with summary paste"
        )},
        {"type": "prose", "text": (
            "<b>Measured workflow:</b> Note context % at refactor start. Run caveman full. At 70%, "
            "/compact focus on remaining files. Compare tokens in /status before vs after - target 40%+ drop "
            "on repetitive edit loops. If tests start failing silently, drop to lite."
        )},
        {"type": "callout", "title": "HUD alert thresholds", "text": (
            "Green 0-60%: normal. Yellow 60-75%: compact at next task boundary. "
            "Red 75%+: finish current file, compact or fork thread. "
            "Subagent count > 3: check if Explore agents are still running - kill stragglers."
        )},
    ],
    [
        {"type": "heading", "text": "Codex bridge - handoff protocol"},
        {"type": "subhead", "text": "openai/codex  |  GPT-5 second opinion"},
        {"type": "prose", "text": (
            "Codex is OpenAI's Rust CLI agent. Bridged into Claude Code it provides a <b>fresh model diagnosis</b> "
            "without you copy-pasting context. Use it when Claude loops 20+ minutes on the same failing test - "
            "not for every bug (cost + context fragmentation)."
        )},
        {"type": "code", "text": (
            "# Install (see github.com/openai/codex README)\n"
            "cargo install codex-cli   # or download release binary\n"
            "export OPENAI_API_KEY=\"sk-...\"   # never commit\n\n"
            "# Handoff prompt (copy exact)\n"
            "STOP local edits. Summarize: failing test, files touched, hypotheses tried.\n"
            "Hand to codex for ONE alternative fix path. Do not apply until I say APPLY.\n"
            "Return: root cause sentence + minimal diff proposal."
        )},
        {"type": "table", "headers": ["Scenario", "Codex?", "Alternative"], "rows": [
            ["Flaky test, unclear cause", "Yes", "One codex pass then stop"],
            ["Wrong architecture", "Yes", "Then Plan agent for redesign"],
            ["Missing env var", "No", "Read error message"],
            ["Spec ambiguity", "No", "Write repro test first"],
            ["Third loop same bug", "Yes + /compact", "New thread after fix"],
        ]},
        {"type": "bullets", "title": "Cost guardrails", "items": [
            "Max 3 codex calls per day per engineer (track in standup)",
            "Never auto-merge codex output - diff review mandatory",
            "Log codex wins in docs/codex-wins.md - improves CLAUDE.md over time",
            "If codex also loops: bug is spec - escalate to human, not more AI",
        ]},
        {"type": "prose", "text": (
            "<b>Pass criteria:</b> tests green, root cause in one sentence, file churn limited to stated scope."
        )},
    ],
    [
        {"type": "heading", "text": "Compound Engineering - phase gates"},
        {"type": "subhead", "text": "EveryInc/compound-engineering-plugin"},
        {"type": "prose", "text": (
            "Compound Engineering formalizes <b>plan -> build -> review</b> as a plugin loop. "
            "Advanced use: each phase has acceptance criteria BEFORE Claude writes code. "
            "Skipping plan is the #1 reason compound feels slow - it is not slow, your spec was vague."
        )},
        {"type": "table", "headers": ["Phase", "Output artifact", "Gate (human)"], "rows": [
            ["Plan", "steps.md + acceptance criteria", "You approve plan before build"],
            ["Build", "diffs + test commands", "Tests run locally"],
            ["Review", "review.md adversarial pass", "You merge or send back"],
        ]},
        {"type": "code", "text": (
            "# Plan phase prompt\n"
            "Run compound plan for: migrate auth from sessions to JWT.\n"
            "Output: numbered steps, files touched, rollback plan, acceptance tests.\n"
            "STOP after plan - wait for my APPROVE.\n\n"
            "# Build phase (only after APPROVE)\n"
            "Execute compound build for approved plan step 1 only.\n\n"
            "# Review phase\n"
            "Run compound review - check tests, security, breaking changes."
        )},
        {"type": "prose", "text": (
            "Works in Claude Code + Cursor + Codex. Install from anthropics/claude-plugins-official marketplace. "
            "Pair with Verification subagent (PDF 02) for automated \"fake done\" checks before review phase."
        )},
        {"type": "callout", "title": "Team template", "text": (
            "Store compound plans in docs/plans/YYYY-MM-DD-feature.md. "
            "Link in PR description. Reviewer reads plan + diff - not just diff."
        )},
    ],
    [
        {"type": "heading", "text": "Superpowers - skill catalog (enable 6 first)"},
        {"type": "subhead", "text": "obra/superpowers  |  20+ packaged workflows"},
        {"type": "prose", "text": (
            "Superpowers auto-loads skills from marketplace. <b>Do not enable all 20 day one.</b> "
            "Below: the six highest ROI skills for product engineering teams, in enable order."
        )},
        {"type": "table", "headers": ["Skill", "Fires when", "ROI signal"], "rows": [
            ["brainstorm", "New feature vague", "Plan doc in 10 min vs 1hr meeting"],
            ["tdd", "Bug fix or new endpoint", "Test exists before implementation"],
            ["debug", "Intermittent failure", "Repro steps documented"],
            ["code-review", "Pre-PR", "Structured review comment"],
            ["refactor", "Tech debt sprint", "Behavior-preserving diff"],
            ["ship", "Release checklist", "Changelog + version bump"],
        ]},
        {"type": "code", "text": (
            "# Install\n"
            "Claude Code -> /plugin -> Superpowers -> Install\n\n"
            "# CLAUDE.md invoke rules\n"
            "## Superpowers\n"
            "- New feature: brainstorm skill before any code\n"
            "- Any bug fix: tdd skill mandatory\n"
            "- Pre-PR: code-review skill on diff stat summary"
        )},
        {"type": "bullets", "title": "Skills to defer (week 3+)", "items": [
            "migration - only during explicit migration sprint",
            "docs - batch weekly, not per commit",
            "performance - after feature complete",
            "security-audit - before release candidate only",
        ]},
    ],
    [
        {"type": "heading", "text": "notebooklm-py - CLI reference + automation"},
        {"type": "subhead", "text": "teng-lin/notebooklm-py  |  15k stars"},
        {"type": "prose", "text": (
            "NotebookLM clusters sources into queryable notebooks. notebooklm-py exposes the product from terminal "
            "so Claude Code can run research pipelines without browser context switching."
        )},
        {"type": "code", "text": (
            "pip install notebooklm-py\n"
            "notebooklm login                    # browser OAuth first time\n"
            "notebooklm notebook create \"Q2-Competitive-Acme\"\n"
            "notebooklm source add \"https://competitor.com/pricing\"\n"
            "notebooklm source add ./earnings-call.pdf\n"
            "notebooklm source add --url \"https://docs.vendor.com/api\"\n"
            "notebooklm ask \"Pricing changes last 90 days with citations\"\n"
            "notebooklm podcast generate --notebook \"Q2-Competitive-Acme\"\n"
            "notebooklm notebook list\n"
            "notebooklm notebook delete \"stale-notebook\""
        )},
        {"type": "prose", "text": (
            "<b>Claude Code automation:</b> Grant Bash permission for notebooklm. Thread opener: "
            "\"Research only via notebooklm-py. Output: bullet brief + source filenames. No web search.\""
        )},
        {"type": "code", "text": (
            "# Weekly cron (operator machine)\n"
            "#!/bin/bash\n"
            "NOTEBOOK=\"Weekly-Industry-Scan\"\n"
            "notebooklm source add --notebook \"$NOTEBOOK\" \"$1\"\n"
            "notebooklm ask --notebook \"$NOTEBOOK\" \"Delta vs last week\" > /tmp/brief.md\n"
            "# Claude reads /tmp/brief.md next session"
        )},
        {"type": "bullets", "title": "Hygiene rules", "items": [
            "One notebook per client or product line - never mix unrelated sources",
            "Refresh sources weekly - stale notebooks hallucinate confidently",
            "Podcast output = commute review only, not legal sign-off",
            "Headless: notebooklm login --help for token-based CI",
        ]},
    ],
    [
        {"type": "heading", "text": "Plugin security audit - 15-point checklist"},
        {"type": "prose", "text": (
            "Plugins 8-10 on the carousel are discovery tools - not install targets. "
            "Before ANY third-party plugin touches production repos, run this audit."
        )},
        {"type": "table", "headers": ["#", "Check", "Fail action"], "rows": [
            ["1", "Read full SKILL.md - what tools can it invoke?", "Reject if Bash without justification"],
            ["2", "Repo stars > 500 OR maintainer known", "Defer to sandbox repo"],
            ["3", "Last commit < 90 days", "Watchlist only"],
            ["4", "No hardcoded external URLs sending code", "Reject"],
            ["5", "No requests for API keys in SKILL.md", "Reject unless you trust maintainer"],
            ["6", "License compatible (MIT/Apache)", "Legal review"],
            ["7", "Install in --dangerously-skip-permissions sandbox first", "Never skip on prod"],
            ["8", "Run on copy of repo, not main", "Mandatory"],
            ["9", "Check GitHub issues for credential leaks", "Reject if open CVE"],
            ["10", "Diff SKILL.md vs last version on update", "Re-audit monthly"],
        ]},
        {"type": "table", "headers": ["#", "Check (cont.)", "Fail action"], "rows": [
            ["11", "Plugin only needs Read/Grep? Prefer that scope", "Restrict tools in agent md"],
            ["12", "Team approval for write-capable plugins", "Two-person rule"],
            ["13", "Log plugin invocations in standup", "Visibility"],
            ["14", "Pin plugin version in team doc", "No auto-update prod"],
            ["15", "Rollback: document uninstall steps", "Keep in RUNBOOK.md"],
        ]},
        {"type": "callout", "title": "Official sources only for week 1", "text": (
            "anthropics/claude-plugins-official + pbakaus/impeccable + jarrodwatts/claude-hud. "
            "Add community plugins week 3 after audit process is habit."
        )},
    ],
    [
        {"type": "heading", "text": "Ecosystem discovery - weekly ritual"},
        {"type": "subhead", "text": "Official directory + tracker + awesome list"},
        {"type": "prose", "text": (
            "Three repos serve different jobs. Do not treat them interchangeably."
        )},
        {"type": "table", "headers": ["Repo", "Update freq", "Operator use"], "rows": [
            ["anthropics/claude-plugins-official", "Curated releases", "Install source of truth"],
            ["linny006/claude-code-plugin-tracker", "Every 15 min", "Friday scan - what's new"],
            ["quemsah/awesome-claude-plugins", "Community index", "Research ideas, not blind install"],
        ]},
        {"type": "code", "text": (
            "# Friday 30-min plugin scan ritual\n"
            "1. Open tracker - sort by stars gained this week\n"
            "2. For each interesting repo: run 15-point audit (page 10)\n"
            "3. One sandbox install max per week\n"
            "4. If ROI proven in sandbox: propose to team Monday\n"
            "5. Update team PLUGIN-ALLOWLIST.md"
        )},
        {"type": "prose", "text": (
            "<b>PLUGIN-ALLOWLIST.md template:</b> name | repo | approved date | approver | tools allowed | notes. "
            "Any plugin not on list requires tech lead sign-off."
        )},
    ],
    [
        {"type": "heading", "text": "Master CLAUDE.md + settings.json"},
        {"type": "code", "text": (
            "# CLAUDE.md - Top 10 Plugin Stack\n\n"
            "## Communication\n"
            "- caveman full on src/ implementation\n"
            "- Normal tone on docs/external/ and client emails\n\n"
            "## UI (Impeccable)\n"
            "- After any .tsx/.vue Write: use skill impeccable on that file\n"
            "- Merge gate: impeccable pass checkbox in PR template\n\n"
            "## Token (HUD + compact)\n"
            "- Context > 70%: /compact focus on current task\n"
            "- Context > 85%: finish file, new thread\n\n"
            "## Rescue (Codex)\n"
            "- Stuck 20m same test: one codex handoff, then stop\n\n"
            "## Workflow (Compound + Superpowers)\n"
            "- New feature: compound plan APPROVE before build\n"
            "- Bug fix: superpowers tdd skill\n\n"
            "## Research\n"
            "- Source-heavy questions: notebooklm-py only\n\n"
            "## Safety\n"
            "- [REVIEW] on all external writes\n"
            "- Plugins not on PLUGIN-ALLOWLIST.md: reject install"
        )},
        {"type": "code", "text": (
            "# .claude/settings.json excerpt\n"
            "{\n"
            '  "permissions": {\n'
            '    "allow": ["Read", "Edit", "Write", "Bash(notebooklm *)", "Bash(npm test *)"],\n'
            '    "deny": ["Bash(curl *| bash)", "Write(.env)"]\n'
            "  },\n"
            '  "env": {\n'
            '    "CLAUDE_CODE_EFFORT": "medium"\n'
            "  }\n"
            "}"
        )},
    ],
    [
        {"type": "heading", "text": "Role-based plugin stacks"},
        {"type": "table", "headers": ["Role", "Week 1 stack", "Week 4 add"], "rows": [
            ["Frontend lead", "Impeccable + Caveman + HUD", "Compound + code-review superpower"],
            ["Backend lead", "Caveman + Compound + Codex", "notebooklm for API research"],
            ["Full-stack", "All week 1 core 4", "Superpowers full set"],
            ["EM / PM", "notebooklm + official directory", "HUD for eng visibility only"],
            ["Security", "Audit checklist + security-sentinel agent", "No write plugins on prod"],
        ]},
        {"type": "prose", "text": (
            "<b>Combo: Impeccable + code-reviewer subagent.</b> Impeccable fixes tells. "
            "code-reviewer agent (see Agents PDF) checks logic, tests, breaking changes. "
            "Run sequentially - not parallel - to avoid conflicting diffs."
        )},
        {"type": "callout", "title": "Combo: Caveman + HUD + Explore agent", "text": (
            "Large refactor: Explore agent maps files (Haiku, cheap). Main thread caveman full on edits. "
            "HUD watches context. At 70% compact. Explore summary stays in thread - do not re-search."
        )},
    ],
    [
        {"type": "heading", "text": "4-week rollout + KPI dashboard"},
        {"type": "table", "headers": ["Week", "Install", "KPI target"], "rows": [
            ["1", "Impeccable + Caveman + HUD", "UI PR interventions down 30%"],
            ["2", "Compound + Superpowers (6 skills)", "Plan docs on every feature PR"],
            ["3", "Codex + notebooklm", "Stuck time < 20m avg; research brief < 2hr"],
            ["4", "Ecosystem ritual + allowlist", "Zero unaudited plugins on main"],
        ]},
        {"type": "table", "headers": ["Metric", "How to measure", "Good"], "rows": [
            ["Tokens per merged PR", "/status logs weekly", "40% down vs baseline"],
            ["Impeccable pass rate", "PR checkbox", ">90% first pass"],
            ["Codex calls per week", "standup tally", "<3 per engineer"],
            ["Compact events per session", "HUD notes", "1 per 2hr session"],
            ["Plugin incidents", "postmortem count", "0 credential leaks"],
        ]},
        {"type": "prose", "text": (
            "Track baseline week 0 before any installs. Without baseline, ROI conversations fail."
        )},
    ],
    [
        {"type": "heading", "text": "Extended troubleshooting"},
        {"type": "table", "headers": ["Symptom", "Cause", "Fix"], "rows": [
            ["/skills empty", "Wrong home dir", "echo $HOME; check ~/.claude/skills"],
            ["Plugin slash missing", "Not installed/enabled", "/plugin list; restart CLI"],
            ["HUD not showing", "Terminal too narrow", "Widen terminal; reinstall HUD"],
            ["Caveman breaks tests", "ultra on complex logic", "Drop to full"],
            ["Compound stuck in build", "Plan not approved", "Say STOP; rerun plan phase"],
            ["notebooklm auth fail", "Headless server", "Token login flow"],
            ["MCP + plugin conflict", "Same tool twice", "Disable duplicate MCP"],
            ["Hooks infinite loop", "PostToolUse triggers Write", "Narrow matcher regex"],
            ["Skills work, plugin doesn't", "Different load path", "Install both or pick one"],
            ["Context still explodes", "No compact habit", "Calendar reminder: compact hourly"],
        ]},
        {"type": "callout", "title": "Nuclear reset", "text": (
            "mv ~/.claude ~/.claude.bak. Reinstall Claude Code. Restore only CLAUDE.md + skills folders. "
            "Re-add plugins one at a time. Takes 2 hours, fixes 90% of mystery bugs."
        )},
    ],
    [
        {"type": "heading", "text": "FAQ + changelog"},
        {"type": "bullets", "title": "FAQ", "items": [
            "All 10 plugins day one? No - week 1 cap is 3.",
            "Impeccable vs ESLint? Complementary - ESLint syntax, Impeccable design judgment.",
            "Caveman for client emails? No - scope to src/ in CLAUDE.md.",
            "Codex without OpenAI budget? Skip - use Plan agent + fresh thread instead.",
            "Tracker repos safe to install? No - they are indexes, not plugins.",
            "Cursor instead of Claude Code? Same skills path; plugin UI differs.",
        ]},
        {"type": "prose", "text": (
            "<b>Version:</b> June 2026 v2 (dense operator rewrite). "
            "<b>Changelog v2:</b> Added security audit, hooks, role stacks, KPI dashboard, "
            "Superpowers enable order, notebooklm automation, extended troubleshooting."
        )},
        {"type": "callout", "title": "Follow @piyush.glitch", "text": (
            "Comment <b>AI</b> on the Top 10 Claude Plugins carousel for PDF updates. "
            "Next in series: 10 Claude Agents PDF, Omni MCP bridge, Higgsfield MCP review."
        )},
    ],
]
