# -*- coding: utf-8 -*-
"""Extended PDF blocks for 50-series carousel 03."""

BATCH50_03_EXTENDED = {
    "50_Series_Carousels/03_50_Hidden_Prompts_That_Ship": {
        "carousel_slides": [
            ("1", "50 Hidden Prompts That Ship in 2026", "Claude + GPT + Cursor operator stack."),
            ("2", "5 XML Tag Prompts", "Structure and boundary control."),
            ("3", "5 Format Contracts", "Reliable output schemas."),
            ("4", "5 Prefill Patterns", "Template speed and consistency."),
            ("5", "5 Non-Goal Blocks", "Prevent drift and risk."),
            ("6", "5 Inbox Operator Prompts", "Triage, replies, and escalation."),
            ("7", "5 Ops Operator Prompts", "KPI, incident, SOP, decisions."),
            ("8", "5 Content Operator Prompts", "Hooks, scripts, carousel mapping."),
            ("9", "5 Reasoning Control Prompts", "Confidence and alternatives."),
            ("10", "Comment AI", "Claim full 50 prompt pack."),
        ],
        "extra_sections": [
            {
                "tab": "04",
                "title": "XML prompts (10)",
                "body": [
                    "Use XML tags to separate context, goals, rules, and output. This reduces instruction collision and "
                    "improves contract adherence across models."
                ],
                "code": {
                    "caption": "XML #1 - role + task + constraints",
                    "lines": "<role>You are a revenue operations analyst.</role>\n<task>Summarize weekly pipeline risk and opportunity.</task>\n<constraints>\nUse only provided data.\nIf data is missing, write UNKNOWN.\nKeep summary under 120 words.\n</constraints>\n<output_contract>\nReturn: KPI table + 3 risks + 3 opportunities + one summary.\n</output_contract>",
                },
                "bullets": [
                    ("#2", "Context splitter with <context><input_data><goal>."),
                    ("#3", "Source-gated research with <sources><evidence_level>."),
                    ("#4", "Decision memo with <options><tradeoffs><recommendation>."),
                    ("#5", "Incident review with <timeline><root_cause><actions>."),
                    ("#6", "Customer support with <ticket><policy><response>."),
                    ("#7", "Product launch with <audience><message><cta>."),
                    ("#8", "PR review with <risk_map><test_gaps><ship_decision>."),
                    ("#9", "Sales prep with <account_data><objections><next_actions>."),
                    ("#10", "Content planner with <hooks><angles><calendar_output>."),
                ],
            },
            {
                "tab": "05",
                "title": "Format contracts (10)",
                "body": [
                    "Contracts remove ambiguity by forcing exact output structure. They are the biggest quality lever for "
                    "business workflows."
                ],
                "code": {
                    "caption": "Contract #1 - strict section return",
                    "lines": "Return EXACTLY these sections in order:\n1) KPI Snapshot table: Metric | Current | Prior | Delta | Confidence\n2) Risks (3 bullets, owner + mitigation)\n3) Opportunities (3 bullets, owner + next action)\n4) Summary (<=120 words)\nDo not add any extra section.",
                },
                "bullets": [
                    ("#2", "JSON schema contract with required keys only."),
                    ("#3", "Decision table contract: Option | Pros | Cons | Risk."),
                    ("#4", "Word cap contract by section."),
                    ("#5", "Citation contract requiring source and date."),
                    ("#6", "Checklist contract with pass/fail and reason."),
                    ("#7", "Draft + approval contract for outbound messages."),
                    ("#8", "Unknown-value contract to prevent hallucinated fields."),
                    ("#9", "Priority-ranked output contract with scoring formula."),
                    ("#10", "One-line executive summary contract."),
                ],
            },
            {
                "tab": "06",
                "title": "Prefill patterns (10)",
                "body": [
                    "Prefill variables turn good prompts into reusable templates across teams, clients, and campaigns."
                ],
                "code": {
                    "caption": "Prefill #1 - account strategy template",
                    "lines": "Account: {{account_name}}\nSegment: {{segment}}\nDecision owner: {{decision_owner}}\nGoal: {{goal}}\nRisk level: {{risk_level}}\nDeadline: {{deadline}}\nForbidden claims: {{forbidden_claims}}",
                },
                "bullets": [
                    ("#2", "Audience + channel + CTA prompt prefill."),
                    ("#3", "Brand voice + banned words prefill."),
                    ("#4", "Tool access + data sources prefill."),
                    ("#5", "Meeting type + outcome template."),
                    ("#6", "Incident severity + response policy prefill."),
                    ("#7", "Launch stage + conversion goal prefill."),
                    ("#8", "Developer task + done criteria prefill."),
                    ("#9", "Research question + confidence threshold prefill."),
                    ("#10", "Approval path + escalation prefill."),
                ],
            },
            {
                "tab": "07",
                "title": "Non-goals and reasoning controls (10 + 10)",
                "body": [
                    "Non-goals stop drift. Reasoning controls improve reliability without needing magic wording."
                ],
                "code": {
                    "caption": "Reasoning control pattern",
                    "lines": "Before final answer:\n1) List assumptions.\n2) Mark confidence per claim (High/Med/Low).\n3) Provide two alternatives + tradeoff.\n4) State unknowns and required data.\n5) Run quality check against output contract.",
                },
                "bullets": [
                    ("Non-goal #1", "No invented percentages or metrics."),
                    ("Non-goal #2", "No legal/financial claims without source."),
                    ("Non-goal #3", "No irreversible actions without approval."),
                    ("Non-goal #4", "No motivational filler language."),
                    ("Non-goal #5", "No scope beyond requested deliverable."),
                    ("Reasoning #1", "Assumptions first, answer second."),
                    ("Reasoning #2", "Confidence labels per claim."),
                    ("Reasoning #3", "Alternatives + tradeoff matrix."),
                    ("Reasoning #4", "Unknowns declared explicitly."),
                    ("Reasoning #5", "Self-check before final output."),
                ],
            },
            {
                "tab": "08",
                "title": "Operator prompt packs: inbox, ops, content (30)",
                "body": [
                    "The final 30 prompts are grouped by practical business function so teams can deploy fast."
                ],
                "bullets": [
                    ("Inbox 1-10", "Priority triage, reply drafting, escalation routing, follow-up sequencing, thread summaries."),
                    ("Ops 11-20", "KPI digest, incident timeline, runbook gaps, weekly blockers, decision logs."),
                    ("Content 21-30", "Hook generation, carousel map, script beats, angle testing, repurpose workflows."),
                    ("Deployment tip", "Assign one owner per prompt category and track accepted-output rate weekly."),
                    ("Governance tip", "Store all templates in one shared prompt library with changelog."),
                ],
            },
        ],
        "hidden_tricks": [
            "Put XML blocks in the same order across all templates for compliance consistency.",
            "When output drifts, tighten contract and non-goals before rewriting whole prompt.",
            "Use UNKNOWN rule to prevent fake precision under pressure.",
            "Capture failed outputs and turn them into counter-examples in templates.",
            "Track accepted-output rate by prompt ID, not by workflow only.",
            "Keep one lightweight prompt style guide so teams do not fork formats.",
            "Run monthly mini-evals after major model updates.",
        ],
    },
}

BATCH50_03_FAQS = {
    "50_Series_Carousels/03_50_Hidden_Prompts_That_Ship": [
        ("Do these prompts work in Claude, GPT, and Cursor?", "Yes. The structure is model-agnostic and contract-focused."),
        ("Why XML tags instead of plain text?", "Tags create cleaner section boundaries and better compliance."),
        ("What if my data is incomplete?", "Use UNKNOWN rule to avoid hallucinated values."),
        ("How many prompts should I launch first?", "Start with 5 in one workflow before scaling."),
        ("Where do non-goals help most?", "Anywhere outputs drift or become risky."),
        ("How do I keep team consistency?", "Use shared templates with prefill variables and changelog."),
    ],
}

BATCH50_03_CASE_STUDIES = {
    "50_Series_Carousels/03_50_Hidden_Prompts_That_Ship": (
        "A 14-person SaaS growth team replaced ad-hoc prompting with contract-driven templates across inbox triage, "
        "weekly KPI summaries, and social content production. In 4 weeks, accepted-output rate rose from 58% to 87%, "
        "manual rewrite time fell by 41%, and stakeholder trust increased because outputs were consistently structured."
    ),
}

BATCH50_03_REFERENCE_APPENDIX = {
    "50_Series_Carousels/03_50_Hidden_Prompts_That_Ship": {
        "title": "Reference: ship-ready prompt checklist",
        "body": ["Use this checklist before adding a prompt to production workflows."],
        "bullets": [
            ("Context block", "Clear role, audience, goal, and data scope."),
            ("Rules block", "Always/never constraints explicitly listed."),
            ("Contract block", "Exact output schema with required sections."),
            ("Prefill block", "Reusable variables for context injection."),
            ("Non-goals block", "Hard limits to prevent drift and unsafe output."),
            ("Quality checks", "Self-check criteria before final response."),
        ],
        "code": {
            "caption": "Template naming convention",
            "lines": "inbox-01-priority-triage.md\nops-04-incident-timeline.md\ncontent-07-hook-stack.md\nreasoning-03-alternative-matrix.md\ncontract-02-json-schema.md",
        },
    },
}

BATCH50_03_TROUBLESHOOTING = {
    "50_Series_Carousels/03_50_Hidden_Prompts_That_Ship": {
        "title": "Troubleshooting hidden prompt systems",
        "body": [
            "If output is generic, tighten the format contract and add one concrete example.",
            "If model invents facts, add UNKNOWN rule and require source citations.",
            "If responses are too long, set strict word caps per section.",
            "If team outputs diverge, enforce one shared template library with IDs.",
            "If prompt quality decays after model updates, run mini-evals and patch contracts.",
        ],
    },
}

BATCH50_03_MASTERY_PATH = {
    "50_Series_Carousels/03_50_Hidden_Prompts_That_Ship": [
        "Week 1: deploy 5 prompt contracts in one workflow.",
        "Week 2: add non-goals and quality checks from failures.",
        "Week 3: expand to inbox + ops categories (20 prompts).",
        "Week 4: add content + reasoning controls (35 prompts).",
        "Month 2: complete 50 prompts and publish team playbook.",
        "Month 3: run monthly quality review and retire weak templates.",
    ],
}

BATCH50_03_EXPERT_DEPTH = {
    "50_Series_Carousels/03_50_Hidden_Prompts_That_Ship": {
        "title": "How expert operators run prompt libraries",
        "body": [
            "They treat prompts like APIs: versioned, testable, and owned.",
            "They optimize accepted-output rate, not prompt creativity.",
            "They standardize XML block order across all business workflows.",
            "They review failed outputs weekly and patch templates quickly.",
            "They keep non-goals short, enforceable, and risk-focused.",
        ],
    },
}

BATCH50_03_CLOSING_NOTES = {
    "50_Series_Carousels/03_50_Hidden_Prompts_That_Ship": [
        "Prompt quality compounds when templates become shared team assets.",
        "Start with 5 contract-driven prompts this week and track accepted-output rate.",
        "Use XML, format contracts, prefill, and non-goals as your default stack.",
        "Expand to 50 only after one workflow proves stable and measurable.",
        "Comment AI on the post to get the full hidden prompt pack and updates.",
        "Follow @piyush.glitch for more operator-grade AI systems.",
    ],
}
