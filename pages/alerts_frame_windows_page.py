from pages.base_page import BasePage
from locators.alerts_frame_windows_page_locators import (BrowserWindowsPageLocators, AlertsPageLocators,
                                                         FramesPageLocators, NestedFramesPageLocators,
                                                         ModalDialogsPageLocators)
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
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


class FramesPage(BasePage):
    locators = FramesPageLocators()

    def get_frame_title(self, frame_number):
        frames = {"frame1": self.locators.FRAME_ONE, "frame2": self.locators.FRAME_TWO}
        frame = self.element_is_present(frames[frame_number])
        self.switch_to_frame(frame)
        frame_title = self.element_is_visible(self.locators.FRAME_TITLE).text
        return frame_title


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    def get_text_of_frames(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.switch_to_frame(parent_frame)
        parent_frame_text = self.element_is_present(self.locators.PARENT_FRAME_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.switch_to_frame(child_frame)
        child_frame_text = self.element_is_present(self.locators.CHILD_FRAME_TEXT).text
        return parent_frame_text, child_frame_text

    def check_that_frame_is_nested(self):
        self.switch_to_default_content()
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.switch_to_frame(parent_frame)
        try:
            child_frame = self.element_is_present(self.locators.CHILD_FRAME)
            self.switch_to_frame(child_frame)
            return True
        except TimeoutException:
            return False


class ModalDialogsPage(BasePage):
    locators = ModalDialogsPageLocators()

    def check_button_click_opens_modal_dialog(self, modal_dialog_button):
        modal_dialogs = {"Small Modal": {"modal_button": self.locators.SMALL_MODAL_BUTTON,
                                         "modal_dialog": self.locators.SMALL_MODAL_DIALOG,
                                         "close_button": self.locators.SMALL_MODAL_DIALOG_CLOSE_BUTTON},
                         "Large Modal": {"modal_button": self.locators.LARGE_MODAL_BUTTON,
                                         "modal_dialog": self.locators.LARGE_MODAL_DIALOG,
                                         "close_button": self.locators.LARGE_MODAL_DIALOG_CLOSE_BUTTON}}
        self.element_is_visible(modal_dialogs[modal_dialog_button]["modal_button"]).click()
        try:
            self.element_is_visible(modal_dialogs[modal_dialog_button]["modal_dialog"])
        except TimeoutException:
            return False
        else:
            self.element_is_visible(modal_dialogs[modal_dialog_button]["close_button"]).click()
            return True

    def get_modal_dialog_title_and_content(self, modal_dialog_button):
        modal_dialogs = {"Small Modal": {"modal_button": self.locators.SMALL_MODAL_BUTTON,
                                         "modal_dialog_title": self.locators.SMALL_MODAL_DIALOG_TITLE,
                                         "modal_dialog_content": self.locators.SMALL_MODAL_DIALOG_CONTENT},
                         "Large Modal": {"modal_button": self.locators.LARGE_MODAL_BUTTON,
                                         "modal_dialog_title": self.locators.LARGE_MODAL_DIALOG_TITLE,
                                         "modal_dialog_content": self.locators.LARGE_MODAL_DIALOG_CONTENT}}
        self.element_is_visible(modal_dialogs[modal_dialog_button]["modal_button"]).click()
        modal_dialog_title = self.element_is_present(modal_dialogs[modal_dialog_button]["modal_dialog_title"]).text
        modal_dialog_content = self.element_is_present(modal_dialogs[modal_dialog_button]["modal_dialog_content"]).text
        return modal_dialog_title, modal_dialog_content