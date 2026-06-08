# API Setup

## Required

```bash
cp .env.example .env
```

Edit `.env`:

```
APIYI_API_KEY=your_key_here
```

Or export in your shell:

```bash
export APIYI_API_KEY=your_key_here
```

## What happens without a key

Every `generate.py` exits with:

```
ERROR: Set APIYI_API_KEY environment variable.
```

No fallback key is shipped in this repo.

## Endpoint

- URL: `https://api.apiyi.com/v1/images/generations`
- Model: `gpt-image-2-all`
- Response: image URL or base64

Get a key from your APIYI account dashboard. Do not share keys in issues or PRs.
