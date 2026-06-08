#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build 10-page operator PDFs for all 5th June carousels."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from content import CAROUSEL_MAP, CAROUSELS
from pdf_builder_rich import build_pdf
from pdf_pages import META, pages_for

ROOT = Path(__file__).resolve().parent


def build_one(carousel: dict) -> Path:
    slug = carousel["slug"]
    folder = ROOT / slug
    folder.mkdir(parents=True, exist_ok=True)
    pdf_name = META[slug]["pdf"]
    out = folder / pdf_name
    page_blocks = pages_for(slug)
    if len(page_blocks) != 10:
        raise ValueError(f"{slug}: expected 10 pages, got {len(page_blocks)}")
    build_pdf(out, page_blocks)
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("ids", nargs="*", help="Carousel id 01-10 (default: all)")
    args = parser.parse_args()

    specs = [CAROUSEL_MAP[cid] for cid in args.ids if cid in CAROUSEL_MAP] if args.ids else CAROUSELS
    if not specs:
        print("No matching carousels.", file=sys.stderr)
        return 1

    for c in specs:
        out = build_one(c)
        print(f"OK {out} ({out.stat().st_size:,} bytes, 10 pages)", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
