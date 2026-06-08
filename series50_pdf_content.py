# -*- coding: utf-8 -*-
"""Base PDF content for 50 Series carousel batch."""

SERIES50_CONTENT = {
    "50_Series_Carousels/02_50_Claude_Skills_Nobody_Set_Up": {
        "title": "50 Claude Skills Nobody Set Up",
        "subtitle": "SKILL.md anatomy, invocation controls, and 7 copy-paste workflows for 2026 operators.",
        "kicker": "AI FOR BUSINESS - 50 SERIES 02",
        "pdf_filename": "50-claude-skills-nobody-set-up.pdf",
        "intro": (
            "Most teams discovered Claude Skills but never operationalized them. They keep re-prompting the same workflows, "
            "bleeding context, and blaming models for process problems. In 2026, operators using Claude at scale treat "
            "skills like production assets: concise SKILL.md contracts, progressive disclosure, strict invocation policy, "
            "golden examples, and weekly drift checks. This guide gives a practical, non-generic implementation map."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "Why most skill libraries fail",
                "body": [
                    "Teams write one giant SKILL.md full of vague advice, then wonder why outputs drift. The issue is not the "
                    "model. It is missing workflow contracts, mixed risk levels, and no ownership policy.",
                    "A production skill library keeps each skill tightly scoped to one repeatable workflow, with explicit "
                    "inputs, ordered steps, constraints, and output contract. The goal is consistency, not creativity."
                ],
                "bullets": [
                    ("Smell 1", "Description field is generic, so trigger routing is noisy."),
                    ("Smell 2", "Side-effect skills auto-invoke without explicit approval patterns."),
                    ("Smell 3", "No golden examples, so quality bar resets every run."),
                    ("Smell 4", "No owner/changelog, so behavior changes silently."),
                ],
            },
            {
                "tab": "02",
                "title": "SKILL.md anatomy that actually works",
                "body": [
                    "A strong skill is short but strict. Frontmatter communicates routing and invocation policy. Body sections "
                    "define procedural behavior and output shape. References and scripts carry depth without bloating base context."
                ],
                "bullets": [
                    ("Frontmatter", "name, description, invocation controls, and tool policy."),
                    ("Purpose", "What outcome this skill must produce and for whom."),
                    ("Inputs", "Artifacts required before execution starts."),
                    ("Steps", "Ordered method, not optional suggestions."),
                    ("Output", "Exact headings/schema expected every run."),
                    ("Never", "Hard constraints to prevent recurring failures."),
                ],
            },
            {
                "tab": "03",
                "title": "Progressive disclosure in practice",
                "body": [
                    "Anthropic's skills docs emphasize progressive loading behavior: metadata first, skill body on invocation, "
                    "and referenced resources only when needed. This is the easiest way to cut context burn without losing quality.",
                    "In business workflows this matters because teams stack many skills. Keeping each skill lean prevents accidental "
                    "token inflation and reduces cross-skill interference."
                ],
                "bullets": [
                    ("Layer 1", "Description should be explicit enough to route correctly."),
                    ("Layer 2", "Core steps in SKILL.md should stay compact and procedural."),
                    ("Layer 3", "Heavy examples/checklists live in references/."),
                    ("Layer 4", "Deterministic transforms belong in scripts/."),
                ],
            },
        ],
        "playbook": [
            "Install 3 read-only analysis skills first and baseline output quality.",
            "Add one side-effect skill with explicit invocation and review policy.",
            "Create 5 golden prompts per skill and store expected output shape.",
            "Run a weekly drift audit against golden prompts after model or prompt updates.",
            "Track usage count and intervention rate per skill; retire low-value skills.",
            "Version the skill library in git with owners and review gates.",
        ],
        "mistakes": [
            "Using one generic skill for unrelated workflows.",
            "Making descriptions catchy instead of operationally precise.",
            "Allowing risky skills to auto-trigger with broad tool access.",
            "Keeping examples only in chat history instead of skill files.",
            "Never running regression checks after model updates.",
        ],
        "glossary": [
            ("Skill", "Reusable workflow contract packaged in a SKILL.md directory."),
            ("Progressive Disclosure", "Load only the context required at each step."),
            ("Golden Prompt", "Fixed test input used to detect behavior drift."),
            ("Invocation Policy", "Rules controlling who or what can trigger a skill."),
            ("Skill Drift", "Behavior quality change caused by edits or model updates."),
        ],
        "callout": {
            "title": "Operator takeaway",
            "text": "Treat skill descriptions as routing infrastructure, not documentation. Trigger precision drives quality and cost more than any stylistic rewrite.",
        },
    },
}

from batch50_03_pdf_content import BATCH50_03_CONTENT

SERIES50_CONTENT.update(BATCH50_03_CONTENT)
