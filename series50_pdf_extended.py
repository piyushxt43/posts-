# -*- coding: utf-8 -*-
"""Extended PDF blocks for 50 Series carousel 02."""

SERIES50_EXTENDED = {
    "50_Series_Carousels/02_50_Claude_Skills_Nobody_Set_Up": {
        "carousel_slides": [
            ("1", "50 Claude skills exist. You set up zero.", "Hook + urgency for business operators."),
            ("2", "SKILL.md anatomy", "Frontmatter and body contract."),
            ("3", "Progressive disclosure", "Lean context loading pattern."),
            ("4", "Invocation flags", "Control auto vs manual trigger behavior."),
            ("5", "Skill 1: PR Security Sentinel", "Risk-first code review workflow."),
            ("6", "Skill 2: Incident Timeline Builder", "Postmortem assembly from evidence."),
            ("7", "Skill 3: GTM Message Calibrator", "Persona-safe messaging transformation."),
            ("8", "Skill 4: Eval Gatekeeper", "Regression and safety blocking workflow."),
            ("9", "Skill 5: Prompt Regression Tracker", "Weekly drift monitoring routine."),
            ("10", "Comment AI", "CTA for copy-paste skill pack."),
        ],
        "extra_sections": [
            {
                "tab": "04",
                "title": "Invocation controls from Anthropic docs (2026)",
                "body": [
                    "Anthropic's 2026 skills documentation describes two key controls: disable-model-invocation and "
                    "user-invocable. Use these as a policy matrix, not random toggles.",
                    "Rule of thumb: read-only analysis skills can allow model invocation; side-effect skills should be "
                    "explicitly user-triggered and audit-friendly."
                ],
                "code": {
                    "caption": "Frontmatter policy pattern",
                    "lines": "---\nname: deploy-prod\ndescription: Deploy production services with preflight checks.\ndisable-model-invocation: true\nuser-invocable: true\nallowed-tools: Bash, Read\ndisallowed-tools: Write\n---",
                },
                "pro_tip": {
                    "title": "Policy split",
                    "text": "Maintain separate folders for analysis skills and action skills so invocation defaults cannot drift silently.",
                },
            },
            {
                "tab": "05",
                "title": "7 copy-paste skills you can deploy this week",
                "body": [
                    "Each skill below is scoped to a repeatable business outcome and includes explicit output contracts."
                ],
                "bullets": [
                    ("1) PR Security Sentinel", "Risk-first pull request review with exploit paths, blast radius, and test gaps."),
                    ("2) Incident Timeline Builder", "Correlates logs, deploys, and tickets into minute-level incident narrative."),
                    ("3) Migration Choreographer", "Designs expand-contract migration with rollback and validation checkpoints."),
                    ("4) GTM Message Calibrator", "Adapts messaging by persona with forbidden claims and proof requirements."),
                    ("5) Eval Gatekeeper", "Runs golden scenarios and blocks releases on task or safety regressions."),
                    ("6) Prompt Regression Tracker", "Schedules weekly golden prompt pass/fail tracking and drift summaries."),
                    ("7) Skill Drift Auditor", "Flags stale trigger phrases, broken examples, and missing verification sections."),
                ],
            },
            {
                "tab": "06",
                "title": "Real example: PR Security Sentinel",
                "body": [
                    "This skill is one of the fastest ROI wins for engineering-heavy teams because it enforces review order: "
                    "security and risk first, style last."
                ],
                "code": {
                    "caption": ".claude/skills/pr-security-sentinel/SKILL.md",
                    "lines": "---\nname: pr-security-sentinel\ndescription: Review pull request diffs for exploitable risks, unsafe defaults, auth gaps, and missing security tests.\nallowed-tools: Read, Grep, Glob\ndisallowed-tools: Bash\n---\n## Inputs\nGit diff, linked issue, architecture notes\n## Steps\n1. List top risks\n2. Map blast radius\n3. Identify test gaps\n4. Recommend ship/no-ship\n## Output\n## Risks\n## Test Gaps\n## Recommendation",
                },
            },
            {
                "tab": "07",
                "title": "Real example: Eval Gatekeeper",
                "body": [
                    "When skills interact with releases, they need deterministic gates. This pattern checks golden scenarios "
                    "before merges and blocks if safety or task quality degrades."
                ],
                "code": {
                    "caption": "Eval gate output contract",
                    "lines": "## Eval Summary\n- Total cases: <n>\n- Task pass rate: <pct>\n- Safety pass rate: <pct>\n- Tool correctness: <pct>\n## Failing cases\n- <case id>: <reason>\n## Decision\nBLOCK or PASS with rationale",
                },
            },
            {
                "tab": "08",
                "title": "Real example: GTM Message Calibrator",
                "body": [
                    "This skill protects message quality and compliance by forcing persona-specific output and proof constraints."
                ],
                "code": {
                    "caption": "GTM calibrator skeleton",
                    "lines": "---\nname: gtm-message-calibrator\ndescription: Rewrite launch messaging by persona while enforcing forbidden-claims list.\n---\n## Inputs\nCurrent draft, target persona, forbidden claims list\n## Steps\n1. Extract core claim\n2. Rewrite for persona pains\n3. Remove unsupported claims\n4. Return final + risk notes",
                },
            },
            {
                "tab": "09",
                "title": "Anthropic docs examples (2026)",
                "body": [
                    "These examples are derived from Anthropic's Claude Code skills docs in 2026, including the official "
                    "skills guide and frontmatter behavior matrix for invocation controls.",
                    "Use these as implementation anchors for your own policy defaults and onboarding docs."
                ],
                "bullets": [
                    ("Skills guide", "code.claude.com/docs/en/skills - authoritative field definitions and invocation behavior."),
                    ("Markdown source", "code.claude.com/docs/en/skills.md - same guidance in raw docs format."),
                    ("Manual-only workflow example", "disable-model-invocation: true for explicit user-triggered side-effect skills."),
                    ("Background knowledge example", "user-invocable: false for helper skills users should not call directly."),
                ],
                "code": {
                    "caption": "Doc-aligned frontmatter matrix (simplified)",
                    "lines": "default: user invoke yes | model invoke yes\ndisable-model-invocation: true -> user invoke yes | model invoke no\nuser-invocable: false -> user invoke no | model invoke yes",
                },
            },
            {
                "tab": "10",
                "title": "Rollout roadmap for business teams",
                "body": [
                    "Week 1: deploy PR Security Sentinel, Incident Timeline Builder, and GTM Message Calibrator.",
                    "Week 2: add Eval Gatekeeper and Prompt Regression Tracker with golden prompts.",
                    "Week 3: add Skill Drift Auditor and Migration Choreographer; review invocation policies.",
                    "Week 4: publish usage/intervention scorecard and retire underperforming skills."
                ],
            },
        ],
        "hidden_tricks": [
            "Write description fields as routing statements, not marketing copy.",
            "Counter-examples reduce repeated failure patterns faster than extra instructions.",
            "Keep deterministic transforms in scripts/ to save context and reduce variance.",
            "Version every skill edit with behavior-change notes in PR description.",
            "Run monthly trigger-phrase audits to reduce accidental invocation overlap.",
            "Track intervention rate per skill; kill anything that stays noisy.",
            "Use one shared template for output contracts across the whole library.",
        ],
    }
}

SERIES50_FAQS = {
    "50_Series_Carousels/02_50_Claude_Skills_Nobody_Set_Up": [
        ("Do I need all 50 skills now?", "No. Start with 3-7 high-impact skills and expand after stability."),
        ("What should I ship first?", "PR Security Sentinel and Incident Timeline Builder usually show immediate ROI."),
        ("How long should SKILL.md be?", "Keep core instructions concise; move depth to references/."),
        ("How do I prevent drift?", "Use golden prompts weekly and compare output contract compliance."),
        ("How do we avoid skill chaos?", "Assign owners, add version history, and retire low-usage skills quarterly."),
    ],
}

SERIES50_CASE_STUDIES = {
    "50_Series_Carousels/02_50_Claude_Skills_Nobody_Set_Up": (
        "A 17-person product + ops team deployed seven skills in four weeks using this exact staged rollout. Their PR review "
        "cycle time dropped 28%, post-incident writeups moved from ad hoc to same-day delivery, and message rewrites required "
        "fewer legal revisions because forbidden-claim checks were built into the skill contract."
    ),
}

SERIES50_REFERENCE_APPENDIX = {
    "50_Series_Carousels/02_50_Claude_Skills_Nobody_Set_Up": {
        "title": "Reference: skill launch checklist",
        "body": ["Use this checklist for every new skill before team rollout."],
        "bullets": [
            ("Description quality", "Clear trigger phrase + explicit use case."),
            ("Input contract", "Required artifacts listed and validated."),
            ("Output contract", "Fixed headings/schema with pass criteria."),
            ("Risk policy", "Invocation and tool permissions reviewed."),
            ("Golden tests", "At least 3 fixed prompts with expected shape."),
            ("Owner", "Named maintainer and changelog entry."),
        ],
        "code": {
            "caption": "PR checklist snippet",
            "lines": "- [ ] Trigger phrase updated\n- [ ] Invocation flags reviewed\n- [ ] Tool policy least privilege\n- [ ] Golden prompts pass\n- [ ] Owner approved",
        },
    },
}

SERIES50_TROUBLESHOOTING = {
    "50_Series_Carousels/02_50_Claude_Skills_Nobody_Set_Up": {
        "title": "Troubleshooting skill rollout issues",
        "body": [
            "Skill triggers too often: narrow description and reduce overlapping phrases with sibling skills.",
            "Quality drops after update: compare against golden prompts and restore missing constraints.",
            "Context cost rises: move long examples into references/ and keep core skill compact.",
            "Unsafe actions appear: split analysis and action skills with stricter invocation defaults.",
            "Low adoption: publish simple slash-invocation playbook for each team workflow.",
        ],
    },
}

SERIES50_MASTERY_PATH = {
    "50_Series_Carousels/02_50_Claude_Skills_Nobody_Set_Up": [
        "Week 1: deploy 3 skills and baseline intervention rate.",
        "Week 2: add eval and regression skills with golden prompts.",
        "Week 3: add drift audit and migration skills; review ownership.",
        "Week 4: publish scorecard and prune low-value skills.",
        "Month 2: expand to 12-15 skills with strict policy templates.",
        "Month 3: quarterly audit for triggers, costs, and ROI.",
    ],
}

SERIES50_EXPERT_DEPTH = {
    "50_Series_Carousels/02_50_Claude_Skills_Nobody_Set_Up": {
        "title": "What advanced teams do differently",
        "body": [
            "They optimize trigger precision before adding more skill count.",
            "They separate analysis and action paths at directory and policy level.",
            "They run a fixed regression set after any skill or model change.",
            "They measure ROI per skill and archive dead workflows quickly.",
            "They treat skill libraries like product assets with ownership and release notes.",
        ],
    },
}

SERIES50_CLOSING_NOTES = {
    "50_Series_Carousels/02_50_Claude_Skills_Nobody_Set_Up": [
        "If a workflow repeats weekly, it should become a skill.",
        "Start with seven copy-paste skills, then tune with golden prompts.",
        "Use progressive disclosure to keep context lean and outputs consistent.",
        "Treat invocation flags as governance controls, not optional metadata.",
        "Comment AI for the full skill pack and rollout templates.",
        "Follow @piyush.glitch for operator-grade Claude workflows.",
    ],
}

from batch50_03_pdf_extended import (
    BATCH50_03_CASE_STUDIES,
    BATCH50_03_CLOSING_NOTES,
    BATCH50_03_EXPERT_DEPTH,
    BATCH50_03_EXTENDED,
    BATCH50_03_FAQS,
    BATCH50_03_MASTERY_PATH,
    BATCH50_03_REFERENCE_APPENDIX,
    BATCH50_03_TROUBLESHOOTING,
)

SERIES50_EXTENDED.update(BATCH50_03_EXTENDED)
SERIES50_FAQS.update(BATCH50_03_FAQS)
SERIES50_CASE_STUDIES.update(BATCH50_03_CASE_STUDIES)
SERIES50_REFERENCE_APPENDIX.update(BATCH50_03_REFERENCE_APPENDIX)
SERIES50_TROUBLESHOOTING.update(BATCH50_03_TROUBLESHOOTING)
SERIES50_MASTERY_PATH.update(BATCH50_03_MASTERY_PATH)
SERIES50_EXPERT_DEPTH.update(BATCH50_03_EXPERT_DEPTH)
SERIES50_CLOSING_NOTES.update(BATCH50_03_CLOSING_NOTES)
