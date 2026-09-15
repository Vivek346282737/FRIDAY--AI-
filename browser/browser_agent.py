from browser.browser_controller import browser


class BrowserAgent:

    def execute(self, instruction):

        if not instruction:

            return {

                "success": False,

                "message": (
                    "Browser instruction is empty."
                )

            }

        text = str(
            instruction
        ).strip()

        lower = text.lower()

        try:

            # ==========================================
            # OPEN CHROME
            # ==========================================

            if lower == "open chrome":

                return browser.open_chrome()


            # ==========================================
            # WAIT
            # ==========================================

            if lower.startswith(
                "wait "
            ):

                value = text[5:].strip()

                value = value.replace(

                    "seconds",

                    ""

                ).replace(

                    "second",

                    ""

                ).strip()

                seconds = float(
                    value
                )

                return browser.wait(
                    seconds
                )


            # ==========================================
            # SEARCH
            # ==========================================

            if lower.startswith(
                "search google "
            ):

                query = text[14:].strip()

                return browser.google(
                    query
                )


            if lower.startswith(
                "google "
            ):

                query = text[7:].strip()

                return browser.google(
                    query
                )


            if lower.startswith(
                "search bing "
            ):

                query = text[12:].strip()

                return browser.bing(
                    query
                )


            if lower.startswith(
                "bing "
            ):

                query = text[5:].strip()

                return browser.bing(
                    query
                )


            if lower.startswith(
                "search "
            ):

                query = text[7:].strip()

                return browser.google(
                    query
                )


            # ==========================================
            # OPEN URL
            # ==========================================

            if lower.startswith(
                "open url "
            ):

                url = text[9:].strip()

                return browser.open_url(
                    url
                )


            # ==========================================
            # COMMON WEBSITES
            # ==========================================

            if lower in (

                "open chatgpt",

                "chatgpt"

            ):

                return browser.open_chatgpt()


            if lower in (

                "open youtube",

                "youtube"

            ):

                return browser.open_youtube()


            if lower in (

                "open spotify",

                "spotify"

            ):

                return browser.open_spotify()


            if lower in (

                "open gmail",

                "gmail"

            ):

                return browser.open_gmail()


            if lower in (

                "open github",

                "github"

            ):

                return browser.open_github()


            if lower in (

                "open openai",

                "openai website"

            ):

                return browser.open_openai()


            # ==========================================
            # NAVIGATION
            # ==========================================

            if lower in (

                "back",

                "go back"

            ):

                return browser.back()


            if lower in (

                "forward",

                "go forward"

            ):

                return browser.forward()


            if lower in (

                "reload",

                "refresh",

                "reload page",

                "refresh page"

            ):

                return browser.reload()


            # ==========================================
            # TAB CONTROL
            # ==========================================

            if lower in (

                "new tab",

                "open new tab"

            ):

                return browser.open_new_tab()


            if lower in (

                "close tab",

                "close current tab"

            ):

                return browser.close_tab()


            if lower in (

                "next tab",

                "switch next tab"

            ):

                return browser.next_tab()


            if lower in (

                "previous tab",

                "switch previous tab"

            ):

                return browser.previous_tab()


            # ==========================================
            # SCROLL
            # ==========================================

            if lower == "scroll down":

                return browser.scroll_down()


            if lower == "scroll up":

                return browser.scroll_up()


            if lower.startswith(
                "scroll down "
            ):

                value = text[12:].strip()

                value = value.replace(

                    "pixels",

                    ""

                ).replace(

                    "pixel",

                    ""

                ).strip()

                amount = int(
                    value
                )

                return browser.scroll_down(
                    amount
                )


            if lower.startswith(
                "scroll up "
            ):

                value = text[10:].strip()

                value = value.replace(

                    "pixels",

                    ""

                ).replace(

                    "pixel",

                    ""

                ).strip()

                amount = int(
                    value
                )

                return browser.scroll_up(
                    amount
                )


            return {

                "success": False,

                "message": (
                    f"Unknown browser instruction: {text}"
                )

            }


        except Exception as e:

            return {

                "success": False,

                "message": str(e)

            }


browser_agent = BrowserAgent()
