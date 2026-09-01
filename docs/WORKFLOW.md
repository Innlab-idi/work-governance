# Development Workflow

Status: normative  
Scope: organization  
Source: work-governance

This document explains the common collaboration process behind the compact
operating contract in `AGENTS_BASE.md`. The versioned repository is persistent
project memory; conversations and agent sessions are temporary working context.
Project-specific rules and evidence remain in the consumer repository according
to its local `AGENTS.md` and documentation contract.

The self-contained managed contract defines consumer-agent obligations. This
workflow develops that contract through explanation, recommendations, and
examples; it does not silently add mandatory consumer behavior.

## 1. Authority and work state

The repository's designated published or default integration branch (typically
`main`) is the authoritative shared baseline for completed work. New work
normally starts from its current state.

There is one important continuity rule: when a task explicitly continues an
open pull request, the identified PR head is the authoritative continuation
point for that in-progress task. The work MUST be continued there rather than
reconstructed from the published baseline. Arbitrary local or unversioned state
is not authoritative merely because it exists. After the PR is merged, the
designated published baseline again contains the authoritative incorporated
state.

This distinction preserves both a stable shared baseline and unfinished work
that has already acquired an explicit review boundary.

## 2. Recover context before acting

A new conversation or agent SHOULD be able to recover the relevant state from
versioned documentation and Git without relying on unrecorded conversational
memory. Before proposing or implementing a change:

1. identify the repository, current commit and branch, and working-tree state;
2. determine whether the task starts from the published baseline or continues
   an identified PR;
3. read the authoritative governance and context documents;
4. inspect the relevant implementation and recent versioned changes;
5. identify the current objective, frozen decisions, and unresolved blockers;
6. only then propose or implement the next change.

There is no universal project file list. The repository's local `AGENTS.md` and
documentation contract define which project-specific sources are authoritative.
A task prompt should describe the requested delta rather than restate that whole
contract, while still providing the objective, scope, any branch or PR
continuity requirement, and task-specific evidence or constraints unavailable
in the repository.

## 3. Collaboration roles

- **Human/operator:** owns intent and authorization, selects priorities,
  supplies unavailable business or domain context, and owns or delegates merge
  authorization for consequential changes.
- **Reviewer/planning agent:** reconstructs project state, helps scope work,
  prepares self-contained task instructions when useful, reviews changes
  against repository authority, and identifies regressions, contradictions,
  and useful next milestones.
- **Implementation agent:** inspects state, implements within scope, validates,
  updates required documentation, reports accurately, and stops at genuine
  blockers or authority gaps.
- **GitHub/version control:** provides the persistent, reviewable record of
  project state; pull requests provide explicit review boundaries for
  consequential changes.

These are functional roles. They do not depend on a particular agent product,
and one participant or tool may perform more than one role when appropriate.

## 4. Default collaboration loop

The normal loop is:

```text
current-state review -> scoped task -> implementation -> validation -> PR
-> review -> targeted correction if needed -> merge -> next milestone
```

The reviewer evaluates the result against authoritative repository state and
requests only corrections relevant to the task. This is a useful default, not
mandatory ceremony for every trivial edit.

## 5. Task and pull-request boundaries

A PR should normally contain one coherent principal technical, architectural,
methodological, documentation, or governance change, together with its directly
necessary tests and documentation. Separate PRs are useful when distinct review
boundaries provide real value, but micro-PRs add no benefit. Unrelated adjacent
work should stay out of scope.

Continuation of an existing PR means updating that PR, not recreating the same
work from the published baseline or opening a replacement. A task may identify
follow-up work without absorbing it into the current PR.

## 6. Branch and PR continuity

A branch name is useful evidence about a checkout, but not sufficient identity
by itself. Cloud or other managed environments may check out an existing PR
head under a generic local branch name. For continuation work, identity can be
assessed from the available evidence, including:

- the current commit SHA;
- the PR head SHA, when available;
- whether the working tree is clean or its modifications are understood; and
- the known task and PR context.

A matching `HEAD` and known PR head, together with an understood working tree,
can establish the correct continuation state even when the local branch name
differs. A trustworthy environment-provided checkout tied to the requested PR
does not require network access merely to prove the same fact again. Inability
to update PR metadata also need not block safe versioned file changes.

If the available checkout cannot be tied safely to the required in-progress
state, or commit identity conflicts with unexplained local changes, stop rather
than modify a different state or manufacture a reconstruction.

## 7. Execution environment and repository boundaries

Cloud execution is generally appropriate for work contained in one repository.
Local or CLI execution is preferable when the task genuinely requires
simultaneous access to multiple repositories, unavailable local files or
external artifacts, local hardware or services, or capabilities the cloud
environment cannot provide. Sibling repositories remain independent unless an
explicit architecture says otherwise; a self-contained task can transfer
necessary knowledge without copying sibling code, files, or methodology by
default.

Network access is best treated as a capability, not a default assumption.
Offline work is preferred when sufficient, with Internet access used when the
task needs it. Installing dependencies and granting unrestricted network access
are separate concerns. A network or provider failure is an environment
limitation until independent evidence shows otherwise; it does not by itself
invalidate a method or implementation.

## 8. Blockers and ambiguity

The common operating contract requires a blockage rather than fabricated or
unauthorized work. Conditions that warrant such a report include:

- required authoritative evidence is unavailable;
- the expected PR or task state cannot be identified safely;
- the task requires an unauthorized destructive or external action;
- ambiguity would change a frozen decision;
- exact required behavior would be replaced by an invented approximation; or
- the scope would need material expansion.

Minor ambiguity that existing rules resolve safely need not block work. As
required by the common operating contract, a blocker report identifies what is
blocked, why, what was checked, what remains unknown, and what was deliberately
not modified. Independent work MAY proceed when it remains safe and in scope.

## 9. Validation and completion

Before completion:

1. inspect the relevant final diff;
2. run applicable repository-defined checks;
3. distinguish checks passed, failed, and not run;
4. report limitations and discrepancies;
5. keep affected documentation consistent; and
6. state truthfully which commit, push, PR creation or update, review-state, and
   merge actions actually occurred.

Validation commands are project-specific and belong in local governance. A
focused commit and accurate PR summary should make both the change and its
remaining uncertainty reviewable.

### Changes to shared governance

Normative changes to `work-governance` MUST be recorded in Git and reviewed
through a pull request. The PR description MUST state the changed normative
behavior, the impact on consumer repositories, and whether resynchronization is
required. Distributed rules MUST NOT change silently outside Git history.

## 10. Governance without ceremony

Governance exists to reduce repeated mistakes and cognitive load, not to create
preventive bureaucracy. Prefer not to add documents without useful content,
artificial gates, mandatory experiments, unnecessary approval chains, needless
PR splitting, or infrastructure without a current use case. Additional process
is useful when it serves a concrete need in reproducibility, implementation
safety, reviewability, methodology, or maintainability.
