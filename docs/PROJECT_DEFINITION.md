# AI Workflow Integration Hub — Project Definition

## Purpose

AI Workflow Integration Hub is a public coordination repo for safe AI-tool workflows.

Its job is to document, test, and improve how ChatGPT, Claude, Codex, GitHub, local AI tools, and local-first projects work together without exposing private data or creating another oversized agent system.

This repo is not the private memory system. It is the public workflow hub.

## Core Distinction

### Public repo

`ai-workflow-integration-hub`

This may contain:

- public documentation
- setup guides
- AI handoff workflows
- prompt templates
- repo-packaging instructions
- AGENTS.md patterns
- Repomix workflows
- MarkItDown workflows
- Basic Memory sandbox notes
- MCP research notes
- safety checklists
- non-private examples
- synthetic sample data only

### Private local system

`marshall-local-os`

This stays local and private.

This may contain:

- personal memories
- private decisions
- open loops
- local context packs
- logs
- notes archives
- data sources
- approval queues
- personal operating state
- financial, work, health, relationship, or identity context
- raw ChatGPT / Claude / Apple Notes exports

`marshall-local-os` must not be pushed to public GitHub.

## Tool Lane

The approved tool lane is:

1. AGENTS.md
2. Repomix
3. MarkItDown
4. Basic Memory sandbox test
5. One controlled MCP layer

The goal is useful AI handoff, not tool-chasing.

## What This Project Should Do

This project should help answer:

- How do I prepare a repo for ChatGPT, Claude, and Codex?
- How do I safely package repo context?
- How do I prevent private data from entering public repos?
- How do I write AGENTS.md instructions?
- How do I test AI workflow tools without overcommitting?
- How do I connect local-first workflows to AI tools safely?

## What This Project Must Not Do

This project must not:

- store private memories
- store personal context packs
- store raw exports
- mirror `marshall-local-os`
- include `.env` files
- include credentials, tokens, keys, or secrets
- include financial records
- include health records
- include work-sensitive information
- include private relationship notes
- include employer data
- include logs from private workflows
- include generated private context packs
- become the source of truth for Marshall’s personal operating system

## Public/Private Barrier

Default rule:

> If the file came from `marshall-local-os/data/`, it does not belong in this public repo.

Also banned from public GitHub:

- `data/memory/`
- `data/decisions/`
- `data/open_loops/`
- `data/context_packs/`
- `data/logs/`
- `data/notes_archive/`
- `data/sources/`
- `data/research/`
- `data/authorizations/`
- `data/approval_queue/`
- raw exports
- screenshots with private info
- API keys
- credentials
- tokens
- browser/session data
- employer information
- W2-adjacent business leads or venue/operator data

## Safety Checklist Before Any Commit

Before committing to this repo, confirm:

- No private `marshall-local-os` data is included.
- No raw ChatGPT, Claude, Apple Notes, email, browser, or document exports are included.
- No credentials, keys, tokens, or `.env` files are included.
- No financial, health, work-sensitive, or relationship context is included.
- No generated private context packs are included.
- Examples are synthetic or public-safe.
- The commit improves workflow documentation, tooling safety, or integration clarity.

## Safety Checklist Before Any Push

Before pushing to GitHub:

1. Run `git status`.
2. Review every changed file.
3. Run `git diff`.
4. Confirm no private paths appear.
5. Confirm no generated context packs are staged.
6. Confirm no personal memory/decision/open-loop data is staged.
7. Push only after review.

## AI Agent Rules

AI tools may help with this repo only under these boundaries:

- Stay inside the repo unless explicitly approved.
- Do not scan the whole computer.
- Do not access private folders.
- Do not upload local files without approval.
- Do not add cloud dependencies by default.
- Do not add a new database by default.
- Do not rewrite the architecture.
- Do not create agents with broad filesystem control.
- Show diffs before committing.
- Never push without explicit approval.

## Relationship To `marshall-local-os`

`marshall-local-os` can use ideas from this hub.

This hub can document safe patterns learned from `marshall-local-os`.

But this hub must not contain `marshall-local-os` private data.

Correct flow:

```text
private local use → extract safe pattern → document public-safe version here
```

Incorrect flow:

```text
copy private local data → push to public repo
```

## Current Phase

The current project phase is definition and safety boundary setup.

Do not add more tools until the public/private barrier is clear.

## Near-Term Roadmap

### Phase 1 — Define the hub

- Add this project definition.
- Add AGENTS.md safety rules.
- Add public/private barrier checklist.
- Add safe repo-handoff workflow.

### Phase 2 — Document proven workflows

- Repomix repo context workflow.
- Codex handoff workflow.
- Claude handoff workflow.
- ChatGPT handoff workflow.
- Review-before-sharing checklist.

### Phase 3 — Add input conversion workflow

- MarkItDown test plan.
- Safe file conversion rules.
- Approved input/output folders.
- No private bulk ingestion.

### Phase 4 — Sandbox memory experiment

- Basic Memory sandbox only.
- Non-sensitive test notes only.
- Compare against `marshall-local-os`.
- Do not replace canonical memory.

### Phase 5 — Controlled MCP layer

- Narrow folder access only.
- No whole-home-directory access.
- No credentials or private exports.
- Read-only by default.
- Explicit approval for write actions.

## Definition of Done

This project is working when it provides a safe, repeatable way to:

- prepare repos for AI tools
- package repo context
- hand off work between ChatGPT, Claude, Codex, and GitHub
- document integration experiments
- prevent private data from entering public GitHub
