# Verification record

## Scope

Foundation files and workflows only. Product code, customer environments and production deployments are outside scope. Templates are starting points, not evidence that a product is validated or production-ready.

## Preparation evidence — 2026-10-14

- Browser created Pragmatic-Ts/.github as Public, initialized on main.
- Connected GitHub account confirms admin/push access.
- Official actions/checkout v6 resolves to d23441a48e516b6c34aea4fa41551a30e30af803; actions/setup-node v6 resolves to 249970729cb0ef3589644e2896645e5dc5ba9c38 via official repository tag reads.
- actionlint 1.7.12 archive hashes obtained from the official release API. The validator checks archive SHA-256 before executing the selected binary.
- GitHub profile save visibly confirmed. Public README rendering verification follows publication.

## Final checks

Executed on Windows, Python 3.14.4 / PyYAML 6.0.3 / Node.js 24.13.0:
- python scripts/validate_foundation.py — passed: required files, relative document links, issue-form structure, workflow metadata and safety conventions.
- node --test tests/foundation.test.mjs — all nine regressions passed, including missing/empty/duplicate planning sections, missing AGENTS.md, broken links, duplicate issue IDs, unpinned actions and missing active CI.
- python scripts/lint_workflows.py — passed: actionlint 1.7.12 validated one active workflow and two templates after replacing GitHub's default-branch placeholder. ShellCheck and Pyflakes are not part of this check.
- Product applications and deployment were not tested. Hosted execution and public readback follow publication.

## Limits

GitHub community defaults do not copy files into product clones or enforce engineering standards. Local agent instructions and product workflows require explicit adoption. Planning validation checks document structure, not requirement accuracy. Node.js CI requires real product scripts and a committed lockfile/runtime configuration. No product tests or live integration acceptance are claimed.

Private security reporting must be enabled and verified per product before production. No invented contact address, support SLA, license, customer, revenue result or product requirement is published.

## Published evidence — 2026-10-14

- Source commit: [9cee6096824fd8048b046bb3c80eda7d6526456f](https://github.com/Pragmatic-Ts/.github/commit/9cee6096824fd8048b046bb3c80eda7d6526456f).
- Anonymous HTTPS clone and exact-content comparison verified all 39 tracked files, including all standards, templates, workflows, scripts and tests.
- [Foundation validation run 38575681221](https://github.com/Pragmatic-Ts/.github/actions/runs/38575681221) completed successfully for that source revision. The workflow executed the structure/link/form checks, nine regression tests and actionlint.
- Browser verified the public organization description and rendered profile README, issue chooser, and actual bug/task/proposal forms with their required fields.
- Company profile display name is Pragmatic-Ts. No contact details, website, location or business achievements were invented.
- The two workflow templates are opt-in starting points, not auto-installed product CI. No product application tests were executed or claimed.
- No existing product repository was edited, deleted or reconfigured; no paid service was enabled.

This final documentation checkpoint records observed source-run evidence. Documentation-only revisions still trigger the same validation workflow; inspect the latest run before adopting changes.
