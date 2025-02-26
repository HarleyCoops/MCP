# FireCrawl MCP Server Setup Guide

## About Model Control Protocol (MCP)
MCP (Model Control Protocol) is an open standard for integrating AI models with external data and tools. It enables:
- Seamless integration between AI models and external tools
- Standardized communication protocols
- Enhanced AI capabilities through tool access
- Project-wide availability of configured tools

For more details, visit the [Claude MCP Documentation](https://www.claudemcp.com/docs/introduction).

## Setup Requirements

1. Global Installation
   ```bash
   npm install -g firecrawl-mcp
   ```

2. MCP Configuration
   The MCP server must be configured in the Cline settings file with:
   - Correct path to the firecrawl-mcp.cmd
   - FIRECRAWL_API_KEY in the environment variables
   ```json
   {
     "command": "C:/Users/chris/AppData/Roaming/npm/firecrawl-mcp.cmd",
     "args": [],
     "env": {
       "FIRECRAWL_API_KEY": "your-api-key"
     }
   }
   ```

3. Connection Status
   - The server can be verified by running: `$env:FIRECRAWL_API_KEY='your-key'; C:/Users/chris/AppData/Roaming/npm/firecrawl-mcp.cmd --help`
   - A successful response shows: "FireCrawl MCP Server initialized successfully"
   - The MCP server must be properly connected to Cline to use its tools

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

## Submitting to MCP Marketplace

Want to make FireCrawl MCP available to millions of developers? You can submit it to the [Cline MCP Marketplace](https://github.com/cline/mcp-marketplace).

### Submission Requirements
1. Create a new issue in the `mcp-marketplace` repository with:
   - GitHub Repo URL of your MCP server
   - 400×400 PNG logo image for the server icon
   - Brief explanation of your server's benefits

### One-Click Installation Support
To ensure smooth one-click installation:
1. Verify your README.md contains clear setup instructions
2. Optionally create `llms-install.md` for complex setups
3. Test that Cline can successfully set up your server using just the documentation

### Submission Process
1. Submit via GitHub issue
2. Wait for team review (typically a few days)
3. Once approved, your MCP server becomes available in the marketplace

For support during submission, join the Discord `#mcp` channel.

Note: While repository stars aren't required for submission, all servers undergo security and stability vetting before marketplace inclusion.
