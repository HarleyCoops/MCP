# FireCrawl MCP Server Setup Guide

## Issue Resolution
We encountered and fixed the following issues with the FireCrawl MCP server:

1. Initial Error: `spawn npx ENOENT`
   - Problem: The configuration was trying to use `npx` directly without proper installation
   - Solution: We needed to:
     a. Install the package globally: `npm install -g firecrawl-mcp`
     b. Update the MCP configuration to use the installed package

2. Configuration Fix:
   - Original problematic configuration:
   ```json
   {
     "command": "npx",
     "args": ["-y", "firecrawl-mcp"]
   }
   ```
   - Working configuration:
   ```json
   {
     "command": "node",
     "args": ["C:/Users/chris/AppData/Roaming/npm/node_modules/firecrawl-mcp/dist/index.js"]
   }
   ```

## Global MCP Configuration
The MCP configuration is stored in:
`C:/Users/chris/AppData/Roaming/Cursor/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`

This is a global configuration file that applies to all projects. When you use Cline in any project:
1. The MCPs defined in this configuration will be available
2. You don't need to reinstall or reconfigure MCPs for each project
3. The configuration uses absolute paths, so it works regardless of the project location

## FireCrawl MCP Capabilities
Once properly configured, the FireCrawl MCP provides several tools:
- `firecrawl_scrape`: Scrape single webpages
- `firecrawl_map`: Discover URLs from a starting point
- `firecrawl_crawl`: Start asynchronous crawls of multiple pages
- `firecrawl_batch_scrape`: Scrape multiple URLs in batch mode
- `firecrawl_search`: Search and retrieve web content
- `firecrawl_extract`: Extract structured information using LLM

Each tool can be accessed from any project through Cline's MCP integration.
