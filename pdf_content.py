"""
Detailed, topic-specific content for the 10 carousel bonus guides.

Each entry is keyed by the carousel folder slug and contains rich, non-generic
copy that gets rendered into a branded PDF by build_pdfs.py.

Schema per topic:
{
  "title":     str   # cover headline
  "subtitle":  str   # one-line promise under the headline
  "kicker":    str   # small label e.g. "AI FOR BUSINESS - 01"
  "intro":     str   # opening paragraph (the "why")
  "sections":  [ {"tab": str, "title": str, "body": [str, ...], "bullets": [(lead, text), ...]} ]
  "playbook":  [str, ...]   # numbered quick-start steps
  "mistakes":  [str, ...]   # what to avoid
  "glossary":  [(term, definition), ...]
  "callout":   {"title": str, "text": str}   # highlighted pro tip
}
"""

CONTENT = {
    "01_Claude_Code_Agent_Teams": {
        "title": "Claude Code as an Agent Team",
        "subtitle": "Stop using it like a chatbot. Run it like an engineering org.",
        "kicker": "AI FOR BUSINESS - 01",
        "intro": (
            "Most people open Claude Code, type a request, and judge it on a single reply. "
            "That is using a Formula 1 car to drive to the mailbox. The real leverage in 2026 is "
            "orchestration: one main agent that plans and delegates, plus specialised helpers that "
            "explore, build, test and review in parallel. The model quality matters, but the moat is "
            "the surface around it - project memory, tool access via MCP, subagents, hooks and skills - "
            "wired into the way software actually ships."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "Subagents: protect your context",
                "body": [
                    "A subagent is a separate Claude session with its own context window, system prompt, "
                    "tool permissions and even its own model. The orchestrator spawns them, they do focused "
                    "work, and they hand back only a summary - not the raw noise."
                ],
                "bullets": [
                    ("Explore agent", "read-only, often a cheaper/faster model, searches the codebase so raw files never flood your main thread."),
                    ("Builder agent", "edits in small reversible steps with write access scoped to the files it needs."),
                    ("Reviewer agent", "critiques the diff for risk, security and tests before anything ships."),
                    ("Why it wins", "context hygiene. Failed experiments and giant search dumps stay out of the main reasoning budget."),
                ],
            },
            {
                "tab": "02",
                "title": "Hooks: deterministic guardrails",
                "body": [
                    "Hooks are scripts that fire on lifecycle events - before/after a tool call, on session "
                    "start, on stop, on subagent completion. Unlike a prompt request, a hook always runs. That "
                    "is how you turn 'please remember to lint' into a rule the agent cannot skip."
                ],
                "bullets": [
                    ("command", "shell script that can block a dangerous action (e.g. refuse to commit a secret)."),
                    ("prompt / agent", "a quick LLM or subagent check: 'does this look like a credential?'"),
                    ("http / mcp_tool", "route to a central policy service or an external security scanner."),
                ],
            },
            {
                "tab": "03",
                "title": "Skills + MCP + Memory",
                "body": [
                    "Skills are reusable packaged instructions (a SKILL.md with goal, steps, constraints and "
                    "examples) you teach once and invoke forever. MCP connectors give the agent live access to "
                    "GitHub, Jira, Postgres, Figma or Slack through one standard interface. Memory keeps "
                    "conventions, architecture notes and vocabulary alive across sessions."
                ],
                "bullets": [
                    ("Skills", "encode taste: PR-review standard, release-note format, migration checklist."),
                    ("MCP", "encode reach: implement from a Jira ticket, query the DB, update from Figma."),
                    ("Memory", "encode continuity: stop re-explaining your stack in every new chat."),
                ],
            },
        ],
        "playbook": [
            "Write a CLAUDE.md with your stack, conventions and 'never do' rules.",
            "Add one Skill for a workflow you repeat weekly (e.g. PR review).",
            "Add a hook that blocks commits containing secrets or skips tests.",
            "Connect one MCP server you actually use (GitHub or your DB).",
            "Run work as: Plan -> Explore (read-only) -> Build -> Test + Review in parallel.",
        ],
        "mistakes": [
            "Dumping the whole repo into one chat instead of using an Explore subagent.",
            "Giving every subagent full write + shell access 'to be safe'. It is the opposite of safe.",
            "Relying on a prompt to enforce a rule that should be a deterministic hook.",
            "Never writing memory, so the agent forgets your architecture every session.",
        ],
        "glossary": [
            ("Orchestrator", "The main agent that plans and delegates to subagents."),
            ("Subagent", "Isolated Claude session with its own context, tools and model."),
            ("Hook", "Event-driven script that runs automatically around tool calls."),
            ("Skill", "Reusable instruction bundle (SKILL.md) invoked on demand."),
            ("MCP", "Model Context Protocol - the standard way agents reach external tools."),
        ],
        "callout": {
            "title": "The pro move",
            "text": "Give read-heavy work to a cheap, fast model in an Explore subagent and reserve your "
                    "strongest model for the orchestrator's planning and the reviewer's judgement. You get "
                    "better answers and lower cost at the same time.",
        },
    },

    "02_ChatGPT_Workspace_Agents": {
        "title": "ChatGPT Workspace Agents",
        "subtitle": "The shift from a personal chatbot to shared, always-on team automation.",
        "kicker": "AI FOR BUSINESS - 02",
        "intro": (
            "Workspace agents are the evolution of custom GPTs. A GPT was a scoped prompt owned by one "
            "person. A workspace agent is a shared, persistent worker - powered by Codex in the cloud - that "
            "any authorised teammate can invoke. It can use files, run code, call connected apps, remember "
            "what it learned and keep working across multiple steps even after you log off. That is the line "
            "between a chatbot and an automation platform."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "Three capabilities GPTs never had",
                "body": [
                    "The defining change is that workspace agents run on the same agentic model family that "
                    "powers computer-use. Reasoning, code execution, file handling and web search are native, "
                    "not bolted on."
                ],
                "bullets": [
                    ("Cloud persistence", "the agent runs server-side and continues long tasks while you are away."),
                    ("Deep tool access", "60+ built-in connectors plus custom MCP servers for anything else."),
                    ("Scheduling", "triggers can start work automatically - a true 'set it and it runs' workflow."),
                ],
            },
            {
                "tab": "02",
                "title": "Where to point it first",
                "body": [
                    "Pick workflows that already have clear inputs and outputs. Ambiguous, taste-heavy work is "
                    "a bad first target; repeatable operations with a defined result are ideal."
                ],
                "bullets": [
                    ("Weekly pipeline report", "pull CRM data, summarise movement, flag at-risk deals."),
                    ("Support macro audit", "review tickets, surface recurring issues, draft better canned replies."),
                    ("Release notes", "turn merged PRs and commit history into a clean changelog."),
                    ("Lead research", "enrich a list of prospects with context before outreach."),
                ],
            },
            {
                "tab": "03",
                "title": "Control before scale",
                "body": [
                    "Shared, always-on agents that can write data are powerful and risky. The teams that win "
                    "design the control model before they scale usage."
                ],
                "bullets": [
                    ("Role-based access", "admins decide who can run which agent."),
                    ("Tool allow-lists", "a reporting agent should not have delete permissions."),
                    ("Approval steps", "write actions to production systems require a human confirm."),
                    ("Audit logs", "every run records user, prompt, tool calls and outputs."),
                ],
            },
        ],
        "playbook": [
            "Open Agents in the ChatGPT sidebar and describe one workflow your team repeats.",
            "Scope its tools to the minimum it needs to finish the job.",
            "Add an approval step for any action that writes to a real system.",
            "Pilot with one department and one measurable outcome.",
            "Track time saved, error rate and manual handoffs removed - then expand.",
        ],
        "mistakes": [
            "Starting with a vague, creative workflow instead of a measurable one.",
            "Granting broad write access on day one.",
            "No logging, so you cannot explain what the agent did or why.",
            "Treating an impressive demo as proof of production reliability.",
        ],
        "glossary": [
            ("Workspace agent", "Shared, persistent, Codex-powered worker inside ChatGPT."),
            ("Connector", "Built-in integration to an app like Slack, Drive or Salesforce."),
            ("Trigger", "An event or schedule that starts an agent automatically."),
            ("Role-based access", "Permissions that decide who can run or edit an agent."),
        ],
        "callout": {
            "title": "The pro move",
            "text": "Build the agent once, but treat it like a product: version it, collect failure cases, and "
                    "improve its instructions over time. A shared agent that quietly gets better every week "
                    "compounds across the whole team.",
        },
    },

    "03_Gemini_CLI_Beyond_Coding": {
        "title": "Gemini CLI Beyond Coding",
        "subtitle": "A 1M-token, search-grounded, multimodal agent that lives in your terminal.",
        "kicker": "AI FOR BUSINESS - 03",
        "intro": (
            "Gemini CLI is open-source and free to start, but most people stop at 'it writes code'. Its real "
            "value is that it sits where operators already work - the terminal - and combines a one-million "
            "token context window, built-in Google Search grounding, multimodal input and MCP extensibility "
            "in one local utility. That makes it a research and operations agent, not just a coding helper."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "The 1M context advantage",
                "body": [
                    "A huge context window changes the kind of work you can do without chopping everything into "
                    "tiny chunks. Whole repos, long contracts, full transcripts and dense specs can be reasoned "
                    "over in one pass."
                ],
                "bullets": [
                    ("Query large codebases", "ask questions across the whole project, not one file."),
                    ("Summarise long documents", "feed a 200-page PDF and get a grounded brief."),
                    ("Checkpointing", "save and resume long sessions so complex work is not lost."),
                ],
            },
            {
                "tab": "02",
                "title": "Grounding + multimodal",
                "body": [
                    "Built-in Google Search lets the agent refresh facts instead of guessing from stale "
                    "training data. Multimodal input means a sketch, screenshot or PDF can become the starting "
                    "point of real work."
                ],
                "bullets": [
                    ("Search grounding", "real-time facts with citations for research briefs."),
                    ("From PDF to plan", "turn a spec or sketch into an app scaffold or task list."),
                    ("Media generation", "wire in Imagen, Veo or Lyria through MCP for images and video."),
                ],
            },
            {
                "tab": "03",
                "title": "Automation with headless mode",
                "body": [
                    "Run Gemini non-interactively inside scripts and pipelines. This is where it stops being a "
                    "chat tool and becomes part of your operational plumbing."
                ],
                "bullets": [
                    ("Scheduled reports", "generate a grounded digest every morning from a cron job."),
                    ("Repo automation", "query pull requests or handle complex rebases on command."),
                    ("GEMINI.md context", "a project file that tailors behaviour the way CLAUDE.md does."),
                ],
            },
        ],
        "playbook": [
            "Install Gemini CLI and authenticate with a personal Google account to start free.",
            "Add a GEMINI.md to a project so it knows your conventions.",
            "Try a non-coding task first: summarise a long PDF with search grounding.",
            "Configure one MCP server in settings.json (docs, DB or media generation).",
            "Wrap a useful prompt in headless mode and run it from a script on a schedule.",
        ],
        "mistakes": [
            "Using it only for code and missing the research/ops value.",
            "Pasting tiny snippets when you could give it the whole document.",
            "Trusting grounded answers without an evaluation step for write actions.",
            "Never saving context to GEMINI.md, so it starts cold every time.",
        ],
        "glossary": [
            ("Context window", "How much text/data the model can consider at once (up to ~1M tokens)."),
            ("Grounding", "Using live search results to anchor answers in current facts."),
            ("Headless mode", "Running the CLI non-interactively inside scripts."),
            ("GEMINI.md", "Per-project file that gives the CLI persistent context."),
        ],
        "callout": {
            "title": "The pro move",
            "text": "Combine grounding with the big context window: feed your internal doc AND let it search "
                    "the web, then ask it to reconcile the two. You get answers that are both on-brand and "
                    "current - something neither source gives you alone.",
        },
    },

    "04_MCP_Connectors_For_Business": {
        "title": "MCP Connectors for Business",
        "subtitle": "The USB-C standard that lets any agent reach your real tools.",
        "kicker": "AI FOR BUSINESS - 04",
        "intro": (
            "Before MCP, every AI-to-tool connection was custom engineering: a different integration, auth "
            "method and failure mode for each SaaS app. The Model Context Protocol replaced that with one "
            "vendor-neutral interface. By 2026 it is the de facto standard, adopted across GitHub, Slack, "
            "Google Workspace, Salesforce, Notion, Linear and Jira - and shared by Anthropic, OpenAI and "
            "Google. Think of it as USB-C for AI agents."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "What an MCP server exposes",
                "body": [
                    "An MCP server publishes its capabilities in a structured, discoverable way so any "
                    "MCP-aware client can use them without bespoke glue code."
                ],
                "bullets": [
                    ("Tools", "actions the agent can take, with typed inputs and outputs."),
                    ("Resources", "data the agent can read (files, records, documents)."),
                    ("Prompts", "reusable prompt templates the server offers."),
                ],
            },
            {
                "tab": "02",
                "title": "The production gateway pattern",
                "body": [
                    "Connecting an agent to live business systems is where things get dangerous. A bad tool "
                    "schema becomes a bad write; a connector bug becomes a data exposure. Mature teams put MCP "
                    "behind a gateway."
                ],
                "bullets": [
                    ("Authentication", "OAuth 2.1 at the gateway, not credentials scattered in configs."),
                    ("Authorization", "role-based access; separate read tools from write tools."),
                    ("Rate limiting", "stop retry storms and runaway loops from spiking cost."),
                    ("Identity propagation", "record which human triggered which tool call."),
                ],
            },
            {
                "tab": "03",
                "title": "Observability is not optional",
                "body": [
                    "Because agents are probabilistic, you must be able to reconstruct exactly what happened. "
                    "OpenTelemetry-style tracing across the agent-gateway-server chain is the foundation."
                ],
                "bullets": [
                    ("Span per tool call", "carry client identity, tool name, latency and errors."),
                    ("Structured logs", "model version, prompt hash, inputs, outputs, timestamps."),
                    ("Health checks", "exercise the real tool path, not just process liveness."),
                ],
            },
        ],
        "playbook": [
            "List the 3 tools your agents touch most (e.g. GitHub, CRM, your DB).",
            "Adopt or build an MCP server for each instead of one-off integrations.",
            "Put them behind a gateway for auth, rate limits and logging.",
            "Split read-only tools from write tools and require approval for writes.",
            "Instrument every tool call with tracing before you scale usage.",
        ],
        "mistakes": [
            "Treating MCP servers like throwaway scripts instead of internal SDKs.",
            "Mixing read and write tools with no permission boundary.",
            "No identity propagation, so writes are untraceable.",
            "Shipping without tracing, then being unable to explain a failure.",
        ],
        "glossary": [
            ("MCP", "Model Context Protocol - standard interface between agents and tools."),
            ("MCP server", "A service that exposes tools, resources and prompts via MCP."),
            ("Gateway", "A control layer for auth, rate limiting, policy and logging."),
            ("Identity propagation", "Carrying the triggering user's identity into tool calls."),
        ],
        "callout": {
            "title": "The pro move",
            "text": "Let platform teams own MCP servers like internal SDKs and let security review one "
                    "permissions model instead of a museum of one-off integrations. New systems then arrive as "
                    "connector rollouts, not rewrites of your agent logic.",
        },
    },

    "05_AI_Skills_As_Operating_Procedures": {
        "title": "AI Skills as Operating Procedures",
        "subtitle": "Turn repeated prompts into reusable, versioned workflows.",
        "kicker": "AI FOR BUSINESS - 05",
        "intro": (
            "If you find yourself re-typing the same instructions, you do not have a prompting problem - you "
            "have a missing operating procedure. A Skill packages a repeatable job into a reusable bundle the "
            "agent loads on demand. It is the difference between explaining a task fresh every time and "
            "teaching it once so the whole team gets the same expert result."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "What a real Skill contains",
                "body": [
                    "A vibe is not a Skill. 'Be helpful and make it good' tells the model nothing repeatable. "
                    "A proper Skill is structured like an SOP."
                ],
                "bullets": [
                    ("Purpose + trigger", "what the job is and exactly when to use it."),
                    ("Inputs", "what the agent needs before it can start."),
                    ("Steps + constraints", "the procedure and the hard limits."),
                    ("Examples + output format", "one or two gold outputs and the exact shape to return."),
                ],
            },
            {
                "tab": "02",
                "title": "Good vs bad, side by side",
                "body": [
                    "Compare a PR-review Skill that says 'inspect the diff, list risks first, verify tests "
                    "exist, flag security issues, and avoid pure style nitpicks' with one that says 'review "
                    "this code well'. Only the first produces consistent output across people and sessions."
                ],
                "bullets": [
                    ("Specific beats vague", "name the steps and the order they happen in."),
                    ("Constraints create quality", "say what NOT to do, not just what to do."),
                    ("Show, do not just tell", "an example output anchors taste better than adjectives."),
                ],
            },
            {
                "tab": "03",
                "title": "Pair Skills with Hooks, then version",
                "body": [
                    "Skills tell the agent how to think; hooks enforce what must happen every time. Together "
                    "they turn a conversational tool into a programmable platform. Then treat your Skills like "
                    "product assets."
                ],
                "bullets": [
                    ("Skill = judgement", "the reusable thinking for a job."),
                    ("Hook = guarantee", "the deterministic check that always runs."),
                    ("Version control", "improve, test, review and keep a changelog."),
                ],
            },
        ],
        "playbook": [
            "Find the workflow you re-explain most often this month.",
            "Write it as: purpose, trigger, inputs, steps, constraints, output format.",
            "Add one gold example and one counter-example of a bad output.",
            "Add a verification step at the end so the agent checks its own work.",
            "Save it, reuse it, and refine it whenever it produces a weak result.",
        ],
        "mistakes": [
            "Writing aspirational adjectives instead of concrete steps.",
            "Forgetting constraints - the 'do not do this' list is half the quality.",
            "No examples, so taste drifts every run.",
            "Never updating Skills, so old mistakes repeat forever.",
        ],
        "glossary": [
            ("Skill", "A packaged, reusable instruction set for a repeatable job."),
            ("SOP", "Standard Operating Procedure - the offline equivalent of a Skill."),
            ("Constraint", "An explicit limit that prevents a class of bad outputs."),
            ("Gold example", "A reference output that defines the quality bar."),
        ],
        "callout": {
            "title": "The pro move",
            "text": "Every time the agent produces a bad output, do not just re-prompt - add a counter-example "
                    "to the Skill. Your Skills then improve the same way good documentation does: by absorbing "
                    "the failures you have already seen.",
        },
    },

    "06_AI_Image_Workflows_For_Brands": {
        "title": "AI Image Workflows for Brands",
        "subtitle": "Stop generating random images. Build a repeatable production system.",
        "kicker": "AI FOR BUSINESS - 06",
        "intro": (
            "AI can now produce campaign-quality visuals without a full production team - but the quality of "
            "the output depends entirely on the precision of the input. The brands that get consistent, "
            "on-brand results do not 'write better prompts'; they build a system: a defined brand world, a "
            "reference library, a shot list, a prompt grammar, a QC pass and an asset pipeline."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "Brand world + reference library",
                "body": [
                    "Consistency comes from constraints you decide once. Define the visual rules, then keep a "
                    "library of approved assets so every generation starts from the same DNA."
                ],
                "bullets": [
                    ("Brand world", "color, lighting, camera, materials, type, and what must NEVER appear."),
                    ("Reference library", "approved faces, products, poses, packaging and locations."),
                    ("Negative examples", "store the off-brand outputs so you can steer away from them."),
                ],
            },
            {
                "tab": "02",
                "title": "Shot list + prompt grammar",
                "body": [
                    "Treat a campaign like a real shoot with a planned set of shots, and write prompts with a "
                    "consistent structure so results are reproducible instead of lucky."
                ],
                "bullets": [
                    ("Shot list", "hero cover, packshot, lifestyle, close-up, comparison, social crop, ad variant."),
                    ("Prompt grammar", "subject + product + scene + camera + lighting + composition + text + constraints + ratio."),
                    ("Ratio first", "put the aspect/format at the very start for higher adherence."),
                ],
            },
            {
                "tab": "03",
                "title": "QC pass + asset pipeline",
                "body": [
                    "The gap between 'looks generated' and 'looks professional' is the review step and the way "
                    "you store what works."
                ],
                "bullets": [
                    ("QC checklist", "check text, hands, logos, product geometry, scale, brand colors and artifacts."),
                    ("Legal check", "confirm the image can actually be used (people, IP, trademarks)."),
                    ("Asset pipeline", "save each final with its prompt, model, references and approval status."),
                ],
            },
        ],
        "playbook": [
            "Write a one-page brand world doc (colors, lighting, camera, never-do list).",
            "Collect 10-20 approved reference images and a few negative examples.",
            "Define your standard shot list for a campaign.",
            "Adopt a prompt grammar template and put ratio/format first.",
            "Run every output through a QC checklist before it enters the library.",
        ],
        "mistakes": [
            "Compressing nothing - oversized input images cause flaky generations.",
            "Writing '4K/8K' and expecting real resolution; use proven ratio phrasing instead.",
            "Skipping QC and shipping warped hands, broken logos or wrong product shapes.",
            "Not saving prompts, so a great result can never be reproduced.",
        ],
        "glossary": [
            ("Brand world", "The fixed visual rules every asset must obey."),
            ("Shot list", "The planned set of images for a campaign."),
            ("Prompt grammar", "A consistent prompt structure for reproducible results."),
            ("Asset pipeline", "How finals are named, stored and approved into a library."),
        ],
        "callout": {
            "title": "The pro move",
            "text": "Compress input images to ~1.5MB before editing/fusion. Output resolution is driven by your "
                    "prompt's format description, not the input file size - so smaller inputs only speed things "
                    "up and improve success rate without hurting quality.",
        },
    },

    "07_Context_Engineering": {
        "title": "Context Engineering",
        "subtitle": "The real skill behind great AI output isn't the prompt - it's the context.",
        "kicker": "AI FOR BUSINESS - 07",
        "intro": (
            "Prompt tricks get you a demo. Context engineering gets you reliable work. The model can only "
            "reason over what it can see, so the highest-leverage skill is shaping that input: the goal, the "
            "source documents, the examples, the constraints, the tool results and the memory. Master this and "
            "you stop hunting for magic words."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "The context stack",
                "body": [
                    "Before you worry about phrasing, assemble the layers the model needs to do the job well."
                ],
                "bullets": [
                    ("Goal + audience", "what success looks like and who it is for."),
                    ("Source material", "the documents, data and facts it should rely on."),
                    ("Examples", "two great outputs and one bad one - taste teaches faster than adjectives."),
                    ("Output format", "the exact structure you want back."),
                ],
            },
            {
                "tab": "02",
                "title": "Constraints and tool results",
                "body": [
                    "Quality comes from boundaries and fresh data, not from longer adjectives. Constraints "
                    "reduce drift; tool results replace guessing."
                ],
                "bullets": [
                    ("Constraints", "length, tone, forbidden claims, allowed data sources, compliance rules."),
                    ("Tool results", "let the agent fetch from search, CRM, docs, analytics or the repo."),
                    ("Non-goals", "state what the answer should NOT include to prevent scope creep."),
                ],
            },
            {
                "tab": "03",
                "title": "Memory and the evaluation loop",
                "body": [
                    "Decide what should persist across sessions, and treat every bad output as a context bug "
                    "rather than a model failure."
                ],
                "bullets": [
                    ("Memory as a product", "brand voice, glossary, architecture, customer segments."),
                    ("Failures into tests", "save bad outputs, turn them into examples and tighter rules."),
                    ("Iterate the input", "fix the context, not just the wording, and the output follows."),
                ],
            },
        ],
        "playbook": [
            "Start every important task with goal, audience, sources, constraints and format.",
            "Add two gold examples and one counter-example.",
            "Give the agent a way to fetch fresh data instead of guessing.",
            "Decide what belongs in long-term memory and write it down.",
            "Keep a log of failures and convert them into context improvements.",
        ],
        "mistakes": [
            "Tuning adjectives ('be amazing') instead of adding real source material.",
            "Leaving out non-goals, then being surprised by scope creep.",
            "Letting the model guess facts it could have fetched with a tool.",
            "Treating a bad output as the model's fault instead of a context gap.",
        ],
        "glossary": [
            ("Context engineering", "Designing everything the model sees before it acts."),
            ("Context stack", "The layered inputs: goal, sources, examples, constraints, tools, memory."),
            ("Non-goal", "An explicit statement of what NOT to include."),
            ("Evaluation loop", "Turning failures into tests and better context."),
        ],
        "callout": {
            "title": "The pro move",
            "text": "Keep a running 'counter-example' file for each recurring task. Feeding the model what a bad "
                    "answer looks like is often more powerful than describing the perfect one - it draws the "
                    "boundary the model keeps crossing.",
        },
    },

    "08_Agent_Evals_As_Release_Gates": {
        "title": "Agent Evals as Release Gates",
        "subtitle": "If it can use tools or change data, vibes are not enough.",
        "kicker": "AI FOR BUSINESS - 08",
        "intro": (
            "An agent wired into real systems amplifies every weak link: a bad tool schema becomes a bad "
            "write, latency becomes compounding retries, one connector bug becomes a data exposure. The teams "
            "doing well in 2026 are not doing more prompt tinkering - they build evaluation pipelines that "
            "block releases. Evals are the unit tests of agent behaviour."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "Not trivia benchmarks - your workflows",
                "body": [
                    "Abstract 'model IQ' benchmarks tell you little once the agent is in your systems. The best "
                    "evals are your own edge cases: refund policy, CRM field mapping, on-call runbook, repo "
                    "conventions. Domain fidelity beats leaderboard scores."
                ],
                "bullets": [
                    ("Golden scenarios", "real cases with known-good expected outputs."),
                    ("Edge cases", "the weird inputs that break naive automation."),
                    ("Policy cases", "compliance language and forbidden actions."),
                ],
            },
            {
                "tab": "02",
                "title": "Three categories to test",
                "body": [
                    "Cover more than 'did it get the right answer'. Production failures usually come from "
                    "safety and operational behaviour, not pure task accuracy."
                ],
                "bullets": [
                    ("Task success", "did it complete the job correctly?"),
                    ("Safety boundaries", "prompt-injection probes, PII leakage, forbidden tool use."),
                    ("Operational behaviour", "loop detection, retry storms, timeouts, cost spikes."),
                    ("Tool correctness", "right tool, right inputs, right time."),
                ],
            },
            {
                "tab": "03",
                "title": "The regression gate",
                "body": [
                    "Run your eval set before changing a prompt, model, tool or memory. If a change improves "
                    "style but breaks compliance, it must not ship. That is the whole point of a gate."
                ],
                "bullets": [
                    ("Block on failure", "a failed safety case stops the release."),
                    ("Metrics that matter", "success rate, intervention rate, tool error rate, cost per task."),
                    ("Production monitoring", "keep watching after release; behaviour drifts."),
                ],
            },
        ],
        "playbook": [
            "Collect 10-20 real cases with known-correct outcomes.",
            "Add safety cases: injection attempts and forbidden actions.",
            "Add operational cases: things that could trigger loops or cost spikes.",
            "Run the set automatically before any prompt/model/tool change.",
            "Treat failures as release blockers, not optional feedback.",
        ],
        "mistakes": [
            "Judging the agent on a leaderboard score instead of your workflows.",
            "Testing only task success and ignoring safety and cost.",
            "Changing the prompt or model with no regression check.",
            "Stopping evals at launch instead of monitoring drift in production.",
        ],
        "glossary": [
            ("Eval", "A repeatable test of agent behaviour on known scenarios."),
            ("Golden scenario", "A real case with an expected, verified output."),
            ("Regression gate", "A check that blocks a release if behaviour worsens."),
            ("Intervention rate", "How often a human has to step in and correct the agent."),
        ],
        "callout": {
            "title": "The pro move",
            "text": "Your best eval set is harvested from production incidents. Every time the agent does "
                    "something wrong in the real world, add that exact case to the gate. Your tests then evolve "
                    "to cover the failures that actually cost you money.",
        },
    },

    "09_Pick_The_Right_AI_Model": {
        "title": "Pick the Right AI Model",
        "subtitle": "The best stack isn't one model - it's routing each task to the right one.",
        "kicker": "AI FOR BUSINESS - 09",
        "intro": (
            "Using one model for everything is like hiring one person to be your strategist, your data-entry "
            "clerk and your designer. The teams that win route work by task: heavy reasoning to a frontier "
            "model, everyday drafting to a balanced model, high-volume extraction to a small fast model, and "
            "visual jobs to a multimodal model. Routing is decided by risk, context size, modality, latency "
            "and cost."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "Match the model to the job",
                "body": [
                    "Start by classifying the work, not by picking a favorite model."
                ],
                "bullets": [
                    ("Deep reasoning", "ambiguous plans, architecture, strategy, legal nuance - use your strongest model."),
                    ("Daily driver", "writing, analysis, code help, research summaries - a balanced model."),
                    ("Fast + cheap at scale", "classification, extraction, tagging, first-pass QA - a small model."),
                    ("Multimodal", "image, PDF, video and sketch work - a vision/media model."),
                ],
            },
            {
                "tab": "02",
                "title": "Agentic work is its own category",
                "body": [
                    "Tasks where the model must plan, call tools, inspect state and recover from errors need "
                    "models built for agentic loops - raw chat quality is not the same skill."
                ],
                "bullets": [
                    ("Tool use", "reliable function calling and structured outputs."),
                    ("Recovery", "the ability to notice a failed step and self-correct."),
                    ("Explainability", "the model can say what it did and why."),
                ],
            },
            {
                "tab": "03",
                "title": "The routing rule",
                "body": [
                    "Two simple heuristics cover most decisions and keep both quality and cost under control."
                ],
                "bullets": [
                    ("If failure is expensive", "use a stronger model AND add evals."),
                    ("If volume is huge", "use a smaller model AND add deterministic checks."),
                    ("Measure, do not guess", "track accuracy, latency and cost per workflow."),
                ],
            },
        ],
        "playbook": [
            "List your recurring AI tasks and tag each by risk, volume and modality.",
            "Assign a model tier to each tag (frontier / balanced / small / multimodal).",
            "Add evals to high-risk routes and checks to high-volume routes.",
            "Measure accuracy, latency and cost per workflow.",
            "Re-route when the numbers (not the hype) say a different tier wins.",
        ],
        "mistakes": [
            "Defaulting to the most expensive model for trivial extraction tasks.",
            "Using a chat-optimized model for heavy tool-calling agent work.",
            "Choosing models by vibe instead of measured cost and accuracy.",
            "Never revisiting routing as models and prices change.",
        ],
        "glossary": [
            ("Model routing", "Sending each task to the most suitable model."),
            ("Frontier model", "A top-tier model for the hardest reasoning."),
            ("Multimodal model", "A model that handles images, audio or video, not just text."),
            ("Cost per task", "The total spend to complete one unit of work."),
        ],
        "callout": {
            "title": "The pro move",
            "text": "Use a cheap model as a router: have it classify the incoming task, then dispatch to the "
                    "right tier. You pay frontier prices only when the work actually needs frontier reasoning.",
        },
    },

    "10_AI_Operating_System_For_Teams": {
        "title": "An AI Operating System for Teams",
        "subtitle": "Random prompts don't scale. Systems do.",
        "kicker": "AI FOR BUSINESS - 10",
        "intro": (
            "The difference between teams that get a novelty bump from AI and teams that compound real "
            "advantage is structure. Winners build an operating system with six layers - context, tools, "
            "workflows, control, evals and libraries - so good results are repeatable instead of lucky. This "
            "is the blueprint that ties every other guide in this series together."
        ),
        "sections": [
            {
                "tab": "01",
                "title": "Layers 1-2: Context and Tools",
                "body": [
                    "The foundation is what the AI knows about your business and what it can actually touch."
                ],
                "bullets": [
                    ("Context", "projects, memory, docs, examples, brand voice, data dictionary, decision logs."),
                    ("Tools", "MCP connectors, APIs, databases, files, browser and code execution."),
                ],
            },
            {
                "tab": "02",
                "title": "Layers 3-4: Workflows and Control",
                "body": [
                    "Package the repeatable work, then make it safe to run at scale."
                ],
                "bullets": [
                    ("Workflows", "reusable Skills, agent templates, SOPs and prompt packs."),
                    ("Control", "permissions, approvals, hooks, logs, identity, spend limits, rollback plans."),
                ],
            },
            {
                "tab": "03",
                "title": "Layers 5-6: Evals and Libraries",
                "body": [
                    "Measure quality and preserve what works so the system improves over time."
                ],
                "bullets": [
                    ("Evals", "workflow tests, regression gates, edge cases, production monitoring."),
                    ("Libraries", "approved outputs become reusable assets: images, prompts, guides, reports."),
                ],
            },
        ],
        "playbook": [
            "Pick three workflows worth systematizing this quarter.",
            "Write the context docs that explain your business to the AI.",
            "Create one reusable Skill per workflow.",
            "Add approvals and logging for any action that writes to a real system.",
            "Build a small eval set and start an asset library of approved outputs.",
        ],
        "mistakes": [
            "Connecting every tool at once instead of the few that matter.",
            "Letting agents write to systems with no identity or logs.",
            "Confusing an impressive demo with reliable operations.",
            "Never preserving outputs, so good work is constantly re-created from scratch.",
        ],
        "glossary": [
            ("AI operating system", "The six-layer structure that makes AI results repeatable."),
            ("Context layer", "Everything the AI knows about your business."),
            ("Control layer", "Permissions, approvals, logging and rollback."),
            ("Library layer", "Approved outputs stored as reusable assets."),
        ],
        "callout": {
            "title": "The pro move",
            "text": "Start with one workflow and build all six layers around it - thin but complete. A single "
                    "end-to-end slice teaches you more than connecting ten tools with no control or evals, and "
                    "it becomes the template you clone for everything else.",
        },
    },
}

from claude_carousel_pdf_content import BATCH2_CONTENT
from claude_batch3_pdf_content import BATCH3_CONTENT
from claude_batch4_pdf_content import BATCH4_CONTENT
from batch50_01_pdf_content import BATCH50_01_CONTENT
from series50_pdf_content import SERIES50_CONTENT
from hook_pdf_overrides import apply_hook_overrides

CONTENT.update(BATCH2_CONTENT)
CONTENT.update(BATCH3_CONTENT)
CONTENT.update(BATCH4_CONTENT)
CONTENT.update(BATCH50_01_CONTENT)
CONTENT.update(SERIES50_CONTENT)
apply_hook_overrides(CONTENT)
