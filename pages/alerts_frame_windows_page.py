from pages.base_page import BasePage
from locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators, AlertsPageLocators
from selenium.common.exceptions import NoAlertPresentException
import time
import random


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


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def check_alert_appears_on_button_click(self):
        self.element_is_visible(self.locators.SIMPLE_ALERT_BUTTON).click()
        try:
            self.switch_to_alert()
            return True
        except NoAlertPresentException:
            return False

    def check_alert_is_not_appeared_on_button_click(self):
        self.element_is_visible(self.locators.TIMER_ALERT_BUTTON).click()
        try:
            self.switch_to_alert()
            return False
        except NoAlertPresentException:
            return True

    def check_alert_appears_after_five_seconds(self):
        time.sleep(5)
        try:
            self.switch_to_alert()
            return True
        except NoAlertPresentException:
            return False

    def close_confirm_alert_box(self, alert_action):
        self.element_is_visible(self.locators.CONFIRM_ACTION_ALERT_BUTTON).click()
        try:
            alert = self.switch_to_alert()
        except NoAlertPresentException:
            return False
        else:
            if alert_action == "accept":
                alert.accept()
            elif alert_action == "dismiss":
                alert.dismiss()
            result_text = self.element_is_present(self.locators.CONFIRM_ACTION_RESULT_MESSAGE).text
            return result_text

    def enter_random_text_in_prompt_alert_box(self):
        entered_text = f"random_text{random.randint(1, 999)}"
        self.element_is_visible(self.locators.PROMPT_BOX_ALERT_BUTTON).click()
        try:
            alert = self.switch_to_alert()
        except NoAlertPresentException:
            return entered_text, ""
        else:
            alert.send_keys(entered_text)
            alert.accept()
            result_text = self.element_is_present(self.locators.PROMPT_BOX_RESULT_MESSAGE).text
            return entered_text, result_text