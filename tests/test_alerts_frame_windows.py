from pages.alerts_frame_windows_page import (BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage,
                                             ModalDialogsPage)
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

    class TestAlerts:
        link = "https://demoqa.com/alerts"

        def test_simple_alert_appears_on_the_page(self, browser):
            alerts_page = AlertsPage(browser, self.link)
            alerts_page.open()
            alert_appears = alerts_page.check_alert_appears_on_button_click()
            assert alert_appears, "Alert is not appeared on the page"

        def test_timer_alert_appears_after_five_seconds(self, browser):
            alerts_page = AlertsPage(browser, self.link)
            alerts_page.open()
            initially_is_not_appeared = alerts_page.check_alert_is_not_appeared_on_button_click()
            assert initially_is_not_appeared, "Alert appears on button click"
            appeared_after_five_seconds = alerts_page.check_alert_appears_after_five_seconds()
            assert appeared_after_five_seconds, "Alert is not appeared after five seconds"

        def test_confirm_alert_box_can_be_accepted(self, browser):
            alerts_page = AlertsPage(browser, self.link)
            alerts_page.open()
            result_text = alerts_page.close_confirm_alert_box(alert_action="accept")
            assert result_text == "You selected Ok", "Alert is not accepted"

        def test_confirm_alert_box_can_be_dismissed(self, browser):
            alerts_page = AlertsPage(browser, self.link)
            alerts_page.open()
            result_text = alerts_page.close_confirm_alert_box(alert_action="dismiss")
            assert result_text == "You selected Cancel", "Alert is not dismissed"

        def test_text_can_be_entered_in_prompt_alert_box(self, browser):
            alerts_page = AlertsPage(browser, self.link)
            alerts_page.open()
            entered_text, result_text = alerts_page.enter_random_text_in_prompt_alert_box()
            assert entered_text in result_text, "Text is not entered in prompt alert box"

    class TestFramesPage:
        link = "https://demoqa.com/frames"
        frames = ["frame1", "frame2"]

        @pytest.mark.parametrize("frame", frames)
        def test_title_is_displayed_inside_the_frame(self, browser, frame):
            frames_page = FramesPage(browser, self.link)
            frames_page.open()
            frame_title = frames_page.get_frame_title(frame)
            assert frame_title == "This is a sample page", "Incorrect title is displayed inside the frame"

    class TestNestedFramesPage:
        link = "https://demoqa.com/nestedframes"

        def test_child_frame_is_nested_in_parent_frame(self, browser):
            nested_frames_page = NestedFramesPage(browser, self.link)
            nested_frames_page.open()
            parent_frame_text, child_frame_text = nested_frames_page.get_text_of_frames()
            assert parent_frame_text == "Parent frame", "Incorrect parent frame text"
            assert child_frame_text == "Child Iframe", "Incorrect child frame text"
            frame_is_nested = nested_frames_page.check_that_frame_is_nested()
            assert frame_is_nested, "Child frame is not nested in parent frame"

    class TestModalDialogsPage:
        link = "https://demoqa.com/modal-dialogs"
        modal_dialog_titles = ["Small Modal", "Large Modal"]

        @pytest.mark.parametrize("dialog_title", modal_dialog_titles)
        def test_modal_dialog_is_opened_on_button_click(self, browser, dialog_title):
            modal_dialogs_page = ModalDialogsPage(browser, self.link)
            modal_dialogs_page.open()
            modal_dialog_is_opened = modal_dialogs_page.check_button_click_opens_modal_dialog(dialog_title)
            assert modal_dialog_is_opened, "Modal dialog is not opened on button click"

        @pytest.mark.parametrize("dialog_title", modal_dialog_titles)
        def test_modal_dialog_has_title_and_content(self, browser, dialog_title):
            modal_dialogs_page = ModalDialogsPage(browser, self.link)
            modal_dialogs_page.open()
            actual_dialog_title, dialog_content = modal_dialogs_page.get_modal_dialog_title_and_content(dialog_title)
            assert actual_dialog_title == dialog_title, "Modal dialog has incorrect title"
            assert dialog_content, "Modal dialog content is absent"