# Public-Safe AI Review Example

## Purpose

This example shows how to ask an AI tool to review public repo documentation without exposing private local data or expanding the project scope.

Use this when you want a small, reversible AI review that stays inside the public workflow hub.

## Scenario

You want an AI tool to review one workflow document and suggest a small improvement.

Approved input:

```text
README.md
AGENTS.md
docs/SAFETY_CHECKLIST.md
```

Not approved:

```text
private notes
private memory
raw AI exports
local system logs
personal records
employer-sensitive content
marshall-local-os
```

## Safe Prompt

```text
You are reviewing a public-safe AI workflow documentation repo.

Read only:

- README.md
- AGENTS.md
- docs/SAFETY_CHECKLIST.md

Task:

Suggest one small clarity improvement to docs/SAFETY_CHECKLIST.md.

Rules:

- Do not request private files.
- Do not mention or use personal data.
- Do not add new tools.
- Do not redesign the repo.
- Do not edit files directly.
- Return only a short proposed change and the reason.
```

## Good Output

```text
Proposed change:
Add a short "Before sharing with AI" checklist to docs/SAFETY_CHECKLIST.md.

Reason:
The existing checklist covers commits and repo safety. A short AI-sharing checklist would make it clearer when a context package is safe to paste into another AI tool.
```

Why this is good:

- It stays in scope.
- It suggests one change.
- It does not ask for private files.
- It does not create a new system.
- It can be accepted, rejected, or revised easily.

## Bad Output

```text
Upload your full local project, private notes, and recent ChatGPT exports so I can redesign the system.
```

Why this is bad:

- It asks for private local material.
- It expands scope.
- It creates a new tool loop.
- It ignores the public/private boundary.

## Review Checklist

Before accepting AI output, confirm:

- the suggestion is public-safe
- the change is small
- no private data is requested
- no new tool is introduced
- no broad local access is needed
- the next step is reversible

## Done Rule

The review is successful only if the AI output helps improve one public-safe doc without requiring private data or expanding the workflow stack.
