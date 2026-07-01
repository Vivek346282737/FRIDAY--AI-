from browser.browser_actions import (
    open_website,
    google_search,
    click_text,
    scroll_page,
    take_screenshot,
    current_url,
    close_browser,
    read_page,
)


class BrowserAgent:

    def execute(self, instruction: str):

        text = instruction.strip()
        lower = text.lower()

        # -------------------------
        # Close Browser
        # -------------------------

        if lower == "close":
            return close_browser()

        # -------------------------
        # Screenshot
        # -------------------------

        if "screenshot" in lower:
            return take_screenshot()

        # -------------------------
        # Current URL
        # -------------------------

        if lower == "current url":
            return current_url()

        # -------------------------
        # Read Page
        # -------------------------

        if lower == "read page":
            return read_page()

        # -------------------------
        # Google Search
        # -------------------------

        if lower.startswith("search "):

            query = text[7:].strip()

            return google_search(query)

        # -------------------------
        # Click Text
        # -------------------------

        if lower.startswith("click "):

            target = text[6:].strip()

            return click_text(target)

        # -------------------------
        # Scroll
        # -------------------------

        if lower == "scroll":
            return scroll_page()

        # -------------------------
        # Open Website
        # -------------------------

        return open_website(text)


browser_agent = BrowserAgent()