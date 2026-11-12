# Worker handoff registry

Status: normative
Scope: organization
Source: work-governance

`WORKER-HANDOFF-01` is a lightweight, informative handoff between a CODEX
WORKER and an AI SUPERVISOR. It is not an approval, execution, review, or merge
authority. The Human/operator retains every material authorization.

## Central registry

Each repository that opts in MUST have exactly one dedicated technical GitHub
issue, named in its local instructions, for this protocol. The issue and its
comments together are the central registry. The issue body MUST identify the
protocol, state that comments are append-only snapshots, and link to this
document. It MUST NOT contain real data, credentials, or sensitive operational
detail.

The registry is initialized with a comment at revision `0` using the format
below, with `No accepted execution yet.` in both sections. Every accepted
execution is a new comment containing a complete replacement snapshot. No
worker edits or deletes an existing snapshot comment. This preserves the
evidence needed to detect concurrent and stale writes even though GitHub issue
comments do not provide an atomic compare-and-swap update.

```md
# WORKER-HANDOFF-01
Revision: <non-negative integer>
Parent revision: <previous revision; omit only for revision 0>

## CURRENT
- Execution: `<globally unique execution id>`
- Started UTC: <ISO-8601 UTC timestamp>
- Completed UTC: <ISO-8601 UTC timestamp>
- Status: <NO_OP | PR_READY | FAILED>
- Summary: <brief public-safe result>
- References: <comma-separated immutable URLs, commit SHA, PR/issue URL, or None>

## RECENT
### 1
- Execution: `<same execution id as CURRENT>`
- Started UTC: <ISO-8601 UTC timestamp>
- Completed UTC: <ISO-8601 UTC timestamp>
- Status: <NO_OP | PR_READY | FAILED>
- Summary: <brief public-safe result>
- References: <references or None>
```

`CURRENT` describes only the accepted current execution. `RECENT` is a
newest-first history, includes the `CURRENT` execution as entry 1, and contains
at most ten entries including that entry. A historical `PR_READY`, `FAILED`, or
`NO_OP` never states the current condition by itself.

An execution ID MUST be globally unique for the repository. It SHOULD combine a
worker/run identifier and a UTC start timestamp. Timestamps are UTC and include
the `Z` offset. `NO_OP` means no repository change was needed; `PR_READY` means
an independently reviewable PR is ready; and `FAILED` means the execution did
not complete its scoped work. References are included when they exist and must
be directly verifiable; their absence is recorded as `None`, not invented.

## Worker publication protocol

For every execution result, including `NO_OP`, a CODEX WORKER MUST attempt this
protocol before its brief Human-facing response:

1. Read the registry issue and all snapshot comments needed to resolve the
   accepted chain. Select the latest accepted snapshot, not merely the newest
   comment. Its revision is the expected parent.
2. Construct the next complete snapshot with `Revision` one greater than that
   parent, `Parent revision` equal to it, an updated `CURRENT`, and a bounded
   `RECENT` list. Check that the execution started no earlier than the accepted
   `CURRENT` completed; otherwise it is stale.
3. Post the snapshot as a new comment; do not edit the prior comment. Re-read
   the issue comments and verify that it is the sole candidate for its parent.
   Only then is the snapshot accepted and only then may the worker report the
   handoff as published.

If two comments name the same parent, a comment has an invalid revision or
format, the worker cannot establish a unique chain, or its execution is stale,
the worker MUST stop publication and reconcile from the real GitHub state. It
MUST NOT overwrite, delete, blindly retry, or select a winner by timestamp. The
previous accepted `CURRENT` remains authoritative until the conflict is resolved
by an authorized reconciliation. The worker reports the publication failure or
uncertainty explicitly to the Human/operator; it does not claim the handoff was
published.

The pure helper in `handoff/registry.py` defines the same revision, retention,
and stale-execution rules for clients that choose to reuse it. It intentionally
has no GitHub client or scheduler: this checkpoint adds neither automation nor
external services.

## Supervisor protocol

An AI SUPERVISOR MUST consult the registry first, resolve its accepted chain,
and then verify the actual repository and GitHub state independently. The
handoff is a prioritization aid only: it never authorizes execution, approval,
or merge, and it never replaces verification of commits, tests, PR state,
reviews, or repository policy.

If the registry issue, comments, or GitHub access is unavailable, the supervisor
MAY continue the normal review. It MUST state that the handoff was unavailable
or could not be resolved, and it must not infer a result from missing data.

## Consumer adoption

This is a new shared normative contract. A consumer that adopts it must name
its dedicated registry issue in local instructions and synchronize the managed
governance block at the adopted revision. Consumers that have not opted in do
not have a registry and continue their existing workflow.
