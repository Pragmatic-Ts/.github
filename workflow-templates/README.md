# Workflow templates

GitHub offers these templates to organization repositories through Actions setup. Files here do not run until adopted under a product's .github/workflows directory.

- **Node.js product CI:** npm-based single-root products with package-lock.json and required lint, typecheck, test:ci and build scripts. Missing scripts fail; commands do not use --if-present. Adapt for monorepos or other package managers before adoption. Runtime comes from .node-version.
- **Product planning validation:** checks required planning headings using a script copied from templates/product. It validates document structure, not truth, product viability or production readiness.

Each .yml has matching .properties.json metadata. GitHub replaces $default-branch on adoption. Official actions are pinned to verified v6 release commits. Dependency updates need review; products must maintain their own action pins and package dependencies.

Both templates use read-only tokens, bounded runtime, PR/push triggers and no secrets or deployment. Never inject issue titles or other untrusted text directly into shell commands. Untrusted contributions should run on hosted isolated runners, never a privileged internal runner.

The foundation's own workflow validates files and runs fixture regressions. Product CI execution requires a real product and its commands; syntax validation here does not establish product test success.
