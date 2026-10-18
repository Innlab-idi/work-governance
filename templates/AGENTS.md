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
- MUST perform a proportionate Research Checkpoint before a material decision
  depends on unresolved external or runtime uncertainty. Prefer directly
  relevant authoritative sources, preserve the consequential result in an
  appropriate reviewable record, and obtain runtime evidence when the claim
  depends on effective system behavior. A failed operation is not positive
  evidence that the intended boundary was exercised unless execution is shown
  to have reached that boundary. Routine work with sufficient local evidence
  does not trigger this checkpoint.
- MUST NOT claim an unperformed test, validation, or check, or hide a failure or
  blockage behind a fabricated implementation.
- MUST NOT destroy, overwrite, or rewrite existing work without necessary
  authority. Inspect what would be lost first.
- Technical capability is not authorization. Privileged, destructive, or
  irreversible operations require both explicit task need and sufficient
  authority. This includes force pushes, history rewrites, branch deletion, PR
  merges, repository-policy changes, and operations on production, real data,
  or external services.
- The Human/operator authorizes material decisions, not workflow events.
  Sufficient authority MAY come from an applicable prior explicit material
  decision, retained as a bounded authorization envelope. Later work MAY inherit
  it only when its human-owned material requirements remain a faithful subset
  of that resolved envelope and no invalidator has occurred. Content and bounds
  govern, not who proposed the work. MUST NOT seek duplicate authorization merely
  for implementation, publication, review, merge, or task closure already covered.
- Inherited authority MUST NOT cover unresolved material choices or survive
  invalidators: material objective, scope, authority, or privilege expansion;
  a new repository/system surface with material consequences; production or
  real/private-data interaction; credential access; destructive/irreversible
  risk; or material architecture, runtime, compatibility, or security-boundary
  changes not already covered. Other invalidators include increasing a consumed
  attempt/retry budget, retrying a genuinely uncertain mutation without resolved
  retry authority, conflicts with multiple materially plausible resolutions,
  a later contradictory human decision, or another unresolved material choice.
  Material consequences already explicitly covered need no duplicate decision;
  later contradictory human decisions supersede prior authority. Unresolved
  material choices require human escalation. Review MAY verify existing authority
  or identify a gap; neither review nor implementation capability creates or
  enlarges human-owned authority.
- MUST NOT commit credentials, tokens, passwords, keys, secrets, or operational
  or sensitive data that should not be stored in the repository.
- A multi-step shell procedure for a human operator MUST fail closed when later
  steps depend on earlier preconditions or perform mutating, privileged, or
  external operations. Prefer one self-contained script for copy-and-paste or
  manual execution unless another equally reliable mechanism enforces that
  property. This does not impose ceremony on trivial, independent inspection
  commands.
- Shell exception modes MUST NOT substitute for checking a native process result.
  When an external executable's success is a precondition, explicitly validate
  its exit code or status and stop on failure. Direct or automated procedures
  MUST use available non-interactive tool mechanisms so prompts or pagers cannot
  accidentally block them.
- Before a control-flow decision to continue, block, mutate, or retry, normalize
  and explicitly interpret relevant shell output as a scalar or validated
  structure. MUST NOT rely on truthiness, implicit coercion, or ambiguous
  collection cardinality.
- Tool, process, network, or hosting failures and apparently contradictory reads
  require exact reconciliation against authoritative state before continuation,
  compensation, or retry. This includes successful remote writes followed by
  conflicting metadata reads or eventual consistency. MUST NOT blindly repeat
  an uncertain mutation. When observation establishes what happened and one safe
  continuation within existing authority, continue from that state; an
  operational stop alone MUST NOT trigger duplicate human authorization.

Projects may strengthen but MUST NOT weaken this baseline. A task defines the
objective and scope within applicable rules; it does not override the mandatory
baseline. It may satisfy only a condition or authorization that a rule
expressly contemplates.

### Common operating defaults

- Explicit approval of an entire task, checkpoint, or phase SHOULD ordinarily
  cover its bounded repository completion unless the Human/operator narrows it:
  in-scope implementation, relevant checks, ordinary non-force publication, PR
  creation/update, independent review, deterministic non-semantic reconciliation,
  ordinary authorized merge, and durable evidence/task closure, as applicable.
  This is not standing authority for future work and MUST NOT silently authorize
  any material choice or operation outside the resolved envelope. Applicable
  safeguards and stricter project constraints still apply.
- Before editing, MUST identify the repository, current branch, latest commit,
  and working tree state; read all normative sources named below; and understand
  the requested scope.
- Existing work state takes priority over starting from the published baseline.
  MUST continue an identified branch or PR state rather than recreate it or
  open a replacement. Stop modifications when that state cannot be identified
  safely or when a branch or PR that is itself the operation target is
  unavailable.
- A managed environment MAY expose its provisioned checkout under a generic
  local branch name, without a local ref for the published branch or a
  configured remote. Those conditions alone MUST NOT block work or require
  creating or reconstructing a local `main`, `master`, or other
  published-branch ref. A request to start from the published baseline normally
  constrains the base state, not the local branch name. The provisioned checkout
  MAY be used when the working tree is understood and available evidence does
  not contradict that state identity; otherwise, stop and report the blockage.
- MUST keep changes focused and avoid unrelated refactors or broad cosmetic
  work. MAY make supporting changes reasonably necessary for correctness.
- MUST run relevant available checks and SHOULD broaden them when risk warrants
  it. Distinguish checks that passed, failed, or were not run, and report
  limitations or discrepancies.
- MUST keep affected documentation accurate and record only consequential
  architectural, methodological, or contractual decisions.
- SHOULD favor deterministic, repeatable, inspectable processes and MUST NOT
  treat derived results as sources of truth.
- A blockage report MUST identify the blocked requirement, missing evidence,
  checks performed, and work deliberately left unchanged.
- Before finishing, MUST review the relevant final diff and follow the
  repository's established PR, review, and merge process. MUST NOT claim a
  commit, push, PR, or merge occurred unless it actually occurred.

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
