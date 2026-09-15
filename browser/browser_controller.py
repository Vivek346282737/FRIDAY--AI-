import os
import time
import subprocess
import urllib.parse

import pyautogui
import pyperclip

try:
    import pygetwindow as gw
except ImportError:
    gw = None


class BrowserController:

    def __init__(self):

        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.15

        self.chrome_paths = [

            r"C:\Program Files\Google\Chrome\Application\chrome.exe",

            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",

            os.path.expandvars(
                r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"
            )

        ]


    # ==================================================
    # INTERNAL HELPERS
    # ==================================================

    def _get_chrome_path(self):

        for path in self.chrome_paths:

            if os.path.exists(path):

                return path

        return None


    def _get_chrome_windows(self):

        if gw is None:

            return []

        try:

            windows = []

            for window in gw.getAllWindows():

                title = (
                    window.title
                    or ""
                ).strip()

                lower_title = title.lower()

                if (
                    "chrome" in lower_title
                    and lower_title not in {
                        "google chrome",
                        "who's using chrome?"
                    }
                ):

                    windows.append(
                        window
                    )

            return windows

        except Exception:

            return []


    def _focus_chrome(self, timeout=8):

        if gw is None:

            return {

                "success": True,

                "message": (
                    "Chrome focus control unavailable."
                )

            }

        start_time = time.time()

        while (

            time.time() - start_time
            < timeout

        ):

            windows = self._get_chrome_windows()

            if windows:

                window = windows[0]

                try:

                    if window.isMinimized:

                        window.restore()

                        time.sleep(0.5)

                except Exception:

                    pass

                try:

                    window.activate()

                    time.sleep(1)

                except Exception:

                    pass

                return {

                    "success": True,

                    "message": (
                        "Chrome window focused."
                    )

                }

            time.sleep(0.3)

        return {

            "success": False,

            "message": (
                "Could not find a Chrome window."
            )

        }


    def _ensure_chrome(self):

        windows = self._get_chrome_windows()

        if windows:

            return self._focus_chrome()

        result = self.open_chrome()

        if not result.get(

            "success",

            False

        ):

            return result

        return self._focus_chrome(
            timeout=8
        )


    def _copy_and_paste(self, text):

        pyperclip.copy(
            str(text)
        )

        time.sleep(0.2)

        pyautogui.hotkey(

            "ctrl",

            "v"

        )


    def _address_bar(self, url):

        focus_result = self._ensure_chrome()

        if not focus_result.get(

            "success",

            False

        ):

            return focus_result

        time.sleep(0.5)

        pyautogui.hotkey(

            "ctrl",

            "l"

        )

        time.sleep(0.3)

        self._copy_and_paste(
            url
        )

        time.sleep(0.3)

        pyautogui.press(
            "enter"
        )

        return {

            "success": True

        }


    def _run_hotkey(self, *keys):

        focus_result = self._ensure_chrome()

        if not focus_result.get(

            "success",

            False

        ):

            return focus_result

        time.sleep(0.3)

        pyautogui.hotkey(
            *keys
        )

        return {

            "success": True

        }


    # ==================================================
    # OPEN CHROME
    # ==================================================

    def open_chrome(self, url=None):

        existing_windows = (
            self._get_chrome_windows()
        )

        if existing_windows:

            result = self._focus_chrome()

            if url:

                self._address_bar(
                    url
                )

            return result

        chrome = self._get_chrome_path()

        if not chrome:

            return {

                "success": False,

                "message": (
                    "Google Chrome executable "
                    "was not found."
                )

            }

        try:

            command = [

                chrome,

                "--profile-directory=Default"

            ]

            if url:

                command.append(
                    url
                )

            subprocess.Popen(

                command,

                stdout=subprocess.DEVNULL,

                stderr=subprocess.DEVNULL

            )

            time.sleep(3)

            focus_result = self._focus_chrome(
                timeout=10
            )

            if not focus_result.get(

                "success",

                False

            ):

                return focus_result

            return {

                "success": True,

                "message": (
                    "Chrome opened and focused successfully."
                ),

                "url": url

            }

        except Exception as e:

            return {

                "success": False,

                "message": str(e)

            }


    # ==================================================
    # OPEN URL
    # ==================================================

    def open_url(self, url):

        if not url:

            return {

                "success": False,

                "message": (
                    "URL is empty."
                )

            }

        try:

            if not url.startswith(

                (

                    "http://",

                    "https://"

                )

            ):

                url = (
                    "https://" + url
                )

            result = self._address_bar(
                url
            )

            if not result.get(

                "success",

                False

            ):

                return result

            time.sleep(3)

            return {

                "success": True,

                "url": url,

                "message": (
                    f"Opened {url}"
                )

            }

        except Exception as e:

            return {

                "success": False,

                "message": str(e)

            }


    # ==================================================
    # GOOGLE SEARCH
    # ==================================================

    def google(self, query):

        if not query:

            return {

                "success": False,

                "message": (
                    "Search query is empty."
                )

            }

        encoded = urllib.parse.quote_plus(
            query
        )

        url = (

            "https://www.google.com/search?q="

            + encoded

        )

        result = self.open_url(
            url
        )

        if result.get(
            "success"
        ):

            result["query"] = query

            result["engine"] = "google"

        return result


    # ==================================================
    # BING SEARCH
    # ==================================================

    def bing(self, query):

        if not query:

            return {

                "success": False,

                "message": (
                    "Search query is empty."
                )

            }

        encoded = urllib.parse.quote_plus(
            query
        )

        url = (

            "https://www.bing.com/search?q="

            + encoded

        )

        result = self.open_url(
            url
        )

        if result.get(
            "success"
        ):

            result["query"] = query

            result["engine"] = "bing"

        return result


    # ==================================================
    # COMMON WEBSITES
    # ==================================================

    def open_chatgpt(self):

        return self.open_url(
            "https://chatgpt.com"
        )


    def open_youtube(self):

        return self.open_url(
            "https://www.youtube.com"
        )


    def open_spotify(self):

        return self.open_url(
            "https://open.spotify.com"
        )


    def open_gmail(self):

        return self.open_url(
            "https://mail.google.com"
        )


    def open_github(self):

        return self.open_url(
            "https://github.com"
        )


    def open_openai(self):

        return self.open_url(
            "https://openai.com"
        )


    # ==================================================
    # NAVIGATION
    # ==================================================

    def back(self):

        result = self._run_hotkey(

            "alt",

            "left"

        )

        if result.get(
            "success"
        ):

            time.sleep(2)

            result["message"] = (
                "Went back."
            )

        return result


    def forward(self):

        result = self._run_hotkey(

            "alt",

            "right"

        )

        if result.get(
            "success"
        ):

            time.sleep(2)

            result["message"] = (
                "Went forward."
            )

        return result


    def reload(self):

        result = self._run_hotkey(

            "ctrl",

            "r"

        )

        if result.get(
            "success"
        ):

            time.sleep(3)

            result["message"] = (
                "Page reloaded."
            )

        return result


    # ==================================================
    # TAB CONTROL
    # ==================================================

    def open_new_tab(self):

        result = self._run_hotkey(

            "ctrl",

            "t"

        )

        if result.get(
            "success"
        ):

            time.sleep(0.7)

            result["message"] = (
                "New tab opened."
            )

        return result


    def new_tab(self):

        return self.open_new_tab()


    def close_tab(self):

        result = self._run_hotkey(

            "ctrl",

            "w"

        )

        if result.get(
            "success"
        ):

            time.sleep(0.7)

            result["message"] = (
                "Current tab closed."
            )

        return result


    def next_tab(self):

        result = self._run_hotkey(

            "ctrl",

            "tab"

        )

        if result.get(
            "success"
        ):

            time.sleep(0.5)

            result["message"] = (
                "Switched to next tab."
            )

        return result


    def previous_tab(self):

        result = self._run_hotkey(

            "ctrl",

            "shift",

            "tab"

        )

        if result.get(
            "success"
        ):

            time.sleep(0.5)

            result["message"] = (
                "Switched to previous tab."
            )

        return result


    # ==================================================
    # HUMAN-LIKE SMOOTH SCROLL
    # ==================================================

    def _smooth_scroll(self, direction, amount=600):

        focus_result = self._ensure_chrome()

        if not focus_result.get(

            "success",

            False

        ):

            return focus_result

        try:

            screen_width, screen_height = (
                pyautogui.size()
            )

            pyautogui.moveTo(

                screen_width // 2,

                screen_height // 2,

                duration=0.25

            )

            amount = abs(
                int(amount)
            )

            if amount < 100:

                amount = 100

            steps = max(

                8,

                min(

                    30,

                    amount // 30

                )

            )

            base_step = max(

                1,

                amount // steps

            )

            for index in range(steps):

                progress = (

                    index + 1

                ) / steps

                multiplier = (

                    0.7

                    + (

                        0.6

                        * (

                            1

                            - abs(

                                (2 * progress)

                                - 1

                            )

                        )

                    )

                )

                current_step = max(

                    1,

                    int(

                        base_step

                        * multiplier

                    )

                )

                if direction == "down":

                    pyautogui.scroll(

                        -current_step

                    )

                else:

                    pyautogui.scroll(

                        current_step

                    )

                time.sleep(

                    0.015

                    + (

                        0.02

                        * (

                            index % 3

                        )

                    )

                )

            time.sleep(0.4)

            return {

                "success": True,

                "message": (
                    f"Smoothly scrolled {direction}."
                ),

                "amount": amount

            }

        except Exception as e:

            return {

                "success": False,

                "message": str(e)

            }


    def scroll_down(self, amount=600):

        return self._smooth_scroll(

            "down",

            amount

        )


    def scroll_up(self, amount=600):

        return self._smooth_scroll(

            "up",

            amount

        )


    # ==================================================
    # WAIT
    # ==================================================

    def wait(self, seconds=1):

        try:

            seconds = float(
                seconds
            )

            time.sleep(
                seconds
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


browser = BrowserController()
