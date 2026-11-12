# Worker handoff registry

Status: normative
Scope: organization
Source: work-governance

`WORKER-HANDOFF-01` is a lightweight, informative handoff between a CODEX
WORKER and an AI SUPERVISOR. It is not an approval, execution, review, or merge
authority. The Human/operator retains every material authorization.

## Central registry

Each repository that opts in MUST have exactly one dedicated technical GitHub
issue, named in its local instructions, for this protocol. The local instructions
MUST identify the protocol and link to this document. The issue **body** is the
central registry and contains one bounded snapshot only, exactly in the format
rendered and parsed by `handoff/registry.py`; it carries no additional protocol
link or metadata. Comments are not a handoff history and workers MUST NOT use
them to publish executions. The body MUST NOT contain real data, credentials, or
sensitive operational detail.

The registry is initialized at revision `0` using the format below, with
`No accepted execution yet.` in both sections. Every accepted execution replaces
the body with the next complete snapshot. Thus the persistent registry contains
one `CURRENT` and at most ten `RECENT` executions, rather than an unbounded
issue-comment history.

```md
# WORKER-HANDOFF-01
Revision: <non-negative integer>
Parent revision: <previous revision, or None only for revision 0>

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

GitHub issue-body updates have no compare-and-swap operation. A read, write,
and readback sequence cannot make concurrent writers safe. Therefore v1 permits
exactly one strictly serialized publisher for a registry: local instructions
must identify the worker or operator-controlled publishing session, and no
second worker may read, prepare, or write that issue body until the active
publisher has completed or failed. A repository needing concurrent publication
must adopt a real atomic mechanism in a later authorized change; it MUST NOT
pretend this protocol supplies one.

For every execution result, including `NO_OP`, the sole CODEX WORKER publisher
MUST attempt this protocol before its brief Human-facing response:

1. Establish that it is the designated active publisher, then read and parse the
   issue body. Reject malformed state, a revision other than the expected
   parent, duplicate IDs, or a stale execution.
2. Construct the next complete snapshot with `Revision` one greater than that
   parent, `Parent revision` equal to it, an updated `CURRENT`, and a bounded
   `RECENT` list. Check that the execution started no earlier than the accepted
   `CURRENT` completed; otherwise it is stale.
3. Replace the issue body with that snapshot, then read and parse the body
   again. Only an identical readback is accepted; only then may the worker
   report the handoff as published.

If serialization cannot be established, the body is malformed, a write fails,
readback differs, or the result is stale, the worker MUST stop publication and
reconcile the actual GitHub state. It MUST NOT overwrite, delete, or blindly
retry. The worker reports the publication failure or uncertainty explicitly to
the Human/operator; it does not claim the handoff was published.

The pure helper in `handoff/registry.py` parses, validates, renders, and runs a
minimal deterministic read/write/read cycle against an injected issue-body
store. Its tests use synthetic stores only; they demonstrate protocol handling,
not effective GitHub API behavior. It intentionally has no GitHub client or
scheduler: this checkpoint adds neither automation nor external services.

## Supervisor protocol

An AI SUPERVISOR MUST consult and parse the issue body first, and then verify
the actual repository and GitHub state independently. The
handoff is a prioritization aid only: it never authorizes execution, approval,
or merge, and it never replaces verification of commits, tests, PR state,
reviews, or repository policy.

If the registry issue, comments, or GitHub access is unavailable, the supervisor
MAY continue the normal review. It MUST state that the handoff was unavailable
or could not be resolved, and it must not infer a result from missing data.

## Consumer adoption

This is a new shared normative contract. A consumer that adopts it must name
its dedicated registry issue, identify this protocol, and link to this document
in local instructions, then synchronize the managed governance block at the
adopted revision. Consumers that have not opted in do not have a registry and
continue their existing workflow.
