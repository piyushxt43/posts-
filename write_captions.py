#!/usr/bin/env python3
"""Write copy-paste Instagram caption .txt files into each carousel folder."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent / "AI_Business_Carousels"

CAPTIONS = {
    "01_Claude_Code_Agent_Teams": """Comment AI to get the full Claude Code agent-team playbook and the complete list of workflows that can help your business ship faster with less chaos.

Most teams still use Claude Code like a chat window. That is the slow path. This carousel breaks down how operators are turning it into a real engineering org: one orchestrator plus specialised helpers that explore, build, test and review in parallel.

What you get in this post (8 slides):
Slide 1: Stop Using Claude Code Like Chat: why the moat is orchestration, not one long reply.
Slide 2: Subagents: separate context windows so research noise never floods your main thread.
Slide 3: MCP Connectors: live access to GitHub, Jira, Postgres, Figma and Slack through one standard layer.
Slide 4: Hooks: deterministic guardrails that run every time (lint, secrets checks, test gates).
Slide 5: Skills: reusable packaged instructions you teach once and reuse forever.
Slide 6: Memory: project conventions that survive across sessions.
Slide 7: Team Pattern: Explore reads, Builder edits, Tester runs, Reviewer critiques.
Slide 8: Comment AI: how to claim the bonus guide.

Bonus PDF (sent when you comment AI):
A 3-page branded guide with the full stack explained: subagents, hooks, skills, MCP and memory. Includes a quick-start playbook, mistakes to avoid, key terms and the pro move most people miss (route read-heavy work to a cheap Explore subagent and reserve your strongest model for planning and review).

If you run a product team, agency or startup and want AI that actually ships code instead of giving advice, save this carousel. The PDF goes deeper than any single post can.

Why this matters for business growth:
You cut rework, protect context, enforce quality automatically and turn one developer into a small coordinated team without hiring.

Trending right now on Claude Code and agent teams:
Anthropic's subagent orchestration and agent teams are the hottest topic in dev Twitter and enterprise AI circles in 2026.
Hooks, Skills and MCP are moving from power-user tricks to standard team setup: the same way CI/CD became non-negotiable.
Legal and ops teams are adopting MCP connectors for contract review and audit workflows, not just engineering.
The shift from "prompt in chat" to "programmable agent platform" is what separates teams that demo AI from teams that run on it.""",

    "02_ChatGPT_Workspace_Agents": """Comment AI to get the full workspace-agent checklist and the complete list of automations that can help your business run while your team sleeps.

ChatGPT is no longer just a personal assistant. Workspace agents are shared, persistent, Codex-powered workers your whole team can invoke: and they keep working after you log off.

What you get in this post (8 slides):
Slide 1: ChatGPT Is Becoming A Teammate: the shift from chatbot to automation platform.
Slide 2: From GPTs To Agents: why GPTs answered but agents act across files, tools and memory.
Slide 3: Runs In The Cloud: reports, follow-ups and recurring ops that continue without you.
Slide 4: Shared By Teams: build once, reuse across sales, ops, support and engineering.
Slide 5: Connects Tools: Slack, Microsoft 365, Google Drive, Salesforce and custom MCP servers.
Slide 6: Admin Controls: permissions, allow-lists and approval steps before anything writes data.
Slide 7: Use Case Stack: pipeline reports, support audits, release notes, lead research and more.
Slide 8: Comment AI: claim the bonus guide.

Bonus PDF (sent when you comment AI):
A detailed 3-page guide on turning ChatGPT into team automation: three capabilities GPTs never had, high-value first workflows, control model design, implementation advice, playbook steps, mistakes to avoid and glossary. Built for founders and operators who need shared AI workers, not another solo chat tab.

Interim takeaway:
Start with one repeatable workflow that has clear inputs and outputs. Measure time saved and errors removed. Then scale permissions and connectors deliberately.

Why this helps your business grow:
Less manual reporting, fewer dropped follow-ups, faster handoffs between departments and one agent improving for the whole org every week.

Trending right now on ChatGPT workspace agents:
OpenAI's workspace agents launch is one of the biggest enterprise AI stories of 2026: the successor to custom GPTs.
Teams are wiring 60+ connectors plus MCP into shared agents for CRM cleanup, weekly digests and support triage.
Admin controls and audit logs are the conversation every CIO is having before rolling agents company-wide.
The line between "AI assistant" and "AI employee" is officially blurring: and early adopters are compounding advantage.""",

    "03_Gemini_CLI_Beyond_Coding": """Comment AI to get the full Gemini CLI workflow map and the complete list of terminal automations that can help your business move faster without adding headcount.

Gemini CLI is free to start and open-source: but most people never get past "it writes code." The real value is a 1M-token context window, Google Search grounding, multimodal input and MCP extensions living inside your terminal.

What you get in this post (8 slides):
Slide 1: Gemini CLI Is Not Just For Code: files, search, shell, huge context and MCP in one place.
Slide 2: 1M Context Window: whole repos, long contracts and dense specs in one pass.
Slide 3: Search Grounding: fresh facts with citations instead of stale model guesses.
Slide 4: Multimodal Starts: PDFs, sketches and images become plans, UI drafts and task lists.
Slide 5: MCP Extensions: databases, docs, media generation (Imagen, Veo) and internal APIs.
Slide 6: Headless Mode: run Gemini inside scripts and cron jobs for repeatable ops.
Slide 7: Checkpointing: save and resume long sessions so work does not vanish.
Slide 8: Comment AI: get the bonus guide.

Bonus PDF (sent when you comment AI):
The terminal agent guide most teams underuse: with sections on context advantage, grounding plus multimodal workflows, headless automation, quick-start playbook, mistakes, key terms and the pro move: reconcile your internal doc with live web search for answers that are both on-brand and current.

Interim takeaway:
Gemini CLI is a research and operations agent for anyone who lives in the terminal: not only developers.

Why this helps your business grow:
Faster grounded research, less copy-paste between tools, automated digests and multimodal prototyping without a full creative team.

Trending right now on Gemini CLI:
Google's open-source Gemini CLI is exploding in the developer community as the free entry point to agentic terminal work.
The 1M context window plus Search grounding combo is becoming the default stack for document-heavy roles (legal, ops, strategy).
MCP media servers (Imagen, Veo, Lyria) are turning the CLI into a creative production line from a single prompt.
Headless mode and GEMINI.md project context are the next wave: scheduled AI ops without a browser open.""",

    "04_MCP_Connectors_For_Business": """Comment AI to get the full MCP production checklist and the complete list of connector patterns that can help your business wire AI into real systems safely.

Before MCP, every AI-to-tool link was custom glue: different auth, schema, retries and failure modes for every app. MCP is the USB-C standard that lets Claude, GPT, Gemini and Cursor-style agents reach your business tools through one interface.

What you get in this post (8 slides):
Slide 1: MCP Is The USB-C For Agents: one standard connector shape for every model.
Slide 2: Before MCP: the museum of one-off integrations every team was maintaining.
Slide 3: After MCP: typed tools, resources and prompts any MCP client can discover.
Slide 4: Business Use Cases: Salesforce, Jira, Drive, Slack, databases and Figma.
Slide 5: Gateway Pattern: auth, rate limits, policy and logging before production.
Slide 6: Identity Matters: which human triggered which tool call: especially for writes.
Slide 7: Trace Everything: OpenTelemetry-style spans across agent, gateway and server.
Slide 8: Comment AI: claim the bonus PDF.

Bonus PDF (sent when you comment AI):
MCP Connectors for Business: a 3-page deep dive on what servers expose, the production gateway pattern, observability requirements, playbook steps, mistakes to avoid and glossary. Written for platform leads and operators who need agents that act on real data without becoming a security incident.

Interim takeaway:
Treat MCP servers like internal SDKs. Put them behind a gateway. Split read tools from write tools. Instrument every call before you scale.

Why this helps your business grow:
Faster connector rollouts, one permissions model for security to review, auditable AI actions and agents that actually touch your revenue stack.

Trending right now on MCP:
Model Context Protocol adoption across GitHub, Slack, Salesforce, Notion and Jira made MCP the de facto enterprise AI interoperability standard in 2026.
Production hardening guides (gateway, OAuth 2.1, identity propagation) are the hottest infra topic as teams move from demos to live writes.
Sales and legal teams are live on MCP for pipeline updates and contract workflows: not just engineering.
Every major AI vendor now shares MCP: the "custom integration per model" era is ending fast.""",

    "05_AI_Skills_As_Operating_Procedures": """Comment AI to get the full Skill template pack and the complete list of reusable workflows that can help your business stop re-explaining the same instructions every week.

If you re-type the same prompt three times, you do not have a prompting problem: you have a missing operating procedure. Skills package repeatable jobs so the whole team gets the same expert output on demand.

What you get in this post (8 slides):
Slide 1: Stop Re-Explaining Work: from ad hoc prompts to reusable SOPs.
Slide 2: What A Skill Contains: purpose, trigger, inputs, steps, constraints and output format.
Slide 3: Good Skill Example: PR review with risks first, tests checked, security flagged.
Slide 4: Bad Skill Example: "be helpful and make it better": a vibe, not a workflow.
Slide 5: Use Across Teams: marketing briefs, sales research, finance audits, launch plans.
Slide 6: Pair With Hooks: Skills encode judgement; hooks enforce guarantees.
Slide 7: Version Your Skills: improve, test, review and changelog like product assets.
Slide 8: Comment AI: get the bonus guide.

Bonus PDF (sent when you comment AI):
AI Skills as Operating Procedures: includes what a real Skill contains, good vs bad side-by-side, pairing Skills with hooks, quick-start playbook, mistakes, glossary and the pro move: every bad output becomes a counter-example in the Skill so quality compounds over time.

Interim takeaway:
Write Skills like SOPs, not wishes. Add gold examples, constraints and a verification step at the end.

Why this helps your business grow:
Consistent quality across people and sessions, faster onboarding, less senior time spent re-explaining and workflows that improve every time something fails.

Trending right now on AI Skills:
Skills (SKILL.md packs in Claude Code, Codex and Cursor) are the fastest-growing pattern for turning AI from chat into repeatable ops.
Teams are versioning Skills in git the same way they version code: with review and changelogs.
Pairing Skills with hooks is becoming the standard "judgement plus enforcement" stack for agent platforms.
Every department from marketing to finance is packaging its best prompts into Skills instead of sharing screenshot threads.""",

    "06_AI_Image_Workflows_For_Brands": """Comment AI to get the full AI image production SOP and the complete list of brand workflows that can help your business ship campaign visuals without random results.

Stop generating one-off images and hoping for luck. The brands winning with AI build a system: brand world, reference library, shot list, prompt grammar, QC pass and asset pipeline.

What you get in this post (8 slides):
Slide 1: Stop Generating Random Images: why systems beat better one-liner prompts.
Slide 2: Brand World: color, lighting, camera, materials and what must never appear.
Slide 3: Reference Library: approved faces, products, poses and negative examples.
Slide 4: Shot List: hero, packshot, lifestyle, close-up, comparison, social crop, ad variant.
Slide 5: Prompt Grammar: subject + product + scene + camera + lighting + constraints + ratio.
Slide 6: QC Pass: text, hands, logos, product geometry, scale and legal clearance.
Slide 7: Asset Pipeline: name files, store prompts, version variants, approve into library.
Slide 8: Comment AI: claim the bonus guide.

Bonus PDF (sent when you comment AI):
AI Image Workflows for Brands: covers brand world design, shot lists, prompt grammar, QC checklist, asset pipeline, playbook, mistakes (including why "4K" in a prompt does not mean 4K output), glossary and the pro move on input compression for faster, more reliable generations.

Interim takeaway:
Consistency is a process problem. Define rules once, run every output through QC, and save what works with its prompt and approval status.

Why this helps your business grow:
Faster campaign turns, on-brand visuals at scale, fewer reshoots and a reusable asset library that compounds every quarter.

Trending right now on AI image workflows for brands:
GPT-Image-2 and multimodal pipelines are letting brands produce full ad sets from one product photo: the carousel topic everyone in performance marketing is testing.
Prompt grammar and ratio-first phrasing (not "make it 4K") is the nuance creators are sharing after thousands of generations.
QC checklists for hands, logos and product shape are the difference between "AI slop" and assets clients actually run.
Brand asset libraries with stored prompts are becoming standard ops: treat AI output like photography, not magic.""",

    "07_Context_Engineering": """Comment AI to get the full context-engineering worksheet and the complete list of input patterns that can help your business get reliable AI output without hunting for magic prompts.

Prompt tricks get you a demo. Context engineering gets you production-quality work. The model can only reason over what it sees: so the highest-leverage skill is shaping that input deliberately.

What you get in this post (8 slides):
Slide 1: Prompting Is Not Enough: the real advantage is what the model sees before it acts.
Slide 2: Context Stack: goal, audience, sources, examples, constraints, tools, memory, format.
Slide 3: Examples Beat Adjectives: two great outputs and one bad one teach taste faster.
Slide 4: Constraints Create Quality: length, tone, forbidden claims and compliance boundaries.
Slide 5: Tool Results Matter: fetch from CRM, docs, analytics: do not let the model guess.
Slide 6: Memory Is A Product: brand voice, glossary, architecture and customer segments.
Slide 7: Evaluation Loop: every bad output is a context bug to fix, not a model failure.
Slide 8: Comment AI: get the bonus PDF.

Bonus PDF (sent when you comment AI):
Context Engineering: the real skill behind better AI work. Includes the context stack, constraints and tool results, memory and evaluation loops, playbook, mistakes, glossary and the pro move: keep a counter-example file for recurring tasks so the model learns the boundary it keeps crossing.

Interim takeaway:
Assemble goal, audience, source material, examples, non-goals, constraints and output format before you worry about wording.

Why this helps your business grow:
Higher first-pass quality, fewer hallucinations, outputs that match your brand and systems that improve every time something goes wrong.

Trending right now on context engineering:
"Context engineering" is replacing "prompt engineering" as the phrase serious AI teams use in 2026.
RAG plus examples plus constraints is the stack enterprises are standardising before they trust agents with customer-facing work.
Counter-example libraries (what bad output looks like) are spreading from ML eval teams into everyday ops.
Memory and project context files (CLAUDE.md, GEMINI.md, ChatGPT Projects) are the infrastructure layer everyone is building now.""",

    "08_Agent_Evals_As_Release_Gates": """Comment AI to get the full agent-eval checklist and the complete list of test patterns that can help your business ship AI automation without silent failures.

If your agent can use tools or change data, vibes are not enough. Evals are the unit tests of agent behaviour: and the teams winning in 2026 treat them as release gates, not optional feedback.

What you get in this post (8 slides):
Slide 1: Your Agent Needs Tests: probabilistic systems wired into deterministic tools need gates.
Slide 2: Not Trivia Benchmarks: your workflows, edge cases and CRM field mapping beat MMLU scores.
Slide 3: Three Eval Types: task success, safety boundaries and operational behaviour.
Slide 4: Golden Scenarios: real cases with known-good expected outputs.
Slide 5: Tool-Use Tests: right tool, right inputs, right time.
Slide 6: Regression Gate: if style improves but compliance breaks, it does not ship.
Slide 7: Metrics That Matter: success rate, intervention rate, tool errors, cost per task.
Slide 8: Comment AI: claim the bonus guide.

Bonus PDF (sent when you comment AI):
Agent Evals as Release Gates: covers why workflow-specific evals beat abstract benchmarks, three test categories, golden scenarios, regression gates, playbook, mistakes, glossary and the pro move: harvest production incidents into your eval set so tests evolve to cover failures that actually cost money.

Interim takeaway:
Build evals from real customer cases and internal policies. Run them before every prompt, model or tool change. Block releases on safety failures.

Why this helps your business grow:
Fewer costly bad writes, lower intervention rates, predictable agent cost and trust from leadership to scale automation.

Trending right now on agent evals:
Evals as release gates (not leaderboard scores) is the dominant production AI discourse in 2026.
Prompt injection probes, PII leakage tests and forbidden-tool-use cases are standard in enterprise agent rollouts.
Production incident harvesting into golden datasets is how mature teams keep agents from repeating the same expensive mistake.
Observability plus evals is the minimum bar before any agent touches CRM, billing or customer data.""",

    "09_Pick_The_Right_AI_Model": """Comment AI to get the full model-routing matrix and the complete list of task-to-model mappings that can help your business spend less on AI while getting better results.

Using one model for everything is like hiring one person to be your strategist, data clerk and designer. The best stacks route work by risk, context size, modality, latency and cost.

What you get in this post (8 slides):
Slide 1: Pick The Right Model: routing beats defaulting to the most expensive option.
Slide 2: Deep Reasoning: ambiguous plans, architecture, strategy and legal nuance.
Slide 3: Daily Driver: writing, analysis, code help and research summaries.
Slide 4: Fast Cheap Scale: classification, extraction, tagging and first-pass QA at volume.
Slide 5: Multimodal Work: image, PDF, video and sketch-heavy tasks.
Slide 6: Agent Work: planning, tool use, state inspection and error recovery.
Slide 7: Routing Rule: expensive failure means stronger model plus evals; huge volume means smaller model plus checks.
Slide 8: Comment AI: get the bonus PDF.

Bonus PDF (sent when you comment AI):
Pick the Right AI Model: includes match-model-to-job framework, agentic work as its own category, routing heuristics, playbook, mistakes, glossary and the pro move: use a cheap model as a router that classifies tasks and dispatches to the right tier so you only pay frontier prices when the work actually needs it.

Interim takeaway:
List your recurring AI tasks, tag by risk and volume, assign a tier, measure accuracy/latency/cost per workflow and re-route when the numbers say so.

Why this helps your business grow:
Lower AI spend at scale, better quality on high-stakes tasks and a measured stack instead of hype-driven model choices.

Trending right now on AI model routing:
Multi-model routing is the cost-optimization story every CFO is asking about in 2026.
Cheap models as routers dispatching to frontier models only when needed is spreading from infra teams to marketing ops.
Opus vs Sonnet vs Haiku (and GPT vs Gemini tiers) conversations are everywhere: but measured routing beats brand loyalty.
Agentic workloads are forcing a separate category: tool reliability matters as much as raw reasoning scores.""",

    "10_AI_Operating_System_For_Teams": """Comment AI to get the full AI operating-system blueprint and the complete list of layers your business needs to turn random prompts into repeatable advantage.

Random prompts do not scale. Systems do. The teams compounding real AI advantage in 2026 build an operating system with six layers: context, tools, workflows, control, evals and libraries.

What you get in this post (8 slides):
Slide 1: Build An AI Operating System: why structure beats sporadic prompting.
Slide 2: Layer 1 Context: projects, memory, docs, examples, brand voice and data dictionary.
Slide 3: Layer 2 Tools: MCP connectors, APIs, databases, files and code execution.
Slide 4: Layer 3 Workflows: reusable Skills, agent templates, SOPs and prompt packs.
Slide 5: Layer 4 Control: permissions, approvals, hooks, logs, identity and spend limits.
Slide 6: Layer 5 Evals: workflow tests, regression gates and production monitoring.
Slide 7: Layer 6 Libraries: approved outputs become reusable assets across the org.
Slide 8: Comment AI: claim the bonus guide.

Bonus PDF (sent when you comment AI):
The AI Operating System for Modern Teams: all six layers explained, first-30-days playbook, mistakes to avoid, glossary and the pro move: start with one workflow and build all six layers around it thin but complete: then clone that template for everything else.

Interim takeaway:
Pick three workflows, write context docs, create one Skill each, add approvals for writes, build a small eval set and start an asset library. Do not connect every tool on day one.

Why this helps your business grow:
Repeatable AI results, safer scaling, preserved institutional knowledge and compounding advantage instead of one-off wins.

Trending right now on AI operating systems for teams:
The "AI OS" framing (context + tools + workflows + control + evals + libraries) is the meta-narrative tying Claude Code, ChatGPT agents, MCP and Skills together in 2026.
Teams that treated AI as a product surface (versioned, logged, evaluated) are pulling ahead of teams still doing ad hoc prompting.
The six-layer blueprint is showing up in enterprise playbooks, startup ops threads and creator education: because it finally names what winners were doing quietly.
Building thin-but-complete around one workflow first is the implementation pattern everyone is copying after expensive "connect everything" failures.""",
}


def fit_caption(text: str, limit: int = 2200) -> str:
    """Trim optional paragraphs so copy stays within Instagram-friendly length."""
    clean = text.replace("*", "").strip()
    if len(clean) <= limit:
        return clean

    drop_phrases = (
        "If you run a product team",
        "Interim takeaway:",
    )
    paragraphs = clean.split("\n\n")
    filtered = [p for p in paragraphs if not any(p.startswith(s) for s in drop_phrases)]
    clean = "\n\n".join(filtered)
    if len(clean) <= limit:
        return clean

    # Shorten slide lines: keep headline only after the colon.
    lines = clean.split("\n")
    out = []
    for line in lines:
        if line.startswith("Slide ") and ": " in line:
            prefix, rest = line.split(": ", 1)
            headline = rest.split(".")[0].split(",")[0]
            line = f"{prefix}: {headline}."
        out.append(line)
    clean = "\n".join(out)
    if len(clean) <= limit:
        return clean

    # Last resort: keep intro, slides block, PDF block, growth, trending; trim PDF prose.
    blocks = clean.split("\n\n")
    trending_idx = next(i for i, b in enumerate(blocks) if b.startswith("Trending right now"))
    keep = blocks[:trending_idx] + blocks[trending_idx:]
    while len("\n\n".join(keep)) > limit and len(keep) > 4:
        # Drop the paragraph just before trending (usually "Why this matters").
        keep.pop(-2)
    clean = "\n\n".join(keep)
    return clean[:limit].rsplit("\n", 1)[0] if len(clean) > limit else clean


def main():
    for slug, text in CAPTIONS.items():
        folder = ROOT / slug
        if not folder.is_dir():
            print(f"SKIP {slug}")
            continue
        path = folder / "caption.txt"
        clean = fit_caption(text)
        path.write_text(clean.strip() + "\n", encoding="utf-8")
        print(f"OK  {slug}: {len(clean.strip())} chars -> {path.name}")


if __name__ == "__main__":
    main()
