#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate carousel 04 (10 slides) for 50 GitHub repos AI operators."""

from __future__ import annotations

import base64
import concurrent.futures
import json
import os
import re
import sys
import time
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent / "50_Series_Carousels" / "04_50_GitHub_Repos_AI_Operators"
API_URL = "https://api.apiyi.com/v1/images/generations"
MODEL = "gpt-image-2-all"
MAX_WORKERS = int(os.environ.get("CAROUSEL_WORKERS", "20"))
TIMEOUT = 300

BASE_STYLE = """
Premium Instagram carousel slide. STRICT 3:4 vertical portrait aspect ratio (1080x1440 feel).
Reference style: @piyush.glitch posts 01-15.
Cream grid paper or editorial blue-sky portrait background, huge confident typography,
bold black sans-serif with one elegant italic serif accent word, coral highlight tabs
and clean card layout. Crisp readable text only, no lorem ipsum.
No watermarks. No Instagram UI.
Footer text: @piyush.glitch bottom-left and page marker bottom-right (x/10).
"""

COVER_STYLE = """
COVER SLIDE:
- Scroll-stopping hook, high contrast, big 3-5 line headline.
- Build urgency and operator vibe. Include GitHub-inspired visual cues.
- Top micro label: AI FOR BUSINESS - 50 SERIES.
"""

INTERIOR_STYLE = """
INTERIOR SLIDES:
- Cream grid background, clean content hierarchy.
- Top-left small label: AI FOR BUSINESS - 50 SERIES.
- Use table/card layout with exactly 5 repo rows for list slides.
- Keep text sharply readable and correctly spelled.
"""

CAROUSEL: dict[str, Any] = {
    "title": "50 GitHub Repos AI Operators Use",
    "slug": "04_50_GitHub_Repos_AI_Operators",
    "angle": (
        "Real repositories for Claude, MCP, agent frameworks, Cursor/coding workflows, "
        "automation, evals, and AI business operations."
    ),
    "slides": [
        (
            "50 GitHub repos AI operators hide from you",
            "Skip tool tourism. Build your AI stack from real open-source repos.",
            "COVER: giant bold headline with word 'hide' in italic serif coral highlight. "
            "Editorial operator desk, floating GitHub-style repo cards and pipeline map.",
        ),
        (
            "Claude Foundations (5 Repos)",
            "anthropics/claude-code | anthropics/anthropic-sdk-python | anthropics/anthropic-sdk-typescript | "
            "anthropics/claude-code-action | anthropics/claude-plugins",
            "Render as 5-row repo table with short tags: CLI agent, Python SDK, TS SDK, GitHub Action, plugins.",
        ),
        (
            "MCP Core Stack (5 Repos)",
            "modelcontextprotocol/modelcontextprotocol | modelcontextprotocol/servers | "
            "modelcontextprotocol/typescript-sdk | modelcontextprotocol/python-sdk | modelcontextprotocol/inspector",
            "Render as 5-row table with short tags: spec, reference servers, TS SDK, Python SDK, testing inspector.",
        ),
        (
            "MCP Ecosystem Lists (5 Repos)",
            "github/github-mcp-server | punkpeye/awesome-mcp-servers | wong2/awesome-mcp-servers | "
            "open-webui/mcpo | mcp-use/mcp-use",
            "Render as 5-row table with short tags: official GitHub MCP, curated lists, MCP gateway, MCP in Python agents.",
        ),
        (
            "Agent Frameworks (5 Repos)",
            "langchain-ai/langgraph | crewAIInc/crewAI | microsoft/autogen | ag2ai/ag2 | huggingface/smolagents",
            "Render as 5-row table with short tags: graph agents, role crews, multi-agent, AutoGen successor, lightweight agents.",
        ),
        (
            "Coding Agents + Cursor Layer (5 Repos)",
            "continue-revolution/continue | Aider-AI/aider | block/goose | All-Hands-AI/OpenHands | "
            "PatrickJS/awesome-cursorrules",
            "Render as 5-row table with short tags: IDE agent, git-native coder, extensible agent, autonomous dev, Cursor rules.",
        ),
        (
            "Automation Orchestration (5 Repos)",
            "n8n-io/n8n | activepieces/activepieces | windmill-labs/windmill | temporalio/temporal | prefecthq/prefect",
            "Render as 5-row table with short tags: workflow automation, no-code flows, scripts+flows, durable orchestration, Python workflows.",
        ),
        (
            "Eval + Observability (5 Repos)",
            "langfuse/langfuse | Arize-ai/phoenix | promptfoo/promptfoo | confident-ai/deepeval | truera/trulens",
            "Render as 5-row table with short tags: tracing, LLM observability, eval tests, benchmark suite, quality checks.",
        ),
        (
            "Data + Retrieval Backbone (5 Repos)",
            "qdrant/qdrant | milvus-io/milvus | weaviate/weaviate | run-llama/llama_index | deepset-ai/haystack",
            "Render as 5-row table with short tags: vector DB, vector search, hybrid retrieval, RAG framework, retrieval pipelines.",
        ),
        (
            "Comment AI for all 50 + setup notes",
            "10 bonus repos + setup playbook in the 10+ page PDF. Build faster, cheaper, and safer.",
            "Premium CTA slide with strong coral Comment AI button, repo cards in background, clean high-end finish.",
        ),
    ],
}


def slugify(text: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "_", text.strip()).strip("_")[:64]


def build_prompt(idx: int, slide: tuple[str, str, str]) -> str:
    headline, body, visual = slide
    page = f"{idx}/10"
    style = f"{BASE_STYLE}\n{COVER_STYLE}" if idx == 1 else f"{BASE_STYLE}\n{INTERIOR_STYLE}"
    return f"""
3:4 vertical Instagram carousel slide.
{style}

Topic: {CAROUSEL['title']}
Angle: {CAROUSEL['angle']}
Slide: {page}

Headline (render exactly): {headline}
Body text (render exactly): {body}
Footer left: @piyush.glitch
Footer right: {page}

Visual direction:
{visual}
""".strip()


def post_json(payload: dict, api_key: str) -> dict:
    req = urllib.request.Request(
        API_URL,
        json.dumps(payload).encode(),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return json.loads(resp.read())


def save_image(result: dict, path: Path) -> None:
    item = result["data"][0]
    if item.get("url"):
        req = urllib.request.Request(item["url"], headers={"User-Agent": "batch50-04/1.0"})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            path.write_bytes(r.read())
        return
    b64 = item.get("b64_json", "")
    if "," in b64:
        b64 = b64.split(",", 1)[1]
    path.write_bytes(base64.b64decode(b64))


def job(api_key: str, idx: int, slide: tuple[str, str, str], force: bool) -> str:
    ROOT.mkdir(parents=True, exist_ok=True)
    name = f"{idx:02d}_{slugify(slide[0])}.png"
    out = ROOT / name
    if not force and out.exists() and out.stat().st_size > 100_000:
        return "skipped"
    for attempt in range(3):
        try:
            result = post_json(
                {"model": MODEL, "prompt": build_prompt(idx, slide), "response_format": "url"},
                api_key,
            )
            save_image(result, out)
            return "ok"
        except Exception:
            if attempt == 2:
                raise
            time.sleep(5 * (attempt + 1))
    return "ok"


def main() -> int:
    api_key = os.environ.get("APIYI_API_KEY")
    if not api_key:
        print("Set APIYI_API_KEY", file=sys.stderr)
        return 2

    force = "--force" in sys.argv
    slides = list(enumerate(CAROUSEL["slides"], 1))
    print(f"Generating {len(slides)} slides in {ROOT}", flush=True)
    failures: list[str] = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(job, api_key, idx, slide, force): idx for idx, slide in slides}
        done = 0
        for fut in concurrent.futures.as_completed(futures):
            idx = futures[fut]
            done += 1
            try:
                st = fut.result()
                print(f"[{done}/{len(slides)}] {st.upper()} slide #{idx}", flush=True)
            except Exception as exc:
                failures.append(f"slide #{idx}: {exc}")
                print(f"[{done}/{len(slides)}] FAIL slide #{idx}: {exc}", flush=True)

    print(f"Done. Failures: {len(failures)}", flush=True)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
