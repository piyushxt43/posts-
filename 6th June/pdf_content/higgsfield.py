# -*- coding: utf-8 -*-
"""14-page dense PDF for Higgsfield MCP review."""

PAGES = [
    [
        {"type": "heading", "text": "Higgsfield MCP - Honest Operator Review"},
        {"type": "subhead", "text": "Advanced setup, credit math, model routing  |  @piyush.glitch"},
        {"type": "prose", "text": (
            "Launched April 30, 2026. Hosted MCP at mcp.higgsfield.ai. "
            "This PDF goes beyond \"worth it yes/no\": exact OAuth setup for Desktop + CLI, "
            "30+ model routing table, credit burn rates, UGC factory workflow, "
            "comparison vs omni-ai-mcp and direct APIs, and when to skip entirely."
        )},
        {"type": "table", "headers": ["Page", "Topic"], "rows": [
            ["2", "Architecture: hosted MCP vs self-hosted"],
            ["3", "OAuth setup - Desktop + Claude Code"],
            ["4", "Credit system + burn rate math"],
            ["5", "Image models - full routing table"],
            ["6", "Video models - full routing table"],
            ["7", "9 UGC presets - when to use each"],
            ["8", "UGC ad factory workflow (step-by-step)"],
            ["9", "Brand SKILL.md integration"],
            ["10", "Higgsfield vs omni vs direct API"],
            ["11", "Meta MCP performance loop"],
            ["12", "When NOT worth it (decision matrix)"],
            ["13", "Failure modes + support"],
            ["14", "Verdict checklist + ROI calculator"],
        ]},
    ],
    [
        {"type": "heading", "text": "Hosted MCP architecture"},
        {"type": "prose", "text": (
            "Higgsfield runs the MCP server. You connect via OAuth - no API key provisioning, "
            "no ComfyUI install. Claude calls tools; Higgsfield bills your existing plan credits."
        )},
        {"type": "table", "headers": ["Component", "You manage", "Higgsfield manages"], "rows": [
            ["MCP server", "Connector URL only", "Uptime, model routing"],
            ["Model keys", "Nothing", "15+ image, 16+ video APIs"],
            ["OAuth", "Sign-in click", "Token refresh"],
            ["Credits", "Budget alerts", "Deduction per gen"],
            ["Output storage", "Download to your bucket", "Temp URLs"],
        ]},
        {"type": "callout", "title": "Trust boundary", "text": (
            "Prompts and brand briefs leave your machine to Higgsfield cloud. "
            "Do not use for unreleased product IP without NDA coverage."
        )},
    ],
    [
        {"type": "heading", "text": "OAuth setup"},
        {"type": "code", "text": (
            "# Claude Desktop / claude.ai\n"
            "Settings -> Connectors -> Add custom connector\n"
            "Name: Higgsfield\n"
            "URL: https://mcp.higgsfield.ai/mcp\n"
            "Transport: HTTP (SSE)\n"
            "Connect -> Sign in with Higgsfield -> Authorize\n\n"
            "# Claude Code CLI\n"
            "claude mcp add --transport http --scope user higgsfield \\\n"
            "  https://mcp.higgsfield.ai/mcp\n"
            "claude mcp list   # higgsfield connected\n\n"
            "# Verify prompt\n"
            "List Higgsfield tools. Show my credit balance and available image models."
        )},
        {"type": "bullets", "title": "Post-setup", "items": [
            "Run one cheap image gen (Nano Banana) before batch",
            "Confirm credit deduction matches dashboard",
            "Add connector to team onboarding doc",
        ]},
    ],
    [
        {"type": "heading", "text": "Credit system + burn math"},
        {"type": "prose", "text": (
            "Free tier ~150 credits/month (May 2026). Paid ~$1 = 16 credits. "
            "Always check balance before batch - mid-batch failure wastes creative momentum."
        )},
        {"type": "table", "headers": ["Action", "Credits est.", "Monthly @ 20/wk"], "rows": [
            ["Nano Banana draft image", "2-4", "160-320 credits"],
            ["FLUX 4K product", "8-12", "640-960 credits"],
            ["Kling UGC 9:16 10s", "15-25", "1200-2000 credits"],
            ["Sora 2 cinematic 30s", "40-80", "3200-6400 credits"],
            ["MiniMax video draft", "5-8", "400-640 credits"],
        ]},
        {"type": "code", "text": (
            "# ROI calculator\n"
            "monthly_credit_budget = 500   # example paid tier\n"
            "hero_videos = budget * 0.2 / 60    # Sora heroes\n"
            "ugc_drafts = budget * 0.6 / 8      # MiniMax drafts\n"
            "image_tests = budget * 0.2 / 3     # Nano hook tests\n"
            "# Adjust ratios weekly from Meta performance data"
        )},
        {"type": "callout", "title": "Credit savers", "text": (
            "MiniMax draft -> human pick -> Sora hero only for winners. "
            "Kill variants below 25% hook rate before more gens."
        )},
    ],
    [
        {"type": "heading", "text": "Image models - routing table"},
        {"type": "table", "headers": ["Model", "Credits", "Best for", "Avoid for"], "rows": [
            ["Soul 2.0", "Med", "Realistic faces, character lock", "Abstract logos"],
            ["Nano Banana Pro", "Low", "Fast hook image tests", "Final 4K print"],
            ["GPT Image 2", "Med", "Text in image, labels", "Pure lifestyle"],
            ["FLUX", "Med-High", "Photoreal product", "Heavy text overlays"],
            ["Seedream 4.0", "Med", "Fashion editorial", "B2B SaaS UI"],
            ["Imagen (via HF)", "Med", "Google ecosystem parity", "Character consistency"],
        ]},
        {"type": "code", "text": (
            "Prompt pattern (let Claude route):\n"
            "Generate product hero for Meta feed 1:1.\n"
            "Product: [name]. Style: UGC authentic.\n"
            "Must include: product label readable.\n"
            "Prefer: FLUX or GPT Image 2 for text.\n"
            "Return: 3 variants, credit estimate each."
        )},
    ],
    [
        {"type": "heading", "text": "Video models - routing table"},
        {"type": "table", "headers": ["Model", "Credits", "Best for", "Aspect"], "rows": [
            ["Sora 2", "High", "Cinematic brand", "16:9"],
            ["Veo 3.1", "High", "Google stack parity", "9:16 or 16:9"],
            ["Kling 3.0", "Med", "UGC talking head", "9:16"],
            ["Seedance 2.0", "Med", "Product motion", "9:16"],
            ["MiniMax Hailuo", "Low", "Fast drafts", "9:16"],
            ["Runway Gen4", "Med", "Motion graphics", "16:9"],
        ]},
        {"type": "prose", "text": (
            "<b>Operator rule:</b> Tell Claude outcome (UGC, unboxing, TV spot) - not model name. "
            "Micromanage model only when A/B testing model performance in sheet."
        )},
    ],
    [
        {"type": "heading", "text": "9 UGC presets"},
        {"type": "table", "headers": ["Preset", "Use", "Typical model"], "rows": [
            ["UGC testimonial", "Social proof ads", "Kling"],
            ["Unboxing", "Product launch", "Seedance"],
            ["Product review", "Consideration stage", "Kling"],
            ["TV spot", "Brand awareness", "Sora 2"],
            ["Talking head", "Founder message", "Kling"],
            ["Lifestyle b-roll", "Aspiration", "Veo 3.1"],
            ["Before/after", "Transformation products", "MiniMax draft"],
            ["ASMR product", "TikTok organic", "Seedance"],
            ["Carousel stills", "Feed multi-image", "Nano Banana"],
        ]},
        {"type": "code", "text": (
            "Use Higgsfield UGC preset: unboxing.\n"
            "Product: skincare serum box.\n"
            "Setting: bathroom counter morning light.\n"
            "Hands only, no face. 9:16, 12 seconds."
        )},
    ],
    [
        {"type": "heading", "text": "UGC ad factory workflow"},
        {"type": "code", "text": (
            "# Weekly UGC factory (2hr operator block)\n"
            "1. Claude: 10 hooks from brand SKILL.md + last week Meta data\n"
            "2. Score hooks 1-5 for hook_rate potential\n"
            "3. Top 5 hooks -> Higgsfield MiniMax 9:16 drafts (5 credits each)\n"
            "4. Human pick 3 drafts [REVIEW]\n"
            "5. Winner -> Higgsfield Kling or Sora final (1 credit tier up)\n"
            "6. Export to Meta Ads Manager\n"
            "7. Tag sheet: hook_id, model, preset, week_live\n"
            "8. Day 7: Meta MCP pull performance -> feed step 1"
        )},
        {"type": "table", "headers": ["Role", "Tool", "Time"], "rows": [
            ["Hooks", "Claude + SKILL.md", "20 min"],
            ["Drafts", "Higgsfield MiniMax", "30 min"],
            ["Review", "Human", "20 min"],
            ["Finals", "Higgsfield Kling/Sora", "30 min"],
            ["Upload", "Meta", "20 min"],
        ]},
    ],
    [
        {"type": "heading", "text": "Brand SKILL.md integration"},
        {"type": "code", "text": (
            "# ~/.claude/skills/brand-ugc/SKILL.md\n"
            "## Brand\n"
            "Voice: confident, never medical claims\n"
            "Colors: #F4EEDE cream, #EF5E45 coral accent\n"
            "Banned: competitor names, before/after skin disease\n\n"
            "## Higgsfield rules\n"
            "- Always 9:16 for paid social\n"
            "- Check credit balance before batch >5\n"
            "- 3 variants max per hook unless manager approve\n"
            "- Tag outputs [REVIEW] in filename\n\n"
            "## Hook formula\n"
            "Problem (3s) -> Product (5s) -> CTA (2s)"
        )},
        {"type": "prose", "text": (
            "Claude reads SKILL.md before every Higgsfield tool call. "
            "Stops off-brand gens before credits burn."
        )},
    ],
    [
        {"type": "heading", "text": "Higgsfield vs alternatives"},
        {"type": "table", "headers": ["Tool", "Strength", "Weakness"], "rows": [
            ["Higgsfield MCP", "30+ models, OAuth easy", "Cloud trust boundary"],
            ["omni-ai-mcp", "Gemini Veo + 1M read", "Fewer image models"],
            ["Direct OpenAI API", "Control, SLAs", "Setup pain per model"],
            ["ComfyUI local", "IP stays local", "Ops overhead"],
            ["Canva AI", "Non-dev friendly", "Not MCP scriptable"],
        ]},
        {"type": "prose", "text": (
            "<b>Stack recommendation:</b> Higgsfield for creative volume. "
            "omni-ai-mcp for doc analyze + Veo when needed. "
            "Meta MCP for performance data. Claude orchestrates all three."
        )},
    ],
    [
        {"type": "heading", "text": "Meta MCP performance loop"},
        {"type": "code", "text": (
            "# Close the loop (pairs with 5th June Meta UGC carousel)\n"
            "1. Meta MCP: pull ad set performance last 7 days\n"
            "2. Claude: rank hooks by hook_rate and CPA\n"
            "3. Kill bottom quartile variants in sheet\n"
            "4. Clone top quartile hooks -> new Higgsfield batch\n"
            "5. Never scale creative without 48hr data minimum"
        )},
        {"type": "table", "headers": ["Metric", "Scale threshold", "Kill threshold"], "rows": [
            ["Hook rate", ">30% after 1k impr", "<15% after 2k impr"],
            ["CPA", "<target after 48hr", ">1.5x target after 72hr"],
            ["CTR", ">1.2% feed", "<0.6%"],
        ]},
    ],
    [
        {"type": "heading", "text": "When NOT worth it"},
        {"type": "table", "headers": ["Profile", "Verdict", "Reason"], "rows": [
            ["Backend engineer only", "Skip", "No creative output"],
            ["IP-sensitive unreleased hardware", "Skip", "Cloud prompt exposure"],
            ["Budget <$20/mo heavy 4K", "Skip", "Credit math fails"],
            ["No [REVIEW] gate", "Skip", "Brand risk"],
            ["DTC 10+ ads/week", "Strong yes", "OAuth saves 10hr/wk"],
            ["Agency multi-client", "Yes", "Model variety in one MCP"],
            ["Already ComfyUI farm", "Maybe", "Compare ops cost"],
        ]},
    ],
    [
        {"type": "heading", "text": "Failure modes"},
        {"type": "table", "headers": ["Issue", "Fix"], "rows": [
            ["OAuth expired", "Reconnect Settings -> Connectors"],
            ["Wrong aspect", "Specify 9:16 or 1:1 in prompt"],
            ["Credits gone mid-batch", "balance check first command"],
            ["Off-brand output", "Tighten brand SKILL.md"],
            ["Tool timeout", "Retry; reduce variant count"],
            ["Model unavailable", "Fallback MiniMax per SKILL.md"],
            ["Text garbled in image", "Switch GPT Image 2"],
            ["Connector not in CLI", "claude mcp add http URL"],
        ]},
    ],
    [
        {"type": "heading", "text": "Verdict checklist + ROI"},
        {"type": "table", "headers": ["Question", "Yes = worth it"], "rows": [
            ["Ship UGC/ads weekly?", "Required"],
            ["Use Claude daily?", "Required"],
            ["Can [REVIEW] before publish?", "Required"],
            ["Code-only job?", "No - skip"],
            [">$50/mo creative budget?", "Recommended"],
        ]},
        {"type": "prose", "text": (
            "<b>ROI proof:</b> Track hours saved vs manual model hopping. "
            "Target: 8+ hours/week saved at 10+ gens/week to justify paid tier."
        )},
        {"type": "callout", "title": "Final verdict", "text": (
            "<b>Worth it</b> for creative operators running Claude + Meta ads. "
            "<b>Skip</b> for code-only devs. Comment <b>AI</b> @piyush.glitch | June 2026 v2"
        )},
    ],
]
