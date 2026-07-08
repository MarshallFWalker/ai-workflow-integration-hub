# AI Workflow Integration Hub — Scope

## Mission

AI Workflow Integration Hub is a public GitHub repo for documenting safe, repeatable workflows between ChatGPT, Claude, Codex, GitHub, local AI tools, and local-first projects.

Its purpose is to improve AI handoff, repo context sharing, prompt reuse, and tool integration without exposing private personal data or creating another oversized agent stack.

## Primary Goal

Create a clean public workflow hub that answers:

- How do I prepare a repo for AI tools?
- How do I package repo context safely?
- How do I hand off work between ChatGPT, Claude, Codex, and GitHub?
- How do I test tools like Repomix, MarkItDown, Basic Memory, and MCP without overbuilding?
- How do I keep private local data out of public GitHub?

## Approved Scope

This repo may include:

- AGENTS.md patterns
- AI handoff instructions
- prompt templates
- repo context packaging workflows
- Repomix documentation
- MarkItDown documentation
- Basic Memory sandbox notes
- controlled MCP notes
- GitHub workflow notes
- safety checklists
- synthetic examples
- public-safe integration experiments

## Out of Scope

This repo must not include:

- personal memory
- private decisions
- open loops
- private logs
- financial records
- health records
- relationship notes
- employer-sensitive information
- raw ChatGPT exports
- raw Claude exports
- screenshots with private data
- `.env` files
- API keys
- credentials
- private context packs
- `marshall-local-os/data/`
- any mirror of `marshall-local-os`

## Public / Private Boundary

`ai-workflow-integration-hub` is public.

`marshall-local-os` is private.

Correct pattern:

```text
private local use → extract safe general pattern → document public-safe version
```

Incorrect pattern:

```text
copy local private data → commit to public GitHub
```

## Tool Lane

The approved tool lane is:

1. AGENTS.md
2. Repomix
3. MarkItDown
4. Basic Memory sandbox
5. One controlled MCP layer

Do not add more agent frameworks unless there is a clear failure in the current lane.

## Near-Term Deliverables

### Phase 1 — Safety Foundation

- PROJECT_DEFINITION.md
- SCOPE.md
- AGENTS.md
- public/private safety checklist
- commit and push checklist

### Phase 2 — AI Handoff Workflows

- ChatGPT handoff workflow
- Claude handoff workflow
- Codex handoff workflow
- GitHub issue/PR workflow
- repo context packaging workflow

### Phase 3 — Repo Context Tools

- Repomix workflow
- safe include/exclude rules
- example context pack using synthetic data only

### Phase 4 — Input Conversion

- MarkItDown workflow
- approved input/output folders
- no private bulk ingestion
- synthetic examples only

### Phase 5 — Memory Sandbox

- Basic Memory test notes
- non-sensitive sandbox only
- comparison against `marshall-local-os`
- no replacement of canonical private memory

### Phase 6 — Controlled MCP

- narrow folder access
- read-only default
- no whole-computer access
- no credentials
- explicit approval for writes

## Success Criteria

This repo is successful when it provides a safe, repeatable way to:

- prepare projects for AI collaboration
- package repo context for AI tools
- move work between ChatGPT, Claude, Codex, and GitHub
- document AI workflow experiments
- avoid tool-chasing
- prevent private data from entering public repos

## Main Risk

The main risk is confusing the public workflow hub with the private local operating system.

When in doubt:

```text
If it contains personal state, it stays local.
If it teaches a reusable public-safe workflow, it can go in the hub.
```
