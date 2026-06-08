# Pipeline Pattern

Every batch folder follows the same three-file pattern.

## 1. content.py

Defines carousels as Python data:

- `slug` — output folder name
- `caption` — Instagram caption (written to `caption.txt`)
- `slides` — list of `(filename, prompt)` tuples

Prompts are long natural-language image generation instructions. No images stored in git.

## 2. generate.py

```bash
export APIYI_API_KEY=your_key
python3 generate.py          # all carousels in folder
python3 generate.py 01       # one carousel by id
python3 generate.py --force  # regenerate existing
```

- Calls `api.apiyi.com` with model `gpt-image-2-all`
- Skips files already on disk (>50KB) unless `--force`
- Writes `caption.txt` per carousel folder

## 3. build_pdfs.py

```bash
python3 build_pdfs.py
```

- Reads content from `content.py` or `pdf_guides.py`
- Outputs `*.pdf` lead magnets (gitignored)
- Uses `pdf_builder_rich.py` or `pdf_builder_gemini.py`

## Output structure

```
Draftly_3D_Free/
  content.py
  generate.py
  01_3D_Websites_Free/
    caption.txt
    01_cover.png      # generated locally
    02_how_it_works.png
    03_prompts_and_chat.png
```

## Adding a new carousel

1. Copy an existing `content.py` block
2. Write slide prompts following `reference-one/draftly-carousel-style.md` or `piyush-style.md`
3. Run `generate.py` then `build_pdfs.py`
4. Post with `caption.txt` content
