"""Validate planning structure; this is not product acceptance or truth verification."""
import argparse
import re
from pathlib import Path

REQUIRED = (
    "Purpose and users", "Validated problem", "Scope and non-goals",
    "Success criteria", "Architecture", "Current state", "Roadmap and priorities",
    "Next tasks", "Blockers and decisions", "Executed checks", "Implementation ledger",
)

def validate(root):
    errors = []
    for name in ("README.md", "AGENTS.md", "PROJECT.md", "docs/ARCHITECTURE.md", "docs/RUNBOOK.md"):
        if not (root / name).is_file():
            errors.append(f"Missing {name}")
    project = root / "PROJECT.md"
    if project.is_file():
        text = project.read_text(encoding="utf-8")
        headings = re.findall(r"^## (.+)$", text, re.MULTILINE)
        for heading in REQUIRED:
            if heading not in headings:
                errors.append(f"Missing PROJECT.md section: {heading}")
            elif headings.count(heading) > 1:
                errors.append(f"Duplicate PROJECT.md section: {heading}")
            else:
                section = re.search(r"^## " + re.escape(heading) + r"\n(.*?)(?=^## |\Z)", text, re.MULTILINE | re.DOTALL)
                if not section or not section.group(1).strip():
                    errors.append(f"Empty PROJECT.md section: {heading}")
    return errors

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args()
    errors = validate(args.root.resolve())
    for error in errors:
        print(error)
    if errors:
        raise SystemExit(1)
    print("Planning structure valid. Content and acceptance require human review.")
