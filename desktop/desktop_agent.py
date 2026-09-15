from desktop.desktop_actions import (
    move_mouse,
    move_mouse_to,
    left_click,
    double_click,
    right_click,
    click_at,
    double_click_at,
    right_click_at,
    type_text,
    press_key,
    press_hotkey,
    screenshot,
    screen_size,
    mouse_position,
    scroll,
    scroll_up,
    scroll_down,
    wait,
    execute_sequence,
)


class DesktopAgent:

    def execute(self, instruction):

        if isinstance(instruction, list):

            return execute_sequence(
                instruction
            )

        if isinstance(instruction, dict):

            steps = instruction.get("steps")

            if isinstance(steps, list):

                return execute_sequence(
                    steps
                )

            return {
                "success": False,
                "message": (
                    "Desktop dictionary must "
                    "contain a steps list."
                )
            }

        if not instruction:

            return {
                "success": False,
                "message": (
                    "Desktop instruction is empty."
                )
            }

        text = str(
            instruction
        ).strip()

        lower = text.lower()

        if lower == "screenshot":
            return screenshot()

        if lower == "screen size":
            return screen_size()

        if lower == "mouse position":
            return mouse_position()

        if lower == "click":
            return left_click()

        if lower == "double click":
            return double_click()

        if lower == "right click":
            return right_click()

        if lower.startswith("click at "):

            try:

                parts = text[9:].split()

                return click_at(
                    int(parts[0]),
                    int(parts[1])
                )

            except Exception as e:

                return {
                    "success": False,
                    "message": (
                        f"Invalid click coordinates: "
                        f"{e}"
                    )
                }

        if lower.startswith("double click at "):

            try:

                parts = text[16:].split()

                return double_click_at(
                    int(parts[0]),
                    int(parts[1])
                )

            except Exception as e:

                return {
                    "success": False,
                    "message": str(e)
                }

        if lower.startswith("right click at "):

            try:

                parts = text[15:].split()

                return right_click_at(
                    int(parts[0]),
                    int(parts[1])
                )

            except Exception as e:

                return {
                    "success": False,
                    "message": str(e)
                }

        if lower.startswith("type "):

            return type_text(
                text[5:]
            )

        if lower.startswith("press "):

            return press_key(
                text[6:].strip()
            )

        if lower.startswith("hotkey "):

            keys = text[7:].split()

            return press_hotkey(
                *keys
            )

        if lower.startswith("wait "):

            try:

                return wait(
                    float(
                        text[5:].strip()
                    )
                )

            except Exception as e:

                return {
                    "success": False,
                    "message": str(e)
                }

        if lower == "scroll up":
            return scroll_up()

        if lower == "scroll down":
            return scroll_down()

        if lower.startswith("scroll "):

            try:

                return scroll(
                    int(
                        text[7:].strip()
                    )
                )

            except Exception as e:

                return {
                    "success": False,
                    "message": str(e)
                }

        if lower.startswith("move"):

            try:

                cleaned = lower

                cleaned = cleaned.replace(
                    "move mouse to",
                    ""
                )

                cleaned = cleaned.replace(
                    "move mouse",
                    ""
                )

                cleaned = cleaned.replace(
                    "move",
                    ""
                )

                parts = cleaned.strip().split()

                return move_mouse_to(
                    int(parts[0]),
                    int(parts[1])
                )

            except Exception as e:

                return {
                    "success": False,
                    "message": str(e)
                }

        return {
            "success": False,
            "message": (
                f"Unknown desktop instruction: "
                f"{text}"
            )
        }


desktop_agent = DesktopAgent()
