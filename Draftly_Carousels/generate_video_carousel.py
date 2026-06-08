#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate one Draftly video carousel: hero image -> Veo 3.1 video -> mixed MP4/PNG slides.

Usage:
  APIYI_API_KEY="..." python3 Draftly_Carousels/generate_video_carousel.py
"""

from __future__ import annotations

import base64
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
SLUG = "16_iPhone_17_Pro_Max"
OUT = ROOT / SLUG

IMAGE_MODEL = "gpt-image-2-all"
VIDEO_MODEL = "veo-3.1-fast-generate-preview"
API_BASE = "https://api.apiyi.com/v1"
TIMEOUT = 300

EDITORIAL = """
3:4 vertical Instagram carousel slide. Mobile Editing Club premium style.
Cream grid #F4EEDE, coral #EF5E45, ink #1B1A17. Space Grotesk headlines, italic serif accent.
TOP RIGHT: text logo DRAFTLY (no icon). NO blue AI UI. Photoreal editorial quality.
"""

CAROUSEL = {
    "title": "iPhone 17 Pro Max",
    "product_label": "iPhone 17 Pro Max",
    "cover_hook": "Prompt a scroll-synced iPhone launch site - hero still, Veo motion, live website. Not a template.",
    "website_prompt": (
        "Build a flagship smartphone launch page for iPhone 17 Pro Max in desert titanium. "
        "Floating centered nav pill: Features, Camera, Performance, Pre-order. "
        "Hero headline 'Forged In Titanium. Built For Pro.' with subcopy on A19 Pro chip, 48MP fusion camera, and all-day battery.\n\n"
        "Scroll sections: cinematic hero with scroll-scrubbed background, three feature cards (Pro Camera System, Titanium Design, Apple Intelligence), "
        "spec comparison strip vs previous generation, trade-in calculator mockup, color picker (Desert Titanium, Natural Titanium, Black Titanium), "
        "and sticky Pre-order CTA with delivery estimate.\n\n"
        "Typography: SF Pro style minimal grotesque, generous whitespace, product-first. "
        "Palette: warm titanium grays, soft white hero, deep charcoal footer. "
        "Motion: hero background scrubs through extracted Veo frames. Flagship launch - not marketplace grid."
    ),
    "image_prompt": (
        "Cinematic photoreal hero still for scroll-scrubbed iPhone 17 Pro Max launch page. No text, no logos, no UI chrome, 3:4 vertical composition suitable for frame extraction.\n\n"
        "Scene: iPhone 17 Pro Max in desert titanium finish standing at slight angle on dark reflective studio surface, triple camera array sharp, "
        "screen showing subtle abstract gradient wallpaper (no readable UI). Soft key light from upper left, cool rim on titanium edges, "
        "caustic reflection on glossy surface beneath phone.\n\n"
        "Background: deep charcoal gradient to near-black, faint atmospheric haze, shallow DOF with creamy bokeh. "
        "Color direction: warm titanium, neutral grays, single soft amber highlight - Apple keynote product photography quality. "
        "Ultra sharp lens detail on camera lenses and titanium texture."
    ),
    "first_frame_prompt": (
        "Opening keyframe: wide product tableau - iPhone 17 Pro Max centered on reflective dark surface, screen off/dim, "
        "lots of negative space above for headline overlay, cool studio top light, same visual world as hero still."
    ),
    "last_frame_prompt": (
        "Closing keyframe: tighter three-quarter angle on camera bump and titanium side rail, screen glowing soft gradient, "
        "camera 20% closer than opening frame, stronger rim light on edges."
    ),
    "video_prompt": (
        "Slow cinematic dolly-in toward iPhone 17 Pro Max in desert titanium, gentle parallax on reflection, "
        "subtle rotation revealing camera array and titanium frame, premium Apple-style product reveal, "
        "6-second seamless loop, steady camera, no text overlays, soft studio lighting shift."
    ),
    "why_website": (
        "Phone launches are cinematic events. Buyers decide on craft before specs. "
        "A scroll-synced site with Veo hero motion proves industrial design and camera story better than static Shopify themes."
    ),
    "result_headline": "Forged In Titanium. Built For Pro.",
    "result_notes": "Shipped scroll site with feature cards, spec table, trade-in module, and pre-order strip over Veo hero frames.",
}


def slugify(text: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "_", text.strip().lower()).strip("_") or "slide"


def post_json(url: str, payload: dict[str, Any], api_key: str) -> dict[str, Any]:
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return json.loads(resp.read().decode("utf-8"))


def get_json(url: str, api_key: str) -> dict[str, Any]:
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {api_key}"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return json.loads(resp.read().decode("utf-8"))


def download_url(url: str, path: Path) -> None:
    req = urllib.request.Request(url, headers={"User-Agent": "draftly-video-carousel/1.0"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        path.write_bytes(resp.read())


def save_image_result(result: dict[str, Any], path: Path) -> None:
    item = result["data"][0]
    if item.get("url"):
        download_url(item["url"], path)
        return
    b64 = item.get("b64_json", "")
    if "," in b64 and b64.startswith("data:"):
        b64 = b64.split(",", 1)[1]
    path.write_bytes(base64.b64decode(b64))


def generate_hero_image(api_key: str, path: Path) -> None:
    prompt = (
        "3:4 vertical portrait. "
        + CAROUSEL["image_prompt"]
        + " No text on image. Premium Apple-style product photography."
    )
    result = post_json(
        f"{API_BASE}/images/generations",
        {"model": IMAGE_MODEL, "prompt": prompt, "response_format": "url"},
        api_key,
    )
    save_image_result(result, path)
    print(f"Hero image -> {path}", flush=True)


def start_veo_video(api_key: str, image_path: Path, prompt: str) -> str:
    cmd = [
        "curl", "-s", "-X", "POST", f"{API_BASE}/videos",
        "-H", f"Authorization: Bearer {api_key}",
        "-F", f"input_reference=@{image_path};type=image/png",
        "-F", f"model={VIDEO_MODEL}",
        "-F", f"prompt={prompt}",
        "-F", "duration=6",
        "-F", "size=720x1280",
        "-F", "resolution=720p",
        "-F", "aspectRatio=9:16",
    ]
    out = subprocess.check_output(cmd, text=True)
    data = json.loads(out)
    task_id = data.get("task_id") or data.get("id")
    if not task_id:
        raise RuntimeError(f"No task_id in video response: {out[:500]}")
    print(f"Veo task started: {task_id} status={data.get('status')}", flush=True)
    return str(task_id)


def poll_veo_video(api_key: str, task_id: str, max_wait: int = 600) -> None:
    deadline = time.time() + max_wait
    while time.time() < deadline:
        data = get_json(f"{API_BASE}/videos/{task_id}", api_key)
        status = data.get("status", "")
        progress = data.get("progress", 0)
        print(f"  poll {task_id}: {status} {progress}%", flush=True)
        if status == "completed":
            return
        if status == "failed":
            raise RuntimeError(f"Veo failed: {data}")
        time.sleep(10)
    raise RuntimeError(f"Veo timed out after {max_wait}s")


def download_veo_video(api_key: str, task_id: str, path: Path) -> None:
    for attempt in range(1, 6):
        try:
            req = urllib.request.Request(
                f"{API_BASE}/videos/{task_id}/content",
                headers={"Authorization": f"Bearer {api_key}"},
            )
            with urllib.request.urlopen(req, timeout=180) as resp:
                path.write_bytes(resp.read())
            print(f"Video saved -> {path} ({path.stat().st_size // 1024} KB)", flush=True)
            return
        except Exception as exc:  # noqa: BLE001
            print(f"  download retry {attempt}/5: {exc}", flush=True)
            time.sleep(5)
    raise RuntimeError("Video download failed")


def build_slide1_hero_mp4(source: Path, dest: Path) -> None:
    """Hero clip scaled to 3:4 for carousel slide 1."""
    subprocess.run(
        [
            "ffmpeg", "-y", "-i", str(source),
            "-vf", "scale=1080:1440:force_original_aspect_ratio=decrease,pad=1080:1440:(ow-iw)/2:(oh-ih)/2:black",
            "-t", "6", "-an", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
            str(dest),
        ],
        check=True,
        capture_output=True,
    )
    print(f"Slide 1 video -> {dest}", flush=True)


def build_slide2_prompt_video(source: Path, dest: Path) -> None:
    """Looping video background with cream lower panel for prompt overlay area."""
    subprocess.run(
        [
            "ffmpeg", "-y", "-stream_loop", "1", "-i", str(source),
            "-vf", (
                "scale=1080:1440:force_original_aspect_ratio=increase,crop=1080:1440,"
                "drawbox=x=0:y=ih*0.50:w=iw:h=ih*0.50:color=#F4EEDE@0.94:t=fill"
            ),
            "-t", "8", "-an", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
            str(dest),
        ],
        check=True,
        capture_output=True,
    )
    print(f"Slide 2 video -> {dest}", flush=True)


def build_image_prompt(api_key: str, slide_index: int, headline: str, body: str, visual: str, extra: str, filename: str) -> None:
    page = f"{slide_index}/8"
    block = f"\n\nRender on slide:\n{extra}" if extra else ""
    prompt = f"""
3:4 vertical Instagram carousel slide.
{EDITORIAL}
Product: {CAROUSEL['product_label']}
Slide {page}
Headline: {headline}
Body: {body}
Visual: {visual}
{block}
Footer slide number {page} bottom-right.
""".strip()
    path = OUT / filename
    if path.exists() and path.stat().st_size > 100_000:
        print(f"SKIP {filename}", flush=True)
        return
    result = post_json(
        f"{API_BASE}/images/generations",
        {"model": IMAGE_MODEL, "prompt": prompt, "response_format": "url"},
        api_key,
    )
    save_image_result(result, path)
    print(f"OK {filename}", flush=True)


def main() -> int:
    api_key = os.environ.get("APIYI_API_KEY")
    if not api_key:
        print("ERROR: set APIYI_API_KEY", file=sys.stderr)
        return 2
    if not shutil.which("ffmpeg"):
        print("ERROR: ffmpeg required", file=sys.stderr)
        return 2

    OUT.mkdir(parents=True, exist_ok=True)
    hero_png = OUT / "00_hero_source.png"
    raw_mp4 = OUT / "00_hero_raw.mp4"

    if not hero_png.exists():
        generate_hero_image(api_key, hero_png)

    if not raw_mp4.exists():
        task_id = start_veo_video(api_key, hero_png, CAROUSEL["video_prompt"])
        poll_veo_video(api_key, task_id)
        download_veo_video(api_key, task_id, raw_mp4)

    slide1 = OUT / "01_hero_video.mp4"
    slide2 = OUT / "02_website_prompt_video.mp4"
    if not slide1.exists():
        build_slide1_hero_mp4(raw_mp4, slide1)
    if not slide2.exists():
        build_slide2_prompt_video(raw_mp4, slide2)

    build_image_prompt(
        api_key,
        2,
        "Website Prompt",
        "Step 1 at /3d-builder. Paste this full production brief - three paragraphs.",
        "Top 45% shows iPhone 17 Pro Max Veo video still in motion on dark studio background. Bottom 55% cream grid with FULL three-paragraph website prompt text readable. DRAFTLY top-right. 2/8.",
        CAROUSEL["website_prompt"],
        "02_website_prompt.png",
    )

    slides = [
        (3, "Hero Image Prompt", "Step 2 - three paragraphs of art direction for the scroll-synced still.", "Cream grid. Full THREE paragraph image prompt readable in card. Small generated iPhone preview.", CAROUSEL["image_prompt"], "03_hero_image_prompt.png"),
        (4, "First and Last Frame", "Keyframe rail: first from hero, last from its own prompt for Veo first-to-last motion.", "Cream grid, keyframe rail UI, two iPhone frame thumbnails with prompt text.", f"FIRST:\n{CAROUSEL['first_frame_prompt']}\n\nLAST:\n{CAROUSEL['last_frame_prompt']}", "04_first_last_frames.png"),
        (5, "Video Motion Prompt", "Step 4 - sent to veo-3.1-fast-generate-preview after hero image.", "Cream grid showing motion prompt card plus label MODEL veo-3.1-fast-generate-preview. Mention slides 1-2 use the generated video.", CAROUSEL["video_prompt"], "05_video_motion_prompt.png"),
        (6, "Why A Cinematic Website", CAROUSEL["why_website"], "Cream editorial, Trust Story Conversion pillars.", "", "06_why_cinematic_website.png"),
        (7, CAROUSEL["result_headline"], CAROUSEL["result_notes"], "Split: cream panel plus draftly.space iPhone site screenshot mockup.", "", "07_finished_website.png"),
        (8, "Prompt. Generate. Ship.", "Image to Veo to scroll site. Deep prompts in, cinematic iPhone launch out.", "Editorial iPhone photo, white pill CTA, draftly.space / piyush.glitch footer.", "", "08_start_prompting.png"),
    ]
    for idx, headline, body, visual, extra, fname in slides:
        build_image_prompt(api_key, idx, headline, body, visual, extra, fname)

    print(f"Done -> {OUT}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
