# -*- coding: utf-8 -*-
"""Dense PDFs for Gemini Pro FREE lead magnets."""

from __future__ import annotations

from pathlib import Path

from content import CAROUSELS
from pdf_builder_rich import build_pdf

ROOT = Path(__file__).resolve().parent


def full_guide_pages() -> list:
    return [
        [
            {"type": "heading", "text": "Google Gemini Pro FREE - Complete Guide"},
            {"type": "subhead", "text": "Rs 35,100 value  |  18 months  |  @piyush.glitch"},
            {"type": "prose", "text": (
                "Comment <b>FREE</b> on the carousel for this PDF. Google AI Pro (formerly AI Premium) "
                "bundles Gemini 3.1 Pro, NotebookLM, Workspace AI, Flow, Veo, and 5 TB Google One storage. "
                "Promotional offers vary by region and eligibility - verify on one.google.com before claiming."
            )},
            {"type": "callout", "title": "What you get", "text": (
                "Gemini app (1M context) + NotebookLM expanded + Gmail/Docs/Vids AI + "
                "5 TB storage + 1000 Flow credits/month + Veo 3.1 video + image tools."
            )},
        ],
        [
            {"type": "heading", "text": "Gemini App - Gemini 3.1 Pro"},
            {"type": "table", "headers": ["Feature", "Pro plan"], "rows": [
                ["Model", "Gemini 3.1 Pro + Deep Research"],
                ["Context", "1 million tokens (~1500 pages)"],
                ["Deep Research", "Up to 20 reports/day"],
                ["Search", "Gemini 3 Pro in Google Search + Deep Search"],
                ["Chrome", "Auto-browse and expanded limits"],
            ]},
            {"type": "prose", "text": (
                "Use for: long document analysis, multi-step research, coding with Gemini CLI and Code Assist (Pro tier)."
            )},
        ],
        [
            {"type": "heading", "text": "NotebookLM (expanded Pro access)"},
            {"type": "table", "headers": ["Limit", "Google AI Pro"], "rows": [
                ["Notebooks", "500"],
                ["Sources per notebook", "300"],
                ["Chats per day", "500"],
                ["Audio overviews/day", "20"],
                ["Video overviews/day", "20"],
                ["Reports / quizzes / day", "100"],
            ]},
            {"type": "prose", "text": (
                "Upload PDFs, URLs, Google Docs. Get cited answers, Audio Overviews, Video Overviews, and study guides. "
                "5X higher limits vs basic NotebookLM."
            )},
        ],
        [
            {"type": "heading", "text": "Google Workspace AI"},
            {"type": "bullets", "items": [
                "Gmail: AI Overviews - instant answers from inbox context",
                "Docs: Write, summarize, rewrite with Gemini side panel",
                "Sheets: Formula help and data analysis",
                "Slides: Generate decks from prompts",
                "Google Vids: AI-assisted workplace video creation",
                "Meet: Gemini meeting notes (where available)",
            ]},
        ],
        [
            {"type": "heading", "text": "Creative: Flow, Veo 3.1, Nano Banana, Whisk"},
            {"type": "table", "headers": ["Tool", "What it does"], "rows": [
                ["Flow", "AI video workflow tool - 1000 credits/month on Pro"],
                ["Veo 3.1", "Text-to-video generation in Gemini and Flow"],
                ["Nano Banana", "AI image editing - one photo to many variants"],
                ["Whisk", "Image generation and remix in Gemini"],
                ["Google Photos", "More Remix + Veo photo-to-video (US)"],
            ]},
        ],
        [
            {"type": "heading", "text": "Google One - 5 TB storage"},
            {"type": "prose", "text": (
                "Google AI Pro includes <b>5 TB</b> Google One cloud storage (bumped from 2 TB, April 2026). "
                "Covers Photos, Drive, Gmail attachments. Also includes Google Home Premium Standard on Pro tier."
            )},
            {"type": "table", "headers": ["Plan", "US price", "India approx"], "rows": [
                ["Google AI Plus", "$7.99/mo", "Entry tier"],
                ["Google AI Pro", "$19.99/mo", "~Rs 1,950/mo"],
                ["18-mo value", "~$360", "~Rs 35,100"],
            ]},
        ],
        [
            {"type": "heading", "text": "How to claim (checklist)"},
            {"type": "bullets", "items": [
                "Use personal Google account (not Workspace admin unless eligible)",
                "Visit one.google.com/about/google-ai-plans/",
                "Check India / student / promo eligibility for 18-month offer",
                "Select Google AI Pro trial or promotional offer if shown",
                "Confirm billing - cancel before paid renewal if trial",
                "Open gemini.google.com - verify Pro badge",
                "Open notebooklm.google.com - verify expanded limits",
                "Enable Gemini in Gmail: Settings > Gemini",
            ]},
            {"type": "callout", "title": "Comment FREE", "text": (
                "Follow @piyush.glitch for updated offer links when Google rotates promos."
            )},
        ],
        [
            {"type": "heading", "text": "Who should claim"},
            {"type": "table", "headers": ["Profile", "Worth it?"], "rows": [
                ["Students / researchers", "Yes - NotebookLM + Deep Research"],
                ["Content creators", "Yes - Veo Flow image tools"],
                ["Google Workspace daily user", "Yes - Gmail Docs AI"],
                ["Need 5 TB backup", "Yes - storage alone offsets cost"],
                ["Rarely use Google", "Maybe - claim trial learn tools"],
            ]},
            {"type": "prose", "text": (
                "Sources: one.google.com, Google I/O 2026 plan updates. Limits change - verify current caps on Google One page."
            )},
        ],
    ]


def short_guide_pages() -> list:
    return [
        [
            {"type": "heading", "text": "Gemini Pro FREE - Quick Guide"},
            {"type": "subhead", "text": "3-slide carousel companion  |  Comment FREE"},
            {"type": "prose", "text": (
                "<b>Offer:</b> Google AI Pro worth approximately Rs 35,100 FREE for 18 months "
                "(promo eligibility required)."
            )},
            {"type": "table", "headers": ["Included", "Highlight"], "rows": [
                ["Gemini 3.1 Pro", "1M token context + Deep Research"],
                ["NotebookLM", "500 notebooks, 20 audio/video overviews daily"],
                ["Workspace", "Gemini in Gmail, Docs, Vids"],
                ["5 TB", "Google One storage"],
                ["Veo 3.1 + Flow", "AI video and 1000 credits/mo"],
            ]},
        ],
        [
            {"type": "heading", "text": "Claim in 5 steps"},
            {"type": "code", "text": (
                "1. Sign in at one.google.com\n"
                "2. Open Google AI Pro / AI plans page\n"
                "3. Apply eligible FREE or trial offer\n"
                "4. Verify Pro at gemini.google.com\n"
                "5. Start NotebookLM at notebooklm.google.com"
            )},
            {"type": "callout", "title": "@piyush.glitch", "text": "Comment FREE on Instagram for full 8-slide PDF guide."},
        ],
    ]


def build_pdf_for(carousel: dict) -> Path:
    folder = ROOT / carousel["slug"]
    folder.mkdir(parents=True, exist_ok=True)
    out = folder / carousel["pdf_name"]
    pages = full_guide_pages() if "Full" in carousel["slug"] else short_guide_pages()
    build_pdf(out, pages)
    return out


def build_all() -> None:
    for c in CAROUSELS:
        p = build_pdf_for(c)
        print(f"OK {p}", flush=True)
