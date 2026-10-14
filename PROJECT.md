# Organization foundation — contract and ledger

## Accepted scope

Set up Pragmatic-Ts's public .github repository, professional profile, company principles, engineering constitution, agent instructions, reusable product planning kit, issue/PR templates and opt-in CI. Verify published files and workflow syntax. Preserve all existing product repositories. No paid services, private information or invented product requirements.

Positioning: product-focused software engineering for intelligent business infrastructure. Mission: reliable, scalable software transforming inefficient business operations into intelligent digital systems. Focus: business SaaS, workflow automation, applied AI, developer infrastructure and selective custom engineering. Long-term strategy: globally competitive recurring-revenue software products; client engineering supports development and opportunity discovery.

## Current state

Public repository created under Pragmatic-Ts on 2026-10-14. Browser and connected account confirm organization access. Company profile updated. Foundation content prepared; final verification evidence is recorded in docs/VERIFICATION.md.

## Implementation ledger

| Task | Status | Evidence / remaining work |
| --- | --- | --- |
| Company positioning and principles | implemented_unverified | Profile saved; prepared profile README and principles. Verify public rendering after publication. |
| Engineering constitution and readiness | implemented_unverified | Architecture, quality, security, testing, documentation, delivery and operations documented. |
| Discoverable agent guidance | implemented_unverified | Root instructions plus explicit per-product adoption kit. |
| Community templates | implemented_unverified | Three issue forms, PR template and community defaults. |
| Product planning kit | implemented_unverified | Product contract, architecture, runbook, ADR/task templates and structural checker. |
| CI and workflow templates | implemented_unverified | Read-only pinned workflows; final local and hosted checks pending. |
| Publication and verification | in_progress | Publish one reviewed coherent commit, verify remote files and hosted workflow. |

## Build and verification contract

- python -m pip install PyYAML==6.0.3
- python scripts/validate_foundation.py
- node --test tests/foundation.test.mjs
- python scripts/lint_workflows.py
- Read back published files at the exact commit and inspect the hosted Foundation validation run.
- Verify organization README rendering and issue forms in the browser.

Checks validate the foundation and planning structure, not product application behavior. No deployment occurs. Preserve action pins and strict validation; do not weaken checks to pass.

## Next tasks and blockers

Finish verification and record exact results before stopping. Product-specific adoption, repository rules and production release acceptance are separate work requiring product owners and actual product requirements.

## Executed checks

See docs/VERIFICATION.md for executed commands/results and hosted evidence. Planned commands above are not passed claims.

## Checkpoint convention

Update this ledger and verification record on each change. Distinguish local checks, GitHub execution, public accessibility and limits. Keep private evidence out of this public repository.
