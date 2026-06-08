#!/usr/bin/env python3
"""
Generate 10 Instagram carousels with 8 AI-generated images and one bonus PDF each.

Usage:
  APIYI_API_KEY="sk-..." python3 generate_carousels.py

The script uses only Python standard library modules. It calls APIYi's
gpt-image-2-all model, downloads URL or b64 outputs, and writes a simple PDF
guide for each carousel.
"""

from __future__ import annotations

import base64
import concurrent.futures
import json
import os
import re
import textwrap
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


API_URL = "https://api.apiyi.com/v1/images/generations"
MODEL = "gpt-image-2-all"
ROOT = Path(__file__).resolve().parent / "AI_Business_Carousels"
MAX_WORKERS = int(os.environ.get("CAROUSEL_WORKERS", "6"))
TIMEOUT_SECONDS = 300


STYLE_SYSTEM = """
Create a premium Instagram carousel slide in a modern editorial AI-business style.
Canvas: 3:4 vertical portrait. Put the aspect instruction first: "3:4".
Reference style: luxury tech creator carousel, cream grid paper background OR blue-sky editorial portrait background, huge confident typography, clean spacing, high-end startup/design-studio feel, bold black sans-serif mixed with one elegant italic serif word, red/coral highlight tabs, subtle UI cards, thin black rules, small footer handle "@piyush.glitch", small page number, polished Figma-like composition.
Typography must be readable, sharp, correctly spelled, and intentional. Use large hierarchy: one main headline, one short subhead, and at most 3 compact supporting points. Do not add random text, lorem ipsum, fake paragraphs, or watermarks.
Design rules: strong whitespace, no clutter, no browser chrome, no Instagram UI, no screenshots of social media, no distorted logos, no messy hands, no tiny unreadable text blocks. Use simple icons/cards/diagrams only when they clarify the idea.
"""


CAROUSELS: list[dict[str, Any]] = [
    {
        "title": "Claude Code Agent Teams",
        "slug": "01_Claude_Code_Agent_Teams",
        "angle": "Claude Code is not just a coding chatbot; it is becoming an orchestration layer with subagents, hooks, skills, MCP and memory.",
        "pdf_title": "Claude Code Agent Teams: The Practical Playbook",
        "slides": [
            ("Stop Using Claude Code Like Chat", "The hidden power is agent teams: subagents, hooks, skills, MCP and memory working together.", "Fashion editorial cover, close crop of a founder/developer, large white text overlay."),
            ("Subagents", "Separate context windows for research, tests, docs, security and review. The main agent gets the summary, not the noise.", "Five clean worker cards orbiting one central task board."),
            ("MCP Connectors", "Claude can pull live context from GitHub, Jira, Postgres, Figma, Slack or internal APIs through a standard connector layer.", "Hub-and-spoke diagram with tool cards and a coral center burst."),
            ("Hooks", "Deterministic scripts run before or after tool use. Think auto-format, secret checks, test gates and policy enforcement.", "Minimal terminal window with checkmarks and red stop gate."),
            ("Skills", "Reusable packaged instructions. Teach the workflow once: release notes, migration plan, QA checklist, PR review, audit.", "Stack of pastel folders labeled Report, Audit, Release, QA."),
            ("Memory", "Project memory keeps conventions alive across sessions: architecture notes, commands, domain vocabulary and team preferences.", "Notebook plus pinned context cards on grid paper."),
            ("Team Pattern", "Explore agent reads. Builder edits. Tester runs. Reviewer critiques. The orchestrator decides what ships.", "Four role cards connected to one commit button."),
            ("Comment AI", "Want the full setup? Comment AI and get the Claude Code agent-team playbook.", "Premium closing slide with one CTA pill and tiny workflow diagram."),
        ],
        "pdf_sections": [
            ("Why this matters", "Claude Code gets dramatically more useful when you stop treating it as one long chat. The useful pattern is an orchestrator plus specialized helpers: one agent explores, another edits, another tests, and another reviews risk."),
            ("The core stack", "Use CLAUDE.md or project rules for baseline behavior, Skills for reusable workflows, Hooks for deterministic checks, MCP for live business tools, and subagents for parallel context isolation."),
            ("Example workflow", "Ask the main agent to plan a feature. Send exploration to a read-only subagent. Let a builder edit in small steps. Run test and review subagents in parallel. Use hooks to block secrets or unsafe commands."),
            ("What most people miss", "The benefit is not only speed. It is context hygiene. Raw searches, failed experiments and noisy logs do not have to pollute the main reasoning thread."),
        ],
    },
    {
        "title": "ChatGPT Workspace Agents",
        "slug": "02_ChatGPT_Workspace_Agents",
        "angle": "OpenAI's workspace agents turn ChatGPT into a shared automation worker for teams, not just an individual prompt box.",
        "pdf_title": "Workspace Agents: Turning ChatGPT Into Team Automation",
        "slides": [
            ("ChatGPT Is Becoming A Teammate", "Workspace agents are shared, persistent Codex-powered workers for repeatable business workflows.", "Editorial portrait cover with blue sky, giant white text."),
            ("From GPTs To Agents", "GPTs answered. Workspace agents can use files, tools, code, connected apps and memory over multiple steps.", "Before/after two-card comparison."),
            ("Runs In The Cloud", "Agents keep working after you leave: reports, follow-ups, coding tasks, cleanup, recurring operations.", "Cloud workspace card with clock and progress checklist."),
            ("Shared By Teams", "Build once. Let sales, ops, support or engineering reuse the same agent with org permissions.", "Team avatars around a single agent card."),
            ("Connects Tools", "Slack, Microsoft 365, Google Drive, Salesforce and custom MCP servers turn chat into real action.", "Connector diagram with app tiles."),
            ("Admin Controls", "The winning teams define who can run what, what tools are allowed, and what actions need approval.", "Policy dashboard UI with allow/deny chips."),
            ("Use Case Stack", "Weekly pipeline report. Customer-risk digest. PR triage. Support macro audit. Campaign asset tracker.", "Five stacked workflow cards with small icons."),
            ("Comment AI", "Want the full workspace-agent checklist? Comment AI and I will send the guide.", "Clean closing CTA with coral button."),
        ],
        "pdf_sections": [
            ("What changed", "Workspace agents move ChatGPT from personal assistant to shared automation surface. The important shift is ownership: a team can create, permission, improve and reuse a workflow agent."),
            ("High-value workflows", "Start with repetitive workflows that already have clear inputs and outputs: weekly reports, CRM cleanup, meeting-to-action summaries, release note drafting, support review, or lead research."),
            ("Control model", "Do not give every agent every tool. Use role-based permissions, approval steps for write actions, and logs that show user, prompt, tool call and output."),
            ("Implementation advice", "Begin with one department, one workflow, one measurable outcome. Measure time saved, error rate and manual handoffs removed."),
        ],
    },
    {
        "title": "Gemini CLI Beyond Coding",
        "slug": "03_Gemini_CLI_Beyond_Coding",
        "angle": "Gemini CLI combines a huge context window, Google Search grounding, multimodal input and MCP extensions inside the terminal.",
        "pdf_title": "Gemini CLI: The Terminal Agent Most Teams Underuse",
        "slides": [
            ("Gemini CLI Is Not Just For Code", "It can read files, use search, run shell commands, inspect huge context and connect tools with MCP.", "Cover with developer holding tablet, giant type."),
            ("1M Context Window", "Large docs, repos, transcripts and specs can be reasoned over without slicing everything into tiny prompts.", "Massive document stack flowing into one prompt box."),
            ("Search Grounding", "Built-in Google Search lets the agent refresh facts instead of relying only on stale memory.", "Search beam illuminating a research board."),
            ("Multimodal Starts", "Sketches, PDFs and images can become app plans, UI drafts, code tasks or research briefs.", "PDF, sketch and image cards converging into app screen."),
            ("MCP Extensions", "Add custom tools: database, docs, internal API, media generation, ticket systems, analytics.", "Plug-in cards around terminal window."),
            ("Headless Mode", "Run Gemini non-interactively in scripts for checks, reports and repeatable ops tasks.", "Automation flow with command line and scheduler."),
            ("Checkpointing", "Long sessions can be saved and resumed so complex work does not vanish after one prompt.", "Timeline with restore points."),
            ("Comment AI", "Want the Gemini CLI workflow map? Comment AI and I will send the full guide.", "CTA slide with terminal card and clean footer."),
        ],
        "pdf_sections": [
            ("The overlooked advantage", "Gemini CLI is valuable because it sits where developers and operators already work: the terminal. It combines tool use, file access and search grounding in one local workflow."),
            ("Best use cases", "Use it for repo exploration, large document summarization, grounded research briefs, operational scripts, migration planning and multimodal app prototyping from PDFs or sketches."),
            ("Extensions", "MCP is the key unlock. Once Gemini CLI can reach internal tools, it becomes a workflow agent rather than a Q&A surface."),
            ("Caution", "Grounded search is not a replacement for evaluation. For write actions, keep approvals, logs and deterministic checks."),
        ],
    },
    {
        "title": "MCP Connectors For Business",
        "slug": "04_MCP_Connectors_For_Business",
        "angle": "MCP is the common connector shape for agents, replacing one-off integrations with typed tools and auditable access.",
        "pdf_title": "MCP Connectors: The Business Layer For AI Agents",
        "slides": [
            ("MCP Is The USB-C For Agents", "One standard way for Claude, GPT, Gemini and Cursor-style agents to reach real tools.", "Diagram cover, cream grid, huge MCP headline."),
            ("Before MCP", "Every tool needed custom glue: auth, schema, retries, logs, permissions and weird edge cases.", "Messy cable diagram simplified into one port."),
            ("After MCP", "Servers expose tools, resources and prompts with structured inputs and outputs.", "Clean connector cards with typed fields."),
            ("Business Use Cases", "Salesforce updates, Jira triage, Drive research, Slack follow-ups, database lookups, Figma context.", "Six app cards around central agent."),
            ("Gateway Pattern", "Production teams put MCP behind auth, rate limits, audit logs and policy checks.", "Security gateway between agent and tools."),
            ("Identity Matters", "The system must know which human triggered which tool call, especially for writes.", "Badge identity card attached to tool invocation."),
            ("Trace Everything", "Log model, prompt hash, user, tool input, tool output, latency and error state.", "Observability dashboard with tool-call timeline."),
            ("Comment AI", "Want the MCP production checklist? Comment AI and I will send it.", "Clean final CTA with connector visual."),
        ],
        "pdf_sections": [
            ("Why MCP matters", "MCP gives agents a standard connector shape. Instead of building custom integrations for every model and every tool, teams expose capabilities through reusable servers."),
            ("Production architecture", "Use an MCP gateway for authentication, authorization, rate limiting, policy, logging and observability. Treat MCP servers like internal APIs, not random scripts."),
            ("Security basics", "Separate read tools from write tools. Require approval for high-impact actions. Propagate user identity. Keep tool schemas narrow and explicit."),
            ("Measurement", "Track success rate, error rate, latency, cost per workflow and rollback frequency. Agents become safer when failures are observable."),
        ],
    },
    {
        "title": "AI Skills As Operating Procedures",
        "slug": "05_AI_Skills_As_Operating_Procedures",
        "angle": "Skills package repeatable instructions so a team can reuse the same expert workflow without re-explaining it every time.",
        "pdf_title": "AI Skills: Reusable Operating Procedures For Teams",
        "slides": [
            ("Stop Re-Explaining Work", "Skills turn repeated prompts into reusable operating procedures your agent can load on demand.", "Cover with premium folder stack and large type."),
            ("What A Skill Contains", "Goal, inputs, steps, constraints, examples, quality bar, output format and failure rules.", "Labeled folder contents diagram."),
            ("Good Skill Example", "PR review skill: inspect diff, list risks first, check tests, flag security and avoid style-only noise.", "Review checklist card."),
            ("Bad Skill Example", "Be helpful. Write good content. Make it better. That is not a workflow; it is a vibe.", "Minimal red X card contrasting vague prompt."),
            ("Use Across Teams", "Marketing briefs, sales research, finance audits, code review, customer summaries, launch plans.", "Six department tabs."),
            ("Pair With Hooks", "Skills tell the agent how to think. Hooks enforce what must happen every time.", "Two interlocking cards: Skill and Hook."),
            ("Version Your Skills", "Treat them like product assets: improve, test, review and keep changelogs.", "Version history UI."),
            ("Comment AI", "Want my skill template pack? Comment AI and I will send it.", "Closing CTA with folder fan."),
        ],
        "pdf_sections": [
            ("Definition", "A Skill is a packaged instruction set for a repeatable job. It lets you move from ad hoc prompting to reusable operating procedures."),
            ("Template", "Every skill should include purpose, when to use it, required inputs, steps, constraints, examples, output format, quality checks and escalation rules."),
            ("Where it helps", "Skills work best when the job has stable taste or policy: content QA, PR review, release notes, customer research, migration planning, analytics narratives."),
            ("How to improve", "Collect failed outputs, add examples, tighten constraints and add a verification step. Skills get better like documentation gets better."),
        ],
    },
    {
        "title": "AI Image Workflows For Brands",
        "slug": "06_AI_Image_Workflows_For_Brands",
        "angle": "Great AI imagery depends on a repeatable workflow: brand world, reference system, shot list, prompt grammar, QC and asset management.",
        "pdf_title": "AI Image Workflow: From Prompt To Brand Asset Library",
        "slides": [
            ("Stop Generating Random Images", "Brands need systems: models, products, lighting, angles, copy, variants and approval flow.", "High-fashion product cover with huge white type."),
            ("Brand World", "Define color, lighting, camera, materials, typography, product rules and what must never appear.", "Moodboard UI with swatches and rules."),
            ("Reference Library", "Keep approved faces, products, poses, packaging, locations and negative examples.", "Asset grid with approved tags."),
            ("Shot List", "Hero cover, packshot, lifestyle, close-up, comparison, tutorial, social crop, ad variant.", "Eight shot cards in a grid."),
            ("Prompt Grammar", "Subject + product + scene + camera + lighting + composition + text + constraints + ratio.", "Formula card with highlighted tokens."),
            ("QC Pass", "Check hands, logos, text, product shape, scale, brand colors, weird artifacts and legal risk.", "Quality checklist over image preview."),
            ("Asset Pipeline", "Name files, store prompts, version variants and move approved outputs into a reusable library.", "Folder system flowing into brand library."),
            ("Comment AI", "Want the AI image production SOP? Comment AI and I will send it.", "CTA slide with camera/product cards."),
        ],
        "pdf_sections": [
            ("Core idea", "AI image quality improves when the prompt is only one part of a system. The full workflow includes brand definition, references, shot lists, QC and storage."),
            ("Prompt grammar", "Use a consistent structure: format, subject, product, scene, style, camera, lighting, composition, visible text and constraints."),
            ("QC checklist", "Inspect text, hands, logos, product geometry, packaging accuracy, brand colors, cultural context and whether the image can be legally used."),
            ("Operations", "Save every final asset with the prompt, date, model, input references and approval status. This turns experiments into a brand asset library."),
        ],
    },
    {
        "title": "Context Engineering",
        "slug": "07_Context_Engineering",
        "angle": "The best AI outputs come from engineered context: documents, examples, constraints, tool results and memory, not magic prompts.",
        "pdf_title": "Context Engineering: The Real Skill Behind Better AI Work",
        "slides": [
            ("Prompting Is Not Enough", "The real advantage is context: what the model sees before it acts.", "Cover with elegant portrait and huge headline."),
            ("Context Stack", "Goal, audience, source docs, examples, constraints, tools, memory, output format and success criteria.", "Layered stack diagram."),
            ("Examples Beat Adjectives", "Show three great outputs and one bad output. The model learns taste faster than from vague words.", "Good/bad gallery cards."),
            ("Constraints Create Quality", "Length, tone, forbidden claims, data sources, compliance rules and design boundaries reduce drift.", "Constraint rails around content block."),
            ("Tool Results Matter", "Let agents fetch fresh data instead of hallucinating: search, CRM, docs, analytics, repo, tickets.", "Tool-result cards feeding prompt."),
            ("Memory Is A Product", "Decide what should persist: brand voice, glossary, architecture, customer segments, workflows.", "Memory notebook with pinned items."),
            ("Evaluation Loop", "Save failures. Turn them into tests, examples and better context.", "Feedback loop diagram."),
            ("Comment AI", "Want the context-engineering worksheet? Comment AI and I will send it.", "Clean CTA with document stack."),
        ],
        "pdf_sections": [
            ("Definition", "Context engineering is the practice of shaping what the model sees: documents, examples, tool outputs, constraints, memory and output rules."),
            ("Why it works", "Models are pattern matchers and reasoners. Better context gives them better patterns, fewer ambiguities and more accurate constraints."),
            ("Practical template", "Start with objective, audience, source material, examples, non-goals, constraints, required format and success criteria."),
            ("Iteration", "Every bad output is a context bug. Add a counterexample, tighten a rule, or improve the source material."),
        ],
    },
    {
        "title": "Agent Evals As Release Gates",
        "slug": "08_Agent_Evals_As_Release_Gates",
        "angle": "Production agents need workflow-specific evals that block unsafe or low-quality behavior before release.",
        "pdf_title": "Agent Evals: How To Stop Shipping Broken Automation",
        "slides": [
            ("Your Agent Needs Tests", "If it can use tools or change data, vibes are not enough. You need evals.", "Cover with bold test-gate visual."),
            ("Not Trivia Benchmarks", "Useful evals are your workflows: refund policy, CRM mapping, on-call runbook, PR standards.", "Business workflow test cards."),
            ("Three Eval Types", "Task success. Safety boundaries. Operational behavior like loops, retries, latency and cost.", "Three-column comparison cards."),
            ("Golden Scenarios", "Save real edge cases and expected outputs. Run them before prompt, model or tool changes.", "Golden dataset folder."),
            ("Tool-Use Tests", "Check whether the agent calls the right tool, with the right inputs, at the right time.", "Tool-call timeline with pass/fail."),
            ("Regression Gate", "If a new prompt improves style but breaks compliance, it should not ship.", "Release gate with red/green result."),
            ("Metrics That Matter", "Success rate, intervention rate, tool error rate, cost per task, hallucinated action rate.", "Analytics dashboard cards."),
            ("Comment AI", "Want the agent-eval checklist? Comment AI and I will send it.", "Final CTA with test cards."),
        ],
        "pdf_sections": [
            ("Why evals matter", "Agents are probabilistic systems wired into deterministic business tools. A small behavior change can create bad writes, loops, cost spikes or compliance risk."),
            ("Build evals from reality", "Use actual customer cases, CRM fields, tickets, docs, bug reports and support policies. Abstract benchmarks are less useful than workflow fidelity."),
            ("Types of tests", "Measure task completion, safety, permission boundaries, prompt injection resistance, tool correctness, retries, latency and cost."),
            ("Release process", "Run evals before changing prompts, tools, models or memory. Treat failures as release blockers, not nice-to-have feedback."),
        ],
    },
    {
        "title": "Pick The Right AI Model",
        "slug": "09_Pick_The_Right_AI_Model",
        "angle": "Teams should route work by task type: deep reasoning, daily drafting, fast triage, multimodal creation and cheap background automation.",
        "pdf_title": "Model Routing: Choosing Claude, GPT, Gemini And Small Models",
        "slides": [
            ("Pick The Right Model", "The best AI stack is not one model. It is routing tasks to the right model.", "Cream grid comparison cover with three cards."),
            ("Deep Reasoning", "Use stronger models for ambiguous plans, architecture, strategy, legal nuance and multi-step decisions.", "Premium card labeled Deep Reasoning."),
            ("Daily Driver", "Use balanced models for writing, analysis, code help, research summaries and normal business tasks.", "Workspace card with everyday tasks."),
            ("Fast Cheap Scale", "Use smaller models for classification, extraction, rewriting, tagging, first-pass QA and routing.", "Many tiny task cards flowing quickly."),
            ("Multimodal Work", "Use Gemini/GPT image/video tools when the input or output is visual, not only text.", "Image, PDF, video and sketch cards."),
            ("Agent Work", "Use models that can plan, call tools, inspect state, recover from errors and explain actions.", "Agent loop diagram."),
            ("Routing Rule", "If failure is expensive, use stronger model plus evals. If volume is huge, use smaller model plus checks.", "Decision tree card."),
            ("Comment AI", "Want the model-routing matrix? Comment AI and I will send it.", "Clean final CTA with routing matrix."),
        ],
        "pdf_sections": [
            ("Principle", "Do not choose one model for everything. Route by risk, context size, modality, latency and cost."),
            ("Suggested routing", "Use top reasoning models for complex strategy or architecture, balanced models for everyday work, smaller models for extraction and classification, and multimodal models for image/PDF/video-heavy tasks."),
            ("Risk rule", "When failure is expensive, pay for stronger reasoning and add evals. When volume is high, use cheaper models with deterministic verification."),
            ("Operational rule", "Track accuracy, latency and cost per workflow. Model routing should be measured, not guessed."),
        ],
    },
    {
        "title": "AI Operating System For Teams",
        "slug": "10_AI_Operating_System_For_Teams",
        "angle": "Winning teams build an AI operating system: context, tools, workflows, approvals, evals and asset libraries.",
        "pdf_title": "The AI Operating System For Modern Teams",
        "slides": [
            ("Build An AI Operating System", "Random prompts do not scale. Systems do.", "Editorial cover with founder and huge type."),
            ("Layer 1: Context", "Projects, memory, docs, examples, brand voice, data dictionary and decision logs.", "Layered workspace board."),
            ("Layer 2: Tools", "MCP connectors, APIs, databases, files, browser, code runner and internal systems.", "Tool connector strip."),
            ("Layer 3: Workflows", "Reusable skills, agent templates, SOPs and prompt packs for repeated work.", "Workflow cards and SOP binder."),
            ("Layer 4: Control", "Permissions, approvals, hooks, logs, identity, spend limits and rollback plans.", "Control panel with approval toggle."),
            ("Layer 5: Evals", "Workflow tests, regression gates, edge cases and production monitoring.", "Eval dashboard."),
            ("Layer 6: Libraries", "Approved outputs become reusable assets: images, prompts, guides, reports and templates.", "Brand library grid."),
            ("Comment AI", "Want the full AI operating-system blueprint? Comment AI and I will send it.", "Final CTA with six-layer diagram."),
        ],
        "pdf_sections": [
            ("The shift", "Teams that win with AI do not rely on random prompting. They build repeatable systems around context, tools, workflows, controls, evals and libraries."),
            ("Six layers", "Context explains the business. Tools connect real systems. Workflows package repeatable jobs. Control prevents damage. Evals measure quality. Libraries preserve what works."),
            ("First 30 days", "Pick three workflows, write context docs, create one reusable skill per workflow, add approvals for write actions, build a small eval set and save final outputs."),
            ("What to avoid", "Do not connect every tool at once. Do not let agents write without identity and logs. Do not confuse impressive demos with reliable operations."),
        ],
    },
]


def slugify(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("_")


def safe_text(value: str) -> str:
    return value.encode("latin-1", "replace").decode("latin-1")


def escape_pdf_text(value: str) -> str:
    value = safe_text(value)
    return value.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def write_simple_pdf(path: Path, title: str, carousel: dict[str, Any]) -> None:
    """Write a lightweight text PDF without third-party dependencies."""
    width, height = 612, 792
    margin = 54
    line_height = 14
    y = height - margin
    lines: list[tuple[int, str]] = []

    def add(font_size: int, text: str = "") -> None:
        nonlocal y
        if text == "":
            y -= line_height
            return
        wrap_width = max(45, int(95 - font_size * 2.2))
        for part in textwrap.wrap(text, width=wrap_width):
            if y < margin + 40:
                lines.append((-1, "PAGE_BREAK"))
                y = height - margin
            lines.append((font_size, part))
            y -= line_height + (font_size - 10) * 0.7
        y -= 4

    add(22, title)
    add(11, f"Carousel: {carousel['title']}")
    add(11, f"Core angle: {carousel['angle']}")
    add(10, "Use this as the bonus guide for people who comment AI on the post.")
    add(10, "")

    for heading, body in carousel["pdf_sections"]:
        add(16, heading)
        add(11, body)
        add(10, "")

    add(16, "Slide-by-slide recap")
    for idx, (headline, body, _) in enumerate(carousel["slides"], start=1):
        add(11, f"{idx}. {headline}: {body}")

    pages: list[list[tuple[int, str]]] = [[]]
    for item in lines:
        if item == (-1, "PAGE_BREAK"):
            pages.append([])
        else:
            pages[-1].append(item)

    objects: list[str] = []
    objects.append("<< /Type /Catalog /Pages 2 0 R >>")
    kids = " ".join(f"{3 + i * 2} 0 R" for i in range(len(pages)))
    objects.append(f"<< /Type /Pages /Kids [{kids}] /Count {len(pages)} >>")

    for i, page_lines in enumerate(pages):
        page_obj_num = 3 + i * 2
        content_obj_num = page_obj_num + 1
        objects.append(
            f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {width} {height}] "
            f"/Resources << /Font << /F1 << /Type /Font /Subtype /Type1 /BaseFont /Helvetica >> "
            f"/F2 << /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >> >> >> "
            f"/Contents {content_obj_num} 0 R >>"
        )
        stream_lines = ["BT"]
        y_pos = height - margin
        for font_size, text in page_lines:
            font = "F2" if font_size >= 16 else "F1"
            stream_lines.append(f"/{font} {font_size} Tf")
            stream_lines.append(f"{margin} {y_pos:.1f} Td ({escape_pdf_text(text)}) Tj")
            stream_lines.append(f"{-margin} {-line_height - (font_size - 10) * 0.7:.1f} Td")
            y_pos -= line_height + (font_size - 10) * 0.7
        stream_lines.append("ET")
        stream = "\n".join(stream_lines)
        objects.append(f"<< /Length {len(stream.encode('latin-1'))} >>\nstream\n{stream}\nendstream")

    pdf = ["%PDF-1.4\n"]
    offsets = [0]
    for idx, obj in enumerate(objects, start=1):
        offsets.append(sum(len(part.encode("latin-1")) for part in pdf))
        pdf.append(f"{idx} 0 obj\n{obj}\nendobj\n")
    xref_start = sum(len(part.encode("latin-1")) for part in pdf)
    pdf.append(f"xref\n0 {len(objects) + 1}\n")
    pdf.append("0000000000 65535 f \n")
    for offset in offsets[1:]:
        pdf.append(f"{offset:010d} 00000 n \n")
    pdf.append(f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref_start}\n%%EOF\n")
    path.write_bytes("".join(pdf).encode("latin-1"))


def build_prompt(carousel: dict[str, Any], slide_index: int, slide: tuple[str, str, str]) -> str:
    headline, body, visual = slide
    page = f"{slide_index}/8"
    cover_note = (
        "This is the first cover slide: make it feel like a premium creator carousel cover, fashion/editorial, big dramatic text."
        if slide_index == 1
        else "This is an interior educational slide: make the information clear, useful, and visually structured."
    )
    return f"""
3:4 vertical Instagram carousel slide.
{STYLE_SYSTEM}

Carousel topic: {carousel['title']}
Strategic angle: {carousel['angle']}
Slide number: {page}
{cover_note}

Exact visible text to include:
Top small label: AI FOR BUSINESS - {slide_index:02d}
Main headline: {headline}
Supporting copy: {body}
Footer left: @piyush.glitch
Footer right: {page}

Visual direction:
{visual}

Composition:
- Main headline must dominate the slide.
- Use cream grid-paper background for diagram/information slides, or blue-sky luxury editorial background for cover/person/product slides.
- Mix bold black sans-serif with one italic serif emphasis word where natural.
- Add a coral/red highlight tab under or behind one important word.
- If using cards, keep them large and readable.
- The slide should feel like a high-performing Instagram carousel about advanced AI workflows for founders, creators and operators.
- No generic AI robot imagery. No random buzzwords. No extra paragraphs. No spelling mistakes.
""".strip()


def post_json(url: str, payload: dict[str, Any], api_key: str) -> dict[str, Any]:
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
        return json.loads(resp.read().decode("utf-8"))


def download_url(url: str, path: Path) -> None:
    req = urllib.request.Request(url, headers={"User-Agent": "carousel-generator/1.0"})
    with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
        path.write_bytes(resp.read())


def save_generation(result: dict[str, Any], path: Path) -> str:
    item = result["data"][0]
    if "url" in item and item["url"]:
        download_url(item["url"], path)
        return item["url"]
    if "b64_json" in item and item["b64_json"]:
        value = item["b64_json"]
        if "," in value and value.startswith("data:"):
            value = value.split(",", 1)[1]
        path.write_bytes(base64.b64decode(value))
        return "b64_json"
    raise RuntimeError(f"No image data in response: {result}")


def generate_one(api_key: str, carousel: dict[str, Any], slide_index: int, slide: tuple[str, str, str]) -> dict[str, Any]:
    folder = ROOT / carousel["slug"]
    folder.mkdir(parents=True, exist_ok=True)
    headline = slide[0]
    filename = f"{slide_index:02d}_{slugify(headline)[:60]}.png"
    out_path = folder / filename
    prompt_path = folder / f"{slide_index:02d}_{slugify(headline)[:60]}.prompt.txt"
    prompt = build_prompt(carousel, slide_index, slide)
    prompt_path.write_text(prompt, encoding="utf-8")

    if out_path.exists() and out_path.stat().st_size > 100_000:
        return {"status": "skipped", "path": str(out_path)}

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "response_format": "url",
    }

    last_error = None
    for attempt in range(1, 4):
        try:
            result = post_json(API_URL, payload, api_key)
            source = save_generation(result, out_path)
            return {"status": "ok", "path": str(out_path), "source": source, "usage": result.get("usage")}
        except Exception as exc:  # noqa: BLE001 - printable retry loop for automation script
            last_error = exc
            wait = min(60, 6 * attempt)
            print(f"[retry {attempt}/3] {carousel['slug']} slide {slide_index}: {exc}; waiting {wait}s", flush=True)
            time.sleep(wait)
    raise RuntimeError(f"Failed {carousel['slug']} slide {slide_index}: {last_error}")


def prepare_folders() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    for carousel in CAROUSELS:
        folder = ROOT / carousel["slug"]
        folder.mkdir(parents=True, exist_ok=True)
        plan = {
            "title": carousel["title"],
            "angle": carousel["angle"],
            "slides": [
                {"slide": idx, "headline": s[0], "copy": s[1], "visual": s[2]}
                for idx, s in enumerate(carousel["slides"], start=1)
            ],
        }
        (folder / "00_content_plan.json").write_text(json.dumps(plan, indent=2), encoding="utf-8")
        write_simple_pdf(folder / "09_bonus_guide.pdf", carousel["pdf_title"], carousel)


def main() -> int:
    api_key = os.environ.get("APIYI_API_KEY")
    if not api_key:
        print("ERROR: set APIYI_API_KEY before running.", flush=True)
        return 2

    prepare_folders()
    jobs = []
    for carousel in CAROUSELS:
        for idx, slide in enumerate(carousel["slides"], start=1):
            jobs.append((carousel, idx, slide))

    print(f"Generating {len(jobs)} images into {ROOT}", flush=True)
    failures: list[str] = []
    completed = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        future_map = {
            pool.submit(generate_one, api_key, carousel, idx, slide): (carousel["slug"], idx, slide[0])
            for carousel, idx, slide in jobs
        }
        for future in concurrent.futures.as_completed(future_map):
            slug, idx, headline = future_map[future]
            completed += 1
            try:
                result = future.result()
                print(f"[{completed:02d}/{len(jobs)}] {result['status'].upper()} {slug} slide {idx}: {headline}", flush=True)
            except Exception as exc:  # noqa: BLE001
                message = f"{slug} slide {idx} failed: {exc}"
                failures.append(message)
                print(f"[{completed:02d}/{len(jobs)}] FAILED {message}", flush=True)

    manifest = {
        "root": str(ROOT),
        "model": MODEL,
        "total_carousels": len(CAROUSELS),
        "slides_per_carousel": 8,
        "failures": failures,
        "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    (ROOT / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Done. Failures: {len(failures)}. Manifest: {ROOT / 'manifest.json'}", flush=True)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
