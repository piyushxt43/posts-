# -*- coding: utf-8 -*-
"""Load carousel slide prompts from maker.md."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MAKER = ROOT / "maker.md"

STYLE_PREFIX = (
    "3:4 vertical portrait ONLY (1080x1440). Premium Instagram carousel slide. "
    "Perfect spelling, crisp readable typography, no watermarks. "
    "Chase H AI terracotta editorial for @piyush.glitch: warm burnt-orange grain (#C45E3B), "
    "header JUN @2026 PIYUSH.GLITCH with slide counter, bold lowercase headlines "
    "(white + black + gradient emphasis), footer dots and SWIPE arrow except slide 08. "
    "Graphic editorial UI - NOT beauty portrait, NOT cream grid. "
)

CAPTIONS = {
    "01_Claude_Small_Business_Cowork": (
        "Claude for Small Business is the 2026 ops stack - Cowork + connectors + approve-before-send.\n\n"
        "Most SMB owners still copy-paste between QuickBooks, HubSpot, and Gmail. Cowork runs "
        "multi-step workflows in one thread and pauses at [REVIEW] before anything goes out.\n\n"
        "Swipe for: connector map, finance + sales workflows, and the safety gate.\n\n"
        "Comment COWORK for the full 12-page operator PDF.\n\n"
        "#ClaudeAI #SmallBusiness #AIWorkflow #Cowork #PIYUSHGLITCH"
    ),
    "02_Skills_MCP_Two_Layer_Stack": (
        "MCP = access. Skills = how to use access well. One diagram. Three real jobs.\n\n"
        "Stop treating MCP servers and Skills as the same thing. USB vs playbook - finally explained.\n\n"
        "Comment STACK for diagram + 3 workflow recipes PDF.\n\n"
        "#MCP #AgentSkills #ClaudeAI #Cursor #PIYUSHGLITCH"
    ),
    "03_Agent_Skills_Write_Once": (
        "SKILL.md works in Claude Code, Cursor, Codex, and Gemini CLI - write once, run everywhere.\n\n"
        "You should not maintain four configs for one PR review workflow. Agent Skills is the open standard.\n\n"
        "Comment SKILLS for SKILL.md anatomy + 3 portable templates.\n\n"
        "#AgentSkills #Cursor #ClaudeCode #PIYUSHGLITCH"
    ),
    "04_Cursor_Cloud_Agents": (
        "Cloud Agents = isolated VMs, browser tests, merge-ready PRs while you sleep.\n\n"
        "Local Composer for pairing. Cloud for shipping. This is the split most devs miss.\n\n"
        "Comment CLOUD for environment.json + definition-of-done PDF.\n\n"
        "#Cursor #CloudAgents #DevTools #PIYUSHGLITCH"
    ),
    "05_OpenAI_Workspace_Agents": (
        "Workspace Agents: shared, scheduled, cloud-run - evolution of Custom GPTs for teams.\n\n"
        "When your output goes to clients on a cron, you need connectors + HITL - not a solo GPT.\n\n"
        "Comment AGENTS for migration guide PDF.\n\n"
        "#OpenAI #ChatGPTBusiness #AIAgents #PIYUSHGLITCH"
    ),
    "06_Google_Workspace_Studio_Gems": (
        "Workspace Studio + Ask a Gem inside flows - agentic Gmail/Sheets automation without code.\n\n"
        "Your trained Gem in the middle of a flow, not just chat sidebar.\n\n"
        "Comment STUDIO for 5 flow walkthroughs PDF.\n\n"
        "#GoogleWorkspace #Gemini #NoCode #PIYUSHGLITCH"
    ),
    "07_Meta_UGC_Creative_OS": (
        "Meta Advantage+ is creative-first: 30-50 variants, hook bible, refresh every 2-3 weeks.\n\n"
        "70-80% of performance is the asset. This is the operating system for variant volume.\n\n"
        "Comment UGC for hook matrix + tagging schema PDF.\n\n"
        "#MetaAds #UGC #DTC #PerformanceMarketing #PIYUSHGLITCH"
    ),
    "08_MCP_Servers_By_Job": (
        "Connect MCP for a job - SEO report, pipeline follow-up, content alerts - not a giant server list.\n\n"
        "Five high-leverage servers cover 80% of solo-founder ops.\n\n"
        "Comment MCP for per-job stacks + proof prompts PDF.\n\n"
        "#MCP #SEO #Automation #PIYUSHGLITCH"
    ),
    "09_Router_Worker_Reviewer": (
        "Router plans. Worker executes. Reviewer gates. Multi-agent pattern that stops drift.\n\n"
        "Same architecture in Claude subagents, OpenAI handoffs, and Cursor parallel runs.\n\n"
        "Comment WORKFLOW for copy-paste roles + weekly report example PDF.\n\n"
        "#AIWorkflow #Claude #Agents #PIYUSHGLITCH"
    ),
    "10_Agent_Governance_SAFE": (
        "Human-in-the-loop before agents send email, payments, or posts.\n\n"
        "[REVIEW] protocol, read-first MCP, blocked tools, audit logs - the trust layer SMBs need.\n\n"
        "Comment SAFE for governance checklist + 1-page team policy PDF.\n\n"
        "#AIGovernance #Compliance #SMB #PIYUSHGLITCH"
    ),
}

PDF_NAMES = {
    "01_Claude_Small_Business_Cowork": "claude-small-business-cowork.pdf",
    "02_Skills_MCP_Two_Layer_Stack": "skills-mcp-two-layer-stack.pdf",
    "03_Agent_Skills_Write_Once": "agent-skills-write-once.pdf",
    "04_Cursor_Cloud_Agents": "cursor-cloud-agents.pdf",
    "05_OpenAI_Workspace_Agents": "openai-workspace-agents.pdf",
    "06_Google_Workspace_Studio_Gems": "google-workspace-studio-gems.pdf",
    "07_Meta_UGC_Creative_OS": "meta-ugc-creative-os.pdf",
    "08_MCP_Servers_By_Job": "mcp-servers-by-job.pdf",
    "09_Router_Worker_Reviewer": "router-worker-reviewer.pdf",
    "10_Agent_Governance_SAFE": "agent-governance-safe.pdf",
}


def _clean(text: str) -> str:
    text = text.replace("\u2014", "-").replace("\u2013", "-")
    text = text.replace("\ufffd", "-")
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\n{3,}", "\n\n", text.strip())
    return text


def parse_maker(path: Path = MAKER) -> list[dict]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    carousels = []
    chunks = re.split(r"\n# Carousel \d+", raw)
    for chunk in chunks[1:]:
        folder_m = re.search(r"\*\*Folder:\*\*\s*`([^`]+)`", chunk)
        if not folder_m:
            continue
        slug = folder_m.group(1).strip()
        slides = []
        slide_parts = re.split(r"\n### Slide \d+", chunk)
        for sp in slide_parts[1:]:
            fn_m = re.match(r"\s*[^\n]*`([^`]+\.png)`", sp)
            if not fn_m:
                continue
            filename = fn_m.group(1)
            body = sp.split("`" + filename + "`", 1)[-1]
            body = re.split(r"\n---\n", body)[0]
            body = _clean(body.strip())
            prompt = STYLE_PREFIX + body
            slides.append((filename, prompt))
        if len(slides) != 8:
            raise ValueError(f"{slug}: expected 8 slides, got {len(slides)}")
        carousels.append({
            "slug": slug,
            "pdf_name": PDF_NAMES[slug],
            "caption": CAPTIONS[slug],
            "slides": slides,
        })
    if len(carousels) != 10:
        raise ValueError(f"Expected 10 carousels, got {len(carousels)}")
    return carousels


def load_carousels() -> list[dict]:
    return parse_maker()
