# -*- coding: utf-8 -*-
"""Content for the Claude2ndJune batch - 5 carousels in the 'Claude agents that run my X system'
reference style (Meghanify-like). Each entry holds the full 10-slide plan, but for this first pass
only the COVER (slide 1) image is generated. The reference PDF stores the full plan + image-prompt
notes so the remaining 9 slides can be generated later with consistent design.

Visual language (match reference exactly):
- Warm off-white / cream paper background, soft grain, gentle drop shadows.
- HUGE bold black geometric sans headline (number + 'Claude agents').
- One line in a hand-marker HIGHLIGHT (alternating warm yellow / lime / pink) = 'that run my X system'.
- A pinned PINK sticky note with a short handwritten phrase + realistic push-pin.
- A coral/terracotta rounded-square Claude logo card with the white sparkle/star mark.
- Small pink 'Swipe to see the workflow ->' line with a hand-drawn arrow.
- BOTTOM HALF: a real, candid, photoreal photo (NOT AI-looking) of an Indian creator/founder.
- Footer center: @piyush.glitch.
- Ratio strictly 4:5 (1080 x 1350).
"""

# Shared design system --------------------------------------------------------
STYLE_BLOCK = """
DESIGN SYSTEM (follow precisely, this is a premium editorial Instagram carousel COVER):
- Aspect ratio STRICTLY 4:5 vertical portrait, 1080x1350 feel. Composition is split:
  TOP 55% is clean graphic design on warm off-white cream paper (#F6F1E7) with very subtle paper grain
  and soft long drop shadows; BOTTOM 45% is a real photograph with a thin cream border/rounded corners.
- Typography: a HUGE, bold, slightly condensed geometric sans-serif headline in near-black ink (#16150F),
  tight leading, confident and modern (think Aileron / Sharp Grotesk / Archivo Black energy).
- HIGHLIGHTER accent: render the sub-headline line as if swiped with a translucent hand-marker highlighter
  (warm yellow #F5D547, lime #C7E06B, or soft pink #F5A8C0 depending on the carousel) behind black text.
- One PINK sticky note (square, #F7A8C4) tilted ~6 degrees with a realistic metal/plastic PUSH-PIN and a soft
  cast shadow, containing a short HANDWRITTEN marker phrase in black.
- A CLAUDE LOGO card: a terracotta/coral rounded-square (#D97757) with the official Anthropic Claude white
  multi-point sparkle/star mark centered, as a small floating 3D sticker with soft shadow.
- Small line in pink marker: 'Swipe to see the workflow ->' with a quick hand-drawn arrow.
- Footer: '@piyush.glitch' centered in small clean grey sans near the very bottom.
- Mood: high-end design studio, calm, expensive, scroll-stopping, NOT a generic tech template.
- STRICT: correct spelling only, no lorem ipsum, no extra random text, no watermark, no Instagram UI,
  no slide number on the cover, no distorted logo, no garbled letters.
"""

PHOTO_RULES = """
PHOTOGRAPHY (critical - must look like a REAL photo, NOT AI-generated):
- Authentic candid documentary photograph, shot on a 35mm full-frame camera, natural available light,
  realistic skin texture with pores and tiny imperfections, true-to-life color, mild film grain,
  shallow depth of field with natural lens bokeh, subtle motion-life imperfection - absolutely not glossy,
  not plastic, not over-smoothed, no waxy skin, no extra fingers, no warped hands, no uncanny eyes.
- Real-world environment with believable clutter and depth. The subject is relaxed and unposed.
- Color-grade the photo to sit harmoniously with the warm cream design above it.
"""


def C(slug, number_word, headline_main, system_line, highlight_color, sticky, photo, scene,
      agents, caption, bottom_bar):
    return {
        "slug": slug,
        "number_word": number_word,
        "headline_main": headline_main,
        "system_line": system_line,
        "highlight_color": highlight_color,
        "sticky": sticky,
        "photo": photo,
        "scene": scene,
        "agents": agents,
        "caption": caption,
        "bottom_bar": bottom_bar,
    }


CAROUSELS = [
    C(
        slug="01_Marketing_System",
        number_word="10",
        headline_main="Claude agents",
        system_line="that run my marketing system",
        highlight_color="lime #C7E06B",
        sticky="1 system.\nMore leverage.",
        photo="a young Indian male marketing lead (early 30s) in a crisp white shirt at a bright agency desk, "
              "leaning forward studying analytics on a large monitor, pen and notebook beside him, editorial daylight",
        scene=(
            "BOTTOM PHOTO: a candid real editorial photograph of a young Indian male marketing lead (early 30s) "
            "in a crisp white open-collar shirt, sitting at a bright modern agency desk, leaning slightly forward "
            "studying analytics and funnel charts on a large curved monitor, a leather notebook and pen beside the "
            "keyboard, soft natural daylight from floor-to-ceiling windows, shallow depth of field, confident focused "
            "expression, not posing for camera. Shot like a Wired or Fast Company profile - premium, believable, real skin."
        ),
        agents=[
            ("Market Research Agent", "Finds trends, pain points, search intent and market opportunities.",
             "inputs -> market scan -> pain points -> opportunities", "clearer positioning + sharper pain points"),
            ("ICP Agent", "Builds your ideal-customer profile from real data, reviews and objections.",
             "data -> segments -> ICP -> objections", "one sharp ICP your whole funnel can target"),
            ("Competitor Analysis Agent", "Breaks down competitor positioning, offers and content gaps.",
             "competitor pages -> messaging -> gaps -> differentiation", "where you win and how to position"),
            ("Content Strategy Agent", "Turns research into pillars, angles and a weekly plan.",
             "research -> pillars -> angles -> weekly plan", "a repeatable content engine"),
            ("LinkedIn Post Agent", "Drafts hook-led posts in your voice from a single idea.",
             "idea -> hook -> body -> CTA", "a week of posts in one run"),
            ("Email Campaign Agent", "Writes sequences mapped to funnel stage and objection.",
             "segment -> sequence -> subject lines -> CTA", "sequences that get opened and clicked"),
            ("Ad Copy Agent", "Generates angle-tested ad variations with negative prompts.",
             "offer -> angles -> variations -> hooks", "scroll-stopping ad variants to test"),
            ("Marketing Ops Agent", "Schedules, tracks and reports - the glue that ships it.",
             "calendar -> publish -> metrics -> report", "a system that runs without you"),
        ],
        caption=(
            "Comment AGENT and I'll send the full build guide (the 10 agents + the prompts + how they hand off).\n\n"
            "Most people use Claude like a smarter Google. Operators wire it into a system.\n\n"
            "This is the 10-agent marketing system I run: market research, ICP, competitor analysis, content "
            "strategy, LinkedIn, email, ad copy, landing pages, analytics and marketing ops - each a Claude agent "
            "with one job, handing structured output to the next.\n\n"
            "Swipe to see the workflow. Save this so you can build it.\n\n"
            "Follow @piyush.glitch for operator-level AI systems.\n\n"
            "#ClaudeAI #AIagents #MarketingSystem #AIforBusiness #ContentStrategy"
        ),
        bottom_bar=["Market Research", "ICP", "Competitor", "Content", "LinkedIn", "Email", "Ad Copy", "Ops"],
    ),
    C(
        slug="02_SMB_Stack_Killer",
        number_word="9",
        headline_main="Claude skills",
        system_line="that replaced my $750/mo tool stack",
        highlight_color="warm yellow #F5D547",
        sticky="Cancelled\n4 tools.",
        photo="a real Indian small-business owner (early 30s, man) at a tidy home-office desk reviewing an invoice "
              "on a laptop, a coffee mug and notebook beside him, soft daylight, candid not posed",
        scene=(
            "BOTTOM PHOTO: a candid real photograph of an Indian small-business owner, a man in his early 30s in a "
            "casual shirt, sitting at a tidy wooden home-office desk, looking at a laptop screen that shows a simple "
            "invoice/dashboard, a ceramic coffee mug and a paper notebook with a pen beside the laptop, soft natural "
            "daylight from a window, warm and real, slight depth of field, lived-in workspace."
        ),
        agents=[
            ("/business-pulse", "QuickBooks + Stripe + HubSpot into a 90-second Monday dashboard.",
             "connect -> pull -> summarize -> 3 to-dos", "cash, revenue, pipeline before coffee"),
            ("/invoice-chase", "Scans overdue invoices, drafts tone-matched reminders per client.",
             "scan -> match tone -> draft -> queue", "recover $2k-$10k you were owed"),
            ("/lead-triage", "Scores every open lead by fit and engagement, drafts follow-ups.",
             "CRM -> score -> rank -> draft", "stop chasing dead leads"),
            ("/monday-brief", "One page: cash, sales, pipeline and the 3 things that matter.",
             "data -> brief -> priorities -> owners", "your week, decided in 60 seconds"),
            ("/contract-review", "Flags red-flag clauses in plain English before you sign.",
             "upload -> parse -> red flags -> plain English", "a $300 review in 45 seconds"),
            ("/job-post-builder", "Full listing + weighted candidate scorecard in under a minute.",
             "role -> listing -> scorecard -> rubric", "hire without the agency fee"),
            ("/receipt-sorter", "Sorts receipts, tags expenses, preps them for your books.",
             "inbox -> extract -> categorize -> export", "tax season stops being a nightmare"),
            ("/client-checkin", "Drafts proactive check-ins so accounts never go cold.",
             "account -> signal -> draft -> schedule", "retention on autopilot"),
        ],
        caption=(
            "Comment SKILLS and I'll send the exact list + which connector each one needs.\n\n"
            "Anthropic shipped 31 pre-built Claude Skills for small businesses - 382,000 downloads on day one. "
            "They plug into the tools you already pay for: QuickBooks, Stripe, HubSpot, Gmail, Square, Canva.\n\n"
            "I ran them for a month and cancelled four subscriptions. These are the 9 that actually replaced "
            "paid tools - cash flow, invoice chasing, lead triage, contract review and more.\n\n"
            "Swipe to see them. Save this before your next renewal.\n\n"
            "Follow @piyush.glitch for AI that pays for itself.\n\n"
            "#ClaudeAI #SmallBusiness #AItools #Automation #Founders"
        ),
        bottom_bar=["Pulse", "Invoice", "Leads", "Brief", "Contracts", "Hiring", "Receipts", "Clients"],
    ),
    C(
        slug="03_Business_As_Projects",
        number_word="5",
        headline_main="Claude Projects",
        system_line="that run my entire business",
        highlight_color="soft pink #F5A8C0",
        sticky="My whole\nbusiness. 1 OS.",
        photo="a real Indian male entrepreneur (early 30s) in a minimal Scandinavian home office, leather notebook "
              "open beside MacBook and iPad, morning window light, thoughtful and calm, editorial not stock",
        scene=(
            "BOTTOM PHOTO: a candid real editorial photograph of an Indian male entrepreneur (early 30s) in a "
            "minimal Scandinavian-style home office - light oak desk, single MacBook and iPad showing organized "
            "project folders, an open leather notebook with handwritten notes, ceramic pour-over coffee, soft "
            "morning window light from the left, muted neutral tones, plants blurred in background. He looks "
            "thoughtfully at the screens with a slight smile, relaxed and unposed. Premium editorial quality like "
            "Monocle or Kinfolk magazine - authentic skin texture, believable clutter, not AI-smooth."
        ),
        agents=[
            ("Client Intelligence Hub", "Every client's context, history and preferences in one Project.",
             "docs -> instructions -> memory -> recall", "never re-explain a client again"),
            ("Content Production Engine", "Briefs in, on-brand drafts out, with your voice baked in.",
             "brief -> draft -> meta -> review", "first drafts in your voice"),
            ("Operations & Admin", "Drafts everything, sends nothing - flags money and deadlines [REVIEW].",
             "task -> draft -> [REVIEW] flag -> human", "volume handled, judgment kept"),
            ("Writer Management", "Onboards writers, enforces style, reviews against the guide.",
             "guide -> brief -> review -> feedback", "consistent quality at scale"),
            ("Strategy Partner", "A thinking partner loaded with your real numbers and goals.",
             "context -> options -> tradeoffs -> decision", "better decisions, faster"),
            ("Knowledge Base", "Your SOPs, FAQs and policies become answerable, living context.",
             "upload -> index -> instruct -> answer", "the company brain that stays current"),
            ("Onboarding Project", "Turns a messy intake into a clean, repeatable client start.",
             "intake -> checklist -> assets -> kickoff", "onboarding that never drops a ball"),
            ("Reporting Project", "Raw numbers become a narrative report with next actions.",
             "data -> narrative -> insights -> actions", "reports clients actually read"),
        ],
        caption=(
            "Comment OS and I'll send the 5-Project setup (instructions, knowledge files, the [REVIEW] rule).\n\n"
            "I stopped using Claude as a chatbot and turned my whole business into 5 Claude Projects - each with "
            "its own knowledge base, custom instructions and memory.\n\n"
            "Client intelligence, content production, operations, writer management and a strategy partner. It "
            "runs onboarding, drafts deliverables, triages support and hands only the exceptions to me.\n\n"
            "Swipe to see the system. Save it and build your own OS.\n\n"
            "Follow @piyush.glitch for the operator playbook.\n\n"
            "#ClaudeAI #BusinessSystems #AIagents #Productivity #Founders"
        ),
        bottom_bar=["Clients", "Content", "Ops", "Writers", "Strategy", "Knowledge", "Onboard", "Reports"],
    ),
    C(
        slug="04_Content_Engine",
        number_word="8",
        headline_main="Claude agents",
        system_line="that run my content engine",
        highlight_color="lime #C7E06B",
        sticky="1 idea ->\n12 posts.",
        photo="a real young Indian male creator at a desk with a microphone and ring light slightly out of frame, "
              "editing on a laptop, headphones around his neck, candid creative-studio vibe, natural light",
        scene=(
            "BOTTOM PHOTO: a candid real photograph of a young Indian male content creator (late 20s) at a creator "
            "desk, headphones resting around his neck, editing on a laptop, a podcast microphone and a softly "
            "out-of-focus ring light at the edge of frame, warm practical lighting, authentic creative studio, "
            "real skin texture, relaxed unposed expression."
        ),
        agents=[
            ("Transcript Agent", "Turns a raw video/voice note into clean, structured source text.",
             "audio -> transcript -> clean -> sections", "one source of truth to repurpose"),
            ("Hook Lab Agent", "Generates 15 angle candidates, picks the scroll-stopping winner.",
             "topic -> 15 angles -> score -> winner", "a hook that earns the swipe"),
            ("Carousel Agent", "Builds hook + slide headlines + body + CTA in your format.",
             "idea -> structure -> copy -> CTA", "a full carousel in one run"),
            ("Thread Agent", "Reshapes the same idea into a tight X/LinkedIn thread.",
             "core -> beats -> thread -> hook", "platform-native, not copy-paste"),
            ("Newsletter Agent", "Expands the idea into a story-led email with one CTA.",
             "idea -> story -> value -> CTA", "an issue your list opens"),
            ("Repurpose Lead", "Coordinates agents so no two platforms lead with the same angle.",
             "core -> assign -> dedupe -> ship", "5 platforms, zero overlap"),
            ("Caption Agent", "Writes save-worthy captions with comment-bait CTAs.",
             "post -> caption -> CTA -> hashtags", "captions engineered for saves"),
            ("Scheduler Agent", "Slots everything into the calendar at your best times.",
             "assets -> calendar -> queue -> publish", "distribution that runs itself"),
        ],
        caption=(
            "Comment ENGINE and I'll send the content team setup (the agents + how the lead dedupes angles).\n\n"
            "One idea should become a week of content. Most creators rewrite it five times by hand.\n\n"
            "This is the 8-agent content engine I run: transcript, hook lab, carousel, thread, newsletter, a "
            "repurpose lead that stops platforms from sounding identical, captions and scheduling.\n\n"
            "Swipe to see the workflow. Save this and stop starting from a blank page.\n\n"
            "Follow @piyush.glitch for content systems that compound.\n\n"
            "#ClaudeAI #ContentCreation #AIagents #CreatorEconomy #Repurposing"
        ),
        bottom_bar=["Transcript", "Hooks", "Carousel", "Thread", "Newsletter", "Repurpose", "Caption", "Schedule"],
    ),
    C(
        slug="05_Sales_Pipeline",
        number_word="7",
        headline_main="Claude agents",
        system_line="that run my sales pipeline",
        highlight_color="warm yellow #F5D547",
        sticky="Pipeline,\nnot vibes.",
        photo="a sharp Indian woman sales leader (late 20s) in a tailored blazer during a confident video call on "
              "laptop in a glass meeting room, CRM visible on screen, premium corporate energy, candid editorial",
        scene=(
            "BOTTOM PHOTO: a candid real editorial photograph of a sharp Indian woman sales leader (late 20s) "
            "wearing a tailored navy blazer over a simple top, standing during a video sales call on a laptop "
            "propped on a glass conference table, the screen shows a clean CRM pipeline board, modern glass-walled "
            "meeting room with blurred city view, confident warm expression mid-conversation, natural side light, "
            "shallow depth of field. Shot like a Bloomberg or Forbes profile - premium, aspirational, real skin "
            "texture and fabric detail, absolutely not stock-photo stiff or AI-waxy."
        ),
        agents=[
            ("Lead Triage Agent", "Scores inbound by fit and intent, routes the hot ones first.",
             "inbound -> score -> rank -> route", "only work leads worth working"),
            ("Research Agent", "Builds a one-page brief on each prospect before the call.",
             "name -> sources -> brief -> angles", "walk in already knowing them"),
            ("Outreach Agent", "Drafts personalized first-touch in your tone, not a template.",
             "brief -> hook -> message -> follow-up", "replies, not ignores"),
            ("Proposal Agent", "Turns a discovery call into a scoped, priced proposal draft.",
             "notes -> scope -> price -> proposal", "proposals out same day"),
            ("Objection Agent", "Prepares tailored responses to each prospect's likely objections.",
             "context -> objections -> responses -> proof", "never caught off guard"),
            ("Win-Loss Agent", "Analyzes closed deals to find what actually moves the needle.",
             "deals -> patterns -> reasons -> playbook", "a playbook from real outcomes"),
            ("Pipeline Ops Agent", "Keeps the CRM clean, nudges stalled deals, reports weekly.",
             "CRM -> hygiene -> nudges -> report", "a pipeline that stays honest"),
            ("Follow-up Agent", "Drafts the right next touch at the right time, every time.",
             "stage -> timing -> draft -> queue", "deals stop dying in silence"),
        ],
        caption=(
            "Comment SALES and I'll send the pipeline build (the 7 agents + the scoring + follow-up cadence).\n\n"
            "Most pipelines run on vibes and forgotten follow-ups. Mine runs on agents.\n\n"
            "Lead triage, prospect research, outreach, proposals, objection prep, win-loss analysis and pipeline "
            "ops - each a Claude agent with one job, gated on human approval before anything sends.\n\n"
            "Swipe to see the workflow. Save this if your follow-up is leaking deals.\n\n"
            "Follow @piyush.glitch for sales systems that close.\n\n"
            "#ClaudeAI #Sales #AIagents #B2B #Pipeline"
        ),
        bottom_bar=["Triage", "Research", "Outreach", "Proposal", "Objection", "Win-Loss", "Pipeline", "Follow-up"],
    ),
]
