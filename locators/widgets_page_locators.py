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