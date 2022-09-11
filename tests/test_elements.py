from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablesPage
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
            assert button == output, f"Radio button '{button}' is not selected or output result is incorrect"

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