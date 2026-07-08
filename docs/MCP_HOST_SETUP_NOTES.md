# MCP Host Setup Notes

## Purpose

This note records what happened during the controlled MCP read-only access test and preserves the retry plan.

The goal is not to make MCP work at any cost. The goal is to test whether an MCP host can safely read a narrow public-safe folder without exposing private local data, requiring write access, or creating a new tool loop.

## Approved Test Scope

The approved first-test folder was:

```text
/tmp/ai-workflow-mcp-test
```

That folder contained only public-safe copies of:

```text
README.md
AGENTS.md
docs/
```

The real repo was not used as the first MCP target.

Private folders were not approved.

## Known Working Pieces

The public-safe test copy existed locally.

The filesystem MCP server started manually from Terminal with:

```bash
/usr/bin/env -i \
  PATH="/Users/marshallfwalker/.nvm/versions/node/v20.17.0/bin:/usr/bin:/bin:/usr/sbin:/sbin" \
  HOME="$HOME" \
  /Users/marshallfwalker/.nvm/versions/node/v20.17.0/bin/npx \
  -y @modelcontextprotocol/server-filesystem /tmp/ai-workflow-mcp-test
```

Observed output:

```text
Secure MCP Filesystem Server running on stdio
```

Verified local tools:

```text
node: v20.17.0
npx: 10.8.2
npx path: /Users/marshallfwalker/.nvm/versions/node/v20.17.0/bin/npx
Docker: not installed
```

## Claude Desktop Result

Claude Desktop was tested first.

A Claude Desktop MCP config was created and pointed only at:

```text
/tmp/ai-workflow-mcp-test
```

Claude saw a server name during testing, but the active session exposed Claude-managed uploads folders instead of the configured local test path.

Result:

```text
Claude Desktop local filesystem MCP test: blocked
```

Likely better retry path:

```text
Docker-backed filesystem MCP with a container-level read-only mount
```

## Cursor Result

Cursor was tested next.

A temporary project-local config was created at:

```text
.cursor/mcp.json
```

The tested config used:

```json
{
  "mcpServers": {
    "workflow_docs_test": {
      "command": "/Users/marshallfwalker/.nvm/versions/node/v20.17.0/bin/npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/tmp/ai-workflow-mcp-test"
      ],
      "env": {
        "PATH": "/Users/marshallfwalker/.nvm/versions/node/v20.17.0/bin:/usr/bin:/bin:/usr/sbin:/sbin",
        "HOME": "/Users/marshallfwalker"
      }
    }
  }
}
```

Cursor sometimes showed the project-configured server, but the active agent session did not consistently expose the `workflow_docs_test` tools.

The local `.cursor` config was removed after testing so it would not be accidentally committed.

Result:

```text
Cursor MCP test: blocked / unstable
```

## Safety Results

The test stayed inside the intended safety boundary.

Successful outcomes:

- no private folders were exposed
- no `marshall-local-os` access was granted
- no real repo write access was tested
- no external actions were run
- no shell fallback was used for the actual MCP read test
- the MCP target remained a public-safe test copy
- temporary Cursor config was removed
- git working tree was clean after cleanup

## Retry Options

Preferred retry order:

1. Install Docker and retry Claude Desktop with a read-only Docker mount.
2. Retry Cursor only after confirming the correct way to start and bind project MCP servers in the active agent session.
3. Try another MCP host only if it supports a clearly scoped read-only filesystem server.

## Stop Conditions

Stop immediately if the host asks for:

- whole-computer access
- broad home-folder access
- `~/Documents`
- `~/Desktop`
- `~/Downloads`
- `marshall-local-os`
- write access for the first test
- external actions
- multiple MCP servers for the first read-only test

Also stop if host setup takes longer than the value of the read-only test.

## Future Test Prompt

Use this prompt only after the MCP host clearly exposes the approved test folder:

```text
Use the workflow_docs_test MCP server only.

List the allowed directories.

Read only:
- README.md
- AGENTS.md
- docs/

Summarize:
1. the project purpose
2. the public/private boundary
3. the current tool lane

Do not edit files.
Do not scan outside the allowed MCP directory.
Do not use browser tools.
Do not use shell commands.
Do not access private folders.
Do not run external actions.
```

## Decision

MCP remains parked until there is a reliable host setup.

The project should continue with public repo documentation and workflow improvements rather than more MCP host debugging.
