from services.process_service import open_app, close_app


def register(mcp):

    @mcp.tool()
    def open_application(app_name: str) -> dict:
        """Open a supported application on the user's Windows computer. Use this tool when the user asks to open an app such as Notepad, Calculator, Chrome, Edge, VS Code, Command Prompt, PowerShell, File Explorer, or Settings."""
        return open_app(app_name)


    @mcp.tool()
    def close_application(app_name: str) -> dict:
        """Close a supported application on the user's Windows computer."""
        return close_app(app_name)
