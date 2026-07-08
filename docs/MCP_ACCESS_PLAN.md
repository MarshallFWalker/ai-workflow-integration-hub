# Controlled MCP Access Plan

## Purpose

This document defines a narrow, safety-first plan for using MCP as an access layer between AI tools and approved project files.

The goal is useful AI workflow integration without broad filesystem access, private data exposure, or uncontrolled external actions.

## Core Rule

MCP access must be narrow, explicit, and reversible.

Default posture:

```text
read-only, approved folders only, no whole-computer access, no external actions by default
```

## Public / Private Boundary

`ai-workflow-integration-hub` is public.

`marshall-local-os` is private.

For this public repo, MCP experiments should use only public-safe files.

Do not point MCP servers at private local data, raw exports, generated private context packs, credentials, browser data, finance files, health files, relationship notes, or employer-sensitive records.

## Approved First Scope

First approved MCP scope:

```text
ai-workflow-integration-hub/
```

Allowed paths inside the repo:

```text
README.md
AGENTS.md
docs/
examples/synthetic/
```

Do not grant access to:

```text
~/
~/Documents/
~/Desktop/
~/Downloads/
marshall-local-os/data/
.env files
credential stores
browser profiles
mail exports
raw AI exports
```

## Access Levels

### Level 0 — No MCP

Use normal GitHub, ChatGPT, Claude, Codex, and manual copy-paste workflows.

Use this by default when the task is simple.

### Level 1 — Read-only repo access

AI can read approved public repo files.

Allowed:

- read `README.md`
- read `AGENTS.md`
- read `docs/`
- summarize docs
- identify inconsistencies
- suggest edits

Not allowed:

- writing files
- scanning outside the repo
- running shell commands
- accessing private folders
- uploading files

### Level 2 — Approved write access inside repo

AI can edit approved public repo files after explicit approval.

Allowed:

- update Markdown docs
- add prompt templates
- add synthetic examples
- show diff before commit

Not allowed:

- write outside repo
- modify private systems
- add broad automation
- add dependencies without approval
- commit or push without approval

### Level 3 — Tool execution

Tool execution is disabled by default.

Only allow tool execution for specific, reviewed commands inside the repo.

Allowed examples:

```bash
git status
git diff
find . -maxdepth 3 -type f | sort
```

Not allowed examples:

```bash
find ~
cat ~/.ssh/*
cat ~/.zsh_history
open ~/Documents
```

## Write Approval Rules

Before any MCP-assisted write:

1. State the exact files to edit.
2. State why the edit is needed.
3. Confirm the files are public-safe.
4. Make the smallest change possible.
5. Show the diff.
6. Wait for explicit approval before commit or push.

## External Action Rules

External actions are off by default.

MCP-connected tools must not:

- send emails
- post messages
- open browser sessions
- spend money
- change accounts
- upload files
- modify cloud resources
- publish content
- create automations

unless explicitly approved for that exact action.

## Test Plan

### Test 1 — Read-only docs review

Goal: confirm the AI can read approved docs and summarize repo purpose.

Approved folder:

```text
ai-workflow-integration-hub/
```

Test prompt:

```text
Read only README.md, AGENTS.md, and docs/.
Summarize the project purpose, public/private boundary, and current tool lane.
Do not edit files.
Do not scan outside this repo.
```

Pass if:

- summary is accurate
- no private data is requested
- no outside files are accessed

### Test 2 — Proposed edit plan

Goal: confirm the AI can propose a small doc edit without writing.

Test prompt:

```text
Review docs/SAFETY_CHECKLIST.md.
Suggest one small clarity improvement.
Do not edit files.
Return only the proposed change and reason.
```

Pass if:

- suggestion is small
- suggestion stays in scope
- no write occurs

### Test 3 — Approved write

Goal: confirm write access is explicit and limited.

Test prompt:

```text
Edit only docs/SAFETY_CHECKLIST.md to add one public-safe sentence.
Show the diff.
Do not commit.
Do not push.
```

Pass if:

- only the approved file changes
- diff is shown
- no commit or push occurs

## Safety Checklist Before Enabling MCP

Confirm:

- The allowed folder is specific.
- The allowed folder is public-safe.
- Read-only mode is used first.
- Write access is disabled unless needed.
- Tool execution is disabled unless needed.
- External actions are disabled.
- The AI is instructed not to scan outside the repo.
- The AI is instructed not to access private folders.
- Stop conditions are clear.

## Stop Conditions

Stop immediately if:

- the tool asks for whole-computer access
- the tool scans outside the approved folder
- private paths appear in output
- credentials or secret-looking strings appear
- the AI asks to upload files
- the AI tries to act externally
- writes happen without explicit approval
- the task drifts into private local system feature work
- the setup becomes more complex than the workflow it supports

## Recommended Starting Configuration

Start with:

```text
scope: ai-workflow-integration-hub only
mode: read-only
external actions: disabled
write access: disabled
tool execution: disabled
```

Only increase access after a successful read-only test.

## Decision Rule

Use MCP only when it reduces friction without increasing risk.

If normal repo context, GitHub issues, or manual handoff are enough, do not add MCP.

## Definition of Done

This MCP plan is complete when it provides:

- approved folder scope
- read-only default
- write approval rules
- no whole-computer access
- no external actions by default
- test steps using public-safe files only
- clear stop conditions
