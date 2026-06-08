# -*- coding: utf-8 -*-
"""Base PDF content for 50-series carousel 03."""

BATCH50_03_CONTENT = {
    "50_Series_Carousels/03_50_Hidden_Prompts_That_Ship": {
        "title": "50 Hidden Prompts That Ship",
        "subtitle": "Operator-grade prompt contracts for Claude, GPT, and Cursor.",
        "kicker": "AI FOR BUSINESS - 50 SERIES - 03",
        "pdf_filename": "50-hidden-prompts-that-ship.pdf",
        "intro": (
            "Most business teams still use AI with generic prompts and vague requests, then wonder why output quality "
            "is inconsistent. Shipping operators in 2026 use a different stack: XML structure, strict format contracts, "
            "prefill variables, reasoning controls, and explicit non-goals. This guide gives you 50 hidden prompts "
            "across inbox, operations, and content workflows, with copy-paste patterns you can deploy immediately."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "Why hidden prompts outperform generic prompts",
                "body": [
                    "Generic prompts are easy to start but expensive to scale. Teams burn time on retries, extra edits, "
                    "and manual cleanup. Hidden prompts are really operating contracts: they reduce ambiguity and force "
                    "the model to produce decision-ready output from the first pass.",
                ],
                "bullets": [
                    ("Precision", "Structured prompts reduce drift and force required fields."),
                    ("Speed", "Less back-and-forth means faster execution cycles."),
                    ("Reliability", "Contracts make outputs reusable across people and teams."),
                    ("Governance", "Non-goals and risk constraints prevent costly mistakes."),
                ],
            },
            {
                "tab": "02",
                "title": "The five-block stack serious operators use",
                "body": [
                    "Most of the 50 prompts in this guide are built from the same five building blocks: XML tags for "
                    "context boundaries, strict output contract, prefill variables, non-goals, and quality checks. "
                    "The stack is portable across Claude, GPT, and Cursor.",
                ],
                "bullets": [
                    ("XML tags", "Clear boundaries for context, rules, and output sections."),
                    ("Format contract", "Exact sections, tables, or JSON schema required."),
                    ("Prefill", "Reusable template variables for speed and consistency."),
                    ("Non-goals", "What output must avoid, explicitly stated."),
                    ("Quality checks", "Self-validation before final answer."),
                ],
            },
            {
                "tab": "03",
                "title": "Deploy strategy: from 5 prompts to 50",
                "body": [
                    "Do not roll out all 50 prompts at once. Start with one workflow, prove accepted-output gains, "
                    "track intervention rate, then expand by category. Prompt systems scale best when treated like "
                    "production assets with owners and versioning.",
                ],
                "bullets": [
                    ("Week 1", "Launch 5 prompts in one high-friction workflow."),
                    ("Week 2", "Refine format contracts from real failures."),
                    ("Week 3", "Expand to 20 prompts across two categories."),
                    ("Week 4+", "Scale to full 50 with governance checklist."),
                ],
            },
        ],
        "playbook": [
            "Pick one workflow where AI output is currently inconsistent.",
            "Apply the five-block prompt stack to your top 5 recurring tasks.",
            "Track accepted-output rate and intervention rate weekly.",
            "Store prompts as templates with {{variables}} and ownership.",
            "Expand to 50 only after one workflow is stable for 2-4 weeks.",
        ],
        "mistakes": [
            "Using long clever prompts without clear section contracts.",
            "Skipping non-goals and then fighting scope drift.",
            "Letting teams copy random prompts without version control.",
            "Optimizing for 'looks smart' instead of accepted output quality.",
            "Rolling out 50 prompts before proving 5 prompts in production.",
        ],
        "glossary": [
            ("Format contract", "Strict output schema the model must follow."),
            ("Prefill variables", "Template placeholders like {{audience}} or {{deadline}}."),
            ("Non-goals", "Explicitly forbidden output patterns or actions."),
            ("Intervention rate", "How often humans must correct model output."),
            ("Accepted-output rate", "Outputs approved without major rework."),
        ],
        "callout": {
            "title": "Operator rule",
            "text": "If the output matters to revenue, risk, or customer trust, treat prompts as production contracts, "
                    "not chat messages.",
        },
    },
}
