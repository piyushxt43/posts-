# -*- coding: utf-8 -*-
"""Extended PDF blocks for batch5 carousels."""

BATCH5_EXTENDED = {
    "34_50_Hidden_GitHub_Repos": {
        "carousel_slides": [
            ("1", "50 Hidden GitHub Repos AI Operators Use Before Everyone Else", "Insider repository stack for ops."),
            ("2", "The 5 Buckets That Matter", "Connector, agent, eval, orchestration, data."),
            ("3", "MCP Repos Most Teams Miss", "Servers, SDKs, inspector, catalogs."),
            ("4", "Claude Skills And Hook Infra", "Reusable workflows and guardrails."),
            ("5", "Agent Frameworks Actually Shipping", "Frameworks that run production loops."),
            ("6", "Eval And Monitoring Stack", "Regression, safety, and traces."),
            ("7", "Ops Automation And Data Backbone", "Schedulers, metadata, retrieval, BI."),
            ("8", "Comment AI", "Claim full 50-repo appendix."),
        ],
        "extra_sections": [
            {
                "tab": "04",
                "title": "Reference appendix: all 50 repos",
                "body": [
                    "Every repository below is real, with direct GitHub URL, purpose, setup one-liner, and why "
                    "operators use it.",
                ],
            },
            {
                "tab": "05",
                "title": "MCP connectors and tooling (10)",
                "bullets": [
                    ("1. modelcontextprotocol/servers", "https://github.com/modelcontextprotocol/servers | Official reference MCP servers for filesystem, GitHub, DB, Slack-style tools | Setup: npm i -g @modelcontextprotocol/server-* | Why: fastest path to trusted connector primitives."),
                    ("2. modelcontextprotocol/typescript-sdk", "https://github.com/modelcontextprotocol/typescript-sdk | TypeScript SDK to build MCP clients/servers | Setup: npm i @modelcontextprotocol/sdk | Why: production-grade typed server tooling."),
                    ("3. modelcontextprotocol/python-sdk", "https://github.com/modelcontextprotocol/python-sdk | Python SDK for MCP implementations | Setup: pip install mcp | Why: easiest Python path for internal connectors."),
                    ("4. modelcontextprotocol/inspector", "https://github.com/modelcontextprotocol/inspector | Debug and inspect MCP traffic/tool schemas | Setup: npm i -g @modelcontextprotocol/inspector | Why: validates tool contracts before prod."),
                    ("5. punkpeye/awesome-mcp-servers", "https://github.com/punkpeye/awesome-mcp-servers | Curated list of MCP servers | Setup: browse + clone target server | Why: discovery layer for proven connectors."),
                    ("6. upstash/context7", "https://github.com/upstash/context7 | Context retrieval service pattern for agent workflows | Setup: docker run upstash/context7 | Why: compact context serving for agent calls."),
                    ("7. simonw/llm", "https://github.com/simonw/llm | CLI for LLM workflows with plugin ecosystem | Setup: pip install llm | Why: quick local experimentation with model/tool workflows."),
                    ("8. jina-ai/reader", "https://github.com/jina-ai/reader | Web/page reader utility for clean extraction | Setup: pip install jina-reader | Why: stable content extraction for agents."),
                    ("9. mem0ai/mem0", "https://github.com/mem0ai/mem0 | Memory layer for AI assistants/agents | Setup: pip install mem0ai | Why: durable personalization and task memory."),
                    ("10. langchain-ai/open_deep_research", "https://github.com/langchain-ai/open_deep_research | Open deep-research patterns/tools | Setup: pip install -r requirements.txt | Why: research-agent scaffolding reference."),
                ],
            },
            {
                "tab": "06",
                "title": "Claude skills, hooks, and agent workflows (10)",
                "bullets": [
                    ("11. microsoft/autogen", "https://github.com/microsoft/autogen | Multi-agent conversation/runtime framework | Setup: pip install pyautogen | Why: orchestrates specialist agents at scale."),
                    ("12. crewAIInc/crewAI", "https://github.com/crewAIInc/crewAI | Role-based multi-agent orchestration | Setup: pip install crewai | Why: business-team style task delegation."),
                    ("13. langchain-ai/langgraph", "https://github.com/langchain-ai/langgraph | Stateful graph runtime for agent workflows | Setup: pip install langgraph | Why: deterministic control over agent loops."),
                    ("14. openai/openai-agents-python", "https://github.com/openai/openai-agents-python | OpenAI agents SDK/runtime patterns | Setup: pip install openai-agents | Why: robust Python agent primitives."),
                    ("15. huggingface/smolagents", "https://github.com/huggingface/smolagents | Lightweight agent framework | Setup: pip install smolagents | Why: simple, fast prototyping."),
                    ("16. all-hands-ai/OpenHands", "https://github.com/all-hands-ai/OpenHands | Open coding agent platform | Setup: docker compose up | Why: autonomous coding assistant infra."),
                    ("17. browser-use/browser-use", "https://github.com/browser-use/browser-use | Browser automation for agent actions | Setup: pip install browser-use | Why: web tasks as agent tools."),
                    ("18. browserbase/stagehand", "https://github.com/browserbase/stagehand | Browser automation SDK for agents | Setup: npm i @browserbasehq/stagehand | Why: reliable browser action layer."),
                    ("19. Aider-AI/aider", "https://github.com/Aider-AI/aider | Terminal coding pair with repo-aware edits | Setup: pip install aider-chat | Why: high-velocity coding ops."),
                    ("20. Significant-Gravitas/AutoGPT", "https://github.com/Significant-Gravitas/AutoGPT | Autonomous agent project framework | Setup: docker compose up | Why: long-running autonomous task experiments."),
                ],
            },
            {
                "tab": "07",
                "title": "Evals, observability, safety (10)",
                "bullets": [
                    ("21. openai/evals", "https://github.com/openai/evals | Eval harness and benchmark framework | Setup: pip install -e . | Why: regression gates for prompt/model changes."),
                    ("22. promptfoo/promptfoo", "https://github.com/promptfoo/promptfoo | Prompt and model evaluation CLI | Setup: npm i -g promptfoo | Why: fast automated evals in CI."),
                    ("23. langfuse/langfuse", "https://github.com/langfuse/langfuse | LLM observability and traces | Setup: docker compose up | Why: production tracing and analytics."),
                    ("24. Arize-ai/phoenix", "https://github.com/Arize-ai/phoenix | LLM observability + eval tooling | Setup: pip install arize-phoenix | Why: drift and quality debugging."),
                    ("25. truera/trulens", "https://github.com/truera/trulens | LLM app eval and feedback metrics | Setup: pip install trulens | Why: quality scoring across runs."),
                    ("26. guardrails-ai/guardrails", "https://github.com/guardrails-ai/guardrails | Validation/guardrails for outputs | Setup: pip install guardrails-ai | Why: structured output safety."),
                    ("27. NVIDIA/garak", "https://github.com/NVIDIA/garak | LLM vulnerability scanning toolkit | Setup: pip install garak | Why: red-team safety testing."),
                    ("28. evidentlyai/evidently", "https://github.com/evidentlyai/evidently | ML/LLM monitoring and reports | Setup: pip install evidently | Why: production quality monitoring."),
                    ("29. whylabs/langkit", "https://github.com/whylabs/langkit | LLM text quality/safety metrics | Setup: pip install langkit | Why: monitor toxicity, relevance, drift."),
                    ("30. HumanSignal/label-studio", "https://github.com/HumanSignal/label-studio | Human annotation/review platform | Setup: docker run heartexlabs/label-studio | Why: human-in-loop eval datasets."),
                ],
            },
            {
                "tab": "08",
                "title": "Orchestration and workflow automation (10)",
                "bullets": [
                    ("31. n8n-io/n8n", "https://github.com/n8n-io/n8n | Low-code workflow automation | Setup: docker run n8nio/n8n | Why: quick ops automations with AI steps."),
                    ("32. apache/airflow", "https://github.com/apache/airflow | DAG scheduler/orchestrator | Setup: pip install apache-airflow | Why: mature scheduled workflow platform."),
                    ("33. PrefectHQ/prefect", "https://github.com/PrefectHQ/prefect | Python-native orchestration platform | Setup: pip install prefect | Why: flexible modern flow orchestration."),
                    ("34. dagster-io/dagster", "https://github.com/dagster-io/dagster | Data-aware orchestration and assets | Setup: pip install dagster | Why: strong data workflow lineage."),
                    ("35. temporalio/temporal", "https://github.com/temporalio/temporal | Durable workflow engine | Setup: brew install temporal && temporal server start-dev | Why: resilient long-running processes."),
                    ("36. microsoft/promptflow", "https://github.com/microsoft/promptflow | Prompt/LLM flow orchestration toolkit | Setup: pip install promptflow | Why: versioned AI flow execution."),
                    ("37. BerriAI/litellm", "https://github.com/BerriAI/litellm | Unified LLM gateway/proxy | Setup: pip install litellm | Why: multi-model routing and governance."),
                    ("38. ollama/ollama", "https://github.com/ollama/ollama | Local model runtime manager | Setup: brew install ollama | Why: private/local inference workflows."),
                    ("39. vllm-project/vllm", "https://github.com/vllm-project/vllm | High-throughput LLM serving engine | Setup: pip install vllm | Why: cost-efficient model serving."),
                    ("40. apache/superset", "https://github.com/apache/superset | BI and dashboard platform | Setup: pip install apache-superset | Why: ops-facing analytics layer."),
                ],
            },
            {
                "tab": "09",
                "title": "Data, retrieval, metadata, BI (10)",
                "bullets": [
                    ("41. langchain-ai/langchain", "https://github.com/langchain-ai/langchain | LLM app building blocks | Setup: pip install langchain | Why: broad integration ecosystem."),
                    ("42. run-llama/llama_index", "https://github.com/run-llama/llama_index | Retrieval/data framework for agents | Setup: pip install llama-index | Why: RAG-first production patterns."),
                    ("43. qdrant/qdrant", "https://github.com/qdrant/qdrant | Vector database engine | Setup: docker run qdrant/qdrant | Why: fast semantic retrieval."),
                    ("44. weaviate/weaviate", "https://github.com/weaviate/weaviate | Open-source vector DB | Setup: docker compose up | Why: retrieval with built-in modules."),
                    ("45. milvus-io/milvus", "https://github.com/milvus-io/milvus | Scalable vector database | Setup: docker compose up | Why: large-scale embedding search."),
                    ("46. chroma-core/chroma", "https://github.com/chroma-core/chroma | Embedding DB for AI apps | Setup: pip install chromadb | Why: lightweight local-first retrieval."),
                    ("47. deepset-ai/haystack", "https://github.com/deepset-ai/haystack | NLP/RAG orchestration framework | Setup: pip install farm-haystack | Why: enterprise retrieval pipelines."),
                    ("48. dbt-labs/dbt-core", "https://github.com/dbt-labs/dbt-core | Analytics engineering transformation framework | Setup: pip install dbt-core | Why: trusted data models for AI workflows."),
                    ("49. datahub-project/datahub", "https://github.com/datahub-project/datahub | Metadata platform/data catalog | Setup: docker compose -f quickstart.yml up | Why: discoverable, governed data assets."),
                    ("50. open-metadata/OpenMetadata", "https://github.com/open-metadata/OpenMetadata | Open metadata and lineage platform | Setup: docker compose up | Why: data context and lineage for agent reliability."),
                ],
            },
        ],
        "hidden_tricks": [
            "Pick one repo from each layer and ship in 7 days; do not 'research' for 7 weeks.",
            "Treat eval repos as mandatory before any write tool goes live.",
            "Connector catalogs are discovery tools, not install-everything lists.",
            "Model gateway repos like litellm simplify routing and spend control quickly.",
            "Durable workflow engines (Temporal/Prefect/Dagster) prevent long-task state loss.",
            "Observability repos pay for themselves the first time a loop runs wild.",
        ],
    },
}

BATCH5_FAQS = {
    "34_50_Hidden_GitHub_Repos": [
        ("Are these real repos?", "Yes, every entry in the appendix uses a real github.com repository URL."),
        ("Should I install all 50?", "No. Pick one workflow and build a thin stack first."),
        ("Where do I start?", "Start with connectors + one agent framework + promptfoo + one scheduler."),
        ("How do I control risk?", "Read-only first, eval gates second, write actions last."),
        ("How do I prove ROI?", "Track intervention rate and cost per successful workflow."),
    ],
}

BATCH5_CASE_STUDIES = {
    "34_50_Hidden_GitHub_Repos": (
        "A 9-person ops team replaced spreadsheet-heavy weekly reporting with a thin stack from this list: "
        "modelcontextprotocol/servers for connectors, langgraph for stateful agent flow, promptfoo for release "
        "gates, n8n for scheduling, and langfuse for traces. They launched in 12 days, cut manual prep time by "
        "68%, and held intervention rate under 10% by blocking writes until eval pass rates stabilized."
    ),
}

BATCH5_REFERENCE_APPENDIX = {
    "34_50_Hidden_GitHub_Repos": {
        "title": "Reference: stack assembly worksheet",
        "body": [
            "Use this quick worksheet to assemble your first production stack from the 50 repos.",
        ],
        "bullets": [
            ("Workflow", "Define one recurring task with clear done-state."),
            ("Connector", "Pick one MCP/tooling repo and stay read-only first."),
            ("Runtime", "Pick one agent framework only."),
            ("Eval", "Add at least 10 golden cases before write enablement."),
            ("Orchestration", "Schedule recurring execution with one tool."),
            ("Observe", "Trace runs and review intervention rate weekly."),
        ],
        "code": {
            "caption": "7-day launch plan",
            "lines": "Day 1: workflow + owner\nDay 2: connector read-only\nDay 3: agent runtime MVP\nDay 4: eval cases (10)\nDay 5: scheduler integration\nDay 6: observability wiring\nDay 7: pilot + scorecard",
        },
    },
}

BATCH5_TROUBLESHOOTING = {
    "34_50_Hidden_GitHub_Repos": {
        "title": "Troubleshooting your first stack",
        "body": [
            "Too many tools, no output: narrow to one workflow and one tool per layer.",
            "Good demos, bad production: add eval gates and run them in CI before prompt/model changes.",
            "Runaway costs: cap tool calls per run and monitor traces for loops.",
            "Bad writes: enforce read/write split and approval for mutations.",
            "Low team adoption: package stack choices into a one-page SOP and owner checklist.",
        ],
    },
}

BATCH5_MASTERY_PATH = {
    "34_50_Hidden_GitHub_Repos": [
        "Week 1: Pick one workflow, install one connector and one agent runtime.",
        "Week 2: Build 10 eval cases and block writes until they pass.",
        "Week 3: Add scheduler and production traces, run a small pilot.",
        "Week 4: Measure intervention rate and cost per success; tune stack.",
        "Month 2: Expand to second workflow by cloning the template.",
        "Month 3: Quarterly stack review, prune unused repos and lock standards.",
    ],
}

BATCH5_EXPERT_DEPTH = {
    "34_50_Hidden_GitHub_Repos": {
        "title": "How senior operators choose repos",
        "body": [
            "Senior teams choose by failure modes, not by stars. They ask: which repo reduces our highest-risk failure "
            "this quarter? They enforce one owner per layer, version stack decisions in docs, and run evals on every "
            "prompt/model/tool update. Their advantage is disciplined integration, not bigger tool lists.",
        ],
    },
}

BATCH5_CLOSING_NOTES = {
    "34_50_Hidden_GitHub_Repos": [
        "This repo list is your map, not your backlog.",
        "Ship one workflow with one repo per layer this week.",
        "Keep writes gated until eval pass rates are stable.",
        "Track intervention rate and cost per success, weekly.",
        "Comment AI for the updated appendix in future drops.",
        "Follow @piyush.glitch for operator-grade AI stacks.",
    ],
}
# -*- coding: utf-8 -*-
"""Extended PDF blocks for carousel 31."""

BATCH5_EXTENDED = {
    "31_50_Claude_Skills_Nobody_Set_Up": {
        "carousel_slides": [
            ("1", "50 Claude Skills Nobody Set Up", "The hidden operating layer for serious teams."),
            ("2", "Skill #1: PR Security Sentinel", "Risk-first pull request review with exploit lens."),
            ("3", "Skill #7: Incident Timeline Builder", "Builds postmortems from logs and commits."),
            ("4", "Skill #13: Migration Choreographer", "Expand-contract DB migration planning."),
            ("5", "Skill #24: GTM Message Calibrator", "Audience-specific message rewrites with guardrails."),
            ("6", "Skill #33: Agent Eval Gatekeeper", "Blocks changes when eval quality drops."),
            ("7", "Skill #45: Skill Drift Auditor", "Finds stale skills and trigger mismatches."),
            ("8", "Comment AI", "Get all 50 skills and setup snippets."),
        ],
        "extra_sections": [
            {
                "tab": "04",
                "title": "Top 6 high-value picks from the 50",
                "body": [
                    "These are the six most practical first installs for operators building a production-ready "
                    "Claude workflow stack. Each one removes repeated manual overhead in a measurable way."
                ],
                "bullets": [
                    ("#1 PR Security Sentinel", "Reads diff, lists exploit paths first, then test and blast-radius gaps."),
                    ("#7 Incident Timeline Builder", "Correlates deploys, logs and tickets into a minute-by-minute timeline."),
                    ("#13 Migration Choreographer", "Creates expand-contract steps, rollback plan, and cutover checklist."),
                    ("#24 GTM Message Calibrator", "Rewrites messaging by persona with forbidden-claims constraints."),
                    ("#33 Agent Eval Gatekeeper", "Runs scenario suite and blocks merges on safety regressions."),
                    ("#45 Skill Drift Auditor", "Flags stale descriptions, broken examples and missing verification steps."),
                ],
            },
            {
                "tab": "05",
                "title": "All 50 real Claude skills (non-generic)",
                "body": [
                    "Grouped by operator function so teams can stage implementation instead of dumping 50 files at once."
                ],
                "bullets": [
                    ("Engineering reliability (1-10)", "PR Security Sentinel; Diff Blast Radius Mapper; Test Gap Finder; API Contract Verifier; Rollback Play Author; CI Flake Triage; Incident Timeline Builder; Error Budget Narrator; Dependency Risk Radar; Secret Exposure Scout."),
                    ("Data and migrations (11-20)", "Schema Drift Detector; Query Plan Examiner; Migration Choreographer; Backfill Sequencer; Data Quality Assertion Writer; PII Boundary Scanner; ETL Failure Explainer; Metric Definition Enforcer; Dashboard Annotation Drafter; Forecast Sanity Checker."),
                    ("Product + GTM (21-30)", "Feature Spec Interrogator; Changelog Storyteller; Win-Loss Pattern Miner; GTM Message Calibrator; ICP Signal Extractor; Objection Library Builder; Demo Script Personalizer; Launch Brief Generator; Offer Positioning Critic; Competitive Claim Verifier."),
                    ("Operations and support (31-40)", "SOP Distiller; Runbook Gap Finder; Agent Eval Gatekeeper; Escalation Summary Composer; SLA Breach Forecaster; Queue Priority Scorer; Support Macro Refiner; Hand-off Checklist Builder; Vendor Risk Recapper; Meeting Decision Logger."),
                    ("AI platform hygiene (41-50)", "Prompt Regression Tracker; Tool Permission Minimizer; Skill Trigger Phrase Optimizer; Reference Pack Curator; Skill Drift Auditor; Cost Leak Finder; Context Window Compressor; Memory Freshness Checker; Hook Policy Validator; Skill ROI Reporter."),
                ],
            },
            {
                "tab": "06",
                "title": "SKILL.md starter template (copy and customize)",
                "body": [
                    "Use this as the base contract for every new skill. Keep the body practical, not poetic."
                ],
                "code": {
                    "caption": ".claude/skills/pr-security-sentinel/SKILL.md",
                    "lines": "---\nname: pr-security-sentinel\ndescription: Review pull request diffs for exploitable risks, unsafe defaults, auth gaps, and missing security tests. Use when asked to review a PR, diff, or release risk.\nallowed-tools: Read, Grep, Glob\ndisallowed-tools: Bash\n---\n## Purpose\nPerform risk-first PR review.\n## Inputs\nGit diff, related ticket, architecture notes.\n## Steps\n1. List top 5 security risks first.\n2. Map blast radius by module.\n3. Check for missing tests and validation.\n4. Provide ship/no-ship recommendation.\n## Never\nDo not focus on style-only nitpicks.\n## Output\n## Risks\n## Test Gaps\n## Recommendation",
                },
            },
            {
                "tab": "07",
                "title": "Invocation flags that teams misconfigure",
                "body": [
                    "Invocation controls should match risk profile. Side-effect workflows need stricter defaults than read-only analysis skills."
                ],
                "code": {
                    "caption": "Manual-only deploy skill frontmatter",
                    "lines": "---\nname: deploy-prod\ndescription: Deploy production services with preflight checks.\ndisable-model-invocation: true\nuser-invocable: true\nallowed-tools: Bash, Read\n---",
                },
                "pro_tip": {
                    "title": "Risk rule",
                    "text": "If a skill can write, deploy, notify customers, or mutate data, make invocation explicit and auditable.",
                },
            },
            {
                "tab": "08",
                "title": "Progressive disclosure pattern",
                "body": [
                    "Keep SKILL.md short and point to deeper reference docs and scripts. This avoids loading giant context unless the skill actually runs."
                ],
                "code": {
                    "caption": "Skill directory shape",
                    "lines": ".claude/skills/\n  incident-timeline-builder/\n    SKILL.md\n    references/\n      log-taxonomy.md\n      severity-mapping.md\n    examples/\n      incident-2026-04.md\n    scripts/\n      parse_timestamps.py",
                },
            },
            {
                "tab": "09",
                "title": "GitHub patterns for team skill libraries",
                "body": [
                    "Treat skills like product code. Give each skill an owner, tests, changelog, and review policy."
                ],
                "bullets": [
                    ("Repo layout", "Store project skills in .claude/skills/ and mirror docs in /docs/skills/."),
                    ("CODEOWNERS", "Require domain-owner review for high-risk skills (deploy, legal, finance)."),
                    ("PR template", "Include: changed trigger phrases, behavior delta, risk impact, rollback."),
                    ("Golden tests", "Run 3-5 fixed prompts per skill after each edit."),
                    ("Versioning", "Tag quarterly releases of skill packs used across repos."),
                ],
            },
            {
                "tab": "10",
                "title": "Rollout roadmap: 50 skills without chaos",
                "body": [
                    "Install in waves. Start with reliability and review skills, then operational and GTM layers."
                ],
                "bullets": [
                    ("Week 1", "Deploy 6 core reliability skills and baseline metrics."),
                    ("Week 2", "Add 8 data/migration and support ops skills."),
                    ("Week 3", "Add GTM and product communication skills."),
                    ("Week 4", "Enable AI hygiene pack: drift, cost, context and memory monitors."),
                    ("Month 2", "Retire low-ROI skills and strengthen high-impact ones."),
                ],
            },
        ],
        "hidden_tricks": [
            "Descriptions are the highest-leverage field - spend time there first.",
            "Counter-examples prevent repeated bad outputs better than extra adjectives.",
            "Keep scripts deterministic; let the model reason around them, not replace them.",
            "Split read-only analysis skills from side-effect action skills.",
            "Use disallowed-tools to prevent accidental shell use in audit workflows.",
            "Track skill usage counts weekly and kill unused skills aggressively.",
            "Run a monthly trigger-phrase audit to reduce accidental auto-selection.",
        ],
    }
}

BATCH5_FAQS = {
    "31_50_Claude_Skills_Nobody_Set_Up": [
        ("Do I need all 50 skills immediately?", "No. Start with 6 high-impact skills and expand in waves."),
        ("What is the fastest first skill to ship?", "PR Security Sentinel or Incident Timeline Builder."),
        ("How long should SKILL.md be?", "Usually under 300-500 lines, with depth moved to references/."),
        ("Should deploy skills auto-invoke?", "Generally no - keep high-impact actions explicit and reviewed."),
        ("How do we avoid skill sprawl?", "Add owners, usage tracking, and quarterly cleanup."),
        ("Can skills be tested?", "Yes. Use golden prompt sets and compare output shape each revision."),
        ("Where should skills live?", "Project-specific in .claude/skills/ for team workflows."),
        ("How do we prove ROI?", "Track edit-time reduction, fewer re-prompts, and incident prevention."),
    ],
}

BATCH5_CASE_STUDIES = {
    "31_50_Claude_Skills_Nobody_Set_Up": (
        "A 22-person SaaS team moved from ad-hoc prompts to a 14-skill starter pack. They deployed PR Security "
        "Sentinel, Migration Choreographer, Incident Timeline Builder, and Skill Drift Auditor first. In 6 weeks, "
        "code review cycle time dropped 31%, rollback incidents fell from 4 to 1, and support postmortems were "
        "published within 24 hours consistently. Their biggest gain came from versioning skills in git with "
        "CODEOWNERS, not from changing models."
    ),
}

BATCH5_REFERENCE_APPENDIX = {
    "31_50_Claude_Skills_Nobody_Set_Up": {
        "title": "Reference: 10-minute skill setup checklist",
        "body": [
            "Use this checklist for each new skill. Fast setup now avoids messy behavior later."
        ],
        "bullets": [
            ("1) Name + description", "Clear trigger phrases and specific workflow scope."),
            ("2) Inputs + steps", "List required artifacts and ordered procedure."),
            ("3) Constraints", "Add never-do rules and failure behavior."),
            ("4) Output contract", "Define exact headings/JSON shape expected."),
            ("5) Example pair", "One good output and one counter-example."),
            ("6) Invocation policy", "Set disable-model-invocation/user-invocable as needed."),
            ("7) Tool policy", "Set allowed/disallowed tools before production usage."),
            ("8) Git controls", "Owner, tests, changelog entry, PR review."),
        ],
        "code": {
            "caption": "Skill PR checklist snippet",
            "lines": "- [ ] Description includes trigger phrases\n- [ ] Invocation flags reviewed\n- [ ] Tool scope least-privilege\n- [ ] Golden prompts updated\n- [ ] Owner approved\n- [ ] Changelog entry added",
        },
    }
}

BATCH5_TROUBLESHOOTING = {
    "31_50_Claude_Skills_Nobody_Set_Up": {
        "title": "Troubleshooting skill libraries at scale",
        "body": [
            "Skill triggers unpredictably: narrow descriptions and remove overlapping phrasing.",
            "Too much context usage: move long guidance from SKILL.md into references/.",
            "Unsafe behavior in action skills: tighten invocation and tool policies immediately.",
            "Team ignores skills: add slash aliases and lightweight onboarding docs.",
            "Output quality drift: refresh examples and run golden prompt regression checks.",
        ],
    }
}

BATCH5_MASTERY_PATH = {
    "31_50_Claude_Skills_Nobody_Set_Up": [
        "Week 1: Launch 6 core skills and baseline current workflow metrics.",
        "Week 2: Add 10 skills across reliability and operations.",
        "Week 3: Add GTM/product skill pack with strict output contracts.",
        "Week 4: Add hygiene skills for drift, cost, and context management.",
        "Month 2: Remove low-usage skills and improve top 12 with examples.",
        "Month 3: Cross-repo skill versioning and quarterly skill review ritual.",
    ]
}

BATCH5_EXPERT_DEPTH = {
    "31_50_Claude_Skills_Nobody_Set_Up": {
        "title": "What senior operators do differently",
        "body": [
            "They treat skill descriptions as routing infrastructure, not documentation fluff.",
            "They split skill classes into read-only analysis and explicit-action workflows.",
            "They run lightweight regression prompts every time a skill is edited.",
            "They assign owners and retirement criteria for every skill in the library.",
            "They optimize for fewer repeated explanations, not more clever prompts.",
        ],
    }
}

BATCH5_CLOSING_NOTES = {
    "31_50_Claude_Skills_Nobody_Set_Up": [
        "If a task repeats, it deserves a skill.",
        "Start with the 6 high-value picks, not all 50 at once.",
        "Protect side-effect skills with strict invocation and tool policies.",
        "Version skills in git so improvements compound across the team.",
        "Comment AI on the post to get the full 50-skill pack and templates.",
        "Follow @piyush.glitch for advanced AI operator systems.",
    ]
}
# -*- coding: utf-8 -*-
"""Extended PDF blocks for carousel 35 with 50 practical shipping patterns."""

BATCH5_EXTENDED = {
    "35_50_AI_Agents_That_Ship": {
        "carousel_slides": [
            ("", "50 AI Agents That Ship", "Not hype threads. Field-tested workflows."),
            ("", "Pattern #1", "Inbound lead qualification triage."),
            ("", "Pattern #2", "Weekly metrics narrative draft."),
            ("", "Pattern #3", "Support ticket risk escalation."),
            ("", "Pattern #4", "Code review and regression gate."),
            ("", "Pattern #5", "Outbound personalization prep."),
            ("", "Pattern #6", "Ops audit and exception digest."),
            ("", "Comment AI", "Get all 50 with templates."),
        ],
        "extra_sections": [
            {
                "tab": "04",
                "title": "How to read the 50 patterns",
                "body": [
                    "Each pattern follows the same operator schema so teams can implement quickly: function category, "
                    "trigger, required inputs, output contract, eval checks, approval gate, and owner. This keeps "
                    "agents portable across GPT/Claude/Cursor without rewriting your operating model.",
                ],
                "code": {
                    "caption": "Pattern card template",
                    "lines": "FUNCTION: sales|ops|research|content|code\nTRIGGER: schedule|event|manual\nINPUTS: connectors + context docs\nOUTPUT: strict schema\nEVAL: success + safety + tool correctness\nAPPROVAL: required write actions\nOWNER: named human",
                },
            },
            {
                "tab": "05",
                "title": "50 shipping patterns by function",
                "body": [
                    "Below are 50 workflows businesses are actually running. Use them as templates, not as prompts."
                ],
                "bullets": [
                    ("Research (1-10)", "1) Competitor launch monitor 2) Pricing diff report 3) Market claim verifier 4) Regulatory change brief 5) Earnings call summarizer 6) Customer review theme extraction 7) Sales call objection miner 8) Vendor risk scan 9) Feature gap intelligence digest 10) Weekly strategic signal memo"),
                    ("Ops (11-20)", "11) Incident postmortem draft 12) SLA breach early warning 13) Inventory exception digest 14) Billing anomaly triage 15) Contract renewal risk flagger 16) Hiring pipeline hygiene audit 17) Finance close checklist tracker 18) Compliance evidence collector 19) Procurement cycle blocker summary 20) Leadership weekly KPI narrative"),
                    ("Content (21-30)", "21) Newsletter first draft 22) Webinar recap repurposer 23) FAQ freshness audit 24) Case-study skeleton writer 25) Product update changelog formatter 26) Executive memo formatter 27) Landing page variant generator 28) Social post series planner 29) Content calendar gap finder 30) Localization quality checker"),
                    ("Code (31-40)", "31) PR risk-first reviewer 32) Migration plan drafter 33) Test gap analyzer 34) Release-note synthesizer 35) Dependency vulnerability digest 36) Incident rollback playbook draft 37) API docs drift detector 38) Bug reproduction hypothesis generator 39) Refactor blast-radius mapper 40) CI failure triage assistant"),
                    ("Sales (41-50)", "41) Inbound lead qualification 42) Account research brief 43) Discovery prep packet 44) Follow-up email draft with objections 45) Renewal expansion signal detector 46) Proposal risk checker 47) Meeting summary to CRM notes 48) Deal desk exception summarizer 49) Lost-deal reason clustering 50) Weekly pipeline coaching digest"),
                ],
            },
            {
                "tab": "06",
                "title": "Eval gates that keep these alive",
                "body": [
                    "Every pattern should pass three eval groups before rollout and on every change: task success, "
                    "safety boundaries, and tool correctness. If one fails, the workflow does not ship.",
                ],
                "code": {
                    "caption": "Eval gate checklist",
                    "lines": "TASK: output schema valid + required fields present\nSAFETY: no forbidden claims/actions\nTOOLS: correct tool, args, timing\nOPS: no loops, timeout, spend cap respected\nRESULT: block release on any red",
                },
            },
            {
                "tab": "07",
                "title": "Approval flows that prevent expensive mistakes",
                "body": [
                    "Shipping teams separate draft actions from committed actions. Agents can prepare recommendations, "
                    "draft updates, and stage changes automatically; humans approve sends, submits, deletes, budget moves, "
                    "and external-facing commits.",
                ],
                "bullets": [
                    ("Draft allowed", "Draft doc, draft email, draft ticket, summary update."),
                    ("Approval required", "Send customer email, mutate CRM fields, pause ads, merge critical PRs."),
                    ("Hard blocked", "Bulk delete, irreversible financial action, policy-violating command."),
                ],
            },
            {
                "tab": "08",
                "title": "Rollout plan: from one agent to fifty patterns",
                "body": [
                    "Do not launch 50 at once. Build one stable pattern in each function first, then clone with the same "
                    "schema, eval gate, and ownership model. Most teams can deploy 8-12 reliable workflows in one quarter, "
                    "then scale to 50 over time.",
                ],
                "pro_tip": {
                    "title": "Scale rule",
                    "text": "Clone only workflows with intervention rate under 15% for four consecutive weeks. Anything "
                            "higher means your context, tools, or output contract is not stable yet.",
                },
            },
        ],
        "hidden_tricks": [
            "Use one cheap classifier agent to route tasks to the right workflow pattern before calling heavy models.",
            "Keep output schemas strict (JSON/table sections) so evals remain deterministic across model updates.",
            "Log prompt version and connector version together - most regressions are tool/schema drift, not model IQ.",
            "Treat failed runs as product bugs: patch the pattern card, add test case, redeploy.",
            "Default to read-only for new connectors for at least two weeks.",
            "For code workflows, pair cloud execution with local human review before merge.",
            "If a workflow needs frequent manual correction, narrow scope before changing models.",
        ],
    },
}

BATCH5_FAQS = {
    "35_50_AI_Agents_That_Ship": [
        ("Do I need all 50 agents?", "No. Start with 3-5 high-friction workflows and expand after stability."),
        ("Which platform should I start with?", "Use the platform your team already runs daily; operational design matters more than brand."),
        ("What is the first KPI to track?", "Intervention rate per workflow. It predicts trust and scale readiness."),
        ("How many eval cases are enough?", "Start with 15-20 real cases, then add failures from production weekly."),
        ("Should agents write directly to systems?", "Only after read-only reliability and approval flows are proven."),
        ("How do I choose what to automate first?", "Pick recurring tasks with clear inputs, outputs, and business owner."),
        ("What kills agent programs fastest?", "No ownership, no eval gate, and broad permissions too early."),
        ("How long until ROI?", "Most teams see measurable time savings in 2-6 weeks on first workflow."),
    ],
}

BATCH5_CASE_STUDIES = {
    "35_50_AI_Agents_That_Ship": (
        "A 35-person services company ran 11 agent pilots in two months. Eight failed due to broad scope and no gates. "
        "They rebooted with the ship-ready pattern card: narrow task, strict output schema, read-first permissions, 18 "
        "golden evals, and approval on writes. In 6 weeks, they stabilized five workflows (lead triage, pipeline digest, "
        "support escalation, release note drafting, invoice anomaly checks) and reduced weekly manual ops by 22 hours."
    ),
}

BATCH5_REFERENCE_APPENDIX = {
    "35_50_AI_Agents_That_Ship": {
        "title": "Reference: ship-ready agent checklist",
        "body": ["Use this before launching any new workflow pattern."],
        "bullets": [
            ("Scope", "One workflow, one owner, one done-state."),
            ("Inputs", "Named connectors + required context docs."),
            ("Output", "Strict format contract with required fields."),
            ("Gates", "Task + safety + tool evals passing."),
            ("Approval", "Explicit list of actions requiring human confirm."),
            ("Monitoring", "Intervention rate, cost per success, failure reasons."),
        ],
        "code": {
            "caption": "Launch gate",
            "lines": "if eval_pass_rate < 95%: block\nif safety_failures > 0: block\nif intervention_rate > 15%: iterate_scope\nif all_green: enable_limited_rollout",
        },
    },
}

BATCH5_TROUBLESHOOTING = {
    "35_50_AI_Agents_That_Ship": {
        "title": "Troubleshooting shipping issues",
        "body": [
            "Agent output drifts weekly: lock output schema and add golden examples.",
            "Tool calls are wrong: narrow tool descriptions and argument validation.",
            "High intervention rate: scope too broad; split into two simpler workflows.",
            "Unexpected costs: enforce spend cap and limit retries/loop behavior.",
            "Low team adoption: unclear owner or no measurable business KPI tied to workflow.",
        ],
    },
}

BATCH5_MASTERY_PATH = {
    "35_50_AI_Agents_That_Ship": [
        "Week 1: select 3 workflows and define pattern cards.",
        "Week 2: deploy read-only versions with strict output contracts.",
        "Week 3: add eval gates and incident logging.",
        "Week 4: add approval flows for high-impact writes.",
        "Month 2: clone stable patterns into adjacent functions.",
        "Month 3: expand toward 20+ workflows with shared governance.",
    ],
}

BATCH5_EXPERT_DEPTH = {
    "35_50_AI_Agents_That_Ship": {
        "title": "What shipping teams do differently",
        "body": [
            "They optimize for intervention rate, not demo impressiveness.",
            "They make every workflow auditable with prompt/tool/version logs.",
            "They treat connector permissions as product decisions, not defaults.",
            "They harvest production failures into eval cases within 48 hours.",
            "They scale by cloning proven patterns, not by creating net-new agents each week.",
            "They keep human approval where business risk is asymmetric.",
        ],
    },
}

BATCH5_CLOSING_NOTES = {
    "35_50_AI_Agents_That_Ship": [
        "Shipping agents is an operations discipline, not a prompting trick.",
        "Start narrow, instrument everything, and gate every consequential write.",
        "Use these 50 patterns as templates and adapt per function owner.",
        "Measure intervention rate weekly to decide what scales next.",
        "Comment AI on the post for the full implementation templates.",
        "Follow @piyush.glitch for field-tested AI operator workflows.",
    ],
}
# -*- coding: utf-8 -*-
"""Extended PDF blocks for batch 5 carousels."""

BATCH5_EXTENDED = {
    "32_50_Hidden_Prompts_That_Ship": {
        "carousel_slides": [
            ("", "50 Hidden Prompts That Ship", "Claude + GPT prompts for real business outputs."),
            ("", "Ops Prompt", "Executive dashboard synthesis with hard schema."),
            ("", "Content Prompt", "Scroll-stopping hook generator with constraints."),
            ("", "Code Prompt", "Refactor plan with test contract and rollback."),
            ("", "Sales Prompt", "Account strategy brief before outreach."),
            ("", "Research Prompt", "Source-graded insight memo with confidence."),
            ("", "Prompt Contract", "XML tags + prefill + non-goals."),
            ("", "Comment AI", "Get all 50 copy-paste prompts."),
        ],
        "extra_sections": [
            {
                "tab": "04",
                "title": "Ops prompts (10)",
                "body": [
                    "These prompts reduce daily operational chaos by forcing structure and decision-ready outputs.",
                ],
                "code": {
                    "caption": "Ops #1 - Executive daily dashboard synthesis",
                    "lines": "<context>\nCompany: {{company_name}}\nAudience: {{exec_role}}\nDate range: {{date_range}}\n</context>\n<data>\nPaste KPI exports from CRM, analytics and support here.\n</data>\n<rules>\nUse only provided data. If missing, write UNKNOWN.\nNo invented percentages. Keep to decision-critical points.\n</rules>\n<output_contract>\nReturn EXACTLY:\n1) KPI Snapshot table: Metric | Current | Prior | Delta | Confidence(High/Med/Low)\n2) 3 Risks (owner + suggested mitigation)\n3) 3 Opportunities (owner + next action)\n4) One-paragraph executive summary <=120 words\n</output_contract>\n<non_goals>\nNo motivational tone, no generic advice, no repeated KPI definitions.\n</non_goals>",
                },
            },
            {
                "tab": "05",
                "title": "Content prompts (10)",
                "body": [
                    "These prompts focus on hooks, angle clarity, and reusable content formats with strict style constraints.",
                ],
                "code": {
                    "caption": "Content #3 - Hook stack for carousels",
                    "lines": "<context>\nTopic: {{topic}}\nAudience: {{audience}}\nBrand voice: {{brand_voice}}\nPlatform: Instagram carousel\n</context>\n<rules>\nGenerate hooks that are specific, contrarian, and business-outcome driven.\nNo generic lines like 'Here are tips'.\n</rules>\n<output_contract>\nReturn 12 hooks in a table:\nHook | Pattern Used (Contrarian/Data/Warning/Status) | Why It Scroll-Stops (<=12 words)\nThen return top 3 selected hooks with a one-line rationale each.\n</output_contract>\n<prefill>\nDesired emotional trigger: {{trigger}}\nForbidden words: {{forbidden_words}}\n</prefill>\n<non_goals>\nNo clickbait lies, no all-caps spam, no vague promises.\n</non_goals>",
                },
            },
            {
                "tab": "06",
                "title": "Code prompts (10)",
                "body": [
                    "Code prompts here emphasize safe change planning, regression checks, and auditable decisions.",
                ],
                "code": {
                    "caption": "Code #6 - Refactor with rollback contract",
                    "lines": "<context>\nRepository: {{repo_name}}\nModule: {{module_path}}\nConstraint: {{constraints}}\n</context>\n<goal>\nRefactor for {{target_outcome}} without changing external behavior.\n</goal>\n<rules>\nPrefer small reversible edits.\nList assumptions before edits.\nDefine rollback for each risky step.\n</rules>\n<output_contract>\nReturn sections exactly:\nA) Risk map (Low/Med/High with justification)\nB) Step-by-step refactor plan (numbered)\nC) Test plan (unit/integration/manual)\nD) Rollback plan (trigger + action)\nE) Done criteria checklist\n</output_contract>\n<non_goals>\nNo broad rewrites, no API signature changes unless explicitly requested.\n</non_goals>",
                },
            },
            {
                "tab": "07",
                "title": "Sales prompts (10)",
                "body": [
                    "Sales prompts are tuned for account preparation, objection handling and conversion-quality messaging.",
                ],
                "code": {
                    "caption": "Sales #2 - Account strategy brief",
                    "lines": "<context>\nAccount: {{account_name}}\nSegment: {{segment}}\nGoal: {{goal}}\n</context>\n<data>\nPaste CRM notes, recent interactions, buying committee details, and renewal timeline.\n</data>\n<rules>\nGround every claim in provided data.\nFlag uncertainty with UNKNOWN.\nFocus on decision influence, not generic rapport tips.\n</rules>\n<output_contract>\nReturn exactly:\n1) Account state summary (<=90 words)\n2) Stakeholder map table: Name | Role | Influence | Priority Message\n3) Objection forecast: Objection | Evidence-backed response | Proof asset needed\n4) Next 3 actions with owner and deadline\n</output_contract>\n<non_goals>\nNo fake personalization, no unverifiable ROI claims.\n</non_goals>",
                },
            },
            {
                "tab": "08",
                "title": "Research prompts (10)",
                "body": [
                    "Research prompts prioritize source quality, evidence confidence and decision-ready synthesis.",
                ],
                "code": {
                    "caption": "Research #4 - Evidence-graded insight memo",
                    "lines": "<context>\nResearch question: {{question}}\nDecision owner: {{owner}}\nTime horizon: {{horizon}}\n</context>\n<sources>\nPaste source excerpts with URLs and dates.\n</sources>\n<rules>\nSeparate facts from inference.\nScore evidence confidence High/Med/Low with reason.\nPrefer recent sources unless historical context is required.\n</rules>\n<output_contract>\nReturn:\nI) Key findings table: Finding | Evidence | Confidence | Source\nII) Contradictions and data gaps\nIII) Decision options (3) with trade-offs\nIV) Recommendation with explicit assumptions\n</output_contract>\n<non_goals>\nNo unsourced claims, no pretending certainty where evidence is weak.\n</non_goals>",
                },
            },
            {
                "tab": "09",
                "title": "Prompt contract skeleton (reuse everywhere)",
                "body": [
                    "Use this skeleton to convert any generic prompt into a ship-ready one.",
                ],
                "code": {
                    "caption": "Universal ship-ready prompt skeleton",
                    "lines": "<context>{{business context}}</context>\n<input_data>{{raw data}}</input_data>\n<goal>{{single explicit objective}}</goal>\n<rules>{{always/never rules}}</rules>\n<output_contract>{{exact schema + limits}}</output_contract>\n<prefill>{{variables to replace}}</prefill>\n<quality_checks>{{self-check list before final}}</quality_checks>\n<non_goals>{{what output must avoid}}</non_goals>",
                },
                "pro_tip": {
                    "title": "Operator shortcut",
                    "text": "When output quality drops, tighten output_contract first, then non_goals. These two fields "
                            "usually fix inconsistency faster than rewriting the whole prompt.",
                },
            },
        ],
        "hidden_tricks": [
            "Put XML blocks in the same order every time; consistency improves model compliance.",
            "Keep non_goals short and sharp (3-5 items) to avoid ambiguity.",
            "Add a quality_checks block to force the model to validate its own output before finalizing.",
            "Use confidence labels (High/Med/Low) whenever claims depend on partial data.",
            "If outputs are verbose, enforce strict word caps in output_contract.",
            "For team reuse, store prompts as templates with {{variables}} and examples.",
            "Run one small eval set on key prompts after model version changes.",
        ],
    },
}

BATCH5_FAQS = {
    "32_50_Hidden_Prompts_That_Ship": [
        ("Do these prompts work in both Claude and GPT?", "Yes. They use platform-agnostic structure with XML tags and strict contracts."),
        ("Why include non-goals?", "Non-goals prevent drift, hallucinated additions, and unnecessary verbosity."),
        ("Can I remove XML tags?", "You can, but output reliability usually drops when sections are not clearly delimited."),
        ("How many prompts should I deploy first?", "Start with 3-5 high-impact prompts in one workflow, then expand."),
        ("What if data is missing?", "The prompts require UNKNOWN instead of invented values."),
        ("How do I adapt for my company?", "Replace {{variables}} in <prefill> and adjust output_contract fields."),
        ("Are these beginner prompts?", "No. They are designed for production business workflows with constraints."),
        ("How do I measure success?", "Track intervention rate, time saved, and accepted-output rate per prompt."),
    ],
}

BATCH5_CASE_STUDIES = {
    "32_50_Hidden_Prompts_That_Ship": (
        "A 9-person growth team replaced five ad-hoc prompt docs with this contract format (XML tags + output "
        "schema + non-goals). Within three weeks, content revision loops dropped by 42%, sales prep quality rose, "
        "and weekly ops brief generation went from 90 minutes to 25 minutes of human review."
    ),
}

BATCH5_REFERENCE_APPENDIX = {
    "32_50_Hidden_Prompts_That_Ship": {
        "title": "Reference: 50-prompt deployment checklist",
        "body": ["Use this before rolling prompts into daily workflows."],
        "bullets": [
            ("Scope", "Pick one workflow and 3 prompts first."),
            ("Template", "Enforce XML blocks in consistent order."),
            ("Contract", "Define exact output shape and quality checks."),
            ("Safety", "Add non-goals and UNKNOWN rule for missing data."),
            ("Measure", "Track intervention rate and accepted-output rate weekly."),
            ("Version", "Store prompt revisions and examples in one shared folder."),
        ],
        "code": {
            "caption": "Prompt file naming",
            "lines": "ops-01-exec-dashboard.md\ncontent-03-hook-stack.md\ncode-06-refactor-plan.md\nsales-02-account-brief.md\nresearch-04-evidence-memo.md",
        },
    },
}

BATCH5_TROUBLESHOOTING = {
    "32_50_Hidden_Prompts_That_Ship": {
        "title": "Troubleshooting ship-ready prompts",
        "body": [
            "Output too generic: tighten output_contract and add one counter-example.",
            "Model invents facts: add UNKNOWN rule and source-only constraints in <rules>.",
            "Too verbose: enforce section-by-section word caps in output_contract.",
            "Inconsistent formatting: keep XML block order fixed and explicit.",
            "Team confusion: centralize prompt templates and version notes in one repo/folder.",
        ],
    },
}

BATCH5_MASTERY_PATH = {
    "32_50_Hidden_Prompts_That_Ship": [
        "Day 1: deploy 3 prompts in one workflow and capture outputs.",
        "Week 1: score outputs against contract and refine weak sections.",
        "Week 2: expand to 10 prompts across two categories.",
        "Week 3: add quality_checks and UNKNOWN rule to all active prompts.",
        "Week 4: publish internal prompt library with owners and examples.",
        "Month 2: run monthly review and retire low-performing prompts.",
    ],
}

BATCH5_EXPERT_DEPTH = {
    "32_50_Hidden_Prompts_That_Ship": {
        "title": "What prompt operators do differently",
        "body": [
            "They optimize for accepted output, not clever wording.",
            "They treat output_contract like an API schema: strict and testable.",
            "They keep prompts short but constraints explicit.",
            "They maintain a counter-example set from real failures.",
            "They version prompts and review changes like production assets.",
        ],
    },
}

BATCH5_CLOSING_NOTES = {
    "32_50_Hidden_Prompts_That_Ship": [
        "Generic prompts do not scale; contract-driven prompts do.",
        "Start with one workflow and prove accepted-output gains quickly.",
        "Use XML tags, format contracts, prefill, and non-goals as your baseline stack.",
        "Track intervention rate to identify your top shipping prompts.",
        "Comment AI on the post to get the full 50-prompt pack.",
        "Follow @piyush.glitch for operator-grade prompt systems.",
    ],
}
# -*- coding: utf-8 -*-
"""Extended PDF blocks for carousel 33 (Cursor secrets)."""

BATCH5_EXTENDED = {
    "33_50_Cursor_Agent_Secrets": {
        "carousel_slides": [
            ("", "50 Cursor Agent Secrets", "Developer + business owner hook."),
            ("", "Secret 1-10", "Cursor 3 and Composer 2 foundations."),
            ("", "Secret 11-20", "Plan Mode and architecture flow."),
            ("", "Secret 21-30", "Rules and .mdc patterns."),
            ("", "Secret 31-40", "Hooks, safety, and auto-fix loops."),
            ("", "Secret 41-46", "/worktree and parallel workflows."),
            ("", "Secret 47-50", "Cloud handoff and scaling pattern."),
            ("", "Comment AI", "Get full secret pack and templates."),
        ],
        "extra_sections": [
            {
                "tab": "04",
                "title": "10 secrets: Cursor 3 and Composer 2",
                "body": [
                    "1) Treat each agent run as a worker lifecycle, not a chat thread.",
                    "2) Keep Composer 2 as default for exploration and low-risk implementation.",
                    "3) Use stronger models only for high-stakes choices to control spend.",
                    "4) Put outcome in first sentence of prompt; model follows early tokens strongly.",
                    "5) Ask for 'risk list first' to avoid optimistic implementations.",
                    "6) For refactors, request impacted modules map before edits.",
                    "7) Use one-line success criteria to prevent prompt drift.",
                    "8) Separate discovery and implementation prompts explicitly.",
                    "9) Keep context focused: remove obsolete tabs and stale logs.",
                    "10) Re-run with same objective after rule changes to validate behavior shift.",
                ],
                "code": {
                    "caption": "Prompt skeleton for stable runs",
                    "lines": "Goal: <one sentence>\nConstraints: <must/must-not>\nDeliverable: <files + format>\nSuccess checks: <tests/lint/output>\nFirst output: risk list, then plan, then edits",
                },
            },
            {
                "tab": "05",
                "title": "10 secrets: Plan Mode mastery",
                "body": [
                    "11) Start any multi-file task in Plan Mode.",
                    "12) Ask for dependency graph in plan output.",
                    "13) Require explicit rollback path for risky changes.",
                    "14) Force plan to identify unknowns before coding.",
                    "15) Ask for migration blast radius estimates.",
                    "16) Break plan into independently testable phases.",
                    "17) Reject plans without verification steps.",
                    "18) Ask plan to name files likely to conflict in parallel work.",
                    "19) Convert accepted plan bullets into checkboxes.",
                    "20) Save good plan templates as team snippets.",
                ],
                "pro_tip": {
                    "title": "Plan review rule",
                    "text": "If a plan does not include failure modes and rollback, it is not ready for code. "
                            "Five extra minutes in planning often saves hours of repair.",
                },
            },
            {
                "tab": "06",
                "title": "10 secrets: .cursor/rules and .mdc",
                "body": [
                    "21) Move from legacy `.cursorrules` to `.cursor/rules/*.mdc`.",
                    "22) Keep one rule file per concern: API, testing, security, style.",
                    "23) Use narrow globs to avoid irrelevant context injection.",
                    "24) Keep always-on rules under ~150 lines.",
                    "25) Put examples in rules, not abstract adjectives.",
                    "26) Add explicit NEVER items for dangerous behaviors.",
                    "27) Include exact test/lint commands in rules.",
                    "28) Version rule changes like code with review.",
                    "29) Add task-trigger phrases in descriptions.",
                    "30) Re-evaluate rules monthly to remove stale constraints.",
                ],
                "code": {
                    "caption": ".cursor/rules/api.mdc example",
                    "lines": "---\ndescription: API conventions for server routes\nglobs: server/**/*.ts\nalwaysApply: false\n---\n- Validate request bodies with zod\n- snake_case JSON response keys\n- Never log PII in request/response bodies",
                },
            },
            {
                "tab": "07",
                "title": "10 secrets: hooks and enforcement",
                "body": [
                    "31) Use pre-action hook to block secrets in shell commands.",
                    "32) Use post-edit hook to run formatter automatically.",
                    "33) Add deny patterns for force-push and destructive shell commands.",
                    "34) Return clear block reason so agents self-correct quickly.",
                    "35) Keep hook scripts fast; slow hooks cause dev friction.",
                    "36) Log blocked events for policy tuning.",
                    "37) Use hooks for mandatory checks, not prompts.",
                    "38) Add bounded test-fix loop hooks with max retries.",
                    "39) Split security hooks from style hooks.",
                    "40) Treat hook config as audited infra, not personal preference.",
                ],
                "code": {
                    "caption": ".cursor/hooks.json concept",
                    "lines": "{\n  \"beforeBash\": [{ \"command\": \"node .cursor/hooks/secret-guard.js\" }],\n  \"afterEdit\": [{ \"command\": \"npm run lint -- --fix\" }]\n}",
                },
            },
            {
                "tab": "08",
                "title": "10 secrets: /worktree, parallelism, cloud handoff",
                "body": [
                    "41) Use `/worktree` before any parallel agent execution.",
                    "42) Assign one objective per worktree, not mixed tasks.",
                    "43) Merge smallest-safe branch first to reduce conflicts.",
                    "44) Keep branch naming tied to task intent, not person.",
                    "45) Use parallel agents for independent files/modules only.",
                    "46) Run a review agent before applying parallel outputs.",
                    "47) Start long work in cloud when runtime exceeds local patience window.",
                    "48) Use cloud-to-local handoff for final checks with local tooling.",
                    "49) Store environment assumptions in repo config, not memory.",
                    "50) Maintain a 'known-good parallel workflow' template for onboarding.",
                ],
                "code": {
                    "caption": "Parallel workflow mini-template",
                    "lines": "Plan Mode -> split into 3 independent tasks\n/worktree task-a\n/worktree task-b\n/worktree task-c\nRun agents in parallel\nReview diffs\nApply/merge in risk order",
                },
            },
        ],
        "hidden_tricks": [
            "Ask for 'files likely touched' before implementation to surface scope quickly.",
            "Use a review-focused agent run that only critiques risk and tests.",
            "When stuck, ask model to explain why plan might fail before coding.",
            "Pin one rule file as onboarding baseline for every new project.",
            "Keep a library of proven prompts for recurring engineering tasks.",
            "For parallel runs, define merge order before spawning agents.",
            "Use cloud runs for exhaustive test-fix cycles overnight.",
        ],
    },
}

BATCH5_FAQS = {
    "33_50_Cursor_Agent_Secrets": [
        ("Is Composer 2 enough for most tasks?", "Yes for exploration and low/medium-risk implementation; escalate on high-risk reasoning."),
        ("When should I use Plan Mode?", "Any task with multiple files, architectural decisions, or unclear requirements."),
        ("Do I need /worktree every time?", "Use it whenever running parallel agents or isolated experiments."),
        ("Rules or hooks first?", "Rules shape behavior; hooks enforce safety. Start with core rules, then add critical hooks."),
        ("Can hooks replace code review?", "No. Hooks automate checks; human review still validates intent and product impact."),
        ("How do I avoid rule bloat?", "Split rules by concern and keep always-on context minimal."),
        ("When is cloud handoff worth it?", "Long-running tasks, heavy refactors, or overnight execution."),
        ("What metric proves improvement?", "Track lead time, rework rate, and human intervention frequency."),
    ]
}

BATCH5_CASE_STUDIES = {
    "33_50_Cursor_Agent_Secrets": (
        "A 9-person product team adopted Plan Mode + scoped .mdc rules + /worktree parallelism for weekly feature "
        "work. They ran one planning pass, split implementation into two independent worktrees, and used hooks to "
        "auto-lint and block risky shell commands. Lead time for medium features dropped from 4.2 days to 2.6 days, "
        "and post-merge fix PRs dropped by nearly half because architecture and safety checks happened earlier."
    )
}

BATCH5_REFERENCE_APPENDIX = {
    "33_50_Cursor_Agent_Secrets": {
        "title": "Reference: Cursor secrets quick card",
        "body": ["Use this as your operating checklist before running production-facing agent tasks."],
        "bullets": [
            ("Plan first", "Review architecture and rollback before code."),
            ("Rules scoped", "Use .mdc globs to keep context relevant."),
            ("Hooks active", "Block secrets and enforce post-edit hygiene."),
            ("/worktree", "Isolate parallel tasks to avoid branch collisions."),
            ("Cloud handoff", "Offload long tasks; finalize locally."),
            ("Measure outcomes", "Track rework and intervention rates."),
        ],
        "code": {
            "caption": "Daily high-signal sequence",
            "lines": "1) Plan Mode\n2) /worktree for each independent task\n3) Run agents\n4) Review + tests\n5) Merge smallest-risk diff first",
        },
    }
}

BATCH5_TROUBLESHOOTING = {
    "33_50_Cursor_Agent_Secrets": {
        "title": "Troubleshooting Cursor workflows",
        "body": [
            "Parallel edits conflict: use separate /worktree per task and avoid shared hotspot files.",
            "Rules ignored: check .mdc glob scope and application mode; broad rules can be skipped or diluted.",
            "Hook not firing: validate event key and command path; ensure script exits with expected codes.",
            "Plan quality weak: require explicit unknowns and verification steps before accepting plan.",
            "Cloud run drifted: hand off back local and run targeted review + test pass before merge.",
        ],
    }
}

BATCH5_MASTERY_PATH = {
    "33_50_Cursor_Agent_Secrets": [
        "Week 1: Adopt Plan Mode for every multi-file task.",
        "Week 2: Migrate conventions to scoped .mdc rules.",
        "Week 3: Add core hooks for secrets and formatting.",
        "Week 4: Run first /worktree parallel feature cycle.",
        "Month 2: Introduce cloud handoff for long jobs.",
        "Month 3: Track lead-time and intervention metrics monthly.",
    ]
}

BATCH5_EXPERT_DEPTH = {
    "33_50_Cursor_Agent_Secrets": {
        "title": "What expert Cursor teams do",
        "body": [
            "They treat prompts as temporary and rules/hooks as durable infrastructure.",
            "They demand architecture clarity before edits, not after failed implementation.",
            "They isolate concurrency with worktrees and merge by risk order.",
            "They keep rule sets minimal, explicit, and versioned with review.",
            "They measure outcome metrics, not 'number of agent runs'.",
        ],
    }
}

BATCH5_CLOSING_NOTES = {
    "33_50_Cursor_Agent_Secrets": [
        "Cursor power comes from systems, not one perfect prompt.",
        "Start with Plan Mode, scoped rules, and two core hooks this week.",
        "Use /worktree whenever you parallelize to avoid self-inflicted merge pain.",
        "Escalate models by risk and keep Composer 2 as your daily default.",
        "Measure lead-time and rework so improvements are visible to leadership.",
        "Comment AI for the full secret templates and checklists.",
    ]
}
