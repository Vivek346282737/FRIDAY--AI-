from browser.browser_controller import browser


def start_browser():
    return browser.start()


def open_website(url: str):
    return browser.open(url)


def google_search(query: str):
    return browser.google(query)


def click_text(text: str):
    return browser.click_text(text)


def click_selector(selector: str):
    return browser.click_selector(selector)


def fill_input(
    selector: str,
    value: str
):
    return browser.fill(
        selector,
        value
    )


def type_text(text: str):
    return browser.type_text(text)


def press_key(key: str):
    return browser.press(key)


def scroll_page(pixels=1000):
    return browser.scroll(pixels)


def wait_seconds(seconds=1):
    return browser.wait(seconds)


def read_page():
    return browser.page_text()


def verify_text(text: str):
    return browser.contains_text(text)


def take_screenshot(path=None):
    return browser.screenshot(path)


def current_url():
    return browser.current_url()


def go_back():
    return browser.back()


def go_forward():
    return browser.forward()


def refresh_page():
    return browser.refresh()


def close_browser():
    return browser.close()
