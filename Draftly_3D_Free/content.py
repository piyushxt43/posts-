# -*- coding: utf-8 -*-
"""Draftly - 3-slide carousel: free 3D websites hook + how it works + prompts."""

from __future__ import annotations

BASE = """
4:5 vertical portrait ONLY (1080x1350). Premium Instagram carousel slide.
Crisp readable text, perfect spelling, no lorem ipsum, no watermarks, no slide numbers on image.
Footer bottom-left: draftly.space in small grey sans. NO progress dots. NO SWIPE arrow.
Top-right: DRAFTLY wordmark in bold Space Grotesk caps (text only, NO icon logo).
"""

SKY_HOOK = BASE + """
SLIDE TYPE: Cinematic overhead/flat-lay product hero - NO human figure at all.
Scene: sleek MacBook Pro open on a minimal white oak desk, the screen glowing with a beautiful
3D scroll website preview (abstract geometric scene, no readable text on screen), beside it
a ceramic espresso cup, a white architectural object, morning window light raking across the wood
from the left. Editorial Kinfolk / Awwwards magazine aesthetic. Soft warm-white background.
Top center tiny dark caps: DRAFTLY in charcoal. Upper-right frosted pill: 3D WEBSITE BUILDER.
Lower third dark text overlay (or white on gradient) as specified.
White pill CTA bottom center black uppercase text as specified.
"""

INTERIOR = BASE + """
SLIDE TYPE: Educational cream grid #F4EEDE - premium Draftly interior slide.
Top small caps: DRAFTLY. Huge bold black sans headline; ONE phrase coral #EF5E45 or italic serif.
2-4 cream cards thin border - render ALL specified text EXACTLY. Monospace for prompts/code.
Coral accent tabs and numbered steps. Strong whitespace. draftly.space footer.
Frame is 4:5 (taller than wide) - use the extra vertical space to spread cards out, no crowding.
"""

PROMPT_DENSE = BASE + """
SLIDE TYPE: Dense cream grid prompt slide - MUST show prompt fields FULLY READABLE.
Coral step pills. Multiple warm cards with monospace prompt text - legible at phone size.
Hand-drawn coral arrows between cards optional. DRAFTLY top-right. Fill the frame - no empty space.
Frame is 4:5 (taller than wide) - stack cards vertically using all the height.
"""


def slide(fn, p):
    return (fn, p.strip())


DATA = {
    "topic": "AI SaaS - Mindloop",
    "website_prompt": (
        "Build a cinematic AI productivity SaaS landing page for Mindloop. Floating centered "
        "nav pill with links Product, Pricing, Docs, Start Free. Hero headline "
        "'Think Faster. Ship Smarter.' with subcopy on AI workflows, team memory, and "
        "one-click automations for founders.\n\n"
        "Scroll sections: three feature cards (AI Memory, Workflow Builder, Team Sync), "
        "dashboard screenshot in browser chrome, integration row (Notion, Slack, Gmail), "
        "pricing toggle monthly/annual, testimonial strip, footer CTA Start Building Free.\n\n"
        "Clean white hero into soft gray product section. Scroll-synced hero motion from "
        "extracted video frames. Premium SaaS - not generic purple AI slop."
    ),
    "image_prompt": (
        "Cinematic photoreal SaaS hero still for scroll-scrubbed 3D website. No text, no logos, "
        "16:9 landscape for 400+ extracted frames.\n\n"
        "Scene: floating holographic UI panels above matte glass desk, soft morning window "
        "light, navy-to-cream gradient atmosphere, subtle particle bokeh, premium tech campaign.\n\n"
        "Camera: 40mm, slight low angle, shallow DOF, warm highlights on glass edges."
    ),
    "first_frame_prompt": (
        "Opening keyframe: wide desk tableau, holographic panels dim, lots of negative space "
        "left third for headline overlay, cool ambient light, same navy environment, 16:9, no text."
    ),
    "last_frame_prompt": (
        "Closing keyframe: panels elevated and glowing, camera 20% closer, warmer rim light, "
        "particle field denser, same environment, no text, photoreal."
    ),
    "video_prompt": (
        "Slow orbital dolly around floating UI panels. Subtle parallax, glass reflection shimmer, "
        "premium SaaS reveal pacing, seamless 8-second loop, no text overlays."
    ),
}


CAROUSELS = [
    {
        "slug": "01_3D_Websites_Free",
        "caption": """Make 3D websites for FREE on Draftly.

One prompt. AI still. 8s video. 400+ scroll frames. Production HTML.

No WebGL. No Three.js. Start from a preset OR build from scratch.

Swipe for exactly what to enter: website prompt, image prompt, first/last frame prompts, video prompt - then chat to change anything.

Comment DRAFTLY for the full prompt PDF.

draftly.space

#Draftly #3DWebsite #WebDesign #AIWebsite #NoCode #StartupTools #LandingPage""",
        "slides": [
            slide("01_cover.png", SKY_HOOK + """
Headline line 1 huge bold dark sans (charcoal on light desk): "Make 3D Websites"
Headline line 2 elegant italic serif charcoal: "For Free on Draftly"
Subline small grey: scroll-synced cinematic sites - no code required
White/light pill CTA black text: START BUILDING FREE
Frosted pill badge top-left: FREE TRIAL - 7 DAYS
Mood: editorial minimal desk hero - calm, premium, Awwwards aesthetic.
"""),
            slide("02_how_it_works.png", INTERIOR + """
Headline: how draftly works - preset or scratch
Subhead coral: two paths - one ship flow

Split layout TWO large cream cards side by side:

LEFT CARD - coral tab FROM SCRATCH
Path: draftly.space/3d-builder
Steps numbered 01-05:
01 Enter website prompt (full site brief)
02 Enter image prompt (hero still)
03 Enter first + last frame prompts (animation bookends)
04 Enter video prompt (8s motion)
05 Draftly extracts 400+ frames and builds scroll HTML

RIGHT CARD - coral tab FROM PRESET
Path: draftly.space/presets
Steps:
01 Pick from 47 production-ready 3D sites
02 Click Customize - edit copy and sections
03 Same image / frame / video prompts if you want custom motion
04 Chat to tweak layout, colors, copy
05 Publish to yourname.draftly.space or export ZIP

Bottom callout card coral border:
After generation - use CHAT to change anything. Add pages. Edit text. Swap media. Re-ship.

Footer stat row three mini pills:
NO WEBGL | 400+ FRAMES | ZIP EXPORT
"""),
            slide("03_prompts_and_chat.png", PROMPT_DENSE + """
Headline: what you enter - then chat to change
Subhead: copy this structure for mindloop saas example

FOUR stacked prompt cards - ALL TEXT MUST BE READABLE:

CARD 1 coral pill WEBSITE PROMPT
""" + DATA["website_prompt"][:520] + """

CARD 2 coral pill IMAGE PROMPT
""" + DATA["image_prompt"][:380] + """

CARD 3 coral pill FIRST FRAME + LAST FRAME (multi-image for animation continuity)
FIRST: """ + DATA["first_frame_prompt"][:200] + """
LAST: """ + DATA["last_frame_prompt"][:200] + """

CARD 4 coral pill VIDEO PROMPT
""" + DATA["video_prompt"][:220] + """

Bottom banner cream with coral left border:
AFTER SHIP: open chat - "make nav darker" "add pricing section" "swap hero copy" - Draftly applies changes without starting over.

White pill CTA center: DRAFTLY.SPACE - TRY FREE
"""),
        ],
    },
]

CAROUSEL_MAP = {"01": CAROUSELS[0]}
