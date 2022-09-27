from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # form fields
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # created form
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    COLLAPSE_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Collapse all']")
    ITEM_TITLE = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEM = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    LIST_ITEM = (By.XPATH, ".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonPageLocators:
    RADIOBUTTON_YES = (By.CSS_SELECTOR, "label[for='yesRadio']")
    RADIOBUTTON_IMPRESSIVE = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
    RADIOBUTTON_NO = (By.CSS_SELECTOR, "label[for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "p span[class='text-success']")


class WebTablesPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
    SEARCH_FIELD = (By.CSS_SELECTOR, "input[id='searchBox']")

    # add person form
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='userEmail']")
    AGE_INPUT = (By.CSS_SELECTOR, "input[id='age']")
    SALARY_INPUT = (By.CSS_SELECTOR, "input[id='salary']")
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, "input[id='department']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # web table
    TABLE_ROW = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    PERSON_IN_TABLE = (By.XPATH, "//div[@class='rt-tr-group']/div[not(contains(@class,'-padRow'))]")
    EDIT_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    NO_ROWS_FOUND = (By.CSS_SELECTOR, "div[class='rt-noData']")
    ROWS_PER_PAGE = (By.CSS_SELECTOR, "select[aria-label='rows per page']")


class ButtonsPageLocators:
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='doubleClickBtn']")
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='rightClickBtn']")
    CLICK_BUTTON = (By.CSS_SELECTOR, "div[class='mt-4']:nth-child(3) button")
    DOUBLE_CLICK_MESSAGE = (By.CSS_SELECTOR, "p[id='doubleClickMessage']")
    RIGHT_CLICK_MESSAGE = (By.CSS_SELECTOR, "p[id='rightClickMessage']")
    CLICK_MESSAGE = (By.CSS_SELECTOR, "p[id='dynamicClickMessage']")


class LinksPageLocators:
    # new tab links
    SIMPLE_LINK = (By.CSS_SELECTOR, "a[id='simpleLink']")
    DYNAMIC_LINK = (By.CSS_SELECTOR, "a[id='dynamicLink']")

    # api call links
    CREATED_LINK = (By.CSS_SELECTOR, "a[id='created']")
    NO_CONTENT_LINK = (By.CSS_SELECTOR, "a[id='no-content']")
    MOVED_LINK = (By.CSS_SELECTOR, "a[id='moved']")
    BAD_REQUEST_LINK = (By.CSS_SELECTOR, "a[id='bad-request']")
    UNAUTHORIZED_LINK = (By.CSS_SELECTOR, "a[id='unauthorized']")
    FORBIDDEN_LINK = (By.CSS_SELECTOR, "a[id='forbidden']")
    NOT_FOUND_LINK = (By.CSS_SELECTOR, "a[id='invalid-url']")
    OUTPUT_MESSAGE = (By.CSS_SELECTOR, "p[id='linkResponse']")


class BrokenLinksImagesPageLocators:
    VALID_IMAGE = (By.XPATH, "//p[text()='Valid image']/following-sibling::img[1]")
    BROKEN_IMAGE = (By.XPATH, "//p[text()='Broken image']/following-sibling::img[1]")
    VALID_LINK = (By.XPATH, "//p[text()='Valid Link']/following-sibling::a[1]")
    BROKEN_LINK = (By.XPATH, "//p[text()='Broken Link']/following-sibling::a[1]")


class UploadAndDownloadPageLocators:
    DOWNLOAD_BUTTON = (By.CSS_SELECTOR, "a[id='downloadButton']")
    UPLOAD_BUTTON = (By.CSS_SELECTOR, "input[id='uploadFile']")
    UPLOADED_FILE_PATH = (By.CSS_SELECTOR, "p[id='uploadedFilePath']")


class DynamicPropertiesPageLocators:
    ENABLE_AFTER_FIVE_SECONDS_BUTTON = (By.CSS_SELECTOR, "button[id='enableAfter']")
    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, "button[id='colorChange']")
    VISIBLE_AFTER_FIVE_SECONDS_BUTTON = (By.CSS_SELECTOR, "button[id='visibleAfter']")