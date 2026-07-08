# Examples

This folder contains small, public-safe workflow examples.

Examples are not private memory, not raw exports, and not templates for broad local ingestion. Each example should demonstrate one narrow workflow that can be reviewed, accepted, rejected, or removed easily.

## Current Examples

| Example | Use When | Boundary |
|---|---|---|
| [`PUBLIC_SAFE_AI_REVIEW.md`](PUBLIC_SAFE_AI_REVIEW.md) | You want an AI tool to review a small set of public repo docs. | No private files, no redesign, one proposed change. |
| [`PUBLIC_SAFE_MARKITDOWN_CONVERSION.md`](PUBLIC_SAFE_MARKITDOWN_CONVERSION.md) | You want to convert one approved file to Markdown for review. | One approved input file, one inspected Markdown output. |
| [`PUBLIC_SAFE_REPOMIX_HANDOFF.md`](PUBLIC_SAFE_REPOMIX_HANDOFF.md) | You want to package public repo context for an AI handoff. | Public repo context only, inspect before sharing. |

## Example Rules

A good example should:

- use synthetic or public-safe material only
- show the exact approved input
- show what is not approved
- include a safe prompt or command pattern
- include a bad-example warning
- include a cleanup or done rule
- stay small enough to review quickly

Do not add examples that require:

- private local folders
- whole-computer scans
- raw AI conversation exports
- credentials, tokens, or secret config
- personal, financial, health, relationship, or employer-sensitive records
- new tools outside the approved lane

## Done Rule

This folder is useful when it helps someone run a safe AI workflow without needing private data or expanding the tool stack.
