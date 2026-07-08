# Repomix Repo-Context Workflow

## Purpose

This document explains how to use Repomix, or an equivalent repo-packing tool, to prepare public-safe repository context for ChatGPT, Claude, Codex, and local AI tools.

The goal is better AI handoff without exposing private local data.

## What Repomix Is For

Use Repomix when an AI tool needs to understand a repo's structure, docs, prompts, scripts, or workflow rules.

Good uses:

- asking ChatGPT to review project scope
- asking Claude to improve documentation structure
- asking Codex to make small repo edits
- preparing a compact repo overview
- checking whether instructions are duplicated or stale
- handing off an issue with enough context

Bad uses:

- packaging a whole computer
- packaging private local systems
- packaging raw exports
- packaging personal state
- packaging generated private context packs
- packaging files before inspection

## Public / Private Boundary

`ai-workflow-integration-hub` is public.

`marshall-local-os` is private.

Correct pattern:

```text
public repo files → package context → inspect output → hand off to AI
```

Incorrect pattern:

```text
private local data → package context → upload or commit publicly
```

## Approved Input

For this repo, Repomix may include:

- `README.md`
- `AGENTS.md`
- `docs/PROJECT_DEFINITION.md`
- `docs/SCOPE.md`
- `docs/SAFETY_CHECKLIST.md`
- `docs/AI_CONTEXT_WORKFLOW.md`
- `docs/AI_HANDOFF_PROMPTS.md`
- `docs/REPOMIX_WORKFLOW.md`
- `docs/MARKITDOWN_WORKFLOW.md`
- `docs/BASIC_MEMORY_SANDBOX.md`
- `docs/MCP_ACCESS_PLAN.md`
- future public-safe prompt templates
- future public-safe workflow docs
- synthetic examples only

Use the smallest useful file set for the current issue. Do not include generated context packages by default.

## Required Excludes

Always exclude:

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

## Before Running Repomix

Confirm:

- You are inside the correct repo.
- The repo is public-safe.
- No private local folders are inside the repo.
- No generated private context packs are present.
- No raw exports are present.
- No unexpected large files are present.
- `AGENTS.md` and `docs/SAFETY_CHECKLIST.md` have been reviewed.

Recommended checks:

```bash
git status
find . -maxdepth 3 -type f | sort
```

## Safe Example Command

Example only. Review the actual Repomix options before running.

```bash
npx repomix . \
  --output repomix-output.md \
  --ignore ".env,.env.*,**/.env,**/.env.*,**/data/**,**/context_packs/**,**/logs/**,**/notes_archive/**,**/exports/**,**/screenshots/**,**/*secret*,**/*token*,**/*credential*,**/*private*"
```

Do not run this from your home directory.

Do not run this against private local systems unless the output is staying local and has been explicitly approved.

## Inspect The Output

After generating a context package, inspect it before sharing.

Run:

```bash
head -80 repomix-output.md
grep -n "marshall-local-os/data" repomix-output.md || true
grep -ni "secret\|token\|credential\|private" repomix-output.md || true
```

Also manually scan the file list at the top of the output.

Do not share the package if anything unexpected appears.

## Handoff Prompt

Use this with ChatGPT, Claude, or Codex after inspection:

```text
You are reviewing the public AI Workflow Integration Hub repo.
Use only the provided public-safe repo context.
Do not ask for private local data.
Do not expand scope into a new agent stack.
Identify the smallest useful improvement for the current issue.
Respect AGENTS.md, the safety checklist, and the public/private boundary.
```

## Stop Conditions

Stop immediately if:

- the package includes unexpected files
- the package includes raw exports
- the package includes private paths
- the package includes generated private context packs
- the package includes personal state
- the command is being run from the wrong folder
- an AI tool asks for broader filesystem access
- the workflow starts drifting into private local system feature polish

## Review Before Commit

Generated context packages should usually not be committed.

Before committing anything related to Repomix, run:

```bash
git status
git diff
```

Confirm:

- no generated context package is staged unless intentionally public-safe
- no private path appears in the diff
- no raw exports appear in the diff
- no secret-looking strings appear in the diff
- documentation changes are the only intended changes

## Recommended Repo Policy

Default policy:

```text
Repomix output is temporary handoff material, not source material.
```

Only commit generated context packages if they are synthetic, small, intentional, and public-safe.

## Definition of Done

A Repomix workflow is successful when:

- the AI tool receives enough repo context to help
- the context is public-safe
- the output was inspected before sharing
- no private data was exposed
- the next action stays inside the current issue scope
