# Repository Agent Instructions

Status: normative
Scope: repository

Before changing shared governance, read `AGENTS_BASE.md`, `docs/WORKFLOW.md`,
and `docs/DOCUMENTATION.md` in full. `AGENTS_BASE.md` remains the canonical
source of the common baseline; this file governs development of this repository
and is not projected into consumer repositories.

- Treat this repository and all versioned content and GitHub metadata as
  public, including branch names, commit messages, PR descriptions, and PR
  comments.
- Do not include secrets, credentials, sensitive data, internal operational
  data, private paths, client names, unnecessary details about private
  consumers, or sensitive infrastructure. This repository is not a secret
  store; real secrets belong in GitHub Secrets, Environments, or another
  appropriate secret-management system, never in Git.
- Keep shared governance generic. Do not add rules for a specific consumer.
- In every normative-change PR, explain the impact on consumers and whether
  they must resynchronize.
- Do not add automation, GitHub Actions, or cross-repository infrastructure
  without an explicit milestone authorizing that work.
