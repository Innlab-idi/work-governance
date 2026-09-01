# Common Agent Instructions

Status: normative  
Scope: organization  
Source: work-governance

These rules apply unless an explicit project-specific constraint overrides
them. Follow the full process in [`docs/WORKFLOW.md`](docs/WORKFLOW.md) and the
document semantics in [`docs/DOCUMENTATION.md`](docs/DOCUMENTATION.md).

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

## Operating rules

- Existing work state takes priority over the convenience of starting from
  `main`. When instructed to continue a branch or pull request, MUST continue
  it; MUST NOT reconstruct it on another branch or open a replacement PR. If a
  specifically required branch is unavailable, stop modifications and report
  the blockage.
- MUST implement the requested scope. MUST NOT add opportunistic refactors,
  broad cosmetic changes, or unrelated features. Auxiliary changes MAY be made
  when reasonably necessary for a correct result.
- MUST NOT present an invented formula, specification, API, format,
  methodology, or contractual behavior as authoritative. Use reliable evidence,
  state uncertainty, or leave the affected work blocked. An approximation is
  allowed only when explicitly permitted and identified as such.
- MUST run available checks relevant to the change and SHOULD broaden testing
  when risk warrants it. Report checks that could not run; MUST NOT claim
  unperformed verification.
- MUST keep relevant documentation consistent with the software, without
  adding documentation merely to repeat the obvious. Record consequential
  architectural, methodological, or contractual decisions, not trivial detail.
- SHOULD favor deterministic, repeatable, inspectable processes with clear
  inputs and outputs. MUST NOT treat derived results as sources of truth.
- MUST NOT erase, overwrite, or restructure existing work without need. Inspect
  what would be lost before a destructive operation.
- A blockage report MUST identify the blocked requirement, missing evidence,
  checks performed, and work deliberately left unchanged. MUST NOT hide a
  blockage behind a fabricated implementation.
