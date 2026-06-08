# -*- coding: utf-8 -*-
"""14-page dense PDF for 10 Claude Agents."""

PAGES = [
    [
        {"type": "heading", "text": "10 Claude Agents - Subagent Playbook"},
        {"type": "subhead", "text": "Advanced context isolation  |  @piyush.glitch"},
        {"type": "prose", "text": (
            "The carousel names agents. This PDF delivers <b>.claude/agents/ templates</b>, "
            "tool permission matrices, Coordinator Mode setup, VoltAgent catalog install scripts, "
            "multi-agent orchestration patterns, and failure recovery - not slide copy."
        )},
        {"type": "callout", "title": "Core insight", "text": (
            "Parent thread sees <b>summary only</b>. Subagent context is isolated. "
            "That is the entire value prop - stop grepping 400 files into main thread."
        )},
        {"type": "table", "headers": ["Page", "Topic"], "rows": [
            ["2", "Agent file anatomy + frontmatter spec"],
            ["3", "Explore agent - advanced invoke patterns"],
            ["4", "Plan agent - acceptance criteria templates"],
            ["5", "Verification agent - auto-trigger behavior"],
            ["6", "Fork + parallel agent patterns"],
            ["7", "Coordinator Mode - feature flag + XML protocol"],
            ["8", "VoltAgent catalog - install 5 agents"],
            ["9", "security-sentinel + code-reviewer deep dive"],
            ["10", "context-manager + debugger + architect"],
            ["11", "Multi-agent daily workflow (timed)"],
            ["12", "CLAUDE.md agent routing rules"],
            ["13", "Troubleshooting + permission errors"],
            ["14", "Team rollout checklist"],
        ]},
    ],
    [
        {"type": "heading", "text": "Agent file anatomy"},
        {"type": "prose", "text": (
            "Agents live in <b>.claude/agents/name.md</b> (project) or <b>~/.claude/agents/</b> (global). "
            "Claude picks agents by matching your prompt to the <b>description</b> field - "
            "this field is more important than the system prompt body."
        )},
        {"type": "code", "text": (
            "---\n"
            "name: explore-codebase\n"
            "description: >\n"
            "  Read-only codebase search and architecture mapping.\n"
            "  Use PROACTIVELY when user mentions: find, search, map, where is, how does X work.\n"
            "tools: Read, Grep, Glob, Bash(rg *)\n"
            "model: haiku\n"
            "permissionMode: plan\n"
            "---\n\n"
            "You are Explore. READ ONLY. Never Edit or Write.\n"
            "Output format:\n"
            "1. Summary (5 bullets max)\n"
            "2. Key files with paths\n"
            "3. Open questions for parent agent"
        )},
        {"type": "table", "headers": ["Field", "Purpose", "Mistake"], "rows": [
            ["name", "Unique id, lowercase-hyphen", "Spaces in name"],
            ["description", "When Claude auto-invokes", "Vague 'helps with code'"],
            ["tools", "Hard cap on capabilities", "Leave default all tools"],
            ["model", "haiku=cheap, sonnet=default", "Opus for every search"],
            ["permissionMode", "plan=read-only mode", "Skip on Explore agents"],
        ]},
        {"type": "bullets", "title": "Reload after changes", "items": [
            "Restart Claude Code session after adding/editing agent files",
            "Test with explicit: 'Use the explore-codebase agent to...'",
            "If auto-invoke fails, improve description with trigger phrases",
        ]},
    ],
    [
        {"type": "heading", "text": "Explore agent - advanced patterns"},
        {"type": "subhead", "text": "Built-in Haiku | Read-only search"},
        {"type": "prose", "text": (
            "Explore is built-in but underused. Advanced teams run Explore <b>before every refactor >10 files</b> "
            "and attach output to PR description as 'architecture snapshot'."
        )},
        {"type": "code", "text": (
            "# Pattern A: Map before refactor\n"
            "Use Explore agent to map all auth-related files.\n"
            "Include: middleware, tests, env vars, external IdP calls.\n"
            "Return file tree + data flow summary only.\n\n"
            "# Pattern B: Grep replacement\n"
            "Use Explore agent: find every usage of deprecated PaymentAPI class.\n"
            "Group by: production code vs tests vs docs.\n\n"
            "# Pattern C: Onboarding new dev\n"
            "Use Explore agent: 30-min architecture brief for new engineer.\n"
            "Cover: entry points, deploy pipeline, top 5 gotchas."
        )},
        {"type": "table", "headers": ["Task size", "Explore?", "Main thread?"], "rows": [
            ["<5 files known", "No", "Direct edit"],
            ["10-50 files unknown", "Yes", "Edit after summary"],
            ["Full repo map", "Yes + save to docs/", "Never grep main thread"],
            ["Security audit surface", "Yes + security-sentinel", "Sequential"],
        ]},
        {"type": "callout", "title": "Cost note", "text": (
            "Haiku Explore costs ~10x less than Sonnet main thread searching. "
            "Run Explore even when you think you know the repo - surprises are common."
        )},
    ],
    [
        {"type": "heading", "text": "Plan agent - acceptance criteria"},
        {"type": "subhead", "text": "Built-in | Read-only planning"},
        {"type": "prose", "text": (
            "Plan agent outputs steps + acceptance criteria. <b>Advanced use:</b> criteria must be "
            "testable commands, not prose. Bad: 'auth works'. Good: 'npm test auth.test.ts passes'."
        )},
        {"type": "code", "text": (
            "Use Plan agent for: migrate Stripe webhooks to idempotent handlers.\n\n"
            "Required output sections:\n"
            "1. Scope (files in/out)\n"
            "2. Numbered steps with rollback per step\n"
            "3. Acceptance criteria as shell commands\n"
            "4. Risk register (high/medium/low)\n"
            "STOP - do not implement until I reply APPROVE."
        )},
        {"type": "table", "headers": ["Criteria type", "Example", "Why"], "rows": [
            ["Test command", "pnpm test src/auth/", "Objective pass/fail"],
            ["Lint command", "pnpm lint --max-warnings 0", "CI parity"],
            ["Manual check", "[REVIEW] staging login flow", "Human gate flagged"],
            ["Metric", "p99 latency unchanged +/- 5%", "Performance guard"],
        ]},
        {"type": "prose", "text": (
            "Store approved plans in docs/plans/. Link in Jira/Linear. "
            "Compound Engineering plugin (Plugins PDF) uses same plan artifact."
        )},
    ],
    [
        {"type": "heading", "text": "Verification agent"},
        {"type": "subhead", "text": "Adversarial 'fake done' detection"},
        {"type": "prose", "text": (
            "Leaked Claude Code source indicates Verification can auto-trigger when you close 3+ tasks "
            "without a verify step. Treat it as <b>adversarial QA</b> - did the work actually ship?"
        )},
        {"type": "code", "text": (
            "# Manual invoke (always do this before 'done')\n"
            "Spawn verification agent. Check:\n"
            "- All acceptance criteria from plan executed?\n"
            "- Tests run and passed (show output)?\n"
            "- No TODO comments left in production paths?\n"
            "- Breaking changes documented?\n"
            "Output: PASS / FAIL with evidence."
        )},
        {"type": "table", "headers": ["Fake done signal", "Verification catches"], "rows": [
            ["Tests not run", "Asks for test output"],
            ["Partial implementation", "Cross-checks plan steps"],
            ["Commented-out code", "Flags production paths"],
            ["Missing migration", "Checks schema files"],
        ]},
        {"type": "callout", "title": "Team rule", "text": (
            "Add to CLAUDE.md: 'No task marked complete without verification agent PASS.' "
            "Enforce in standup - not optional for production repos."
        )},
    ],
    [
        {"type": "heading", "text": "Fork + parallel patterns"},
        {"type": "prose", "text": (
            "<b>Fork:</b> Subagent inherits full parent conversation - for side tasks without re-explaining. "
            "<b>Parallel:</b> Multiple agents same time - only when tasks are independent."
        )},
        {"type": "code", "text": (
            "# Fork pattern - side investigation\n"
            "Fork subagent: investigate why CI flaky on main only.\n"
            "Parent continues: implement feature on branch.\n"
            "Fork returns: root cause summary only.\n\n"
            "# Parallel pattern (safe)\n"
            "Agent A (Explore): map payment module\n"
            "Agent B (Explore): map notification module\n"
            "Main thread: waits for both summaries before plan"
        )},
        {"type": "table", "headers": ["Pattern", "Safe when", "Unsafe when"], "rows": [
            ["Fork", "Read-only side task", "Both edit same files"],
            ["Parallel Explore", "Disjoint directories", "Same file set"],
            ["Parallel Edit", "Never default", "Coordinated lock file"],
        ]},
    ],
    [
        {"type": "heading", "text": "Coordinator Mode"},
        {"type": "subhead", "text": "Experimental agent swarms | COORDINATOR_MODE"},
        {"type": "prose", "text": (
            "Coordinator Mode spawns parallel workers via XML task protocol + shared scratch directory. "
            "For multi-phase agency workflows - large migrations, multi-repo refactors. Not for daily fixes."
        )},
        {"type": "code", "text": (
            "# Enable (see AKCodez/claude-code-secrets for current flag)\n"
            "# Set in environment or feature flags per Anthropic docs\n"
            "export CLAUDE_CODE_COORDINATOR_MODE=1\n\n"
            "# Invoke\n"
            "Coordinator: split migration into 4 parallel workstreams.\n"
            "Scratch dir: .claude/coordinator-scratch/\n"
            "Each worker reports XML task complete.\n"
            "Coordinator merges summaries - I review before any merge."
        )},
        {"type": "bullets", "title": "When to use vs skip", "items": [
            "Use: 50+ file migration, multi-package monorepo change",
            "Use: deadline crunch with clear task boundaries",
            "Skip: single bug fix, unclear spec, junior on call alone",
            "Skip: production incident - use single thread + caveman",
        ]},
    ],
    [
        {"type": "heading", "text": "VoltAgent catalog install"},
        {"type": "subhead", "text": "VoltAgent/awesome-claude-code-subagents | 154 agents"},
        {"type": "code", "text": (
            "# Install 5 starter agents\n"
            "git clone https://github.com/VoltAgent/awesome-claude-code-subagents.git /tmp/va\n"
            "mkdir -p .claude/agents\n"
            "cp /tmp/va/agents/security-sentinel.md .claude/agents/\n"
            "cp /tmp/va/agents/code-reviewer.md .claude/agents/\n"
            "cp /tmp/va/agents/debugger.md .claude/agents/\n"
            "cp /tmp/va/agents/context-manager.md .claude/agents/\n"
            "cp /tmp/va/agents/architect-review.md .claude/agents/\n\n"
            "# Browse in Claude Code\n"
            "/subagent-catalog:search security\n"
            "/subagent-catalog:fetch code-reviewer"
        )},
        {"type": "table", "headers": ["Agent", "Model", "Tools"], "rows": [
            ["security-sentinel", "sonnet", "Read, Grep, Glob"],
            ["code-reviewer", "sonnet", "Read, Grep, Glob"],
            ["debugger", "sonnet", "Read, Bash, Grep"],
            ["context-manager", "haiku", "Read only"],
            ["architect-review", "opus", "Read, Grep"],
        ]},
        {"type": "prose", "text": (
            "Edit copied files: tighten description with your repo trigger phrases. "
            "Remove tools you do not want - never leave Bash on review-only agents."
        )},
    ],
    [
        {"type": "heading", "text": "security-sentinel + code-reviewer"},
        {"type": "subhead", "text": "Pre-merge security and quality gates"},
        {"type": "code", "text": (
            "# security-sentinel invoke (pre-deploy)\n"
            "Use security-sentinel agent on diff against main.\n"
            "Check: OWASP top 10, hardcoded secrets, SQL injection, SSRF.\n"
            "Output: severity-tagged findings. No auto-fix.\n\n"
            "# code-reviewer invoke (pre-PR)\n"
            "Use code-reviewer agent on git diff stat summary.\n"
            "Check: test coverage, breaking API changes, error handling.\n"
            "Output: structured review - Approve / Request changes."
        )},
        {"type": "table", "headers": ["Finding", "Action"], "rows": [
            ["CRITICAL secret in diff", "Block merge immediately"],
            ["HIGH missing auth check", "Fix before review request"],
            ["MEDIUM style issue", "Optional fix"],
            ["Reviewer Request changes", "Address before human review"],
        ]},
        {"type": "callout", "title": "Never auto-merge", "text": (
            "Agents output comments - they do not merge PRs. Pair with Impeccable for UI PRs (Plugins PDF)."
        )},
    ],
    [
        {"type": "heading", "text": "context-manager + debugger + architect"},
        {"type": "prose", "text": (
            "<b>context-manager:</b> Suggests what to drop from bloated threads. "
            "Invoke at 65% context before blind /compact.<br/>"
            "<b>debugger:</b> Isolates repro steps + root cause. Use when 3+ hypotheses failed.<br/>"
            "<b>architect-review:</b> Adversarial system design before build. Opus model - use sparingly."
        )},
        {"type": "code", "text": (
            "# context-manager\n"
            "Use context-manager agent: thread at 68% context.\n"
            "What can we drop without losing task state? Output: keep list + drop list.\n\n"
            "# debugger\n"
            "Use debugger agent: flaky test payments.test.ts fails 30% on CI.\n"
            "Output: repro steps, minimal hypothesis tree, suggested instrumentations.\n\n"
            "# architect-review\n"
            "Use architect-review agent: propose event-driven billing redesign.\n"
            "Attack: scaling, consistency, failure modes. No code - design only."
        )},
        {"type": "bullets", "title": "Model cost routing", "items": [
            "Haiku: Explore, context-manager",
            "Sonnet: security-sentinel, code-reviewer, debugger",
            "Opus: architect-review only - max 2 calls/week",
        ]},
    ],
    [
        {"type": "heading", "text": "Multi-agent daily workflow"},
        {"type": "table", "headers": ["Time", "Agent(s)", "Output"], "rows": [
            ["9:00", "Explore", "Yesterday's touched modules map"],
            ["9:15", "Plan", "Today's feature plan + criteria"],
            ["10:00-14:00", "Main + caveman", "Implementation diffs"],
            ["14:00", "code-reviewer", "Pre-PR review comment"],
            ["14:30", "security-sentinel", "If touching auth/payments"],
            ["15:00", "Verification", "PASS before PR open"],
            ["17:00", "context-manager", "If thread > 60% context"],
        ]},
        {"type": "prose", "text": (
            "Total agent calls target: 5-8 per day. More = you are using agents as chat, not isolation."
        )},
    ],
    [
        {"type": "heading", "text": "CLAUDE.md agent routing"},
        {"type": "code", "text": (
            "## Agent routing\n"
            "- Refactor >10 files: Explore agent FIRST\n"
            "- New feature: Plan agent -> APPROVE -> build\n"
            "- Pre-PR: code-reviewer agent mandatory\n"
            "- Auth/payment diffs: security-sentinel mandatory\n"
            "- Thread >65% context: context-manager before compact\n"
            "- Stuck debugging 30m: debugger agent once\n"
            "- Architecture proposals: architect-review before implementation\n"
            "- Task complete: verification agent PASS required\n\n"
            "## Parallel rules\n"
            "- Parallel Explore only on disjoint directories\n"
            "- Never parallel Write on same branch"
        )},
    ],
    [
        {"type": "heading", "text": "Troubleshooting"},
        {"type": "table", "headers": ["Symptom", "Fix"], "rows": [
            ["Agent never invoked", "Rewrite description with trigger phrases"],
            ["Agent edits when read-only", "Set tools: Read, Grep, Glob only"],
            ["Subagent pollutes context", "Use Explore not main for search"],
            ["Catalog search empty", "Update Claude Code CLI"],
            ["Permission denied Bash", "Add to tools or remove Bash from agent"],
            ["Wrong model cost", "Set model: haiku on Explore"],
            ["Coordinator crash", "Disable flag; fall back to sequential"],
            ["Duplicate agent names", "Unique name field required"],
        ]},
        {"type": "callout", "title": "Debug invoke", "text": (
            "Explicit beat implicit: 'Use the code-reviewer agent' always works. "
            "Auto-invoke depends on description quality - iterate weekly."
        )},
    ],
    [
        {"type": "heading", "text": "Team rollout checklist"},
        {"type": "table", "headers": ["Done?", "Item"], "rows": [
            ["", ".claude/agents/ in repo (committed)"],
            ["", "5 VoltAgent agents installed + customized"],
            ["", "CLAUDE.md agent routing section"],
            ["", "PR template: verification PASS checkbox"],
            ["", "Explore mandatory for >10 file refactors"],
            ["", "Opus architect-review budget documented"],
            ["", "Team trained: agents summarize, parent decides"],
        ]},
        {"type": "callout", "title": "@piyush.glitch", "text": (
            "Comment <b>AI</b> on carousel. Version: June 2026 v2 dense playbook."
        )},
    ],
]
