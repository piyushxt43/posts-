# -*- coding: utf-8 -*-
"""7th June - 2 Gemini Pro FREE carousels (8-slide deep + 3-slide short)."""

BASE = """
3:4 vertical portrait ONLY (1080x1440). Premium Instagram carousel slide.
Crisp readable text, perfect spelling, no lorem ipsum, no watermarks, no slide numbers on image.
Footer bottom-left: @piyush.glitch in small grey sans. NO progress dots. NO SWIPE arrow.
"""

GEMINI_WHITE = BASE + """
SLIDE TYPE: Google Gemini promo style - clean WHITE background.
Soft pastel blob accents in corners only: light mint green top-right, light sky blue top-left, soft pink bottom-right.
Scattered small four-pointed Gemini stars with blue-yellow-green-red gradient (official Gemini sparkle colors).
Top center small caps: PIYUSH.GLITCH. Professional clean sans-serif typography like Google marketing.
Use OFFICIAL Google Gemini four-pointed star logo (multicolor gradient) where specified - accurate recognizable shape.
NO dark backgrounds. Bright airy tech promo aesthetic matching placement.guide reference carousels.
"""

GEMINI_GRID = BASE + """
SLIDE TYPE: White background Gemini feature grid slide - 2x3 or 2x2 cream-white cards with rounded corners,
subtle drop shadow, small colored subtitle per card (blue green red purple). Official Gemini star logo top center.
Color-coded feature titles. @piyush.glitch footer. Clean Google One marketing layout.
"""

GEMINI_CTA = BASE + """
SLIDE TYPE: White Gemini finale - pastel blobs, gradient stars, profile circle bottom-left placeholder.
Headline Comment FREE for Details. Gradient pill button blue-to-coral 'Claim offer' style.
PIYUSH.GLITCH top center. @piyush.glitch footer.
"""


def slide(fn, p):
    return (fn, p.strip())


def C(slug, pdf, cap, slides):
    return {"slug": slug, "pdf_name": pdf, "caption": cap, "slides": slides}


CAROUSELS = [
    C(
        "01_Gemini_Pro_FREE_Full_Guide",
        "gemini-pro-free-full-guide.pdf",
        """Google Gemini Pro worth Rs 35,100 - FREE for 18 months.

NotebookLM. Veo 3.1. Flow. 5TB Google One. Gemini in Gmail, Docs, Vids.

Swipe for everything included in Google AI Pro and how to claim it.

Comment FREE and I'll send the complete activation guide PDF.

Follow @piyush.glitch

#GoogleGemini #GeminiPro #GoogleOne #NotebookLM #FreeAI #PIYUSHGLITCH""",
        [
            slide("01_cover.png", GEMINI_WHITE + """
Large official Google Gemini multicolor four-pointed star logo centered top.
Headline black bold sans: "Pro plan of Google Gemini"
Second line: "Rs 35,100" with strikethrough + "FREE" in bold red #E53935
Third line bold black: "for 18 months"
Small text: Comment 'FREE' for Details
Gradient pill button bottom: CLAIM OFFER (blue left to coral right).
Pastel corner blobs and scattered gradient stars.
"""),
            slide("02_everything_included.png", GEMINI_GRID + """
Headline: "Google Gemini" bold + subhead "Everything you need to create, research and do more with AI"
Words create (blue) research (green) do more (red) color-coded.
2x3 grid cards EXACT text:
1 NotebookLM | Advanced Research | Research assistant with 5X higher limits
2 Google Gemini | Access to Gemini 3.1 Pro | Most capable model + Deep Research
3 Google Workspace | AI in Gmail Docs Vids | Gemini inside your work apps
4 Google One | 5 TB Storage | Photos emails docs never run out
5 Nano Banana | AI Image Editing | Latest AI image update - one photo countless creations
6 Veo 3.1 | AI Video Tool | Describe your idea - watch it come to life
"""),
            slide("03_gemini_app.png", GEMINI_WHITE + """
Card layout on white. Pill: GEMINI APP. Headline: gemini 3.1 pro + deep research.
Body bullets readable:
- 1 million token context window (~1500 pages)
- Deep Research multi-source reports
- Gemini 3.1 Pro highest reasoning tier on Pro plan
- Higher daily limits vs free tier
Small official Gemini logo top-right.
"""),
            slide("04_notebooklm.png", GEMINI_WHITE + """
Pill blue: NOTEBOOKLM. Headline: study and research smarter.
Stats cards:
500 notebooks | 300 sources per notebook | 500 chats/day
20 audio overviews per day | 20 video overviews per day
100 reports flashcards quizzes per day
Body: Upload PDFs URLs docs - get cited answers podcasts and study guides.
"""),
            slide("05_workspace.png", GEMINI_WHITE + """
Pill green: GOOGLE WORKSPACE. Headline: gemini inside gmail docs vids and more.
Grid icons row: Gmail | Docs | Sheets | Slides | Drive | Meet
Bullets:
- AI Overviews in Gmail - answers without opening every email
- Write and edit in Docs with Gemini side panel
- Google Vids - AI video creation for work
- Deep Search in Google Search with Gemini 3 Pro
"""),
            slide("06_flow_veo_creative.png", GEMINI_WHITE + """
Pill purple: CREATIVE AI. Headline: flow veo 3.1 nano banana.
Three cards:
FLOW - 1000 AI credits/month for video workflows
VEO 3.1 - AI video generator from text prompt
NANO BANANA - AI image editing one photo to countless variants
WHISK - image generation in Gemini app
Body: Create images music and video inside Gemini and Search.
"""),
            slide("07_google_one.png", GEMINI_WHITE + """
Pill red: GOOGLE ONE AI PRO. Headline: 5 tb storage + pro extras.
Table readable:
Storage: 5 TB (up from 2 TB April 2026)
AI Credits: 1000/month for Flow creative tools
Google Home Premium Standard included
Gemini in Chrome auto-browse
Developer: Gemini CLI + Code Assist access
Price anchor: ~Rs 1,950/mo value - FREE 18 months promo
"""),
            slide("08_cta.png", GEMINI_CTA + """
Headline: "comment" black sans + "FREE" red highlight box + "for the complete guide pdf"
Sub: Rs 35,100 Gemini Pro - 18 months - activation steps inside PDF
White pill: COMMENT FREE FOR THE PDF
Recap tiny: Gemini NotebookLM Workspace Veo Flow 5TB
"""),
        ],
    ),
    C(
        "02_Gemini_Pro_FREE_3_Slides",
        "gemini-pro-free-3-slides.pdf",
        """Rs 35,100 Google Gemini Pro. FREE. 18 months.

Comment FREE for the activation guide.

@piyush.glitch

#GeminiPro #GoogleAI #Free""",
        [
            slide("01_cover.png", GEMINI_WHITE + """
MUST include large accurate OFFICIAL Google Gemini four-pointed star logo (blue green yellow red gradient) centered.
Small Google G logo watermark subtle top-left optional.
Headline: "Pro plan of Google Gemini"
"Rs 35,100" strikethrough + "FREE" bold red
"for 18 months" bold black
Comment 'FREE' for Details below headline
Gradient CLAIM OFFER button blue to orange-red
Pastel blobs corners. Maximum visual match to placement.guide reference slide 1.
"""),
            slide("02_major_highlights.png", GEMINI_GRID + """
Official Gemini logo top. Headline: 3 reasons this is insane value
Three large cards only (not six):
CARD 1 - Rs 35,100 FREE | 18 months Google AI Pro - no payment
CARD 2 - 5 TB Google One + Gemini 3.1 Pro + NotebookLM expanded
CARD 3 - Veo 3.1 video + Flow + Workspace AI in Gmail Docs Vids
Bottom line: India student and creator promo - claim before offer ends
"""),
            slide("03_cta.png", GEMINI_CTA + """
Official Gemini multicolor star logo above headline.
Headline: Comment FREE for Details
Body: Full PDF with step-by-step claim link checklist and what's included
Gradient pill: GET THE FREE GUIDE
@piyush.glitch prominent
"""),
        ],
    ),
]

CAROUSEL_MAP = {f"{i:02d}": CAROUSELS[i - 1] for i in range(1, len(CAROUSELS) + 1)}
