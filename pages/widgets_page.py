from pages.base_page import BasePage
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators
from generator.generator import generated_colors
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys
import random


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


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()
    colors = generated_colors()

    def enter_multiple_color_names_via_autocomplete(self):
        multiple_colors = random.sample(self.colors, k=random.randint(2, len(self.colors)))
        multi_input_field = self.element_is_visible(self.locators.MULTIPLE_INPUT_FIELD)
        for color in multiple_colors:
            multi_input_field.send_keys(color[0])
            try:
                autocomplete_options = self.elements_are_present(self.locators.MULTI_AUTOCOMPLETE_OPTIONS)
            except TimeoutException:
                return None
            for option in autocomplete_options:
                if color == option.text:
                    option.click()
                    break
            else:
                return False
        return multiple_colors

    def enter_multiple_color_names(self):
        colors = random.sample(self.colors, k=random.randint(2, len(self.colors)))
        multi_input_field = self.element_is_visible(self.locators.MULTIPLE_INPUT_FIELD)
        for color in colors:
            multi_input_field.send_keys(color)
            multi_input_field.send_keys(Keys.ENTER)

    def get_color_names_of_multi_input_field(self):
        try:
            multiple_color_list = self.elements_are_visible(self.locators.MULTI_VALUE)
            return [color.text for color in multiple_color_list]
        except TimeoutException:
            return []

    def remove_each_color_name(self):
        list_of_remove_buttons = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE)
        for remove_button in list_of_remove_buttons:
            remove_button.click()

    def remove_all_color_names(self):
        self.element_is_visible(self.locators.MULTI_REMOVE_ALL_VALUES).click()

    def enter_single_color_name_via_autocomplete(self):
        color = random.choice(self.colors)
        single_input_field = self.element_is_visible(self.locators.SINGLE_INPUT_FIELD)
        single_input_field.send_keys(color[0])
        try:
            autocomplete_options = self.elements_are_present(self.locators.SINGLE_AUTOCOMPLETE_OPTIONS)
        except TimeoutException:
            return None
        for option in autocomplete_options:
            if color == option.text:
                option.click()
                break
        else:
            return False
        return color

    def get_color_name_of_single_input_field(self):
        try:
            color = self.element_is_visible(self.locators.SINGLE_VALUE)
            return color.text
        except TimeoutException:
            return ""

    def enter_two_color_names(self):
        colors = random.sample(self.colors, k=2)
        input_field = self.element_is_visible(self.locators.SINGLE_INPUT_FIELD)
        for color in colors:
            input_field.send_keys(color)
            input_field.send_keys(Keys.ENTER)

    def get_number_of_color_names(self, field):
        input_values = {"multi": self.locators.MULTI_VALUE, "single": self.locators.SINGLE_VALUE}
        try:
            color_list = self.elements_are_visible(input_values[field])
            return len(color_list)
        except TimeoutException:
            return 0