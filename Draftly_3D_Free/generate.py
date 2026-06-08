#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Draftly 3-slide carousel images."""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from content import CAROUSEL_MAP, CAROUSELS

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
        req = urllib.request.Request(item["url"], headers={"User-Agent": "draftly-3d-free/1.0"})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            path.write_bytes(r.read())
        return
    b64 = item.get("b64_json", "")
    if "," in b64:
        b64 = b64.split(",", 1)[1]
    path.write_bytes(base64.b64decode(b64))


def run_job(api_key: str, slug: str, folder: Path, filename: str, prompt: str) -> tuple[str, str]:
    out = folder / filename
    save_image(
        post_json(API_URL, {"model": MODEL, "prompt": prompt, "response_format": "url"}, api_key),
        out,
    )
    return slug, filename


def collect_jobs(specs: list, force: bool) -> list:
    jobs = []
    for spec in specs:
        folder = ROOT / spec["slug"]
        folder.mkdir(parents=True, exist_ok=True)
        cap = spec["caption"]
        if len(cap) > 2200:
            cap = cap[:2197] + "..."
        (folder / "caption.txt").write_text(cap, encoding="utf-8")
        for filename, prompt in spec["slides"]:
            out = folder / filename
            if out.exists() and not force and out.stat().st_size > 50_000:
                continue
            jobs.append((spec["slug"], folder, filename, prompt))
    return jobs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("ids", nargs="*", help="01 (default: all)")
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    api_key = os.environ.get("APIYI_API_KEY")
    if not api_key:
        print("ERROR: Set APIYI_API_KEY environment variable.", file=sys.stderr)
        return 2
    specs = [CAROUSEL_MAP[c] for c in args.ids if c in CAROUSEL_MAP] if args.ids else CAROUSELS
    jobs = collect_jobs(specs, args.force)
    if not jobs:
        print("All slides exist.", flush=True)
        return 0
    print(f"Generating {len(jobs)} slides...", flush=True)
    ok = fail = 0
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futs = {pool.submit(run_job, api_key, *j): (j[0], j[2]) for j in jobs}
        for fut in as_completed(futs):
            slug, fn = futs[fut]
            try:
                fut.result()
                ok += 1
                print(f"OK {slug}/{fn}", flush=True)
            except Exception as e:
                fail += 1
                print(f"FAIL {slug}/{fn}: {e}", flush=True)
    print(f"Done: {ok} ok, {fail} fail", flush=True)
    return 1 if fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
