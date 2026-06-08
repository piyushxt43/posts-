# -*- coding: utf-8 -*-
"""Draftly Growth - 5 carousels x 8 slides. Visual AI Club twist + DRAFTLY brand."""

from __future__ import annotations

BASE = """
3:4 vertical portrait ONLY (1080x1440). Premium Instagram carousel slide.
Crisp readable text, perfect spelling, no lorem ipsum, no watermarks, no slide numbers on image.
Footer bottom-left: draftly.space in small grey sans. NO progress dots. NO SWIPE arrow.
Top-right: DRAFTLY wordmark in bold Space Grotesk caps (text only, NO icon logo).
"""

SKY_F = BASE + """
SLIDE TYPE: Visual AI Club sky hero - bright blue sky, soft clouds, low-angle cinematic.
Female model late 20s, wavy dirty-blonde, light freckles, terracotta-rust flowing linen outfit,
confident calm expression, wind in hair, 24-35mm film grade. Sky dominates - NO dark studio.
Top center tiny white caps: DRAFTLY. Upper-right frosted pill: 3D WEBSITE BUILDER.
Lower third huge white bold sans headline + white italic serif second line as specified.
White pill CTA bottom center black uppercase text as specified.
"""

SKY_M = BASE + """
SLIDE TYPE: Sky hero - male founder energy. Man early 30s, olive linen shirt, stubble,
holding MacBook at chest, bright blue sky behind, low-angle heroic, cinematic warm grade.
Top center DRAFTLY white caps. Lower third white headline stack as specified.
White pill CTA as specified. NO dark background.
"""

SKY_CTA = BASE + """
SLIDE TYPE: Sky hero finale - side profile terracotta outfit OR founder silhouette against blue sky.
Lower third white headline. White pill CTA as specified. DRAFTLY top center.
"""

INTERIOR = BASE + """
SLIDE TYPE: Educational cream grid #F4EEDE - premium Draftly interior slide.
Top small caps: DRAFTLY. Huge bold black sans headline; ONE phrase coral #EF5E45 or italic serif.
2-3 cream cards thin border - render ALL specified text EXACTLY. Monospace for prompts/code.
Coral accent tabs and numbered steps. Strong whitespace. draftly.space footer.
"""

EDITORIAL = BASE + """
SLIDE TYPE: Full-bleed editorial photo with text overlay lower third - NOT cream grid.
Cinematic product or workspace photography as specified. White or black text overlay.
Magazine quality lighting. DRAFTLY top center.
"""

PROMPT = BASE + """
SLIDE TYPE: Cream grid prompt slide - MUST show multi-paragraph prompt text FULLY READABLE.
Left: coral step pill + headline. Right or center: large warm card with 2-3 paragraphs monospace prompt.
Hand-drawn coral arrow optional. Text must be legible at phone size. DRAFTLY top-right.
"""


def slide(fn, p):
    return (fn, p.strip())


def C(slug, pdf, caption, data, slides):
    return {"slug": slug, "pdf_name": pdf, "caption": caption, **data, "slides": slides}


# --- Carousel 01: Pipeline + DeFi ---
C01_DATA = {
    "title": "One Prompt to Production",
    "keyword": "BUILD",
    "topic": "DeFi Staking - Rivr Protocol",
    "website_prompt": (
        "Build a DeFi crypto staking platform landing page for Rivr Protocol. "
        "Floating centered nav pill with links Stake, Pools, Docs, Launch App. "
        "Hero headline 'Stake Smarter. Earn Faster.' with subcopy on liquid staking, "
        "12% APY range, audited smart contracts, and instant unstaking windows.\n\n"
        "Scroll sections after hero: live APY ticker strip with monospace numbers, "
        "three pool cards (ETH, SOL, USDC) with TVL and reward rate, security audit "
        "badges row (CertiK, Trail of Bits), how-it-works 3-step diagram with icons, "
        "wallet connect CTA with MetaMask and WalletConnect chips, footer Discord and GitHub.\n\n"
        "Dark hero transitioning to deep purple-gray tech section. Typography bold grotesque "
        "headlines, monospace for APY. Motion: hero background scrubs with scroll using "
        "extracted video frames. Web3 premium - not generic AI purple gradient slop."
    ),
    "image_prompt": (
        "Cinematic photoreal Web3 staking hero still for scroll-scrubbed landing page. "
        "No text, no logos, 16:9 landscape suitable for 200+ extracted frames.\n\n"
        "Scene: two floating holographic ETH and SOL tokens above dark tempered glass "
        "platform, deep space navy gradient background, volumetric blue-purple rim light "
        "on token edges, faint grid reflection on glass surface.\n\n"
        "Camera: 50mm equivalent, slight low angle, shallow depth of field, creamy bokeh "
        "on distant particles. Color grade: cool shadows, warm accent on token highlights. "
        "Premium crypto campaign quality - never neon oversaturation."
    ),
    "first_frame_prompt": (
        "Opening keyframe: wide tableau, tokens resting on glass platform, dim ambient, "
        "LED indicators off, lots of negative space left third for headline overlay, "
        "same navy environment, 16:9, no text, photoreal."
    ),
    "last_frame_prompt": (
        "Closing keyframe: tokens elevated and rotating slightly, rim light intensified, "
        "camera 20% closer, particle field denser, green accent glow on platform edge, "
        "same environment, no text."
    ),
    "video_prompt": (
        "Slow orbital dolly clockwise around floating tokens. Subtle particle drift upward, "
        "glass reflection shimmer, premium DeFi reveal pacing, seamless 8-second loop, "
        "no text overlays, no strobe."
    ),
}

# --- Carousel 02: Presets + Agency ---
C02_DATA = {
    "title": "47 Presets Zero Blank Canvas",
    "keyword": "PRESET",
    "topic": "Creative Agency - Axion Studio",
    "website_prompt": (
        "Create a creative agency landing page for Axion Studio. Wordmark nav left, "
        "links Work, Services, Studio, Contact in muted uppercase tracking. "
        "Hero headline 'We Build Brands That Move' with subcopy on motion-first identity "
        "for Series B startups and luxury DTC.\n\n"
        "Scroll sections: featured projects grid (asymmetric 2-col), services trio "
        "(Brand Strategy, Web and Motion, Campaign Production), team portrait row "
        "with hover bios, client logo strip, testimonial slider with serif pull quotes, "
        "project inquiry form with budget dropdown.\n\n"
        "Palette cream and charcoal with single coral CTA. Editorial typography mix. "
        "Hero motion scrubs through showreel frames on scroll. Premium agency - "
        "not template marketplace aesthetic."
    ),
    "image_prompt": (
        "High-fashion creative agency environment for scroll frames. No text, 16:9. "
        "Minimal concrete studio with large format monitor showing motion graphics, "
        "designer hands on trackpad in foreground blur, morning side light through "
        "industrial windows, terracotta accent chair, mood boards pinned on wall soft focus.\n\n"
        "Atmosphere: calm creative confidence, shallow DOF, warm stone grays and cream tones, "
        "fine film grain. Camera at desk height 35mm. Avoid cluttered startup chaos aesthetic."
    ),
    "first_frame_prompt": "Wide empty studio, monitor off, morning light beam, negative space left, no text.",
    "last_frame_prompt": "Monitor glowing with colorful motion reel, hands active on keyboard, tighter crop, no text.",
    "video_prompt": "Slow dolly toward monitor as reel animates. Light dust in sunbeam, calm agency film pacing, 8s loop.",
}

# --- Carousel 03: Pricing + Analytics SaaS ---
C03_DATA = {
    "title": "Stop Paying 5K For Hero",
    "keyword": "PRICING",
    "topic": "Analytics SaaS - Nordhaven",
    "website_prompt": (
        "Build an analytics SaaS landing page for Nordhaven Analytics. Nav Product, Solutions, "
        "Pricing, Book Demo. Hero 'See Your Pipeline Before It Breaks' with subcopy on "
        "revenue forecasting, CRM sync, and anomaly alerts for sales teams.\n\n"
        "Sections: dashboard screenshot hero in browser chrome, three integration cards "
        "(Salesforce, HubSpot, Stripe), ROI calculator widget mockup, customer logo wall, "
        "security SOC2 badge row, book demo form with company size selector.\n\n"
        "Clean white hero into soft gray product section. Trust-first B2B typography. "
        "Scroll-synced UI motion in hero from extracted frames. Enterprise credible - "
        "not meme startup gradients."
    ),
    "image_prompt": (
        "B2B SaaS dashboard hero still for scroll site. No text, 16:9. Floating laptop "
        "showing analytics charts with upward trend lines, glass desk, soft office bokeh, "
        "cool morning window light, navy and white color story with single green accent on chart.\n\n"
        "Photoreal product photography style. Camera slightly above desk, 40mm, crisp screen "
        "detail without readable fake UI text."
    ),
    "first_frame_prompt": "Laptop closed on desk, wide office, pre-demo calm, cool light, no text.",
    "last_frame_prompt": "Laptop open dashboard glowing, tighter crop on screen, same desk, no text.",
    "video_prompt": "Gentle push-in toward laptop screen as charts appear to animate. Subtle parallax on desk objects, 8s loop.",
}

# --- Carousel 04: Scroll Engine + Luxury EV ---
C04_DATA = {
    "title": "No WebGL Just Scroll",
    "keyword": "SCROLL",
    "topic": "Luxury EV - Silence Amplified",
    "website_prompt": (
        "Build a luxury electric vehicle brand landing page. Nav Vehicle, Technology, Reserve. "
        "Hero headline 'Silence, Amplified.' with subcopy on 800V architecture, 520-mile range, "
        "and 2.9s 0-60.\n\n"
        "Scroll sections: exterior beauty strip with scroll-scrubbed drive frames, interior "
        "material callouts (vegan leather, recycled aluminum), charging network map, "
        "configurator color swatches (obsidian, glacier, bronze), reserve deposit CTA.\n\n"
        "Monochrome hero into warm bronze accents. Automotive editorial typography. "
        "Motion scrubs extracted desert highway drive sequence. Rivian-adjacent premium - "
        "not stock car template."
    ),
    "image_prompt": (
        "Cinematic automotive hero for scroll-scrubbed EV landing. No text, 16:9. Sleek "
        "matte bronze electric sedan on desert highway at dawn, long shadow, heat haze "
        "on horizon, mountains soft background.\n\n"
        "Lighting: golden hour key from left, cool fill sky, 35mm low front three-quarter "
        "camera. Photoreal automotive campaign - no exaggerated CGI shine."
    ),
    "first_frame_prompt": "Car distant silhouette on highway, wide dawn landscape, lots of sky, no text.",
    "last_frame_prompt": "Car close three-quarter front, headlights on, same highway, camera nearer, no text.",
    "video_prompt": "Slow tracking shot as car glides forward on highway. Heat shimmer, wheel rotation subtle, cinematic automotive 8s loop.",
}

# --- Carousel 05: Agency workflow + Wellness ---
C05_DATA = {
    "title": "Agency Pitch in 20 Minutes",
    "keyword": "AGENCY",
    "topic": "Wellness Studio - Equilibrium",
    "website_prompt": (
        "Design a wellness and yoga studio landing page for Equilibrium Studio. Nav Classes, "
        "Schedule, Instructors, Membership. Hero 'Find Your Center' with subcopy on heated "
        "vinyasa, reformer pilates, and infrared recovery suites.\n\n"
        "Scroll sections: weekly class schedule grid, instructor cards with specialties, "
        "studio interior gallery, membership tiers (Drop-in, Monthly, Unlimited), "
        "first class free CTA, location map with parking note.\n\n"
        "Soft sage and cream palette. Calm grotesque typography. Hero scrubs through "
        "slow-motion studio atmosphere frames. Aesop-meets-Equinox calm - not generic gym template."
    ),
    "image_prompt": (
        "Wellness studio hero still for scroll frames. No text, 16:9. Sunlit yoga studio "
        "with linen curtains, woman in neutral activewear in warrior pose silhouette soft focus, "
        "plants and warm wood floors, steam mist catching window light.\n\n"
        "Serene spa atmosphere, shallow DOF, muted sage and cream tones. Camera wide 28mm "
        "from corner. Peaceful not stock-photo cheesy smile."
    ),
    "first_frame_prompt": "Empty studio at dawn, mats rolled, wide calm space, soft light, no people, no text.",
    "last_frame_prompt": "Single practitioner mid-flow, tighter composition, warmer light, same studio, no text.",
    "video_prompt": "Slow dolly through studio as light shifts. Curtain drift, dust motes in sunbeam, meditative 8s loop.",
}

CAROUSELS = [
    C(
        "01_One_Prompt_To_Production",
        "one-prompt-to-production.pdf",
        """Your hero should not cost $5,000.

Draftly: one prompt -> AI still -> 8s video -> 400+ frames -> production HTML.

No WebGL. No Three.js. You own the ZIP.

Swipe for the full pipeline + copy-paste DeFi staking prompts.

Comment BUILD for the prompt PDF.

draftly.space

#Draftly #WebDesign #AIWebsite #3DWebsite #DeFi #StartupTools""",
        C01_DATA,
        [
            slide("01_cover.png", EDITORIAL + """
COVER STYLE: Dark cinematic Web3 product hero - NO human, NO blue sky, NO terracotta outfit.
Full-bleed deep navy-to-black gradient. Floating photoreal ETH and SOL holographic tokens
above dark glass platform, volumetric purple-blue rim light, particle bokeh, premium crypto
campaign like Coinbase product launch. Lower third white text overlay.
Headline: "One Prompt" bold white sans + "Cinematic 3D Site" white italic serif.
White pill CTA: TRY DRAFTLY FREE. Small frosted PIPELINE badge. Moody not cheerful.
"""),
            slide("02_problem.png", INTERIOR + """
Headline: your hero section should not cost five thousand dollars.
Body card: Agencies charge 2-4 weeks for scroll motion. Framer templates look like templates.
Stat card coral border: Average motion landing $3k-$15k vs Draftly from $25/mo.
"""),
            slide("03_pipeline.png", INTERIOR + """
Headline: describe - image - video - frames - html
Three cream cards stacked with coral step numbers 01-05:
01 Prompt Input | 02 Visual Draft | 03 Motion Pass | 04 Frame Extract | 05 Website Ready
Badge: 10x faster than hand-coding scroll pipelines.
"""),
            slide("04_website_prompt.png", PROMPT + """
Coral pill: STEP 01 - WEBSITE PROMPT. Headline: defi staking platform - rivr protocol.
RENDER FULL PROMPT TEXT READABLE IN CREAM CARD (3 paragraphs):
""" + C01_DATA["website_prompt"][:1200]),
            slide("05_image_prompt.png", PROMPT + """
Coral pill: STEP 02 - HERO IMAGE. Headline: cinematic web3 still - full art direction.
RENDER FULL IMAGE PROMPT (3 paragraphs) in readable monospace card:
""" + C01_DATA["image_prompt"]),
            slide("06_motion_prompts.png", PROMPT + """
Coral pill: STEPS 03-04. Headline: first frame - last frame - video motion.
Three smaller cards: FIRST FRAME, LAST FRAME, VIDEO MOTION with prompt excerpts readable.
FIRST: """ + C01_DATA["first_frame_prompt"][:200] + """
LAST: """ + C01_DATA["last_frame_prompt"][:200] + """
VIDEO: """ + C01_DATA["video_prompt"]),
            slide("07_result.png", EDITORIAL + """
Split feel: left text overlay "What ships in under an hour" white on dark gradient.
Right: realistic browser mockup of dark DeFi staking site with APY ticker and wallet CTA.
Subline: 400 frames under the hood - scroll to animate.
"""),
            slide("08_cta.png", SKY_CTA + """
Headline: "comment" white sans + "BUILD" coral highlight box + "for the full prompt pdf" white italic.
White pill: DRAFTLY.SPACE - START FREE. Recap tiny: Prompt Visual Motion Frames Ship.
"""),
        ],
    ),
    C(
        "02_47_Presets_Zero_Blank_Canvas",
        "47-presets-zero-blank-canvas.pdf",
        """Blank canvas kills conversion.

Draftly has 47 production-ready presets - Mindloop, Equilibrium, Jack 3D Creator, Rivr DeFi.

Click to edit. Chat to customize. Publish to your domain.

Comment PRESET for the top 10 preset guide PDF.

draftly.space/presets

#Draftly #WebDesign #SaaS #AgencyLife #LandingPage""",
        C02_DATA,
        [
            slide("01_cover.png", EDITORIAL + """
COVER STYLE: Warm overhead flat-lay on white marble desk - NO sky, NO portrait model.
MacBook open showing colorful website preset gallery grid on screen (multiple mini site
thumbnails). Ceramic coffee cup, coral pen, linen napkin corner. Soft morning window light
from left, lifestyle Pinterest-meets-Awwwards aesthetic. Text overlay bottom on subtle
dark gradient strip for readability.
Headline: "47 Presets" bold black + "Zero Blank Canvas" coral italic serif.
White pill: BROWSE PRESETS FREE. Badge TEMPLATE GALLERY coral outline.
"""),
            slide("02_two_paths.png", INTERIOR + """
Headline: two paths - one platform.
Split table cards: 3D Builder = from scratch | Presets = production-ready.
Same ship flow: Customize - Ship - Publish.
"""),
            slide("03_gallery.png", INTERIOR + """
Headline: website presets - beta gallery
Five preset name cards: Mindloop | Equilibrium | Jack 3D Creator | Rivr DeFi | Brandly Agency
Body: 47 live presets - click to edit copy in minutes.
"""),
            slide("04_website_prompt.png", PROMPT + """
Coral pill: BUILD YOUR OWN. Headline: axion studio agency prompt.
FULL WEBSITE PROMPT readable:
""" + C02_DATA["website_prompt"][:1200]),
            slide("05_image_prompt.png", PROMPT + """
Coral pill: HERO IMAGE. Headline: creative agency environment still.
FULL IMAGE PROMPT readable:
""" + C02_DATA["image_prompt"]),
            slide("06_motion_prompts.png", PROMPT + """
Headline: keyframes + motion for agency reel hero.
Cards for first frame, last frame, video prompts - text readable.
VIDEO: """ + C02_DATA["video_prompt"]),
            slide("07_customize.png", INTERIOR + """
Headline: customize - ship - design
Tabs coral: Customize | Ship | Design. Tools: Add page | Text | Edit | Media | Apply changes.
Body: Pro unlocks preset AI chat. Publish to yourclient.draftly.space.
"""),
            slide("08_cta.png", SKY_CTA + """
Headline: comment PRESET for top 10 preset guide pdf.
White pill: DRAFTLY.SPACE/PRESETS.
"""),
        ],
    ),
    C(
        "03_Stop_Paying_5K_For_Hero",
        "stop-paying-5k-for-hero.pdf",
        """Agencies charge $8k for a motion hero. Draftly Pro: $60/mo.

7-day free trial. Seven full sites. ZIP export.

Swipe for plan picker + Nordhaven Analytics prompt.

Comment PRICING for ROI calculator PDF.

draftly.space/pricing

#Draftly #AgencyPricing #WebDesign #SaaS""",
        C03_DATA,
        [
            slide("01_cover.png", INTERIOR + """
COVER STYLE: Bold typographic split-screen graphic on cream grid #F4EEDE - NO photo model.
Left half: distressed red stamp graphic "AGENCY BILL $8,400" with crossed invoice lines.
Right half: clean coral card "DRAFTLY PRO $60/mo" with green checkmarks. Center torn-paper
tear effect between halves. Huge headline dominates top half of slide.
Headline: "Stop Paying" black bold sans + "$5K For A Hero" coral italic serif underline.
White pill at bottom: START FREE TRIAL. Graphic design poster feel - not photography cover.
"""),
            slide("02_agency_math.png", INTERIOR + """
Headline: agency math vs draftly math
Table: Motion designer $6k + Dev $2.4k + Revisions $2k = $8k-$15k
vs Pro $60/mo - 7 sites - 6000 credits - ZIP export.
"""),
            slide("03_plans.png", INTERIOR + """
Headline: plan picker
Cards: Basic $25 | Basic Plus $40 | Pro $60 MOST POPULAR coral | Premium $200
Badge: 7-day free trial - no credit card.
"""),
            slide("04_website_prompt.png", PROMPT + """
Coral pill: CLIENT PITCH PROMPT. Headline: nordhaven analytics saas.
FULL WEBSITE PROMPT:
""" + C03_DATA["website_prompt"][:1200]),
            slide("05_image_prompt.png", PROMPT + """
Coral pill: HERO STILL. FULL IMAGE PROMPT readable:
""" + C03_DATA["image_prompt"]),
            slide("06_motion_prompts.png", PROMPT + """
Headline: motion layer for b2b dashboard hero.
First, last, video prompt cards readable.
"""),
            slide("07_roi.png", INTERIOR + """
Headline: pro pays for itself on one client deposit
Callout: Pitch Monday - staging link Wednesday - ZIP handoff Friday.
Credit table: Image 20cr | Video 128cr | Site 600cr.
"""),
            slide("08_cta.png", SKY_M + """
Headline: comment PRICING for roi calculator pdf.
White pill: DRAFTLY.SPACE/PRICING.
"""),
        ],
    ),
    C(
        "04_No_WebGL_Just_Scroll",
        "no-webgl-just-scroll.pdf",
        """Everyone adds Three.js. Draftly extracts 400+ frames and scrubs on scroll.

No WebGL. No performance tax. Works on every phone.

Comment SCROLL for the engine deep dive PDF.

draftly.space/3d-builder

#Draftly #WebDev #ScrollAnimation #Frontend""",
        C04_DATA,
        [
            slide("01_cover.png", EDITORIAL + """
COVER STYLE: Night city neon macro - NO sky, NO woman. Close-up Black hands holding iPhone
at night, screen shows luxury car website mid-scroll with frame-scrub motion blur effect.
Neon pink and cyan city bokeh reflected on phone glass and fingernails. Blade Runner
meets Apple product shot. Dark moody background, rim light on phone edges.
Overlay lower third white text: "No WebGL" bold + "Just Scroll" italic serif.
White pill: SEE THE ENGINE. Completely different from blue-sky covers.
"""),
            slide("02_insight.png", INTERIOR + """
Headline: your video becomes a scroll experience
Body: AI video -> hundreds of frames -> visitor scroll = film scrubs. Native browser. Every device.
Badge: ZERO CODE - No Three.js at runtime.
"""),
            slide("03_frames.png", INTERIOR + """
Headline: extracting frames - 400 / 400
Settings chips: 10-40 FPS | 36-2000 frames | FFmpeg WASM client-side.
Body: No GPU tax. No mobile jank.
"""),
            slide("04_website_prompt.png", PROMPT + """
Coral pill: LUXURY EV PROMPT. Headline: silence amplified - full site brief.
FULL WEBSITE PROMPT:
""" + C04_DATA["website_prompt"][:1200]),
            slide("05_image_prompt.png", PROMPT + """
Coral pill: AUTOMOTIVE HERO. FULL IMAGE PROMPT:
""" + C04_DATA["image_prompt"]),
            slide("06_motion_prompts.png", PROMPT + """
Headline: first / last frame control for drive sequence.
FIRST LAST VIDEO prompts in three readable cards.
"""),
            slide("07_export.png", INTERIOR + """
Headline: zip ready to deploy
Code card: index.html | styles.css | scroll.js | /frames/*.webp
Body: Semantic HTML + Tailwind. Vercel Netlify S3 anywhere.
"""),
            slide("08_cta.png", SKY_CTA + """
Headline: comment SCROLL for engine deep dive pdf.
White pill: DRAFTLY.SPACE/3D-BUILDER. Terracotta outfit model silhouette optional.
"""),
        ],
    ),
    C(
        "05_Agency_Pitch_20_Minutes",
        "agency-pitch-20-minutes.pdf",
        """Agencies lose deals waiting 2 weeks for a motion mockup.

Draftly: pick preset -> inject assets -> chat edit -> staging link in 20 minutes.

Comment AGENCY for the 20-min playbook PDF.

draftly.space/presets

#Draftly #AgencyLife #FreelanceDesign #ClientWork""",
        C05_DATA,
        [
            slide("01_cover.png", EDITORIAL + """
COVER STYLE: Modern glass conference room at dusk - NOT blue sky low-angle terracotta.
South Asian woman creative director age 32, navy structured blazer, standing beside large
monitor showing client website preview to two blurred colleagues seated. City skyline
golden hour through floor-to-ceiling windows, warm interior tungsten mixed with cool dusk.
Documentary corporate photography - NOT fashion sky editorial.
Headline overlay white on dark lower band: "Pitch The Client" sans + "In 20 Minutes" italic.
White pill: AGENCY PLAYBOOK.
"""),
            slide("02_old_vs_new.png", INTERIOR + """
Headline: old workflow vs draftly workflow
OLD: Day 1-14 moodboard figma webflow revisions.
NEW: Min 0-5 preset | 5-12 customize | 12-18 staging | 18-20 send link.
"""),
            slide("03_preset_picker.png", INTERIOR + """
Headline: match vertical in 60 seconds
Map cards: SaaS Mindloop | Wellness Equilibrium | DeFi Rivr | Agency Brandly | Real estate Zenith.
"""),
            slide("04_website_prompt.png", PROMPT + """
Coral pill: CLIENT-READY. Headline: equilibrium wellness studio.
FULL WEBSITE PROMPT:
""" + C05_DATA["website_prompt"][:1200]),
            slide("05_image_prompt.png", PROMPT + """
Coral pill: HERO STILL. FULL IMAGE PROMPT:
""" + C05_DATA["image_prompt"]),
            slide("06_motion_prompts.png", PROMPT + """
Headline: studio atmosphere motion layer.
Video and keyframe prompts readable.
"""),
            slide("07_ship.png", INTERIOR + """
Headline: publish staging - export zip
UI labels: Publish | yourclient.draftly.space
Email script card: Preview live here. ZIP on approval. 2 revision rounds included.
"""),
            slide("08_cta.png", SKY_CTA + """
Headline: comment AGENCY for 20-min playbook pdf.
White pill: PRO $60/MO - ONE CLIENT PAYS FOR IT.
"""),
        ],
    ),
]

CAROUSEL_MAP = {f"{i:02d}": CAROUSELS[i - 1] for i in range(1, len(CAROUSELS) + 1)}
