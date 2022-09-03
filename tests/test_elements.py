from pages.elements_page import TextBoxPage


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