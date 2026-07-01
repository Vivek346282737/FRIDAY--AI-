import time
from datetime import datetime

import pyautogui
import pyperclip


class DesktopController:

    def __init__(self):

        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.2

    # ==================================================
    # SCREEN
    # ==================================================

    def screen_size(self):

        width, height = pyautogui.size()

        return {
            "width": width,
            "height": height
        }

    def mouse_position(self):

        x, y = pyautogui.position()

        return {
            "x": x,
            "y": y
        }

    # ==================================================
    # MOUSE
    # ==================================================

    def move(self, x, y, duration=0.3):

        pyautogui.moveTo(
            x,
            y,
            duration=duration
        )

        return {
            "success": True
        }

    def click(self):

        pyautogui.click()

        return {
            "success": True
        }

    def double_click(self):

        pyautogui.doubleClick()

        return {
            "success": True
        }

    def right_click(self):

        pyautogui.rightClick()

        return {
            "success": True
        }

    def drag(self, x, y, duration=0.5):

        pyautogui.dragTo(
            x,
            y,
            duration=duration
        )

        return {
            "success": True
        }

    def scroll(self, amount):

        pyautogui.scroll(amount)

        return {
            "success": True
        }

    # ==================================================
    # KEYBOARD
    # ==================================================

    def type(self, text):

        pyautogui.write(
            text,
            interval=0.02
        )

        return {
            "success": True
        }

    def press(self, key):

        pyautogui.press(key)

        return {
            "success": True
        }

    def hotkey(self, *keys):

        pyautogui.hotkey(*keys)

        return {
            "success": True
        }

    # ==================================================
    # CLIPBOARD
    # ==================================================

    def copy(self, text):

        pyperclip.copy(text)

        return {
            "success": True
        }

    def paste(self):

        pyautogui.hotkey("ctrl", "v")

        return {
            "success": True
        }

    # ==================================================
    # SCREENSHOT
    # ==================================================

    def screenshot(self):

        filename = datetime.now().strftime(
            "desktop_%Y%m%d_%H%M%S.png"
        )

        image = pyautogui.screenshot()

        image.save(filename)

        return {
            "success": True,
            "file": filename
        }

    # ==================================================
    # WAIT
    # ==================================================

    def wait(self, seconds):

        time.sleep(seconds)

        return {
            "success": True
        }


desktop = DesktopController()