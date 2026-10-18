# Browser Automation MCP Servers

A comparison of MCP (Model Context Protocol) servers that let AI assistants control a web browser.

> Compiled October 2026. Commands and links change often, so check the official docs before installing.

## Contents

- [Quick picks](#quick-picks)
- [Overview](#overview)
- [Features and limitations](#features-and-limitations)
- [Setup commands](#setup-commands)
- [AI client compatibility](#ai-client-compatibility)

---

## Quick picks

| If you want to... | Use |
|---|---|
| Automate and test websites (general purpose) | **Playwright MCP** |
| Debug performance, network or console errors on your site | **Chrome DevTools MCP** |
| Run many browsers in the cloud, unattended or in parallel | **Browserbase MCP** |
| Use your real, logged-in browser | **Browser MCP** or **Claude in Chrome** |
| Mix plain-English steps with Playwright code | **Stagehand** |
| Scrape sites with strong anti-bot protection | **Stealth Browser MCP** |

---

## Overview

| MCP Server | Maintainer | Runs where | Best for | Browsers | Official docs |
|---|---|---|---|---|---|
| **Playwright MCP** | Microsoft | Local (open source) | General automation, end-to-end testing | Chrome, Firefox, WebKit (Safari), Edge | [GitHub](https://github.com/microsoft/playwright-mcp) |
| **Chrome DevTools MCP** | Google Chrome DevTools team | Local (open source) | Debugging, performance, network inspection | Chrome only | [GitHub](https://github.com/ChromeDevTools/chrome-devtools-mcp) |
| **Puppeteer MCP** | MCP reference server (archived) | Local (open source) | Lightweight Chromium scripting | Chromium / Chrome | [GitHub](https://github.com/modelcontextprotocol/servers-archived) |
| **Selenium MCP** | Angie Jones (community) | Local (open source) | Teams with existing Selenium tests | Chrome, Firefox | [GitHub](https://github.com/angiejones/mcp-selenium) |
| **Browser MCP** | browsermcp.io | Local + Chrome extension | Automating your logged-in browser | Chrome | [Website](https://browsermcp.io) · [Docs](https://docs.browsermcp.io) |
| **Browser Tools MCP** | AgentDesk AI | Local + Chrome extension | Sending console/network logs to coding agents | Chrome | [GitHub](https://github.com/AgentDeskAI/browser-tools-mcp) |
| **Browserbase MCP** | Browserbase | Cloud (also local) | Scale, unattended or parallel runs | Chromium (cloud) | [GitHub](https://github.com/browserbase/mcp-server-browserbase) · [Docs](https://docs.browserbase.com) |
| **Anchor Browser MCP** | Anchor | Cloud | Remote browsers with Playwright-style tools | Chromium (cloud) | [Docs](https://docs.anchorbrowser.io) |
| **Stagehand** | Browserbase | Library (MCP via Browserbase) | Natural language + Playwright code | Chromium | [GitHub](https://github.com/browserbase/stagehand) · [Docs](https://docs.stagehand.dev) |
| **Browser Use** | browser-use (open source) | Library with MCP mode, also cloud | Fully AI-driven browser agents | Chromium | [GitHub](https://github.com/browser-use/browser-use) · [Docs](https://docs.browser-use.com) |
| **Stealth Browser MCP** | Community | Local (open source) | Anti-bot / stealth scraping | Chrome / Chromium | [GitHub](https://github.com/vibheksoni/stealth-browser-mcp) |
| **BrowserWing** | Community | Local | Turning recorded actions into MCP tools | Chrome / Chromium | Search GitHub for "BrowserWing" |
| **Claude in Chrome** | Anthropic | Chrome extension | Letting Claude act in your real Chrome | Chrome | [claude.ai/chrome](https://claude.ai/chrome) |

---

## Features and limitations

| MCP Server | Key features | Limitations |
|---|---|---|
| **Playwright MCP** | Accessibility-tree snapshots (fast, low token use); 15+ tools: navigate, click, type, forms, tabs, screenshots, PDF; headed or headless | Can be blocked by anti-bot sites; not built for stealth scraping |
| **Chrome DevTools MCP** | First-party DevTools Protocol access; performance traces, network requests, console logs, Lighthouse-style audits | Chrome only; weaker for long automation flows |
| **Puppeteer MCP** | Selector-based navigate, click, fill, hover, screenshots, run JavaScript | Archived (no longer maintained); Chromium only |
| **Selenium MCP** | WebDriver sessions; find elements, click, type, screenshots; headless mode for CI | Slower than DevTools-based tools |
| **Browser MCP** | Uses your existing cookies and sessions; avoids fresh-profile bot detection | Acts in your real accounts, so review actions |
| **Browser Tools MCP** | Console and network log capture, screenshots, DOM inspection, accessibility/SEO audits | Mostly observation; limited automation |
| **Browserbase MCP** | Hosted cloud browsers; natural-language actions (act / extract / observe); sessions, stealth, proxies | Paid beyond free tier; data goes through a third-party cloud |
| **Anchor Browser MCP** | Cloud browser sessions driven by Playwright tools | Paid service; smaller ecosystem |
| **Stagehand** | `act`, `observe`, `extract` in plain English next to raw Playwright; self-healing selectors | A library, not a standalone MCP server; model calls add cost |
| **Browser Use** | LLM decides each step; vision + DOM understanding; multi-tab | Less predictable; model in the loop every step |
| **Stealth Browser MCP** | Undetected Chrome, fingerprint evasion, network interception | Community project; respect site terms and laws |
| **BrowserWing** | Record actions once, replay as MCP tools | Newer project; check it's maintained |
| **Claude in Chrome** | Navigate, read pages, fill forms, multi-tab, console/network reading, GIF recording; per-site permissions | Works with Claude only |

---

## Setup commands

| MCP Server | Install / run command | Requirements |
|---|---|---|
| **Playwright MCP** | `npx @playwright/mcp@latest` | Node.js 18+ |
| **Chrome DevTools MCP** | `npx chrome-devtools-mcp@latest` | Node.js, Chrome |
| **Puppeteer MCP** | `npx -y @modelcontextprotocol/server-puppeteer` | Node.js |
| **Selenium MCP** | `npx -y @angiejones/mcp-selenium` | Node.js, browser driver |
| **Browser MCP** | `npx @browsermcp/mcp@latest` | Browser MCP Chrome extension |
| **Browser Tools MCP** | `npx @agentdeskai/browser-tools-mcp@latest` and `npx @agentdeskai/browser-tools-server@latest` | Browser Tools Chrome extension |
| **Browserbase MCP** | `npx @browserbasehq/mcp-server-browserbase` | `BROWSERBASE_API_KEY`, `BROWSERBASE_PROJECT_ID`, LLM API key |
| **Anchor Browser MCP** | See Anchor docs | Anchor API key |
| **Stagehand** | `npm install @browserbasehq/stagehand` (or `pip install stagehand`) | LLM API key |
| **Browser Use** | `pip install browser-use` (see docs for MCP mode) | Python, LLM API key |
| **Stealth Browser MCP** | Clone the repo and follow the README | Python |
| **BrowserWing** | See project README | — |
| **Claude in Chrome** | Install from [claude.ai/chrome](https://claude.ai/chrome) | Chrome, Claude account |

### Adding a server to Claude Code

```bash
claude mcp add playwright -- npx @playwright/mcp@latest
claude mcp add chrome-devtools -- npx chrome-devtools-mcp@latest
claude mcp add selenium -- npx -y @angiejones/mcp-selenium
```

### Adding a server to Claude Desktop, Cursor, VS Code, etc.

Most clients use a JSON config like this:

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

---

## AI client compatibility

MCP is an open standard, so almost every server here works with **any MCP-capable client** and **any LLM** behind it.

| Client | Supported |
|---|---|
| Claude Desktop / Claude Code | ✅ |
| Cursor | ✅ |
| VS Code (GitHub Copilot) | ✅ (Copilot Coding Agent includes Playwright MCP by default) |
| Windsurf | ✅ |
| Cline | ✅ |
| ChatGPT (via hosted MCP URLs, e.g. Browserbase) | ✅ |
| Custom agents built with an MCP SDK | ✅ |

**Exceptions:** Claude in Chrome works with Claude only. Stagehand and Browser Use are libraries that work with Claude, GPT, Gemini and local models directly, and reach MCP clients through their MCP modes.

---

## Notes

- **Local vs cloud:** local servers run on your machine (free, private, but can be blocked by anti-bot sites); cloud servers run browsers remotely (scalable, but paid and your data leaves your machine).
- **Less-verified entries:** the Anchor Browser, Browser Use (MCP command), Stealth Browser MCP and BrowserWing rows come from smaller or fast-changing projects. Confirm details in their docs first.
