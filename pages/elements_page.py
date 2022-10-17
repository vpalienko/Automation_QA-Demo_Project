from locators.elements_page_locators import (TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators,
                                             WebTablesPageLocators, ButtonsPageLocators, LinksPageLocators,
                                             BrokenLinksImagesPageLocators, UploadAndDownloadPageLocators,
                                             DynamicPropertiesPageLocators)
from pages.base_page import BasePage
from generator.generator import generated_person
from conftest import root_dir
from selenium.common.exceptions import TimeoutException, InvalidArgumentException, NoSuchElementException
from selenium.webdriver.support.ui import Select
import random
import requests
import os
import time


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()
    person_info = generated_person()

    def input_full_name(self):
        full_name = self.person_info.full_name
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        return full_name

    def input_email(self):
        email = self.person_info.email
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        return email

    def input_current_address(self):
        current_address = self.person_info.current_address
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        return current_address

    def input_permanent_address(self):
        permanent_address = self.person_info.permanent_address
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        return permanent_address

    def submit_form(self):
        self.go_to_element(self.element_is_present(self.locators.SUBMIT))
        self.element_is_visible(self.locators.SUBMIT).click()

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(":")[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(":")[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def expand_all_items(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def collapse_all_items(self):
        self.element_is_visible(self.locators.COLLAPSE_ALL_BUTTON).click()

    def get_number_of_items(self):
        list_of_items = self.elements_are_visible(self.locators.ITEM_TITLE)
        return len(list_of_items)

    def click_random_checkboxes(self):
        list_of_items = self.elements_are_visible(self.locators.ITEM_TITLE)
        clicks = random.randint(1, len(list_of_items))
        while clicks != 0:
            item = list_of_items[random.randrange(len(list_of_items))]
            self.go_to_element(item)
            item.click()
            clicks -= 1

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEM)
        data = []
        for box in checked_list:
            title_item = box.find_element(*self.locators.LIST_ITEM)
            data.append(title_item.text.replace(" ", "").replace(".doc", "").lower())
        return ", ".join(data)

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text.lower())
        return ", ".join(data)


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_on_the_radio_button(self, choice):
        buttons = {"Yes": self.locators.RADIOBUTTON_YES,
                   "Impressive": self.locators.RADIOBUTTON_IMPRESSIVE,
                   "No": self.locators.RADIOBUTTON_NO}
        self.element_is_visible(buttons[choice]).click()

    def get_output_result(self):
        try:
            return self.element_is_present(self.locators.OUTPUT_RESULT).text
        except TimeoutException:
            return None


class WebTablesPage(BasePage):
    locators = WebTablesPageLocators()

    def add_new_person(self):
        person_info = generated_person()
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        age = str(person_info.age)
        salary = str(person_info.salary)
        department = person_info.department
        self.element_is_visible(self.locators.ADD_BUTTON).click()
        self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
        self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
        self.element_is_visible(self.locators.SUBMIT).click()
        return [first_name, last_name, age, email, salary, department]

    def get_list_of_persons_in_table(self):
        try:
            list_of_persons = self.elements_are_present(self.locators.PERSON_IN_TABLE)
            return [person.text.splitlines() for person in list_of_persons]
        except TimeoutException:
            return [self.element_is_present(self.locators.NO_ROWS_FOUND).text]

    def search_for_person_by_keyword(self, key_word):
        self.element_is_visible(self.locators.SEARCH_FIELD).clear()
        self.element_is_visible(self.locators.SEARCH_FIELD).send_keys(key_word)

    def update_person_information(self):
        person_info = generated_person()
        person_info_dict = {person_info.first_name: self.locators.FIRST_NAME_INPUT,
                            person_info.last_name: self.locators.LAST_NAME_INPUT,
                            str(person_info.age): self.locators.AGE_INPUT,
                            person_info.email: self.locators.EMAIL_INPUT,
                            str(person_info.salary): self.locators.SALARY_INPUT,
                            person_info.department: self.locators.DEPARTMENT_INPUT}
        self.element_is_visible(self.locators.EDIT_BUTTON).click()
        for input_value, input_field in person_info_dict.items():
            self.element_is_visible(input_field).clear()
            self.element_is_visible(input_field).send_keys(input_value)
        self.element_is_visible(self.locators.SUBMIT).click()
        return list(person_info_dict.keys())

    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def change_number_of_rows_per_page(self):
        rows_per_page = Select(self.element_is_present(self.locators.ROWS_PER_PAGE))
        number_of_rows_per_page = [option.get_attribute('value') for option in rows_per_page.options]
        number_of_rows_in_table = []
        for number_of_rows in number_of_rows_per_page:
            rows_per_page.select_by_value(number_of_rows)
            number_of_rows_in_table.append(str(len(self.elements_are_visible(self.locators.TABLE_ROW))))
        return number_of_rows_per_page, number_of_rows_in_table


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def perform_double_click_with_mouse(self):
        self.double_click_action(self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON))
        double_click_message = self.element_is_present(self.locators.DOUBLE_CLICK_MESSAGE).text
        return double_click_message

    def perform_right_click_with_mouse(self):
        self.right_click_action(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
        right_click_message = self.element_is_present(self.locators.RIGHT_CLICK_MESSAGE).text
        return right_click_message

    def perform_single_click_with_mouse(self):
        self.click_action(self.element_is_visible(self.locators.CLICK_BUTTON))
        single_click_message = self.element_is_present(self.locators.CLICK_MESSAGE).text
        return single_click_message


class LinksPage(BasePage):
    locators = LinksPageLocators()

    def check_link_opened_in_new_tab(self, link):
        links = {"Simple link": self.locators.SIMPLE_LINK, "Dynamic link": self.locators.DYNAMIC_LINK}
        link_locator = self.element_is_visible(links[link])
        url_link = link_locator.get_attribute("href")
        request = requests.get(url_link)
        if request.status_code < 400:
            link_locator.click()
            tabs = self.browser.window_handles
            if len(tabs) == 2:
                self.switch_to_opened_window()
            return len(tabs), request.status_code
        else:
            return False, request.status_code

    def check_link_sends_api_call(self, link_status):
        links = {"Created": {"link": self.locators.CREATED_LINK, "link_url": "created"},
                 "No Content": {"link": self.locators.NO_CONTENT_LINK, "link_url": "no-content"},
                 "Moved Permanently": {"link": self.locators.MOVED_LINK, "link_url": "moved"},
                 "Bad Request": {"link": self.locators.BAD_REQUEST_LINK, "link_url": "bad-request"},
                 "Unauthorized": {"link": self.locators.UNAUTHORIZED_LINK, "link_url": "unauthorized"},
                 "Forbidden": {"link": self.locators.FORBIDDEN_LINK, "link_url": "forbidden"},
                 "Not Found": {"link": self.locators.NOT_FOUND_LINK, "link_url": "invalid-url"}}
        self.element_is_visible(links[link_status]["link"]).click()
        url_link = f"https://demoqa.com/{links[link_status]['link_url']}"
        request = requests.get(url_link)
        status_code = request.status_code
        status = request.reason
        return str(status_code), status

    def get_output_message(self):
        return self.element_is_present(self.locators.OUTPUT_MESSAGE).text


class BrokenLinksImagesPage(BasePage):
    locators = BrokenLinksImagesPageLocators()

    def check_image_is_visible(self, image_type):
        images = {"Valid image": self.locators.VALID_IMAGE, "Broken image": self.locators.BROKEN_IMAGE}
        image = self.element_is_visible(images[image_type])
        width = image.get_attribute("naturalWidth")
        height = image.get_attribute("naturalHeight")
        if width != "0" and height != "0":
            return True
        else:
            return False

    def check_link_is_valid(self, link_type):
        links = {"Valid Link": self.locators.VALID_LINK, "Broken Link": self.locators.BROKEN_LINK}
        href_link = self.element_is_present(links[link_type]).get_attribute("href")
        request = requests.get(href_link)
        if request.status_code < 400:
            return True
        else:
            return False


class UploadAndDownloadPage(BasePage):
    locators = UploadAndDownloadPageLocators()

    def download_file(self):
        self.element_is_visible(self.locators.DOWNLOAD_BUTTON).click()

    def get_downloaded_file_name(self):
        return self.element_is_present(self.locators.DOWNLOAD_BUTTON).get_attribute("download")

    def check_downloaded_file_exists(self, timeout=5):
        file_name = self.get_downloaded_file_name()
        file_path = os.path.join(root_dir, file_name)
        while timeout:
            if os.path.exists(file_path):
                os.remove(file_path)
                return True
            time.sleep(1)
            timeout -= 1

    def upload_file(self, file_to_upload):
        try:
            self.element_is_visible(self.locators.UPLOAD_BUTTON).send_keys(file_to_upload)
            file_name = file_to_upload.rsplit("\\", maxsplit=1)[1]
            return file_name
        except InvalidArgumentException:
            return None

    def get_upload_path(self):
        try:
            return self.element_is_present(self.locators.UPLOADED_FILE_PATH).text
        except TimeoutException:
            return ""


class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesPageLocators()

    def check_button_is_disabled_by_default(self):
        button = self.browser.find_element(*self.locators.ENABLE_AFTER_FIVE_SECONDS_BUTTON)
        disabled_state = button.get_attribute("disabled")
        return True if disabled_state else False

    def check_button_is_enabled_after_five_seconds(self):
        try:
            self.element_is_clickable(self.locators.ENABLE_AFTER_FIVE_SECONDS_BUTTON, timeout=5)
            return True
        except TimeoutException:
            return False

    def check_button_color_is_changed_after_five_seconds(self):
        button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        button_color_before = button.value_of_css_property("color")
        time.sleep(5)
        button_color_after = button.value_of_css_property("color")
        return button_color_before, button_color_after

    def check_button_is_absent_by_default(self):
        try:
            self.browser.find_element(*self.locators.VISIBLE_AFTER_FIVE_SECONDS_BUTTON)
            return False
        except NoSuchElementException:
            return True

    def check_button_is_appeared_after_five_seconds(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_FIVE_SECONDS_BUTTON, timeout=5)
            return True
        except TimeoutException:
            return False