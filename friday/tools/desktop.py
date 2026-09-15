from desktop.desktop_actions import (
    type_text,
    press_key,
    press_hotkey,
    wait,
    move_mouse_to,
    click_at,
    double_click_at,
    right_click_at,
    scroll,
    execute_sequence,
)


def register(mcp):

    @mcp.tool()
    def type_on_keyboard(text: str) -> dict:
        """Type text into the currently focused application or input field."""
        return type_text(text)


    @mcp.tool()
    def wait_for(seconds: float) -> dict:
        """Wait for the specified number of seconds."""
        return wait(seconds)


    @mcp.tool()
    def press_keyboard_key(key: str) -> dict:
        """Press a keyboard key such as enter, tab, escape, or space."""
        return press_key(key)


    @mcp.tool()
    def press_keyboard_hotkey(keys: str) -> dict:
        """Press a keyboard shortcut. Provide keys separated by spaces, for example: ctrl s."""
        return press_hotkey(*keys.split())


    @mcp.tool()
    def move_mouse_to_position(x: int, y: int) -> dict:
        """Move the mouse cursor to screen coordinates x and y."""
        return move_mouse_to(x, y)


    @mcp.tool()
    def click_screen_position(x: int, y: int) -> dict:
        """Move the mouse to coordinates and perform a left click."""
        return click_at(x, y)


    @mcp.tool()
    def double_click_screen_position(x: int, y: int) -> dict:
        """Move the mouse to coordinates and perform a double click."""
        return double_click_at(x, y)


    @mcp.tool()
    def right_click_screen_position(x: int, y: int) -> dict:
        """Move the mouse to coordinates and perform a right click."""
        return right_click_at(x, y)


    @mcp.tool()
    def scroll_screen(amount: int) -> dict:
        """Scroll the screen. Use positive values for up and negative values for down."""
        return scroll(amount)


    @mcp.tool()
    def execute_desktop_sequence(actions: list[dict]) -> dict:
        """
        Execute multiple desktop actions in order.

        Each action must contain an action name and required parameters.

        Supported actions:
        move: x, y
        click: x, y
        double_click: x, y
        right_click: x, y
        type: text
        press: key
        hotkey: keys
        scroll: amount
        wait: seconds

        Execution stops immediately if an action fails.
        """
        return execute_sequence(actions)
