# WSL Workaround for MCP Server

When trying to use the standard method of creating `mcp.json` in the `.vscode` folder, I encountered the `Connection state: Error spawn .... ENOENT` error. After some research, I found that this is a known issue in VS Code, which will be addressed in a future update.

You can track the issue here: [https://github.com/microsoft/vscode/issues/251308](https://github.com/microsoft/vscode/issues/251308)

## The Workaround

Since the update might take a while, I'm using a temporary workaround in my `settings.json`. As I use VS Code in WSL and didn't want to modify the Windows `settings.json`, I'm using the following configuration:

```json
"mcp": {
    "servers": {
        "DevOpsUtilityCommands": {
            "type": "stdio",
            "command": "wsl.exe", // Invokes the WSL subsystem
            "args": [
                "/home/edipof/Documents/repo/mcp-lab/code/python-mcp/.venv/bin/python", // Command to be executed inside WSL
                "/home/edipof/Documents/repo/mcp-lab/code/python-mcp/server-mcp.py" // Path inside WSL
            ]
        }
    }
}
```

### Standard Configuration (for when the issue is fixed)

If it weren't for this problem, the `mcp.json` could be created like this:

```json
{
  "servers": {
    "DevOpsUtilityCommands": {
      "type": "stdio",
      "command": "${workspaceFolder}/code/python-mcp/.venv/bin/python",
      "args": [
        "${workspaceFolder}/code/python-mcp/server-mcp.py"
      ]
    }
  }
}
```

## Important Considerations

After applying this workaround, everything works as expected. Copilot can detect the MCP server, and I can list Docker containers, execute Kubernetes commands, and even control Jenkins perfectly.

**A word of caution:** These commands are simple and easy to implement, but they must be used with extreme care. In this repository, they are for testing purposes. In an environment with access to critical systems, the best approach is to create highly restrictive functions.

## Future Plans

This repository is a work in progress. I will be adding more tools over time, including a TypeScript version of the MCP server.
