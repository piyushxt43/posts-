# -*- coding: utf-8 -*-
"""Build 12+ page beauty PDFs with embedded carousel images + prompts."""

from __future__ import annotations

import re
from pathlib import Path

from reportlab.lib.units import inch

from pdf_builder_rich import build_pdf

ROOT = Path(__file__).resolve().parent

DNA_BLOCK = """CHARACTER DNA (LOCKED - paste on every prompt):
Caucasian woman, 27, fair skin, light freckles nose and cheeks,
light green-hazel eyes, wavy dirty-blonde hair shoulder length,
editorial bone structure, minimal makeup, visible pores,
no plastic skin, no wax smoothing, no beauty filter."""

NEGATIVE_BLOCK = """NEGATIVE (append every generation):
plastic skin, wax doll, beauty filter, poreless, uncanny eyes,
extra fingers, CGI gloss lips, painted tears, warped text,
watermark, lorem ipsum, generic influencer face, over-sharpened"""

SKIP_PREFIXES = (
    "SLIDE TYPE:", "SAME MODEL", "3:4 vertical", "Crisp readable",
    "Footer bottom", "Hyper-real skin", "NO cream", "NOT full-bleed",
    "Top label:", "Top center", "Clinical beauty", "Shot on 85mm",
)


def _clean_prompt(raw: str) -> str:
    lines = []
    for line in raw.replace("\r", "").split("\n"):
        s = line.strip()
        if not s:
            continue
        if any(s.startswith(p) for p in SKIP_PREFIXES):
            continue
        lines.append(s)
    text = "\n".join(lines).strip()
    if len(text) > 1400:
        text = text[:1397] + "..."
    return text or "(See image for on-slide layout.)"


def _slide_title(filename: str) -> str:
    base = filename.replace(".png", "").replace("_", " ")
    return base[3:].title() if len(base) > 3 else base.title()


META = {
    "06_Build_Realistic_AI_Character_Shoots": {
        "title": "Build Realistic AI Character Shoots",
        "cta": "SHOOTS",
        "tagline": "Visual AI Club 7-slide proof system",
        "insights": {
            "01_cover.png": "Scroll-stop emotional cover. One tear + finger near lip sells humanity before macros.",
            "02_detailed_models.png": "Typography slide proves hyper-real without another face dump.",
            "03_eye_macro.png": "Eye macro is your credibility slide - iris fibers + tear bead.",
            "04_skin_macro.png": "Pores and freckles must be irregular - repeating patterns fail QA.",
            "05_lip_macro.png": "Lip + finger interaction shows skin ridges on hands too.",
            "06_texture_split.png": "Split panel compares moisture + freckle field in one frame.",
            "07_sky_hero_cta.png": "Sky hero converts to campaign - terracotta + blue sky contrast.",
        },
        "workflow": [
            "Lock DNA block once",
            "Generate cover x4, pick reference face",
            "Run macros in order: eye, skin, lip, split",
            "Typography slide in Figma if text warps",
            "Sky hero last with 24-35mm language",
        ],
    },
    "07_Generate_AI_Beauty_Campaigns": {
        "title": "Generate AI Beauty Campaigns",
        "cta": "BEAUTY",
        "tagline": "Moisture, shadow truth, and sky closer",
        "insights": {
            "01_cover.png": "Build Realistic headline stack sets educational tone.",
            "02_detailed_models.png": "Dual inset: portrait + eye macro proves system depth.",
            "03_eye_macro.png": "Reuse eye macro for grid consistency with carousel 06.",
            "04_pores_macro.png": "Water droplet on cheek - single fluid rule.",
            "05_lip_macro.png": "Lip gloss highlight must be micro-wrinkles visible.",
            "06_shadow_texture.png": "Side light defines philtrum shadow - anti-CGI proof.",
            "07_sky_hero_cta.png": "Generate + AI Shoots type on sky - comment BEAUTY.",
        },
        "workflow": [
            "Same DNA as character shoots series",
            "Add moisture clause on skin macros",
            "One shadow-truth slide minimum",
            "Match warm grade cover to sky finale",
        ],
    },
    "08_Identity_Lock_Character_DNA": {
        "title": "Identity Lock Character DNA",
        "cta": "IDENTITY",
        "tagline": "Stop face drift across slides",
        "insights": {
            "01_cover.png": "Identity Lock cover - DNA before beauty.",
            "02_character_dna.png": "Highest-save slide: copy-paste DNA card.",
            "03_three_angles.png": "Three angles must match at thumbnail size.",
            "04_reference_workflow.png": "Reference upload workflow - fix wording not random re-roll.",
            "05_freckle_map.png": "Permanent marks anchor every macro.",
            "06_seed_discipline.png": "Seed + prefix discipline for GPT and MJ.",
            "07_qa_checklist.png": "Pre-publish identity QA - 150px test.",
            "08_sky_cta.png": "Sky CTA locks brand after technical proof.",
        },
        "workflow": [
            "Write DNA before any image gen",
            "Cover x4, upload winner as reference",
            "Three-angle test same session",
            "Freckle map copied verbatim into macros",
        ],
    },
    "09_Macro_Prompt_Library": {
        "title": "Macro Prompt Library",
        "cta": "MACRO",
        "tagline": "Copy-paste blocks for eye, skin, lips",
        "insights": {
            "01_cover.png": "Library cover - positions deck as tool not inspiration.",
            "02_macro_blocks.png": "Teach three blocks: eye, skin, lips.",
            "03_eye_macro.png": "Labels: Realistic Eye, Tears, Lashes.",
            "04_skin_macro.png": "Labels: Pores, Texture, Moles.",
            "05_lip_macro.png": "Finger skin texture equals face rigor.",
            "06_tear_system.png": "One fluid per image - tear OR sweat OR gloss.",
            "07_batch_order.png": "Batch order reduces drift between gens.",
            "08_sky_cta.png": "Macro library CTA on sky hero.",
        },
        "workflow": [
            "Copy blocks from slide 2 into prompt doc",
            "Never paraphrase DNA mid-batch",
            "Append negative + Phase One suffix",
            "Run batch order slide 7 exactly",
        ],
    },
    "10_Lighting_Camera_Beauty_Setups": {
        "title": "Lighting and Camera Setups",
        "cta": "LIGHT",
        "tagline": "Window, raking macro, sky setups",
        "insights": {
            "01_cover.png": "Light Direction cover.",
            "02_window_setup.png": "Key 45 left + fill bounce - cover and portraits.",
            "03_raking_macro.png": "Raking side for pore revelation.",
            "04_camera_clauses.png": "85mm cover vs 100mm macro vs 35mm sky.",
            "05_light_diagram.png": "Diagram + result inset teaches matching.",
            "06_skin_macro.png": "Macro proves lighting vector matches diagram.",
            "07_grade_tokens.png": "Color grade tokens prevent orange drift.",
            "08_sky_cta.png": "Outdoor Setup C on sky finale.",
        },
        "workflow": [
            "Pick setup before posing language",
            "Never mix studio macro light with sky cover",
            "Document winning setup in lighting.txt",
            "Match vector across all macros in set",
        ],
    },
    "11_Quality_Gates_Negative_Prompts": {
        "title": "Quality Gates and Negative Prompts",
        "cta": "QUALITY",
        "tagline": "Reject plastic before publish",
        "insights": {
            "01_cover.png": "Quality Gates cover - stop plastic skin.",
            "02_negative_block.png": "Master negative - never shorten mid-campaign.",
            "03_pass_fail.png": "Thumbnail PASS/FAIL columns.",
            "04_plastic_recovery.png": "Recovery adds pores, removes porcelain words.",
            "05_eye_recovery.png": "Capillaries + iris fibers fix glass eyes.",
            "06_skin_macro.png": "Post-recovery macro proof slide.",
            "07_pre_publish.png": "Seven-point checklist before Instagram.",
            "08_sky_cta.png": "Quality system CTA.",
        },
        "workflow": [
            "Append negative on every gen",
            "150px thumbnail identity test",
            "Run recovery prompts once, not five",
            "Log reject reason tags per failed gen",
        ],
    },
    "12_Campaign_Contact_Sheet_Export": {
        "title": "Campaign Contact Sheet Export",
        "cta": "CAMPAIGN",
        "tagline": "Six deliverables from one character",
        "insights": {
            "01_cover.png": "Campaign board cover.",
            "02_six_deliverables.png": "Hero, macros, angles, sky, square crop.",
            "03_scene_swap.png": "Background clause only - never drop DNA.",
            "04_contact_sheet.png": "Flat lay six prints - art director desk.",
            "05_pricing.png": "Price the system not per image.",
            "06_figma_assembly.png": "Vectors for type, PNG for faces.",
            "07_grid_slide.png": "2x3 grid Ready for campaign use.",
            "08_sky_cta.png": "Campaign ready sky closer.",
        },
        "workflow": [
            "Lock character before scene swaps",
            "Export 1080x1350 + 1080x1080",
            "Figma assembly for warped text fixes",
            "Package DNA.txt + negative.txt with delivery",
        ],
    },
}


def _intro_pages(carousel: dict, meta: dict) -> list:
    slug = carousel["slug"]
    slides = carousel["slides"]
    n = len(slides)
    return [
        [
            {"type": "heading", "text": meta["title"]},
            {"type": "subhead", "text": f"@piyush.glitch  |  {meta['tagline']}"},
            {"type": "prose", "text": (
                f"This PDF matches Instagram carousel <b>{slug}</b> ({n} slides). "
                "Every slide from the carousel is printed below with the <b>actual generated image</b>, "
                "the image-generation prompt used in production, and operator notes so you can reproduce the deck."
            )},
            {"type": "callout", "title": "Comment keyword", "text": (
                f"On Instagram, comment <b>{meta['cta']}</b> to receive this PDF. "
                "Files included: all slide PNGs (also in this folder), caption.txt, and this guide."
            )},
            {"type": "table", "headers": ["Slide", "File", "Role"], "rows": [
                [str(i), fn, _slide_title(fn)] for i, (fn, _) in enumerate(slides, 1)
            ]},
            {"type": "prose", "text": (
                "<b>Tools:</b> GPT Image (1024x1536), Midjourney v6 with character reference, "
                "or Flux with reference image. Ratio: 4:5 (1080x1350) for Instagram."
            )},
        ],
        [
            {"type": "heading", "text": "Operator workflow"},
            {"type": "bullets", "title": f"Steps for {meta['title']}", "items": meta["workflow"]},
            {"type": "code", "text": DNA_BLOCK},
            {"type": "code", "text": NEGATIVE_BLOCK},
            {"type": "table", "headers": ["Check", "Pass?"], "rows": [
                ["DNA block in every prompt", ""],
                ["Negative block appended", ""],
                ["Same face at 150px thumbnail", ""],
                ["Lighting vector consistent", ""],
                ["Text spelling on overlays", ""],
                ["Sky slide not clipping skin", ""],
            ]},
            {"type": "prose", "text": (
                "<b>Next pages:</b> one page per carousel slide - image on top, prompt below, insights at bottom. "
                "Use this as your shoot bible during generation sessions."
            )},
        ],
    ]


def _slide_page(folder: Path, filename: str, prompt: str, meta: dict, index: int) -> list:
    insight = meta["insights"].get(filename, "Reproduce layout and lighting from the image.")
    title = _slide_title(filename)
    img_path = folder / filename
    return [
        [
            {"type": "subhead", "text": f"Slide {index} - {title}"},
            {"type": "image", "path": str(img_path), "caption": f"Actual output: {filename}", "max_height": 3.75 * inch},
            {"type": "h3", "text": "What this slide does"},
            {"type": "prose", "text": insight},
            {"type": "h3", "text": "Generation prompt (copy-paste)"},
            {"type": "code", "text": _clean_prompt(prompt)},
            {"type": "bullets", "title": "Production notes", "items": [
                "Generate 4 variations; pick best face match to DNA",
                "Keep PIYUSH.GLITCH header and @piyush.glitch footer",
                "If text warps, rebuild type in Figma using PNG face only",
                "Do not change eye color or freckle map mid-series",
            ]},
        ]
    ]


def _appendix_page(meta: dict) -> list:
    return [
        [
            {"type": "heading", "text": "Master prompt stack"},
            {"type": "prose", "text": (
                "Combine DNA + shot clause + negative on every generation. "
                "Below is the suffix to append on macro slides."
            )},
            {"type": "code", "text": (
                "Phase One editorial macro, visible pores and peach fuzz,\n"
                "natural moisture, 4:5 vertical 1080x1350,\n"
                "PIYUSH.GLITCH top right, @piyush.glitch footer.\n"
                "Handwritten white arrows for labels on macro slides only."
            )},
            {"type": "table", "headers": ["Problem", "Fix"], "rows": [
                ["Plastic skin", "Add pores + peach fuzz; remove porcelain from prompt"],
                ["Face drift", "Re-upload reference; fix DNA wording"],
                ["Warped overlay text", "Figma typography on exported PNG"],
                ["Orange skin drift", "Add honest undertone + desaturate grade"],
                ["Glass eyes", "Add capillaries, iris fibers, moisture"],
            ]},
            {"type": "callout", "title": "Stay updated", "text": (
                f"Follow @piyush.glitch. Comment <b>{meta['cta']}</b> on the carousel for PDF updates. "
                f"Guide: {meta['title']}."
            )},
        ],
    ]


def build_pages_for_carousel(carousel: dict) -> list:
    meta = META[carousel["slug"]]
    folder = ROOT / carousel["slug"]
    pages = []
    pages.extend(_intro_pages(carousel, meta))
    for i, (fn, pr) in enumerate(carousel["slides"], 1):
        pages.extend(_slide_page(folder, fn, pr, meta, i))
    pages.extend(_appendix_page(meta))
    return pages


def build_beauty_pdf(carousel: dict) -> Path:
    folder = ROOT / carousel["slug"]
    folder.mkdir(parents=True, exist_ok=True)
    out = folder / carousel["pdf_name"]
    pages = build_pages_for_carousel(carousel)
    build_pdf(out, pages)
    return out


BEAUTY_SLUGS = set(META.keys())
