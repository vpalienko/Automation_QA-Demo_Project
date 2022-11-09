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