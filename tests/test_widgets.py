from pages.widgets_page import AccordianPage, AutoCompletePage
import pytest


class TestWidgets:
    class TestAccordian:
        link = "https://demoqa.com/accordian"
        accordian_sections = ["section1", "section2", "section3"]

        @pytest.mark.parametrize("section", accordian_sections)
        def test_accordian_section_can_be_opened_and_closed(self, browser, section):
            accordian_page = AccordianPage(browser, self.link)
            accordian_page.open()
            is_opened, is_closed = accordian_page.open_and_close_accordian_section(section)
            assert is_opened, "Accordian section is not opened"
            assert is_closed, "Accordian section is not closed"

        @pytest.mark.parametrize("section", accordian_sections)
        def test_accordian_section_has_title_and_content(self, browser, section):
            accordian_page = AccordianPage(browser, self.link)
            accordian_page.open()
            section_title, section_content = accordian_page.get_accordian_section_title_and_content(section)
            assert section_title, "Accordian section title is absent"
            assert section_content, "Accordian section content is absent"

    class TestAutoComplete:
        link = "https://demoqa.com/auto-complete"

        @pytest.fixture(scope="function")
        def field_with_multiple_color_names(self, browser):
            page = AutoCompletePage(browser, self.link)
            page.open()
            page.enter_multiple_color_names()
            return page

        def test_multiple_color_names_can_be_entered_in_multi_input_field_via_autocomplete(self, browser):
            autocomplete_page = AutoCompletePage(browser, self.link)
            autocomplete_page.open()
            input_colors = autocomplete_page.enter_multiple_color_names_via_autocomplete()
            output_colors = autocomplete_page.get_color_names_of_multi_input_field()
            assert input_colors == output_colors, "Multiple color names are not entered via autocomplete"

        def test_each_color_name_can_be_removed_from_multi_input_field(self, browser, field_with_multiple_color_names):
            autocomplete_page = field_with_multiple_color_names
            autocomplete_page.remove_each_color_name()
            number_of_output_colors = autocomplete_page.get_number_of_color_names(field="multi")
            assert number_of_output_colors == 0, "Some color names are not removed from multi input field"

        def test_all_color_names_can_be_removed_from_multi_input_field(self, browser, field_with_multiple_color_names):
            autocomplete_page = field_with_multiple_color_names
            autocomplete_page.remove_all_color_names()
            number_of_output_colors = autocomplete_page.get_number_of_color_names(field="multi")
            assert number_of_output_colors == 0, "All color names are not removed from multi input field"

        def test_single_color_name_can_be_entered_in_single_input_field_via_autocomplete(self, browser):
            autocomplete_page = AutoCompletePage(browser, self.link)
            autocomplete_page.open()
            input_color = autocomplete_page.enter_single_color_name_via_autocomplete()
            output_color = autocomplete_page.get_color_name_of_single_input_field()
            assert input_color == output_color, "Single color name is not entered via autocomplete"

        def test_more_than_one_color_name_cannot_be_entered_in_single_input_field(self, browser):
            autocomplete_page = AutoCompletePage(browser, self.link)
            autocomplete_page.open()
            autocomplete_page.enter_two_color_names()
            number_of_output_colors = autocomplete_page.get_number_of_color_names(field="single")
            assert number_of_output_colors == 1, "Several color names can be entered in single input field"