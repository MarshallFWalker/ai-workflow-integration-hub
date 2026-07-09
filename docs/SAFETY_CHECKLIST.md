# Safety Checklist

## Purpose

This checklist prevents private local data from entering the public `ai-workflow-integration-hub` repository.

Use it before every commit, push, pull request, AI handoff, repo-packaging step, or tool experiment.

## Core Rule

`ai-workflow-integration-hub` is public.

`marshall-local-os` is private.

If a file contains personal state, it stays local.

If a file teaches a reusable public-safe workflow, it can be documented here.

## Never Commit

Do not commit:

- private memories
- private decisions
- open loops
- private logs
- private context packs
- raw AI conversation exports
- private notes exports
- email exports
- browser/session exports
- screenshots with private data
- financial records
- health records
- relationship notes
- employer-sensitive information
- private work data
- `.env` files
- secret config files
- API keys
- credentials
- tokens
- `marshall-local-os/data/`
- mirrors or copies of `marshall-local-os`

## Safe To Commit

It is usually safe to commit:

- public documentation
- workflow descriptions
- prompt templates
- AGENTS.md patterns
- Repomix instructions
- MarkItDown instructions
- Basic Memory sandbox notes
- controlled MCP notes
- GitHub workflow notes
- checklists
- synthetic examples
- public-safe sample data

## Before Running an AI Tool

Confirm:

- The tool is working inside this repo only.
- The tool is not scanning the whole computer.
- The tool is not reading private folders.
- The tool is not uploading files without approval.
- The tool is not using private local data as context.
- The task is documentation or public-safe workflow design.
- The task is not drifting into `marshall-local-os` feature polish.

## Before Packaging Repo Context

Confirm:

- Only public repo files are included.
- No private context packs are included.
- No raw exports are included.
- No generated private files are included.
- No hidden local files are included.
- No private folders are included.
- Exclude rules are active before packaging.

Minimum exclude patterns:

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
```

## Before Committing

Run:

```bash
git status
git diff
```

Then confirm:

- Every changed file is expected.
- No private data appears in the diff.
- No raw exports appear in the diff.
- No credentials appear in the diff.
- No private paths appear in the diff.
- No generated private context packs are staged.
- Examples are synthetic or public-safe.
- The change improves workflow documentation, tooling safety, or integration clarity.

## Before Pushing

Run:

```bash
git status
git diff --cached
```

Then confirm:

- The branch contains only public-safe files.
- No private local system files are staged.
- No private personal context is staged.
- No accidental generated files are staged.
- No AI tool included extra files.
- The commit message is accurate.

If uncertain, stop before pushing.

## Before Creating a Pull Request

Confirm:

- The PR description does not reveal private data.
- The changed files are public-safe.
- Any examples are synthetic.
- The PR scope matches the project lane.
- The change does not add a new agent framework without a clear reason.
- The change does not expand filesystem access.

## Before Adding a New Tool

Ask:

- Does this tool support the current lane?
- Does it replace something broken, or is it tool-chasing?
- Can it run on synthetic/public-safe data first?
- Can it be tested without private data?
- Can it be removed easily?
- Does it require broad filesystem access?
- Does it require cloud upload?
- Does it require credentials?

Allowed lane:

1. AGENTS.md
2. Repomix
3. MarkItDown
4. Basic Memory sandbox
5. One controlled MCP layer

Do not add more agent frameworks unless the current lane clearly fails.

## Red Flags

Stop immediately if you see:

- `marshall-local-os/data/`
- raw AI exports
- private context packs
- screenshots with personal information
- unexpected binary files
- large unexplained files
- broad filesystem scan commands
- cloud upload commands
- credentials or secret-looking strings
- tool output copied from a private workflow
- anything that looks like personal state

## If Private Data Was Committed

Deleting the file in a new commit does not remove it. Git history keeps it.

1. Stop. Do not push. If already pushed, assume the data was seen.
2. If credentials, tokens, or keys leaked, revoke and rotate them immediately.
3. Remove the data from git history, not just the working tree, before any new push.
4. If it reached public GitHub, contact GitHub support to clear cached views.
5. Note which checklist step failed and tighten it.

## Correct Flow

```text
private local use → extract safe general pattern → document public-safe version here
```

## Incorrect Flow

```text
copy private local data → commit to public GitHub
```

## Final Decision Rule

When in doubt, do not commit it.

Document the public-safe pattern instead.
