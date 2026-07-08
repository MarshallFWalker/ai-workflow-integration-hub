# Public-Safe Repomix Handoff Example

## Purpose

This example shows how to package public repo context with Repomix and hand it to an AI tool without exposing private local data.

Use this when an AI tool needs more than one file of repo context, but does not need private notes, raw exports, logs, or broad local filesystem access.

## Scenario

You want an AI tool to review the public workflow docs and suggest one small improvement.

Approved source:

```text
ai-workflow-integration-hub
```

Approved files:

```text
README.md
AGENTS.md
docs/PROJECT_DEFINITION.md
docs/SCOPE.md
docs/SAFETY_CHECKLIST.md
docs/AI_CONTEXT_WORKFLOW.md
```

Not approved:

```text
private notes
private memory
raw ChatGPT exports
raw Claude exports
local logs
context packs from private projects
screenshots with personal information
credentials or tokens
marshall-local-os
```

## Safe Repomix Command Pattern

Run Repomix only from the public repo root.

Before running:

```bash
pwd
git status --short
```

Expected repo folder:

```text
ai-workflow-integration-hub
```

Example command:

```bash
npx repomix . \
  --output repomix-output.md \
  --ignore ".env,.env.*,**/.env,**/.env.*,**/data/**,**/context_packs/**,**/logs/**,**/notes_archive/**,**/exports/**,**/screenshots/**,**/*secret*,**/*token*,**/*credential*,**/*private*"
```

## Required Inspection

Before sharing the generated output with any AI tool, inspect it.

```bash
head -80 repomix-output.md
grep -ni "secret\|token\|credential\|private\|marshall-local-os" repomix-output.md || true
git status --short
```

The grep command may return safe policy language such as "private data" or "do not include credentials." That is acceptable.

Stop if it returns actual private paths, values, logs, exports, or personal records.

## Safe Handoff Prompt

```text
You are reviewing a public-safe workflow documentation repo.

Use the attached Repomix context only.

Task:
Suggest one small improvement to make the public/private boundary clearer.

Rules:
- Do not request private files.
- Do not ask for marshall-local-os.
- Do not ask for raw AI exports.
- Do not add new tools.
- Do not redesign the repo.
- Do not propose broad local filesystem access.
- Return only one proposed change and the reason.
```

## Good AI Output

```text
Proposed change:
Add a short "Never include" block near the top of README.md that lists private local data, raw exports, credentials, and marshall-local-os as prohibited.

Reason:
The README already explains the public/private boundary. A compact warning near the top would make the rule harder to miss for future AI handoffs.
```

Why this is good:

- It uses only the shared public repo context.
- It proposes one small change.
- It does not request private data.
- It does not add another tool.
- It is reversible.

## Bad AI Output

```text
Upload your private local operating system files so I can compare them against this public repo and redesign the whole system.
```

Why this is bad:

- It asks for private local files.
- It violates the public/private boundary.
- It expands scope.
- It creates a tool-chasing loop.

## Cleanup

After review, remove the temporary Repomix output unless it is intentionally kept outside git.

```bash
rm -f repomix-output.md
git status --short
```

`repomix-output.md` should not be committed by default.

## Done Rule

This workflow is successful only if the AI review uses public-safe repo context, suggests one small improvement, and does not require private data, broader access, or a new tool stack.
