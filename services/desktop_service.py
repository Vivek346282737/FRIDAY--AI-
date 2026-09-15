import time
from pathlib import Path

import pyautogui


# =====================================================
# SAFETY SETTINGS
# =====================================================

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.15


class DesktopService:

    # =================================================
    # SCREEN INFORMATION
    # =================================================

    def screen_size(self):

        try:

            width, height = pyautogui.size()

            return {

                "success": True,

                "width": width,

                "height": height

            }

        except Exception as e:

            return {

                "success": False,

                "message": str(e)

            }

    # =================================================
    # MOUSE POSITION
    # =================================================

    def mouse_position(self):

        try:

            x, y = pyautogui.position()

            return {

                "success": True,

                "x": x,

                "y": y

            }

        except Exception as e:

            return {

                "success": False,

                "message": str(e)

            }

    # =================================================
    # MOVE MOUSE
    # =================================================

    def move(self, x, y, duration=0.3):

        try:

            pyautogui.moveTo(

                int(x),

                int(y),

                duration=float(duration)

            )

            return {

                "success": True,

                "message": f"Mouse moved to {x}, {y}.",

                "x": int(x),

                "y": int(y)

            }

        except Exception as e:

            return {

                "success": False,

                "message": str(e)

            }

    # =================================================
    # CLICK
    # =================================================

    def click(

        self,

        x=None,

        y=None,

        button="left",

        clicks=1,

        interval=0.1

    ):

        try:

            if x is not None and y is not None:

                pyautogui.click(

                    int(x),

                    int(y),

                    clicks=int(clicks),

                    interval=float(interval),

                    button=button

                )

            else:

                pyautogui.click(

                    clicks=int(clicks),

                    interval=float(interval),

                    button=button

                )

            return {

                "success": True,

                "message": "Click executed.",

                "button": button,

                "clicks": int(clicks)

            }

        except Exception as e:

            return {

                "success": False,

                "message": str(e)

            }

    # =================================================
    # DOUBLE CLICK
    # =================================================

    def double_click(self, x=None, y=None):

        return self.click(

            x=x,

            y=y,

            clicks=2

        )

    # =================================================
    # RIGHT CLICK
    # =================================================

    def right_click(self, x=None, y=None):

        return self.click(

            x=x,

            y=y,

            button="right"

        )

    # =================================================
    # TYPE TEXT
    # =================================================

    def type_text(

        self,

        text,

        interval=0.03

    ):

        try:

            text = str(text)

            pyautogui.write(

                text,

                interval=float(interval)

            )

            return {

                "success": True,

                "message": "Text typed successfully.",

                "text_length": len(text)

            }

        except Exception as e:

            return {

                "success": False,

                "message": str(e)

            }

    # =================================================
    # PRESS KEY
    # =================================================

    def press(

        self,

        key,

        presses=1,

        interval=0.1

    ):

        try:

            pyautogui.press(

                str(key),

                presses=int(presses),

                interval=float(interval)

            )

            return {

                "success": True,

                "message": f"Pressed {key}.",

                "key": str(key)

            }

        except Exception as e:

            return {

                "success": False,

                "message": str(e)

            }

    # =================================================
    # HOTKEY
    # =================================================

    def hotkey(self, *keys):

        try:

            keys = [

                str(key)

                for key in keys

            ]

            pyautogui.hotkey(

                *keys

            )

            return {

                "success": True,

                "message": (

                    "Hotkey executed: "

                    + " + ".join(keys)

                )

            }

        except Exception as e:

            return {

                "success": False,

                "message": str(e)

            }

    # =================================================
    # SCROLL
    # =================================================

    def scroll(

        self,

        amount,

        x=None,

        y=None

    ):

        try:

            if x is not None and y is not None:

                pyautogui.moveTo(

                    int(x),

                    int(y)

                )

            pyautogui.scroll(

                int(amount)

            )

            return {

                "success": True,

                "message": (

                    f"Scrolled {amount}."

                )

            }

        except Exception as e:

            return {

                "success": False,

                "message": str(e)

            }

    # =================================================
    # DRAG
    # =================================================

    def drag(

        self,

        start_x,

        start_y,

        end_x,

        end_y,

        duration=0.5,

        button="left"

    ):

        try:

            pyautogui.moveTo(

                int(start_x),

                int(start_y),

                duration=0.2

            )

            pyautogui.dragTo(

                int(end_x),

                int(end_y),

                duration=float(duration),

                button=button

            )

            return {

                "success": True,

                "message": (

                    "Drag completed successfully."

                )

            }

        except Exception as e:

            return {

                "success": False,

                "message": str(e)

            }

    # =================================================
    # WAIT
    # =================================================

    def wait(self, seconds):

        try:

            seconds = float(seconds)

            time.sleep(

                max(

                    0,

                    seconds

                )

            )

            return {

                "success": True,

                "message": (

                    f"Waited {seconds} seconds."

                )

            }

        except Exception as e:

            return {

                "success": False,

                "message": str(e)

            }

    # =================================================
    # SCREENSHOT
    # =================================================

    def screenshot(

        self,

        path="screenshots/screen.png"

    ):

        try:

            file_path = Path(path)

            file_path.parent.mkdir(

                parents=True,

                exist_ok=True

            )

            image = pyautogui.screenshot()

            image.save(

                str(file_path)

            )

            return {

                "success": True,

                "message": (

                    "Screenshot captured."

                ),

                "file": str(file_path)

            }

        except Exception as e:

            return {

                "success": False,

                "message": str(e)

            }

    # =================================================
    # EXECUTE STRUCTURED ACTION
    # =================================================

    def execute(

        self,

        action,

        **kwargs

    ):

        action = str(

            action

        ).strip().upper()

        # ---------------------------------------------

        if action == "MOVE":

            return self.move(

                kwargs.get("x"),

                kwargs.get("y"),

                kwargs.get(

                    "duration",

                    0.3

                )

            )

        # ---------------------------------------------

        if action == "CLICK":

            return self.click(

                kwargs.get("x"),

                kwargs.get("y"),

                kwargs.get(

                    "button",

                    "left"

                ),

                kwargs.get(

                    "clicks",

                    1

                ),

                kwargs.get(

                    "interval",

                    0.1

                )

            )

        # ---------------------------------------------

        if action == "DOUBLE_CLICK":

            return self.double_click(

                kwargs.get("x"),

                kwargs.get("y")

            )

        # ---------------------------------------------

        if action == "RIGHT_CLICK":

            return self.right_click(

                kwargs.get("x"),

                kwargs.get("y")

            )

        # ---------------------------------------------

        if action == "TYPE":

            return self.type_text(

                kwargs.get(

                    "text",

                    ""

                ),

                kwargs.get(

                    "interval",

                    0.03

                )

            )

        # ---------------------------------------------

        if action == "PRESS":

            return self.press(

                kwargs.get("key"),

                kwargs.get(

                    "presses",

                    1

                ),

                kwargs.get(

                    "interval",

                    0.1

                )

            )

        # ---------------------------------------------

        if action == "HOTKEY":

            keys = kwargs.get(

                "keys",

                []

            )

            return self.hotkey(

                *keys

            )

        # ---------------------------------------------

        if action == "SCROLL":

            return self.scroll(

                kwargs.get(

                    "amount",

                    0

                ),

                kwargs.get("x"),

                kwargs.get("y")

            )

        # ---------------------------------------------

        if action == "DRAG":

            return self.drag(

                kwargs.get(

                    "start_x"

                ),

                kwargs.get(

                    "start_y"

                ),

                kwargs.get(

                    "end_x"

                ),

                kwargs.get(

                    "end_y"

                ),

                kwargs.get(

                    "duration",

                    0.5

                ),

                kwargs.get(

                    "button",

                    "left"

                )

            )

        # ---------------------------------------------

        if action == "WAIT":

            return self.wait(

                kwargs.get(

                    "seconds",

                    1

                )

            )

        # ---------------------------------------------

        if action == "SCREENSHOT":

            return self.screenshot(

                kwargs.get(

                    "path",

                    "screenshots/screen.png"

                )

            )

        # ---------------------------------------------

        if action == "SCREEN_SIZE":

            return self.screen_size()

        # ---------------------------------------------

        if action == "MOUSE_POSITION":

            return self.mouse_position()

        # ---------------------------------------------

        return {

            "success": False,

            "message": (

                f"Unsupported desktop action: "

                f"{action}"

            )

        }


desktop_service = DesktopService()
