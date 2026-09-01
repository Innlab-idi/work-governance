# Work Governance

Status: informative  
Scope: organization

This repository is the canonical source for development governance shared by a
family of independent software repositories. It contains stable common rules,
not the architecture, domain knowledge, or roadmap of any consumer project.

> Common where stable, local where specific.

Consumer repositories combine a managed common section in `AGENTS.md` with
project-specific instructions that remain locally owned. The precedence is:

1. explicit project-specific constraints;
2. common governance from `work-governance`;
3. templates and defaults.

A local exception must be explicit. Missing or stale local documentation does
not override common governance.

## Contents

- [`AGENTS_BASE.md`](AGENTS_BASE.md): compact common operating rules.
- [`docs/WORKFLOW.md`](docs/WORKFLOW.md): the shared development process.
- [`docs/DOCUMENTATION.md`](docs/DOCUMENTATION.md): documentation semantics and ownership.
- [`templates/`](templates/): lightweight starting documents for consumers.
- [`sync/README.md`](sync/README.md): the intended future synchronization contract.

## Adoption

A consumer should start from [`templates/AGENTS.md`](templates/AGENTS.md), keep
its local material outside the managed markers, and adapt only the local
section. It may adopt the other templates when those documents are useful.

Synchronization is not implemented. Until an explicit, reviewable sync process
exists, adoption and updates are manual. Consumer projects remain independent
Git repositories; they are not submodules or parts of a monorepo.
