# AI Context Workflow

## Purpose

This workflow explains how to safely prepare repo context for ChatGPT, Claude, Codex, GitHub, and local AI tools.

The goal is to make AI collaboration easier without exposing private local data.

## Core Rule

Only package public-safe repo context.

Do not package private memory, raw exports, personal logs, generated private context packs, screenshots with private information, or anything from `marshall-local-os/data/`.

## Approved Flow

```text
choose public-safe repo files → review include/exclude rules → package context → inspect output → hand off to AI tool
```

Never skip the inspection step.

## Public / Private Boundary

`ai-workflow-integration-hub` is public.

`marshall-local-os` is private.

Correct pattern:

```text
private local use → extract safe general pattern → document public-safe workflow here
```

Incorrect pattern:

```text
copy private local data → package context → upload or commit publicly
```

## When To Use This Workflow

Use this workflow when asking an AI tool to:

- understand a repo
- review documentation
- improve AGENTS.md
- draft prompt templates
- identify workflow gaps
- suggest safe next steps
- review public-safe examples
- compare integration patterns

Do not use this workflow for private personal memory, finances, health, relationship notes, employer-sensitive information, or raw exports.

## Minimum Context Package

A useful public-safe AI context package should usually include:

- README.md
- AGENTS.md
- docs/PROJECT_DEFINITION.md
- docs/SCOPE.md
- docs/SAFETY_CHECKLIST.md
- docs/AI_CONTEXT_WORKFLOW.md
- relevant prompt templates
- relevant workflow docs
- synthetic examples only

## Exclude Patterns

Before packaging context, exclude:

```text
.env
.env.*
**/.env
**/.env.*
**/data/**
**/context_packs/**
**/logs/**
**/notes_archive/**
**/exports/**
**/screenshots/**
**/*secret*
**/*token*
**/*credential*
**/*private*
```

## Repomix Workflow

Repomix or equivalent repo-packing tools may be used only on public-safe repos or approved folders.

Safe process:

1. Confirm you are in the correct public repo.
2. Review `AGENTS.md`.
3. Review `docs/SAFETY_CHECKLIST.md`.
4. Apply exclude patterns.
5. Generate the context package.
6. Open the generated output.
7. Search the output for private terms and paths.
8. Only then share with an AI tool.

Example review commands:

```bash
git status
git diff
```

Example private-path checks:

```bash
grep -R "marshall-local-os/data" .
grep -R "BEGIN PRIVATE" .
```

Do not run packaging against the whole home directory.

## ChatGPT Handoff

Use ChatGPT for:

- project direction
- scope control
- safety review
- workflow design
- documentation drafting
- next-step selection
- loop prevention

Good handoff prompt:

```text
You are reviewing the public AI Workflow Integration Hub repo.
Use only the provided public-safe context.
Do not ask for private local data.
Identify the smallest next improvement that strengthens safe AI handoff.
Avoid adding new tools unless the current lane clearly fails.
```

## Claude Handoff

Use Claude for:

- large-context review
- documentation cleanup
- conceptual restructuring
- identifying ambiguity
- drafting safer workflow language

Good handoff prompt:

```text
Review this public-safe repo context.
Improve clarity, safety boundaries, and workflow usefulness.
Do not add private-data assumptions.
Do not expand scope into a new agent platform.
Return a concise diff plan before suggesting edits.
```

## Codex Handoff

Use Codex for:

- small file changes
- docs edits
- shell script stubs
- tests if code exists
- reviewing diffs before commit

Good handoff prompt:

```text
Work only inside this repository.
Do not scan outside the repo.
Do not add dependencies.
Do not upload anything.
Keep changes small.
Show git diff and git status before commit.
Do not commit or push without approval.
```

## GitHub Handoff

Use GitHub for:

- public docs
- issues
- pull requests
- project tracking
- safe workflow templates
- non-private examples

Do not use GitHub as the private memory source of truth.

## Local AI Handoff

Use local AI tools only with approved public-safe folders unless explicitly testing a private local workflow.

For this public repo, local AI should:

- stay inside the repo
- use synthetic examples
- avoid broad filesystem access
- avoid external actions
- avoid private context ingestion

## Inspection Checklist

Before sharing a context package with any AI tool, confirm:

- No private data appears.
- No raw exports appear.
- No secret-looking strings appear.
- No private file paths appear.
- No generated private context packs appear.
- No screenshots with private information appear.
- Examples are synthetic or public-safe.
- The context supports the current task.

## Stop Conditions

Stop if:

- the output includes `marshall-local-os/data/`
- the output includes raw exports
- the output includes personal state
- the tool wants broad filesystem access
- the task starts drifting into private local system feature polish
- the package includes files you did not expect

## Decision Rule

If context is needed but private data would be exposed, do not include the private data.

Instead:

```text
summarize the public-safe pattern → remove personal details → document the generalized workflow
```

## Definition of Done

A context handoff is successful when:

- the AI tool understands the repo goal
- the AI tool has enough public-safe context to help
- no private data was exposed
- the output is actionable
- the next step stays inside the approved lane
