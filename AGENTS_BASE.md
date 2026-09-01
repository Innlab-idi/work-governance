# Common Agent Instructions

Status: normative  
Scope: organization  
Source: work-governance

This is the primary source for the common operating contract. The mandatory
baseline cannot be weakened by project instructions or a task; projects may
make it stricter. Explicit normative project constraints may replace common
defaults where the baseline permits variation. A task defines the objective
and scope within applicable rules; it does not override the mandatory baseline.
It may satisfy only a condition or authorization that a rule expressly
contemplates. Follow the expanded process in
[`docs/WORKFLOW.md`](docs/WORKFLOW.md) and the document semantics in
[`docs/DOCUMENTATION.md`](docs/DOCUMENTATION.md).

## Before changing files

You MUST identify the repository, current branch, latest commit, and working
tree state. You MUST read in full every normative source named by the local
`AGENTS.md` and understand the requested scope. Commands such as these are a
convenient inspection method, not a required implementation:

```bash
git branch --show-current
git log -1 --format='%H %s'
git status --short --branch
```

## Mandatory baseline

- MUST NOT present unsupported evidence, specifications, formulas, APIs,
  formats, methodologies, or contracts as authoritative. Use reliable evidence,
  state uncertainty, or leave the affected work blocked. An approximation is
  allowed only when explicitly permitted and identified as such.
- MUST NOT claim a test, validation, or check ran when it did not, or hide a
  failure or blockage behind a fabricated implementation.
- MUST NOT destroy, overwrite, or rewrite existing work without necessary
  authority. Inspect what would be lost before a destructive operation.
- Technical capability is not authorization. Force pushes, history rewrites,
  branch deletion, PR merges, repository-policy changes, and operations on
  production, real data, or external services require both explicit task need
  and sufficient authority. The same applies to comparably privileged,
  destructive, or irreversible operations.
- MUST NOT commit credentials, tokens, passwords, keys, secrets, or operational
  or sensitive data that should not be stored in the repository.

## Common operating defaults

- Existing work state takes priority over the convenience of starting from
  `main`. When instructed to continue a branch or pull request, MUST continue
  it; MUST NOT reconstruct it on another branch or open a replacement PR. If a
  specifically required branch is unavailable, stop modifications and report
  the blockage.
- MUST implement the requested scope. MUST NOT add opportunistic refactors,
  broad cosmetic changes, or unrelated features. Auxiliary changes MAY be made
  when reasonably necessary for a correct result.
- MUST run available checks relevant to the change and SHOULD broaden testing
  when risk warrants it. Distinguish checks that passed, failed, or were not
  run, and report limitations or discrepancies.
- MUST keep relevant documentation consistent with the software, without
  adding documentation merely to repeat the obvious. Record consequential
  architectural, methodological, or contractual decisions, not trivial detail.
- SHOULD favor deterministic, repeatable, inspectable processes with clear
  inputs and outputs. MUST NOT treat derived results as sources of truth.
- A blockage report MUST identify the blocked requirement, missing evidence,
  checks performed, and work deliberately left unchanged. MUST NOT hide a
  blockage behind a fabricated implementation.
- Before finishing, MUST review the relevant final diff and follow the
  repository's established PR, review, and merge process. MUST NOT claim a
  commit, push, PR, or merge occurred unless it actually occurred.
