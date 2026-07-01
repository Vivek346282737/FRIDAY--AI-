from desktop.desktop_actions import (
    move_mouse,
    left_click,
    double_click,
    right_click,
    type_text,
    press_key,
    press_hotkey,
    screenshot,
    screen_size,
    mouse_position,
    scroll_up,
    scroll_down,
)


class DesktopAgent:

    def execute(self, instruction: str):

        text = instruction.strip()
        lower = text.lower()

        # ====================================
        # SCREENSHOT
        # ====================================

        if lower == "screenshot":

            return screenshot()

        # ====================================
        # SCREEN SIZE
        # ====================================

        if lower == "screen size":

            return screen_size()

        # ====================================
        # MOUSE POSITION
        # ====================================

        if lower == "mouse position":

            return mouse_position()

        # ====================================
        # CLICK
        # ====================================

        if lower == "click":

            return left_click()

        if lower == "double click":

            return double_click()

        if lower == "right click":

            return right_click()

        # ====================================
        # SCROLL
        # ====================================

        if lower == "scroll up":

            return scroll_up()

        if lower == "scroll down":

            return scroll_down()

        # ====================================
        # TYPE
        # ====================================

        if lower.startswith("type "):

            return type_text(text[5:])

        # ====================================
        # PRESS
        # ====================================

        if lower.startswith("press "):

            key = text[6:].strip()

            return press_key(key)

        # ====================================
        # HOTKEY
        # ====================================

        if lower.startswith("hotkey "):

            keys = text[7:].split()

            return press_hotkey(*keys)

        # ====================================
        # MOVE
        #
        # Supports:
        # move 500 300
        # move mouse 500 300
        # move mouse to 500 300
        # ====================================

        if lower.startswith("move"):

            try:

                cleaned = lower

                cleaned = cleaned.replace("move mouse to", "")
                cleaned = cleaned.replace("move mouse", "")
                cleaned = cleaned.replace("move", "")
                cleaned = cleaned.strip()

                parts = cleaned.split()

                x = int(parts[0])
                y = int(parts[1])

                return move_mouse(x, y)

            except Exception as e:

                return {
                    "success": False,
                    "message": str(e)
                }

        return {
            "success": False,
            "message": "Unknown desktop instruction."
        }


desktop_agent = DesktopAgent()