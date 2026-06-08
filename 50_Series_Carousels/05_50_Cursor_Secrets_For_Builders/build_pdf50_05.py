#!/usr/bin/env python3
"""Build 10+ page PDF for 50 Cursor secrets carousel."""

from __future__ import annotations

from pathlib import Path

from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parent
OUT_PDF = ROOT / "50-cursor-secrets-for-builders.pdf"

CREAM = HexColor("#F4EEDE")
GRID = HexColor("#E6DEC7")
CARD = HexColor("#FCFAF3")
INK = HexColor("#1B1A17")
MUTED = HexColor("#6E6657")
CORAL = HexColor("#EF5E45")
LINE = HexColor("#D8CFB8")
GREEN = HexColor("#2E7D5B")

PAGE_W, PAGE_H = letter
MARGIN = 0.72 * inch
CONTENT_W = PAGE_W - 2 * MARGIN

STY_H1 = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=28, leading=32, textColor=INK)
STY_H2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=16, leading=20, textColor=INK, spaceAfter=6)
STY_EYE = ParagraphStyle("eye", fontName="Helvetica-Bold", fontSize=10.5, leading=13, textColor=CORAL, spaceAfter=6)
STY_BODY = ParagraphStyle("body", fontName="Helvetica", fontSize=10.5, leading=15.5, textColor=INK, spaceAfter=6)
STY_CODE = ParagraphStyle("code", fontName="Courier", fontSize=8.6, leading=11.3, textColor=INK)
STY_FOOT = ParagraphStyle("foot", fontName="Helvetica", fontSize=8.5, leading=11, textColor=MUTED)

INTRO = (
    "Cursor in 2026 is no longer 'AI autocomplete.' Teams using it well run an operator stack: Composer 2.5 for "
    "daily execution, Plan Mode for architecture decisions, scoped .cursor/rules for consistency, hooks for "
    "deterministic safety, skills for repeatable workflows, worktrees for safe parallelism, and cloud agents for "
    "long-running implementation. This guide gives 50 practical secrets for developers and business builders."
)

SLIDES_RECAP = [
    ("Slide 1", "50 Cursor tricks. You're using 8.", "The hook and stack overview."),
    ("Slide 2", "Secrets 1-5: Composer 2.5", "Model and cost operating logic."),
    ("Slide 3", "Secrets 6-10: Agents Window", "Parallel workflow supervision."),
    ("Slide 4", "Secrets 11-15: Plan Mode", "Anti-rework planning pattern."),
    ("Slide 5", "Secrets 16-20: .cursor/rules", "Scoped .mdc rule architecture."),
    ("Slide 6", "Secrets 21-30: Hooks + Guardrails", "Deterministic enforcement loops."),
    ("Slide 7", "Secrets 31-35: Skills", "Reusable SOP packs for teams."),
    ("Slide 8", "Secrets 36-40: /worktree", "Isolated parallel implementation."),
    ("Slide 9", "Secrets 41-50: Cloud Agents", "Local-cloud handoff operating model."),
    ("Slide 10", "Comment AI", "Get full 50-secret workbook."),
]

SECRETS = {
    "Composer 2.5 (1-5)": [
        "Default to Composer 2.5 fast for most tasks; escalate only for high-risk decisions.",
        "Start prompts with outcome + constraints; early tokens bias execution quality.",
        "Request 'risk list first' before edits to reduce optimistic implementation.",
        "Use model escalation only when ambiguity/risk justifies token cost.",
        "Track rework rate per model tier, not only speed.",
    ],
    "Agents Window (6-10)": [
        "Use Agents Window as mission control for parallel local/cloud sessions.",
        "Assign one objective per agent to avoid context bleed.",
        "Use new diff review before staging; never auto-merge parallel work.",
        "Move stalled sessions to cloud when runtime exceeds your focus window.",
        "Close or archive stale sessions to keep context hygiene high.",
    ],
    "Plan Mode (11-15)": [
        "Shift+Tab into Plan Mode for multi-file or architectural work.",
        "Require unknowns and assumptions before implementation starts.",
        "Reject plans with no rollback path for risky edits.",
        "Break work into independently testable phases.",
        "Convert approved plan bullets into checklist execution.",
    ],
    ".cursor/rules/*.mdc (16-20)": [
        "Split by concern: API, tests, security, naming.",
        "Use globs narrowly so only relevant files pull each rule.",
        "Keep always-on rules short; move depth to referenced docs.",
        "Add concrete examples and explicit NEVER constraints.",
        "Version rule changes with review like production code.",
    ],
    "Hooks + guardrails (21-30)": [
        "Use pre-action hooks to block dangerous shell patterns.",
        "Use post-edit hooks for fast deterministic hygiene (lint/format/tests).",
        "Return explicit block reasons so agents self-correct quickly.",
        "Add bounded retry loops for auto-fix flows.",
        "Separate security hooks from style hooks.",
        "Log blocked events for policy tuning.",
        "Use hooks for guarantees, not general guidance.",
        "Keep hook scripts fast to avoid workflow drag.",
        "Guard against secret exposure in commit and command layers.",
        "Treat hook config as governance infrastructure.",
    ],
    "Skills (31-35)": [
        "Encode repeatable workflows as SKILL.md packs.",
        "Keep skill descriptions specific with trigger phrases.",
        "Add counter-examples to prevent recurring bad output.",
        "Pair skills with rules + hooks for routing and enforcement.",
        "Review skill usage monthly and retire low-ROI packs.",
    ],
    "/worktree parallelism (36-40)": [
        "Use /worktree before parallel implementation.",
        "Run one task per worktree; avoid shared hotspot files.",
        "Define merge order before running parallel agents.",
        "Apply smallest-risk diff first to reduce conflicts.",
        "Use /best-of-n when comparing model approaches safely.",
    ],
    "Cloud agents + handoff (41-50)": [
        "Start cloud agents for long tasks you cannot babysit.",
        "Use cloud for heavy refactors and overnight loops.",
        "Pull cloud runs local for final verification and testing.",
        "Keep environment assumptions in repo config, not memory.",
        "Treat cloud demos/screenshots as verification inputs, not truth.",
        "Track cloud run interventions as quality signal.",
        "Use local-cloud-local baton passing for efficiency.",
        "Run security review before merging cloud-produced diffs.",
        "Use cloud sessions across repos for orchestration.",
        "Document your known-good handoff template for onboarding.",
    ],
}

RULES_SNIPPET = """---
description: API and service conventions
globs:
  - "apps/api/**/*.ts"
  - "services/**/*.ts"
alwaysApply: false
---
- Validate external payloads with zod schemas
- Return typed error envelopes; no raw stack traces
- NEVER log tokens, secrets, or full request bodies
- Include test command in PR notes: `pnpm test:api`
"""

HOOKS_JSON_SNIPPET = """{
  "beforeBash": [
    { "command": "node .cursor/hooks/secret_guard.js" },
    { "command": "node .cursor/hooks/block_dangerous_git.js" }
  ],
  "afterEdit": [
    { "command": "pnpm lint --fix" },
    { "command": "pnpm test -- --runInBand --bail=1" }
  ]
}"""

HOOK_SCRIPT_SNIPPET = """#!/usr/bin/env node
// .cursor/hooks/secret_guard.js
const cmd = process.env.CURSOR_BASH_COMMAND || "";
const deny = [/api[_-]?key/i, /token\\s*=/i, /password\\s*=/i];
if (deny.some((rx) => rx.test(cmd))) {
  console.error("Blocked: possible secret in command.");
  process.exit(2);
}
process.exit(0);
"""

SKILL_SNIPPET = """---
name: pr-risk-review
description: Review PR diff for regressions, risky edits, and missing tests.
---
## Inputs
- Git diff
- Related ticket
- Test output

## Steps
1. List top 5 behavioral risks first.
2. Map blast radius by module.
3. Flag missing tests and rollback gaps.
4. Return ship/no-ship recommendation.
"""


def paint_background(canvas):
    canvas.saveState()
    canvas.setFillColor(CREAM)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    canvas.setStrokeColor(GRID)
    canvas.setLineWidth(0.5)
    step = 22
    x = 0
    while x <= PAGE_W:
        canvas.line(x, 0, x, PAGE_H)
        x += step
    y = 0
    while y <= PAGE_H:
        canvas.line(0, y, PAGE_W, y)
        y += step
    canvas.restoreState()


def draw_footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.8)
    canvas.line(MARGIN, 0.55 * inch, PAGE_W - MARGIN, 0.55 * inch)
    canvas.setFont("Helvetica-Bold", 8.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(MARGIN, 0.4 * inch, "@piyush.glitch")
    canvas.setFont("Helvetica", 8.5)
    canvas.drawRightString(PAGE_W - MARGIN, 0.4 * inch, "Comment AI for full 50-secret workbook")
    canvas.drawCentredString(PAGE_W / 2, 0.4 * inch, str(doc.page))
    canvas.restoreState()


def on_page(canvas, doc):
    paint_background(canvas)
    draw_footer(canvas, doc)


def section_header(title: str) -> Table:
    t = Table([[Paragraph(title.upper(), STY_H2)]], colWidths=[CONTENT_W])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), CARD),
                ("LEFTPADDING", (0, 0), (-1, -1), 12),
                ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("LINEABOVE", (0, 0), (-1, 0), 2, CORAL),
                ("BOX", (0, 0), (-1, -1), 0.8, LINE),
            ]
        )
    )
    return t


def bullets(items: list[str], numbered: bool = True, accent: str = "#EF5E45") -> Table:
    rows = []
    for i, text in enumerate(items, start=1):
        lead = f"<font color='{accent}'><b>{i}.</b></font>" if numbered else f"<font color='{accent}'><b>&#9632;</b></font>"
        rows.append([Paragraph(f"{lead} {text}", STY_BODY)])
    t = Table(rows, colWidths=[CONTENT_W])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), CARD),
                ("LEFTPADDING", (0, 0), (-1, -1), 12),
                ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("BOX", (0, 0), (-1, -1), 0.8, LINE),
            ]
        )
    )
    return t


def code_block(title: str, code: str) -> list:
    rows = [[Paragraph(f"<b>{title}</b>", STY_BODY)]]
    for line in code.splitlines():
        safe = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        rows.append([Paragraph(safe if safe else " ", STY_CODE)])
    t = Table(rows, colWidths=[CONTENT_W])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), HexColor("#ECE7DB")),
                ("LEFTPADDING", (0, 0), (-1, -1), 12),
                ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ("BOX", (0, 0), (-1, -1), 0.8, LINE),
            ]
        )
    )
    return [t, Spacer(1, 10)]


def build() -> int:
    doc = BaseDocTemplate(
        str(OUT_PDF),
        pagesize=letter,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=0.75 * inch,
        title="50 Cursor Secrets For Builders",
        author="@piyush.glitch",
    )
    frame = Frame(MARGIN, 0.75 * inch, CONTENT_W, PAGE_H - MARGIN - 0.75 * inch, id="main")
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=on_page)])

    story = []
    story.append(NextPageTemplate("main"))
    story.append(Paragraph("50 Cursor Secrets<br/>For Builders", STY_H1))
    story.append(Spacer(1, 8))
    story.append(Paragraph("10-slide carousel companion (2026 edition)", STY_EYE))
    story.append(Paragraph(INTRO, STY_BODY))
    story.append(Spacer(1, 10))

    recap_rows = [[Paragraph(f"<b>{s}</b> - {t} - {d}", STY_BODY)] for s, t, d in SLIDES_RECAP]
    recap = Table(recap_rows, colWidths=[CONTENT_W])
    recap.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), CARD),
                ("LEFTPADDING", (0, 0), (-1, -1), 12),
                ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ("BOX", (0, 0), (-1, -1), 0.8, LINE),
            ]
        )
    )
    story.append(recap)
    story.append(PageBreak())

    story.append(Paragraph("THE 50 SECRETS", STY_EYE))
    for idx, (group, items) in enumerate(SECRETS.items(), start=1):
        story.append(section_header(f"{idx}. {group}"))
        story.append(Spacer(1, 6))
        story.append(bullets(items, numbered=True, accent="#EF5E45"))
        story.append(Spacer(1, 12))
        if idx < len(SECRETS):
            story.append(PageBreak())

    story.append(PageBreak())
    story.append(Paragraph("RULES + HOOKS CODE SNIPPETS", STY_EYE))
    story.append(Paragraph("These are practical starter templates you can copy into real repos.", STY_BODY))
    story.append(Spacer(1, 8))
    story.extend(code_block(".cursor/rules/api-conventions.mdc", RULES_SNIPPET))
    story.extend(code_block(".cursor/hooks.json", HOOKS_JSON_SNIPPET))
    story.extend(code_block(".cursor/hooks/secret_guard.js", HOOK_SCRIPT_SNIPPET))
    story.extend(code_block(".cursor/skills/pr-risk-review/SKILL.md", SKILL_SNIPPET))

    story.append(PageBreak())
    story.append(Paragraph("ROLL-OUT PLAYBOOK (30 DAYS)", STY_EYE))
    playbook = [
        "Week 1: set default model policy (Composer 2.5 fast + escalation rubric).",
        "Week 1: enforce 2-3 scoped .mdc rules for API/testing/security.",
        "Week 2: add pre-action secret guard and post-edit lint/test hooks.",
        "Week 2: package two high-frequency workflows into skills.",
        "Week 3: ship first parallel /worktree implementation cycle.",
        "Week 3: define merge-order protocol and risk-first review checklist.",
        "Week 4: run one long cloud-agent task with local final verification.",
        "Week 4: instrument intervention rate, rework rate, and lead time.",
    ]
    story.append(bullets(playbook, numbered=True, accent="#2E7D5B"))
    story.append(Spacer(1, 10))

    mistakes = [
        "Parallelizing before defining ownership and merge order.",
        "Adding broad always-on rules that flood context.",
        "Using hooks for vague advice instead of deterministic checks.",
        "Letting cloud-run output merge without local verification.",
        "No metrics, so workflow quality appears random.",
    ]
    story.append(section_header("Mistakes that kill adoption"))
    story.append(Spacer(1, 6))
    story.append(bullets(mistakes, numbered=False, accent="#EF5E45"))
    story.append(Spacer(1, 14))

    story.append(Paragraph("Comment AI to get the editable templates bundle.", STY_H2))
    story.append(Paragraph("#Cursor #CursorAI #Composer2 #AIAgents #BuildInPublic", STY_FOOT))

    doc.build(story)
    return 0


if __name__ == "__main__":
    raise SystemExit(build())
