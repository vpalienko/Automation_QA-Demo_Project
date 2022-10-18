from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def open_and_remove_footer(self):
        self.browser.get(self.url)
        self.browser.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.browser.execute_script("document.getElementById('close-fixedban').remove();")
        self.browser.execute_script("document.getElementById('adplus-anchor').remove();")

    def element_is_visible(self, locator, timeout=5):
        self.go_to_element(self.element_is_present(locator))
        return wait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return wait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        return wait(self.browser, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        return wait(self.browser, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.browser, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.browser, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.browser.execute_script("arguments[0].scrollIntoView();", element)

    def double_click_action(self, element):
        action = ActionChains(self.browser)
        action.double_click(element)
        action.perform()

    def right_click_action(self, element):
        action = ActionChains(self.browser)
        action.context_click(element)
        action.perform()

    def click_action(self, element):
        action = ActionChains(self.browser)
        action.click(element)
        action.perform()

    def switch_to_opened_window(self):
        self.browser.switch_to.window(self.browser.window_handles[1])

    def switch_to_alert(self):
        return self.browser.switch_to.alert

    def switch_to_frame(self, element):
        self.browser.switch_to.frame(element)

    def select_option_by_text(self, menu_element, value):
        select_menu = Select(self.element_is_present(menu_element))
        select_menu.select_by_visible_text(value)

    def get_all_options_from_select_menu(self, menu_element):
        select_menu = Select(self.element_is_present(menu_element))
        available_options = select_menu.options
        return available_options