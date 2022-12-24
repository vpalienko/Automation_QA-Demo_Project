from selenium.webdriver.common.by import By


class AccordianPageLocators:
    FIRST_SECTION_TITLE = (By.CSS_SELECTOR, "div[id='section1Heading']")
    FIRST_SECTION_CONTENT = (By.CSS_SELECTOR, "div[id='section1Content'] p")
    SECOND_SECTION_TITLE = (By.CSS_SELECTOR, "div[id='section2Heading']")
    SECOND_SECTION_CONTENT = (By.CSS_SELECTOR, "div[id='section2Content'] p")
    THIRD_SECTION_TITLE = (By.CSS_SELECTOR, "div[id='section3Heading']")
    THIRD_SECTION_CONTENT = (By.CSS_SELECTOR, "div[id='section3Content'] p")
    SECTION_COLLAPSE_STATE = (By.XPATH, "./following-sibling::div[contains(@class, 'collapse')]")
    COLLAPSING_PROCESS = (By.CSS_SELECTOR, "div[class='collapsing']")


class AutoCompletePageLocators:
    MULTIPLE_INPUT_FIELD = (By.CSS_SELECTOR, "input[id='autoCompleteMultipleInput']")
    MULTI_VALUE = (By.CSS_SELECTOR, "div[class='css-1rhbuit-multiValue auto-complete__multi-value']")
    MULTI_AUTOCOMPLETE_OPTIONS = (By.CSS_SELECTOR, "div[id^='react-select-2-option']")
    MULTI_VALUE_REMOVE = (By.CSS_SELECTOR, "div[class='css-1rhbuit-multiValue auto-complete__multi-value'] svg path")
    MULTI_REMOVE_ALL_VALUES = (By.CSS_SELECTOR, "div[class='auto-complete__indicators css-1wy0on6'] svg path")
    SINGLE_INPUT_FIELD = (By.CSS_SELECTOR, "input[id='autoCompleteSingleInput']")
    SINGLE_VALUE = (By.CSS_SELECTOR, "div[class='auto-complete__single-value css-1uccc91-singleValue']")
    SINGLE_AUTOCOMPLETE_OPTIONS = (By.CSS_SELECTOR, "div[id^='react-select-3-option']")


class DatePickerPageLocators:
    DATE_INPUT = (By.CSS_SELECTOR, "input[id='datePickerMonthYearInput']")
    DATE_MONTH_SELECT_MENU = (By.CSS_SELECTOR, "select[class='react-datepicker__month-select']")
    DATE_YEAR_SELECT_MENU = (By.CSS_SELECTOR, "select[class='react-datepicker__year-select']")
    DATE_DAY = (By.CSS_SELECTOR, "div[class^='react-datepicker__day ']:not([class$='outside-month'])")
    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, "input[id='dateAndTimePickerInput']")
    DATE_AND_TIME_MONTH = (By.CSS_SELECTOR, "div[class='react-datepicker__month-read-view']")
    DATE_AND_TIME_YEAR = (By.CSS_SELECTOR, "div[class='react-datepicker__year-read-view']")
    DATE_AND_TIME_DAY = (By.CSS_SELECTOR, "div[class^='react-datepicker__day ']:not([class$='outside-month'])")
    DATE_AND_TIME_TIME_OPTION = (By.CSS_SELECTOR, "li[class='react-datepicker__time-list-item ']")
    DATE_AND_TIME_MONTH_OPTION = (By.CSS_SELECTOR, "div[class^='react-datepicker__month-option']")
    DATE_AND_TIME_YEAR_OPTION = (By.CSS_SELECTOR, "div[class*='year-option']:not(:first-child):not(:last-child)")
    DATE_AND_TIME_YEAR_UPCOMING_OPTION = (By.CSS_SELECTOR, "a[class$='years-upcoming']")
    DATE_AND_TIME_YEAR_PREVIOUS_OPTION = (By.CSS_SELECTOR, "a[class$='years-previous']")


class SliderPageLocators:
    SLIDER = (By.CSS_SELECTOR, "input[class='range-slider range-slider--primary']")
    SLIDER_VALUE = (By.CSS_SELECTOR, "input[id='sliderValue']")


class ProgressBarPageLocators:
    PROGRESS_BAR_START_STOP_BUTTON = (By.CSS_SELECTOR, "button[id='startStopButton']")
    PROGRESS_BAR_VALUE = (By.CSS_SELECTOR, "div[class='progress-bar bg-info']")
    PROGRESS_BAR_VALUE_SUCCESS = (By.CSS_SELECTOR, "div[class='progress-bar bg-success']")
    PROGRESS_BAR_RESET_BUTTON = (By.CSS_SELECTOR, "button[id='resetButton']")