from desktop.desktop_controller import desktop


# ==========================================
# SCREEN
# ==========================================

def screenshot():
    return desktop.screenshot()


def screen_size():
    return desktop.screen_size()


def mouse_position():
    return desktop.mouse_position()


# ==========================================
# MOUSE
# ==========================================

def move_mouse(x, y):
    return desktop.move(x, y)


def left_click():
    return desktop.click()


def double_click():
    return desktop.double_click()


def right_click():
    return desktop.right_click()


def scroll_up():
    return desktop.scroll(500)


def scroll_down():
    return desktop.scroll(-500)


# ==========================================
# KEYBOARD
# ==========================================

def type_text(text):
    return desktop.type(text)


def press_key(key):
    return desktop.press(key)


def press_hotkey(*keys):
    return desktop.hotkey(*keys)


# ==========================================
# CLIPBOARD
# ==========================================

def copy_text(text):
    return desktop.copy(text)


def paste():
    return desktop.paste()


# ==========================================
# WAIT
# ==========================================

def wait(seconds):
    return desktop.wait(seconds)