from pages.forms_page import PracticeFormPage


class TestForms:
    class TestPracticeForm:
        link = "https://demoqa.com/automation-practice-form"

        def test_registration_form_can_be_filled_and_submitted(self, browser, blank_file):
            practice_form_page = PracticeFormPage(browser, self.link)
            practice_form_page.open_and_remove_footer()
            full_name = practice_form_page.input_first_name_and_last_name()
            email = practice_form_page.input_email()
            gender = practice_form_page.select_gender()
            mobile = practice_form_page.input_mobile_number()
            date_of_birth = practice_form_page.select_date_of_birth()
            subjects = practice_form_page.select_subjects()
            hobbies = practice_form_page.select_hobbies()
            picture = practice_form_page.upload_picture(blank_file(file_format="png"))
            current_address = practice_form_page.input_current_address()
            state_and_city = practice_form_page.select_state_and_city()
            registration_form = [full_name, email, gender, mobile, date_of_birth, subjects, hobbies, picture,
                                 current_address, state_and_city]
            practice_form_page.submit_form()
            output_form = practice_form_page.get_submitted_values()
            assert registration_form == output_form, "Registration values do not match submitted values"