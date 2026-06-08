# -*- coding: utf-8 -*-
"""Base PDF content for batch5 carousels (31+)."""

BATCH5_CONTENT = {
    "34_50_Hidden_GitHub_Repos": {
        "title": "50 Hidden GitHub Repos For AI Business Ops",
        "subtitle": "A real operator stack for MCP, agents, evals, and automation.",
        "kicker": "AI FOR BUSINESS - 34",
        "pdf_filename": "50-hidden-github-repos.pdf",
        "intro": (
            "Most AI teams share the same 5 obvious repos. Operators who actually ship AI business workflows use a "
            "deeper stack: MCP servers and SDKs for connectors, agent frameworks for execution loops, eval stacks for "
            "release gating, orchestration tools for workflows, and data/observability layers for reliability. This "
            "guide gives you 50 real repositories with direct GitHub URLs, what each does, setup one-liners, and why "
            "operators choose them in production."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "How to use this repo list",
                "body": [
                    "Do not install all 50. Pick one workflow (for example: weekly pipeline digest), then select one "
                    "repo per layer: connector, agent runtime, eval, orchestration, and monitoring. Production wins "
                    "come from a coherent stack, not a giant bookmark list.",
                ],
                "bullets": [
                    ("Step 1", "Pick your highest-value recurring workflow."),
                    ("Step 2", "Start read-only on connectors and tools."),
                    ("Step 3", "Add evals before enabling writes."),
                    ("Step 4", "Track intervention rate and cost per successful run."),
                ],
            },
            {
                "tab": "02",
                "title": "Five bucket map",
                "body": [
                    "The 50 repos are grouped into five practical buckets so you can assemble a stack faster: MCP "
                    "connectors, agent frameworks, eval and observability, orchestration and automation, and data "
                    "backbone plus retrieval.",
                ],
                "bullets": [
                    ("MCP", "Connector servers, SDKs, and connector catalogs."),
                    ("Agents", "Frameworks, coding agents, browser agents."),
                    ("Evals", "Regression, safety, and traces."),
                    ("Automation", "Workflow orchestrators and schedulers."),
                    ("Data", "Vector DBs, metadata, and BI layers."),
                ],
            },
            {
                "tab": "03",
                "title": "Starter stack recommendation",
                "body": [
                    "For most business ops teams, a strong starter stack is: MCP connector layer + one agent "
                    "framework + eval gate + one orchestrator + one observability tool. Keep it narrow for 30 days, "
                    "then expand only from measured pain points.",
                ],
                "bullets": [
                    ("Connectors", "modelcontextprotocol/servers + upstash/context7"),
                    ("Agent loop", "langchain-ai/langgraph or microsoft/autogen"),
                    ("Evals", "promptfoo/promptfoo + openai/evals"),
                    ("Orchestration", "n8n-io/n8n or PrefectHQ/prefect"),
                    ("Observability", "langfuse/langfuse or Arize-ai/phoenix"),
                ],
            },
        ],
        "playbook": [
            "Select one recurring ops workflow and document done-state.",
            "Install one connector repo and validate read-only answers.",
            "Pick one agent framework and ship a minimal end-to-end flow.",
            "Add an eval suite before any write actions.",
            "Wire one scheduler/orchestrator for recurring execution.",
            "Track success rate, intervention rate, latency, and cost weekly.",
        ],
        "mistakes": [
            "Installing too many frameworks before one workflow is stable.",
            "Connecting write tools before eval gates exist.",
            "No ownership for repo updates and dependency drift.",
            "Treating stars as quality without production validation.",
            "Skipping observability until after the first incident.",
        ],
        "glossary": [
            ("MCP", "Model Context Protocol: standard interface between agents and tools."),
            ("Agent Framework", "Library/runtime that manages planning, tool use, and state."),
            ("Eval Gate", "Automated tests that block unsafe model/prompt/tool changes."),
            ("Intervention Rate", "How often a human has to fix or override the agent."),
            ("Cost per Success", "Total workflow spend divided by successful outcomes."),
        ],
        "callout": {
            "title": "Operator principle",
            "text": "One workflow, one stack, one scorecard. Compounding wins beat tool tourism.",
        },
    },
}
# -*- coding: utf-8 -*-
"""Base PDF content for carousel 35: 50 AI agents that actually ship."""

BATCH5_CONTENT = {
    "35_50_AI_Agents_That_Ship": {
        "title": "50 AI Agents That Ship (Not Demo)",
        "subtitle": "Field-tested agent workflows with eval gates, narrow scope, and human approval paths.",
        "kicker": "AI FOR BUSINESS - AGENTS",
        "pdf_filename": "50-ai-agents-that-ship.pdf",
        "intro": (
            "Most agent content is theater: broad prompts, no boundaries, and no safety rails. It demos well and "
            "fails in production. Operators shipping real workflows in 2026 use a different pattern: one narrow job, "
            "clear done-state, strict tool permissions, eval gates before release, and approval for any consequential "
            "write. This guide distills what business owners actually run using ChatGPT Agent mode, Claude agents, and "
            "Cursor cloud agents, with 50 practical workflow patterns you can deploy this quarter."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "Why 90% of agents never ship",
                "body": [
                    "Most failed agents are designed like a pitch deck, not an operations process. Teams ask one agent "
                    "to do ten jobs, connect every tool on day one, and skip acceptance criteria. The result is fragile "
                    "automation that needs constant babysitting.",
                    "Shipping teams treat agents like junior operators with strict scope: one role, one workflow, one "
                    "owner, one KPI. They gate writes, log every action, and harden only after read-only reliability is proven.",
                ],
                "bullets": [
                    ("Too broad", "One 'do everything' agent creates unpredictable behavior and tool misuse."),
                    ("No gates", "Without evals and approvals, quality drift reaches production silently."),
                    ("No owner", "Agents without a named owner decay into stale prompts and broken connectors."),
                ],
            },
            {
                "tab": "02",
                "title": "The ship-ready architecture",
                "body": [
                    "A production agent loop is simple and repeatable: define a narrow task, run in read-first mode, "
                    "measure against golden cases, then enable controlled writes. This pattern works across GPT, Claude, "
                    "and Cursor because it is operational design, not model branding.",
                ],
                "bullets": [
                    ("Narrow scope", "One workflow with fixed input, output schema, and done-state."),
                    ("Eval gate", "Golden scenarios for success, safety, and tool correctness before release."),
                    ("Approval flow", "Human confirmation on sends, submits, budget changes, and data mutations."),
                    ("Observability", "Log model, prompt version, tool calls, latency, failures, and intervention rate."),
                ],
            },
            {
                "tab": "03",
                "title": "Platform reality: what businesses actually use",
                "body": [
                    "ChatGPT Agent mode is strong for browser automation, recurring assistant tasks, and quick operator "
                    "research with approvals. Claude agents excel where SOP-heavy workflows, custom skills, and strict "
                    "tool governance matter. Cursor cloud agents dominate engineering workflows that need repo context, "
                    "parallel worktrees, and long-running refactors.",
                ],
                "bullets": [
                    ("ChatGPT Agent mode", "Great for research, admin tasks, and scheduled repetitive work."),
                    ("Claude agents", "Best for structured workflows with Skills, Hooks, MCP, and reusable SOPs."),
                    ("Cursor cloud agents", "Best for codebase-native execution and parallel engineering streams."),
                ],
            },
        ],
        "playbook": [
            "Pick one high-friction recurring workflow and define the done-state in one sentence.",
            "Launch read-only first with a strict output format and named workflow owner.",
            "Build 15-20 golden eval cases from real incidents and edge scenarios.",
            "Add approval gates for every consequential write action.",
            "Track intervention rate and cost per successful run weekly.",
            "Clone the pattern to adjacent workflows only after 4 straight weeks of stable performance.",
        ],
        "mistakes": [
            "Comparing models before defining workflow boundaries and ownership.",
            "Turning on write permissions before proving read-only reliability.",
            "Measuring output style instead of intervention rate and business outcomes.",
            "Skipping incident-to-eval feedback loops after failures.",
        ],
        "glossary": [
            ("Agent workflow", "A repeatable task loop with fixed inputs, outputs, and success checks."),
            ("Eval gate", "A test suite that blocks prompt/model/tool changes if quality drops."),
            ("Approval flow", "Human confirmation step before high-impact actions execute."),
            ("Intervention rate", "How often a person must step in to correct an agent run."),
            ("Cost per success", "Total run cost divided by successful completed outcomes."),
        ],
        "callout": {
            "title": "Operator rule",
            "text": "Treat every agent like a process, not a personality: narrow scope, explicit gates, named owner, "
                    "and logged actions. That is how 'AI demo' becomes business infrastructure.",
        },
    },
}
