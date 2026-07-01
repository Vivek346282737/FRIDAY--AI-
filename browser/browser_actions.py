from browser.browser_controller import browser


def open_website(url: str):
    return browser.open(url)


def google_search(query: str):
    return browser.google(query)


def click_text(text: str):
    return browser.click_text(text)


def fill_input(selector: str, value: str):
    return browser.fill(selector, value)


def press_key(key: str):
    return browser.press(key)


def scroll_page(pixels=1000):
    return browser.scroll(pixels)


def read_page():
    return {
        "success": True,
        "text": browser.page_text()
    }


def take_screenshot(path="browser.png"):
    return browser.screenshot(path)


def current_url():
    return {
        "success": True,
        "url": browser.current_url()
    }


def close_browser():
    browser.close()

    return {
        "success": True,
        "message": "Browser closed successfully."
    }