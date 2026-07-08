# AI Handoff Prompt Templates

## Purpose

These templates help move public-safe work between ChatGPT, Claude, Codex, GitHub, and local AI tools without losing scope or exposing private local data.

Use these prompts when working on this public repo or another public-safe project.

## Core Boundary

`ai-workflow-integration-hub` is public.

`marshall-local-os` is private.

Use only public-safe repo context unless explicitly approved otherwise.

Do not ask an AI tool to use private local memory, raw exports, personal logs, or generated private context packs for this public repo.

## Universal Handoff Rules

Add this block to any handoff prompt:

```text
Use only the provided public-safe repo context.
Respect AGENTS.md and the safety checklist.
Do not ask for private local data.
Do not scan outside the approved repo.
Do not expand this into a new agent framework.
Keep the next step small, reversible, and issue-scoped.
Show a concise plan before making changes.
```

## ChatGPT — Strategy And Scope Review

Use ChatGPT when you need project direction, prioritization, safety review, or loop prevention.

```text
You are reviewing the public AI Workflow Integration Hub repo.

Goal:
Help choose the smallest useful next step for the current GitHub issue.

Context:
Use only the provided public-safe repo context.
Respect PROJECT_DEFINITION.md, SCOPE.md, AGENTS.md, SAFETY_CHECKLIST.md, and AI_CONTEXT_WORKFLOW.md.

Rules:
- Do not ask for private local data.
- Do not expand this into a new agent stack.
- Do not suggest adding tools unless the current lane clearly fails.
- Keep recommendations issue-scoped.
- Prefer a small documentation or workflow improvement over architecture changes.

Output:
1. One-sentence diagnosis.
2. The smallest next action.
3. Any safety concern.
4. Stop condition if the task starts drifting.
```

## Claude — Documentation Review

Use Claude when you want large-context review, clearer wording, better structure, or ambiguity cleanup.

```text
You are reviewing public-safe documentation for the AI Workflow Integration Hub repo.

Goal:
Improve clarity, structure, and safety boundaries without expanding scope.

Context:
Use only the provided repo docs and issue description.

Rules:
- Do not add private-data assumptions.
- Do not introduce a new memory system.
- Do not introduce a new agent framework.
- Preserve the public/private boundary.
- Keep examples synthetic or public-safe.
- Return a concise diff plan before edits.

Output:
1. What is unclear.
2. What should change.
3. What should stay unchanged.
4. Proposed Markdown patch or section outline.
```

## Codex — Small Repo Edit

Use Codex for small file changes, Markdown updates, script stubs, and diff review.

```text
Work only inside this repository.

Goal:
Complete GitHub issue #<ISSUE_NUMBER> with the smallest safe change.

Rules:
- Read AGENTS.md first.
- Read docs/SAFETY_CHECKLIST.md before editing.
- Do not scan outside this repo.
- Do not add dependencies.
- Do not upload anything.
- Do not create broad automation.
- Do not add private local data.
- Keep changes small and reversible.
- Show git diff and git status before commit.
- Do not commit or push without approval.

Task:
<PASTE ISSUE BODY HERE>

Output:
1. Files changed.
2. Summary of edits.
3. Safety check.
4. git diff.
5. git status.
```

## GitHub Issue-To-PR Workflow

Use this when turning an open issue into a branch and pull request.

```text
You are working in the public AI Workflow Integration Hub repo.

Issue:
#<ISSUE_NUMBER> — <ISSUE_TITLE>

Goal:
Create a small public-safe change that closes the issue.

Rules:
- Keep the PR limited to the issue scope.
- Do not include private local data.
- Do not add generated context packages unless explicitly intended and public-safe.
- Update docs only unless code is clearly required.
- Link the PR to the issue.
- Include a short safety note in the PR description.

PR description format:
## Summary
- ...

## Safety
- Uses public-safe docs only.
- Does not include private local data.
- Does not expand repo scope.

Closes #<ISSUE_NUMBER>
```

## Local AI Tool Handoff

Use this for local AI tools when working with approved public folders.

```text
Use only this approved project folder.
Do not scan the home directory.
Do not access private folders.
Do not call external services.
Do not modify files unless explicitly approved.

Goal:
Review the public-safe repo context and suggest the smallest next improvement.

Output:
- Summary of relevant files reviewed.
- One recommended next action.
- Any safety concern.
```

## Review Prompt For Generated Repo Context

Use this after creating a repo context package and inspecting it locally.

```text
Review this public-safe repo context.

Goal:
Find gaps, stale instructions, duplicated guidance, and the smallest useful next improvement.

Rules:
- Use only the provided context.
- Do not ask for private local data.
- Do not expand scope.
- Do not recommend new tools unless necessary.
- Prioritize safety, clarity, and usefulness.

Output:
1. What is strong.
2. What is missing.
3. What is risky or unclear.
4. One next action.
```

## Stop Conditions

Stop the handoff if:

- the AI asks for broad filesystem access
- the AI asks for private local data
- the AI suggests replacing the private system
- the AI suggests adding another major agent framework without a clear failure
- the AI starts solving a different project
- the AI output includes unexpected private details

## Default Decision Rule

If the work is about reusable public-safe workflows, continue in this repo.

If the work is about personal memory, decisions, logs, or operating state, it belongs in the private local system instead.
