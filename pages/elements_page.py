from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators
from pages.base_page import BasePage
from generator.generator import generated_person
import random


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