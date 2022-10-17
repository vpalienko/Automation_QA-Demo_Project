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