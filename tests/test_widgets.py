from pages.widgets_page import (AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage,
                                ToolTipsPage)
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

    class TestDatePicker:
        link = "https://demoqa.com/date-picker"

        def test_date_can_be_selected_via_date_picker(self, browser):
            date_picker_page = DatePickerPage(browser, self.link)
            date_picker_page.open()
            input_date = date_picker_page.select_date()
            output_date = date_picker_page.get_output_date(field="date")
            assert input_date == output_date, "Date is not selected via date picker"

        def test_date_and_time_can_be_set_via_date_picker(self, browser):
            date_picker_page = DatePickerPage(browser, self.link)
            date_picker_page.open()
            input_date = date_picker_page.set_date_and_time()
            output_date = date_picker_page.get_output_date(field="date_and_time")
            assert input_date == output_date, "Date is not set via date picker"

    class TestSlider:
        link = "https://demoqa.com/slider"

        def test_slider_value_changes_after_slider_is_moved(self, browser):
            slider_page = SliderPage(browser, self.link)
            slider_page.open()
            value_before, value_after = slider_page.move_slider()
            assert value_before != value_after, "Slider value is not changed or slider is not moved"

    class TestProgressBar:
        link = "https://demoqa.com/progress-bar"

        def test_progress_bar_value_can_be_changed(self, browser):
            progress_bar_page = ProgressBarPage(browser, self.link)
            progress_bar_page.open()
            value_before, value_after = progress_bar_page.change_progress_bar_value()
            assert value_before != value_after, "Progress bar value is not changed"

        def test_progress_bar_can_be_filled_and_reset(self, browser):
            progress_bar_page = ProgressBarPage(browser, self.link)
            progress_bar_page.open()
            initial_value, value_before_reset, value_after_reset = progress_bar_page.reset_progress_bar_value()
            assert value_before_reset == "100%", "Progress bar full value is not 100%"
            assert initial_value == value_after_reset, "Progress bar value is not reset"

    class TestTabs:
        link = "https://demoqa.com/tabs"
        tabs = ["What", "Origin", "Use", pytest.param("More", marks=pytest.mark.xfail(reason="tab disabled"))]

        @pytest.mark.parametrize("tab_name", tabs)
        def test_selected_tab_has_title_and_content(self, browser, tab_name):
            tabs_page = TabsPage(browser, self.link)
            tabs_page.open()
            tab_is_selected = tabs_page.click_on_the_tab(tab_name)
            assert tab_is_selected, "Tab is not selected"
            actual_tab_title, tab_content = tabs_page.get_tab_title_and_content(tab_name)
            assert actual_tab_title == tab_name, "Tab has incorrect title"
            assert tab_content, "Tab content is absent"

    class TestToolTips:
        link = "https://demoqa.com/tool-tips"
        elements_with_tooltips = ["Button", "text field", "Contrary", "1.10.32"]

        @pytest.mark.parametrize("tooltip_element", elements_with_tooltips)
        def test_tooltip_is_displayed_and_has_text(self, browser, tooltip_element):
            tooltip_page = ToolTipsPage(browser, self.link)
            tooltip_page.open()
            tooltip_is_displayed = tooltip_page.hover_over_element_to_show_tooltip(tooltip_element)
            assert tooltip_is_displayed, "Tooltip isn't displayed"
            tooltip_text = tooltip_page.get_tooltip_text()
            assert tooltip_text == f"You hovered over the {tooltip_element}", "Tooltip has incorrect text"