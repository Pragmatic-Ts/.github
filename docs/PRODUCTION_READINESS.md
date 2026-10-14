# Production readiness

Complete against the exact release revision. Each gate records owner, evidence/date, status (passed, failed, blocked or justified not applicable) and any authorized exception. A tick without evidence is insufficient.

- Product users, validated problem, scope, non-goals and measurable success criteria accepted.
- Critical user journeys and accessibility checked on supported environments.
- Types/static analysis, meaningful tests and reproducible production build executed.
- Real external integration acceptance distinguished from mocked or fixture checks.
- Authorization and isolation verified at every exposed server boundary.
- Input/resource limits, retry/concurrency/idempotency and error recovery verified.
- Dependencies reviewed; known vulnerabilities resolved or explicitly assessed.
- Secrets excluded from source, logs, artifacts and client bundles.
- Data collection, ownership, retention/deletion and privacy requirements documented.
- AI-specific evaluation, prompt/tool boundaries, cost caps and fallback assessed when applicable.
- Environment configuration and migration compatibility verified.
- Release owner, rollout, smoke checks, rollback/roll-forward and recovery documented.
- Useful health checks/monitoring, incident route and support owner established.
- Backup and restore exercised for important persistent data.
- Product-specific availability, latency, cost and recovery objectives documented.
- Legal/licensing/data-use obligations and required approvals resolved.
- Deployment evidence and remaining live/device acceptance recorded after release.

Do not convert a prototype into a production-ready claim by weakening gates. Prefer fixing gaps; document risk, owner, controls, review date and exit criteria for accepted exceptions.
