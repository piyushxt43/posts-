#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build dense, filled-page PDFs for Fourth June carousels."""

from __future__ import annotations

from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

from content import CAROUSELS
from pdf_content import PAGES

ROOT = Path(__file__).resolve().parent
CREAM = HexColor("#F4EEDE")
TERRA = HexColor("#C45E3B")
INK = HexColor("#1B1A17")
CORAL = HexColor("#EF5E45")
GREY = HexColor("#6E6657")
CARD = HexColor("#F9E5DC")
CODE_BG = HexColor("#EDE8DC")
WHITE = HexColor("#FFFFFF")
MARGIN = 0.6 * inch
CONTENT_W = letter[0] - 2 * MARGIN

PDF_BY_SLUG = {"01_Top_5_Claude_Code_Plugins_June": PAGES}


def _styles():
    ss = getSampleStyleSheet()
    return {
        "h1": ParagraphStyle(
            "h1", parent=ss["Title"], fontName="Helvetica-Bold", fontSize=20,
            textColor=INK, leading=24, spaceAfter=6,
        ),
        "h2": ParagraphStyle(
            "h2", parent=ss["Heading2"], fontName="Helvetica-Bold", fontSize=11,
            textColor=TERRA, leading=14, spaceBefore=8, spaceAfter=4,
        ),
        "body": ParagraphStyle(
            "b", parent=ss["Normal"], fontSize=9.5, leading=13,
            textColor=INK, spaceAfter=6,
        ),
        "bullet": ParagraphStyle(
            "bu", parent=ss["Normal"], fontSize=9.5, leading=12.5,
            textColor=INK, leftIndent=14, bulletIndent=6, spaceAfter=3,
        ),
        "code": ParagraphStyle(
            "c", parent=ss["Code"], fontName="Courier", fontSize=7.5,
            leading=10, textColor=INK, spaceAfter=0,
        ),
        "th": ParagraphStyle(
            "th", parent=ss["Normal"], fontName="Helvetica-Bold", fontSize=8.5,
            textColor=WHITE, leading=11,
        ),
        "td": ParagraphStyle(
            "td", parent=ss["Normal"], fontSize=8.5, leading=11, textColor=INK,
        ),
    }


def _bg(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(CREAM)
    canvas.rect(0, 0, letter[0], letter[1], fill=1, stroke=0)
    canvas.setFillColor(TERRA)
    canvas.rect(0, letter[1] - 7, letter[0], 7, fill=1, stroke=0)
    canvas.setFillColor(GREY)
    canvas.setFont("Helvetica", 7)
    canvas.drawString(MARGIN, 0.42 * inch, "@piyush.glitch  |  Claude Code Plugins  |  June 2026")
    canvas.drawRightString(letter[0] - MARGIN, 0.42 * inch, f"Page {doc.page}")
    canvas.restoreState()


def _table(headers: list, rows: list, st: dict, col_widths: list | None = None) -> Table:
    hdr = [Paragraph(h, st["th"]) for h in headers]
    data = [hdr]
    for row in rows:
        data.append([Paragraph(str(c), st["td"]) for c in row])
    if not col_widths:
        n = len(headers)
        col_widths = [CONTENT_W / n] * n
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), TERRA),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, HexColor("#FBF8F2")]),
        ("GRID", (0, 0), (-1, -1), 0.4, GREY),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]))
    return t


def _code_block(text: str, st: dict) -> Table:
    escaped = text.strip().replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    body = Paragraph(escaped.replace("\n", "<br/>"), st["code"])
    outer = Table([[body]], colWidths=[CONTENT_W])
    outer.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CODE_BG),
        ("BOX", (0, 0), (-1, -1), 0.6, GREY),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    return outer


def _callout(title: str, text: str, st: dict) -> Table:
    body = Paragraph(f"<b>{title}</b><br/>{text}", st["body"])
    t = Table([[body]], colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CARD),
        ("BOX", (0, 0), (-1, -1), 0.8, TERRA),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    return t


def _render_blocks(blocks: list, st: dict) -> list:
    flow = []
    for b in blocks:
        t = b["type"]
        if t == "heading":
            flow.append(Paragraph(b["text"], st["h1"]))
        elif t == "subhead":
            flow.append(Paragraph(b["text"], st["h2"]))
        elif t == "prose":
            flow.append(Paragraph(b["text"], st["body"]))
        elif t == "bullets":
            if b.get("title"):
                flow.append(Paragraph(f"<b>{b['title']}</b>", st["body"]))
            for item in b["items"]:
                flow.append(Paragraph(item, st["bullet"], bulletText="-"))
        elif t == "code":
            flow.append(_code_block(b["text"], st))
            flow.append(Spacer(1, 8))
        elif t == "table":
            cw = b.get("col_widths")
            if cw:
                cw = [w * inch for w in cw]
            flow.append(_table(b["headers"], b["rows"], st, cw))
            flow.append(Spacer(1, 8))
        elif t == "callout":
            flow.append(_callout(b["title"], b["text"], st))
            flow.append(Spacer(1, 8))
        elif t == "divider":
            flow.append(Spacer(1, 6))
    return flow


def build_one(carousel: dict) -> Path:
    st = _styles()
    folder = ROOT / carousel["slug"]
    folder.mkdir(parents=True, exist_ok=True)
    out = folder / carousel["pdf_name"]
    page_blocks = PDF_BY_SLUG[carousel["slug"]]

    doc = BaseDocTemplate(
        str(out), pagesize=letter,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=0.55 * inch, bottomMargin=0.55 * inch,
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=_bg)])

    flow = []
    for i, blocks in enumerate(page_blocks):
        flow.extend(_render_blocks(blocks, st))
        if i < len(page_blocks) - 1:
            flow.append(PageBreak())

    doc.build(flow)
    return out


def main() -> int:
    for c in CAROUSELS:
        out = build_one(c)
        print(f"OK {out} ({out.stat().st_size:,} bytes, {len(PDF_BY_SLUG[c['slug']])} pages)", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
