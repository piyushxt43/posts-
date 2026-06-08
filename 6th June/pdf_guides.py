# -*- coding: utf-8 -*-
"""Dense full-page operator PDFs - advanced depth beyond carousel."""

from __future__ import annotations

from pathlib import Path

from content import CAROUSELS
from pdf_builder_rich import build_pdf
from pdf_content.agents import PAGES as AGENTS_PAGES
from pdf_content.claude_gpt import PAGES as CLAUDE_GPT_PAGES
from pdf_content.higgsfield import PAGES as HIGGSFIELD_PAGES
from pdf_content.omni import PAGES as OMNI_PAGES
from pdf_content.plugins import PAGES as PLUGINS_PAGES

ROOT = Path(__file__).resolve().parent

SLUG_PAGES = {
    "01_Top_10_Claude_Plugins_June": PLUGINS_PAGES,
    "02_10_Claude_Agents_You_Dont_Know": AGENTS_PAGES,
    "03_Claude_vs_GPT_Different_Angles": CLAUDE_GPT_PAGES,
    "04_Google_Omni_Claude_Bridge": OMNI_PAGES,
    "05_Is_Higgsfield_MCP_Worth_It": HIGGSFIELD_PAGES,
}


def pages_for(slug: str) -> list:
    return SLUG_PAGES[slug]


def build_pdf_for(carousel: dict) -> Path:
    folder = ROOT / carousel["slug"]
    folder.mkdir(parents=True, exist_ok=True)
    out = folder / carousel["pdf_name"]
    build_pdf(out, pages_for(carousel["slug"]))
    return out


def build_all() -> list[Path]:
    return [build_pdf_for(c) for c in CAROUSELS]
