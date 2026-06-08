# -*- coding: utf-8 -*-
"""Cover-only prompts v2 - AI Business Carousels style, unique per deck."""

from __future__ import annotations

BASE = """
3:4 vertical portrait ONLY (1080x1440). Premium @piyush.glitch AI Business Carousels cover style.
Match generate_carousels.py posts 01-15: luxury tech editorial, huge confident typography,
clean spacing, Figma-like polish. Readable sharp correctly spelled text only.

TYPOGRAPHY RULES (critical):
- Headlines in bold BLACK sans-serif (#1B1A17) on cream OR white on blue-sky photo only.
- One key phrase in elegant italic serif OR inside coral highlight box #EF5E45.
- Coral brush underline on the hook word. Never use low-contrast white text on terracotta.
- Subheads in dark grey #4A4540, not faint white.

FOOTER RULES (critical - user rejected old style):
- ONLY small "@piyush.glitch" bottom-left in grey.
- NO progress dots. NO SWIPE arrow. NO slide counter. NO 01/08. NO pagination.

TOP ROW: micro label left "PIYUSH.GLITCH", center coral pill with category tag, optional brand logo right.
No watermarks, no lorem ipsum, no Instagram UI chrome.
"""

COVERS = [
    {
        "slug": "01_Claude_Small_Business_Cowork",
        "filename": "01_Landing_Cover.png",
        "prompt": BASE + """
COVER TYPE A: blue-sky editorial portrait (like AI_Business_Carousels post 02).
Close crop professional woman at modern desk, bright daylight, lens flare, shallow depth of field.
Headline EXACT black-on-white text box upper-left:
Line 1: "Claude for" bold black
Line 2: "Small Business" with "Business" in coral #EF5E45 highlight box
Line 3: "Cowork" bold black with rough hand-underline stroke
Subhead dark grey: "connectors + 15 ready workflows"
RIGHT SIDE: large 3D Claude terracotta app icon card (accurate sparkle logo) + small QuickBooks and HubSpot icon chips.
Bottom-left footer ONLY: @piyush.glitch. No dots, no swipe, no page numbers.
Mood: founder ops energy, not marble bust template.
""",
    },
    {
        "slug": "02_Skills_MCP_Two_Layer_Stack",
        "filename": "01_Landing_Cover.png",
        "prompt": BASE + """
COVER TYPE B: cream grid paper #F4EEDE (like post 04 MCP USB-C cover).
Center: clean 3D split object - left half glossy USB-C plug sculpture, right half open playbook book - on subtle shadow.
Headline EXACT stacked black sans:
"Skills +" black | "MCP" inside coral rounded pill | "two-layer stack" black
Italic serif word "playbook" in subhead line.
Small diagram arrow: USB -> Playbook in thin black line art.
Top pill: AI FOR BUSINESS - STACK
Tiny MCP plug icon + SKILL.md file icon floating. Claude logo badge top-right.
Footer ONLY @piyush.glitch bottom-left. No swipe, no dots.
""",
    },
    {
        "slug": "03_Agent_Skills_Write_Once",
        "filename": "01_Landing_Cover.png",
        "prompt": BASE + """
COVER TYPE B+: cream grid with surreal floating archive (like hook cover 27).
Glowing stack of SKILL.md folders in warm library light, hand reaching for top folder.
Headline EXACT black:
"Agent Skills:" black | "write once" with coral brush underline | "run everywhere" black
Subhead: "one SKILL.md - Claude, Cursor, Codex, Gemini CLI"
Row of four small accurate tool logos beneath headline (not identical sizes - varied layout).
Faded oversized lowercase "skills" watermark behind headline at 8% opacity.
Top pill: AI FOR BUSINESS - SKILLS. Footer ONLY @piyush.glitch. No dots, no swipe.
""",
    },
    {
        "slug": "04_Cursor_Cloud_Agents",
        "filename": "01_Landing_Cover.png",
        "prompt": BASE + """
COVER TYPE C: surreal editorial photoreal (like hook covers).
Developer silhouette watching floating laptop with green "Merge PR" badge and cloud VM wireframe.
Headline EXACT:
"Cursor" black | "Cloud Agents" in violet-to-blue gradient text still readable on cream mist overlay | "open PRs" coral box
Large Cursor cube logo card RIGHT (35% frame height) - accurate black/white cube mark.
Slack + Linear small icons as floating chips, not a row of identical busts.
Top: PIYUSH.GLITCH | pill DEV TOOLS - CLOUD
Footer ONLY @piyush.glitch. No pagination UI.
""",
    },
    {
        "slug": "05_OpenAI_Workspace_Agents",
        "filename": "01_Landing_Cover.png",
        "prompt": BASE + """
COVER TYPE A variant: soft office window light, team standup blur background.
Headline on cream card overlay:
"OpenAI" black | "Workspace Agents" with italic serif "Workspace" | "for teams" coral underline
Center: one shared agent card orbited by 4 team avatar circles (sales ops support eng labels).
ChatGPT swirl logo on agent card - accurate. Salesforce + Slack connector chips.
Top pill: AI FOR BUSINESS - AGENTS
Footer ONLY @piyush.glitch bottom-left. No swipe dots page counter.
""",
    },
    {
        "slug": "06_Google_Workspace_Studio_Gems",
        "filename": "01_Landing_Cover.png",
        "prompt": BASE + """
COVER TYPE B: cream grid automation diagram cover.
Horizontal flow diagram in clean black line art: Gmail icon -> Gem diamond -> Sheets icon -> checkmark.
Headline EXACT black sans:
"Google" black | "Workspace Studio" with each word in subtle Google-color thin borders not rainbow fill | "+ Gems" coral box
Subhead dark grey: "Ask a Gem inside the flow - not just chat"
3D Gmail envelope prop lower-right with soft shadow. Small Gem sparkle icon.
Top pill: AI FOR BUSINESS - STUDIO
Footer ONLY @piyush.glitch. No dots no swipe.
""",
    },
    {
        "slug": "07_Meta_UGC_Creative_OS",
        "filename": "01_Landing_Cover.png",
        "prompt": BASE + """
COVER TYPE D: split layout - left 55% cream grid, right 45% photo collage.
LEFT: black headline "Meta" | "UGC Creative" Meta-blue accent bar behind Creative only | "Operating System" black
Hook timer badge "0:03" in coral circle. Bullet trio in black: variant volume, hook bible, refresh cadence.
RIGHT: 2x3 grid of vertical phone ad frames (generic blurred faces), Reels UI hints.
Instagram + Reels icons small. Top pill: UGC OPS - META
Footer ONLY @piyush.glitch on cream side. No swipe dots.
Not beauty portrait close-up.
""",
    },
    {
        "slug": "08_MCP_Servers_By_Job",
        "filename": "01_Landing_Cover.png",
        "prompt": BASE + """
COVER TYPE B: cream grid with toolbox still-life (unique from bust template).
Open wooden toolbox containing labeled 3D cubes: GSC green, GA4 orange, GitHub black, HubSpot orange, n8n red - each different size angle.
Headline EXACT:
"MCP servers" black | "by job" coral highlight box | "not a list" black italic serif
Crossed-out giant numbered list on left (faded) vs toolbox on right - visual contrast.
Top pill: AI FOR BUSINESS - MCP
Footer ONLY @piyush.glitch. No pagination.
""",
    },
    {
        "slug": "09_Router_Worker_Reviewer",
        "filename": "01_Landing_Cover.png",
        "prompt": BASE + """
COVER TYPE E: three-column role board on cream grid (not three marble busts).
Three tall UI cards left to right:
Card 1 ROUTER (checklist icon, black header, coral top stripe)
Card 2 WORKER (wrench icon, black header, white body)
Card 3 REVIEWER (shield icon, black header, gold accent)
Arrows between cards in thin black lines.
Headline above cards stacked huge black: "Router" / "Worker" / "Reviewer" - only Reviewer gets gold italic serif.
Subhead: "multi-agent pattern for business"
Top pill: AI FOR BUSINESS - WORKFLOW
Footer ONLY @piyush.glitch. No swipe no dots.
""",
    },
    {
        "slug": "10_Agent_Governance_SAFE",
        "filename": "01_Landing_Cover.png",
        "prompt": BASE + """
COVER TYPE A: blue-sky editorial + trust motif (like post 01 energy).
Close crop hands pausing over laptop keyboard, red APPROVE stamp floating as 3D object not overlay on bust.
Headline on white semi-transparent card:
"Human-in-the-loop" black | "governance" slate-blue italic serif | "before send" coral underline
Three small icons row: lock shield, audit scroll, email with X - line art black.
Top pill: AI FOR BUSINESS - SAFE
Claude logo small top-right. Footer ONLY @piyush.glitch bottom-left.
No progress dots, no SWIPE, no terracotta full-bleed background.
""",
    },
]
