# AI Workflow Integration Hub

AI Workflow Integration Hub is a public repo for safe, repeatable workflows between ChatGPT, Claude, Codex, GitHub, local AI tools, and local-first projects.

The goal is simple: make AI collaboration easier without exposing private local data or building another oversized agent stack.

## Start Here

Read these first:

1. [`docs/PROJECT_DEFINITION.md`](docs/PROJECT_DEFINITION.md) — what this project is and what it is not
2. [`docs/SCOPE.md`](docs/SCOPE.md) — approved scope, out-of-scope work, and roadmap
3. [`AGENTS.md`](AGENTS.md) — rules for Codex, Claude, ChatGPT, and other AI agents
4. [`docs/SAFETY_CHECKLIST.md`](docs/SAFETY_CHECKLIST.md) — pre-commit, pre-push, and AI handoff safety checks
5. [`docs/AI_CONTEXT_WORKFLOW.md`](docs/AI_CONTEXT_WORKFLOW.md) — how to prepare repo context for AI tools safely
6. [`docs/AI_HANDOFF_PROMPTS.md`](docs/AI_HANDOFF_PROMPTS.md) — copy-paste prompts for ChatGPT, Claude, Codex, GitHub, and local AI
7. [`docs/REPOMIX_WORKFLOW.md`](docs/REPOMIX_WORKFLOW.md) — public-safe repo context packaging workflow
8. [`docs/MARKITDOWN_WORKFLOW.md`](docs/MARKITDOWN_WORKFLOW.md) — safe file-to-Markdown conversion workflow
9. [`docs/BASIC_MEMORY_SANDBOX.md`](docs/BASIC_MEMORY_SANDBOX.md) — sandbox-only Basic Memory experiment plan
10. [`docs/MCP_ACCESS_PLAN.md`](docs/MCP_ACCESS_PLAN.md) — controlled MCP access plan
11. [`docs/MCP_HOST_SETUP_NOTES.md`](docs/MCP_HOST_SETUP_NOTES.md) — MCP host test results and retry plan

## What This Repo Is

This repo is a public workflow hub for:

- AI handoff patterns
- prompt templates
- repo-context workflows
- AGENTS.md patterns
- Repomix workflows
- MarkItDown workflows
- Basic Memory sandbox planning
- controlled MCP planning
- GitHub issue and PR workflows
- synthetic public-safe examples

## What This Repo Is Not

This repo is not a private memory system.

It must not contain:

- personal memories
- private decisions
- open loops
- private logs
- raw AI conversation exports
- generated private context packs
- financial, health, relationship, or employer-sensitive records
- credentials, tokens, or secret configuration files
- mirrors or copies of private local systems

## Public / Private Boundary

`ai-workflow-integration-hub` is public.

`marshall-local-os` is private.

Correct pattern:

```text
private local use → extract safe general pattern → document public-safe workflow here
```

Incorrect pattern:

```text
copy private local data → commit to public GitHub
```

## Current Tool Lane

The approved lane is:

1. AGENTS.md
2. Repomix
3. MarkItDown
4. Basic Memory sandbox
5. One controlled MCP layer

Do not add more agent frameworks unless the current lane clearly fails.

## Repo Map

```text
.
├── AGENTS.md
├── README.md
└── docs/
    ├── AI_CONTEXT_WORKFLOW.md
    ├── AI_HANDOFF_PROMPTS.md
    ├── BASIC_MEMORY_SANDBOX.md
    ├── MARKITDOWN_WORKFLOW.md
    ├── MCP_ACCESS_PLAN.md
    ├── MCP_HOST_SETUP_NOTES.md
    ├── PROJECT_DEFINITION.md
    ├── REPOMIX_WORKFLOW.md
    ├── SAFETY_CHECKLIST.md
    ├── SCOPE.md
    └── examples/
        ├── PUBLIC_SAFE_AI_REVIEW.md
        └── PUBLIC_SAFE_REPOMIX_HANDOFF.md
```

## Examples

Start with:

- [`docs/examples/PUBLIC_SAFE_AI_REVIEW.md`](docs/examples/PUBLIC_SAFE_AI_REVIEW.md) — a small public-safe AI review workflow
- [`docs/examples/PUBLIC_SAFE_REPOMIX_HANDOFF.md`](docs/examples/PUBLIC_SAFE_REPOMIX_HANDOFF.md) — a safe Repomix-to-AI handoff workflow

Examples should stay synthetic, narrow, and reversible.

## Completed Foundation

The first workflow foundation is complete:

1. README quickstart and repo map
2. Repomix repo-context workflow
3. AI handoff prompt templates
4. MarkItDown conversion workflow
5. Basic Memory sandbox experiment plan
6. Controlled MCP access plan
7. MCP host setup notes and retry plan
8. Public-safe AI review example
9. Public-safe Repomix handoff example

Next work should be issue-scoped cleanup, testing, or public-safe examples. Do not add new tools until the current lane has been tested.

## Default Workflow

Before adding anything:

1. Confirm the work belongs in the public hub.
2. Check `AGENTS.md`.
3. Check `docs/SAFETY_CHECKLIST.md`.
4. Keep examples synthetic or public-safe.
5. Review the diff before committing.

## Success Criteria

This repo is working when it provides a safe, repeatable way to:

- prepare repos for AI collaboration
- package repo context for ChatGPT, Claude, Codex, and local AI tools
- document integration experiments
- prevent private data from entering public GitHub
- avoid tool-chasing and scope creep
