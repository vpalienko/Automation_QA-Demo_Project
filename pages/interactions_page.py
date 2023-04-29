from pages.base_page import BasePage
from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators
import random


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def get_items_order(self, tab_name):
        tabs = {"List": {"tab": self.locators.TAB_LIST,
                         "item": self.locators.TAB_LIST_ITEM},
                "Grid": {"tab": self.locators.TAB_GRID,
                         "item": self.locators.TAB_GRID_ITEM}}
        self.open_tab(tabs[tab_name]["tab"])
        items_list = self.elements_are_visible(tabs[tab_name]["item"])
        return [item.text for item in items_list]

    def change_items_order(self, tab_name):
        tab_item = {"List": self.locators.TAB_LIST_ITEM,
                    "Grid": self.locators.TAB_GRID_ITEM}
        items_list = self.elements_are_visible(tab_item[tab_name])
        for i in range(random.randint(1, len(items_list))):
            what_item, where_to_move = random.sample(items_list, k=2)
            self.drag_and_drop_to_target_action(what_item, where_to_move)


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    def check_if_all_items_are_selected(self, tab_name):
        tabs = {"List": {"tab": self.locators.TAB_LIST,
                         "item": self.locators.TAB_LIST_ITEM},
                "Grid": {"tab": self.locators.TAB_GRID,
                         "item": self.locators.TAB_GRID_ITEM}}
        self.open_tab(tabs[tab_name]["tab"])
        items_list = self.elements_are_visible(tabs[tab_name]["item"])
        return all(["active" in item.get_attribute("class") for item in items_list])

    def check_if_all_items_are_not_selected(self, tab_name):
        tabs = {"List": {"tab": self.locators.TAB_LIST,
                         "item": self.locators.TAB_LIST_ITEM},
                "Grid": {"tab": self.locators.TAB_GRID,
                         "item": self.locators.TAB_GRID_ITEM}}
        self.open_tab(tabs[tab_name]["tab"])
        items_list = self.elements_are_visible(tabs[tab_name]["item"])
        return all(["active" not in item.get_attribute("class") for item in items_list])

    def click_on_each_item(self, tab_name):
        tab_item = {"List": self.locators.TAB_LIST_ITEM,
                    "Grid": self.locators.TAB_GRID_ITEM}
        items_list = self.elements_are_visible(tab_item[tab_name])
        for item in items_list:
            item.click()