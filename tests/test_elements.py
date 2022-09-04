from pages.elements_page import TextBoxPage, CheckBoxPage


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