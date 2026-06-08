# -*- coding: utf-8 -*-
"""Extended PDF content for batch50 carousel 01."""

BATCH50_01_EXTENDED = {
    "50_Series_Carousels/01_50_Claude_Agent_Secrets": {
        "carousel_slides": [
            ("1", "I tested 50 Claude agent tricks", "12 consistently ship work."),
            ("2", "Subagents", "5 delegation secrets to reduce context noise."),
            ("3", "Hooks", "5 lifecycle guardrail secrets for safety."),
            ("4", "MCP", "5 connector secrets for real operations."),
            ("5", "Skills", "5 SKILL.md patterns for repeatability."),
            ("6", "/compact", "5 context secrets to prevent drift."),
            ("7", "Effort + model", "5 routing secrets for cost and quality."),
            ("8", "Hidden workflows", "5 operator loops for daily shipping."),
            ("9", "GitHub refs", "5 repos worth cloning immediately."),
            ("10", "Final 5", "Rollout cadence plus Comment AI CTA."),
        ],
        "extra_sections": [
            {
                "tab": "04",
                "title": "Bucket 1: Subagents (secrets 1-5)",
                "bullets": [
                    ("1", "Create project subagents in `.claude/agents/` for versioned team behavior."),
                    ("2", "Use a cheap model for Explore and reserve stronger models for final judgment."),
                    ("3", "Whitelist tools per subagent to avoid accidental broad permissions."),
                    ("4", "Use `isolation: worktree` for parallel task streams with low merge conflict risk."),
                    ("5", "Set `maxTurns` to prevent low-signal wandering loops on narrow tasks."),
                ],
            },
            {
                "tab": "05",
                "title": "Bucket 2: Hooks (secrets 6-10)",
                "bullets": [
                    ("6", "Use `PreToolUse` to block dangerous shell commands before execution."),
                    ("7", "Use `PostToolUse` to auto-format and run lightweight checks after edits."),
                    ("8", "Add `Stop` hooks for final sanity checks and summary output."),
                    ("9", "Use regex `matcher` fields to target only the tools you intend."),
                    ("10", "Return block decisions deterministically so failures become teachable and repeatable."),
                ],
                "code": {
                    "caption": "Project hook shape",
                    "lines": "{\n  \"hooks\": {\n    \"PreToolUse\": [{\"matcher\": \"Bash\", \"hooks\": [{\"type\": \"command\", \"command\": \"./.claude/hooks/block.sh\"}]}],\n    \"PostToolUse\": [{\"matcher\": \"Write|Edit\", \"hooks\": [{\"type\": \"command\", \"command\": \"./.claude/hooks/fix.sh\"}]}]\n  }\n}"
                },
            },
            {
                "tab": "06",
                "title": "Bucket 3: MCP (secrets 11-15)",
                "body": [
                    "MCP quality depends more on tool schema clarity and permissions than on model sophistication."
                ],
                "bullets": [
                    ("11", "Start read-only tools first and gate writes with explicit approvals."),
                    ("12", "Split broad connectors into narrow task-specific tools."),
                    ("13", "Use inspector tooling before production rollout of new MCP servers."),
                    ("14", "Attach user identity and request metadata to every tool call."),
                    ("15", "Track latency/error traces to catch retry storms early."),
                ],
            },
            {
                "tab": "07",
                "title": "Bucket 4: Skills (secrets 16-20)",
                "bullets": [
                    ("16", "Lead with precise `description` trigger phrases in SKILL.md frontmatter."),
                    ("17", "Keep top-level skill files concise; move deep detail to `references/`."),
                    ("18", "Bundle deterministic scripts for repetitive transformations and checks."),
                    ("19", "Include one good output and one counter-example to anchor quality."),
                    ("20", "Version skills in git with ownership and monthly quality review."),
                ],
            },
            {
                "tab": "08",
                "title": "Bucket 5: Context + /compact (secrets 21-25)",
                "bullets": [
                    ("21", "Compact at task boundaries, not randomly mid-constraint."),
                    ("22", "Use `/compact focus on <constraint>` to preserve critical intent."),
                    ("23", "Store stable rules in CLAUDE.md rather than conversational memory."),
                    ("24", "Avoid repeated compact cycles that degrade details over time."),
                    ("25", "After compact, immediately verify assumptions before executing writes."),
                ],
            },
            {
                "tab": "09",
                "title": "Buckets 6-8: Routing, Parallelism, Evals (secrets 26-40)",
                "bullets": [
                    ("26-30", "Route effort/model by risk profile; avoid default max-effort usage."),
                    ("31-35", "Split parallel work with worktrees and merge by risk order."),
                    ("36-40", "Use eval gates for task success, safety, and tool correctness before release."),
                ],
            },
            {
                "tab": "10",
                "title": "Bucket 9: GitHub reference repos (secrets 41-45)",
                "bullets": [
                    ("41", "modelcontextprotocol/servers - official MCP reference servers"),
                    ("42", "modelcontextprotocol/inspector - MCP debugging and validation tool"),
                    ("43", "anthropics/claude-code - Claude Code tooling and examples"),
                    ("44", "punkpeye/awesome-mcp-servers - curated MCP ecosystem directory"),
                    ("45", "promptfoo/promptfoo - prompt and agent eval automation"),
                ],
            },
            {
                "tab": "11",
                "title": "Bucket 10: Operating cadence (secrets 46-50)",
                "bullets": [
                    ("46", "Name an owner per workflow; orphaned agents decay quickly."),
                    ("47", "Review blocked hook events weekly and tune policies."),
                    ("48", "Promote only workflows below 15% intervention rate."),
                    ("49", "Log cost per successful run by workflow, not by model call."),
                    ("50", "Clone stable workflows as templates instead of reinventing prompts."),
                ],
            },
        ],
        "hidden_tricks": [
            "Use an Explore subagent to gather evidence, then a Reviewer subagent to challenge assumptions before code edits.",
            "Keep action-oriented tools in separate connectors so read workflows never request dangerous permissions.",
            "When /compact is frequent, persist invariant rules in CLAUDE.md and refresh them via hooks.",
            "Track intervention reasons as tags (scope, tool, policy, context) to prioritize fixes objectively.",
            "Use small deterministic scripts in hooks/skills for repeatable validations and low token usage.",
            "Treat every production incident as a new eval case within 48 hours.",
        ],
    }
}

BATCH50_01_FAQS = {
    "50_Series_Carousels/01_50_Claude_Agent_Secrets": [
        ("Do I need all 50 secrets at once?", "No. Deploy one bucket per week and measure intervention rate before expanding."),
        ("Which secret has fastest ROI?", "PreToolUse safety hook + one Explore subagent usually provides immediate gains."),
        ("When should I use /compact?", "At clear task boundaries or before switching contexts, with an explicit focus string."),
        ("How do I stop runaway costs?", "Route by risk, cap retries, monitor cost per success, and constrain tools."),
        ("What proves this is working?", "Lower intervention rate, faster cycle time, and fewer unsafe tool incidents."),
    ],
}

BATCH50_01_CASE_STUDIES = {
    "50_Series_Carousels/01_50_Claude_Agent_Secrets": (
        "A 14-person product team moved from ad-hoc Claude chats to a bucketed operator system: subagents for exploration, "
        "hooks for policy enforcement, one read-only MCP connector, and weekly eval gating. In five weeks they cut intervention "
        "rate from 29% to 11%, reduced average feature review rework by 37%, and eliminated two recurring secret-exposure near misses."
    ),
}

BATCH50_01_REFERENCE_APPENDIX = {
    "50_Series_Carousels/01_50_Claude_Agent_Secrets": {
        "title": "Reference appendix: first-week setup checklist",
        "body": [
            "Use this checklist to implement the first 10 secrets without over-scoping your rollout.",
        ],
        "bullets": [
            ("Day 1", "Create/update CLAUDE.md with commands, architecture, never-do rules."),
            ("Day 2", "Add a PreToolUse Bash hook to block dangerous command patterns."),
            ("Day 3", "Define one Explore subagent with read-only tool access."),
            ("Day 4", "Connect one read-only MCP server and validate via inspector."),
            ("Day 5", "Draft 15 eval cases from real incidents and edge workflows."),
            ("Day 6", "Run pilot on one workflow with explicit owner and output schema."),
            ("Day 7", "Review intervention tags and tune one bottleneck policy."),
        ],
    }
}

BATCH50_01_TROUBLESHOOTING = {
    "50_Series_Carousels/01_50_Claude_Agent_Secrets": {
        "title": "Troubleshooting common Claude agent failures",
        "body": [
            "Subagent overreach: tighten allowed tools and set maxTurns.",
            "Hooks not firing: validate JSON shape and event matcher regex in settings files.",
            "MCP tool confusion: split broad tools into explicit read/write actions with clearer descriptions.",
            "Compaction regressions: persist critical constraints in CLAUDE.md and use focused compaction.",
            "High intervention despite good prompts: inspect tool traces and output contracts before changing models.",
        ],
    }
}

BATCH50_01_MASTERY_PATH = {
    "50_Series_Carousels/01_50_Claude_Agent_Secrets": [
        "Week 1: safety hooks + one explore subagent + CLAUDE.md baseline.",
        "Week 2: one MCP connector (read-only) + output schema hardening.",
        "Week 3: eval gates and intervention tagging for real incidents.",
        "Week 4: model/effort routing and cost-per-success reporting.",
        "Week 5-6: parallel worktree workflow for independent tasks.",
        "Week 7+: clone proven workflow template into adjacent business functions.",
    ]
}

BATCH50_01_EXPERT_DEPTH = {
    "50_Series_Carousels/01_50_Claude_Agent_Secrets": {
        "title": "How senior Claude operators stay merge-ready",
        "body": [
            "They optimize for intervention rate and blast radius, not one-shot demo quality.",
            "They place strict policy in hooks and keep prompts focused on task intent.",
            "They version subagents and skills like product code with ownership.",
            "They keep connector surfaces narrow to improve tool-call correctness.",
            "They treat /compact as memory hygiene with explicit focus and post-checks.",
        ],
    }
}

BATCH50_01_CLOSING_NOTES = {
    "50_Series_Carousels/01_50_Claude_Agent_Secrets": [
        "These 50 secrets work best as an operating system, not isolated hacks.",
        "Implement one bucket per week and score outcomes with intervention rate.",
        "Keep writes gated until eval and policy checks are stable.",
        "Use GitHub references as starter kits, then tailor to your workflow constraints.",
        "Comment AI on the post for the full implementation pack and templates.",
        "Follow @piyush.glitch for operator-grade AI systems content.",
    ],
}
