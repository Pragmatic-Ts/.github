# Organization foundation — contract and ledger

## Accepted scope

Set up Pragmatic-Ts's public .github repository, professional profile, company principles, engineering constitution, agent instructions, reusable product planning kit, issue/PR templates and opt-in CI. Verify published files and workflow syntax. Preserve all existing product repositories. No paid services, private information or invented product requirements.

Positioning: product-focused software engineering for intelligent business infrastructure. Mission: reliable, scalable software transforming inefficient business operations into intelligent digital systems. Focus: business SaaS, workflow automation, applied AI, developer infrastructure and selective custom engineering. Long-term strategy: globally competitive recurring-revenue software products; client engineering supports development and opportunity discovery.

## Current state

Public repository created under Pragmatic-Ts on 2026-10-14. Browser and connected account confirm organization access. Company profile updated. All 39 foundation files published and anonymously read back exactly. Foundation validation passed on GitHub; profile and all three issue forms rendered correctly. Detailed evidence is recorded in docs/VERIFICATION.md.

## Implementation ledger

| Task | Status | Evidence / remaining work |
| --- | --- | --- |
| Company positioning and principles | verified | Company profile saved; public organization README rendered with accepted positioning. |
| Engineering constitution and readiness | verified | Published standards and readiness gates read back exactly; documentation checked. |
| Discoverable agent guidance | verified | Root AGENTS.md and product-root adoption instructions published and read back. |
| Community templates | verified | All three issue forms rendered in GitHub; PR template and community defaults published/read back. |
| Product planning kit | verified | Stack-neutral contract, architecture, runbook, ADR/task templates and checker published; regression checks passed. |
| CI and workflow templates | verified | All three workflows pass actionlint; hosted Foundation validation succeeds. Product CI remains opt-in and unexecuted against products. |
| Publication and verification | verified | Source commit 9cee609 published; all 39 files anonymously read back; hosted CI and browser verification pass. |

## Build and verification contract

- python -m pip install PyYAML==6.0.3
- python scripts/validate_foundation.py
- node --test tests/foundation.test.mjs
- python scripts/lint_workflows.py
- Read back published files at the exact commit and inspect the hosted Foundation validation run.
- Verify organization README rendering and issue forms in the browser.

Checks validate the foundation and planning structure, not product application behavior. No deployment occurs. Preserve action pins and strict validation; do not weaken checks to pass.

## Next tasks and blockers

Foundation setup is complete and checkpointed. Next authorized work would be adoption in a new product repository after its owner defines users, problem evidence, scope, architecture, roadmap and success criteria. No product is invented here. Product repository rules and production release acceptance remain separate tasks; no existing product repositories were changed.

## Executed checks

See docs/VERIFICATION.md for executed commands/results and hosted evidence. Planned commands above are not passed claims.

## Checkpoint convention

Update this ledger and verification record on each change. Distinguish local checks, GitHub execution, public accessibility and limits. Keep private evidence out of this public repository.
