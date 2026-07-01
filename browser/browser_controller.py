from playwright.sync_api import sync_playwright


class BrowserController:

    def __init__(self):

        self.playwright = None
        self.browser = None
        self.page = None

    # =====================================================
    # INTERNAL
    # =====================================================

    def _is_alive(self):

        try:

            if self.page is None:
                return False

            self.page.title()

            return True

        except:

            return False

    def _reset(self):

        try:

            if self.browser:
                self.browser.close()

        except:
            pass

        try:

            if self.playwright:
                self.playwright.stop()

        except:
            pass

        self.playwright = None
        self.browser = None
        self.page = None

    # =====================================================
    # START
    # =====================================================

    def start(self, headless=False):

        if self._is_alive():
            return

        self._reset()

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=headless
        )

        self.page = self.browser.new_page()

    # =====================================================
    # ENSURE
    # =====================================================

    def ensure(self):

        if not self._is_alive():

            self.start()

    # =====================================================
    # OPEN WEBSITE
    # =====================================================

    def open(self, url: str):

        self.ensure()

        if not url.startswith("http"):

            url = "https://" + url

        try:

            self.page.goto(
                url,
                wait_until="networkidle"
            )

        except:

            self.start()

            self.page.goto(
                url,
                wait_until="networkidle"
            )

        return {
            "success": True,
            "url": self.page.url
        }

    # =====================================================
    # GOOGLE SEARCH
    # =====================================================

    def google(self, query: str):

        self.ensure()

        try:

            self.page.goto(
                "https://www.google.com",
                wait_until="networkidle"
            )

        except:

            self.start()

            self.page.goto(
                "https://www.google.com",
                wait_until="networkidle"
            )

        self.page.locator(
            "textarea[name='q']"
        ).fill(query)

        self.page.keyboard.press("Enter")

        self.page.wait_for_load_state(
            "networkidle"
        )

        return {
            "success": True,
            "query": query,
            "url": self.page.url
        }

    # =====================================================
    # CLICK TEXT
    # =====================================================

    def click_text(self, text: str):

        self.ensure()

        self.page.get_by_text(
            text,
            exact=False
        ).first.click()

        self.page.wait_for_load_state(
            "networkidle"
        )

        return {
            "success": True,
            "clicked": text
        }

    # =====================================================
    # FILL INPUT
    # =====================================================

    def fill(self, selector, value):

        self.ensure()

        self.page.locator(selector).fill(value)

        return {
            "success": True
        }

    # =====================================================
    # PRESS KEY
    # =====================================================

    def press(self, key):

        self.ensure()

        self.page.keyboard.press(key)

        return {
            "success": True
        }

    # =====================================================
    # SCROLL
    # =====================================================

    def scroll(self, pixels=1000):

        self.ensure()

        self.page.mouse.wheel(
            0,
            pixels
        )

        return {
            "success": True
        }

    # =====================================================
    # PAGE TEXT
    # =====================================================

    def page_text(self):

        self.ensure()

        return self.page.locator(
            "body"
        ).inner_text()

    # =====================================================
    # SCREENSHOT
    # =====================================================

    def screenshot(self, path="browser.png"):

        self.ensure()

        self.page.screenshot(path=path)

        return {
            "success": True,
            "file": path
        }

    # =====================================================
    # URL
    # =====================================================

    def current_url(self):

        self.ensure()

        return self.page.url

    # =====================================================
    # REFRESH
    # =====================================================

    def refresh(self):

        self.ensure()

        self.page.reload()

        self.page.wait_for_load_state(
            "networkidle"
        )

        return {
            "success": True
        }

    # =====================================================
    # BACK
    # =====================================================

    def back(self):

        self.ensure()

        self.page.go_back()

        return {
            "success": True
        }

    # =====================================================
    # FORWARD
    # =====================================================

    def forward(self):

        self.ensure()

        self.page.go_forward()

        return {
            "success": True
        }

    # =====================================================
    # CLOSE
    # =====================================================

    def close(self):

        self._reset()

        return {
            "success": True
        }


browser = BrowserController()