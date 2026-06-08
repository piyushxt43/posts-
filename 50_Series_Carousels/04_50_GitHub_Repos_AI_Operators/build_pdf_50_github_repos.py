#!/usr/bin/env python3
"""Build 50-github-repos-ai-operators.pdf with full appendix + setup notes."""

from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "50-github-repos-ai-operators.pdf"

REPOS = [
    ("Claude Foundations", "anthropics/claude-code", "Agentic coding CLI + IDE workflows.", "Operators use it for full dev loops with tools, planning, and execution.", "npm i -g @anthropic-ai/claude-code"),
    ("Claude Foundations", "anthropics/anthropic-sdk-python", "Official Python SDK for Claude API.", "Stable API wrappers for backend automation and agents.", "pip install anthropic"),
    ("Claude Foundations", "anthropics/anthropic-sdk-typescript", "Official TypeScript/JS SDK for Claude API.", "Typed integrations for web apps and internal tools.", "npm i @anthropic-ai/sdk"),
    ("Claude Foundations", "anthropics/anthropic-cookbook", "Prompting, tools, and production examples.", "Copy battle-tested patterns instead of starting from scratch.", "Clone and run examples for your model tier."),
    ("Claude Foundations", "openai/openai-cookbook", "Production AI patterns and implementation recipes.", "Cross-model patterns for evals, retrieval, and agent architecture.", "Review cookbook sections for your use-case."),
    ("MCP Core", "modelcontextprotocol/modelcontextprotocol", "Canonical MCP specification and docs.", "Protocol source of truth for client/server interoperability.", "Read spec + transport/auth sections first."),
    ("MCP Core", "modelcontextprotocol/servers", "Reference MCP server implementations.", "Faster connector development with known-good examples.", "Run one reference server locally before custom builds."),
    ("MCP Core", "modelcontextprotocol/typescript-sdk", "Official TypeScript SDK for MCP.", "Build MCP clients/servers in JS stacks quickly.", "npm i @modelcontextprotocol/sdk"),
    ("MCP Core", "modelcontextprotocol/python-sdk", "Official Python SDK for MCP.", "Best path for Python-first agent connector layers.", "pip install mcp"),
    ("MCP Core", "modelcontextprotocol/inspector", "Inspector UI for MCP testing/debug.", "Validate tools, schemas, and errors before production.", "Run inspector and test each tool contract."),
    ("MCP Ecosystem", "github/github-mcp-server", "Official GitHub MCP server.", "Agents can read/write issues, PRs, and repos via MCP.", "Configure PAT + server endpoint in your MCP client."),
    ("MCP Ecosystem", "punkpeye/awesome-mcp-servers", "Largest curated MCP server list.", "Shortcut to discover connectors by category quickly.", "Filter list for your stack: DB, SaaS, search, BI."),
    ("MCP Ecosystem", "wong2/awesome-mcp-servers", "Curated MCP servers with ecosystem links.", "Cross-reference options and maintenance maturity.", "Use as a second source before choosing connectors."),
    ("MCP Ecosystem", "open-webui/mcpo", "MCP proxy / bridge utility.", "Centralize MCP routing for cleaner deployments.", "Deploy mcpo as MCP gateway between agents and tools."),
    ("MCP Ecosystem", "PipedreamHQ/pipedream", "Thousands of integrations incl. MCP support.", "Rapid API wiring without building every connector yourself.", "Use hosted or self-hosted components for connector layer."),
    ("Agent Frameworks", "langchain-ai/langgraph", "Stateful graph framework for agents.", "Durable execution and explicit control flow for production.", "pip install langgraph"),
    ("Agent Frameworks", "crewAIInc/crewAI", "Role-based multi-agent orchestration.", "Fast path for business workflows with clear agent roles.", "pip install crewai"),
    ("Agent Frameworks", "microsoft/autogen", "Multi-agent conversation framework.", "Useful for collaborative agent patterns and enterprise familiarity.", "pip install pyautogen"),
    ("Agent Frameworks", "ag2ai/ag2", "Community continuation of AutoGen ideas.", "Modernized path for AutoGen-style architectures.", "pip install ag2"),
    ("Agent Frameworks", "huggingface/smolagents", "Lightweight code-first agent framework.", "Small surface area, easy to reason about and deploy.", "pip install smolagents"),
    ("Coding + Cursor Layer", "continue-revolution/continue", "Open-source coding agent in IDE.", "Policy + prompt + model control for team environments.", "Install Continue extension in your IDE."),
    ("Coding + Cursor Layer", "Aider-AI/aider", "Git-native coding assistant in terminal.", "Great for multi-file refactors with safe git loops.", "pip install aider-chat"),
    ("Coding + Cursor Layer", "block/goose", "Extensible local-first agent platform.", "Strong fit for custom workflows and tool integrations.", "Follow Goose quickstart and add provider keys."),
    ("Coding + Cursor Layer", "All-Hands-AI/OpenHands", "Autonomous software engineering agent.", "Issue-to-code automation and reproducible agent runs.", "Use Docker setup for first local run."),
    ("Coding + Cursor Layer", "PatrickJS/awesome-cursorrules", "Large Cursor rules collection.", "Faster setup of coding conventions and reusable rule packs.", "Copy relevant `.mdc` rules into `.cursor/rules/`."),
    ("Automation Orchestration", "n8n-io/n8n", "Visual workflow automation engine.", "Connect AI + SaaS tools fast with broad integrations.", "Run via Docker and configure credentials vault."),
    ("Automation Orchestration", "activepieces/activepieces", "Open-source automation builder.", "MIT-friendly option for workflow automation teams.", "Deploy with Docker Compose for team use."),
    ("Automation Orchestration", "windmill-labs/windmill", "Scripts -> workflows -> internal apps.", "Developer-friendly automation and operational UIs.", "Self-host and start with one scripted flow."),
    ("Automation Orchestration", "temporalio/temporal", "Durable execution workflow platform.", "Reliability for long-running, mission-critical automations.", "Use Temporal server + workers for stateful jobs."),
    ("Automation Orchestration", "prefecthq/prefect", "Python-native orchestration platform.", "Data/ML + business workflows in one orchestrator.", "pip install prefect"),
    ("Eval + Observability", "langfuse/langfuse", "Tracing, evals, prompts, and costs.", "Single pane for model quality + latency + spend.", "Self-host or cloud; instrument SDK in app."),
    ("Eval + Observability", "Arize-ai/phoenix", "Open-source LLM observability and eval.", "Detect quality regressions and hallucination patterns.", "pip install arize-phoenix"),
    ("Eval + Observability", "promptfoo/promptfoo", "Prompt/model eval tests in CI.", "Ship prompt changes with test gates like code.", "npm i -g promptfoo"),
    ("Eval + Observability", "confident-ai/deepeval", "LLM evaluation framework and metrics.", "Automate benchmark checks before releases.", "pip install deepeval"),
    ("Eval + Observability", "truera/trulens", "Evaluation and feedback instrumentation.", "Track reliability and explainability in pipelines.", "pip install trulens"),
    ("Data + Retrieval", "qdrant/qdrant", "High-performance vector database.", "Fast semantic retrieval and scalable similarity search.", "Run Docker image, create first collection."),
    ("Data + Retrieval", "milvus-io/milvus", "Distributed vector database system.", "Large-scale retrieval for high-volume AI workloads.", "Deploy Milvus standalone before clustering."),
    ("Data + Retrieval", "weaviate/weaviate", "Vector DB with hybrid retrieval.", "Semantic + keyword retrieval in one engine.", "Run Weaviate with your preferred embedding setup."),
    ("Data + Retrieval", "run-llama/llama_index", "RAG/data framework for LLM apps.", "Quickly connect docs and data to agents.", "pip install llama-index"),
    ("Data + Retrieval", "deepset-ai/haystack", "Search and RAG pipeline framework.", "Production-ready retrieval pipelines and components.", "pip install farm-haystack"),
    ("Bonus 10", "dagster-io/dagster", "Data orchestration with software-defined assets.", "Strong lineage, testing, and reproducible data workflows.", "pip install dagster"),
    ("Bonus 10", "apache/airflow", "Workflow scheduler and DAG orchestrator.", "Mature scheduling ecosystem for recurring jobs.", "pip install apache-airflow"),
    ("Bonus 10", "dbt-labs/dbt-core", "Analytics engineering transformation framework.", "Reliable semantic layer for AI-ready data models.", "pip install dbt-core"),
    ("Bonus 10", "jlowin/fastmcp", "Python-first MCP server framework.", "Build MCP servers quickly with concise abstractions.", "pip install fastmcp"),
    ("Bonus 10", "modelcontextprotocol/registry", "Community MCP registry service.", "Central server discovery and publishing workflows.", "Browse registry before building custom connectors."),
    ("Bonus 10", "simonw/llm", "CLI toolkit for multiple LLM providers.", "Fast experimentation and scripted model workflows.", "pip install llm"),
    ("Bonus 10", "BerriAI/litellm", "Unified API gateway across many LLMs.", "Provider abstraction + retries + spend controls.", "pip install litellm"),
    ("Bonus 10", "FlowiseAI/Flowise", "Visual AI flow builder and orchestration.", "Rapid prototyping for chat/RAG/agent use-cases.", "npm install -g flowise"),
    ("Bonus 10", "langchain-ai/langchain", "LLM app framework components and integrations.", "Reusable primitives across agents and retrieval workflows.", "pip install langchain"),
    ("Bonus 10", "microsoft/semantic-kernel", "Agent orchestration and plugin framework.", "Enterprise-friendly orchestration across .NET/Python/Java.", "pip install semantic-kernel"),
]

SETUP_NOTES = [
    "Start read-only: wire connectors with read scopes before any write tools.",
    "Ship one workflow first (e.g., daily KPI summary) before expanding stack.",
    "Add eval gates before enabling autonomous write actions.",
    "Log every agent run: model, prompt hash, tools called, latency, cost.",
    "Create one rollback path per workflow (manual fallback + feature flag).",
]

STACK_PATTERNS = [
    "Content + Research Stack: Claude Code + LangGraph + Langfuse + Qdrant + n8n",
    "Engineering Ops Stack: Claude Code + GitHub MCP + Aider + Promptfoo + Temporal",
    "RevOps Stack: CrewAI + MCP servers + Windmill + LiteLLM + Prefect",
    "Data QA Stack: LlamaIndex + Weaviate + DeepEval + Phoenix + Dagster",
]


def build() -> int:
    styles = getSampleStyleSheet()
    h1 = ParagraphStyle("h1", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=24, leading=28, textColor=colors.HexColor("#1B1A17"))
    h2 = ParagraphStyle("h2", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=15, leading=19, textColor=colors.HexColor("#1B1A17"))
    body = ParagraphStyle("body", parent=styles["BodyText"], fontName="Helvetica", fontSize=10, leading=14, textColor=colors.HexColor("#1B1A17"))
    small = ParagraphStyle("small", parent=styles["BodyText"], fontName="Helvetica", fontSize=9, leading=12, textColor=colors.HexColor("#534C3E"))

    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=letter,
        rightMargin=0.65 * inch,
        leftMargin=0.65 * inch,
        topMargin=0.65 * inch,
        bottomMargin=0.65 * inch,
        title="50 GitHub Repos AI Operators",
        author="@piyush.glitch",
    )

    story = []
    story.append(Paragraph("50 GitHub Repos AI Operators", h1))
    story.append(Paragraph("Full Appendix + Setup Notes", h2))
    story.append(Spacer(1, 0.2 * inch))
    story.append(
        Paragraph(
            "This guide compiles 50 real repositories across Claude, MCP, agents, Cursor/coding workflows, "
            "automation, eval/observability, and retrieval infrastructure. Use it as a build map, not a shopping list.",
            body,
        )
    )
    story.append(Spacer(1, 0.15 * inch))
    story.append(Paragraph("Operator rule: pick one workflow, then one repo per layer.", small))
    story.append(PageBreak())

    categories = []
    for row in REPOS:
        if row[0] not in categories:
            categories.append(row[0])

    for category in categories:
        story.append(Paragraph(category, h2))
        story.append(Spacer(1, 0.08 * inch))
        rows = [["Repository", "What it does", "Why operators use it", "Setup note"]]
        for cat, repo, what, why, setup in REPOS:
            if cat == category:
                rows.append([repo, what, why, setup])
        table = Table(rows, colWidths=[1.65 * inch, 1.7 * inch, 2.1 * inch, 1.55 * inch], repeatRows=1)
        table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EF5E45")),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("FONTSIZE", (0, 0), (-1, 0), 9),
                    ("FONTSIZE", (0, 1), (-1, -1), 8.6),
                    ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                    ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#FCFAF3")),
                    ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#D8CFB8")),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 5),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                    ("TOPPADDING", (0, 0), (-1, -1), 4),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ]
            )
        )
        story.append(table)
        story.append(Spacer(1, 0.18 * inch))
        story.append(Paragraph("Tip: verify repo activity and docs before production adoption.", small))
        story.append(PageBreak())

    story.append(Paragraph("Setup Notes For Operators", h2))
    story.append(Spacer(1, 0.1 * inch))
    for note in SETUP_NOTES:
        story.append(Paragraph(f"- {note}", body))
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph("Starter Stack Patterns", h2))
    story.append(Spacer(1, 0.08 * inch))
    for stack in STACK_PATTERNS:
        story.append(Paragraph(f"- {stack}", body))
    story.append(Spacer(1, 0.2 * inch))
    story.append(
        Paragraph(
            "Comment AI on the post to get this file + the implementation checklist version.",
            small,
        )
    )

    doc.build(story)
    return 0


if __name__ == "__main__":
    raise SystemExit(build())
