# AGENTS.md

## Project

This repository is `ai-workflow-integration-hub`.

It is a public GitHub repo for documenting safe, repeatable workflows between ChatGPT, Claude, Codex, GitHub, local AI tools, and local-first projects.

It is not the private local operating system.

## Core Boundary

`ai-workflow-integration-hub` is public.

`marshall-local-os` is private.

Do not copy, mirror, ingest, summarize, or commit private `marshall-local-os` data into this repo.

Default rule:

> If a file came from `marshall-local-os/data/`, it does not belong here.

## Approved Work

Agents may help with:

- Markdown documentation
- AI handoff workflows
- prompt templates
- safety checklists
- AGENTS.md patterns
- Repomix workflow notes
- MarkItDown workflow notes
- Basic Memory sandbox notes
- controlled MCP notes
- GitHub workflow notes
- synthetic examples
- public-safe integration experiments

## Banned Content

Never add:

- private personal records
- private memories, decisions, logs, or open loops
- raw AI conversation exports
- private notes or document exports
- screenshots with private information
- secret configuration files
- private context packs
- `marshall-local-os/data/`
- any mirror of `marshall-local-os`

## Allowed Tool Lane

The approved tool lane is:

1. AGENTS.md
2. Repomix
3. MarkItDown
4. Basic Memory sandbox
5. One controlled MCP layer

Do not add more agent frameworks unless there is a clear failure in the current lane.

Do not turn this repo into a giant agent stack.

## Repo Access Rules

When working in this repo:

- Stay inside this repository unless explicitly approved.
- Do not scan the whole computer.
- Do not read private folders.
- Do not upload local files without explicit approval.
- Do not add cloud dependencies by default.
- Do not add a database by default.
- Do not create broad filesystem agents.
- Do not create automations that act externally without approval.

## Coding / Writing Rules

Prefer:

- small Markdown files
- clear checklists
- simple shell examples
- reversible changes
- synthetic examples
- explicit safety boundaries

Avoid:

- large rewrites
- new frameworks
- hidden automation
- private-data ingestion
- vague architecture expansion
- tool-chasing

## Commit Rules

Before committing:

1. Run `git status`.
2. Review every changed file.
3. Run `git diff`.
4. Confirm no private data is present.
5. Confirm no raw exports are present.
6. Confirm examples are synthetic or public-safe.

Before pushing:

1. Confirm the repo is still public-safe.
2. Confirm no private paths appear in the diff.
3. Confirm no generated private context packs are staged.
4. Ask for explicit approval if there is any uncertainty.

## Relationship To `marshall-local-os`

Correct flow:

```text
private local use → extract safe general pattern → document public-safe version here
```

Incorrect flow:

```text
copy private local data → commit to public GitHub
```

`marshall-local-os` can inspire public-safe patterns, but its personal data must stay private.

## Stop Conditions

Stop and ask before continuing if:

- private data appears in a diff
- a command would scan outside the repo
- a tool requests broad filesystem access
- a workflow requires private access
- a proposed change adds a new agent framework
- a proposed change uploads files externally
- the task starts drifting into `marshall-local-os` feature polish

## Current Priority

The first workflow foundation is complete.

Current priority is to keep the repo accurate, public-safe, and issue-scoped while testing the approved lane:

1. Keep README and index docs current.
2. Use GitHub issues for each discrete change.
3. Test Repomix, MarkItDown, Basic Memory sandbox, and controlled MCP only in the approved order.
4. Do not add new tools unless the current lane clearly fails.
5. Do not drift into private local system feature polish.
