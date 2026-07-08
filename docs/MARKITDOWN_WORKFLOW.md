# MarkItDown Conversion Workflow

## Purpose

This document explains how to safely use MarkItDown, or an equivalent file-to-Markdown converter, to turn approved files into Markdown for AI review.

The goal is to make messy files easier for ChatGPT, Claude, Codex, and local AI tools to reason over without turning this repo into a private data ingestion system.

## What MarkItDown Is For

Use MarkItDown when a file needs to become plain Markdown before review, summarization, or repo documentation.

Good uses:

- converting public-safe PDFs into Markdown
- converting public-safe docs into Markdown
- converting public-safe slide decks into Markdown
- converting public-safe spreadsheets into Markdown summaries
- converting synthetic examples for testing
- preparing public workflow documentation

Bad uses:

- bulk-ingesting private files
- converting raw AI conversation exports into a public repo
- converting personal notes into a public repo
- converting financial, health, relationship, or employer-sensitive records
- converting files without inspecting the output
- using conversion as a substitute for deciding what is safe to share

## Public / Private Boundary

`ai-workflow-integration-hub` is public.

`marshall-local-os` is private.

Correct pattern:

```text
approved public-safe file → convert to Markdown → inspect output → use in public workflow doc
```

Incorrect pattern:

```text
private local files → bulk convert → commit to public GitHub
```

## Approved Inputs

For this repo, approved inputs are:

- public documentation
- public-safe PDFs
- public-safe docs
- public-safe slide decks
- public-safe spreadsheets
- synthetic sample files
- test files created specifically for this repo

Do not use private local files as source material for public examples.

## Approved Outputs

Approved outputs may go in:

```text
docs/
examples/synthetic/
```

Only commit converted output if it is:

- intentionally public-safe
- reviewed manually
- useful for this repo
- small enough to inspect
- free of private details

## Recommended Folder Pattern

Use a clear staging pattern:

```text
input/public-safe/       # approved source files only
output/markdown-review/  # generated Markdown for inspection
examples/synthetic/      # committed examples only if synthetic/public-safe
```

Generated conversion output should usually stay temporary unless intentionally curated.

## Before Converting

Confirm:

- The source file is approved for public-safe use.
- The file is not a raw export.
- The file does not contain personal state.
- The file does not contain private records.
- The file does not contain employer-sensitive information.
- The file does not contain credentials or secrets.
- The conversion output will be inspected before use.

## Safe Example Command

Example only. Review actual installed MarkItDown options before running.

```bash
markitdown input/public-safe/example.pdf > output/markdown-review/example.md
```

Do not run conversion across broad folders.

Avoid commands like:

```bash
markitdown ~/Documents/**
```

## Inspect The Output

After conversion, inspect the output before using or committing it.

Run:

```bash
head -80 output/markdown-review/example.md
grep -ni "secret\|token\|credential\|private" output/markdown-review/example.md || true
grep -n "marshall-local-os/data" output/markdown-review/example.md || true
```

Also manually review the full file if it is short.

For long files, review the beginning, headings, file references, tables, and any extracted metadata.

## Conversion Review Checklist

Before using converted Markdown, confirm:

- The source file was approved.
- The output contains only expected content.
- No private paths appear.
- No personal state appears.
- No raw exports appear.
- No secret-looking strings appear.
- No unexpected metadata appears.
- Any examples are synthetic or public-safe.
- The output supports the current issue or workflow.

## Commit Rules

Before committing converted Markdown:

```bash
git status
git diff
```

Confirm:

- the converted file belongs in this public repo
- the file is intentionally included
- the file is not a generated dump
- the content was manually inspected
- the file improves documentation, testing, or workflow clarity

Default rule:

```text
converted output is temporary review material unless curated into a public-safe example
```

## Handoff Prompt

After converting and inspecting a public-safe file, use this prompt with an AI tool:

```text
You are reviewing converted Markdown from an approved public-safe file.
Use only the provided content.
Do not infer private context.
Do not ask for private source files.
Summarize what is useful for the current repo issue.
Flag anything that looks unsafe, irrelevant, or out of scope.
```

## Stop Conditions

Stop immediately if:

- the source file was not explicitly approved
- the conversion output includes unexpected private content
- the output includes raw exports
- the output includes personal state
- the output includes credentials or secret-looking strings
- the conversion command targets a broad folder
- the workflow becomes bulk ingestion
- the task drifts away from public-safe workflow documentation

## Definition of Done

A MarkItDown workflow is successful when:

- the source file was approved
- the output was inspected
- only public-safe content was used
- any committed examples are synthetic or curated
- no private data entered the public repo
- the conversion helped a specific workflow or issue
