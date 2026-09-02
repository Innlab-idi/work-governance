# Future Governance Synchronization

Status: informative  
Scope: organization

No synchronization tooling is implemented in this repository. This document
records the intended contract so automation can be designed later without
weakening local ownership or Git auditability.

As a public baseline, `work-governance` can be read without credentials for a
private sibling repository. Public read access does not grant the authorization
required for future write operations on private consumers, such as creating
branches or pull requests.

## Target flow

```text
change in work-governance
-> render/copy managed governance block
-> consumer AGENTS.md
-> reviewable Git diff / PR
-> review
-> merge
```

The rendered block contains the operational rules an agent needs, so the
consumer remains usable without access to `work-governance`. It is a projection,
not a second canonical source. `Source: work-governance` records its origin and
`Revision` records the source Git revision used for that adoption or update.

A future synchronizer may update only the content between
`<!-- GOVERNANCE:BEGIN -->` and `<!-- GOVERNANCE:END -->` in a consumer's
`AGENTS.md`. Content outside those markers is locally owned and must never be
silently removed or rewritten. Missing, duplicate, or malformed markers should
cause a visible failure rather than a best-effort destructive edit.

Updates should be explicit Git changes, normally reviewable in a consumer PR.
Consumers may adopt updates on different schedules; the design must not assume
immediate adoption of the latest governance state. The mandatory baseline is
non-overridable within a consumer's adopted revision; it does not require every
consumer to use the same revision.

## Deferred design

Future work may define versioning or opt-in profiles, but their schema and
semantics are intentionally unspecified. There are no scripts, bots, GitHub
Actions, cross-repository credentials, or invisible out-of-Git updates in this
initial version.
