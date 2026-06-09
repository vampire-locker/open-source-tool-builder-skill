#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "open-source-tool-builder"
SKILL_MD = SKILL / "SKILL.md"
OPENAI_YAML = SKILL / "agents" / "openai.yaml"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        fail("SKILL.md frontmatter must be closed with ---")
    block = text[4:end]
    data: dict[str, str] = {}
    for line in block.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def main() -> None:
    if not SKILL_MD.exists():
        fail("missing open-source-tool-builder/SKILL.md")
    if not OPENAI_YAML.exists():
        fail("missing open-source-tool-builder/agents/openai.yaml")

    text = SKILL_MD.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(text)

    if frontmatter.get("name") != "open-source-tool-builder":
        fail("frontmatter name must be open-source-tool-builder")
    description = frontmatter.get("description", "")
    if len(description) < 80 or "[TODO" in description or "TODO:" in description:
        fail("frontmatter description must be complete and trigger-friendly")
    if "[TODO" in text or "TODO:" in text or "yourname" in text:
        fail("SKILL.md contains placeholder text")

    yaml_text = OPENAI_YAML.read_text(encoding="utf-8")
    required = [
        'display_name: "Open Source Tool Builder"',
        'short_description: "Create polished open-source tool projects"',
        'default_prompt: "Use $open-source-tool-builder',
    ]
    for value in required:
        if value not in yaml_text:
            fail(f"agents/openai.yaml missing {value}")

    reference_files = list((SKILL / "references").glob("*.md"))
    if len(reference_files) < 3:
        fail("expected multiple reference markdown files")
    for ref_path in reference_files:
        content = ref_path.read_text(encoding="utf-8")
        if "[TODO" in content or "TODO:" in content or "yourname" in content:
            fail(f"{ref_path.name} contains placeholder text")

    if not re.search(r"## Core Workflow", text):
        fail("SKILL.md should include the core workflow section")

    print("Skill validation passed")


if __name__ == "__main__":
    main()
