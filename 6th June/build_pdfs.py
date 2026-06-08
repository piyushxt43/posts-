#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build dense operator PDFs (no slide prompt dumps)."""

from __future__ import annotations

import argparse
import sys

from content import CAROUSEL_MAP, CAROUSELS
from pdf_guides import build_pdf_for


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("ids", nargs="*", help="01-05")
    args = parser.parse_args()
    specs = [CAROUSEL_MAP[c] for c in args.ids if c in CAROUSEL_MAP] if args.ids else CAROUSELS
    if not specs:
        print("No match", file=sys.stderr)
        return 1
    for c in specs:
        out = build_pdf_for(c)
        print(f"OK {out} ({out.stat().st_size:,} bytes)", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
