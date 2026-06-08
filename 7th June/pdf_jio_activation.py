# -*- coding: utf-8 -*-
"""15-page premium Google Gemini Pro (via Jio) activation + tools guide.

Dense, designed pages: cover, plan economics, eligibility, activation,
deep-dives on every Google AI Pro tool, and use cases for students,
professionals and businesses. Built on pdf_builder_gemini.
"""

from __future__ import annotations

from pathlib import Path

from pdf_builder_gemini import (
    CORAL, G_BLUE, G_GREEN, G_PINK, G_PURPLE, G_YELLOW, build_pdf,
)

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "Google_Gemini_Pro_Jio_Activation_Guide.pdf"


def pages() -> list:
    return [
        # ---------------------------------------------------------------- #
        # 1 - COVER
        # ---------------------------------------------------------------- #
        [
            {"type": "hero", "text": "Google Gemini Pro<br/>FREE for 18 Months"},
            {"type": "herosub", "text": (
                "The complete activation &amp; power-user playbook for the "
                "Reliance Jio x Google AI Pro offer worth Rs 35,100"
            )},
            {"type": "stat_cards", "cards": [
                {"value": "Rs 0", "label": "Your cost via Jio", "color": G_GREEN},
                {"value": "18 mo", "label": "Free subscription", "color": G_BLUE},
                {"value": "5 TB", "label": "Cloud storage", "color": G_PINK},
                {"value": "1M", "label": "Token context", "color": G_PURPLE},
            ]},
            {"type": "prose", "text": (
                "In October 2025, Reliance Jio and Google partnered to give eligible Jio users "
                "<b>18 months of Google AI Pro</b> (the plan that normally costs around Rs 1,950/month, "
                "about Rs 35,100 over 18 months) at <b>zero extra cost</b>. This is one of the largest "
                "consumer AI giveaways ever - aimed at putting Google's most capable models in the hands "
                "of ~500 million Indians."
            )},
            {"type": "prose", "text": (
                "But most people claim it and use 5% of what they paid nothing for. This guide fixes that: "
                "first we get you <b>activated correctly</b> (so the benefits lock to the right Google account), "
                "then we go tool-by-tool through <b>everything Google AI Pro unlocks</b> - with real workflows "
                "for students, working professionals, and businesses."
            )},
            {"type": "callout", "title": "Inside this guide", "color": G_BLUE, "text": (
                "Offer economics &amp; plan comparison  |  Eligibility &amp; non-Jio workaround  |  "
                "6-step MyJio activation  |  Gemini app, Deep Research, Gems, Scheduled Actions, NotebookLM, "
                "Canvas, Gemini Live, Flow, Veo 3.1, Whisk, Nano Banana, 5 TB storage  |  "
                "Use cases for students / pros / business  |  Troubleshooting."
            )},
            {"type": "subhead", "text": "Do these three things today"},
            {"type": "two_col_bullets",
             "left": [
                 "1. Confirm you're on a Rs 349+ Jio 5G plan",
                 "2. Update MyJio and claim the Gemini banner",
             ],
             "right": [
                 "3. Link your MAIN Gmail (not a throwaway)",
                 "Then read pages 8-14 to actually use it",
             ]},
            {"type": "callout", "title": "Why this matters", "color": G_PINK, "text": (
                "Rs 35,100 of AI is meaningless if it sits unused. The activation takes 5 minutes; the real "
                "return comes from the workflows in this guide. Bookmark it and work through one tool per day."
            )},
        ],
        # ---------------------------------------------------------------- #
        # 2 - THE OFFER DECODED + plan comparison
        # ---------------------------------------------------------------- #
        [
            {"type": "heading", "text": "The Offer, Decoded"},
            {"type": "prose", "text": (
                "Google's AI subscriptions were overhauled at Google I/O 2026 into four tiers: a free tier, "
                "<b>Google AI Plus</b>, <b>Google AI Pro</b>, and <b>Google AI Ultra</b>. The Jio offer gives you "
                "the <b>Pro</b> tier - the sweet spot for everyday power users - free for 18 months."
            )},
            {"type": "subhead", "text": "What each tier actually gives you (2026)"},
            {"type": "table",
             "headers": ["Capability", "Free", "Plus", "Pro (your offer)", "Ultra"],
             "col_widths": [2.3, 1.05, 1.1, 1.65, 1.3],
             "rows": [
                 ["Top model", "3 Flash", "3.1 Pro (cap)", "3.1 Pro full", "3.1 Pro"],
                 ["Context window", "~32K", "128K", "1 million", "1 million"],
                 ["Deep Research", "5 / month", "12 / day", "20 / day", "120 / day"],
                 ["AI credits / mo", "50 / day", "200", "1,000", "25,000"],
                 ["NotebookLM notebooks", "Basic", "200", "500", "500+"],
                 ["Veo video (Flow)", "No", "~10 / mo", "~50 / mo", "~1,250 / mo"],
                 ["Cloud storage", "15 GB", "200 GB", "5 TB", "30 TB"],
                 ["Workspace side-panel", "No", "Limited", "Full", "Full"],
             ]},
            {"type": "callout", "title": "Why Pro is the value pick", "color": G_GREEN, "text": (
                "Pro includes the <b>full 1M-token context</b> and <b>full Workspace integration</b> that Plus caps, "
                "but skips Ultra's Rs 20,000+/month price. The 5 TB storage alone (vs paying for Google One 2 TB at "
                "~Rs 210/month) plus full Gemini access is why Rs 35,100 is the realistic 18-month value."
            )},
            {"type": "prose", "text": (
                "<b>Lesser-known:</b> usage in 2026 is now <b>compute-based</b>, not a fixed daily prompt count. "
                "Your allowance refreshes every <b>5 hours</b> until you hit a weekly cap. Heavy actions "
                "(Deep Think, media generation, Deep Research) burn it faster - so batch big jobs."
            )},
            {"type": "subhead", "text": "Where the Rs 35,100 value comes from"},
            {"type": "table", "headers": ["Component", "If bought separately", "Over 18 months"], "col_widths": [2.6, 2.4, 2.4], "rows": [
                ["Google AI Pro (AI features)", "~Rs 1,750/mo", "~Rs 31,500"],
                ["Google One 5 TB storage", "bundled in Pro", "included above"],
                ["YouTube Premium Lite", "~Rs 89/mo", "~Rs 1,600"],
                ["Google Home Premium + perks", "varies", "included"],
                ["Total realistic value", "-", "~Rs 35,100"],
            ]},
            {"type": "callout", "title": "How the 18 months are counted", "color": G_BLUE, "text": (
                "The clock starts on your <b>activation date</b>, not the offer launch date. So claiming later in the "
                "window still gives you the full 18 months - as long as you claim before the offer closes and keep an "
                "eligible plan active throughout."
            )},
        ],
        # ---------------------------------------------------------------- #
        # 3 - ELIGIBILITY
        # ---------------------------------------------------------------- #
        [
            {"type": "heading", "text": "Step 0: Check Your Eligibility"},
            {"type": "prose", "text": (
                "The offer is for <b>Jio retail users</b> only (corporate / enterprise SIMs are excluded) and "
                "must be claimed inside the official MyJio app before the offer window closes."
            )},
            {"type": "table", "headers": ["Requirement", "Details"], "col_widths": [2.1, 5.3], "rows": [
                ["Active Jio SIM", "Retail prepaid or postpaid Jio mobile number"],
                ["Age", "18 years or older at the time of claiming"],
                ["Primary plan", "Active Jio Unlimited 5G plan of Rs 349 or above"],
                ["Extended plan", "From 11 Feb 2026, active 1.5 GB/day plans of Rs 299+ also qualify"],
                ["Plan continuity", "Keep an eligible plan active the ENTIRE 18 months or benefits pause"],
                ["Geography", "India only"],
                ["Claim limit", "Once per unique eligible Jio mobile number"],
                ["Offer window", "30 Oct 2025 to 29 Oct 2026 (subject to change by Jio)"],
            ]},
            {"type": "subhead", "text": "Do this 5 minutes before you open MyJio"},
            {"type": "two_col_bullets",
             "left": [
                 "Recharge to an eligible plan if you're on a lower pack",
                 "Update MyJio to the latest version (store)",
             ],
             "right": [
                 "Decide your primary Gmail (storage locks to it)",
                 "Keep your Jio number ready for OTP",
             ]},
            {"type": "callout", "title": "Not a Jio user? You can still get it", "color": G_PURPLE, "text": (
                "Option A: Get a new Jio SIM and recharge Rs 349+ Unlimited 5G, then claim. "
                "Option B: If a family member or friend has an eligible Jio SIM, they can claim on MyJio with their "
                "number but link <b>your</b> Gmail at Step 5 - benefits attach to the Google account, not the phone. "
                "They just complete the OTP."
            )},
        ],
        # ---------------------------------------------------------------- #
        # 4 - ACTIVATION PART 1
        # ---------------------------------------------------------------- #
        [
            {"type": "heading", "text": "Activation: Steps 1 to 3"},
            {"type": "pill", "text": "Step 1", "color": G_BLUE},
            {"type": "h3", "text": "Install or update MyJio"},
            {"type": "bullets", "items": [
                "Android: Play Store - search 'MyJio' by Reliance Jio Infocomm Limited",
                "iOS: App Store - same publisher, update to the latest version",
                "Force-close and reopen after updating so promotional banners load",
            ]},
            {"type": "pill", "text": "Step 2", "color": G_GREEN},
            {"type": "h3", "text": "Log in securely"},
            {"type": "code", "text": (
                "1.  Open MyJio\n"
                "2.  Enter your eligible Jio mobile number\n"
                "3.  Verify with the OTP sent to that SIM\n"
                "4.  Complete your profile if prompted"
            )},
            {"type": "callout", "title": "Security first", "color": CORAL, "text": (
                "Never share your OTP with anyone. Claim ONLY inside the official MyJio app or at "
                "jio.com/google-gemini-offer. Treat any DM, SMS or 'agent' offering to 'activate Gemini for you' "
                "as a scam - Google and Jio never ask for your OTP or password."
            )},
            {"type": "pill", "text": "Step 3", "color": G_PINK},
            {"type": "h3", "text": "Find the offer banner"},
            {"type": "bullets", "items": [
                "On the MyJio home screen, scroll the top banner / carousel section",
                "Look for 'Pro plan of Google Gemini FREE' or 'Google Gemini Offer'",
                "Banner missing? Confirm an eligible recharge, update the app, then wait up to 24h",
                "Still nothing? Open jio.com/google-gemini-offer on the same device",
            ]},
        ],
        # ---------------------------------------------------------------- #
        # 5 - ACTIVATION PART 2
        # ---------------------------------------------------------------- #
        [
            {"type": "heading", "text": "Activation: Steps 4 to 6"},
            {"type": "pill", "text": "Step 4", "color": G_YELLOW},
            {"type": "h3", "text": "Claim the subscription"},
            {"type": "bullets", "items": [
                "Tap the Google Gemini offer banner on the MyJio home screen",
                "Review the offer summary (18 months Google AI Pro, Rs 35,100 value)",
                "Tap 'Claim Now' (or 'Register Interest')",
                "Scroll the Terms & Conditions to the bottom, then tap 'Agree'",
            ]},
            {"type": "pill", "text": "Step 5", "color": G_PURPLE},
            {"type": "h3", "text": "Link the RIGHT Google account"},
            {"type": "prose", "text": (
                "MyJio redirects you to sign in with Google. This is the most important decision in the whole "
                "process: <b>the 5 TB storage and all AI Pro features lock to the Gmail you pick here</b>, and "
                "switching later is painful. Choose your main personal account - the one you use for Drive, "
                "Photos and Gmail every day."
            )},
            {"type": "two_col_bullets",
             "left": [
                 "Use your daily personal @gmail.com",
                 "Avoid school / work Workspace accounts",
             ],
             "right": [
                 "Complete the Google One / AI Pro consent",
                 "Don't pick a throwaway email",
             ]},
            {"type": "pill", "text": "Step 6", "color": G_BLUE},
            {"type": "h3", "text": "Verify your premium status"},
            {"type": "code", "text": (
                "gemini.google.com      ->  profile shows Google AI Pro / Advanced\n"
                "one.google.com         ->  plan shows AI Pro, storage now 5 TB\n"
                "notebooklm.google.com  ->  expanded Pro limits are active\n"
                "Gmail > Settings       ->  turn on Gemini features if prompted"
            )},
            {"type": "callout", "title": "If the badge doesn't show", "color": G_GREEN, "text": (
                "Wait up to 30 minutes, then sign out and back into your Google account and recheck "
                "one.google.com. If MyJio says 'claimed' but Google still shows free, contact Jio support with "
                "a screenshot of the MyJio confirmation."
            )},
        ],
        # ---------------------------------------------------------------- #
        # 6 - PLAN RULES & KEEPING IT ACTIVE
        # ---------------------------------------------------------------- #
        [
            {"type": "heading", "text": "Keeping the Benefits for 18 Months"},
            {"type": "prose", "text": (
                "This is a <b>continuity offer</b>. The free Pro access is tied to maintaining an eligible Jio "
                "recharge. Let your plan lapse and your AI Pro and 5 TB storage can be paused until you recharge again."
            )},
            {"type": "table", "headers": ["Situation", "What happens / what to do"], "col_widths": [2.4, 5.0], "rows": [
                ["Plan drops below Rs 349", "Recharge back to an eligible plan immediately to restore benefits"],
                ["SIM ported out of Jio", "Benefits end - finish anything important before porting"],
                ["Already claimed on number", "You cannot claim twice on the same Jio mobile number"],
                ["Corporate / enterprise SIM", "Usually ineligible - claim on a personal retail SIM instead"],
                ["Storage over 5 TB at expiry", "New uploads blocked; existing files stay readable - don't lose data"],
                ["Offer ends Oct 2026", "Claim before 29 Oct 2026; the 18 months then run from your activation date"],
            ]},
            {"type": "subhead", "text": "Your 18-month maintenance checklist"},
            {"type": "bullets", "items": [
                "Set a calendar reminder 2 days before every plan expiry",
                "Enable auto-pay / auto-recharge on the eligible plan where possible",
                "Screenshot the MyJio confirmation and your Google One plan page right after claiming",
                "Do NOT manually cancel Google One - it is tied to the Jio promo enrollment",
                "If you near 5 TB, archive old files to free space rather than buying more",
            ]},
            {"type": "callout", "title": "Pro tip", "color": G_PURPLE, "text": (
                "Treat the 18 months as a runway to build habits and assets (Gems, NotebookLM libraries, "
                "automations) that keep paying off even if you don't renew later."
            )},
        ],
        # ---------------------------------------------------------------- #
        # 7 - EVERYTHING INCLUDED (cards grid)
        # ---------------------------------------------------------------- #
        [
            {"type": "heading", "text": "Everything Google AI Pro Unlocks"},
            {"type": "prose", "text": (
                "Your Rs 35,100 bundle is not one app - it's a stack of Google's best AI spread across the apps you "
                "already use. Here's the full map; the next pages show how to actually use each one."
            )},
            {"type": "cards_grid", "cards": [
                {"title": "Gemini app - 3.1 Pro", "body": "Most capable model, 1M-token context, thinking modes, Deep Research."},
                {"title": "Deep Research", "body": "Auto-browses hundreds of sources AND your Gmail/Drive/Meet into cited reports. 20/day."},
                {"title": "Gems", "body": "Reusable custom AI agents with their own instructions + knowledge base."},
                {"title": "Scheduled Actions", "body": "Recurring prompts that run on their own - daily briefs, weekly digests."},
                {"title": "NotebookLM", "body": "500 notebooks, 300 sources each, Audio + Video Overviews of your docs."},
                {"title": "Canvas", "body": "Side-by-side editor for docs and no-code app/website prototyping."},
                {"title": "Gemini Live", "body": "Voice + camera + screen-share assistant tied to Maps, Calendar, Tasks, Keep."},
                {"title": "Workspace AI", "body": "Gemini side panel inside Gmail, Docs, Sheets, Slides, Drive and Vids."},
                {"title": "Flow + Veo 3.1", "body": "AI filmmaking studio, ~50 videos/month, 1,000 monthly credits."},
                {"title": "Whisk + Nano Banana", "body": "Image-to-video and pro image generation/editing from one photo."},
                {"title": "5 TB Google One", "body": "Storage across Drive, Gmail, Photos + family sharing."},
                {"title": "Bonus perks", "body": "YouTube Premium Lite, Google Home Premium, developer credits."},
            ]},
        ],
        # ---------------------------------------------------------------- #
        # 8 - GEMINI APP DEEP DIVE
        # ---------------------------------------------------------------- #
        [
            {"type": "heading", "text": "Tool 1: The Gemini App (3.1 Pro)"},
            {"type": "prose", "text": (
                "The headline benefit. On Pro you get <b>Gemini 3.1 Pro</b> with the full <b>1-million-token "
                "context window</b> - roughly <b>1,500 pages of text or 30,000 lines of code in a single chat</b>. "
                "It won't 'forget' the start of a long document while reading the end."
            )},
            {"type": "subhead", "text": "Thinking modes - pick the right brain"},
            {"type": "table", "headers": ["Mode", "When to use it"], "col_widths": [1.8, 5.6], "rows": [
                ["Fast", "Quick drafts, simple Q&A, rephrasing - lowest compute cost"],
                ["Thinking (3 Pro)", "Logic, math, planning, multi-step reasoning - plans before answering"],
                ["Deep Think", "Hardest problems (Ultra-only) - mentioned so you know the ceiling"],
            ]},
            {"type": "subhead", "text": "What to actually do with 1M context"},
            {"type": "bullets", "items": [
                "Drop an entire textbook or 200-page PDF and ask for a chapter-by-chapter summary",
                "Paste a whole codebase module and ask for a security / bug review",
                "Upload a 2-hour meeting transcript and extract decisions, owners and deadlines",
                "Feed a full contract and ask 'what are the 5 riskiest clauses for me?'",
            ]},
            {"type": "callout", "title": "Lesser-known: usage math", "color": G_BLUE, "text": (
                "Because limits are compute-based and refresh every 5 hours, do your heaviest Deep Think / Deep "
                "Research jobs in the morning, lighter chat in the afternoon. If you hit a model cap, Google "
                "auto-shifts you to a fast smaller model so you're never fully blocked."
            )},
        ],
        # ---------------------------------------------------------------- #
        # 9 - DEEP RESEARCH
        # ---------------------------------------------------------------- #
        [
            {"type": "heading", "text": "Tool 2: Deep Research"},
            {"type": "prose", "text": (
                "The single most underused Pro feature. Turn it on, type a topic, and Gemini shows a "
                "<b>research plan</b> (usually 6-12 sub-questions) that <b>you can edit before it runs</b>. It then "
                "browses dozens to hundreds of sources for several minutes and returns a structured, "
                "<b>cited multi-section report</b>. Pro gets <b>20 runs per day</b>."
            )},
            {"type": "callout", "title": "The 2026 game-changer most people miss", "color": G_PINK, "text": (
                "Deep Research no longer searches only the public web - it can also pull from <b>your own Gmail, "
                "Drive and Meet recordings</b>. So you can ask 'what has my team already decided about X?' and get a "
                "synthesis of the internet PLUS your private context, with citations to both."
            )},
            {"type": "subhead", "text": "High-leverage prompts to try"},
            {"type": "bullets", "items": [
                "Students: 'Build a cited literature review on <topic> with the 10 most important papers'",
                "Job seekers: 'Deep dive on <company> - business model, recent news, likely interview questions'",
                "Professionals: 'Compare <3 vendors> on price, security, integrations - table + recommendation'",
                "Founders: 'Map the Indian <market> 2026 - size, top players, gaps, with sources'",
            ]},
            {"type": "subhead", "text": "Turn the report into something usable"},
            {"type": "bullets", "items": [
                "Pipe it into Canvas to edit into a polished doc or slide outline",
                "Ask for an infographic via the Canva extension",
                "Ask Gemini to generate an Audio Overview so you can review it on a commute",
            ]},
        ],
        # ---------------------------------------------------------------- #
        # 10 - GEMS + SCHEDULED ACTIONS
        # ---------------------------------------------------------------- #
        [
            {"type": "heading", "text": "Tools 3 & 4: Gems and Scheduled Actions"},
            {"type": "subhead", "text": "Gems - build an AI assistant once, reuse it forever"},
            {"type": "prose", "text": (
                "A Gem is a saved AI persona: a role, a set of instructions, and optionally a connected Google Doc "
                "or NotebookLM notebook as its <b>knowledge base</b>. Every chat with that Gem opens with all that "
                "context pre-loaded - removing the 'explain who I am every time' tax. Open <b>Gem Manager</b> in the "
                "left sidebar of gemini.google.com, click New Gem, paste instructions, save (5 minutes once)."
            )},
            {"type": "cards_grid", "cards": [
                {"title": "Email Triager", "body": "Paste an email -> get action needed, urgency, and a 3-line reply."},
                {"title": "Outline Critic", "body": "Paste a draft outline -> it flags weak sections and missing arguments."},
                {"title": "Code Explainer", "body": "Paste unfamiliar code -> plain-English, line-by-line explanation."},
                {"title": "Learning Coach", "body": "Acts as a tutor for any subject; quizzes you instead of just answering."},
            ]},
            {"type": "subhead", "text": "Scheduled Actions - automation without leaving the chat"},
            {"type": "prose", "text": (
                "Ask Gemini to run a prompt on a schedule and it executes on its own, pulling from your connected "
                "Google tools - no need to be in the conversation."
            )},
            {"type": "code", "text": (
                "\"Every morning at 8 AM, summarise my unread emails and today's calendar.\"\n"
                "\"Every Monday, give me a competitor news digest on <X> with links.\"\n"
                "\"On the 1st of each month, draft a progress report from my Drive notes.\""
            )},
            {"type": "subhead", "text": "Build your first Gem in 60 seconds"},
            {"type": "code", "text": (
                "1.  gemini.google.com -> sidebar -> Gem Manager -> New Gem\n"
                "2.  Name it (e.g. 'Resume Reviewer')\n"
                "3.  Instructions: who it is + how it should respond + format\n"
                "4.  (Optional) attach a Google Doc / NotebookLM as its knowledge\n"
                "5.  Save - now it's one click away in every future session"
            )},
            {"type": "callout", "title": "The compounding effect", "color": G_GREEN, "text": (
                "Gems + Scheduled Actions are where the 18 months pay off long-term: a handful of well-built Gems "
                "and two or three automations quietly save hours every week. Build them early so they run all year."
            )},
            {"type": "prose", "text": (
                "<b>Note:</b> the core Gems feature is now available even on free accounts, but Pro adds higher "
                "capacity and full Workspace integration, so your Gems can read from Gmail, Docs and Drive."
            )},
        ],
        # ---------------------------------------------------------------- #
        # 11 - NOTEBOOKLM
        # ---------------------------------------------------------------- #
        [
            {"type": "heading", "text": "Tool 5: NotebookLM (a research superpower)"},
            {"type": "prose", "text": (
                "NotebookLM turns your own documents into a personal, citeable knowledge base. It only answers from "
                "the sources you give it, so it <b>doesn't hallucinate outside your materials</b> - perfect for study "
                "and research. Pro unlocks dramatically higher limits."
            )},
            {"type": "table", "headers": ["Limit", "Free / Basic", "Pro (yours)"], "col_widths": [2.7, 2.3, 2.4], "rows": [
                ["Notebooks", "Few", "500"],
                ["Sources per notebook", "~50", "300"],
                ["Chats per day", "Limited", "500"],
                ["Audio Overviews / day", "Few", "20"],
                ["Video Overviews", "No", "Yes"],
                ["Share notebooks", "No", "Yes"],
            ]},
            {"type": "subhead", "text": "Killer workflows"},
            {"type": "bullets", "items": [
                "Exam prep: upload notes + past papers, generate a quiz and an Audio Overview to revise on the go",
                "Audio Overview = an AI podcast of two hosts discussing your material - great for revision",
                "Video Overview = a narrated visual explainer built from your sources",
                "Job research: add a company's filings + news, then ask interview questions grounded in them",
                "Content/biz: feed 10 articles, export a briefing doc with citations in minutes",
            ]},
            {"type": "callout", "title": "Stack it with Gemini", "color": G_GREEN, "text": (
                "The Gemini iOS app can pull a NotebookLM notebook into a prompt, then run Canvas, Veo, Guided "
                "Learning or Deep Research on top of your notebook's contents."
            )},
        ],
        # ---------------------------------------------------------------- #
        # 12 - CANVAS + GUIDED LEARNING + LIVE
        # ---------------------------------------------------------------- #
        [
            {"type": "heading", "text": "Tools 6-8: Canvas, Guided Learning, Live"},
            {"type": "subhead", "text": "Canvas - a workspace beside your chat"},
            {"type": "prose", "text": (
                "Canvas opens a side-by-side editor - part Google Docs, part code editor. Draft and refine long "
                "documents in place, or describe an app in plain English and Gemini <b>writes the code and runs an "
                "interactive preview</b> - genuine no-code prototyping."
            )},
            {"type": "two_col_bullets",
             "left": [
                 "Draft essays, reports, posts and iterate visually",
                 "Build a calculator, quiz, or mini-site from a sentence",
             ],
             "right": [
                 "Turn research into interactive flashcards",
                 "Prototype a tool to show a client - no setup",
             ]},
            {"type": "subhead", "text": "Guided Learning - a tutor, not an answer machine"},
            {"type": "prose", "text": (
                "Guided Learning makes Gemini teach: it asks you questions, runs quizzes, and explains step by step "
                "instead of just handing over the answer. Available as a default Gem ('Learning Coach') - ideal for "
                "students and for ramping up on an unfamiliar topic before a meeting."
            )},
            {"type": "subhead", "text": "Gemini Live - hands-free, multimodal"},
            {"type": "bullets", "items": [
                "Hold a natural voice conversation on mobile",
                "Share your camera ('what is this part?') or your screen ('explain this error')",
                "Connected to Google Maps, Calendar, Tasks and Keep so it can act, not just talk",
            ]},
        ],
        # ---------------------------------------------------------------- #
        # 13 - CREATIVE STACK
        # ---------------------------------------------------------------- #
        [
            {"type": "heading", "text": "Tools 9-12: The Creative Stack"},
            {"type": "prose", "text": (
                "Pro includes <b>1,000 AI credits per month</b> for media generation across Google's creative studio. "
                "Here's what each tool does and what your Pro tier gets."
            )},
            {"type": "table", "headers": ["Tool", "What it does", "Pro allowance"], "col_widths": [1.5, 4.1, 1.8], "rows": [
                ["Flow", "AI filmmaking studio - storyboard scenes into films", "1,000 credits/mo"],
                ["Veo 3.1 Fast", "Text/image to video clips inside Flow & Gemini", "~50 videos/mo"],
                ["Whisk", "Animate a still image into a short video sequence", "~50 / month"],
                ["Nano Banana Pro", "High-quality image generation & one-photo editing", "~100 images/day"],
                ["Lyria 3", "AI music generation", "Included"],
                ["Gemini Omni", "New model: create/edit video from text+image+video", "Included"],
            ]},
            {"type": "callout", "title": "Gemini Omni - the newest unlock", "color": G_PURPLE, "text": (
                "Omni combines Gemini's reasoning with Google's media models. Upload any photo or clip from your "
                "camera roll, apply one-click templates, and edit conversationally - it even keeps a character's "
                "identity and voice consistent across scenes. No equipment or jargon required."
            )},
            {"type": "subhead", "text": "Practical creative prompts"},
            {"type": "bullets", "items": [
                "Reels/marketing: 'cinematic 8-second product shot of <item> on a marble table, soft light'",
                "Personal: animate an old family photo into a gentle moving portrait with Whisk",
                "Thumbnails/posts: generate 4 variations of a hero image, then edit one with Nano Banana",
            ]},
        ],
        # ---------------------------------------------------------------- #
        # 14 - WHO SHOULD USE IT (use cases) + storage + perks
        # ---------------------------------------------------------------- #
        [
            {"type": "heading", "text": "How Students, Pros & Businesses Win"},
            {"type": "cards_grid", "cards": [
                {"title": "Students", "body": "NotebookLM for notes->quizzes->audio revision; Guided Learning tutor; Deep Research for cited essays; 5 TB for every project file.", "color": G_BLUE},
                {"title": "Job seekers", "body": "Deep Research on target companies; a Resume Reviewer Gem; mock-interview Gems; Canvas to tailor each application.", "color": G_GREEN},
                {"title": "Professionals", "body": "Workspace side-panel in Gmail/Docs/Sheets; Email Triager + Meeting Decoder Gems; Scheduled morning briefings.", "color": G_PINK},
                {"title": "Businesses", "body": "Deep Research market/competitor reports; NotebookLM as a team knowledge base; Flow/Veo for ad creative; 5 TB shared storage.", "color": G_PURPLE},
                {"title": "Creators", "body": "Flow + Veo + Whisk + Nano Banana for video and images; Omni for fast edits; 1,000 credits/month.", "color": CORAL},
                {"title": "Everyone", "body": "5 TB backups, YouTube Premium Lite (fewer ads), Google Home Premium, Gemini Live as a daily assistant.", "color": G_YELLOW},
            ]},
            {"type": "subhead", "text": "Don't forget the non-AI perks"},
            {"type": "bullets", "items": [
                "5 TB Google One - back up phones, move large files off device, add family members to the plan",
                "YouTube Premium Lite - reduced ads on most videos, included at no extra charge",
                "Google Home Premium - enhanced features for Nest devices",
                "Developer credits for Google Cloud / Antigravity for those who build",
            ]},
        ],
        # ---------------------------------------------------------------- #
        # 15 - TROUBLESHOOTING + CTA
        # ---------------------------------------------------------------- #
        [
            {"type": "heading", "text": "Troubleshooting & Final Checklist"},
            {"type": "table", "headers": ["Problem", "Fix"], "col_widths": [2.5, 4.9], "rows": [
                ["No banner in MyJio", "Recharge Rs 349+, update app, wait up to 24h, or use jio.com/google-gemini-offer"],
                ["Claim fails at Google login", "Use a personal @gmail.com, disable VPN, retry in a browser"],
                ["Pro not showing after claim", "Wait 30 min, sign out/in to Google, recheck one.google.com"],
                ["NotebookLM still on free limits", "Open notebooklm.google.com signed in to the SAME Gmail you linked"],
                ["Benefits suddenly stopped", "Your eligible Jio plan likely lapsed - recharge to restore"],
                ["Wrong Gmail linked", "Contact Jio + Google support early - switching the linked account is hard"],
                ["Hitting usage limits fast", "Limits are compute-based; batch heavy jobs, lighter chat refreshes every 5h"],
            ]},
            {"type": "callout", "title": "Post-claim checklist", "color": G_GREEN, "text": (
                "MyJio shows 'claimed'  -  gemini.google.com shows Pro  -  one.google.com shows 5 TB  -  "
                "NotebookLM expanded limits live  -  Gemini enabled in Gmail settings  -  first Gem created."
            )},
            {"type": "prose", "text": (
                "<b>Sources:</b> jio.com/google-gemini-offer, one.google.com AI plans, Google I/O 2026 subscription "
                "announcements, and Google support documentation. Offer terms, plan thresholds, usage caps and "
                "storage can change - always verify on official Google and Jio pages before claiming."
            )},
            {"type": "callout", "title": "Found this useful?", "color": CORAL, "text": (
                "Comment FREE and follow <b>@piyush.glitch</b> for more no-fluff AI guides, tool breakdowns and "
                "offers worth claiming."
            )},
        ],
    ]


def build() -> Path:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    build_pdf(OUT, pages(), cover=True)
    return OUT


if __name__ == "__main__":
    p = build()
    print(f"OK {p}", flush=True)
