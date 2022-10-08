from pages.base_page import BasePage
from locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_button_click_opens_new_window(self, button):
        buttons = {"New Tab": self.locators.NEW_TAB_BUTTON,
                   "New Window": self.locators.NEW_WINDOW_BUTTON,
                   "New Window Message": self.locators.NEW_WINDOW_MESSAGE_BUTTON}
        self.element_is_visible(buttons[button]).click()
        windows = self.browser.window_handles
        if len(windows) == 2:
            self.switch_to_opened_window()
        return len(windows)