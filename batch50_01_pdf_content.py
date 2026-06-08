# -*- coding: utf-8 -*-
"""Base PDF content for batch50 carousel 01."""

BATCH50_01_CONTENT = {
    "50_Series_Carousels/01_50_Claude_Agent_Secrets": {
        "title": "50 Claude Agent Secrets (That Actually Ship)",
        "subtitle": "Real Claude Code operator patterns for subagents, MCP, hooks, /compact, effort routing, and hidden workflows.",
        "kicker": "AI FOR BUSINESS - 50/01",
        "pdf_filename": "50-claude-agent-secrets.pdf",
        "intro": (
            "Most Claude tutorials stop at prompt phrasing. Teams that ship production work with Claude Code use a "
            "different stack: scoped subagents, deterministic hooks, MCP connectors with strict permissions, compact "
            "discipline for long sessions, and model+effort routing based on risk. This guide distills 50 practical "
            "secrets with real repositories, implementation patterns, and workflow guardrails."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "Why these 50 secrets matter",
                "body": [
                    "Claude Code is no longer just a coding chat. It is an agent runtime with delegation, tools, and policy hooks. "
                    "Without operator patterns, teams get context blowups, unsafe tool calls, and expensive rework.",
                    "The 50 secrets here are grouped into ten operator domains so you can implement in sequence instead of adopting "
                    "everything at once."
                ],
                "bullets": [
                    ("Reality", "Most failures are workflow design failures, not base-model IQ issues."),
                    ("Leverage", "A single hook or skill often removes repeated human correction."),
                    ("Outcome", "Target lower intervention rate and faster time-to-ship, not prettier prompts."),
                ],
            },
            {
                "tab": "02",
                "title": "10-bucket map for the 50 secrets",
                "body": [
                    "Each bucket contains 5 secrets. Implement one bucket per week for a practical 10-week rollout."
                ],
                "bullets": [
                    ("1", "Subagent architecture and delegation"),
                    ("2", "Hook lifecycle and policy enforcement"),
                    ("3", "MCP connector design and governance"),
                    ("4", "Skills and reusable SOP packaging"),
                    ("5", "Context and /compact discipline"),
                    ("6", "Model + effort routing strategy"),
                    ("7", "Parallel execution and worktree flows"),
                    ("8", "Evaluation gates and reliability metrics"),
                    ("9", "GitHub reference stack and implementation repos"),
                    ("10", "Leadership rollout and operating cadence"),
                ],
            },
            {
                "tab": "03",
                "title": "Starter implementation sequence",
                "body": [
                    "Do not install all patterns in one sprint. Start with safety and visibility, then layer delegation and scale.",
                ],
                "bullets": [
                    ("Step 1", "Write/update CLAUDE.md with commands, architecture, and never-do list."),
                    ("Step 2", "Add one PreToolUse hook to block dangerous shell actions and secrets."),
                    ("Step 3", "Create one Explore subagent (read-only) and one Reviewer subagent."),
                    ("Step 4", "Connect one read-only MCP server and log all tool calls."),
                    ("Step 5", "Add 15 golden eval cases before enabling high-impact write actions."),
                ],
            },
        ],
        "playbook": [
            "Pick one recurring workflow and define success in one sentence.",
            "Run read-only first with explicit output schema and ownership.",
            "Add deterministic hooks for safety and formatting.",
            "Route heavy tasks to stronger effort/model only when risk justifies it.",
            "Track intervention rate, eval pass rate, and cost per successful run weekly.",
            "Scale by cloning proven workflow templates, not by improvising new ones.",
        ],
        "mistakes": [
            "Using one general-purpose agent for every task and tool.",
            "Skipping hooks and relying on prompt reminders for policy.",
            "Granting write permissions before read-only reliability is proven.",
            "Compacting blindly without preserving critical focus constraints.",
            "Choosing models by hype instead of risk/volume routing metrics.",
        ],
        "glossary": [
            ("Subagent", "An isolated Claude worker with scoped instructions, tools, and optional model override."),
            ("Hook", "Lifecycle script that can block, validate, or post-process tool calls."),
            ("MCP", "Model Context Protocol: standard interface between agents and external tools/data."),
            ("Intervention Rate", "Percentage of runs requiring human correction before completion."),
            ("Cost per Success", "Total workflow cost divided by successfully completed outcomes."),
        ],
        "callout": {
            "title": "Operator principle",
            "text": "Treat Claude like an operating system: strict boundaries, reusable workflows, measurable reliability. "
                    "That is how experimental chat turns into production infrastructure.",
        },
    }
}
