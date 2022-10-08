from pages.alerts_frame_windows_page import BrowserWindowsPage
import pytest


class TestAlertsFrameWindows:
    class TestBrowserWindows:
        link = "https://demoqa.com/browser-windows"
        new_window_buttons = ["New Tab", "New Window", "New Window Message"]

        @pytest.mark.parametrize("button", new_window_buttons)
        def test_new_browser_window_is_opened_on_button_click(self, browser, button):
            browser_windows_page = BrowserWindowsPage(browser, self.link)
            browser_windows_page.open()
            windows_count = browser_windows_page.check_button_click_opens_new_window(button)
            assert windows_count == 2, "New window is not opened"