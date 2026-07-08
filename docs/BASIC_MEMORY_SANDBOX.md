# Basic Memory Sandbox Experiment

## Purpose

This document defines a small, reversible experiment for testing Basic Memory as a shared memory layer for AI tools.

The goal is to evaluate whether Basic Memory improves AI handoff and retrieval without replacing the private local operating system.

## Core Rule

This is a sandbox experiment only.

Basic Memory is not canonical memory for this project.

`marshall-local-os` remains the private local source of truth for personal memory, decisions, open loops, logs, and operating state.

## Experiment Goal

Test whether a simple Markdown-based memory layer can help ChatGPT, Claude, Codex, or local AI tools retrieve project facts, decisions, and open loops from non-sensitive notes.

This test should answer:

- Does the memory layer reduce repeated context setup?
- Can it retrieve decisions accurately?
- Can it distinguish active tasks from background notes?
- Can it support multiple AI tools without adding too much friction?
- Is it simpler or more useful than the current workflow?

## Public / Private Boundary

`ai-workflow-integration-hub` is public.

`marshall-local-os` is private.

Use only synthetic or non-sensitive notes for this experiment.

Do not import private local memory, raw exports, personal logs, or generated private context packs.

## Approved Sandbox Folder

Use a separate sandbox folder, not the private system and not the public repo as canonical memory.

Suggested local folder:

```text
~/basic-memory-sandbox
```

Suggested structure:

```text
basic-memory-sandbox/
├── notes/
│   ├── project-definition.md
│   ├── tool-lane.md
│   ├── decision-log.md
│   ├── open-loops.md
│   └── safety-boundaries.md
└── README.md
```

Do not point the tool at the whole home directory.

Do not point the tool at private data folders.

## Synthetic Notes To Create

Create only test notes like these:

### `project-definition.md`

```markdown
# Project Definition

AI Workflow Integration Hub is a public repo for safe AI workflow documentation.
It is not the private local memory system.
```

### `tool-lane.md`

```markdown
# Tool Lane

Approved lane:
1. AGENTS.md
2. Repomix
3. MarkItDown
4. Basic Memory sandbox
5. One controlled MCP layer
```

### `decision-log.md`

```markdown
# Decision Log

- Decision: Keep private local memory separate from public GitHub docs.
- Decision: Test Basic Memory only with synthetic notes first.
- Decision: Do not replace canonical memory during the sandbox test.
```

### `open-loops.md`

```markdown
# Open Loops

- Write prompt templates for AI handoff.
- Test whether Basic Memory retrieves decisions accurately.
- Compare retrieval friction against existing local workflow.
```

### `safety-boundaries.md`

```markdown
# Safety Boundaries

- No private local data.
- No raw exports.
- No whole-computer scan.
- No credentials.
- No public commit of sandbox memory unless fully synthetic and reviewed.
```

## Retrieval Questions To Test

Ask the memory layer:

1. What is the project definition?
2. What is the approved tool lane?
3. What decisions have already been made?
4. What open loops remain?
5. What safety boundaries apply?
6. Is Basic Memory canonical memory for this project?
7. What should not be imported into this sandbox?

## Expected Answers

The system should answer:

- The hub is public workflow documentation.
- The private local system remains separate.
- The approved lane is AGENTS.md, Repomix, MarkItDown, Basic Memory sandbox, and controlled MCP.
- Basic Memory is sandbox-only.
- Private data must not be imported.
- Whole-computer access is not allowed.

## Comparison Criteria

Compare Basic Memory against the current local-first workflow using these criteria:

### Retrieval quality

- Does it retrieve the right note?
- Does it preserve decisions accurately?
- Does it confuse old notes with active decisions?

### Friction

- How much setup is required?
- How much manual context is still needed?
- Does it save time after the first setup?

### Safety

- Can access be limited to the sandbox folder?
- Is it clear what files are being read?
- Can private data be excluded reliably?

### Tool compatibility

- Can multiple AI tools use the same notes?
- Does it work cleanly with terminal-based workflows?
- Does it add value beyond plain Markdown plus repo context?

### Reversibility

- Can the sandbox be deleted without harming the real system?
- Does it avoid database lock-in?
- Does it keep notes human-readable?

## Pass Criteria

The experiment passes if Basic Memory:

- works with synthetic notes only
- retrieves decisions and open loops accurately
- keeps memory human-readable
- stays limited to the sandbox folder
- reduces repeated context setup
- does not require replacing `marshall-local-os`

## Fail Criteria

The experiment fails if Basic Memory:

- requires broad filesystem access
- encourages importing private data
- confuses temporary notes with canonical memory
- adds more friction than it removes
- makes source-of-truth boundaries unclear
- pushes the project toward tool-chasing

## Stop Conditions

Stop immediately if:

- the tool asks for broad filesystem access
- the tool points at private folders
- private local data appears in the sandbox
- raw exports are imported
- credentials or secret-looking strings appear
- the experiment starts replacing canonical memory
- the task drifts into building a second private operating system

## Review Questions After The Test

After testing, answer:

1. Did it retrieve the right facts?
2. Did it reduce repeated explanation?
3. Was setup easy enough to justify?
4. Did it preserve the public/private boundary?
5. Did it create any source-of-truth confusion?
6. Should it remain sandbox-only, be retired, or be tested again later?

## Decision Rule

Do not canonize Basic Memory after one test.

The only approved outcomes are:

```text
keep sandbox → test more later
retire sandbox → no action
extract public-safe lessons → document in this repo
```

Do not replace `marshall-local-os` with Basic Memory during this phase.

## Definition of Done

This experiment plan is complete when:

- the sandbox folder is clearly separated
- notes are synthetic and non-sensitive
- retrieval questions are defined
- pass/fail criteria are defined
- stop conditions are defined
- the plan does not require private data
- the plan does not replace canonical memory
