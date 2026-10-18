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
`main`, `master`, or another repository-designated name) is the authoritative
shared baseline for completed work. New work normally starts from its current
state. In a managed environment, the task checkout may be a provisioned
projection of that state under a different, generic local branch name. That
local name neither changes the identity of the published branch nor proves the
checkout's content identity by itself.

There is one important continuity rule: when a task explicitly continues an
open pull request, the identified PR head is the authoritative continuation
point for that in-progress task. The work MUST be continued there rather than
reconstructed from the published baseline. Arbitrary local or unversioned state
is not authoritative merely because it exists. After the PR is merged, the
designated published baseline again contains the authoritative incorporated
state.

This distinction preserves both a stable shared baseline and unfinished work
that has already acquired an explicit review boundary.

### Material decisions and durable authority

The Human/operator authorizes material decisions, not workflow events. Separate
ownership of a material decision from whether it remains unresolved and from the
workflow events that execute it. A human-owned choice can already be resolved;
implementation, publication, review, merge, issue closure, or another mechanical
boundary does not by itself reopen it.

An explicit human/operator material decision may remain applicable beyond its
original conversation, task event, or workflow boundary. Treat it as a bounded
authorization envelope. Later work may inherit that authority when all of its
human-owned material requirements are a faithful subset of the resolved envelope
and no invalidator has occurred. Recover the decision, its bounds, and any later
changes from available evidence; do not invent missing authorization.

Content and bounds govern. Agent-proposed work may faithfully materialize a
prior human resolution. Human-proposed work does not authorize arbitrary later
expansion. Task provenance or authorship alone is insufficient evidence of the
needed authority. Technical capability likewise remains distinct from authority.

### Default bounded completion

When the Human/operator explicitly approves an entire task, checkpoint, or phase
without narrowing completion authority, that decision should ordinarily cover
the bounded repository lifecycle necessary to complete it, as applicable:

- implementation inside the approved scope and relevant checks;
- ordinary non-force publication and PR creation/update;
- independent review and deterministic non-semantic reconciliation;
- ordinary authorized merge; and
- durable evidence and task/issue closure.

This default remains subject to the mandatory baseline and stricter project
constraints. Explicit limits govern: for example, an instruction to leave a PR
unmerged excludes merge from the envelope. Completion authority is not blanket
standing authority for arbitrary future work. It does not silently authorize
material scope or objective expansion, production effects, real/private-data
exposure, credentials, new privilege, destructive or irreversible operations,
force pushes or history rewrites, new security/containment boundaries, materially
new architecture/runtime decisions, extra attempts after a bounded limit is
consumed, or other material choices outside the resolved decision. Such work
requires sufficient explicit authority covering those consequences.

### Invalidators and unresolved material choices

Inherited authority ceases to be sufficient when safe continuation needs a
material choice not already covered. Check for:

- material objective or scope expansion;
- authority or privilege expansion;
- a new repository or system surface with material consequences;
- production or real/private-data interaction, exposure, or credential access;
- destructive or irreversible risk;
- material architecture, runtime, compatibility, or security/containment-boundary
  changes not already covered;
- an increase in the attempt/retry budget after a defined limit is consumed;
- retry of a mutation whose outcome remains genuinely uncertain and whose retry
  authority was not already resolved;
- a conflict with multiple materially plausible resolutions;
- a later contradictory human decision; or
- another genuinely unresolved material decision.

Escalate to the Human/operator when a material choice remains unresolved or prior
authority has been exceeded or invalidated. Ordinary implementation defects,
naming, local organization, test organization, deterministic representation
fixes, exact state reconciliation, and routine mechanical completion do not
in themselves create new human decisions. If fixing a defect does require an
uncovered material choice, escalate that choice rather than the workflow event.

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

- **Human/operator:** owns intent and material authorization, selects priorities,
  supplies unavailable business or domain context, and resolves material choices
  outside existing authority. May authorize bounded completion, including merge,
  in advance or expressly narrow that authority.
- **Reviewer/planning agent:** reconstructs project state, helps scope work,
  prepares self-contained task instructions when useful, reviews changes
  against repository authority, and identifies regressions, contradictions,
  and useful next milestones. May verify that work fits an existing decision or
  identify an authority gap; review does not create, enlarge, or substitute for
  human-owned authority.
- **Implementation agent:** inspects state, implements within scope, validates,
  updates required documentation, reports accurately, and stops at genuine
  blockers or authority gaps. May inherit applicable resolved authority but
  cannot enlarge it through implementation capability or scope changes.
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
mandatory ceremony for every trivial edit. Each stage executes within applicable
authority; reaching a commit, publication, PR update, completed review, merge, or
closure does not itself require the same human decision again. Review still
checks compliance and correctness, and does not supply missing authorization.

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
by itself. Managed environments may expose either a provisioned published
baseline or an existing PR head under a generic local branch name, potentially
without a local published-branch ref or configured remote.

For new work, a request to start from the published baseline normally specifies
the content and state from which work begins, not the spelling of the local
branch. The provisioned task checkout can represent that baseline when its
working tree is understood and no available evidence contradicts that identity.
The generic name is neither validation nor a blocker, and there is no reason to
manufacture a local `main`, `master`, or other published-branch ref solely to
match the designated branch's name. Lack of a remote or network access likewise
does not require revalidating an otherwise trustworthy provisioned state.

For continuation work, identity can be assessed from the available evidence,
including:

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
than modify a different state or manufacture a reconstruction. The same caution
applies to a new task when its provisioned content conflicts with the required
baseline. When the task operates on a specific branch or PR as a Git or review
object, rather than merely starting from its content, that object's identity and
availability remain part of the requirement.

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

### Operator shell procedures

A multi-step shell procedure intended for a human operator must fail closed
when later steps depend on earlier preconditions or include mutating,
privileged, or external operations. A failure or unmet precondition must stop
the dependent steps. For instructions intended to be copied, pasted, or run
manually, prefer one self-contained script unless another mechanism reliably
provides the same guarantee. This is proportional guidance: trivial,
independent inspection commands do not need procedural scaffolding.

Shell exception modes can help, but they do not replace an explicit check of a
native process result. When success from an external executable is required to
continue, the procedure must inspect and validate its exit code or other
reported status, then stop on failure.

Procedures intended for direct or automated execution must avoid accidental
interaction through pagers, prompts, or similar blocking behavior. Use the
tool's supported non-interactive mechanism when available. For example,
`git --no-pager` prevents Git from invoking a pager; the general rule applies
to every applicable tool, not only Git.

Control-flow decisions must not depend on truthiness, implicit coercion, or
ambiguous cardinality in collections, arrays, JSON, multiline output, or shell
objects. Normalize relevant output to a scalar value or explicitly interpret
and validate a structure before deciding to continue, block, mutate, or retry.
For example, PowerShell procedures should explicitly test the intended value or
count instead of depending on implicit conversion of command output.

Remote systems may acknowledge a successful write before every metadata read
reflects it. When an immediate read appears to contradict a successful write,
treat the result as uncertain or possibly eventually consistent. Revalidate the
authoritative state before retrying, compensating, or making another mutation;
do not infer failure or blindly repeat the write. This applies to APIs, Git
hosting, and other external services.

A tool, process, network, or hosting failure is an operational condition, not a
new grant of authority or automatically a new human decision. Before continuing,
compensating, or retrying, reconcile exactly what happened against authoritative
observations. If they establish the outcome and a unique safe continuation
within existing authority, continue from the observed state. Never blindly
repeat an uncertain mutation. If the outcome remains genuinely uncertain, do
not retry without sufficient resolved retry authority; report the operational
blockage when evidence is unavailable. Escalate to the Human/operator only when
resolution itself requires a new material choice or new authority, such as an
uncovered uncertain retry, a consumed retry-budget increase, or multiple
materially plausible conflict resolutions. An operational stop does not reset
an attempt budget or create authority.

## 8. Blockers and ambiguity

The common operating contract requires a blockage rather than fabricated or
unauthorized work. Conditions that warrant such a report include:

- required authoritative evidence is unavailable;
- the expected PR or task state cannot be identified safely;
- the task requires an unauthorized destructive or external action;
- ambiguity would change a frozen decision;
- exact required behavior would be replaced by an invented approximation; or
- the scope would need material expansion.

Human escalation has a high threshold: a genuinely unresolved material choice,
exceeded authority, or an invalidator described in section 1. Starting
implementation, making a commit, publishing, creating/updating a PR, completing
review, merging, closing a task, or reconciling an operational stop with one safe
authorized continuation is not by itself such a choice. Missing operational
evidence may block the affected action without needing a new human decision.

Minor ambiguity that existing rules resolve safely need not block work. As
required by the common operating contract, a blocker report identifies what is
blocked, why, what was checked, what remains unknown, and what was deliberately
not modified. Independent work MAY proceed when it remains safe and in scope.

## 9. Research Checkpoint

A Research Checkpoint is required before making a material decision that
depends on unresolved external or runtime uncertainty. Typical triggers include:

- unexpected or unexplained runtime behavior;
- a security, authority, isolation, or privilege boundary;
- current or version-specific behavior of a runtime, API, platform, library, or
  external service;
- a consequential workaround for which prior art, an upstream limitation, or a
  known solution may exist; or
- an external assumption whose falsity could invalidate the implementation or
  the evidence offered for it.

The checkpoint is proportional to the uncertainty and the consequence of being
wrong. Routine work supported by sufficient local evidence does not trigger it.
When one authoritative source resolves the question adequately, no broader
survey or additional ceremony is required. The checkpoint is an evidence step,
not a new human approval gate.

When applicable, prefer sources in this order:

1. the exact relevant version, source code, protocol, or specification;
2. upstream issues, pull requests, commits, release notes, and official
   documentation;
3. applicable standards and established technical literature;
4. relevant recent research; and
5. community material as a source of hypotheses, not authority by default.

External documentation and prior art can establish expected behavior or known
problems, but they do not replace runtime evidence when the requirement being
demonstrated depends on effective system behavior. Likewise, failure of an
operation is not positive evidence that the intended boundary was exercised
unless there is evidence that execution actually reached that boundary.

When the checkpoint materially affects a decision, retain enough information
in an appropriate durable, reviewable location to reconstruct the reasoning.
Depending on the project, that may be an issue, pull request, `DECISIONS.md`,
roadmap, or another suitable versioned source. Useful content includes the
research question, version or scope, sources inspected, established facts, open
uncertainties, design impact, and a conclusion such as `NO_CHANGE`,
`MODIFY_DESIGN`, `NEED_RUNTIME_EVIDENCE`, or `BLOCKED_UPSTREAM`. This is
conceptual guidance, not a mandatory new document or fixed format.

## 10. Validation and completion

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

## 11. Governance without ceremony

Governance exists to reduce repeated mistakes and cognitive load, not to create
preventive bureaucracy. Prefer not to add documents without useful content,
artificial gates, mandatory experiments, unnecessary approval chains, needless
PR splitting, or infrastructure without a current use case. Additional process
is useful when it serves a concrete need in reproducibility, implementation
safety, reviewability, methodology, or maintainability.
