from unittest.mock import patch

from browser.browser_agent import browser_agent


def test_open():

    with patch(
        "browser.browser_agent.open_website"
    ) as mock_open:

        mock_open.return_value = {
            "success": True
        }

        result = browser_agent.execute(
            "open google.com"
        )

        print(
            "OPEN RESULT:",
            result
        )

        print(
            "OPEN CALLED:",
            mock_open.call_args
        )


def test_scroll():

    with patch(
        "browser.browser_agent.scroll_page"
    ) as mock_scroll:

        mock_scroll.return_value = {
            "success": True
        }

        result = browser_agent.execute(
            "scroll down"
        )

        print(
            "SCROLL RESULT:",
            result
        )

        print(
            "SCROLL CALLED:",
            mock_scroll.call_args
        )


def test_fill():

    with patch(
        "browser.browser_agent.fill_input"
    ) as mock_fill:

        mock_fill.return_value = {
            "success": True
        }

        result = browser_agent.execute(
            "fill input[name=email] | test@example.com"
        )

        print(
            "FILL RESULT:",
            result
        )

        print(
            "FILL CALLED:",
            mock_fill.call_args
        )


test_open()
print()

test_scroll()
print()

test_fill()
