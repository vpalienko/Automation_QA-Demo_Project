from selenium.webdriver.common.by import By


class SortablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, "a[id='demo-tab-list']")
    TAB_LIST_ITEM = (By.CSS_SELECTOR, "div[id='demo-tabpane-list'] div[class='list-group-item list-group-item-action']")
    TAB_GRID = (By.CSS_SELECTOR, "a[id='demo-tab-grid']")
    TAB_GRID_ITEM = (By.CSS_SELECTOR, "div[id='demo-tabpane-grid'] div[class='list-group-item list-group-item-action']")


class SelectablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, "a[id='demo-tab-list']")
    TAB_LIST_ITEM = (By.CSS_SELECTOR, "ul[id='verticalListContainer'] li[class^='mt-2 list-group-item']")
    TAB_GRID = (By.CSS_SELECTOR, "a[id='demo-tab-grid']")
    TAB_GRID_ITEM = (By.CSS_SELECTOR, "div[id='gridContainer'] li[class^='list-group-item']")


class ResizablePageLocators:
    RESIZABLE_BOX = (By.CSS_SELECTOR, "div[id='resizableBoxWithRestriction']")
    RESIZABLE_BOX_HANDLE = (By.CSS_SELECTOR, "div[id='resizableBoxWithRestriction'] span[class*='handle']")
    RESIZABLE = (By.CSS_SELECTOR, "div[id='resizable']")
    RESIZABLE_HANDLE = (By.CSS_SELECTOR, "div[id='resizable'] span[class*='handle']")