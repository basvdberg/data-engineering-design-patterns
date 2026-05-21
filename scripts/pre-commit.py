"""
Pre-commit hook for the Data Engineering Design Patterns project.

Tasks:
1. Refresh Markdown table of contents and project structure (scripts/update_markdown_docs.py)
2. Check naming conventions (kebab-case for all .md files and folders)
3. Validate generated Markdown markers
4. Update prompts.md from agent transcripts

Usage:
    python scripts/pre-commit.py
"""

import os
import re
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

EXCLUDED_FILES = {"prompts.md"}
LOCAL_TOC_EXEMPT = {"readme.md"}  # root readme has no content sections
EXCLUDED_DIRS = {".git", "scripts", "node_modules", ".cursor"}

TOC_START = "<!-- markdown-toc:start -->"
TOC_END = "<!-- markdown-toc:end -->"
STRUCT_START = "<!-- markdown-project-structure:start -->"
STRUCT_END = "<!-- markdown-project-structure:end -->"

KEBAB_CASE_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def get_markdown_files():
    """Return all .md files in the project, excluding special directories."""
    files = []
    for path in PROJECT_ROOT.rglob("*.md"):
        rel = path.relative_to(PROJECT_ROOT)
        if any(part in EXCLUDED_DIRS for part in rel.parts):
            continue
        files.append(path)
    return sorted(files)


def get_content_files():
    """Return markdown files that should have TOC structure (excludes prompts.md)."""
    return [f for f in get_markdown_files() if f.name not in EXCLUDED_FILES]


# --- Task 1: Check naming conventions ---

def check_naming_conventions():
    """Validate that all markdown files and folders use kebab-case."""
    errors = []

    for path in get_markdown_files():
        rel = path.relative_to(PROJECT_ROOT)

        stem = path.stem
        if stem != "readme" and not KEBAB_CASE_PATTERN.match(stem):
            errors.append(f"  File does not follow kebab-case: {rel}")

        for part in rel.parent.parts:
            if not KEBAB_CASE_PATTERN.match(part):
                errors.append(f"  Folder does not follow kebab-case: {part} (in {rel})")

    if errors:
        seen = set()
        unique_errors = []
        for e in errors:
            if e not in seen:
                seen.add(e)
                unique_errors.append(e)
        print("NAMING CONVENTION ERRORS:")
        print("\n".join(unique_errors))
    return errors


# --- Task 2: Check TOC structure ---

def check_toc_structure():
    """Ensure generated Markdown markers are present and the structure block is last."""
    errors = []

    for path in get_content_files():
        rel = path.relative_to(PROJECT_ROOT)
        content = path.read_text(encoding="utf-8")

        if TOC_START not in content or TOC_END not in content:
            errors.append(f"  Missing table of contents markers: {rel}")

        if STRUCT_START not in content or STRUCT_END not in content:
            errors.append(f"  Missing project structure markers: {rel}")

        if STRUCT_END in content:
            remaining = content.split(STRUCT_END, maxsplit=1)[-1].strip()
            if remaining:
                errors.append(f"  Project structure is not at end of file: {rel}")

        if TOC_START in content:
            lines = content.split("\n")
            title_found = False
            toc_near_title = False
            for i, line in enumerate(lines):
                if line.startswith("# "):
                    title_found = True
                    for j in range(i + 1, min(i + 20, len(lines))):
                        if TOC_START in lines[j]:
                            toc_near_title = True
                            break
                    break
            if title_found and not toc_near_title:
                errors.append(f"  Table of contents not positioned near title: {rel}")

    if errors:
        print("TOC STRUCTURE ERRORS:")
        print("\n".join(errors))
    return errors


def update_markdown_docs():
    """Run the shared Markdown documentation updater."""
    script = PROJECT_ROOT / "scripts" / "update_markdown_docs.py"
    result = subprocess.run(
        [sys.executable, str(script)],
        cwd=PROJECT_ROOT,
        check=False,
    )
    if result.returncode != 0:
        print("Failed to update Markdown documentation.", file=sys.stderr)
        sys.exit(result.returncode)


def update_prompts():
    """Update prompts.md from agent transcripts (project-scoped)."""
    script = PROJECT_ROOT / "scripts" / "update_prompts.py"
    result = subprocess.run(
        [sys.executable, str(script)],
        cwd=PROJECT_ROOT,
        check=False,
    )
    if result.returncode != 0:
        print("Failed to update prompts.md.", file=sys.stderr)
        sys.exit(result.returncode)
    return [Path("prompts.md")]


# --- Main ---

def main():
    print("Running pre-commit checks...\n")
    errors = []
    staged_updates = []

    update_markdown_docs()
    for path in get_markdown_files():
        staged_updates.append(path.relative_to(PROJECT_ROOT))

    naming_errors = check_naming_conventions()
    errors.extend(naming_errors)

    toc_errors = check_toc_structure()
    errors.extend(toc_errors)

    updated_prompts = update_prompts()
    staged_updates.extend(updated_prompts)

    if staged_updates:
        unique_updates = sorted({str(f) for f in staged_updates})
        print(f"\n{len(unique_updates)} Markdown file(s) were refreshed.")
        for rel in unique_updates:
            os.system(f'git -C "{PROJECT_ROOT}" add "{rel}"')

    if errors:
        print(f"\n{len(errors)} error(s) found. Commit aborted.")
        sys.exit(1)

    print("\nAll checks passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
