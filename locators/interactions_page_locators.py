from selenium.webdriver.common.by import By


class SortablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, "a[id='demo-tab-list']")
    TAB_LIST_ITEM = (By.CSS_SELECTOR, "div[id='demo-tabpane-list'] div[class='list-group-item list-group-item-action']")
    TAB_GRID = (By.CSS_SELECTOR, "a[id='demo-tab-grid']")
    TAB_GRID_ITEM = (By.CSS_SELECTOR, "div[id='demo-tabpane-grid'] div[class='list-group-item list-group-item-action']")