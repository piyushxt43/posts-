# -*- coding: utf-8 -*-
"""Build 5-6 page prompt guide PDFs for each Draftly carousel."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT_PKG = Path(__file__).resolve().parent
if str(ROOT_PKG) not in sys.path:
    sys.path.insert(0, str(ROOT_PKG))

from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_LEFT
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

from content import CAROUSELS

ROOT = ROOT_PKG
CREAM = HexColor("#F4EEDE")
GRID = HexColor("#E7DEC6")
CARD = HexColor("#FCFAF3")
INK = HexColor("#1B1A17")
MUTED = HexColor("#6E6657")
CORAL = HexColor("#EF5E45")
CORAL_SOFT = HexColor("#FBE0D8")
LINE = HexColor("#D8CFB8")
PAGE_W, PAGE_H = letter
MARGIN = 0.72 * inch
CONTENT_W = PAGE_W - 2 * MARGIN

STY_TITLE = ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=24, leading=28, textColor=INK)
STY_SUB = ParagraphStyle("sub", fontName="Helvetica", fontSize=12, leading=16, textColor=MUTED, spaceAfter=10)
STY_H2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=15, leading=18, textColor=INK, spaceBefore=8, spaceAfter=6)
STY_BODY = ParagraphStyle("body", fontName="Helvetica", fontSize=10.5, leading=15.5, textColor=INK, spaceAfter=8)
STY_PROMPT = ParagraphStyle(
    "prompt", fontName="Courier", fontSize=8.6, leading=12.5, textColor=INK, spaceAfter=10, leftIndent=8, rightIndent=8,
)
STY_EYEBROW = ParagraphStyle("eyebrow", fontName="Helvetica-Bold", fontSize=10, leading=12, textColor=CORAL, spaceAfter=6)


def esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def paint_bg(canvas):
    canvas.saveState()
    canvas.setFillColor(CREAM)
    canvas.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
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


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.line(MARGIN, 0.55 * inch, PAGE_W - MARGIN, 0.55 * inch)
    canvas.setFont("Helvetica-Bold", 8.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(MARGIN, 0.4 * inch, "draftly.space / piyush.glitch")
    canvas.setFont("Helvetica", 8.5)
    canvas.drawRightString(PAGE_W - MARGIN, 0.4 * inch, "Prompt Guide")
    canvas.drawCentredString(PAGE_W / 2, 0.4 * inch, str(doc.page))
    canvas.restoreState()


def on_page(canvas, doc):
    paint_bg(canvas)
    if doc.page > 1:
        footer(canvas, doc)


def prompt_block(title: str, text: str) -> list:
    return [
        Paragraph(title.upper(), STY_EYEBROW),
        Table(
            [[Paragraph(esc(text).replace("\n", "<br/>"), STY_PROMPT)]],
            colWidths=[CONTENT_W - 16],
            style=TableStyle([
                ("BACKGROUND", (0, 0), (-1, -1), CARD),
                ("BOX", (0, 0), (-1, -1), 0.8, LINE),
                ("LEFTPADDING", (0, 0), (-1, -1), 12),
                ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                ("TOPPADDING", (0, 0), (-1, -1), 10),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
            ]),
        ),
        Spacer(1, 8),
    ]


def build_story(carousel: dict) -> list:
    story = [
        Paragraph("DRAFTLY", STY_EYEBROW),
        Paragraph(f"{esc(carousel['title'])} Prompt Guide", STY_TITLE),
        Paragraph(
            f"Copy-paste prompts for {esc(carousel['product_label'])}. "
            "Each block matches the Draftly 3D builder flow: website, hero image, keyframes, motion, ship.",
            STY_SUB,
        ),
        Paragraph("How to use this guide", STY_H2),
        Paragraph(
            "Open draftly.space/3d-builder. Paste the website prompt at step one, the hero image prompt at step two, "
            "set first and last frames in the right rail, add the motion prompt before video generation, then ship the scroll site. "
            "These are production-grade briefs - not one-liners.",
            STY_BODY,
        ),
        PageBreak(),
        Paragraph("Step 1 - Website prompt", STY_H2),
        Paragraph(
            "Paste when the builder asks you to describe the website. Include layout, copy, sections, palette, and CTA behavior.",
            STY_BODY,
        ),
        *prompt_block("Website prompt", carousel["website_prompt"]),
        Paragraph("Step 2 - Hero image prompt", STY_H2),
        Paragraph(
            "Paste when Draftly asks for the hero background. This controls the scroll-synced cinematic still - scene, lens, light, mood, and color.",
            STY_BODY,
        ),
        *prompt_block("Hero image prompt", carousel["image_prompt"]),
        PageBreak(),
        Paragraph("Step 3 - First and last frame prompts", STY_H2),
        Paragraph(
            "Use the hero still as the first frame. Generate the last frame from its own prompt for first-to-last video motion.",
            STY_BODY,
        ),
        *prompt_block("First frame prompt", carousel["first_frame_prompt"]),
        *prompt_block("Last frame prompt", carousel["last_frame_prompt"]),
        Paragraph("Step 4 - Video motion prompt", STY_H2),
        Paragraph(
            "Optional camera direction at the confirm-image step. Keep it one focused paragraph of cinematic motion notes.",
            STY_BODY,
        ),
        *prompt_block("Video motion prompt", carousel["video_prompt"]),
        PageBreak(),
        Paragraph("Expected output", STY_H2),
        Paragraph(f"<b>Headline:</b> {esc(carousel['result_headline'])}", STY_BODY),
        Paragraph(esc(carousel["result_notes"]), STY_BODY),
        Paragraph("Why this workflow matters", STY_H2),
        Paragraph(esc(carousel["why_website"]), STY_BODY),
        Paragraph("Quick checklist", STY_H2),
        Paragraph(
            "1. Website prompt saved<br/>"
            "2. Hero still generated and approved<br/>"
            "3. Last frame optional but set for first-to-last motion<br/>"
            "4. Motion prompt added before video<br/>"
            "5. Frames extracted and site layered on top<br/>"
            "6. Iterate copy in chat after ship",
            STY_BODY,
        ),
        Spacer(1, 12),
        Table(
            [[Paragraph(
                "Pro tip: Treat each prompt like a creative brief you would send to a photographer, "
                "motion designer, and web team - specificity is what makes the output feel premium.",
                STY_BODY,
            )]],
            colWidths=[CONTENT_W],
            style=TableStyle([
                ("BACKGROUND", (0, 0), (-1, -1), CORAL_SOFT),
                ("LEFTPADDING", (0, 0), (-1, -1), 14),
                ("RIGHTPADDING", (0, 0), (-1, -1), 14),
                ("TOPPADDING", (0, 0), (-1, -1), 12),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
                ("LINEBEFORE", (0, 0), (0, -1), 3, CORAL),
            ]),
        ),
    ]
    return story


def render_pdf(path: Path, carousel: dict) -> None:
    doc = BaseDocTemplate(
        str(path),
        pagesize=letter,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=0.75 * inch,
        title=f"Draftly {carousel['title']} Prompt Guide",
    )
    frame = Frame(MARGIN, 0.75 * inch, CONTENT_W, PAGE_H - MARGIN - 0.75 * inch, id="normal")
    doc.addPageTemplates([
        PageTemplate(id="Cover", frames=frame, onPage=on_page),
        PageTemplate(id="Later", frames=frame, onPage=on_page),
    ])
    story = build_story(carousel)
    story.insert(0, NextPageTemplate("Later"))
    doc.build(story)


def main() -> int:
    for carousel in CAROUSELS:
        folder = ROOT / carousel["slug"]
        folder.mkdir(parents=True, exist_ok=True)
        out = folder / "09_prompt_guide.pdf"
        render_pdf(out, carousel)
        print(f"PDF {out.name} -> {carousel['slug']}", flush=True)
    print(f"Done. {len(CAROUSELS)} PDFs in {ROOT}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
