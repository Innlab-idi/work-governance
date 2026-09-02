# Work Governance

Status: informative  
Scope: organization

This repository is the public, reusable baseline and canonical source for
development governance shared by a family of independent software repositories.
Its consumers may be public or private. This repository contains stable common
rules, not sensitive consumer context, architecture, domain knowledge, or the
roadmap of any consumer project.

> Common where stable, local where specific.

Consumer repositories combine a managed common section in `AGENTS.md` with
project-specific instructions that remain locally owned. The precedence is:

1. the mandatory baseline in the adopted governance revision;
2. explicit normative project-specific constraints where variation is allowed;
3. common operating defaults;
4. templates and defaults not adopted as normative.

Projects may strengthen but not weaken the mandatory baseline. A local
exception to a common default must be explicit; missing or stale local
documentation is not an exception.

## Contents

- [`AGENTS_BASE.md`](AGENTS_BASE.md): compact common operating rules.
- [`docs/WORKFLOW.md`](docs/WORKFLOW.md): the shared development process.
- [`docs/DOCUMENTATION.md`](docs/DOCUMENTATION.md): documentation semantics and ownership.
- [`templates/`](templates/): lightweight starting documents for consumers.
- [`sync/README.md`](sync/README.md): the intended future synchronization contract.

## Adoption

A consumer should start from [`templates/AGENTS.md`](templates/AGENTS.md). Its
managed block is a self-contained projection of the common operating contract,
identified by source revision; `work-governance` remains the single canonical
source. The consumer keeps its local material outside the managed markers and
may adopt the other templates when useful.

Synchronization is not implemented. Until an explicit, reviewable sync process
exists, adoption and updates are manual. Consumer projects remain independent
Git repositories; they are not submodules or parts of a monorepo.

## Public baseline and private extensions

All content and associated metadata in this repository must be suitable for
public disclosure. If sensitive organizational rules, internal workflows,
private repository names, infrastructure, permissions, configuration, or
specific automation are needed in the future, they must live in a separate
private extension. That extension should depend conceptually on this baseline,
must not duplicate it or become a second canonical source, and should add only
private constraints or behavior.

Neither this repository nor a future private extension may store real secrets
in Git. Secret values belong in GitHub Secrets, Environments, or another
appropriate secret-management system.

## License

This repository is available under the [MIT License](LICENSE).
