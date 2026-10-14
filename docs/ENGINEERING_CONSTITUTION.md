# Engineering constitution

These are company-wide defaults for humans and agents. Apply controls proportionate to data sensitivity, failure impact and system maturity. A document is guidance; enforcement requires repository checks, review and operational ownership.

## 1. Architecture

Begin with the simplest deployable design that meets the product's constraints. Prefer a modular single application over distributed services until independent scaling, ownership or isolation warrants separation. Define module boundaries, data ownership, external dependencies and contracts. Document consequential tradeoffs in an ADR, including alternatives and reversal cost.

Validate inputs at trust boundaries. Keep authorization in every server entry point. Design retries, concurrency and state transitions explicitly; require idempotency for retried mutations. Use migrations compatible with rolling deployment and a tested recovery path.

## 2. Code quality

Use the language's strict checks and formatter where practical. Keep functions cohesive, errors actionable and public interfaces explicit. Avoid speculative abstractions, dead code and duplicate sources of truth. Pin reproducible dependencies and runtime versions; commit lockfiles. Do not bypass type checking, linting or framework checks to make a build appear successful.

Comments explain constraints and non-obvious decisions; documentation describes behavior. Follow the actual framework version's current official guidance and local instructions.

## 3. Testing and evidence

Test critical behavior, boundaries and failure modes rather than mirroring implementation. Use unit checks for isolated logic, integration checks for real contracts and focused end-to-end tests for critical user journeys. Include ownership, invalid input, concurrency, retries and recovery when relevant.

Fixtures must be isolated, synthetic and safe to delete. Never run destructive tests against customer data. Record commands, environment, result, date and scope in PROJECT.md. Report skipped or unverified provider/device behavior explicitly. A mocked test does not prove a live integration; a passing build does not prove user acceptance.

## 4. Security and privacy

Use least privilege, server-side authorization and secure defaults. Keep secrets outside source control and browser bundles. Do not log credentials, raw sensitive payloads or private conversations. Minimize collection, define retention and deletion, encrypt transport and use platform storage protections.

Assess threats at meaningful trust boundaries. Limit request sizes, resource consumption and abuse. Review dependency provenance and vulnerabilities. Pin third-party actions to full commits, reduce CI token permissions and keep untrusted pull requests away from secrets and privileged runners. Never execute untrusted code using pull_request_target.

Maintain a private reporting route and an incident response owner. Do not promise a response SLA until staffing and process support it.

## 5. Documentation and planning

Each product keeps a README, root AGENTS.md and PROJECT.md current. PROJECT.md defines purpose, users, validated problem and evidence, scope/non-goals, success criteria, architecture links, current state, prioritized roadmap, next tasks, blockers and executed checks.

Record important architecture decisions, local setup, external prerequisites and operational recovery. Distinguish proposal from accepted requirement. Keep restricted business or customer evidence in appropriate private systems; public documents use sanitized summaries.

## 6. Delivery and deployment

Build reproducibly and validate the exact revision being released. Review changes before production. Deploy small increments with a rollback or roll-forward plan, compatible migrations and smoke checks. Manage environments separately. Store credentials in appropriate secret stores and prefer short-lived identity where supported.

CI never deploys by default. Production changes require applicable owner authorization, an explicit environment and evidence. A provider's ready status is not a substitute for post-release verification. Do not enable paid services without authorization.

## 7. Maintainability and operations

Assign ownership for releases, incidents and dependencies. Define health checks, safe logs and useful monitoring before a service is production-ready. Establish product-specific availability, latency, recovery and cost objectives rather than inventing universal thresholds.

Test backups and restores when persistent data matters. Document failure modes, runbooks, retention and decommissioning. Review cost and performance with measurements; optimize measured bottlenecks. Remove obsolete dependencies and document accepted debt.

## 8. Applied AI

Treat prompts, retrieved content and tool output as untrusted input. Restrict tool access and data scope. Evaluate task accuracy and failure rates on representative, rights-cleared examples; compare to a simpler baseline. Bound cost, latency and resource use. Provide fallbacks or human review according to consequence. Never claim grounded, deterministic or fully autonomous behavior without appropriate evidence.

## 9. Production readiness

Before release, apply [the readiness checklist](PRODUCTION_READINESS.md). Unsupported gates block a production-ready claim or require a documented, authorized exception. Prototype, internal pilot and production releases may have different gates, but their labels must match the evidence.

## 10. Change and exceptions

Propose standard changes in a pull request with the problem, tradeoff and adoption impact. Product-specific deviations belong in that product's ADRs and exception ledger. Each exception includes owner, affected scope, risk, compensating control, review date and exit condition. Never use an exception to disguise a failing build or silently weaken security.
