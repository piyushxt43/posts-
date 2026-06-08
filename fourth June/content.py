# -*- coding: utf-8 -*-
"""Fourth June - Chase H AI style Claude Code Plugins carousel (8 slides)."""

BASE = """
4:5 vertical portrait ONLY (1080x1350). Premium Instagram carousel slide.
Perfect spelling, crisp readable typography, no watermarks, no slide numbers baked into art.
"""

CHASE_STYLE = BASE + """
STYLE REFERENCE: chase.h.ai Claude Code plugin carousel (terracotta paper texture background).
Match reference.md Visual DNA exactly.

Background: warm terracotta burnt-orange with subtle grain texture (#C45E3B feel).
Top header row small light text: JUN @2026  PIYUSH.GLITCH  [slide N / 08].
Black rounded pill tag white text for plugin labels.
Headline: huge bold lowercase sans-serif - some words white, emphasis words black.
Body: short white paragraph, key phrases in black bold.
Bottom: white GitHub-style repo card tilted slightly, translucent tape strips on top-left and bottom-right corners.
Card shows: blue repo path, bold repo name, grey description line, language dot + star count.
Footer: slide counter bottom-left, row of progress dots center, SWIPE -> bottom-right.
NOT cream grid, NOT beauty portrait - graphic editorial UI slide.
"""

LANDING = CHASE_STYLE + """
SLIDE TYPE: LANDING COVER ONLY (reference image 1 - David statue cover).
Light grey off-white textured background OR split terracotta left panel.
Huge headline: "Top 5" black + "Claude Code" gradient purple-to-orange + "Plugins" black + "for June" black.
Hero: classical marble bust (David-style) with pink-orange paint stroke across eyes - modern glitch art.
Floating 3D rounded app icons: GitHub black octocat icon, Claude orange sunburst icon.
NO plugin pill on this slide. Header: JUN @2026 PIYUSH.GLITCH 01 / 08.
Mood: scroll-stopping tech editorial, not photo of a person.
"""

PLUGIN_SLIDE = CHASE_STYLE + """
SLIDE TYPE: PLUGIN INFORMATION SLIDE (reference images 2-6).
Include black pill tag as specified in prompt.
Include taped GitHub repo card at bottom with exact repo path and stats from prompt.
Educational copy must be legible on mobile.
"""


def slide(filename, prompt):
    return (filename, prompt.strip())


def C(slug, pdf_name, caption, slides):
    return {"slug": slug, "pdf_name": pdf_name, "caption": caption, "slides": slides}


CAROUSELS = [
    C(
        "01_Top_5_Claude_Code_Plugins_June",
        "top-5-claude-code-plugins-june.pdf",
        """Comment PLUGINS and I'll send the full 12-page install guide  -  every repo, command, and config snippet from this carousel.

Most devs run Claude Code vanilla and bleed tokens on UI slop, stuck tasks, and zero memory.

Swipe for 5 plugins that actually ship:
1. Impeccable  -  kills 24 AI UI tells before merge
2. Caveman  -  cuts ~75% token noise, keeps accuracy
3. Codex  -  GPT-5 second opinion when Claude stalls
4. notebooklm-py  -  NotebookLM from terminal
5. Obsidian vault  -  local markdown memory (no plugin, just a folder)

Save this. Follow @piyush.glitch for operator-level Claude Code stacks.

#ClaudeCode #ClaudeAI #DevTools #AIagents #BuildInPublic""",
        [
            slide("01_cover.png", LANDING + """
Headline exactly: Top 5 Claude Code Plugins for June
Marble bust with pink paint stroke, GitHub + Claude floating icons.
01 / 08 in header. No pill tag.
"""),
            slide("02_impeccable.png", PLUGIN_SLIDE + """
Pill: PLUGIN 01 / IMPECCABLE
Headline white+black: impeccable kills the ai slop in your ui.
Body white: Audits frontend for 24 design tells - purple gradients, bounce easing, cramped padding - and fixes before ship. Bold black: 24 design tells.
Repo card: pbakaus / impeccable | Anti-AI-slop design skill | JavaScript dot | 1.2k stars
Header 02 / 08
"""),
            slide("03_caveman.png", PLUGIN_SLIDE + """
Pill: PLUGIN 02 / CAVEMAN
Headline: caveman mode cuts ~75% of your tokens.
Body: Drops articles, filler, pleasantries. Bold black: Full technical accuracy stays. Toggle lite / full / ultra.
Card: black polaroid with 3D grey rock object labeled caveman in white lowercase - taped to background
03 / 08
"""),
            slide("04_codex.png", PLUGIN_SLIDE + """
Pill: PLUGIN 03 / CODEX
Headline: codex hands stuck tasks to gpt-5.
Body: When Claude stalls, codex passes thread to GPT-5 for fresh diagnosis or second implementation - same runtime, no context lost. Bold: GPT-5, second implementation.
Repo card: openai / codex | Lightweight coding agent CLI bridge | Rust dot | 30.4k stars
04 / 08
"""),
            slide("05_notebooklm.png", PLUGIN_SLIDE + """
Pill: PLUGIN 04 / NOTEBOOKLM
Headline: notebooklm, driven by claude code.
Body: notebooklm-py gives Claude full NotebookLM access - spin notebooks, add sources, generate podcasts from terminal. Bold: right from the terminal.
Repo card: teng-lin / notebooklm-py | Programmatic NotebookLM | Python dot | 15.8k stars
05 / 08
"""),
            slide("06_obsidian.png", PLUGIN_SLIDE + """
Pill: BONUS / OBSIDIAN
Headline: obsidian becomes claude's memory.
Body: Point Claude Code at your Obsidian vault folder - notes become persistent searchable memory. Bold: Not a true plugin - just a folder.
Repo card: obsidianmd / obsidian | Local-first markdown vault memory | Markdown dot | local tag
06 / 08
"""),
            slide("07_install_stack.png", PLUGIN_SLIDE + """
Pill: SETUP / STACK
Headline white+black: install all five in one session.
Body white with black bold steps:
1. npx skills add impeccable
2. /caveman ultra in Claude Code
3. codex bridge in settings
4. pip install notebooklm-py
5. Point CLAUDE.md at Obsidian vault path
Large cream-white checklist card instead of GitHub card - five lines legible monospace
07 / 08
"""),
            slide("08_cta.png", CHASE_STYLE + """
Pill: GET THE PDF
Headline: comment plugins for the full guide.
Body: 12-page install PDF - every repo link, config block, and troubleshooting step from this carousel.
Terracotta background, large white CTA text, small recap list: Impeccable, Caveman, Codex, NotebookLM, Obsidian.
Optional taped white card: PIYUSH.GLITCH / top-5-claude-code-plugins-june.pdf
08 / 08 - last slide, no SWIPE arrow or say DONE
"""),
        ],
    ),
]

CAROUSEL_MAP = {"01": CAROUSELS[0]}
