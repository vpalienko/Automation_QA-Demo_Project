from selenium.webdriver.common.by import By
import random


class PracticeFormPageLocators:
    # student registration form
    FIRST_NAME = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    GENDER = (By.CSS_SELECTOR, "div[class*='custom-radio'] label")
    MOBILE = (By.CSS_SELECTOR, "input[id='userNumber']")
    DATE_OF_BIRTH = (By.CSS_SELECTOR, "input[id='dateOfBirthInput']")
    MONTH_SELECT_MENU = (By.CSS_SELECTOR, "select[class='react-datepicker__month-select']")
    YEAR_SELECT_MENU = (By.CSS_SELECTOR, "select[class='react-datepicker__year-select']")
    DAY_OF_THE_MONTH = (By.CSS_SELECTOR, "div[class^='react-datepicker__day react-datepicker__day']")
    SELECTED_MONTH_AND_YEAR = (By.CSS_SELECTOR, "div[class*='react-datepicker__current-month']")
    SELECTED_DAY = (By.CSS_SELECTOR, "div[class*='react-datepicker__day--selected']")
    SUBJECTS = (By.CSS_SELECTOR, "input[id='subjectsInput']")
    SUBJECT_AUTO_COMPLETE_OPTION = (By.CSS_SELECTOR, "div[class^='subjects-auto-complete__option']")
    HOBBIES = (By.CSS_SELECTOR, "div[class*='custom-checkbox'] label")
    PICTURE_UPLOAD = (By.CSS_SELECTOR, "input[id='uploadPicture']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    STATE_SELECT_MENU = (By.CSS_SELECTOR, "div[id='state']")
    STATE_INPUT = (By.CSS_SELECTOR, "input[id='react-select-3-input']")
    STATE_AUTO_COMPLETE_OPTION = (By.CSS_SELECTOR, "div[id^='react-select-3-option']")
    CITY_SELECT_MENU = (By.CSS_SELECTOR, "div[id='city']")
    CITY_INPUT = (By.CSS_SELECTOR, "input[id='react-select-4-input']")
    CITY_AUTO_COMPLETE_OPTION = (By.CSS_SELECTOR, "div[id^='react-select-4-option']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # submitted form
    RESULT_TABLE_VALUES = (By.XPATH, "//div[@class='table-responsive']//td[2]")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "button[id='closeLargeModal']")