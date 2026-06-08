#!/usr/bin/env python3
"""
Render branded, detailed bonus-guide PDFs for all 10 carousels.

Design language matches the carousels: cream grid-paper background, bold black
sans-serif headlines with one italic-serif accent word, coral numbered tabs,
soft callout boxes, and a @piyush.glitch footer.

Run with the project's venv:
    ./.venv/bin/python build_pdfs.py
"""

from __future__ import annotations

from pathlib import Path

from reportlab.lib.colors import Color, HexColor, white
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Flowable,
    Frame,
    KeepTogether,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.lib.styles import ParagraphStyle

from pdf_content import CONTENT
from expand_pdf_content import merge_content

CONTENT = merge_content(CONTENT)

ROOT = Path(__file__).resolve().parent / "AI_Business_Carousels"

# ---- Brand palette -------------------------------------------------------
CREAM = HexColor("#F4EEDE")
GRID = HexColor("#E7DEC6")
CARD = HexColor("#FCFAF3")
INK = HexColor("#1B1A17")
MUTED = HexColor("#6E6657")
CORAL = HexColor("#EF5E45")
CORAL_SOFT = HexColor("#FBE0D8")
LINE = HexColor("#D8CFB8")
GREEN = HexColor("#2E7D5B")

PAGE_W, PAGE_H = letter
MARGIN = 0.72 * inch
CONTENT_W = PAGE_W - 2 * MARGIN

# ---- Paragraph styles ----------------------------------------------------
STY_INTRO = ParagraphStyle(
    "intro", fontName="Helvetica", fontSize=11.5, leading=17, textColor=INK, spaceAfter=4,
)
STY_BODY = ParagraphStyle(
    "body", fontName="Helvetica", fontSize=10.5, leading=15.5, textColor=INK, spaceAfter=6,
)
STY_SECTION = ParagraphStyle(
    "section", fontName="Helvetica-Bold", fontSize=16, leading=19, textColor=INK,
)
STY_BULLET_LEAD = ParagraphStyle(
    "blead", fontName="Helvetica-Bold", fontSize=10.5, leading=15, textColor=INK,
)
STY_BULLET = ParagraphStyle(
    "bullet", fontName="Helvetica", fontSize=10.5, leading=15, textColor=INK,
)
STY_PANEL_TITLE = ParagraphStyle(
    "ptitle", fontName="Helvetica-Bold", fontSize=12.5, leading=15, textColor=INK,
)
STY_PANEL_ITEM = ParagraphStyle(
    "pitem", fontName="Helvetica", fontSize=10, leading=14.5, textColor=INK,
)
STY_CALLOUT_TITLE = ParagraphStyle(
    "ctitle", fontName="Helvetica-Bold", fontSize=11, leading=14, textColor=CORAL,
)
STY_CALLOUT = ParagraphStyle(
    "callout", fontName="Helvetica", fontSize=10.5, leading=15.5, textColor=INK,
)
STY_GLOSS_TERM = ParagraphStyle(
    "gterm", fontName="Helvetica-Bold", fontSize=10, leading=13.5, textColor=CORAL,
)
STY_GLOSS_DEF = ParagraphStyle(
    "gdef", fontName="Helvetica", fontSize=10, leading=13.5, textColor=INK,
)
STY_CODE = ParagraphStyle(
    "code", fontName="Courier", fontSize=8.5, leading=11.5, textColor=INK,
)
STY_CODE_CAP = ParagraphStyle(
    "codec", fontName="Helvetica-Bold", fontSize=9, leading=11, textColor=MUTED, spaceAfter=4,
)
STY_PRO = ParagraphStyle(
    "pro", fontName="Helvetica", fontSize=10, leading=14.5, textColor=INK,
)
STY_PRO_TITLE = ParagraphStyle(
    "protitle", fontName="Helvetica-Bold", fontSize=10, leading=13, textColor=GREEN,
)
STY_SLIDE = ParagraphStyle(
    "slide", fontName="Helvetica", fontSize=10, leading=14, textColor=INK, leftIndent=12,
)
STY_EYEBROW = ParagraphStyle(
    "eyebrow", fontName="Helvetica-Bold", fontSize=10.5, leading=13, textColor=CORAL,
    spaceAfter=10,
)


def esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ---- Background + footer painters ---------------------------------------
def paint_background(canvas):
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


def draw_footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.8)
    canvas.line(MARGIN, 0.55 * inch, PAGE_W - MARGIN, 0.55 * inch)
    canvas.setFont("Helvetica-Bold", 8.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(MARGIN, 0.4 * inch, "@piyush.glitch")
    canvas.setFont("Helvetica", 8.5)
    canvas.drawRightString(PAGE_W - MARGIN, 0.4 * inch, "Bonus Guide  -  Comment AI for the full breakdown")
    canvas.setFont("Helvetica-Bold", 8.5)
    canvas.drawCentredString(PAGE_W / 2, 0.4 * inch, str(doc.page))
    canvas.restoreState()


def on_content_page(canvas, doc):
    paint_background(canvas)
    draw_footer(canvas, doc)


def on_cover_page(canvas, doc):
    paint_background(canvas)


# ---- Custom flowables ----------------------------------------------------
class SectionHeader(Flowable):
    """A coral numbered tab + heading + underline rule."""

    def __init__(self, number: str, title: str, width: float):
        super().__init__()
        self.number = number
        self.title = title
        self.width = width
        self.height = 30

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        return availWidth, self.height

    def draw(self):
        c = self.canv
        tab_w, tab_h = 26, 20
        c.setFillColor(CORAL)
        c.roundRect(0, 6, tab_w, tab_h, 4, stroke=0, fill=1)
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 11)
        c.drawCentredString(tab_w / 2, 11.5, self.number)
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 15)
        c.drawString(tab_w + 12, 11, self.title)
        c.setStrokeColor(LINE)
        c.setLineWidth(0.8)
        c.line(0, 1, self.width, 1)


class Divider(Flowable):
    def __init__(self, width=CONTENT_W, color=LINE, thickness=0.8, pad=4):
        super().__init__()
        self.width = width
        self.color = color
        self.thickness = thickness
        self.height = pad

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        return availWidth, self.height

    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.thickness)
        self.canv.line(0, self.height / 2, self.width, self.height / 2)


def bullets_table(bullets) -> Table:
    rows = []
    for lead, text in bullets:
        marker = Paragraph('<font color="#EF5E45">&#9632;</font>', STY_BULLET)
        cell = Paragraph(f'<b>{lead}.</b> {text}', STY_BULLET)
        rows.append([marker, cell])
    t = Table(rows, colWidths=[16, CONTENT_W - 16])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ]))
    return t


def callout_box(title: str, text: str) -> Table:
    inner = [
        [Paragraph(title.upper(), STY_CALLOUT_TITLE)],
        [Paragraph(text, STY_CALLOUT)],
    ]
    t = Table(inner, colWidths=[CONTENT_W - 24])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CORAL_SOFT),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
        ("TOPPADDING", (0, 0), (0, 0), 12),
        ("BOTTOMPADDING", (0, 0), (0, 0), 2),
        ("TOPPADDING", (0, 1), (0, 1), 0),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 12),
        ("LINEBEFORE", (0, 0), (0, -1), 3, CORAL),
    ]))
    return t


def panel(title: str, items, numbered: bool, accent: Color) -> Table:
    item_style = ParagraphStyle(
        "panelitem_hang", parent=STY_PANEL_ITEM, leftIndent=18, firstLineIndent=-18,
        spaceBefore=2, spaceAfter=2,
    )
    rows = [[Paragraph(title.upper(), STY_PANEL_TITLE)]]
    for i, item in enumerate(items, start=1):
        if numbered:
            marker = f'<font color="#EF5E45"><b>{i}.</b></font>&nbsp;&nbsp;'
        else:
            mk = "&#10003;" if accent == GREEN else "&#10007;"
            col = "#2E7D5B" if accent == GREEN else "#EF5E45"
            marker = f'<font color="{col}"><b>{mk}</b></font>&nbsp;&nbsp;'
        rows.append([Paragraph(marker + item, item_style)])
    t = Table(rows, colWidths=[CONTENT_W])
    style = [
        ("BACKGROUND", (0, 0), (-1, -1), CARD),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 16),
        ("RIGHTPADDING", (0, 0), (-1, -1), 16),
        ("TOPPADDING", (0, 0), (-1, 0), 12),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 7),
        ("TOPPADDING", (0, 1), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 2),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 12),
        ("LINEABOVE", (0, 0), (-1, 0), 2, accent),
        ("BOX", (0, 0), (-1, -1), 0.8, LINE),
    ]
    t.setStyle(TableStyle(style))
    return t


def glossary_table(items) -> Table:
    rows = []
    for term, definition in items:
        rows.append([Paragraph(term, STY_GLOSS_TERM), Paragraph(definition, STY_GLOSS_DEF)])
    t = Table(rows, colWidths=[1.45 * inch, CONTENT_W - 1.45 * inch])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("LINEBELOW", (0, 0), (-1, -2), 0.5, LINE),
    ]))
    return t


def code_block(caption: str, code: str) -> Table:
    rows = [[Paragraph(caption.upper(), STY_CODE_CAP)]]
    for line in code.split("\n"):
        rows.append([Paragraph(
            f"<font face='Courier' size='8.5'>{esc(line) if line else ' '}</font>",
            STY_CODE,
        )])
    inner = Table(rows, colWidths=[CONTENT_W - 28])
    inner.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), HexColor("#EDE8DC")),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, 0), 10),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 10),
        ("TOPPADDING", (0, 1), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -2), 0),
        ("BOX", (0, 0), (-1, -1), 0.8, LINE),
    ]))
    return inner


def pro_tip_box(title: str, text: str) -> Table:
    inner = [
        [Paragraph(title.upper(), STY_PRO_TITLE)],
        [Paragraph(text, STY_PRO)],
    ]
    t = Table(inner, colWidths=[CONTENT_W - 24])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), HexColor("#E8F5EE")),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
        ("TOPPADDING", (0, 0), (0, 0), 10),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 10),
        ("LINEABOVE", (0, 0), (-1, 0), 2, GREEN),
        ("BOX", (0, 0), (-1, -1), 0.8, LINE),
    ]))
    return t


def carousel_recap_table(slides) -> Table:
    rows = []
    for num, title, summary in slides:
        cell = Paragraph(
            f'<font color="#EF5E45"><b>Slide {num}</b></font> &nbsp; '
            f'<b>{esc(title)}</b> - {esc(summary)}',
            STY_SLIDE,
        )
        rows.append([cell])
    t = Table(rows, colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CARD),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("BOX", (0, 0), (-1, -1), 0.8, LINE),
    ]))
    return t


def faq_table(items) -> Table:
    rows = []
    for question, answer in items:
        rows.append([
            Paragraph(f"<b>{esc(question)}</b>", STY_BODY),
            Paragraph(esc(answer), STY_BODY),
        ])
    t = Table(rows, colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("LINEBELOW", (0, 0), (-1, -2), 0.5, LINE),
    ]))
    return t


def render_section(sec: dict) -> list:
    """Build flowables for one chapter - flows across pages naturally."""
    block = [
        SectionHeader(sec["tab"], sec["title"], CONTENT_W),
        Spacer(1, 8),
    ]
    for para in sec.get("body", []):
        block.append(Paragraph(para, STY_BODY))
    if sec.get("bullets"):
        block.append(Spacer(1, 2))
        block.append(bullets_table(sec["bullets"]))
    if sec.get("code"):
        block.append(Spacer(1, 8))
        block.append(code_block(sec["code"]["caption"], sec["code"]["lines"]))
    if sec.get("pro_tip"):
        block.append(Spacer(1, 8))
        block.append(pro_tip_box(sec["pro_tip"]["title"], sec["pro_tip"]["text"]))
    block.append(Spacer(1, 14))
    return block


# ---- Cover --------------------------------------------------------------
def draw_cover(canvas, kicker: str, title: str, subtitle: str):
    canvas.saveState()
    left = MARGIN
    # Top kicker tab
    canvas.setFont("Helvetica-Bold", 10)
    tab_w = canvas.stringWidth(kicker, "Helvetica-Bold", 10) + 20
    canvas.setFillColor(CORAL)
    canvas.roundRect(left, PAGE_H - 1.45 * inch, tab_w, 22, 5, stroke=0, fill=1)
    canvas.setFillColor(white)
    canvas.drawString(left + 10, PAGE_H - 1.45 * inch + 7, kicker)

    # Headline (wrapped manually, large)
    canvas.setFillColor(INK)
    words = title.split()
    lines = []
    cur = ""
    max_chars = 17
    for w in words:
        if len(cur) + len(w) + 1 <= max_chars:
            cur = (cur + " " + w).strip()
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    y = PAGE_H - 2.5 * inch
    canvas.setFont("Helvetica-Bold", 40)
    for ln in lines:
        canvas.drawString(left, y, ln)
        y -= 44

    # Coral underline accent
    canvas.setFillColor(CORAL)
    canvas.rect(left, y + 18, 2.2 * inch, 6, stroke=0, fill=1)
    y -= 18

    # Subtitle
    canvas.setFillColor(MUTED)
    canvas.setFont("Helvetica", 13.5)
    sub_words = subtitle.split()
    cur = ""
    sub_lines = []
    for w in sub_words:
        if len(cur) + len(w) + 1 <= 56:
            cur = (cur + " " + w).strip()
        else:
            sub_lines.append(cur)
            cur = w
    if cur:
        sub_lines.append(cur)
    for ln in sub_lines:
        canvas.drawString(left, y, ln)
        y -= 19

    # Bottom meta
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.8)
    canvas.line(left, 1.25 * inch, PAGE_W - MARGIN, 1.25 * inch)
    canvas.setFillColor(INK)
    canvas.setFont("Helvetica-Bold", 11)
    canvas.drawString(left, 0.95 * inch, "@piyush.glitch")
    canvas.setFillColor(MUTED)
    canvas.setFont("Helvetica", 10)
    canvas.drawString(left, 0.78 * inch, "Save this. Comment AI on the post for the full breakdown.")
    canvas.restoreState()


class CoverFlowable(Flowable):
    def __init__(self, kicker, title, subtitle):
        super().__init__()
        self.kicker = kicker
        self.title = title
        self.subtitle = subtitle
        self.width = CONTENT_W
        self.height = PAGE_H - 2 * MARGIN

    def wrap(self, availWidth, availHeight):
        return availWidth, availHeight

    def draw(self):
        # translate to absolute page coords
        self.canv.saveState()
        self.canv.translate(-MARGIN, -MARGIN)
        draw_cover(self.canv, self.kicker, self.title, self.subtitle)
        self.canv.restoreState()


# ---- Build one PDF -------------------------------------------------------
def build_pdf(path: Path, data: dict):
    doc = BaseDocTemplate(
        str(path),
        pagesize=letter,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=0.75 * inch,
        title=data["title"],
        author="@piyush.glitch",
    )
    frame = Frame(MARGIN, 0.75 * inch, CONTENT_W, PAGE_H - MARGIN - 0.75 * inch, id="main")
    doc.addPageTemplates([
        PageTemplate(id="cover", frames=[frame], onPage=on_cover_page),
        PageTemplate(id="content", frames=[frame], onPage=on_content_page),
    ])

    story = []
    story.append(NextPageTemplate("content"))
    story.append(CoverFlowable(data["kicker"], data["title"], data["subtitle"]))
    story.append(PageBreak())

    # Overview
    story.append(Paragraph("THE BIG IDEA", STY_EYEBROW))
    story.append(Paragraph(data["intro"], STY_INTRO))
    story.append(Spacer(1, 10))
    story.append(callout_box(data["callout"]["title"], data["callout"]["text"]))
    story.append(Spacer(1, 14))

    # Carousel recap
    if data.get("carousel_slides"):
        story.append(Paragraph("WHAT THIS POST COVERS", STY_EYEBROW))
        story.append(Paragraph(
            "Eight slides walk you through the core ideas. This PDF goes much deeper with setup "
            "templates, code patterns, pro moves and tricks most teams discover only after months of trial.",
            STY_BODY,
        ))
        story.append(Spacer(1, 8))
        story.append(carousel_recap_table(data["carousel_slides"]))
        story.append(Spacer(1, 16))
        story.append(PageBreak())

    # Chapters
    story.append(Paragraph("DEEP DIVE", STY_EYEBROW))
    story.append(Spacer(1, 6))
    for sec in data["sections"]:
        story.extend(render_section(sec))

    # Hidden tricks
    if data.get("hidden_tricks"):
        story.append(PageBreak())
        story.append(Paragraph("HIDDEN TRICKS MOST PEOPLE MISS", STY_EYEBROW))
        story.append(Paragraph(
            "These are not in the carousel slides. Operators and senior builders use them daily.",
            STY_BODY,
        ))
        story.append(Spacer(1, 8))
        story.append(panel("Pro tricks and shortcuts", data["hidden_tricks"], numbered=True, accent=CORAL))
        story.append(Spacer(1, 14))

    # Playbook + mistakes
    story.append(PageBreak())
    story.append(Paragraph("IMPLEMENTATION", STY_EYEBROW))
    story.append(Spacer(1, 6))
    story.append(panel("Quick-start playbook", data["playbook"], numbered=True, accent=GREEN))
    story.append(Spacer(1, 14))
    story.append(panel("Mistakes to avoid", data["mistakes"], numbered=False, accent=CORAL))
    story.append(Spacer(1, 14))

    # FAQ
    if data.get("faq"):
        story.append(PageBreak())
        story.append(Paragraph("FAQ", STY_EYEBROW))
        story.append(Paragraph(
            "Answers to what people ask once they try to implement this inside a real team.",
            STY_BODY,
        ))
        story.append(Spacer(1, 8))
        story.append(faq_table(data["faq"]))
        story.append(Spacer(1, 14))

    # Closing notes (extra page for action items)
    if data.get("closing_notes"):
        story.append(PageBreak())
        story.append(Paragraph("YOUR NEXT STEPS", STY_EYEBROW))
        for note in data["closing_notes"]:
            story.append(Paragraph(note, STY_BODY))
        story.append(Spacer(1, 14))

    # Glossary
    story.append(PageBreak())
    story.append(Paragraph("KEY TERMS", STY_EYEBROW))
    story.append(glossary_table(data["glossary"]))
    story.append(Spacer(1, 20))
    story.append(callout_box(
        "Save this guide",
        "Comment AI on the Instagram post if you want the next playbook in this series. "
        "Follow @piyush.glitch for more AI-for-business breakdowns you can actually use.",
    ))

    doc.build(story)
    return doc.page


def main() -> int:
    built = 0
    for slug, data in CONTENT.items():
        if "/" in slug:
            folder = Path(__file__).resolve().parent / slug
        else:
            folder = ROOT / slug
        if not folder.exists():
            print(f"SKIP missing folder: {folder}")
            continue
        out_name = data.get("pdf_filename", "09_bonus_guide.pdf")
        out = folder / out_name
        pages = build_pdf(out, data)
        size_kb = out.stat().st_size / 1024
        print(f"OK  {slug}: {out.name} ({pages} pages, {size_kb:.0f} KB)")
        built += 1
    print(f"\nBuilt {built} PDFs in {ROOT}")
    return 0 if built == len(CONTENT) else 1


if __name__ == "__main__":
    raise SystemExit(main())
