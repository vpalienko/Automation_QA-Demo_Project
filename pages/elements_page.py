from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage
from generator.generator import generated_person


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