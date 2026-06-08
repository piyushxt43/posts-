#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build a reference PDF in each Claude2ndJune carousel folder.

This PDF is the build-spec for the carousel: cover concept, the full 10-slide plan
(each agent's flow + output), the design rules for the interior slides, the caption,
and copy-paste image-prompt notes for slides 2-10 so the remaining nine can be
generated later with consistent design. Also writes caption.txt.
"""

from __future__ import annotations

from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak,
)

from carousels_content import CAROUSELS

ROOT = Path(__file__).resolve().parent

CREAM = HexColor("#F6F1E7")
INK = HexColor("#16150F")
CORAL = HexColor("#D97757")
PINK = HexColor("#F7A8C4")
LIME = HexColor("#9DBE3B")
GREY = HexColor("#6B6655")


def _styles():
    ss = getSampleStyleSheet()
    base = "Helvetica"
    return {
        "kicker": ParagraphStyle("kicker", parent=ss["Normal"], fontName="Helvetica-Bold",
                                 fontSize=11, textColor=CORAL, spaceAfter=4, leading=14,
                                 alignment=TA_LEFT),
        "h1": ParagraphStyle("h1", parent=ss["Title"], fontName="Helvetica-Bold", fontSize=30,
                             textColor=INK, leading=33, spaceAfter=8),
        "h2": ParagraphStyle("h2", parent=ss["Heading2"], fontName="Helvetica-Bold", fontSize=16,
                             textColor=INK, leading=20, spaceBefore=12, spaceAfter=6),
        "sub": ParagraphStyle("sub", parent=ss["Normal"], fontName="Helvetica", fontSize=13,
                              textColor=GREY, leading=18, spaceAfter=10),
        "body": ParagraphStyle("body", parent=ss["Normal"], fontName=base, fontSize=10.5,
                               textColor=INK, leading=15, spaceAfter=6),
        "small": ParagraphStyle("small", parent=ss["Normal"], fontName="Helvetica", fontSize=9,
                                textColor=GREY, leading=12.5),
        "mono": ParagraphStyle("mono", parent=ss["Normal"], fontName="Courier", fontSize=8.6,
                               textColor=INK, leading=12, backColor=HexColor("#EFE9DB"),
                               borderPadding=6, spaceAfter=8),
        "agent": ParagraphStyle("agent", parent=ss["Normal"], fontName="Helvetica-Bold", fontSize=12.5,
                                textColor=INK, leading=16),
    }


def _bg(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(CREAM)
    canvas.rect(0, 0, A4[0], A4[1], stroke=0, fill=1)
    canvas.setFillColor(CORAL)
    canvas.rect(0, A4[1] - 8 * mm, A4[0], 8 * mm, stroke=0, fill=1)
    canvas.setFillColor(GREY)
    canvas.setFont("Helvetica", 8)
    canvas.drawString(18 * mm, 12 * mm, "@piyush.glitch  -  Claude build spec")
    canvas.drawRightString(A4[0] - 18 * mm, 12 * mm, "page %d" % doc.page)
    canvas.restoreState()


def build_one(c: dict) -> Path:
    st = _styles()
    folder = ROOT / c["slug"]
    folder.mkdir(parents=True, exist_ok=True)
    out = folder / f"REFERENCE_{c['slug']}.pdf"

    doc = BaseDocTemplate(str(out), pagesize=A4,
                          leftMargin=18 * mm, rightMargin=18 * mm,
                          topMargin=20 * mm, bottomMargin=18 * mm)
    frame = Frame(doc.leftMargin, doc.bottomMargin,
                  doc.width, doc.height, id="f")
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=_bg)])

    full_title = f"{c['number_word']} {c['headline_main']} {c['system_line']}"
    flow = []

    def P(text, style):
        flow.append(Paragraph(text, st[style]))

    # ---- Page 1: cover concept ----
    P("CLAUDE2NDJUNE  /  CAROUSEL BUILD SPEC", "kicker")
    P(full_title, "h1")
    P("Reference document for slides 2-10. Slide 1 (cover) is already generated as "
      "<b>01_cover.png</b> in this folder. Use the design rules + prompts below to generate the rest.", "sub")

    P("Cover (slide 1) - DONE", "h2")
    P(f"<b>Headline:</b> {c['number_word']} {c['headline_main']}<br/>"
      f"<b>Highlight line:</b> {c['system_line']}<br/>"
      f"<b>Sticky note:</b> {c['sticky'].replace(chr(10), ' / ')}<br/>"
      f"<b>Highlight color:</b> {c['highlight_color']}<br/>"
      f"<b>Bottom photo:</b> {c['photo']}", "body")

    P("Design system (every slide)", "h2")
    P("- Ratio 4:5 (1080x1350). Warm cream paper (#F6F1E7), subtle grain, soft long shadows.<br/>"
      "- Headline: huge bold near-black condensed sans. Sub-text on a hand-marker highlight swipe.<br/>"
      "- Pink sticky note with push-pin for the one-liner takeaway.<br/>"
      "- Coral (#D97757) Claude logo card with white sparkle mark on EVERY slide (small, top-right).<br/>"
      "- Interior slides show the agent name + a left-to-right node flow (rounded tiles with icons) + an "
      "'Output:' note on a highlighted sticky.<br/>"
      "- Footer center: @piyush.glitch. No slide numbers baked into the art (post order is flexible).<br/>"
      "- A real, candid, NOT-AI-looking photo only on the cover and the final CTA slide.", "body")

    flow.append(PageBreak())

    # ---- Interior agent pages ----
    P("The workflow - slides 2 to 9", "h2")
    P("Each agent gets one slide. Title = agent name. Show the flow as connected rounded tiles. "
      "Put the outcome on a highlighted sticky labeled 'Output:'.", "sub")

    cell = ParagraphStyle(
        "cell", parent=st["body"], fontSize=8, leading=11, spaceAfter=0, spaceBefore=0,
    )
    cell_bold = ParagraphStyle(
        "cell_bold", parent=cell, fontName="Helvetica-Bold",
    )

    def cell_p(text: str, bold: bool = False) -> Paragraph:
        safe = text.replace("&", "&amp;").replace("<", "&lt;")
        return Paragraph(safe, cell_bold if bold else cell)

    usable = doc.width
    col_w = [10 * mm, 34 * mm, usable - 10 * mm - 34 * mm]
    rows = [[cell_p("#", bold=True), cell_p("Agent", bold=True), cell_p("What it does / Flow / Output", bold=True)]]
    for i, (name, does, fl, outp) in enumerate(c["agents"], start=2):
        block = (
            f"{does}<br/><br/>"
            f"<b>Flow:</b> {fl}<br/><br/>"
            f"<b>Output:</b> {outp}"
        )
        rows.append([cell_p(str(i)), cell_p(name, bold=True), cell_p(block)])

    tbl = Table(rows, colWidths=col_w, repeatRows=1)
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), CORAL),
        ("TEXTCOLOR", (0, 0), (-1, 0), HexColor("#FFFFFF")),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [HexColor("#FBF7EE"), HexColor("#F0EADB")]),
        ("GRID", (0, 0), (-1, -1), 0.4, HexColor("#D8D0BE")),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    flow.append(tbl)
    flow.append(Spacer(1, 8))

    P("Slide 10 - CTA", "h2")
    P("Recap the system in one line, then the call to action. Bring back a real candid photo (same person "
      "as the cover for continuity) and the Claude logo. Sticky note: 'Save + comment to get the build.'", "body")

    flow.append(PageBreak())

    # ---- Image-prompt notes for each interior slide ----
    P("Copy-paste image prompts (slides 2-10)", "h2")
    P("Reuse the cover DESIGN SYSTEM block, then append the per-slide block below. Render all text exactly.", "sub")

    for i, (name, does, fl, outp) in enumerate(c["agents"], start=2):
        nodes = " -> ".join(s.strip() for s in fl.split("->"))
        prompt = (
            f"Slide {i}/10. Same cream editorial design system. Top-left big bold black title: "
            f"\"{name}\". Under it, on a {c['highlight_color']} highlighter swipe: \"{does}\". "
            f"Center: a clean left-to-right workflow of rounded cream tiles connected by arrows, each tile "
            f"a small flat icon + label, sequence: {nodes}. Bottom-right: a highlighted sticky note labeled "
            f"'Output:' reading \"{outp}\". Top-right: small accurate coral Claude logo card with white "
            f"sparkle. Footer center: @piyush.glitch. No slide number in the art. Crisp, correct spelling, 4:5."
        )
        P(f"Slide {i}: {name}", "agent")
        P(prompt, "mono")

    cta_prompt = (
        f"Slide 10/10. CTA. Cream design. Big bold title: \"Build this {c['headline_main'].lower()} system\". "
        f"Highlighted line: \"{c['system_line']}\". A real candid NOT-AI photo of the same creator from the "
        f"cover, relaxed, looking at camera. Pink sticky: \"Save + comment to get the build\". Coral Claude logo "
        f"card top-right. Footer center: @piyush.glitch. 4:5, crisp, correct spelling."
    )
    P("Slide 10: CTA", "agent")
    P(cta_prompt, "mono")

    flow.append(PageBreak())

    # ---- Caption page ----
    P("Instagram caption", "h2")
    P(c["caption"].replace("\n", "<br/>"), "body")

    doc.build(flow)

    # caption.txt alongside
    (folder / "caption.txt").write_text(c["caption"], encoding="utf-8")
    return out


def main() -> int:
    for c in CAROUSELS:
        out = build_one(c)
        print(f"OK {out}", flush=True)
    print("All reference PDFs done.", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
