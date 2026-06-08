# -*- coding: utf-8 -*-
"""14-page dense PDF for Google Omni + Claude bridge."""

PAGES = [
    [
        {"type": "heading", "text": "Google Omni + Claude Bridge - Complete Setup"},
        {"type": "subhead", "text": "omni-ai-mcp operator manual  |  @piyush.glitch"},
        {"type": "prose", "text": (
            "Omni is not a Claude replacement - it is a <b>Gemini tool layer</b> Claude orchestrates. "
            "This PDF: pip install, MCP configs for Desktop + CLI, every tool with invoke examples, "
            "OpenRouter fallback, cost math vs raw paste, production workflows, and failure recovery."
        )},
        {"type": "table", "headers": ["Page", "Topic"], "rows": [
            ["2", "Architecture: Claude router + Gemini worker"],
            ["3", "Prerequisites + API key setup"],
            ["4", "Install + verify gemini_list_models"],
            ["5", "Veo 3.1 video - params + examples"],
            ["6", "Imagen 4K + TTS tools"],
            ["7", "1M context gemini-analyze deep dive"],
            ["8", "Deep Research workflows"],
            ["9", "ask_model OpenRouter routing"],
            ["10", "Slash commands reference"],
            ["11", "Monday brief production workflow"],
            ["12", "Alternative bridges comparison"],
            ["13", "Security + quota management"],
            ["14", "Troubleshooting + checklist"],
        ]},
    ],
    [
        {"type": "heading", "text": "Architecture"},
        {"type": "prose", "text": (
            "Claude Code holds session memory, project rules, MCP connectors. "
            "omni-ai-mcp exposes Gemini capabilities as <b>tools</b> Claude calls on demand. "
            "Heavy reads and video gen happen on Gemini; Claude synthesizes and gates output."
        )},
        {"type": "code", "text": (
            "User prompt\n"
            "    -> Claude (router: pick tool)\n"
            "        -> omni-ai-mcp tool call\n"
            "            -> Gemini API (Veo / analyze / research)\n"
            "        <- structured result\n"
            "    <- Claude summary + [REVIEW] tag\n"
            "User approves external send/publish"
        )},
        {"type": "table", "headers": ["Task", "Without Omni", "With Omni"], "rows": [
            ["Read 400-page PDF", "Paste chunks, lose context", "1M analyze once"],
            ["Generate video", "Leave Claude, use web UI", "Veo tool in thread"],
            ["Market research", "Manual tabs", "Deep Research tool"],
            ["Multi-model compare", "Separate chats", "ask_model OpenRouter"],
        ]},
    ],
    [
        {"type": "heading", "text": "Prerequisites"},
        {"type": "bullets", "title": "Required", "items": [
            "Python 3.9+ and pip",
            "Claude Code CLI or Claude Desktop with MCP support",
            "GEMINI_API_KEY from aistudio.google.com (free tier for dev)",
            "Network egress to Google AI API endpoints",
        ]},
        {"type": "bullets", "title": "Optional", "items": [
            "OPENROUTER_API_KEY for ask_model 400+ model fallback",
            "Google Cloud billing for production Veo volume",
            "Separate GCP project for quota isolation",
        ]},
        {"type": "code", "text": (
            "# Never commit keys\n"
            "export GEMINI_API_KEY=\"AIza...\"\n"
            "export OPENROUTER_API_KEY=\"sk-or-...\"   # optional\n\n"
            "# Verify key\n"
            "curl \"https://generativelanguage.googleapis.com/v1beta/models?key=$GEMINI_API_KEY\" | head"
        )},
    ],
    [
        {"type": "heading", "text": "Install + MCP config"},
        {"type": "code", "text": (
            "pip install omni-ai-mcp\n"
            "pip show omni-ai-mcp   # note version for team doc\n\n"
            "# Claude Desktop (~/.claude/claude_desktop_config.json)\n"
            "{\n"
            '  "mcpServers": {\n'
            '    "omni-ai": {\n'
            '      "command": "omni-ai-mcp",\n'
            '      "env": {\n'
            '        "GEMINI_API_KEY": "your_key",\n'
            '        "OPENROUTER_API_KEY": "optional"\n'
            "      }\n"
            "    }\n"
            "  }\n"
            "}\n\n"
            "# Claude Code CLI\n"
            "claude mcp add omni-ai -- omni-ai-mcp\n"
            "# Set env in shell profile or mcp config"
        )},
        {"type": "prose", "text": (
            "<b>Verify:</b> Restart Claude. Ask: \"Call gemini_list_models and show count.\" "
            "Expect 20+ models. If empty, MCP server not connected - check /mcp output."
        )},
    ],
    [
        {"type": "heading", "text": "Veo 3.1 video generation"},
        {"type": "prose", "text": (
            "Veo generates video with audio from text brief. Claude sets aspect ratio, duration, style. "
            "Returns URL or file path per tool implementation."
        )},
        {"type": "code", "text": (
            "Prompt:\n"
            "Use Gemini Veo tool to generate:\n"
            "- Aspect: 9:16 (Instagram Reels)\n"
            "- Duration: 8 seconds\n"
            "- Subject: skincare bottle on marble, soft morning light\n"
            "- Audio: upbeat lo-fi, no voiceover\n"
            "- Style: UGC authentic, not studio polish\n"
            "Return download URL. Tag output [REVIEW] before client send."
        )},
        {"type": "table", "headers": ["Param", "UGC ads", "Brand spot"], "rows": [
            ["Aspect", "9:16", "16:9"],
            ["Duration", "6-15s", "30-60s"],
            ["Audio", "Trending music", "Licensed or none"],
            ["Style", "Handheld feel", "Cinematic"],
        ]},
        {"type": "callout", "title": "Quota", "text": (
            "Veo is quota-heavy. Draft with MiniMax/Higgsfield; hero with Veo. Track generations in sheet."
        )},
    ],
    [
        {"type": "heading", "text": "Imagen 4K + TTS"},
        {"type": "prose", "text": (
            "Imagen 4K for still assets when video overkill. TTS for voiceover on explainers. "
            "Claude chains: Imagen hero frame -> Veo motion -> TTS narration -> you stitch in editor."
        )},
        {"type": "code", "text": (
            "# Imagen\n"
            "Generate 4K product hero: wireless earbuds on concrete,\n"
            "hard side light, Apple-adjacent minimalism, no text in image.\n\n"
            "# TTS\n"
            "Generate TTS: professional female US accent, 150 wpm.\n"
            "Script: 'Meet the earbuds that disappear in your ear.'\n"
            "Export wav to ./assets/voiceover.wav"
        )},
        {"type": "bullets", "title": "Quality gates", "items": [
            "Check product logo not hallucinated wrong",
            "TTS pronunciation of brand name - listen before publish",
            "4K file size - compress for web delivery",
        ]},
    ],
    [
        {"type": "heading", "text": "1M context gemini-analyze"},
        {"type": "subhead", "text": "~2000x token savings vs pasting into Claude"},
        {"type": "prose", "text": (
            "Dump entire repo docs, contract folders, or log archives. Gemini reads 1M tokens. "
            "Returns structured summary Claude uses for decisions - without blowing Claude context."
        )},
        {"type": "code", "text": (
            "/gemini-analyze\n\n"
            "Analyze entire directory ./legal/contracts/2024-2026/\n"
            "Find: conflicting termination clauses across vendors.\n"
            "Output: table vendor | clause | conflict | page ref.\n"
            "Do not summarize unrelated sections."
        )},
        {"type": "table", "headers": ["Corpus size", "Claude alone", "Omni analyze"], "rows": [
            ["50 pages", "Works", "Faster, cheaper"],
            ["500 pages", "Multi-session paste", "One call"],
            ["Full repo docs", "Impossible in one thread", "Standard pattern"],
            ["CI logs 7 days", "Compact hell", "Analyze once"],
        ]},
        {"type": "callout", "title": "Advanced", "text": (
            "Chain: gemini-analyze -> Claude writes ADR -> git commit. "
            "Store analyze output in docs/analysis/ for audit trail."
        )},
    ],
    [
        {"type": "heading", "text": "Deep Research workflows"},
        {"type": "prose", "text": (
            "Deep Research runs multi-step web research with citations. "
            "Claude frames question; Gemini researches; Claude produces action brief."
        )},
        {"type": "code", "text": (
            "Deep Research job:\n"
            "Topic: B2B SaaS pricing moves in CRM space last 90 days.\n"
            "Deliverable: 1-page brief with citations.\n"
            "Sections: price changes, packaging shifts, enterprise discounts.\n"
            "Claude: synthesize into 5 bullet actions for our pricing committee."
        )},
        {"type": "table", "headers": ["Use case", "Frequency", "Owner"], "rows": [
            ["Competitor pricing", "Weekly", "Product ops"],
            ["Regulatory update", "Monthly", "Legal"],
            ["Tech landscape pitch", "Per deal", "Sales eng"],
            ["Vendor eval", "Per RFP", "Procurement"],
        ]},
    ],
    [
        {"type": "heading", "text": "ask_model OpenRouter"},
        {"type": "prose", "text": (
            "When Gemini native is wrong tool, ask_model routes to 400+ models via OpenRouter. "
            "Routing logic in omni-ai-mcp: prefer Gemini API when key present (fastest); "
            "fallback OpenRouter for GPT-4o, Llama, Mistral, etc."
        )},
        {"type": "code", "text": (
            'ask_model("openai/gpt-4o", """\n'
            "Compare these two JSON schemas for breaking changes only.\n"
            "Schema A: {...}\n"
            "Schema B: {...}\n"
            '""")\n\n'
            'ask_model("anthropic/claude-3.5-sonnet", "Red-team this API design: ...")'
        )},
        {"type": "bullets", "title": "When to ask_model vs native Claude", "items": [
            "ask_model: quick second opinion without codex bridge",
            "Native Claude: anything touching your repo files",
            "Never ask_model with secrets in prompt",
        ]},
    ],
    [
        {"type": "heading", "text": "Slash commands reference"},
        {"type": "table", "headers": ["Command", "Action"], "rows": [
            ["/gemini-analyze", "1M context directory/file analysis"],
            ["/gemini-research", "Deep Research job"],
            ["/gemini-video", "Veo generation shortcut"],
            ["/gemini-image", "Imagen generation"],
            ["/gemini-tts", "Text to speech"],
            ["/gemini-models", "List available models"],
        ]},
        {"type": "prose", "text": (
            "Exact slash commands depend on omni-ai-mcp version - run /help after install. "
            "Pin version in team requirements.txt."
        )},
    ],
    [
        {"type": "heading", "text": "Monday brief production workflow"},
        {"type": "code", "text": (
            "# 45-minute Monday brief (copy to runbook)\n"
            "1. Claude: outline brief sections from CLAUDE.md priorities\n"
            "2. gemini-analyze: pull ./reports/ + Drive export folder\n"
            "3. Deep Research: competitor moves last 7 days\n"
            "4. Claude: merge into exec summary draft\n"
            "5. Veo: 15s optional Slack recap video\n"
            "6. Human [REVIEW] -> send email + post Slack\n"
            "7. Log brief path: docs/briefs/YYYY-MM-DD.md"
        )},
        {"type": "table", "headers": ["Step", "Tool", "Time"], "rows": [
            ["Outline", "Claude", "5 min"],
            ["Doc analyze", "gemini-analyze", "10 min"],
            ["Research", "Deep Research", "15 min"],
            ["Synthesize", "Claude", "10 min"],
            ["Video optional", "Veo", "5 min"],
        ]},
    ],
    [
        {"type": "heading", "text": "Alternative bridges"},
        {"type": "table", "headers": ["Bridge", "Best for", "Tradeoff"], "rows": [
            ["omni-ai-mcp", "Full Gemini API surface", "Python dep"],
            ["making-gemini-useful-with-claude", "Free CLI delegation", "Less video"],
            ["claude-gemini-bridge", "Large codebase hooks", "Narrow scope"],
            ["Composio Gemini MCP", "Enterprise OAuth", "Paid tier"],
        ]},
        {"type": "prose", "text": (
            "Run omni-ai-mcp as primary. Add Composio if enterprise needs Google Workspace OAuth "
            "without manual key management."
        )},
    ],
    [
        {"type": "heading", "text": "Security + quota"},
        {"type": "bullets", "title": "Security", "items": [
            "GEMINI_API_KEY in env only - never in repo",
            "Rotate keys quarterly",
            "Do not analyze folders with unredacted PII without legal OK",
            "[REVIEW] all generated video/audio before client delivery",
            "Log tool calls in docs/omni-audit.log",
        ]},
        {"type": "bullets", "title": "Quota management", "items": [
            "Set GCP budget alert at 80% monthly cap",
            "Separate dev vs prod API keys",
            "Cache gemini-analyze outputs - do not re-analyze same corpus daily",
            "Veo generations require explicit human trigger in CLAUDE.md",
        ]},
    ],
    [
        {"type": "heading", "text": "Troubleshooting + checklist"},
        {"type": "table", "headers": ["Issue", "Fix"], "rows": [
            ["Tool not visible", "Restart Claude; check /mcp"],
            ["Invalid API key", "Regenerate AI Studio key"],
            ["Veo quota exceeded", "Billing enable or wait reset"],
            ["Empty analyze result", "Check path exists; binary files excluded"],
            ["OpenRouter 401", "Set OPENROUTER_API_KEY"],
            ["Slow analyze", "Normal for 1M; run async, continue other work"],
        ]},
        {"type": "table", "headers": ["Done?", "Item"], "rows": [
            ["", "pip install omni-ai-mcp"],
            ["", "gemini_list_models works"],
            ["", "One gemini-analyze on real corpus"],
            ["", "One Veo test generation"],
            ["", "Monday brief in runbook"],
            ["", "Keys in secrets manager not repo"],
        ]},
        {"type": "callout", "title": "@piyush.glitch", "text": (
            "Comment <b>AI</b> | github.com/marmyx77/omni-ai-mcp | June 2026 v2"
        )},
    ],
]
