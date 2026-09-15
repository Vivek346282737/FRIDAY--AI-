from desktop.desktop_controller import desktop


def screenshot():
    return desktop.screenshot()


def screen_size():
    return desktop.screen_size()


def mouse_position():
    return desktop.mouse_position()


def move_mouse(x, y):
    return desktop.move(x, y)


def move_mouse_to(x, y):
    return desktop.move(int(x), int(y))


def left_click():
    return desktop.click()


def double_click():
    return desktop.double_click()


def right_click():
    return desktop.right_click()


def click_at(x, y):
    desktop.move(int(x), int(y))
    return desktop.click()


def double_click_at(x, y):
    desktop.move(int(x), int(y))
    return desktop.double_click()


def right_click_at(x, y):
    desktop.move(int(x), int(y))
    return desktop.right_click()


def type_text(text):
    return desktop.type(str(text))


def press_key(key):
    return desktop.press(str(key))


def press_hotkey(*keys):
    return desktop.hotkey(*keys)


def scroll(amount):
    return desktop.scroll(int(amount))


def scroll_up():
    return desktop.scroll(500)


def scroll_down():
    return desktop.scroll(-500)


def wait(seconds):
    return desktop.wait(float(seconds))


def execute_sequence(actions):

    if not isinstance(actions, list):
        return {
            "success": False,
            "message": "Desktop sequence must be a list."
        }

    results = []

    for index, step in enumerate(actions, start=1):

        if not isinstance(step, dict):

            return {
                "success": False,
                "failed_step": index,
                "message": "Invalid desktop sequence step.",
                "results": results
            }

        action = str(
            step.get("action", "")
        ).lower().strip()

        try:

            if action == "move":

                result = move_mouse_to(
                    step["x"],
                    step["y"]
                )

            elif action == "click":

                if "x" in step and "y" in step:

                    result = click_at(
                        step["x"],
                        step["y"]
                    )

                else:

                    result = left_click()

            elif action == "double_click":

                if "x" in step and "y" in step:

                    result = double_click_at(
                        step["x"],
                        step["y"]
                    )

                else:

                    result = double_click()

            elif action == "right_click":

                if "x" in step and "y" in step:

                    result = right_click_at(
                        step["x"],
                        step["y"]
                    )

                else:

                    result = right_click()

            elif action == "type":

                result = type_text(
                    step.get("text", "")
                )

            elif action == "press":

                result = press_key(
                    step["key"]
                )

            elif action == "hotkey":

                result = press_hotkey(
                    *step["keys"]
                )

            elif action == "scroll":

                result = scroll(
                    step.get("amount", -500)
                )

            elif action == "wait":

                result = wait(
                    step.get("seconds", 1)
                )

            elif action == "screenshot":

                result = screenshot()

            else:

                result = {
                    "success": False,
                    "message": (
                        f"Unknown desktop action: "
                        f"{action}"
                    )
                }

        except Exception as e:

            result = {
                "success": False,
                "message": str(e)
            }

        results.append(
            {
                "step": index,
                "action": action,
                "result": result
            }
        )

        if not result.get("success", False):

            return {
                "success": False,
                "failed_step": index,
                "results": results,
                "message": result.get(
                    "message",
                    "Desktop sequence failed."
                )
            }

    return {
        "success": True,
        "type": "desktop_sequence",
        "results": results
    }
