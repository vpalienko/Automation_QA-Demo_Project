from pages.widgets_page import AccordianPage
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