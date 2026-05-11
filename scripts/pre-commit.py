"""
Pre-commit hook for the Data Engineering Design Patterns project.

Tasks:
1. Check naming conventions (kebab-case for all .md files and folders)
2. Ensure every markdown file starts with a local TOC and ends with a project TOC
3. Update the project table of contents in all markdown files
4. Update prompts.md from agent transcripts

Usage:
    python scripts/pre-commit.py
"""

import json
import os
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
TRANSCRIPTS_DIR = Path.home() / ".cursor" / "projects" / "c-Dev2-Data-Engineering-2-0" / "agent-transcripts"

EXCLUDED_FILES = {"prompts.md"}
LOCAL_TOC_EXEMPT = {"readme.md"}  # root readme has no content sections
EXCLUDED_DIRS = {".git", "scripts", "node_modules", ".cursor"}

TOC_START = "<!-- toc:start -->"
TOC_END = "<!-- toc:end -->"
PROJECT_TOC_START = "<!-- project-toc:start -->"
PROJECT_TOC_END = "<!-- project-toc:end -->"

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
    """Ensure every content markdown file has local TOC at start and project TOC at end."""
    errors = []

    for path in get_content_files():
        rel = path.relative_to(PROJECT_ROOT)
        content = path.read_text(encoding="utf-8")

        is_local_toc_exempt = (
            rel == Path("readme.md") or
            (rel.name in LOCAL_TOC_EXEMPT and rel.parent == Path("."))
        )

        if not is_local_toc_exempt:
            if TOC_START not in content or TOC_END not in content:
                errors.append(f"  Missing local table of contents: {rel}")

        if PROJECT_TOC_START not in content or PROJECT_TOC_END not in content:
            errors.append(f"  Missing project table of contents: {rel}")

        if not is_local_toc_exempt and TOC_START in content:
            lines = content.split("\n")
            toc_line = None
            title_found = False
            for i, line in enumerate(lines):
                if line.startswith("# "):
                    title_found = True
                    for j in range(i + 1, min(i + 20, len(lines))):
                        if TOC_START in lines[j]:
                            toc_line = j
                            break
                    break
            if title_found and toc_line is None:
                errors.append(f"  Local TOC not positioned near title (within 20 lines): {rel}")

        if PROJECT_TOC_START in content:
            lines = content.split("\n")
            toc_idx = None
            for i, line in enumerate(lines):
                if PROJECT_TOC_START in line:
                    toc_idx = i
            end_idx = None
            for i, line in enumerate(lines):
                if PROJECT_TOC_END in line:
                    end_idx = i
            if end_idx is not None:
                remaining = "\n".join(lines[end_idx + 1:]).strip()
                if remaining:
                    errors.append(f"  Project TOC is not at end of file: {rel}")

    if errors:
        print("TOC STRUCTURE ERRORS:")
        print("\n".join(errors))
    return errors


# --- Task 3: Update project table of contents ---

def build_project_toc_tree():
    """Build the project TOC tree from the file system."""
    definitions = []
    design_patterns = []
    implementation = {}

    for path in sorted(PROJECT_ROOT.glob("definitions/*.md")):
        if path.name == "readme.md":
            continue
        title = extract_title(path)
        definitions.append((title, path))

    for path in sorted(PROJECT_ROOT.glob("design-patterns/*.md")):
        if path.name == "readme.md":
            continue
        title = extract_title(path)
        design_patterns.append((title, path))

    impl_dir = PROJECT_ROOT / "implementation"
    if impl_dir.exists():
        for sub in sorted(impl_dir.iterdir()):
            if sub.is_dir() and sub.name not in EXCLUDED_DIRS:
                impl_files = []
                for path in sorted(sub.glob("*.md")):
                    if path.name == "readme.md":
                        continue
                    title = extract_title(path)
                    impl_files.append((title, path))
                if impl_files:
                    section_title = sub.name.replace("-", " ").capitalize()
                    implementation[section_title] = impl_files

    return definitions, design_patterns, implementation


def extract_title(path):
    """Extract the H1 title from a markdown file."""
    content = path.read_text(encoding="utf-8")
    for line in content.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").capitalize()


def generate_project_toc(from_file, definitions, design_patterns, implementation):
    """Generate project TOC content with paths relative to from_file."""
    lines = []
    from_dir = from_file.parent

    root_readme = PROJECT_ROOT / "readme.md"
    rel_root = os.path.relpath(root_readme, from_dir).replace("\\", "/")
    lines.append(f"- [Data Engineering Design Patterns]({rel_root})")

    if definitions:
        lines.append("  - Definitions")
        for title, path in definitions:
            rel = os.path.relpath(path, from_dir).replace("\\", "/")
            lines.append(f"    - [{title}]({rel})")

    if design_patterns:
        lines.append("  - Design patterns")
        for title, path in design_patterns:
            rel = os.path.relpath(path, from_dir).replace("\\", "/")
            lines.append(f"    - [{title}]({rel})")

    if implementation:
        lines.append("  - Implementation")
        for section_title, files in implementation.items():
            lines.append(f"    - {section_title}")
            for title, path in files:
                rel = os.path.relpath(path, from_dir).replace("\\", "/")
                lines.append(f"      - [{title}]({rel})")

    return "\n".join(lines)


def update_project_toc():
    """Update the project TOC in all content markdown files."""
    definitions, design_patterns, implementation = build_project_toc_tree()
    updated_files = []

    for path in get_content_files():
        content = path.read_text(encoding="utf-8")
        if PROJECT_TOC_START not in content:
            continue

        new_toc = generate_project_toc(path, definitions, design_patterns, implementation)
        new_block = f"{PROJECT_TOC_START}\n{new_toc}\n{PROJECT_TOC_END}"

        pattern = re.compile(
            re.escape(PROJECT_TOC_START) + r".*?" + re.escape(PROJECT_TOC_END),
            re.DOTALL,
        )
        new_content = pattern.sub(new_block, content)

        if new_content != content:
            path.write_text(new_content, encoding="utf-8")
            updated_files.append(path.relative_to(PROJECT_ROOT))

    if updated_files:
        print("UPDATED PROJECT TOC:")
        for f in updated_files:
            print(f"  {f}")
    return updated_files


# --- Task 4: Update prompts.md ---

def extract_prompts_from_transcripts():
    """Extract user prompts from agent transcript JSONL files."""
    if not TRANSCRIPTS_DIR.exists():
        return None

    sessions = []

    for session_dir in sorted(TRANSCRIPTS_DIR.iterdir()):
        if not session_dir.is_dir():
            continue
        transcript = session_dir / f"{session_dir.name}.jsonl"
        if not transcript.exists():
            continue

        prompts = []
        try:
            for line in transcript.read_text(encoding="utf-8").splitlines():
                if not line.strip():
                    continue
                entry = json.loads(line)
                if entry.get("role") != "user":
                    continue
                content = entry.get("message", {}).get("content", [])
                for block in content:
                    if block.get("type") == "text":
                        text = block["text"]
                        match = re.search(
                            r"<user_query>\s*(.*?)\s*</user_query>", text, re.DOTALL
                        )
                        if match:
                            prompt = match.group(1).strip()
                            if is_content_prompt(prompt):
                                prompts.append(prompt)
        except (json.JSONDecodeError, KeyError, UnicodeDecodeError):
            continue

        if prompts:
            sessions.append(prompts)

    return sessions


SKIP_PATTERNS = [
    re.compile(r"^(yes|no|ja|nee)$", re.IGNORECASE),
    re.compile(r"^commit", re.IGNORECASE),
    re.compile(r"^push", re.IGNORECASE),
    re.compile(r"^clone\s+http", re.IGNORECASE),
    re.compile(r"^install\s", re.IGNORECASE),
    re.compile(r"cursor\s*(plan|billing|spending|cost|usage)", re.IGNORECASE),
    re.compile(r"(left click|context menu|extension).*(cursor|ide)", re.IGNORECASE),
    re.compile(r"^(how can I|add an item|can you add).*(cursor|ide|menu)", re.IGNORECASE),
    re.compile(r"(preview|open).*(markdown|default)", re.IGNORECASE),
    re.compile(r"^Store all prompts", re.IGNORECASE),
    re.compile(r"^Create pre-commit", re.IGNORECASE),
    re.compile(r"(key|keybind|shortcut).*(Edit Markdown|assign)", re.IGNORECASE),
    re.compile(r"I mean.*(cursor|ide|extension|context menu)", re.IGNORECASE),
    re.compile(r"(dashboard|visuali[sz]e).*(cursor|usage|cost)", re.IGNORECASE),
    re.compile(r"(monthly|plan limit|tokens used|csv)", re.IGNORECASE),
    re.compile(r"(image generation|model.*runtime)", re.IGNORECASE),
    re.compile(r"(disabled by default|expensive)", re.IGNORECASE),
    re.compile(r"^Rename the repo", re.IGNORECASE),
    re.compile(r"^I mean (the|in)", re.IGNORECASE),
    re.compile(r"percentage.*(covered|usage|max)", re.IGNORECASE),
    re.compile(r"(show me|inform me).*(usage|resources|cost)", re.IGNORECASE),
    re.compile(r"schematic picture", re.IGNORECASE),
    re.compile(r"Switch to a model", re.IGNORECASE),
    re.compile(r"7\.4M tokens", re.IGNORECASE),
    re.compile(r"dalssoft", re.IGNORECASE),
    re.compile(r"(change|find out).*(items|options).*(context menu|this menu)", re.IGNORECASE),
]


def is_content_prompt(prompt):
    """Filter out non-content prompts (git commands, IDE settings, confirmations)."""
    for pattern in SKIP_PATTERNS:
        if pattern.search(prompt):
            return False
    return len(prompt) > 5


def generate_prompts_md(sessions):
    """Generate the prompts.md content from extracted sessions."""
    lines = ["# Prompts", "", "This document contains all the prompts used to generate and refine the content in this project.", ""]

    for i, prompts in enumerate(sessions, 1):
        lines.append(f"## Session {i}")
        lines.append("")
        for j, prompt in enumerate(prompts, 1):
            lines.append(f"{j}. {prompt}")
            lines.append("")

    return "\n".join(lines)


def update_prompts():
    """Update prompts.md from agent transcripts."""
    sessions = extract_prompts_from_transcripts()
    if sessions is None:
        return []

    new_content = generate_prompts_md(sessions)
    prompts_path = PROJECT_ROOT / "prompts.md"

    if prompts_path.exists():
        current = prompts_path.read_text(encoding="utf-8")
        if current.strip() == new_content.strip():
            return []

    prompts_path.write_text(new_content, encoding="utf-8")
    print("UPDATED: prompts.md")
    return [prompts_path.relative_to(PROJECT_ROOT)]


# --- Main ---

def main():
    print("Running pre-commit checks...\n")
    errors = []
    staged_updates = []

    naming_errors = check_naming_conventions()
    errors.extend(naming_errors)

    toc_errors = check_toc_structure()
    errors.extend(toc_errors)

    updated_toc = update_project_toc()
    staged_updates.extend(updated_toc)

    updated_prompts = update_prompts()
    staged_updates.extend(updated_prompts)

    if staged_updates:
        print(f"\n{len(staged_updates)} file(s) were auto-updated and staged.")
        for f in staged_updates:
            os.system(f'git -C "{PROJECT_ROOT}" add "{f}"')

    if errors:
        print(f"\n{len(errors)} error(s) found. Commit aborted.")
        sys.exit(1)

    print("\nAll checks passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
