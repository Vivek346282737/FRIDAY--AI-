"""
FRIDAY Core MCP Tools.
Provides access to the main FRIDAY processing pipeline.
"""

from friday_core import process_message


def ask_friday_core(message: str) -> dict:
    """
    Process a request using FRIDAY's main AI pipeline,
    including planning, reasoning, vision context, and execution.
    """
    return process_message(message)


def register(mcp):
    """Register FRIDAY Core tools with the MCP server."""
    mcp.tool()(ask_friday_core)
