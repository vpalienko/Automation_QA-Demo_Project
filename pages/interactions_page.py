from pages.base_page import BasePage
from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators
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


class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    def get_element_width_and_height(self, element):
        element_size = self.element_is_visible(element).get_attribute("style")
        width = element_size.split(";")[0].split(": ")[1]
        height = element_size.split(";")[1].split(": ")[1]
        return width, height

    def get_resizable_box_width_and_height(self):
        resizable_box_width, resizable_box_height = self.get_element_width_and_height(self.locators.RESIZABLE_BOX)
        return resizable_box_width, resizable_box_height

    def get_resizable_width_and_height(self):
        resizable_width, resizable_height = self.get_element_width_and_height(self.locators.RESIZABLE)
        return resizable_width, resizable_height

    def increase_resizable_element(self, element, width, height):
        if width == "random_value":
            width = random.randint(1, 150)
        if height == "random_value":
            height = random.randint(1, 150)
        self.drag_and_drop_by_offset_action(self.element_is_present(element), abs(width), abs(height))

    def decrease_resizable_element(self, element, width, height):
        if width == "random_value":
            width = random.randint(-150, -1)
        if height == "random_value":
            height = random.randint(-150, -1)
        self.drag_and_drop_by_offset_action(self.element_is_present(element), -abs(width), -abs(height))

    def change_resizable_box_size(self, operation="increase", width="random_value", height="random_value"):
        if operation == "increase":
            self.increase_resizable_element(self.locators.RESIZABLE_BOX_HANDLE, width, height)
        elif operation == "decrease":
            self.decrease_resizable_element(self.locators.RESIZABLE_BOX_HANDLE, width, height)

    def change_resizable_size(self, operation="increase", width="random_value", height="random_value"):
        if operation == "increase":
            self.increase_resizable_element(self.locators.RESIZABLE_HANDLE, width, height)
        elif operation == "decrease":
            self.decrease_resizable_element(self.locators.RESIZABLE_HANDLE, width, height)