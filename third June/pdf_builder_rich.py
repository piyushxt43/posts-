# -*- coding: utf-8 -*-
"""Rich PDF renderer: filled pages, tables, code blocks, embedded images."""

from __future__ import annotations

from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    Image,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

CREAM = HexColor("#F4EEDE")
CORAL = HexColor("#EF5E45")
TERRA = HexColor("#C45E3B")
INK = HexColor("#1B1A17")
GREY = HexColor("#6E6657")
CARD = HexColor("#F9E5DC")
CODE_BG = HexColor("#EDE8DC")
WHITE = HexColor("#FFFFFF")
MARGIN = 0.55 * inch
CONTENT_W = letter[0] - 2 * MARGIN


def _styles():
    ss = getSampleStyleSheet()
    return {
        "h1": ParagraphStyle(
            "h1", parent=ss["Title"], fontName="Helvetica-Bold", fontSize=19,
            textColor=INK, leading=23, spaceAfter=6,
        ),
        "h2": ParagraphStyle(
            "h2", parent=ss["Heading2"], fontName="Helvetica-Bold", fontSize=11,
            textColor=CORAL, leading=14, spaceBefore=6, spaceAfter=4,
        ),
        "h3": ParagraphStyle(
            "h3", parent=ss["Heading3"], fontName="Helvetica-Bold", fontSize=9.5,
            textColor=INK, leading=12, spaceAfter=3,
        ),
        "body": ParagraphStyle(
            "b", parent=ss["Normal"], fontSize=9.5, leading=13,
            textColor=INK, spaceAfter=5,
        ),
        "bullet": ParagraphStyle(
            "bu", parent=ss["Normal"], fontSize=9, leading=12,
            textColor=INK, leftIndent=12, bulletIndent=5, spaceAfter=2,
        ),
        "caption": ParagraphStyle(
            "cap", parent=ss["Normal"], fontSize=8, leading=10,
            textColor=GREY, spaceAfter=4, alignment=1,
        ),
        "code": ParagraphStyle(
            "c", parent=ss["Code"], fontName="Courier", fontSize=7,
            leading=9.5, textColor=INK,
        ),
        "th": ParagraphStyle(
            "th", parent=ss["Normal"], fontName="Helvetica-Bold", fontSize=8,
            textColor=WHITE, leading=10,
        ),
        "td": ParagraphStyle(
            "td", parent=ss["Normal"], fontSize=8, leading=10, textColor=INK,
        ),
    }


def _bg(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(CREAM)
    canvas.rect(0, 0, letter[0], letter[1], fill=1, stroke=0)
    canvas.setFillColor(CORAL)
    canvas.rect(0, letter[1] - 7, letter[0], 7, fill=1, stroke=0)
    canvas.setFillColor(TERRA)
    canvas.rect(0, letter[1] - 13, letter[0] * 0.28, 5, fill=1, stroke=0)
    canvas.setFillColor(GREY)
    canvas.setFont("Helvetica", 7)
    canvas.drawString(MARGIN, 0.4 * inch, "@piyush.glitch  |  AI Beauty Operator Guide")
    canvas.drawRightString(letter[0] - MARGIN, 0.4 * inch, f"Page {doc.page}")
    canvas.restoreState()


def _table(headers, rows, st, col_widths=None):
    hdr = [Paragraph(h, st["th"]) for h in headers]
    data = [hdr] + [[Paragraph(str(c), st["td"]) for c in r] for r in rows]
    if not col_widths:
        col_widths = [CONTENT_W / len(headers)] * len(headers)
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), CORAL),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, HexColor("#FBF8F2")]),
        ("GRID", (0, 0), (-1, -1), 0.35, GREY),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ]))
    return t


def _code_block(text, st):
    escaped = text.strip().replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    body = Paragraph(escaped.replace("\n", "<br/>"), st["code"])
    outer = Table([[body]], colWidths=[CONTENT_W])
    outer.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CODE_BG),
        ("BOX", (0, 0), (-1, -1), 0.5, GREY),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
    ]))
    return outer


def _callout(title, text, st):
    body = Paragraph(f"<b>{title}</b><br/>{text}", st["body"])
    t = Table([[body]], colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CARD),
        ("BOX", (0, 0), (-1, -1), 0.7, CORAL),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
    ]))
    return t


def _image_block(path: Path, caption: str, st: dict, max_h: float = 4.2 * inch) -> list:
    flow = []
    if not path.exists():
        flow.append(Paragraph(f"<i>Image missing: {path.name}</i>", st["body"]))
        return flow
    img = Image(str(path))
    iw, ih = img.imageWidth, img.imageHeight
    scale = min(CONTENT_W / iw, max_h / ih)
    img.drawWidth = iw * scale
    img.drawHeight = ih * scale
    t = Table([[img]], colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("BOX", (0, 0), (-1, -1), 0.5, GREY),
        ("BACKGROUND", (0, 0), (-1, -1), WHITE),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    flow.append(t)
    if caption:
        flow.append(Paragraph(caption, st["caption"]))
    flow.append(Spacer(1, 6))
    return flow


def render_blocks(blocks, st) -> list:
    flow = []
    for b in blocks:
        t = b["type"]
        if t == "heading":
            flow.append(Paragraph(b["text"], st["h1"]))
        elif t == "subhead":
            flow.append(Paragraph(b["text"], st["h2"]))
        elif t == "h3":
            flow.append(Paragraph(b["text"], st["h3"]))
        elif t == "prose":
            flow.append(Paragraph(b["text"], st["body"]))
        elif t == "bullets":
            if b.get("title"):
                flow.append(Paragraph(f"<b>{b['title']}</b>", st["body"]))
            for item in b["items"]:
                flow.append(Paragraph(item, st["bullet"], bulletText="-"))
        elif t == "code":
            flow.append(_code_block(b["text"], st))
            flow.append(Spacer(1, 6))
        elif t == "table":
            cw = [w * inch for w in b["col_widths"]] if b.get("col_widths") else None
            flow.append(_table(b["headers"], b["rows"], st, cw))
            flow.append(Spacer(1, 6))
        elif t == "callout":
            flow.append(_callout(b["title"], b["text"], st))
            flow.append(Spacer(1, 6))
        elif t == "image":
            flow.extend(_image_block(Path(b["path"]), b.get("caption", ""), st, b.get("max_height", 4.2 * inch)))
        elif t == "spacer":
            flow.append(Spacer(1, b.get("height", 8)))
    return flow


def build_pdf(out_path: Path, page_blocks: list) -> Path:
    st = _styles()
    doc = BaseDocTemplate(
        str(out_path), pagesize=letter,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=0.5 * inch, bottomMargin=0.5 * inch,
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=_bg)])

    flow = []
    for i, blocks in enumerate(page_blocks):
        flow.extend(render_blocks(blocks, st))
        if i < len(page_blocks) - 1:
            flow.append(PageBreak())
    doc.build(flow)
    return out_path
