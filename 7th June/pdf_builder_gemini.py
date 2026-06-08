# -*- coding: utf-8 -*-
"""Premium PDF renderer for the Gemini Pro guide.

Adds a vector Gemini sparkle logo, a designed cover page, colored stat cards,
feature-card grids, pill labels and two-column layouts on top of the cream/coral
@piyush.glitch brand.
"""

from __future__ import annotations

import math
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    Image,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

# Brand palette
CREAM = HexColor("#F4EEDE")
PAPER = HexColor("#FBF8F0")
CORAL = HexColor("#EF5E45")
TERRA = HexColor("#C45E3B")
INK = HexColor("#1B1A17")
GREY = HexColor("#6E6657")
CARD = HexColor("#F9E5DC")
CODE_BG = HexColor("#ECE7DB")
WHITE = HexColor("#FFFFFF")

# Gemini accent colors
G_BLUE = HexColor("#4285F4")
G_PURPLE = HexColor("#9168C0")
G_PINK = HexColor("#D96570")
G_GREEN = HexColor("#1EA45F")
G_YELLOW = HexColor("#E8A23D")

CARD_COLORS = [G_BLUE, G_GREEN, G_PINK, G_PURPLE, CORAL, G_YELLOW]

MARGIN = 0.55 * inch
CONTENT_W = letter[0] - 2 * MARGIN
COVER_TOP = 2.5 * inch


# --------------------------------------------------------------------------- #
# Vector Gemini sparkle
# --------------------------------------------------------------------------- #
def _star_path(canvas, cx, cy, r, inner=0.34):
    """Four-pointed concave sparkle path."""
    p = canvas.beginPath()
    ir = r * inner
    pts = []
    for i in range(4):
        a_tip = math.radians(90 - i * 90)
        pts.append((cx + r * math.cos(a_tip), cy + r * math.sin(a_tip)))
        a_val = a_tip - math.radians(45)
        pts.append((cx + ir * math.cos(a_val), cy + ir * math.sin(a_val)))
    p.moveTo(*pts[0])
    for x, y in pts[1:]:
        p.lineTo(x, y)
    p.close()
    return p


def draw_gemini_star(canvas, cx, cy, r, gradient=True, solid=None):
    """Draw a Gemini sparkle with a blue->purple->pink gradient fill."""
    canvas.saveState()
    path = _star_path(canvas, cx, cy, r)
    if gradient:
        canvas.clipPath(path, stroke=0, fill=0)
        canvas.linearGradient(
            cx - r, cy + r, cx + r, cy - r,
            (G_BLUE, G_PURPLE, G_PINK),
            (0.0, 0.55, 1.0),
            extend=True,
        )
    else:
        canvas.setFillColor(solid or CORAL)
        canvas.drawPath(path, fill=1, stroke=0)
    canvas.restoreState()


def _mini_star(canvas, cx, cy, r, color):
    canvas.saveState()
    path = _star_path(canvas, cx, cy, r)
    canvas.setFillColor(color)
    canvas.drawPath(path, fill=1, stroke=0)
    canvas.restoreState()


# --------------------------------------------------------------------------- #
# Page backgrounds
# --------------------------------------------------------------------------- #
def _footer(canvas, doc):
    canvas.setFillColor(GREY)
    canvas.setFont("Helvetica", 7)
    canvas.drawString(MARGIN, 0.34 * inch, "@piyush.glitch   |   Google Gemini Pro FREE - Activation & Tools Guide")
    canvas.drawRightString(letter[0] - MARGIN, 0.34 * inch, f"{doc.page}")


def _cover_bg(canvas, doc):
    w, h = letter
    canvas.saveState()
    canvas.setFillColor(CREAM)
    canvas.rect(0, 0, w, h, fill=1, stroke=0)

    # decorative mini sparkles
    _mini_star(canvas, MARGIN + 0.35 * inch, h - 0.95 * inch, 9, G_BLUE)
    _mini_star(canvas, w - MARGIN - 0.4 * inch, h - 1.15 * inch, 7, G_PINK)
    _mini_star(canvas, w - MARGIN - 1.4 * inch, h - 0.8 * inch, 5, G_GREEN)
    _mini_star(canvas, MARGIN + 1.3 * inch, h - 1.4 * inch, 5, G_YELLOW)

    # big hero star
    draw_gemini_star(canvas, w / 2, h - 1.5 * inch, 0.62 * inch)

    # kicker under star
    canvas.setFillColor(GREY)
    canvas.setFont("Helvetica-Bold", 10)
    canvas.drawCentredString(w / 2, h - 2.15 * inch, "G O O G L E   A I   P R O")

    # bottom accent
    canvas.setFillColor(CORAL)
    canvas.rect(0, 0, w, 6, fill=1, stroke=0)
    _footer(canvas, doc)
    canvas.restoreState()


def _bg(canvas, doc):
    w, h = letter
    canvas.saveState()
    canvas.setFillColor(CREAM)
    canvas.rect(0, 0, w, h, fill=1, stroke=0)
    # header band
    canvas.setFillColor(CORAL)
    canvas.rect(0, h - 7, w, 7, fill=1, stroke=0)
    canvas.setFillColor(TERRA)
    canvas.rect(0, h - 13, w * 0.28, 5, fill=1, stroke=0)
    # small sparkle top-right
    _mini_star(canvas, w - MARGIN - 6, h - 0.42 * inch, 7, G_PURPLE)
    canvas.setFillColor(GREY)
    canvas.setFont("Helvetica-Bold", 7.5)
    canvas.drawRightString(w - MARGIN - 18, h - 0.46 * inch, "GOOGLE AI PRO")
    # bottom accent
    canvas.setFillColor(CORAL)
    canvas.rect(0, 0, w, 5, fill=1, stroke=0)
    _footer(canvas, doc)
    canvas.restoreState()


# --------------------------------------------------------------------------- #
# Styles
# --------------------------------------------------------------------------- #
def _styles():
    ss = getSampleStyleSheet()
    return {
        "hero": ParagraphStyle("hero", parent=ss["Title"], fontName="Helvetica-Bold",
                               fontSize=27, textColor=INK, leading=30, alignment=1, spaceAfter=6),
        "herosub": ParagraphStyle("herosub", parent=ss["Normal"], fontName="Helvetica",
                                  fontSize=12, textColor=GREY, leading=16, alignment=1, spaceAfter=10),
        "h1": ParagraphStyle("h1", parent=ss["Title"], fontName="Helvetica-Bold",
                             fontSize=18, textColor=INK, leading=22, spaceAfter=4, alignment=0),
        "h2": ParagraphStyle("h2", parent=ss["Heading2"], fontName="Helvetica-Bold",
                             fontSize=11, textColor=CORAL, leading=14, spaceBefore=6, spaceAfter=4),
        "h3": ParagraphStyle("h3", parent=ss["Heading3"], fontName="Helvetica-Bold",
                             fontSize=10.5, textColor=INK, leading=13, spaceBefore=4, spaceAfter=3),
        "body": ParagraphStyle("b", parent=ss["Normal"], fontSize=9.6, leading=13.5,
                               textColor=INK, spaceAfter=5),
        "bullet": ParagraphStyle("bu", parent=ss["Normal"], fontSize=9.2, leading=12.6,
                                 textColor=INK, leftIndent=12, bulletIndent=4, spaceAfter=2.5),
        "caption": ParagraphStyle("cap", parent=ss["Normal"], fontSize=8, leading=10,
                                  textColor=GREY, spaceAfter=4, alignment=1),
        "code": ParagraphStyle("c", parent=ss["Code"], fontName="Courier", fontSize=8,
                               leading=11, textColor=INK),
        "th": ParagraphStyle("th", parent=ss["Normal"], fontName="Helvetica-Bold",
                             fontSize=8, textColor=WHITE, leading=10),
        "td": ParagraphStyle("td", parent=ss["Normal"], fontSize=8, leading=10.5, textColor=INK),
        "pill": ParagraphStyle("pill", parent=ss["Normal"], fontName="Helvetica-Bold",
                               fontSize=8, textColor=WHITE, leading=10, alignment=1),
        "statval": ParagraphStyle("sv", parent=ss["Normal"], fontName="Helvetica-Bold",
                                  fontSize=17, textColor=INK, leading=19, alignment=1),
        "statlabel": ParagraphStyle("sl", parent=ss["Normal"], fontSize=7.5, textColor=GREY,
                                    leading=9.5, alignment=1),
        "cardtitle": ParagraphStyle("ct", parent=ss["Normal"], fontName="Helvetica-Bold",
                                    fontSize=9.5, textColor=WHITE, leading=12),
        "cardbody": ParagraphStyle("cb", parent=ss["Normal"], fontSize=8.3, leading=11, textColor=INK),
    }


def _esc(text) -> str:
    s = str(text)
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# --------------------------------------------------------------------------- #
# Components
# --------------------------------------------------------------------------- #
def _table(headers, rows, st, col_widths=None):
    hdr = [Paragraph(_esc(h), st["th"]) for h in headers]
    data = [hdr] + [[Paragraph(_esc(c), st["td"]) for c in r] for r in rows]
    if not col_widths:
        col_widths = [CONTENT_W / len(headers)] * len(headers)
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), CORAL),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, PAPER]),
        ("GRID", (0, 0), (-1, -1), 0.35, HexColor("#D8CFBC")),
        ("LINEBELOW", (0, 0), (-1, 0), 0.8, TERRA),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 5.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5.5),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]))
    return t


def _code_block(text, st):
    body = Paragraph(_esc(text.strip()).replace("\n", "<br/>"), st["code"])
    outer = Table([[body]], colWidths=[CONTENT_W])
    outer.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CODE_BG),
        ("BOX", (0, 0), (-1, -1), 0.5, GREY),
        ("LINEBEFORE", (0, 0), (0, -1), 3, G_BLUE),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
    ]))
    return outer


def _callout(title, text, st, color=CORAL):
    body = Paragraph(f"<b>{_esc(title)}</b><br/>{text}", st["body"])
    t = Table([[body]], colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CARD),
        ("BOX", (0, 0), (-1, -1), 0.6, color),
        ("LINEBEFORE", (0, 0), (0, -1), 4, color),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
        ("LEFTPADDING", (0, 0), (-1, -1), 11),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    return t


def _pill(text, st, color=CORAL):
    p = Paragraph(_esc(text).upper(), st["pill"])
    t = Table([[p]], colWidths=[min(CONTENT_W, 0.16 * inch + 7 * len(text))])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), color),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("ROUNDEDCORNERS", [5, 5, 5, 5]),
    ]))
    return t


def _stat_cards(cards, st):
    """cards: list of {value, label, color}."""
    cells = []
    for c in cards:
        inner = Table(
            [[Paragraph(_esc(c["value"]), st["statval"])],
             [Paragraph(_esc(c["label"]), st["statlabel"])]],
            colWidths=[CONTENT_W / len(cards) - 8],
        )
        inner.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), WHITE),
            ("BOX", (0, 0), (-1, -1), 0.5, HexColor("#E2D9C7")),
            ("LINEABOVE", (0, 0), (-1, 0), 3, c.get("color", CORAL)),
            ("TOPPADDING", (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ]))
        cells.append(inner)
    outer = Table([cells], colWidths=[CONTENT_W / len(cards)] * len(cards))
    outer.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return outer


def _one_card(card, st):
    color = card.get("color", CORAL)
    title = Table([[Paragraph(_esc(card["title"]), st["cardtitle"])]],
                  colWidths=[CONTENT_W / 2 - 10])
    title.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), color),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    body = Table([[Paragraph(card["body"], st["cardbody"])]],
                 colWidths=[CONTENT_W / 2 - 10])
    body.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), WHITE),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    wrap = Table([[title], [body]], colWidths=[CONTENT_W / 2 - 10])
    wrap.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.5, HexColor("#E2D9C7")),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return wrap


def _cards_grid(cards, st):
    rows = []
    for i in range(0, len(cards), 2):
        pair = cards[i:i + 2]
        for j, c in enumerate(pair):
            c.setdefault("color", CARD_COLORS[(i + j) % len(CARD_COLORS)])
        cells = [_one_card(c, st) for c in pair]
        if len(cells) == 1:
            cells.append("")
        rows.append(cells)
    g = Table(rows, colWidths=[CONTENT_W / 2, CONTENT_W / 2])
    g.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return g


def _two_col_bullets(left, right, st):
    def col(items):
        flow = [Paragraph(_esc(it), st["bullet"], bulletText="-") for it in items]
        return flow
    t = Table([[col(left), col(right)]], colWidths=[CONTENT_W / 2 - 6, CONTENT_W / 2 - 6])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]))
    return t


def _image_block(path: Path, caption, st, max_h=4.0 * inch):
    flow = []
    if not path.exists():
        flow.append(Paragraph(f"<i>Image missing: {path.name}</i>", st["body"]))
        return flow
    img = Image(str(path))
    scale = min(CONTENT_W / img.imageWidth, max_h / img.imageHeight)
    img.drawWidth = img.imageWidth * scale
    img.drawHeight = img.imageHeight * scale
    t = Table([[img]], colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
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


def _divider():
    t = Table([[""]], colWidths=[CONTENT_W], rowHeights=[2])
    t.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, -1), 0.6, HexColor("#D8CFBC"))]))
    return t


# --------------------------------------------------------------------------- #
# Block renderer
# --------------------------------------------------------------------------- #
def render_blocks(blocks, st):
    flow = []
    for b in blocks:
        t = b["type"]
        if t == "hero":
            flow.append(Paragraph(b["text"], st["hero"]))
        elif t == "herosub":
            flow.append(Paragraph(b["text"], st["herosub"]))
        elif t == "heading":
            flow.append(Paragraph(b["text"], st["h1"]))
            flow.append(_divider())
            flow.append(Spacer(1, 6))
        elif t == "subhead":
            flow.append(Paragraph(b["text"], st["h2"]))
        elif t == "h3":
            flow.append(Paragraph(b["text"], st["h3"]))
        elif t == "prose":
            flow.append(Paragraph(b["text"], st["body"]))
        elif t == "bullets":
            if b.get("title"):
                flow.append(Paragraph(f"<b>{_esc(b['title'])}</b>", st["body"]))
            for item in b["items"]:
                flow.append(Paragraph(_esc(item), st["bullet"], bulletText="-"))
        elif t == "two_col_bullets":
            flow.append(_two_col_bullets(b["left"], b["right"], st))
            flow.append(Spacer(1, 4))
        elif t == "code":
            flow.append(_code_block(b["text"], st))
            flow.append(Spacer(1, 6))
        elif t == "table":
            cw = [w * inch for w in b["col_widths"]] if b.get("col_widths") else None
            flow.append(_table(b["headers"], b["rows"], st, cw))
            flow.append(Spacer(1, 6))
        elif t == "callout":
            flow.append(_callout(b["title"], b["text"], st, b.get("color", CORAL)))
            flow.append(Spacer(1, 6))
        elif t == "pill":
            flow.append(_pill(b["text"], st, b.get("color", CORAL)))
            flow.append(Spacer(1, 4))
        elif t == "stat_cards":
            flow.append(_stat_cards(b["cards"], st))
            flow.append(Spacer(1, 8))
        elif t == "cards_grid":
            flow.append(_cards_grid(b["cards"], st))
            flow.append(Spacer(1, 6))
        elif t == "divider":
            flow.append(_divider())
            flow.append(Spacer(1, 6))
        elif t == "image":
            flow.extend(_image_block(Path(b["path"]), b.get("caption", ""), st, b.get("max_height", 4.0 * inch)))
        elif t == "spacer":
            flow.append(Spacer(1, b.get("height", 8)))
    return flow


def build_pdf(out_path: Path, page_blocks: list, cover: bool = True) -> Path:
    st = _styles()
    doc = BaseDocTemplate(
        str(out_path), pagesize=letter,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=0.55 * inch, bottomMargin=0.6 * inch,
        title="Google Gemini Pro FREE - Activation & Tools Guide",
        author="@piyush.glitch",
    )
    cover_frame = Frame(
        MARGIN, doc.bottomMargin, CONTENT_W,
        letter[1] - doc.bottomMargin - COVER_TOP, id="cover",
    )
    main_frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
    doc.addPageTemplates([
        PageTemplate(id="cover", frames=[cover_frame], onPage=_cover_bg),
        PageTemplate(id="main", frames=[main_frame], onPage=_bg),
    ])

    flow = []
    pages = page_blocks
    if cover:
        flow.extend(render_blocks(pages[0], st))
        flow.append(NextPageTemplate("main"))
        flow.append(PageBreak())
        pages = page_blocks[1:]
    for i, blocks in enumerate(pages):
        flow.extend(render_blocks(blocks, st))
        if i < len(pages) - 1:
            flow.append(PageBreak())
    doc.build(flow)
    return out_path
