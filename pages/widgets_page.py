from pages.base_page import BasePage
from locators.widgets_page_locators import (AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators,
                                            SliderPageLocators, ProgressBarPageLocators, TabsPageLocators)
from generator.generator import generated_colors, generated_date, generated_date_and_time
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver import Keys
import random
import calendar
import time


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


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    def set_date_item_from_list_of_options(self, element, value):
        list_of_options = self.elements_are_present(element)
        for item in list_of_options:
            if item.text.strip("✓\n") == value:
                item.click()
                break

    def set_specific_year(self, element, value):
        list_of_years = self.elements_are_present(element)
        top_year = int(list_of_years[0].text)
        bottom_year = int(list_of_years[-1].text)
        if int(value) > top_year:
            for _ in range(int(value) - top_year):
                self.element_is_clickable(self.locators.DATE_AND_TIME_YEAR_UPCOMING_OPTION).click()
        elif int(value) < bottom_year:
            for _ in range(bottom_year - int(value)):
                self.element_is_clickable(self.locators.DATE_AND_TIME_YEAR_PREVIOUS_OPTION).click()
        self.set_date_item_from_list_of_options(element, value)

    def select_date(self):
        month, day, year = generated_date().date.split()
        self.element_is_visible(self.locators.DATE_INPUT).click()
        self.select_option_by_text(self.locators.DATE_MONTH_SELECT_MENU, month)
        self.select_option_by_text(self.locators.DATE_YEAR_SELECT_MENU, year)
        self.set_date_item_from_list_of_options(self.locators.DATE_DAY, day)
        formatted_date = f"{list(calendar.month_name).index(month):02d}/{day.zfill(2)}/{year}"
        return formatted_date

    def set_date_and_time(self):
        date_and_time = generated_date_and_time()
        month, day, year = date_and_time.date.split()
        h24_time = date_and_time.time
        h12_time = time.strftime("%#I:%M %p", time.strptime(h24_time, "%H:%M"))
        self.element_is_visible(self.locators.DATE_AND_TIME_INPUT).click()
        self.element_is_clickable(self.locators.DATE_AND_TIME_MONTH).click()
        self.set_date_item_from_list_of_options(self.locators.DATE_AND_TIME_MONTH_OPTION, month)
        self.element_is_clickable(self.locators.DATE_AND_TIME_YEAR).click()
        self.set_specific_year(self.locators.DATE_AND_TIME_YEAR_OPTION, year)
        self.set_date_item_from_list_of_options(self.locators.DATE_AND_TIME_DAY, day)
        self.set_date_item_from_list_of_options(self.locators.DATE_AND_TIME_TIME_OPTION, h24_time)
        formatted_date_and_time = f"{month} {day}, {year} {h12_time}"
        return formatted_date_and_time

    def get_output_date(self, field):
        input_fields = {"date": self.locators.DATE_INPUT, "date_and_time": self.locators.DATE_AND_TIME_INPUT}
        input_field = self.element_is_visible(input_fields[field])
        input_field_value = input_field.get_attribute("value")
        return input_field_value


class SliderPage(BasePage):
    locators = SliderPageLocators()

    def move_slider(self):
        slider_value_before = self.element_is_present(self.locators.SLIDER_VALUE).get_attribute("value")
        slider = self.element_is_visible(self.locators.SLIDER)
        self.drag_and_drop_by_offset_action(slider, random.randint(1, 150), 0)
        slider_value_after = self.element_is_present(self.locators.SLIDER_VALUE).get_attribute("value")
        return slider_value_before, slider_value_after


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    def change_progress_bar_value(self):
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).get_attribute("textContent")
        start_stop_button = self.element_is_clickable(self.locators.PROGRESS_BAR_START_STOP_BUTTON)
        start_stop_button.click()
        time.sleep(round(random.uniform(0.1, 9.9), 1))
        start_stop_button.click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        return value_before, value_after

    def reset_progress_bar_value(self):
        initial_value = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).get_attribute("textContent")
        start_button = self.element_is_clickable(self.locators.PROGRESS_BAR_START_STOP_BUTTON)
        start_button.click()
        reset_button = self.element_is_clickable(self.locators.PROGRESS_BAR_RESET_BUTTON, timeout=20)
        value_before_reset = self.element_is_present(self.locators.PROGRESS_BAR_VALUE_SUCCESS).text
        reset_button.click()
        value_after_reset = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        return initial_value, value_before_reset, value_after_reset


class TabsPage(BasePage):
    locators = TabsPageLocators()

    def click_on_the_tab(self, tab_name):
        tabs = {"What": self.locators.TAB_WHAT,
                "Origin": self.locators.TAB_ORIGIN,
                "Use": self.locators.TAB_USE,
                "More": self.locators.TAB_MORE}
        tab = self.element_is_visible(tabs[tab_name])
        try:
            tab.click()
            tab_is_selected = tab.get_attribute("aria-selected")
            return tab_is_selected == "true"
        except ElementClickInterceptedException:
            return False

    def get_tab_title_and_content(self, tab_name):
        tabs = {"What": {"title": self.locators.TAB_WHAT,
                         "content": self.locators.TAB_WHAT_CONTENT},
                "Origin": {"title": self.locators.TAB_ORIGIN,
                           "content": self.locators.TAB_ORIGIN_CONTENT},
                "Use": {"title": self.locators.TAB_USE,
                        "content": self.locators.TAB_USE_CONTENT},
                "More": {"title": self.locators.TAB_MORE,
                         "content": self.locators.TAB_MORE_CONTENT}
                }
        title_and_content = []
        try:
            tab_title = self.element_is_present(tabs[tab_name]["title"]).text
            title_and_content.append(tab_title)
        except TimeoutException:
            title_and_content.append(None)
        try:
            tab_content = self.element_is_present(tabs[tab_name]["content"]).text
            title_and_content.append(tab_content)
        except TimeoutException:
            title_and_content.append(None)
        return title_and_content