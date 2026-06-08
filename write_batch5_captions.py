#!/usr/bin/env python3
"""Write caption.txt for batch5 carousels."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent / "AI_Business_Carousels"

CAPTIONS = {
    "33_50_Cursor_Agent_Secrets": """Comment AI to get the full "50 Cursor Agent Secrets" PDF with code blocks, .mdc examples, hooks templates, and rollout checklists.

Most people still use Cursor like autocomplete. High-performing teams in 2026 run Cursor 3 like an operating system:
Plan Mode for architecture,
Composer 2 for fast implementation,
.cursor/rules for consistency,
hooks.json for enforcement,
/worktree for safe parallel agents,
cloud handoff for long refactors.

What this carousel covers:
Slide 1: 50 Cursor Agent Secrets Developers Hide (for business owners + developers)
Slide 2: Secrets 1-10 (Cursor 3 + Composer 2 fundamentals)
Slide 3: Secrets 11-20 (Plan Mode and anti-rework workflow)
Slide 4: Secrets 21-30 (.cursor/rules/*.mdc patterns)
Slide 5: Secrets 31-40 (hooks.json safety + auto-fix loops)
Slide 6: Secrets 41-46 (/worktree parallel agent pattern)
Slide 7: Secrets 47-50 (cloud handoff and scale)
Slide 8: Comment AI CTA

Bonus PDF: 50-cursor-agent-secrets.pdf (10+ pages)
- 50 practical secrets with examples
- .cursor/rules .mdc snippets
- hooks.json enforcement patterns
- /worktree parallel templates
- cloud-to-local handoff pattern
- troubleshooting + mastery roadmap

If you run a startup, agency, product team, or engineering org:
this is how you cut rework, reduce merge chaos, and ship faster with less babysitting.

Comment AI and I will send the complete pack.

#Cursor #CursorAI #Composer2 #CodingAgent #AIAgents #DeveloperTools #BuildInPublic #StartupTech #SaaS #ProductEngineering #Automation #VibeCoding""",
}


def fit_caption(text: str, limit: int = 2200) -> str:
    clean = text.strip()
    if len(clean) <= limit:
        return clean
    lines = []
    for line in clean.split("\n"):
        if line.startswith("Slide "):
            line = line.split("(", 1)[0].strip()
        lines.append(line)
    clean = "\n".join(lines)
    if len(clean) <= limit:
        return clean
    return clean[:limit].rsplit("\n", 1)[0]


def main() -> None:
    for slug, text in CAPTIONS.items():
        folder = ROOT / slug
        folder.mkdir(parents=True, exist_ok=True)
        caption = fit_caption(text)
        (folder / "caption.txt").write_text(caption + "\n", encoding="utf-8")
        print(f"OK  {slug}: {len(caption)} chars")


if __name__ == "__main__":
    main()
