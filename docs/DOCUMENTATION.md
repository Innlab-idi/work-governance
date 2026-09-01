# Documentation Convention

Status: normative  
Scope: organization  
Source: work-governance

This document defines the shared documentation taxonomy. Projects SHOULD keep
only the documents that provide durable value; the taxonomy is not a mandate to
create empty files.

## Status, scope, and source

Use a short readable declaration near the title when semantics matter:

```text
Status: normative
Scope: project
Source: work-governance
```

- **Normative** content states rules, constraints, or required behavior.
- **Informative** content explains or summarizes and does not create a
  requirement.
- **Organization** scope applies across consumers through common governance.
- **Project** scope belongs to one consumer repository.
- `Source: work-governance` identifies managed content originating here.

Not every informal note needs metadata. Normative documents SHOULD declare
status and scope; synchronized documents MAY also declare their source.

## Precedence and ownership

When sources conflict, apply this order:

1. explicit project-specific constraints;
2. common governance from `work-governance`;
3. templates and defaults.

An exception to common governance MUST be explicit. Silence, omission, or an
old local copy does not constitute an override. A project owns its specific
context and constraints; `work-governance` owns shared rules. Informative text
cannot override normative text.

## Document roles

| Document | Primary role | Update when |
| --- | --- | --- |
| `AGENTS.md` | Concise operational instructions and a reading map for agents and contributors. | Required actions, sources, constraints, or validation commands change. |
| `PROJECT.md` | Stable purpose, scope, boundaries, actors, and relevant systems. | The project's identity or boundaries change. |
| `ARCHITECTURE.md` | Current technical architecture. It describes what exists, not a future roadmap. | Implemented architecture changes materially. |
| `ROADMAP.md` | Planned future work, milestones, and priorities. | Plans or priorities change. |
| `DECISIONS.md` | Consequential decisions already made and their rationale. | A durable decision is made, superseded, or deliberately reversed. |
| `WORKFLOW.md` | Development process from task through merge. | The actual development process changes. |
| `METHODOLOGY.md` | Optional formal definition of a project-specific domain methodology. | The methodology changes; omit this file when no such methodology exists. |
| `README.md` | Human entry point and navigation. | Onboarding or links change; it MUST NOT replace normative sources. |

## Maintenance without duplication

Give each concept one primary home. Other documents SHOULD link to that source
and summarize only what a reader needs at that point. Do not place architecture,
roadmap, or domain exposition in `AGENTS.md`; use it to direct readers to those
sources. Do not copy common rules into several project documents.

Documentation is part of software state. Update relevant normative and
informative descriptions when a change invalidates them, but do not edit files
solely to satisfy ceremony or restate self-evident code. Derived reports and
generated outputs MUST NOT be treated as canonical inputs.
