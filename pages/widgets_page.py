from pages.base_page import BasePage
from locators.widgets_page_locators import AccordianPageLocators


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def open_and_close_accordian_section(self, section_number):
        accordian_sections = {"section1": self.locators.FIRST_SECTION_TITLE,
                              "section2": self.locators.SECOND_SECTION_TITLE,
                              "section3": self.locators.THIRD_SECTION_TITLE}
        section = self.element_is_visible(accordian_sections[section_number])
        result = []
        for _ in range(2):
            section.click()
            self.element_is_not_visible(self.locators.COLLAPSING_PROCESS)
            section_state = section.find_element(*self.locators.SECTION_COLLAPSE_STATE).get_attribute("class")
            result.append(section_state)
        return "collapse show" in result, "collapse" in result

    def get_accordian_section_title_and_content(self, section_number):
        accordian_sections = {"section1": {"title": self.locators.FIRST_SECTION_TITLE,
                                           "content": self.locators.FIRST_SECTION_CONTENT},
                              "section2": {"title": self.locators.SECOND_SECTION_TITLE,
                                           "content": self.locators.SECOND_SECTION_CONTENT},
                              "section3": {"title": self.locators.THIRD_SECTION_TITLE,
                                           "content": self.locators.THIRD_SECTION_CONTENT}}
        section = self.element_is_visible(accordian_sections[section_number]["title"])
        section_state = section.find_element(*self.locators.SECTION_COLLAPSE_STATE).get_attribute("class")
        if section_state == "collapse":
            section.click()
        accordian_section_title = section.text
        accordian_section_content = self.element_is_visible(accordian_sections[section_number]["content"]).text
        return accordian_section_title, accordian_section_content