#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regenerate cover slides only (v2 AI Business style)."""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from cover_prompts import COVERS
from maker_loader import CAPTIONS, PDF_NAMES

ROOT = Path(__file__).resolve().parent
API_URL = "https://api.apiyi.com/v1/images/generations"
MODEL = "gpt-image-2-all"
TIMEOUT = 360


def post_json(url: str, payload: dict, api_key: str) -> dict:
    req = urllib.request.Request(
        url,
        json.dumps(payload).encode(),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return json.loads(r.read())


def save_image(result: dict, path: Path) -> None:
    item = result["data"][0]
    if item.get("url"):
        req = urllib.request.Request(item["url"], headers={"User-Agent": "5th-june-covers/2.0"})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            path.write_bytes(r.read())
        return
    b64 = item.get("b64_json", "")
    if "," in b64:
        b64 = b64.split(",", 1)[1]
    path.write_bytes(base64.b64decode(b64))


def run_one(api_key: str, spec: dict) -> str:
    slug = spec["slug"]
    folder = ROOT / slug
    folder.mkdir(parents=True, exist_ok=True)
    out = folder / spec["filename"]
    cap = CAPTIONS.get(slug, "")
    if cap:
        (folder / "caption.txt").write_text(cap, encoding="utf-8")
    save_image(
        post_json(API_URL, {"model": MODEL, "prompt": spec["prompt"], "response_format": "url"}, api_key),
        out,
    )
    return f"{slug}/{spec['filename']}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("nums", nargs="*", help="Carousel number 01-10 (default: all)")
    parser.add_argument("--workers", type=int, default=10)
    args = parser.parse_args()

    api_key = os.environ.get("APIYI_API_KEY")
    if not api_key:
        print("ERROR: Set APIYI_API_KEY environment variable.", file=sys.stderr)
        return 2
    specs = COVERS
    if args.nums:
        want = {n.zfill(2) for n in args.nums}
        specs = [c for c in COVERS if c["slug"][:2] in want]

    workers = min(args.workers, len(specs))
    print(f"Regenerating {len(specs)} covers ({workers} workers)...", flush=True)

    ok = fail = 0
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futs = {pool.submit(run_one, api_key, s): s["slug"] for s in specs}
        for fut in as_completed(futs):
            slug = futs[fut]
            try:
                path = fut.result()
                ok += 1
                print(f"OK {path}", flush=True)
            except Exception as e:
                fail += 1
                print(f"FAIL {slug}: {e}", flush=True)

    print(f"\nDone: {ok} ok, {fail} failed.", flush=True)
    return 1 if fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
