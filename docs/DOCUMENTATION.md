# Documentation Convention

Status: normative  
Scope: organization  
Source: work-governance

This document defines the shared documentation taxonomy. Projects SHOULD keep
only the documents that provide durable value; the taxonomy is not a mandate to
create empty files.

## Status, scope, and source

Use a short readable declaration near the title when semantics matter. A
project-owned document might declare:

```text
Status: normative
Scope: project
```

A managed projection declares its provenance separately:

```text
Status: normative
Scope: organization
Source: work-governance
Revision: <source revision>
```

- **Normative** content states rules, constraints, or required behavior.
- **Informative** content explains or summarizes and does not create a
  requirement.
- **Organization** scope applies across consumers through common governance.
- **Project** scope belongs to one consumer repository.
- `Source: work-governance` identifies a managed projection originating here.
- `Revision` identifies the Git revision used to produce or adopt that copy; it
  is set during adoption or synchronization, not embedded in the source
  template's own commit.

Not every informal note needs metadata. Normative documents SHOULD declare
status and scope. Managed projections SHOULD declare source and revision.

## Precedence and ownership

Within the governance revision a consumer has adopted, apply this order:

1. the mandatory baseline;
2. explicit normative project-specific constraints where variation is allowed;
3. common operating defaults;
4. templates and defaults not adopted as normative.

Projects may strengthen but MUST NOT weaken the mandatory baseline. An exception
to a common default MUST be explicit; silence or omission is not an override. A
task defines work within applicable normative constraints rather than adding a
new precedence layer. Informative text cannot override normative text.

`work-governance` is the canonical source for shared rules. A synchronized
managed block is a self-contained, identified projection, not an independent
normative source. Its `Source` and `Revision` make its origin inspectable.
Consumers may legitimately adopt different revisions; the baseline is
non-overridable within the revision each has adopted, not a requirement to
track the latest commit immediately.

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
and summarize only what a reader needs at that point. The managed `AGENTS.md`
block necessarily materializes the operational contract so a consumer remains
self-contained, but its provenance prevents it becoming a second canonical
source. Do not place architecture, roadmap, or domain exposition in `AGENTS.md`;
use it to direct readers to those sources.

Documentation is part of software state. Update relevant normative and
informative descriptions when a change invalidates them, but do not edit files
solely to satisfy ceremony or restate self-evident code. Derived reports and
generated outputs MUST NOT be treated as canonical inputs.
