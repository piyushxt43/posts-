#!/usr/bin/env python3
"""Generate 10 carousel images for 50 Cursor secrets."""

from __future__ import annotations

import base64
import concurrent.futures
import json
import os
import re
import time
import urllib.request
from pathlib import Path
from typing import Any

API_URL = "https://api.apiyi.com/v1/images/generations"
MODEL = "gpt-image-2-all"
ROOT = Path(__file__).resolve().parent
MAX_WORKERS = int(os.environ.get("CAROUSEL_WORKERS", "4"))
TIMEOUT_SECONDS = 300

STYLE_SYSTEM = """
Create a premium Instagram carousel slide in cream grid editorial style.
Canvas MUST be 3:4 vertical portrait.
Design language: cream grid-paper background, bold black sans-serif typography, one tasteful italic serif accent word, coral highlight tabs, thin black rules, UI cards, startup-operator aesthetic.
Keep text sharp, correctly spelled, and minimal.
No clutter, no lorem ipsum, no fake paragraphs, no social UI chrome.
When the slide is a cover or CTA, include a subtle Cursor logo mark in one corner (do not distort logo).
"""

CAROUSEL = {
    "title": "50 Cursor Secrets For Builders",
    "slug": "05_50_Cursor_Secrets_For_Builders",
    "angle": (
        "Cursor 2026 workflow secrets for developers and business builders: Composer 2.5, Agents Window, "
        "Plan Mode, .cursor/rules, hooks, skills, worktrees, cloud agents."
    ),
    "slides": [
        (
            "50 Cursor tricks. You're using 8.",
            "The 2026 builder workflow nobody teaches: from Composer 2 to cloud handoff.",
            "Cover slide, strong scroll-stopper, cream grid style, subtle Cursor logo top-right.",
        ),
        (
            "Secrets 1-5: Composer 2.5",
            "Use Composer 2.5 fast as your default. Escalate model strength only when risk is high.",
            "Operator dashboard card with risk tiers and token-efficiency callout.",
        ),
        (
            "Secrets 6-10: Agents Window",
            "Run parallel local + cloud agents from one view. Use new diff view before merge.",
            "Multi-agent board with three task columns and review panel.",
        ),
        (
            "Secrets 11-15: Plan Mode",
            "Shift+Tab before coding. Force unknowns, rollback paths, and verification steps first.",
            "Plan checklist card with risk map and rollback lanes.",
        ),
        (
            "Secrets 16-20: .cursor/rules",
            "Split rules by concern using .mdc files. Keep scopes narrow with globs and examples.",
            "Rule architecture diagram with folders and scoped globs.",
        ),
        (
            "Secrets 21-30: Hooks + Guardrails",
            "Use hooks for deterministic enforcement: secret-block, lint-fix, and test gates.",
            "Terminal style cards with pass/fail statuses and policy shield icon.",
        ),
        (
            "Secrets 31-35: Skills",
            "Encode repeatable workflows into SKILL.md packs for engineering and GTM execution.",
            "Skill cards (PR review, release notes, outreach brief, incident timeline).",
        ),
        (
            "Secrets 36-40: /worktree",
            "Parallelize safely with isolated checkouts. Merge smallest-risk branch first.",
            "Three worktree lanes feeding a single protected merge gate.",
        ),
        (
            "Secrets 41-50: Cloud Agents",
            "Move local to cloud for long runs, cloud to local for final verification.",
            "Cloud/local handoff flow with progress timeline and quality gate.",
        ),
        (
            "Comment AI",
            "Get the 10+ page PDF with all 50 secrets, rules/hooks snippets, and rollout playbook.",
            "Final CTA slide in cream grid style with subtle Cursor logo and coral CTA pill.",
        ),
    ],
}


def slugify(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("_")


def build_prompt(slide_index: int, slide: tuple[str, str, str]) -> str:
    headline, body, visual = slide
    page = f"{slide_index}/10"
    return f"""
3:4 vertical Instagram carousel slide.
{STYLE_SYSTEM}

Carousel topic: {CAROUSEL['title']}
Strategic angle: {CAROUSEL['angle']}
Slide number: {page}

Exact visible text to include:
Top label: CURSOR SECRETS - {slide_index:02d}
Main headline: {headline}
Supporting copy: {body}
Footer left: @piyush.glitch
Footer right: {page}

Visual direction:
{visual}

Rules:
- Keep layout premium, sparse, and readable.
- Max 3 compact support points as micro bullets if needed.
- Cream grid look is mandatory on every slide.
- Cursor logo appears only on cover and CTA style slides.
- No generic AI robot visuals. No spelling errors.
""".strip()


def post_json(url: str, payload: dict[str, Any], api_key: str) -> dict[str, Any]:
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
        return json.loads(resp.read().decode("utf-8"))


def download_url(url: str, path: Path) -> None:
    req = urllib.request.Request(url, headers={"User-Agent": "cursor-carousel-batch50-05/1.0"})
    with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
        path.write_bytes(resp.read())


def save_generation(result: dict[str, Any], path: Path) -> str:
    item = result["data"][0]
    if item.get("url"):
        download_url(item["url"], path)
        return item["url"]
    if item.get("b64_json"):
        raw = item["b64_json"]
        if raw.startswith("data:") and "," in raw:
            raw = raw.split(",", 1)[1]
        path.write_bytes(base64.b64decode(raw))
        return "b64_json"
    raise RuntimeError(f"No image output in API response: {result}")


def generate_one(api_key: str, slide_index: int, slide: tuple[str, str, str]) -> dict[str, Any]:
    folder = ROOT
    headline = slide[0]
    stem = slugify(headline)[:56]
    img_path = folder / f"{slide_index:02d}_{stem}.png"
    prompt_path = folder / f"{slide_index:02d}_{stem}.prompt.txt"
    prompt = build_prompt(slide_index, slide)
    prompt_path.write_text(prompt + "\n", encoding="utf-8")

    if img_path.exists() and img_path.stat().st_size > 120_000:
        return {"status": "skipped", "path": str(img_path)}

    payload = {"model": MODEL, "prompt": prompt, "response_format": "url"}
    last_error: Exception | None = None
    for attempt in range(1, 4):
        try:
            result = post_json(API_URL, payload, api_key)
            source = save_generation(result, img_path)
            return {"status": "ok", "path": str(img_path), "source": source}
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            wait = min(40, attempt * 6)
            print(f"[retry {attempt}/3] slide {slide_index}: {exc}; waiting {wait}s", flush=True)
            time.sleep(wait)
    raise RuntimeError(f"Slide {slide_index} failed after retries: {last_error}")


def main() -> int:
    api_key = os.environ.get("APIYI_API_KEY")
    if not api_key:
        print("ERROR: APIYI_API_KEY is required.", flush=True)
        return 2

    ROOT.mkdir(parents=True, exist_ok=True)
    plan = {
        "title": CAROUSEL["title"],
        "angle": CAROUSEL["angle"],
        "slides": [
            {"slide": i, "headline": s[0], "copy": s[1], "visual": s[2]}
            for i, s in enumerate(CAROUSEL["slides"], start=1)
        ],
    }
    (ROOT / "00_content_plan.json").write_text(json.dumps(plan, indent=2), encoding="utf-8")

    failures: list[str] = []
    print(f"Generating {len(CAROUSEL['slides'])} images in {ROOT}", flush=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        future_map = {
            pool.submit(generate_one, api_key, i, s): (i, s[0])
            for i, s in enumerate(CAROUSEL["slides"], start=1)
        }
        completed = 0
        for future in concurrent.futures.as_completed(future_map):
            completed += 1
            idx, headline = future_map[future]
            try:
                result = future.result()
                print(
                    f"[{completed:02d}/{len(CAROUSEL['slides'])}] {result['status'].upper()} slide {idx}: {headline}",
                    flush=True,
                )
            except Exception as exc:  # noqa: BLE001
                msg = f"slide {idx} failed: {exc}"
                failures.append(msg)
                print(f"[{completed:02d}/{len(CAROUSEL['slides'])}] FAILED {msg}", flush=True)

    manifest = {
        "carousel": CAROUSEL["slug"],
        "model": MODEL,
        "slides": len(CAROUSEL["slides"]),
        "failures": failures,
        "generated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    (ROOT / "manifest_images.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Done. Failures: {len(failures)}", flush=True)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
