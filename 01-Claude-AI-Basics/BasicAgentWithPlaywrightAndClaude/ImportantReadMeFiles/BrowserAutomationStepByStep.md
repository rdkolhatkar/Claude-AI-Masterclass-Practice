# Browser Automation Using an MCP Server: Step-by-Step

This guide completes the six-point outline in `ImportantNotes/ImportantNotes.txt` (lines 33–39) and follows the screenshots in `Images/01_ClaudePlaywrightMCP.PNG` through `Images/14_ClaudePlaywrightMCP_B.PNG`.

**Tools used:** Claude Desktop app, Playwright MCP server (Microsoft), Node.js 18+.

---

## Outline point 1: Use the Playwright MCP server

Playwright MCP is an MCP server from Microsoft that lets an AI model drive a real browser through tools such as *navigate*, *click*, *type text*, *fill form*, *take screenshot*, and *page snapshot*.

- Project: https://github.com/microsoft/playwright-mcp
- Screenshot `01_ClaudePlaywrightMCP.PNG` shows the project's README, the "Getting started" section, and the standard JSON config.

## Outline point 2: Source and reference

- Maintainer: Microsoft.
- Always confirm the current install command in the README before you copy it, because package names and arguments change.

## Outline point 3: Provide the MCP configuration in JSON

Claude reads its MCP servers from a JSON config file. Copy the standard config from the README (`01_ClaudePlaywrightMCP.PNG`) into that file.

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

**Where to put it (Claude Desktop on Windows):**

1. Open Claude Desktop and go to **File → Settings** (`02`, `03`).
2. Choose **Developer** under *This computer*, then click **Edit config** (`04`).
3. This opens `claude_desktop_config.json`. On this machine it is at `C:\Users\Ratnakar\AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude` (the Store-app location shown in `05`). Open it with Notepad (`06`).
4. Add the `playwright` block under `mcpServers` (`07`). Keep the other keys in the file as they are.
5. Save the file and restart Claude Desktop.

## Outline point 4: Claude starts the MCP server locally

- Claude Desktop runs the `command` from the config (`npx @playwright/mcp@latest`) on your machine. `npx` downloads the package the first time.
- Go back to **Settings → Developer**. The server appears under *Local MCP servers* with the status **Running** and a **View logs** button (`08`). If it does not show *Running*, open the logs first.
- No browser is opened at this stage. The browser starts when Claude first calls a Playwright tool.

## Outline point 5: Give a plain-English prompt

Once the server is running, you enable it in the chat and type a normal sentence.

1. In a new session, click **+ → Connectors** and turn on **playwright** (`09`). Use **Manage connectors** (`10`) if you need to change it.
2. In *Connectors*, the `playwright` entry is listed as *Desktop · Local dev* with a check mark (`11`).
3. Type the instruction in plain English (`13`):

   > Navigate to the "https://rahulshettyacademy.com/client" and click on the "Don't have an account? Register here" link

4. Claude decides which MCP tools to call, runs them, and reports back. In `14_A` the answer says it used 4 tools, opened the page, clicked "Register here", and stopped on `/client/#/auth/register` without filling in or submitting the form. That stopping point is intentional in the prompt.

## Outline point 6: The server exposes tools, and you specify which ones to use

Playwright MCP publishes its tool list to Claude. In **Settings → Connectors → playwright** you can see them (`12_A`, `12_B`):

| Group | Count | Examples | Default permission |
|---|---|---|---|
| Read-only tools | 7 | Page snapshot, Take a screenshot, Get console messages, List network requests, Wait for | Needs approval |
| Write/delete tools | 18 | Navigate to a URL, Click, Type text, Fill form, Press a key, Upload files, Evaluate JavaScript, Close browser | Needs approval |

For each tool you can choose one of three icons per row: allow (✓), needs approval (hand, the current setting in the screenshots), or block (⊘). Set the tools your test needs to *Always allow* and keep *Needs approval* for anything that changes data. For the registration test above, *Navigate to a URL*, *Click*, and *Page snapshot* are the tools that matter.

---

## Full run order (summary)

| Step | Action | Screenshot |
|---|---|---|
| 1 | Open the Playwright MCP GitHub README and copy the standard config | 01 |
| 2 | Open Claude Desktop → File → Settings | 02, 03 |
| 3 | Developer → Edit config | 04 |
| 4 | Open `claude_desktop_config.json` in Notepad | 05, 06 |
| 5 | Paste the `playwright` block under `mcpServers`, save, restart | 07 |
| 6 | Confirm the server shows **Running** under Developer | 08 |
| 7 | In a chat, enable **playwright** under Connectors | 09, 10, 11 |
| 8 | Review tool permissions (Always allow / Needs approval) | 12_A, 12_B |
| 9 | Type the plain-English prompt | 13 |
| 10 | Read the result and check the page the browser reached | 14_A, 14_B |

## Notes

- `14_B` shows the browser pane that opened beside the chat with the Register form. The chat reports the browser tool result, so the form was only reached, not filled.
- The config in `07` was already present on this machine. The `command` and `args` lines match the README.
- The MCP server runs locally, so the browser and any page content stay on your computer. Keep the *Needs approval* setting for write actions when you test real sites.
- Commands and config paths can change between releases. Check the official README if a step differs on your version.
