"""
FRIDAY Core MCP Tools.
Provides access to the main FRIDAY processing pipeline.
"""

from friday_core import process_message


def register(mcp):

    @mcp.tool()
    def ask_friday_core(message: str) -> dict:
        """
        Process a request using FRIDAY's main AI pipeline,
        including planning, reasoning, vision context, and execution.
        Use this when a request should be handled by the main FRIDAY core.
        """

        return process_message(message)
