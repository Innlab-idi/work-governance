# Development Workflow

Status: normative  
Scope: organization  
Source: work-governance

This document is the primary source for the common development process:

```text
task -> context review -> repository inspection -> implementation
     -> tests -> documentation -> PR/review -> merge
```

## 1. Establish context

Read the task and the repository's `AGENTS.md` before editing. Read every
normative document it requires, then consult descriptive context needed for the
change. Identify assumptions and the boundary between requested work and
possible follow-up work.

## 2. Inspect the repository

Confirm the repository identity, current branch, latest commit, and working
tree state. Inspect existing changes before touching them. An unborn repository
may have no latest commit; that is a valid state to record, not a reason to
invent history.

### Branch and review continuity

The real state of existing work takes priority over the convenience of starting
from `main`. If the task names an existing branch or pull request:

- verify the branch before editing and continue on it;
- do not recreate its changes from `main` or on a replacement branch;
- continue the existing PR rather than opening a new one.

If a specifically required branch is unavailable, stop before modifying files
and report the blockage. Do not manufacture an alternative state.

## 3. Implement the requested change

Keep the change focused. Avoid unrelated cleanup, extensive cosmetic edits, and
speculative features. Small supporting changes are appropriate only when they
are reasonably necessary to complete the task correctly.

Use established sources for precision-sensitive requirements. If authoritative
evidence for a formula, API, format, methodology, specification, or contract is
missing, investigate reliable available sources. Otherwise preserve the
uncertainty or block that portion; never silently substitute an approximation.

Before destructive work, inspect the affected content and determine what would
be lost. Prefer deterministic, repeatable, and inspectable transformations.

## 4. Validate

Run the most relevant available tests and checks. Expand to broader suites when
the change's risk or reach justifies it. Distinguish clearly among passed,
failed, and unexecuted checks. A task is not verified by a check that was not
run.

Review the resulting diff for unintended changes, unresolved placeholders,
and accidental loss of existing work.

## 5. Reconcile documentation and decisions

Update documentation in the same task when the change makes it inaccurate.
Follow [`DOCUMENTATION.md`](DOCUMENTATION.md) to update the correct source
instead of duplicating content. Record a decision only when its architectural,
methodological, or contractual effect will meaningfully constrain future work.

## 6. Review and merge

Prepare a focused commit and an accurate review summary. Include validation
results and any remaining uncertainty. Use the repository's established PR,
review, and merge path; do not claim merge completion until it has occurred.

## Blockages

A precise blockage report states:

1. the requirement that cannot be completed;
2. the evidence or capability that is missing;
3. what was inspected or attempted; and
4. what was deliberately not changed.

A blockage is preferable to an authoritative-looking invention. Work that is
independent of the blocked portion MAY proceed when doing so is safe and within
scope.
