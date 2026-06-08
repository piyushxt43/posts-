#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dense prompt PDFs for Draftly Growth carousels."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
from content import CAROUSELS
from pdf_builder_rich import build_pdf


def pages_for(c: dict) -> list:
    k = c["keyword"]
    t = c["topic"]
    return [
        [
            {"type": "heading", "text": f"Draftly Prompt Guide - {c['title']}"},
            {"type": "subhead", "text": f"{t}  |  draftly.space  |  Comment {k}"},
            {"type": "prose", "text": (
                "Copy-paste prompts for the Draftly 3D builder at <b>draftly.space/3d-builder</b>. "
                "Each block is a production-grade creative brief - website copy, hero still, keyframes, "
                "and motion. Not one-liners."
            )},
            {"type": "callout", "title": f"Comment {k}", "text": (
                f"Comment <b>{k}</b> on the Instagram carousel for PDF updates."
            )},
            {"type": "table", "headers": ["Step", "Paste when"], "rows": [
                ["1", "Describe the website you want to build..."],
                ["2", "Hero image / visual draft"],
                ["3", "First + last frame keyframes (right rail)"],
                ["4", "Video motion before animate"],
                ["5", "Ship - frames extract automatically"],
            ]},
        ],
        [
            {"type": "heading", "text": "Step 1 - Website prompt (full)"},
            {"type": "prose", "text": (
                "Paste at <b>Prompt Input</b>. Include nav, hero copy, every scroll section, "
                "palette, typography, CTA behavior, and motion notes."
            )},
            {"type": "code", "text": c["website_prompt"]},
            {"type": "bullets", "title": "Website prompt checklist", "items": [
                "Nav links and hero headline verbatim",
                "At least 4 scroll sections named",
                "Palette and typography direction",
                "Motion: scroll-scrubbed frames noted",
                "Anti-slop line (not generic AI aesthetic)",
            ]},
        ],
        [
            {"type": "heading", "text": "Step 2 - Hero image prompt (full)"},
            {"type": "prose", "text": (
                "Paste at <b>Visual Draft</b>. Controls the cinematic still extracted into 200+ frames. "
                "Minimum three paragraphs: scene, materials/light, camera/color grade."
            )},
            {"type": "code", "text": c["image_prompt"]},
            {"type": "callout", "title": "Aspect ratio", "text": (
                "Default 16:9 landscape for scroll extraction. Match your target hero proportions."
            )},
        ],
        [
            {"type": "heading", "text": "Step 3 - First frame prompt"},
            {"type": "prose", "text": (
                "Opening keyframe - wide composition, negative space for headline overlay, "
                "same visual world as hero still."
            )},
            {"type": "code", "text": c["first_frame_prompt"]},
        ],
        [
            {"type": "heading", "text": "Step 3 - Last frame prompt"},
            {"type": "prose", "text": (
                "Closing keyframe - camera closer, product/hero more revealed, "
                "stronger rim light or action peak."
            )},
            {"type": "code", "text": c["last_frame_prompt"]},
        ],
        [
            {"type": "heading", "text": "Step 4 - Video motion prompt (full)"},
            {"type": "prose", "text": (
                "Paste at <b>Motion Pass</b> / confirm-image. One focused paragraph: "
                "dolly direction, speed, loop length, what moves vs stays static."
            )},
            {"type": "code", "text": c["video_prompt"]},
            {"type": "table", "headers": ["Setting", "Recommendation"], "rows": [
                ["FPS", "10-24 for web hero, 30-40 for smooth product"],
                ["Duration", "~8 seconds default"],
                ["Loop", "Seamless for infinite scroll feel"],
            ]},
        ],
        [
            {"type": "heading", "text": "Step 5 - Ship checklist"},
            {"type": "bullets", "items": [
                "Website prompt saved and approved",
                "Hero still generated - check no fake text in image",
                "First + last frames set for motion arc",
                "Video generated - preview before extract",
                "400+ frames extracted - test scroll on mobile",
                "Publish to *.draftly.space or ZIP export (Pro+)",
                "Iterate copy via chat - no rebuild needed for text",
            ]},
            {"type": "code", "text": (
                "# After ship - chat edits\n"
                "Change hero headline to: [new copy]\n"
                "Update primary CTA color to #EF5E45\n"
                "Add testimonial section below pricing"
            )},
        ],
        [
            {"type": "heading", "text": "Post-ship chat iteration prompts"},
            {"type": "prose", "text": (
                "After Website Ready, use AI Copilot to edit without rebuilding motion. "
                "Copy these follow-ups into the builder chat."
            )},
            {"type": "code", "text": (
                "# Copy tweaks (no motion rebuild)\n"
                "Change hero headline to a shorter 6-word version.\n"
                "Update all body copy to more enterprise tone.\n"
                "Swap primary CTA from 'Book Demo' to 'Start Free Trial'.\n"
                "Add a testimonial row with 3 client quotes below the feature section.\n\n"
                "# Design tweaks\n"
                "Shift palette accent from coral to deep navy.\n"
                "Increase section padding by 20% for more luxury whitespace.\n\n"
                "# When to rebuild motion\n"
                "Only regenerate video if hero composition is wrong.\n"
                "Text and layout changes never require new frame extraction."
            )},
        ],
        [
            {"type": "heading", "text": "Draftly builder quick reference"},
            {"type": "table", "headers": ["UI label", "Location"], "rows": [
                ["Describe the website...", "3d-builder main chat"],
                ["Preview / Ship / Pipeline", "Right panel tabs"],
                ["Customize / Ship / Design", "Preset editor"],
                ["Extracting Frames 400/400", "Frames tab"],
                ["Publish & custom domain", "Ship tab"],
            ]},
            {"type": "prose", "text": (
                "<b>Free trial:</b> draftly.space - 7 days, 1 site, no credit card. "
                "<b>Pro $60/mo:</b> ZIP export, 7 sites, preset AI chat."
            )},
            {"type": "callout", "title": "Pro tip", "text": (
                "Treat each prompt like a brief to photographer + motion designer + web team. "
                "Specificity is what makes output feel premium - not another AI template."
            )},
        ],
    ]


def main() -> int:
    for c in CAROUSELS:
        folder = ROOT / c["slug"]
        folder.mkdir(parents=True, exist_ok=True)
        out = folder / c["pdf_name"]
        build_pdf(out, pages_for(c))
        print(f"OK {out} ({out.stat().st_size:,} bytes)", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
