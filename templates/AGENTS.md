# Agent Instructions

<!-- GOVERNANCE:BEGIN -->
Status: normative  
Scope: organization  
Source: work-governance
Revision: <set to the source Git revision during adoption or synchronization>

This managed block is a self-contained projection of the common operating
contract. `work-governance` remains its canonical source.

### Mandatory baseline

- MUST NOT present unsupported evidence, specifications, formulas, APIs,
  formats, methodologies, or contracts as authoritative. Use reliable evidence,
  state uncertainty, or leave the affected work blocked. Identify any expressly
  permitted approximation as an approximation.
- MUST NOT claim an unperformed test, validation, or check, or hide a failure or
  blockage behind a fabricated implementation.
- MUST NOT destroy, overwrite, or rewrite existing work without necessary
  authority. Inspect what would be lost first.
- Technical capability is not authorization. Privileged, destructive, or
  irreversible operations require both explicit task need and sufficient
  authority. This includes force pushes, history rewrites, branch deletion, PR
  merges, repository-policy changes, and operations on production, real data,
  or external services.
- MUST NOT commit credentials, tokens, passwords, keys, secrets, or operational
  or sensitive data that should not be stored in the repository.

Projects may strengthen but MUST NOT weaken this baseline. A task defines the
objective and scope within applicable rules; it does not silently override
them. It may satisfy a condition a rule expressly permits.

### Common operating defaults

- Before editing, MUST identify the repository, current branch, latest commit,
  and working tree state; read all normative sources named below; and understand
  the requested scope.
- Existing work state takes priority over starting from `main`. MUST continue a
  named branch or PR rather than recreate it or open a replacement. If a
  specifically required branch is unavailable, stop modifications and report
  the blockage.
- MUST keep changes focused and avoid unrelated refactors or broad cosmetic
  work. MAY make supporting changes reasonably necessary for correctness.
- MUST run relevant available checks and SHOULD broaden them when risk warrants
  it. Report checks that could not run.
- MUST keep affected documentation accurate and record only consequential
  architectural, methodological, or contractual decisions.
- SHOULD favor deterministic, repeatable, inspectable processes and MUST NOT
  treat derived results as sources of truth.
- A blockage report MUST identify the blocked requirement, missing evidence,
  checks performed, and work deliberately left unchanged.

Explicit normative project constraints may replace these common defaults where
the mandatory baseline permits variation. Silence or omission is not an
exception. Unadopted template text is only a default.

The content between the governance markers is managed. A future synchronizer
MAY replace only content between those markers. It MUST NOT edit content outside
them or silently destroy local rules.
<!-- GOVERNANCE:END -->

## Project-specific instructions

The consumer repository owns everything outside the managed markers.

### Required context

- Read `PROJECT.md`.
- Add other required normative or contextual documents here; remove this note
  when unused.

### Local constraints

- Add explicit project-specific constraints and exceptions to common defaults
  here, or state `None`. Local rules cannot weaken the mandatory baseline.

### Validation

- Add project-specific test, lint, build, or documentation commands here when
  they exist.
