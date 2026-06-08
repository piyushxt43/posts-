# -*- coding: utf-8 -*-
"""
Full-page PDF blocks for Top 5 Claude Code Plugins.
Each page is a list of block dicts: heading, prose, bullets, code, table, callout, spacer.
Goal: fill the printable area - no one-line pages.
"""

# block types: heading, subhead, prose, bullets, code, table, callout, divider

PAGES = [
    # --- Page 1: Cover ---
    [
        {"type": "heading", "text": "Top 5 Claude Code Plugins"},
        {"type": "subhead", "text": "June 2026 Operator Guide  |  @piyush.glitch"},
        {"type": "prose", "text": (
            "This PDF is the companion to the Instagram carousel. It is written for developers who already "
            "use Claude Code daily but still ship purple gradients, burn tokens on filler, stall on hard bugs, "
            "and re-paste the same context into every thread."
        )},
        {"type": "callout", "title": "What you will have after 45 minutes", "text": (
            "Five tools installed in the right order, a CLAUDE.md file that enforces communication and memory rules, "
            "and a repeatable daily loop so each plugin fires at the correct moment - not all at once."
        )},
        {"type": "table", "headers": ["Plugin", "Fixes", "Repo"], "rows": [
            ["Impeccable", "24 AI UI tells in frontend", "pbakaus/impeccable"],
            ["Caveman", "~75% token noise reduction", "skill / instruction"],
            ["Codex", "GPT-5 rescue when Claude stalls", "openai/codex"],
            ["notebooklm-py", "NotebookLM from terminal", "teng-lin/notebooklm-py"],
            ["Obsidian vault", "Persistent local memory", "obsidianmd/obsidian"],
        ]},
        {"type": "prose", "text": (
            "<b>Prerequisites:</b> Claude Code CLI installed and logged in. Node.js 18+ for skill folders. "
            "Python 3.10+ for notebooklm-py. A project with CLAUDE.md at repo root (create with /init if missing)."
        )},
        {"type": "bullets", "title": "Files this guide references", "items": [
            "~/.claude/skills/ - skill folders (Impeccable)",
            "~/.claude/CLAUDE.md or project CLAUDE.md - project rules",
            "Project .claude/settings.json - hooks and permissions",
            "~/Obsidian/YourVault - optional memory directory",
        ]},
    ],
    # --- Page 2: How to read + TOC ---
    [
        {"type": "heading", "text": "How to use this guide"},
        {"type": "prose", "text": (
            "Do not skim. Each plugin page follows the same structure so you can compare apples to apples: "
            "<b>Problem</b> (why vanilla Claude fails), <b>Mechanism</b> (what the tool actually does), "
            "<b>Install</b> (copy-paste commands), <b>Invoke</b> (exact phrases in Claude Code), "
            "<b>Pass criteria</b> (how you know it worked), <b>Failure modes</b> (what to fix)."
        )},
        {"type": "table", "headers": ["Read order", "Topic", "Time"], "rows": [
            ["1", "Impeccable - UI audit skill", "12 min"],
            ["2", "Caveman - token modes", "8 min"],
            ["3", "Codex - second opinion", "10 min"],
            ["4", "notebooklm-py - research", "12 min"],
            ["5", "Obsidian - vault memory", "8 min"],
            ["6", "Install stack (one sitting)", "15 min"],
            ["7", "Daily loop + master CLAUDE.md", "10 min"],
            ["8", "Troubleshooting + FAQ", "5 min"],
        ]},
        {"type": "callout", "title": "Instagram CTA", "text": (
            "Comment <b>PLUGINS</b> on the @piyush.glitch carousel post. Auto-DM this PDF from your workflow tool. "
            "Version tag: June 2026 v1."
        )},
        {"type": "prose", "text": (
            "<b>Safety rule for all plugins:</b> Nothing in this guide auto-merges code, sends email, or writes to "
            "production databases. Claude drafts; you review. Tag risky outputs [REVIEW] before shipping."
        )},
    ],
    # --- Page 3: Impeccable overview ---
    [
        {"type": "heading", "text": "Plugin 1: Impeccable"},
        {"type": "subhead", "text": "Kills AI slop in your UI before it ships"},
        {"type": "prose", "text": (
            "Claude Code is excellent at generating working React, Vue, and Svelte components. It is also excellent "
            "at generating the same 24 visual tells that make users think \"AI made this.\" Impeccable is a Claude "
            "skill that audits files for those tells and rewrites them to match human design standards - spacing scale, "
            "restrained color, motion that does not bounce for no reason, typography that is not Inter-on-gradient soup."
        )},
        {"type": "prose", "text": (
            "<b>When to run:</b> After Claude produces any UI diff and before you accept the PR. "
            "Not on backend-only changes. Not on design system token files unless you are intentionally refreshing tokens."
        )},
        {"type": "table", "headers": ["AI tell (sample)", "Human fix"], "rows": [
            ["Purple/pink gradient hero text", "Solid ink on white or one brand accent"],
            ["bounce / elastic easing on hovers", "ease-out 150-200ms or none"],
            ["Cramped 4px padding grids", "8px base spacing scale (8/16/24/32)"],
            ["Generic \"Get Started\" CTA only", "Verb matched to user job"],
            ["Glassmorphism on everything", "One surface depth level max"],
            ["Stock illustration placeholders", "Real product screenshot or remove"],
        ]},
        {"type": "prose", "text": (
            "The carousel claims <b>24 tells</b> - treat the table above as examples. The skill encodes the full list. "
            "Your job is to run it consistently, not memorize every tell."
        )},
    ],
    # --- Page 4: Impeccable install ---
    [
        {"type": "heading", "text": "Impeccable: install and daily use"},
        {"type": "subhead", "text": "github.com/pbakaus/impeccable"},
        {"type": "code", "text": (
            "# 1) Clone and install as Claude Code skill\n"
            "git clone https://github.com/pbakaus/impeccable.git\n"
            "mkdir -p ~/.claude/skills/impeccable\n"
            "cp -r impeccable/* ~/.claude/skills/impeccable/\n\n"
            "# 2) Verify skill is visible\n"
            "# In Claude Code:\n"
            "/skills\n"
            "# You should see impeccable in the list"
        )},
        {"type": "prose", "text": (
            "<b>Invoke pattern:</b> Reference the skill by name plus the file path. Be specific about which tells "
            "you saw in the draft so Claude does not over-correct into a different generic style."
        )},
        {"type": "code", "text": (
            "Use skill impeccable.\n"
            "Audit src/components/marketing/Hero.tsx.\n"
            "Remove AI tells: purple gradient text, bounce easing, cramped padding.\n"
            "Keep: headline copy, CTA destination, component API.\n"
            "Return diff only."
        )},
        {"type": "bullets", "title": "Pass criteria (merge gate)", "items": [
            "Primary CTA has one clear action - not three equal buttons",
            "Spacing uses consistent scale - no random 6px and 13px pairs",
            "Motion is subtle or absent on marketing pages",
            "Focus states visible for keyboard users",
            "No gradient text on white backgrounds unless brand requires it",
        ]},
        {"type": "bullets", "title": "Failure modes", "items": [
            "Skill not listed: wrong folder - must be ~/.claude/skills/impeccable/SKILL.md",
            "Over-stripped design: prompt said remove all color - narrow the tell list",
            "Skill never triggered: you forgot to say Use skill impeccable at thread start",
        ]},
    ],
    # --- Page 5: Caveman ---
    [
        {"type": "heading", "text": "Plugin 2: Caveman mode"},
        {"type": "subhead", "text": "Cuts token noise - keeps technical accuracy"},
        {"type": "prose", "text": (
            "Long Claude Code sessions accumulate pleasantries (\"Great question!\"), repeated summaries of work "
            "already visible in the diff, and article-length explanations when you only need the patch. Caveman mode "
            "is a communication constraint: drop filler, keep types, errors, security notes, and test names intact."
        )},
        {"type": "table", "headers": ["Mode", "Use when", "Risk"], "rows": [
            ["lite", "Quick fixes, single-file edits", "Low - still readable"],
            ["full", "Multi-hour refactors, debugging", "Medium - review diffs carefully"],
            ["ultra", "Log dumps, test failures, grep tasks", "High - too terse for stakeholders"],
        ]},
        {"type": "code", "text": (
            "# Session toggle\n"
            "/caveman ultra\n\n"
            "# Permanent - add to project CLAUDE.md\n"
            "## Communication\n"
            "- caveman full: no filler, no apologies, no restating the prompt\n"
            "- Always include: file paths, error codes, command output\n"
            "- Never remove: security warnings, breaking change notes"
        )},
        {"type": "prose", "text": (
            "<b>Measured outcome:</b> Operators report roughly 75% fewer output tokens on repetitive tasks. "
            "Measure yourself: note context % before/after on a 2-hour refactor. If accuracy drops, step down to lite."
        )},
        {"type": "callout", "title": "Pair with /compact", "text": (
            "After each merged feature, run /compact focus on [next task] so Caveman is not fighting a bloated thread. "
            "Caveman reduces noise per message; compact reduces noise in memory."
        )},
    ],
    # --- Page 6: Codex ---
    [
        {"type": "heading", "text": "Plugin 3: Codex bridge"},
        {"type": "subhead", "text": "GPT-5 second opinion when Claude stalls"},
        {"type": "prose", "text": (
            "Sometimes Claude Code loops: it partial-fixes a test file, re-introduces the bug, apologizes, tries again. "
            "Codex is OpenAI's lightweight coding agent CLI (Rust). Bridged into your session, it can take the current "
            "thread context and ask GPT-5 for a fresh diagnosis or a second implementation path - without you "
            "manually copying context into a new chat."
        )},
        {"type": "prose", "text": (
            "<b>Repo:</b> github.com/openai/codex (30k+ stars). Install per README - typically a cargo install or "
            "released binary plus API key in environment."
        )},
        {"type": "code", "text": (
            "# Example env (never commit keys)\n"
            "export OPENAI_API_KEY=\"sk-...\"\n\n"
            "# When Claude has stalled 20+ minutes:\n"
            "Stop local edits. Ask Claude:\n"
            "\"Use codex to analyze why auth middleware tests fail.\n"
            " Propose one clean fix. Do not apply until I approve.\""
        )},
        {"type": "bullets", "title": "Operator rules", "items": [
            "One codex rescue per stuck issue - then /compact or new thread",
            "Never auto-merge codex output - diff review required",
            "Log what codex suggested that Claude missed - improves CLAUDE.md",
            "If codex also loops, the bug is spec ambiguity - write a repro test first",
        ]},
        {"type": "prose", "text": (
            "<b>Pass criteria:</b> Tests green, root cause named in one sentence, no unrelated file churn."
        )},
    ],
    # --- Page 7: notebooklm ---
    [
        {"type": "heading", "text": "Plugin 4: notebooklm-py"},
        {"type": "subhead", "text": "NotebookLM driven from Claude Code terminal"},
        {"type": "prose", "text": (
            "Research workflows die in tab soup: PDFs in Drive, URLs in Slack, notes in Notion. NotebookLM clusters "
            "sources into a notebook you can query. notebooklm-py exposes that product programmatically so Claude Code "
            "can create notebooks, attach sources, and generate summaries or podcasts while you stay in the terminal."
        )},
        {"type": "code", "text": (
            "pip install notebooklm-py\n"
            "notebooklm login\n\n"
            "notebooklm notebook create \"Client - Acme Q2\"\n"
            "notebooklm source add \"https://competitor.com/pricing\"\n"
            "notebooklm source add \"/path/to/earnings.pdf\"\n"
            "notebooklm ask \"What changed in pricing vs last quarter?\"\n"
            "notebooklm podcast generate --notebook \"Client - Acme Q2\""
        )},
        {"type": "prose", "text": (
            "<b>Claude Code pattern:</b> Give Claude permission to run notebooklm commands via Bash. "
            "Start thread with: \"Research task: use notebooklm-py only; summarize in bullet brief; cite sources.\""
        )},
        {"type": "bullets", "title": "Best practices", "items": [
            "One notebook per client or per product line - do not mix unrelated sources",
            "Refresh sources weekly - stale notebooks hallucinate confidently",
            "Podcast output is for commute review - not for legal sign-off",
            "Headless login: see notebooklm login --help for token-based CI setups",
        ]},
    ],
    # --- Page 8: Obsidian ---
    [
        {"type": "heading", "text": "Bonus: Obsidian vault memory"},
        {"type": "subhead", "text": "Not a plugin - a folder Claude reads"},
        {"type": "prose", "text": (
            "The highest-ROI \"plugin\" on the carousel is not code: it is pointing Claude Code at your Obsidian vault. "
            "Every meeting note, PRD, and decision log lives in markdown on disk. Claude greps and reads those files "
            "instead of pretending it remembers last week's architecture call."
        )},
        {"type": "code", "text": (
            "# Add to project CLAUDE.md\n"
            "## Memory - Obsidian (read-first)\n"
            "Vault path: /Users/you/Obsidian/ProductionVault\n"
            "Before product or architecture questions:\n"
            "1. Search vault for relevant notes (rg or Claude read)\n"
            "2. Cite note filename in answer\n"
            "3. Never write to vault without [REVIEW] in commit message"
        )},
        {"type": "prose", "text": (
            "<b>Vault hygiene:</b> Use consistent filenames (YYYY-MM-DD-client-topic.md). "
            "Link decisions with [[wikilinks]] so human browsing stays easy. "
            "Symlink client subfolder into code repo only when needed for a sprint."
        )},
        {"type": "bullets", "title": "What to store vs not store", "items": [
            "Store: ADRs, API contracts, onboarding checklists, postmortems",
            "Store: Client tone guides and brand voice notes",
            "Do not store: raw API keys, passwords, unredacted PII",
            "Do not store: huge binary PDFs - link path or summarize in md first",
        ]},
    ],
    # --- Page 9: Install stack ---
    [
        {"type": "heading", "text": "One-session install stack"},
        {"type": "subhead", "text": "45 minutes - do not change order"},
        {"type": "table", "headers": ["Step", "Action", "Verify"], "rows": [
            ["1", "Install Impeccable skill folder", "/skills lists impeccable"],
            ["2", "Add Caveman block to CLAUDE.md", "Next reply has no filler"],
            ["3", "Install codex CLI + API key", "codex --version works"],
            ["4", "pip install notebooklm-py + login", "notebooklm notebook list"],
            ["5", "Set Obsidian vault path in CLAUDE.md", "Claude cites a real note"],
            ["6", "Restart Claude Code", "All skills load fresh"],
        ]},
        {"type": "prose", "text": (
            "Restart matters. Skills copied while a session is open may not appear until CLI reload. "
            "After restart, run a <b>smoke test thread</b>: one UI file through Impeccable, one /caveman ultra "
            "on a log file, one notebooklm ask, one vault search question."
        )},
        {"type": "callout", "title": "Smoke test script (copy to terminal notes)", "text": (
            "1) impeccable on Button.tsx  2) caveman ultra + fix lint  "
            "3) notebooklm ask on test notebook  4) What did we decide about auth in vault?"
        )},
    ],
    # --- Page 10: Daily loop + master CLAUDE.md ---
    [
        {"type": "heading", "text": "Daily operator loop"},
        {"type": "subhead", "text": "When each plugin fires"},
        {"type": "table", "headers": ["Time", "Action", "Tool"], "rows": [
            ["Morning", "Refresh notebook sources for active client", "notebooklm-py"],
            ["Build", "caveman full on implementation threads", "Caveman"],
            ["Pre-PR", "impeccable on every UI touched file", "Impeccable"],
            ["Stuck 20m+", "one codex rescue, then stop", "Codex"],
            ["Evening", "decision log md to Obsidian vault", "Vault"],
        ]},
        {"type": "heading", "text": "Master CLAUDE.md snippet (combine all five)"},
        {"type": "code", "text": (
            "# Project: [NAME]\n\n"
            "## Communication\n"
            "- caveman full on implementation; normal tone on client emails\n\n"
            "## UI\n"
            "- After UI diffs: use skill impeccable before merge\n\n"
            "## Research\n"
            "- Use notebooklm-py for source-heavy questions\n\n"
            "## Memory\n"
            "- Vault: /absolute/path/to/Obsidian/Vault\n"
            "- Search vault before architecture answers\n\n"
            "## Rescue\n"
            "- If stuck 20m on same test: one codex diagnosis, then /compact\n\n"
            "## Safety\n"
            "- Never commit .env; tag [REVIEW] on writes"
        )},
    ],
    # --- Page 11: Troubleshooting ---
    [
        {"type": "heading", "text": "Troubleshooting"},
        {"type": "table", "headers": ["Symptom", "Likely cause", "Fix"], "rows": [
            ["impeccable not in /skills", "Wrong path", "~/.claude/skills/impeccable/SKILL.md"],
            ["UI still looks AI", "Skill not invoked", "Say Use skill impeccable explicitly"],
            ["Caveman too terse", "ultra on wrong task", "Drop to lite for docs"],
            ["Codex auth error", "Missing API key", "export OPENAI_API_KEY"],
            ["notebooklm login fail", "Headless env", "Use token flow from --help"],
            ["Vault answers wrong", "Relative path", "Absolute path in CLAUDE.md"],
            ["Tokens still high", "No /compact", "Compact at task boundaries"],
        ]},
        {"type": "prose", "text": (
            "If multiple plugins conflict, simplify: run <b>Caveman + Obsidian</b> for one week before adding Codex. "
            "Add Impeccable when you touch frontend again. Add notebooklm when research is the bottleneck."
        )},
    ],
    # --- Page 12: FAQ + close ---
    [
        {"type": "heading", "text": "FAQ and next steps"},
        {"type": "bullets", "title": "FAQ", "items": [
            "Do I need all five day one? No - start Caveman + Obsidian, add Impeccable on next UI PR.",
            "Does Obsidian sync break paths? Use one machine path or sync vault before sessions.",
            "Will Caveman break client calls? Use normal tone in CLAUDE.md for external comms files.",
            "Is codex required? No - only for stuck threads after 20 minutes.",
            "Can I use Cursor instead? Same ideas; skill paths differ - see Cursor rules docs.",
        ]},
        {"type": "prose", "text": (
            "<b>Metrics that prove ROI:</b> (1) intervention rate on UI PRs drops after Impeccable, "
            "(2) tokens per merged PR drops after Caveman + compact, (3) time-to-diagnosis drops after Obsidian vault, "
            "(4) research briefs faster with notebooklm."
        )},
        {"type": "callout", "title": "Stay updated", "text": (
            "Follow @piyush.glitch on Instagram. Comment PLUGINS on the carousel for PDF updates. "
            "Next guides in this series: MCP sync, Cursor agent stack, multi-model ops."
        )},
        {"type": "prose", "text": (
            "You now have the same stack shown in the carousel: Impeccable, Caveman, Codex, notebooklm-py, and Obsidian memory. "
            "Install in order, paste the master CLAUDE.md, run the smoke test, then ship one real PR with the full loop."
        )},
    ],
]
