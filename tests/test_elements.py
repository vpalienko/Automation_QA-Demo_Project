from pages.elements_page import (TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablesPage, ButtonsPage, LinksPage,
                                 BrokenLinksImagesPage, UploadAndDownloadPage, DynamicPropertiesPage)
import pytest
import random


class TestElements:
    class TestTextBox:
        link = "https://demoqa.com/text-box"

        def test_text_box_form_can_be_filled(self, browser):
            text_box_page = TextBoxPage(browser, self.link)
            text_box_page.open()
            full_name = text_box_page.input_full_name()
            email = text_box_page.input_email()
            current_address = text_box_page.input_current_address()
            permanent_address = text_box_page.input_permanent_address()
            text_box_page.submit_form()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
            assert full_name == output_name, "Full name does not match the output"
            assert email == output_email, "Email does not match the output"
            assert current_address == output_cur_addr, "Current address does not match the output"
            assert permanent_address == output_per_addr, "Permanent address does not match the output"

    class TestCheckBox:
        link = "https://demoqa.com/checkbox"

        def test_items_can_be_expanded_and_collapsed(self, browser):
            check_box_page = CheckBoxPage(browser, self.link)
            check_box_page.open()
            number_of_items_before_expand = check_box_page.get_number_of_items()
            check_box_page.expand_all_items()
            number_of_items_after_expand = check_box_page.get_number_of_items()
            check_box_page.collapse_all_items()
            number_of_items_after_collapse = check_box_page.get_number_of_items()
            assert number_of_items_before_expand < number_of_items_after_expand, "Items are not expanded"
            assert number_of_items_before_expand == number_of_items_after_collapse, "Items are not collapsed"

        def test_select_random_checkboxes(self, browser):
            check_box_page = CheckBoxPage(browser, self.link)
            check_box_page.open()
            check_box_page.expand_all_items()
            check_box_page.click_random_checkboxes()
            input_checkboxes = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkboxes == output_result, "Selected checkboxes do not match the output checkboxes"

    class TestRadioButton:
        link = "https://demoqa.com/radio-button"
        radio_buttons = ["Yes", "Impressive", pytest.param("No", marks=pytest.mark.xfail(reason="button disabled"))]

        @pytest.mark.parametrize("button", radio_buttons)
        def test_radio_button_can_be_selected(self, browser, button):
            radio_button_page = RadioButtonPage(browser, self.link)
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button(button)
            output = radio_button_page.get_output_result()
            assert button == output, "Radio button is not selected or output result is incorrect"

    class TestWebTables:
        link = "https://demoqa.com/webtables"

        def test_new_person_can_be_added(self, browser):
            web_tables_page = WebTablesPage(browser, self.link)
            web_tables_page.open()
            new_person = web_tables_page.add_new_person()
            table_result = web_tables_page.get_list_of_persons_in_table()
            assert new_person in table_result, "New person is not added to the table"

        def test_person_can_be_found_via_search(self, browser):
            web_tables_page = WebTablesPage(browser, self.link)
            web_tables_page.open()
            added_person = web_tables_page.add_new_person()
            keyword_for_search = added_person[random.randrange(len(added_person))]
            web_tables_page.search_for_person_by_keyword(keyword_for_search)
            search_result = web_tables_page.get_list_of_persons_in_table()
            assert added_person in search_result, "Person is not found"

        def test_person_information_can_be_updated(self, browser):
            web_tables_page = WebTablesPage(browser, self.link)
            web_tables_page.open()
            added_person = web_tables_page.add_new_person()
            web_tables_page.search_for_person_by_keyword(added_person[3])
            updated_person = web_tables_page.update_person_information()
            web_tables_page.search_for_person_by_keyword(updated_person[3])
            table_result = web_tables_page.get_list_of_persons_in_table()
            assert updated_person in table_result, "Person information is not updated"

        def test_person_can_be_deleted(self, browser):
            web_tables_page = WebTablesPage(browser, self.link)
            web_tables_page.open()
            added_person = web_tables_page.add_new_person()
            web_tables_page.search_for_person_by_keyword(added_person[3])
            web_tables_page.delete_person()
            table_result = web_tables_page.get_list_of_persons_in_table()
            assert "No rows found" in table_result, "Person is not deleted"

        def test_number_of_table_rows_can_be_changed(self, browser):
            web_tables_page = WebTablesPage(browser, self.link)
            web_tables_page.open()
            number_of_rows_per_page, number_of_rows_in_table = web_tables_page.change_number_of_rows_per_page()
            assert number_of_rows_per_page == number_of_rows_in_table, "The number of rows in the table is not changed"

    class TestButtons:
        link = "https://demoqa.com/buttons"

        def test_different_types_of_mouse_clicks(self, browser):
            buttons_page = ButtonsPage(browser, self.link)
            buttons_page.open()
            double_click_button = buttons_page.perform_double_click_with_mouse()
            right_click_button = buttons_page.perform_right_click_with_mouse()
            single_click_button = buttons_page.perform_single_click_with_mouse()
            assert double_click_button == "You have done a double click", "'Double Click Me' button is not pressed"
            assert right_click_button == "You have done a right click", "'Right Click Me' button is not pressed"
            assert single_click_button == "You have done a dynamic click", "'Click Me' button is not pressed"

    class TestLinks:
        link = "https://demoqa.com/links"
        new_tab_links = ["Simple link", "Dynamic link"]
        api_call_links = [("201", "Created"), ("204", "No Content"), ("301", "Moved Permanently"),
                          ("400", "Bad Request"), ("401", "Unauthorized"), ("403", "Forbidden"), ("404", "Not Found")]

        @pytest.mark.parametrize("link", new_tab_links)
        def test_link_is_opened_in_new_tab(self, browser, link):
            links_page = LinksPage(browser, self.link)
            links_page.open()
            tabs_count, status_code = links_page.check_link_opened_in_new_tab(link)
            assert tabs_count == 2 and status_code < 400, "Link is not opened in a new tab or link is incorrect"

        @pytest.mark.parametrize("code, status", api_call_links)
        def test_link_should_send_api_call(self, browser, code, status):
            links_page = LinksPage(browser, self.link)
            links_page.open()
            returned_code, returned_status = links_page.check_link_sends_api_call(status)
            message = links_page.get_output_message()
            assert returned_code == code and returned_status == status, "Incorrect code or status is returned"
            assert returned_code in message and returned_status in message, "Incorrect code or status is displayed"

    class TestBrokenLinksImages:
        link = "https://demoqa.com/broken"
        image_links = ["Valid image", pytest.param("Broken image", marks=pytest.mark.xfail(reason="known issue"))]
        url_links = ["Valid Link", pytest.param("Broken Link", marks=pytest.mark.xfail(reason="known issue"))]

        @pytest.mark.parametrize("image", image_links)
        def test_image_link_is_valid(self, browser, image):
            broken_links_images_page = BrokenLinksImagesPage(browser, self.link)
            broken_links_images_page.open()
            visible_image = broken_links_images_page.check_image_is_visible(image)
            assert visible_image, "Image link is broken"

        @pytest.mark.parametrize("link", url_links)
        def test_url_link_is_valid(self, browser, link):
            broken_links_images_page = BrokenLinksImagesPage(browser, self.link)
            broken_links_images_page.open()
            valid_link = broken_links_images_page.check_link_is_valid(link)
            assert valid_link, "URL link is broken"

    class TestUploadAndDownload:
        link = "https://demoqa.com/upload-download"

        def test_file_can_be_downloaded(self, browser):
            upload_and_download_page = UploadAndDownloadPage(browser, self.link)
            upload_and_download_page.open()
            upload_and_download_page.download_file()
            file_exists = upload_and_download_page.check_downloaded_file_exists()
            assert file_exists, "File is not downloaded"

        def test_file_can_be_uploaded(self, browser, blank_file):
            upload_and_download_page = UploadAndDownloadPage(browser, self.link)
            upload_and_download_page.open()
            test_file = blank_file(file_format="txt")
            file_name = upload_and_download_page.upload_file(test_file)
            assert file_name, "File is not uploaded"
            output_path = upload_and_download_page.get_upload_path()
            assert file_name in output_path, "Output path is incorrect"

    class TestDynamicProperties:
        link = "https://demoqa.com/dynamic-properties"

        def test_button_enables_after_five_seconds(self, browser):
            dynamic_properties_page = DynamicPropertiesPage(browser, self.link)
            dynamic_properties_page.open()
            initially_disabled = dynamic_properties_page.check_button_is_disabled_by_default()
            assert initially_disabled, "Button is not disabled by default"
            enabled_after_five_seconds = dynamic_properties_page.check_button_is_enabled_after_five_seconds()
            assert enabled_after_five_seconds, "Button is not enabled after five seconds"

        def test_button_color_changes_after_five_seconds(self, browser):
            dynamic_properties_page = DynamicPropertiesPage(browser, self.link)
            dynamic_properties_page.open()
            color_before, color_after = dynamic_properties_page.check_button_color_is_changed_after_five_seconds()
            assert color_before != color_after, "Button color is not changed after five seconds"

        def test_button_appears_after_five_seconds(self, browser):
            dynamic_properties_page = DynamicPropertiesPage(browser, self.link)
            dynamic_properties_page.open()
            initially_is_absent = dynamic_properties_page.check_button_is_absent_by_default()
            assert initially_is_absent, "Button is present by default"
            appeared_after_five_seconds = dynamic_properties_page.check_button_is_appeared_after_five_seconds()
            assert appeared_after_five_seconds, "Button is not appeared after five seconds"