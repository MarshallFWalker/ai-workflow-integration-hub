# Public-Safe MarkItDown Conversion Example

## Purpose

This example shows how to convert an approved file to Markdown using MarkItDown without turning conversion into a broad ingestion pipeline.

Use this when a document needs to be converted into Markdown for public-safe review, summarization, or documentation work.

## Scenario

You have one approved, non-sensitive source file and want to convert it into Markdown before handing it to an AI tool.

Approved input example:

```text
examples/source/public-workflow-notes.pdf
```

Approved output example:

```text
examples/converted/public-workflow-notes.md
```

Not approved:

```text
private notes
private memory
raw AI exports
local logs
personal records
employer-sensitive content
financial records
health records
relationship records
credentials or tokens
marshall-local-os
whole-folder bulk imports
```

## Safe Conversion Pattern

Use a dedicated input folder and output folder for approved files only.

```text
examples/source/
examples/converted/
```

Before converting, confirm the file is safe:

```bash
ls -la examples/source/
```

Convert one file at a time.

Example command pattern:

```bash
markitdown examples/source/public-workflow-notes.pdf > examples/converted/public-workflow-notes.md
```

If using a different command form, keep the same rule:

```text
one approved input file → one Markdown output file
```

## Required Inspection

Before sharing the converted Markdown with any AI tool, inspect it.

```bash
sed -n '1,120p' examples/converted/public-workflow-notes.md
grep -ni "secret\|token\|credential\|private\|personal\|financial\|health\|marshall-local-os" examples/converted/public-workflow-notes.md || true
git status --short
```

The grep command may return safe policy language such as "do not include private data." That is acceptable.

Stop if it returns actual private records, private paths, credentials, or sensitive details.

## Safe AI Handoff Prompt

```text
You are reviewing a Markdown conversion from an approved public-safe source file.

Use only the converted Markdown provided.

Task:
Summarize the document in five bullets and identify whether it belongs in the public workflow repo.

Rules:
- Do not request private files.
- Do not ask for original private documents.
- Do not infer personal details.
- Do not add new tools.
- Do not redesign the repo.
- Return only the summary, public-safety assessment, and one recommended next step.
```

## Good AI Output

```text
Summary:
- The document describes a safe AI review workflow.
- It limits inputs to public repo docs.
- It prohibits private local data and credentials.
- It asks for one small improvement only.
- It keeps the next step reversible.

Public-safety assessment:
This belongs in the public workflow repo because it uses synthetic/public-safe content and does not include private records.

Recommended next step:
Add it as a public-safe example under docs/examples/.
```

Why this is good:

- It uses only the converted Markdown.
- It checks public safety.
- It suggests one next step.
- It does not request private source material.

## Bad AI Output

```text
Convert your full notes folder and upload all Markdown outputs so I can build a complete memory index.
```

Why this is bad:

- It asks for bulk ingestion.
- It risks private data exposure.
- It expands scope.
- It turns a conversion workflow into a memory system.

## Cleanup

Temporary conversion outputs should not be committed unless intentionally reviewed and approved.

```bash
rm -f examples/converted/public-workflow-notes.md
git status --short
```

If the converted Markdown is intentionally kept, confirm:

- the source file was approved
- the Markdown was inspected
- no private data is present
- the file belongs in the public repo

## Done Rule

The conversion is successful only if one approved file becomes one inspected Markdown file and the output can be safely used without private data, bulk ingestion, or a new tool loop.
