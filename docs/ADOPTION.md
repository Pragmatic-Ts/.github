# Adoption guide

This setup adds only the organization .github foundation. It does not modify existing products, install a stack, enable paid services, or automatically enforce policies.

## New product repository

1. Create the repository with the intended visibility; keep private plans private.
2. Copy templates/product/ contents into its root. Replace every TODO with evidence, an owner-approved requirement, or an explicit unknown. Do not copy this foundation's PROJECT.md as a product specification.
3. Read the company principles and constitution, then define product-specific users, validated problem, scope, architecture, roadmap and success criteria.
4. Assign an accountable product/engineering owner and maintainer contact route. Make an explicit licensing decision.
5. Choose a supported stack and reproducible runtime. Implement documented setup, meaningful tests, strict/static checks and production build commands.
6. Adopt only applicable workflow templates. GitHub's Actions setup gallery exposes workflow-templates; they do not run in products automatically.
7. Run the new repository's documented commands on real source, then run its hosted CI. Record evidence before setting required check names.
8. Where available within the existing plan, configure reviewed PRs, passing checks, restricted direct writes and safe release environments. Do not purchase upgrades or change existing repository settings as part of this guide.
9. Establish private vulnerability reporting and verify the route. Assign release, incident, dependency and recovery ownership.
10. Review production readiness for each release.

## Defaults and opt-in files

Supported community health and issue/PR files may appear where a product has no local equivalents. Local issue-template configuration replaces the default group. Defaults do not become files in product clones.

AGENTS.md, PROJECT.md, architecture docs, ADRs, runbooks, licenses and CI are explicit adoption. Copy the product AGENTS.md to the repository root so agents can discover it. Agents should read root and applicable nested instructions before edits. Links to company standards help humans, but offline agents need a pinned local copy when network access is unavailable; document the source commit and review it periodically.

## Repository kits

templates/product is a reusable, stack-neutral skeleton stored in this repository. It is not a separate GitHub repository marked "Template repository." A separate stack-specific starter may be created later only with approved requirements and tested build commands. Do not mark the organization .github repository as a product starter: doing so would copy organization-specific files into products.

## Planning conventions

Use PROJECT.md as the current contract and ledger, issues for bounded work, and ADRs for consequential decisions. Prioritize P0 (security/outage/data loss), P1 (accepted critical path), P2 (quality/efficiency) and P3 (exploration). A priority is an owner decision, not a claim of urgency.

A task records problem, acceptance criteria, dependencies, owner, risk, verification and next action. Ledger statuses: proposed, ready, in_progress, implemented_unverified, verified, blocked, deferred. Verified requires executed evidence of the stated scope. Roadmap changes preserve the accepted scope and explain tradeoffs.

## Security and automation

Review new-repository settings before production. CODEOWNERS requires real authorized handles/teams; do not insert fictional teams. CI examples use hosted Linux runners, read-only tokens, no secrets and no deployment. Assess the organization's current Actions allowance before broader rollout; no paid feature is needed for this foundation.
