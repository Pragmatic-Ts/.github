"""Validate organization files, local links, forms and workflow safety conventions."""
import importlib.util
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote
import yaml

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md", "profile/README.md", "AGENTS.md", "PROJECT.md", "CONTRIBUTING.md",
    "SECURITY.md", "SUPPORT.md", "CODE_OF_CONDUCT.md",
    "docs/COMPANY_PRINCIPLES.md", "docs/ENGINEERING_CONSTITUTION.md",
    "docs/PRODUCT_EVALUATION.md", "docs/ADOPTION.md", "docs/PRODUCTION_READINESS.md",
    "docs/VERIFICATION.md", ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/workflows/foundation.yml", ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/product_proposal.yml", ".github/ISSUE_TEMPLATE/engineering_task.yml",
    ".github/ISSUE_TEMPLATE/config.yml", "workflow-templates/node-product-ci.yml",
    "workflow-templates/product-planning.yml",
)
PIN = re.compile(r"^[^\s@]+/[^\s@]+@[0-9a-f]{40}$")

def validate(root):
    errors = []
    for name in REQUIRED:
        if not (root / name).is_file():
            errors.append(f"Missing {name}")
    for path in sorted(root.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        if not text.strip():
            errors.append(f"Empty document: {path.relative_to(root)}")
        for link in re.findall(r"(?<!!)\[[^\]]*\]\(([^)]+)\)", text):
            if re.match(r"^(https?://|mailto:|#)", link):
                continue
            target = path.parent / unquote(link.split("#")[0])
            if not target.exists():
                errors.append(f"Broken local link in {path.relative_to(root)}: {link}")
    forms = sorted((root / ".github/ISSUE_TEMPLATE").glob("*.yml"))
    for path in forms:
        try:
            form = yaml.safe_load(path.read_text(encoding="utf-8"))
            if path.name == "config.yml":
                if not isinstance(form.get("blank_issues_enabled"), bool):
                    errors.append("Issue config needs boolean blank_issues_enabled")
                continue
            if not form.get("name") or not form.get("description") or not form.get("body"):
                errors.append(f"Incomplete issue form: {path.name}")
            ids = []
            for item in form.get("body", []):
                if item.get("type") not in ("markdown", "input", "textarea", "dropdown", "checkboxes"):
                    errors.append(f"Invalid issue field type: {path.name}")
                if item.get("type") != "markdown":
                    ids.append(item.get("id"))
                    if not item.get("attributes", {}).get("label"):
                        errors.append(f"Unlabelled issue field: {path.name}")
            if None in ids or len(ids) != len(set(ids)):
                errors.append(f"Missing or duplicate issue field IDs: {path.name}")
        except (yaml.YAMLError, AttributeError, TypeError) as error:
            errors.append(f"Invalid issue YAML: {path.name}: {error}")
    workflows = list((root / ".github/workflows").glob("*.yml")) + list((root / "workflow-templates").glob("*.yml"))
    for path in workflows:
        try:
            text = path.read_text(encoding="utf-8")
            # BaseLoader preserves "on" rather than YAML 1.1 coercing it to True.
            workflow = yaml.load(text, Loader=yaml.BaseLoader)
            if workflow.get("permissions") != {"contents": "read"}:
                errors.append(f"Workflow requires read-only permissions: {path.name}")
            if "pull_request_target" in workflow.get("on", {}):
                errors.append(f"Privileged PR trigger prohibited: {path.name}")
            for job in workflow.get("jobs", {}).values():
                if not job.get("timeout-minutes"):
                    errors.append(f"Missing workflow timeout: {path.name}")
                for step in job.get("steps", []):
                    if "uses" in step and not PIN.fullmatch(step["uses"]):
                        errors.append(f"Unpinned external action: {path.name}")
            if path.parent.name == "workflow-templates":
                metadata_path = path.with_suffix(".properties.json")
                metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
                if not metadata.get("name") or not metadata.get("description"):
                    errors.append(f"Incomplete workflow metadata: {path.name}")
        except (yaml.YAMLError, OSError, ValueError, AttributeError, TypeError) as error:
            errors.append(f"Invalid workflow: {path.name}: {error}")
    spec = importlib.util.spec_from_file_location("planning", root / "templates/product/scripts/validate_project.py")
    if spec and spec.loader:
        planning = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(planning)
        errors.extend(planning.validate(root / "templates/product"))
    return errors

if __name__ == "__main__":
    errors = validate(ROOT)
    for error in errors:
        print(error)
    if errors:
        sys.exit(1)
    print("Foundation structure, local links, issue forms, metadata and workflow safety checks valid.")
