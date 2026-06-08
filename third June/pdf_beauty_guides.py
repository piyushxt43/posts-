# -*- coding: utf-8 -*-
"""10+ page PDF content for beauty / character shoot carousels (06-12)."""

def _p(*parts):
    return "<br/><br/>".join(parts)


# --- 06 / 07 expanded (were too thin) ---

_PAGES_06 = [
    ("What this system solves", _p(
        "Generic AI portraits fail for campaigns because skin turns plastic, eyes go glassy, and every new prompt changes the face. "
        "This guide is the operator stack Visual AI Club uses: <b>lock identity first</b>, shoot macros second, export a contact sheet last.",
        "<b>Tools:</b> GPT Image (gpt-image-1), Midjourney v6 with --cref, Flux with reference, or any model that accepts a 150-250 word character block + negative list.",
        "<b>Deliverable:</b> one Instagram carousel (7 slides) + 6 ad crops from the same face.",
    )),
    ("Step 0  -  Character DNA block", _p(
        "Paste this block at the top of <b>every</b> prompt in a shoot. Edit once, never paraphrase mid-series.",
        "<pre>CHARACTER DNA (LOCKED):\nCaucasian woman, 27, fair skin, light freckles nose+cheeks,\nlight green-hazel eyes, wavy dirty-blonde hair shoulder length,\neditorial bone structure, minimal makeup, natural pores visible,\nno glamour retouch, no plastic skin, no wax smoothing.</pre>",
        "Add 2 reference adjectives only: e.g. <i>intimate editorial</i>, <i>beauty campaign</i>  -  not \"stunning gorgeous model\".",
    )),
    ("Step 1  -  Cover portrait prompt", _p(
        "<pre>Full-bleed 4:5 portrait, 85mm f/2, soft window key camera-left,\n[CHARACTER DNA], one realistic tear on cheek, finger near lower lip,\ndark soft background, hyper-real pores, PIYUSH.GLITCH top center,\nlower third white serif \"This is\" + bold italic \"AI Shoots\",\npill CTA \"GENERATE SHOOTS WITH AI\".</pre>",
        "Run 4 variations. Pick the face you will use as master reference. Upscale winner only after identity passes checklist (page 9).",
    )),
    ("Step 2  -  Typography slide", _p(
        "Layout: warm off-white #FAF8F4, headline <b>Detailed</b> (brown serif) + <b>models</b> (tan italic). "
        "Two overlapping rounded inset cards: (1) tight face crop same DNA, (2) macro eye with tear.",
        "Handwritten arrow label: <b>Hyper Realistic</b>. This slide sells the system  -  it is not another pretty face, it is proof of texture.",
    )),
    ("Eye macro  -  copy/paste", _p(
        "<pre>Extreme macro human eye, [CHARACTER DNA],\ngreen-hazel iris radial fibers, wet lower lash line,\nsingle tear bead, capillaries in sclera, mascara micro-clumps,\n100mm macro beauty dish + soft fill, Phase One sharpness,\nlabels with arrows: Realistic Eye, Realistic Tears, Realistic Eyelashes,\nno glass eye, no horror.</pre>",
    )),
    ("Skin macro  -  copy/paste", _p(
        "<pre>Macro nose bridge + upper cheeks, [CHARACTER DNA],\nvisible pores, sebum sheen, light freckles, one small mole,\npeach fuzz in sidelight, warm honest grade,\nlabels: Realistic Pores, Realistic Texture, Realistic Moles.</pre>",
    )),
    ("Lip + split texture", _p(
        "<b>Lips:</b> parted lips, natural pink, gloss lower lip, fingertip at corner  -  finger ridges visible.<br/>"
        "<b>Split frame:</b> left panel eye + tear droplet; right panel cheek freckles + water bead. "
        "Labels: Realistic Texture, Realistic shadows. Same lighting vector on both panels.",
    )),
    ("Sky hero finale", _p(
        "<pre>Low-angle 4:5 outdoors, clear blue sky + soft clouds,\n[CHARACTER DNA], side profile three-quarter,\nterracotta rust dress or top, wind in hair, 24-35mm,\n\"This is\" + \"AI Shoots\" white type, pill COMMENT SHOOTS FOR THE PDF.</pre>",
        "Sky must dominate  -  not grey studio. Match warm grade to cover for carousel continuity.",
    )),
    ("Negative prompt block (always append)", _p(
        "<pre>NEGATIVE: plastic skin, wax smoothing, beauty filter, airbrushed,\nuncanny eyes, extra fingers, warped text, CGI gloss lips,\ngeneric influencer face, over-sharpened pores, orange skin,\nlorem ipsum, watermark, slide numbers, deformed hands.</pre>",
    )),
    ("Identity QA checklist", _p(
        "Before publishing, verify:<br/>"
        "- Same eye color and freckle pattern across slides 2-6<br/>"
        "- Hair part and volume consistent<br/>"
        "- Skin undertone not drifting orange/cool between macros<br/>"
        "- Moisture looks photographic (not painted highlight blob)<br/>"
        "- Text spelling perfect on overlays<br/>"
        "- Slide 7 sky exposure not clipping skin highlights",
    )),
    ("Export sizes for Instagram", _p(
        "Master: 1080x1350 (4:5). Also export 1080x1080 center crop for feed grid.<br/>"
        "Story safe zone: keep CTA pill 120px above bottom.<br/>"
        "PDF delivery: attach build-realistic-ai-character-shoots.pdf when user comments <b>SHOOTS</b>.",
    )),
    ("7-day rollout", _p(
        "<b>Day 1:</b> Lock DNA + cover.<br/><b>Day 2:</b> Macros (eye, skin, lip).<br/><b>Day 3:</b> Split texture.<br/>"
        "<b>Day 4:</b> Typography slide.<br/><b>Day 5:</b> Sky hero.<br/><b>Day 6:</b> Caption + hashtags.<br/>"
        "<b>Day 7:</b> Reply PDF to comments. Reuse DNA for paid client work.",
    )),
]

_PAGES_07 = [
    ("Campaign deck overview", _p(
        "This companion deck proves you can run a <b>full beauty campaign</b> from one character: emotional cover, education slides, macro evidence, blue-sky closer. "
        "Comment keyword <b>BEAUTY</b> for the macro library PDF.",
    )),
    ("Build Realistic cover variant", _p(
        "Slide 1 headline stack: <b>Build Realistic</b> (sans) + <b>AI Character Shoots</b> (italic). Dark full-bleed portrait  -  same DNA as carousel 06 for grid consistency.",
    )),
    ("Moisture system", _p(
        "AI skin fails when dryness is default. Add one moisture cue per macro: tear bead, sweat trail, lip gloss, or cheek water droplet. "
        "Prompt clause: <i>natural sebum sheen, micro moisture, not airbrushed</i>.",
        "<pre>Cheek droplet macro: side-lit cheek, single clear water bead,\npores and vellus hair sharp, label Realistic Pores.</pre>",
    )),
    ("Shadow truth slide", _p(
        "Philtrum and nostril shadows separate editorial from CGI. Use <b>bright natural side light</b>  -  not flat front flash. "
        "Prompt: <i>soft shadow under nose, gradient falloff on cheek, no painted-on shadow</i>.",
    )),
    ("Macro suffix (append to all)", _p(
        "<pre>Phase One editorial macro, visible pores and peach fuzz,\nnatural moisture, no beauty filter, 4:5 vertical 1080x1350,\nPIYUSH.GLITCH top right, @piyush.glitch footer.</pre>",
    )),
    ("Tool-specific settings", _p(
        "<b>GPT Image:</b> size 1024x1536, quality high, 2-paragraph prompt.<br/>"
        "<b>Midjourney:</b> --style raw --stylize 50-120, character reference on cover.<br/>"
        "<b>Flux:</b> reference image weight 0.6-0.8, avoid high CFG on skin.<br/>"
        "Always generate 4-up, pick one face, discard rest before continuing series.",
    )),
    ("Caption structure", _p(
        "Hook: plastic skin problem. Body: 3 bullets (identity, macro, sky). CTA: Comment BEAUTY. "
        "Hashtags: #AIBeauty #Skin #AIPortraits #PromptEngineering #VisualAI",
    )),
    ("Carousel slide map", _p(
        "1 Cover Build Realistic | 2 Detailed models | 3 Eye | 4 Pores+droplet | 5 Lips | 6 Shadow texture | 7 Sky Generate/AI Shoots",
    )),
    ("Client handoff", _p(
        "Package: 7 PNGs + PDF + DNA.txt + negative.txt. "
        "Charge for <b>system</b> not single images. Upsell: 6-scene contact sheet (see carousel 12 PDF).",
    )),
    ("Quality gate", _p(
        "Reject if: symmetrical plastic skin, missing catchlights, freckles disappear in macros, or sky slide skin is blown out.",
    )),
    ("Next steps", _p(
        "Study carousels 08-12 in this folder: Identity Lock, Macro Library, Lighting, Quality Gates, Campaign Export. "
        "Each has 8 Instagram slides + 10-page PDF.",
    )),
]

_PAGES_08 = [
    ("Identity Lock System", _p(
        "The #1 campaign killer is <b>face drift</b>  -  slide 3 looks like a different person. "
        "Identity Lock means one DNA block, one master reference, and a 12-point QA before any background or outfit change.",
    )),
    ("Character DNA  -  full template", _p(
        "<pre>SUBJECT: [name optional] Caucasian woman 27\nSKIN: fair, light freckles nose+cheeks, visible pores\nEYES: green-hazel, limbal ring, natural moisture\nHAIR: dirty-blonde wavy, shoulder, left part\nFACE: oval, editorial cheekbones, minimal makeup\nNEGATIVE FACE: no plastic, no wax, no filter</pre>",
        "Store in identity-lock.txt. Version it in git when you change a client character.",
    )),
    ("Three-angle rule", _p(
        "Generate in one session:<br/>1. Front neutral, eyes to lens<br/>2. Three-quarter, soft expression<br/>3. Profile, hair tucked behind ear<br/>"
        "Lighting locked: key 45- left, fill bounce right. If angle 3 drifts, re-roll only angle 3 with same seed/reference.",
    )),
    ("Freckle + mole map", _p(
        "Document permanent marks in prose: <i>freckles dense on nose bridge, sparse on forehead, one mole 2mm left cheek</i>. "
        "Re-use exact phrase in every macro  -  models treat this as anchor detail.",
    )),
    ("Reference image workflow", _p(
        "<b>Step 1:</b> Generate cover, pick winner.<br/><b>Step 2:</b> Upload as reference (tool-native).<br/>"
        "<b>Step 3:</b> All macros use reference + DNA text.<br/><b>Step 4:</b> If drift &gt;10%, stop and fix DNA wording, don't brute-force more gens.",
    )),
    ("Seed and session discipline", _p(
        "Midjourney: note seed from hero, use --seed on variants. GPT Image: keep prompt prefix identical, change only shot clause. "
        "Never change eye color between slides to 'fix' lighting  -  fix lighting instead.",
    )),
    ("Instagram slide 2  -  what to teach", _p(
        "Cream slide headline: <b>Character DNA</b> + italic <b>copy this</b>. "
        "Show DNA card readable on mobile. This is your highest-save slide.",
    )),
    ("Instagram slide 5  -  QA card", _p(
        "Headline: <b>Same face</b> / <b>three shots</b>. Checklist card: Identity Locked  -  freckles match, eye color match, undertone match. "
        "Optional 1x3 inset row of three angles.",
    )),
    ("When to reset", _p(
        "Reset DNA if: client changes ethnicity/age, you switch models (MJ-GPT), or after 30+ gens with cumulative drift. "
        "Export new master reference before continuing campaign.",
    )),
    ("Commercial use", _p(
        "Disclose AI per platform rules. Keep DNA file for brand consistency across months. "
        "Same system works for product hands + face campaigns  -  DNA block includes hand skin tone match.",
    )),
    ("Comment CTA: IDENTITY", _p(
        "Instagram CTA: Comment <b>IDENTITY</b> for this PDF. Auto-DM the PDF link in your workflow tool.",
    )),
    ("Exercise  -  30 minutes", _p(
        "1) Write DNA (10 min). 2) Generate coverx4 (10 min). 3) Run 3-angle test (10 min). "
        "Pass = all three recognizable as same person at thumbnail size.",
    )),
]

_PAGES_09 = [
    ("Macro Prompt Library", _p(
        "Macros are your <b>proof slides</b>  -  they justify the cover portrait. "
        "This library gives copy-paste blocks for eye, skin, lips, brow, and tear systems with annotation labels for Instagram.",
    )),
    ("Eye  -  hero macro", _p(
        "<pre>SUBJECT: extreme macro left eye [DNA]\nIRIS: green-hazel fibrous detail, black pupil, catchlight 10 o'clock\nLASHES: individual strands, slight clump mascara\nMOISTURE: one tear bead lower lid\nSKIN: periorbital pores, capillaries sclera\nLIGHT: beauty dish 45- left, fill -1.5 stops\nLABELS: Realistic Eye, Realistic Tears, Realistic Eyelashes</pre>",
    )),
    ("Skin  -  pore field", _p(
        "<pre>SUBJECT: macro nose bridge + malar [DNA]\nTEXTURE: pores 0.3-1mm visible, sebum T-zone, peach fuzz\nMARKS: freckles per map, one mole left cheek\nLIGHT: raking side light 30-\nLABELS: Realistic Pores, Realistic Texture, Realistic Moles</pre>",
    )),
    ("Lips  -  interaction shot", _p(
        "<pre>SUBJECT: macro mouth [DNA]\nLIPS: parted 2mm, natural pink, lower lip gloss\nHAND: index finger touches lower lip corner, skin ridges visible\nLABELS: Realistic Lips, Realistic Features</pre>",
    )),
    ("Brow + lash line", _p(
        "<pre>SUBJECT: macro brow and upper lid [DNA]\nDETAIL: single brow hairs, skin under brow pores\nLASH: upper lash line sharp\nUse when eye slide feels too tight  -  alternate carousel slide.</pre>",
    )),
    ("Tear / sweat system", _p(
        "Specify <b>one</b> fluid element per image: tear track, sweat bead, or water splash. "
        "Multi-fluid often looks CGI. Prompt: <i>single clear droplet, surface tension highlight, not gel blob</i>.",
    )),
    ("Annotation style", _p(
        "Thin white handwritten arrows + 2-3 words max. Never cover the pupil. "
        "Brand: PIYUSH.GLITCH top right on photo slides.",
    )),
    ("Focal length guide", _p(
        "Eye/lips: 85-100mm macro equivalent. Skin field: 70-100mm. "
        "Full face cover: 85mm f/1.8-2.8. Sky hero: 24-35mm  -  do not use macro lens language on sky slide.",
    )),
    ("Batch generation order", _p(
        "Order reduces drift: Cover - Eye - Skin - Lips - Split texture - Typography (can be designed in Figma with exports) - Sky.",
    )),
    ("Slide 4  -  teach the library", _p(
        "Cream slide: headline <b>Macro</b> / <b>blocks</b>. Show eye block in monospace card  -  largest readable font. "
        "Coral tab: COPY ALL MACROS.",
    )),
    ("Common failures", _p(
        "Glass eye: add capillaries + iris fibers. Plastic skin: add pores + negative block. "
        "Lip gel: specify micro-wrinkles on lip surface.",
    )),
    ("Comment CTA: MACRO", _p(
        "Deliver this PDF when user comments <b>MACRO</b>. Pair with carousel 08 DNA file.",
    )),
]

_PAGES_10 = [
    ("Lighting & Camera for AI Beauty", _p(
        "Lighting language in prompts controls 60% of realism. "
        "This guide maps <b>key, fill, rim</b> setups to copy-paste clauses and shows which slide type each serves.",
    )),
    ("Setup A  -  Window editorial (default)", _p(
        "<pre>KEY: large soft source 45- camera-left, window quality\nFILL: white bounce camera-right, -1.5 stops\nRIM: optional narrow strip behind hair\nMOOD: intimate editorial, neutral color grade</pre>",
        "Use: cover, typography insets, 3-angle row.",
    )),
    ("Setup B  -  Raking macro", _p(
        "<pre>KEY: hard-ish side 30- for texture revelation\nFILL: minimal\nGOAL: pores, freckles, vellus hair\nAVOID: flat front beauty dish only (looks commercial fake)</pre>",
        "Use: skin, pore, shadow-truth slides.",
    )),
    ("Setup C  -  Outdoor sky hero", _p(
        "<pre>KEY: sun behind camera, blue sky fill\nCAMERA: low angle 24-35mm\nWARDROBE: terracotta or cream for sky contrast\nSKIN: keep highlight rolloff, no clipped forehead</pre>",
        "Use: slide 7/8 finale only.",
    )),
    ("Camera clause cheat sheet", _p(
        "Cover: <i>85mm f/2, shallow DOF, natural catchlights</i><br/>"
        "Macro: <i>100mm macro, f/5.6-8, sharp focal plane on iris or pores</i><br/>"
        "Sky: <i>35mm, deep DOF on face, sky saturated natural not neon</i>",
    )),
    ("Color grade tokens", _p(
        "Editorial neutral: <i>slightly desaturated, warm skin, cool shadows</i><br/>"
        "Macro honest: <i>no orange skin, preserve undertone</i><br/>"
        "Sky campaign: <i>warm skin vs cool sky separation</i>",
    )),
    ("Diagram slide for Instagram", _p(
        "Cream slide: <b>Light</b> / <b>Direction</b>. Bullets: Key 45- left, Fill bounce right, Rim hair. "
        "Simple overhead diagram circle + arrows. Inset small lit face result.",
    )),
    ("Matching macros to cover", _p(
        "If cover is window-left, macros MUST say same vector. Mismatched light = subconscious fake cue.",
    )),
    ("HDR and blowout fixes", _p(
        "Prompt: <i>retain skin highlight detail, no clipped forehead, soft highlight rolloff</i>. "
        "Regenerate sky slide if clouds are grey mush  -  specify <i>clear blue sky, soft cumulus</i>.",
    )),
    ("Studio vs location language", _p(
        "Dark soft background = studio intimacy. Blue sky = location campaign. "
        "Do not mix studio macro lighting with sky cover in same session without re-prompting light block.",
    )),
    ("10-slide lighting test", _p(
        "Generate same eye macro with Setup A vs B side by side. Pick which sells texture for your brand. Document winner in lighting.txt.",
    )),
    ("Comment CTA: LIGHT", _p(
        "Comment <b>LIGHT</b> for PDF. Cross-link Identity (08) and Macro (09) PDFs in DM.",
    )),
]

_PAGES_11 = [
    ("Quality Gates & Negative Prompts", _p(
        "Operators don't need more prompts  -  they need <b>reject criteria</b>. "
        "This gate system stops plastic skin posts before they hit your grid.",
    )),
    ("Master negative block", _p(
        "<pre>plastic skin, wax doll, beauty filter, airbrush, poreless,\nuncanny eyes, dead stare, mismatched catchlights,\nextra fingers, fused hands, warped typography,\nCGI gloss lips, painted tears, floating jewelry,\nover-sharpen halos, AI face symmetry overload,\nlow-res skin, jpeg face, watermark, lorem ipsum</pre>",
        "Append to every generation. Never shorten mid-campaign.",
    )),
    ("Pass / fail  -  thumbnail test", _p(
        "<b>PASS:</b> At 150px width, face still looks like same person; skin has texture noise.<br/>"
        "<b>FAIL:</b> Porcelain cheek, no pore noise, or eyes look like stickers.",
    )),
    ("Pass / fail  -  macro test", _p(
        "<b>PASS:</b> Iris fibers visible, moisture has highlight physics, freckles irregular.<br/>"
        "<b>FAIL:</b> Perfect radial blur iris, repeating freckle pattern, mole moves location.",
    )),
    ("Pass / fail  -  text overlay", _p(
        "<b>PASS:</b> All brand words spelled, pill CTA readable, no gibberish.<br/>"
        "<b>FAIL:</b> Warped letters  -  regenerate before adding type in Figma as backup.",
    )),
    ("Plastic skin recovery", _p(
        "Add: <i>visible pores, peach fuzz, natural sebum, editorial raw capture</i>. "
        "Reduce: glamour, flawless, porcelain, 8k beauty. Lower stylize if using Midjourney.",
    )),
    ("Eye recovery", _p(
        "Add: <i>capillaries in sclera, iris fibrous detail, asymmetric catchlights</i>. "
        "Remove: <i>glowing eyes, crystal iris, doll eyes</i>.",
    )),
    ("Instagram QC slide content", _p(
        "Cream slide headline: <b>Quality</b> / <b>gate</b>. "
        "Two columns PASS vs FAIL with 3 bullets each. Coral highlight on NEGATIVE block card.",
    )),
    ("Pre-publish checklist", _p(
        "- DNA block used on every gen<br/>- Negative block appended<br/>- Lighting vector consistent<br/>- 3-angle identity pass<br/>- Macro moisture single-type<br/>- Sky slide not clipping skin<br/>- Caption CTA keyword correct",
    )),
    ("Version control", _p(
        "Save prompts/negative-lighting-dna as v1.0 when carousel goes live. "
        "Client revision = bump version, don't edit live files silently.",
    )),
    ("Legal & disclosure", _p(
        "Many regions require clear AI labeling for ads. Add #AI or platform sticker where required. "
        "Keep generation logs for brand disputes.",
    )),
    ("Comment CTA: QUALITY", _p(
        "Comment <b>QUALITY</b> for this PDF  -  send with 08 Identity for full operator stack.",
    )),
]

_PAGES_12 = [
    ("Campaign Contact Sheet", _p(
        "One locked character should yield <b>6 deliverables</b> without reshooting: hero, macro, 3 angles, sky, and 2 crops. "
        "This is how you productize AI beauty beyond single viral slides.",
    )),
    ("Deliverable map", _p(
        "1. Hero cover 4:5<br/>2. Eye macro ad<br/>3. Skin macro ad<br/>4. 3-angle identity strip<br/>"
        "5. Sky campaign poster<br/>6. 1080x1080 feed crop<br/>Optional: Story 9:16 center-safe reframe.",
    )),
    ("Contact sheet prompt", _p(
        "<pre>Flat lay white desk, six printed 4:5 cards arranged grid,\nsame [DNA] character across all prints, soft overhead daylight,\nblack pen, sticky note handwritten \"Hero / Macro / Sky\",\neditorial art director desk, PIYUSH.GLITCH small top</pre>",
        "Generate or composite in Figma using your exports.",
    )),
    ("Scene swap without face drift", _p(
        "Change ONLY background clause after identity pass: <i>dark studio</i> - <i>blue sky</i> - <i>warm interior</i>. "
        "Never remove DNA block when swapping scene.",
    )),
    ("Caption variants per asset", _p(
        "Hero: emotional hook. Macro: educational \"pores don't lie\". Sky: campaign CTA. "
        "Same comment keyword, different first line per post in Stories highlights.",
    )),
    ("Pricing anchor", _p(
        "Sell package: 7 carousel slides + 6 exports + 3 prompt files + this PDF. "
        "Do not price per image  -  price per <b>system</b>.",
    )),
    ("Figma assembly", _p(
        "Import PNGs - 1080x1350 frames - typography on slides 2,5,8 in vectors for perfect text. "
        "Keep photo gens for faces only if text warps.",
    )),
    ("Automation outline", _p(
        "Sheet columns: slide_id, prompt, negative, lighting, status, seed, file_path. "
        "n8n/Make: comment trigger - send PDF + DNA zip from Drive.",
    )),
    ("Instagram slide  -  6-up grid", _p(
        "Cream slide: <b>Campaign</b> / <b>board</b>. Show 2x3 grid of six crops. "
        "Handwritten arrow: Ready for campaign use.",
    )),
    ("Retention loop", _p(
        "Week 2 post: behind-the-scenes DNA screenshot. Week 4: client result. "
        "Same keyword routes to updated PDF version.",
    )),
    ("Metrics", _p(
        "Track: saves per slide (expect slide 2,4 highest), comment rate, DM delivery success, "
        "cost per accepted image (total API spend / approved count).",
    )),
    ("Comment CTA: CAMPAIGN", _p(
        "Comment <b>CAMPAIGN</b> for contact sheet PDF + recommend carousels 08-11 as prerequisite reading.",
    )),
]

BEAUTY_PDF_PAGES = {
    "06_Build_Realistic_AI_Character_Shoots": _PAGES_06,
    "07_Generate_AI_Beauty_Campaigns": _PAGES_07,
    "08_Identity_Lock_Character_DNA": _PAGES_08,
    "09_Macro_Prompt_Library": _PAGES_09,
    "10_Lighting_Camera_Beauty_Setups": _PAGES_10,
    "11_Quality_Gates_Negative_Prompts": _PAGES_11,
    "12_Campaign_Contact_Sheet_Export": _PAGES_12,
}
