from selenium.webdriver import Keys
from pages.base_page import BasePage
from locators.forms_page_locators import PracticeFormPageLocators
from generator.generator import generated_person, generated_subjects, generated_state_and_city
import random


class PracticeFormPage(BasePage):
    locators = PracticeFormPageLocators()
    person_info = generated_person()

    def input_first_name_and_last_name(self):
        first_name = self.person_info.first_name
        last_name = self.person_info.last_name
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        return f"{first_name} {last_name}"

    def input_email(self):
        email = self.person_info.email
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        return email

    def select_gender(self):
        genders = self.elements_are_visible(self.locators.GENDER)
        random_gender = random.choice(genders)
        random_gender.click()
        return random_gender.text

    def input_mobile_number(self):
        mobile = self.person_info.mobile
        self.element_is_visible(self.locators.MOBILE).send_keys(mobile)
        return mobile

    def select_date_of_birth(self):
        date_of_birth_field = self.element_is_visible(self.locators.DATE_OF_BIRTH)
        date_of_birth_field.click()
        available_months = self.get_all_options_from_select_menu(self.locators.MONTH_SELECT_MENU)
        self.select_option_by_text(self.locators.MONTH_SELECT_MENU, random.choice(available_months).text)
        available_years = self.get_all_options_from_select_menu(self.locators.YEAR_SELECT_MENU)
        self.select_option_by_text(self.locators.YEAR_SELECT_MENU, random.choice(available_years).text)
        available_days = self.elements_are_visible(self.locators.DAY_OF_THE_MONTH)
        random.choice(available_days).click()
        date_of_birth_field.click()
        month_and_year = self.element_is_visible(self.locators.SELECTED_MONTH_AND_YEAR).text
        day = self.element_is_visible(self.locators.SELECTED_DAY).text
        date_of_birth_field.send_keys(Keys.RETURN)
        return f"{day.zfill(2)} {','.join(month_and_year.split())}"

    def select_subjects(self):
        subjects = generated_subjects()
        for subject in subjects:
            self.element_is_visible(self.locators.SUBJECTS).send_keys(subject)
            self.element_is_present(self.locators.SUBJECT_AUTO_COMPLETE_OPTION).click()
        return ", ".join(subjects)

    def select_hobbies(self):
        hobbies = self.elements_are_visible(self.locators.HOBBIES)
        number_of_hobbies = random.randint(1, len(hobbies))
        random_hobbies = random.sample(hobbies, number_of_hobbies)
        for hobby in random_hobbies:
            hobby.click()
        return ", ".join(hobby.text for hobby in random_hobbies)

    def upload_picture(self, picture_to_upload):
        self.element_is_visible(self.locators.PICTURE_UPLOAD).send_keys(picture_to_upload)
        file_name = picture_to_upload.rsplit("\\", maxsplit=1)[1]
        return file_name

    def input_current_address(self):
        address = self.person_info.current_address
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(address)
        return address

    def select_state_and_city(self):
        state, city = generated_state_and_city()
        self.element_is_visible(self.locators.STATE_SELECT_MENU).click()
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(state)
        self.element_is_present(self.locators.STATE_AUTO_COMPLETE_OPTION).click()
        self.element_is_visible(self.locators.CITY_SELECT_MENU).click()
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(city)
        self.element_is_present(self.locators.CITY_AUTO_COMPLETE_OPTION).click()
        return f"{state} {city}"

    def submit_form(self):
        self.go_to_element(self.element_is_present(self.locators.SUBMIT))
        self.element_is_visible(self.locators.SUBMIT).click()

    def get_submitted_values(self):
        result_table_values = self.elements_are_visible(self.locators.RESULT_TABLE_VALUES)
        submitted_values = [item.text for item in result_table_values if item.text]
        self.element_is_visible(self.locators.CLOSE_BUTTON).click()
        return submitted_values