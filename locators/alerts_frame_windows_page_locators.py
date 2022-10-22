from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "button[id='tabButton']")
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, "button[id='windowButton']")
    NEW_WINDOW_MESSAGE_BUTTON = (By.CSS_SELECTOR, "button[id='messageWindowButton']")


class AlertsPageLocators:
    SIMPLE_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='alertButton']")
    TIMER_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='timerAlertButton']")
    CONFIRM_ACTION_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='confirmButton']")
    CONFIRM_ACTION_RESULT_MESSAGE = (By.CSS_SELECTOR, "span[id='confirmResult']")
    PROMPT_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='promtButton']")
    PROMPT_BOX_RESULT_MESSAGE = (By.CSS_SELECTOR, "span[id='promptResult']")


class FramesPageLocators:
    FRAME_ONE = (By.CSS_SELECTOR, "iframe[id='frame1']")
    FRAME_TWO = (By.CSS_SELECTOR, "iframe[id='frame2']")
    FRAME_TITLE = (By.CSS_SELECTOR, "h1[id='sampleHeading']")


class NestedFramesPageLocators:
    PARENT_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    PARENT_FRAME_TEXT = (By.CSS_SELECTOR, "body")
    CHILD_FRAME = (By.CSS_SELECTOR, "iframe[srcdoc='<p>Child Iframe</p>']")
    CHILD_FRAME_TEXT = (By.CSS_SELECTOR, "p")


class ModalDialogsPageLocators:
    SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, "button[id='showSmallModal']")
    SMALL_MODAL_DIALOG = (By.CSS_SELECTOR, "div[class$='modal-sm'] div[class='modal-content']")
    SMALL_MODAL_DIALOG_TITLE = (By.CSS_SELECTOR, "div[id='example-modal-sizes-title-sm']")
    SMALL_MODAL_DIALOG_CONTENT = (By.CSS_SELECTOR, "div[class='modal-body']")
    SMALL_MODAL_DIALOG_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[id='closeSmallModal']")
    LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, "button[id='showLargeModal']")
    LARGE_MODAL_DIALOG = (By.CSS_SELECTOR, "div[class$='modal-lg'] div[class='modal-content']")
    LARGE_MODAL_DIALOG_TITLE = (By.CSS_SELECTOR, "div[id='example-modal-sizes-title-lg']")
    LARGE_MODAL_DIALOG_CONTENT = (By.CSS_SELECTOR, "div[class='modal-body'] p")
    LARGE_MODAL_DIALOG_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[id='closeLargeModal']")