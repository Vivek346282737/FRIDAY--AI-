"""
Tool registry - imports and registers all tool modules with the MCP server.
"""

from friday.tools import web, system, utils, applications, desktop, core


def register_all_tools(mcp):
    """Register all tool groups onto the MCP server instance."""
    web.register(mcp)
    system.register(mcp)
    utils.register(mcp)
    applications.register(mcp)
    desktop.register(mcp)
    core.register(mcp)

