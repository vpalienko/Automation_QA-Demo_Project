from pages.interactions_page import SortablePage, SelectablePage, ResizablePage
import pytest


class TestInteractions:
    class TestSortable:
        link = "https://demoqa.com/sortable"
        tab_names = ["List", "Grid"]

        @pytest.mark.parametrize("tab", tab_names)
        def test_items_can_be_sorted_randomly(self, browser, tab):
            sortable_page = SortablePage(browser, self.link)
            sortable_page.open()
            order_before_sort = sortable_page.get_items_order(tab)
            sortable_page.change_items_order(tab)
            order_after_sort = sortable_page.get_items_order(tab)
            assert order_before_sort != order_after_sort, "The order of the items is not changed"

    class TestSelectable:
        link = "https://demoqa.com/selectable"
        tab_names = ["List", "Grid"]

        @pytest.mark.parametrize("tab", tab_names)
        def test_each_item_can_be_selected_and_unselected(self, browser, tab):
            selectable_page = SelectablePage(browser, self.link)
            selectable_page.open()
            items_not_selected_by_default = selectable_page.check_if_all_items_are_not_selected(tab)
            assert items_not_selected_by_default, "Some items are selected by default"
            selectable_page.click_on_each_item(tab)
            all_items_selected = selectable_page.check_if_all_items_are_selected(tab)
            assert all_items_selected, "Items cannot be selected"
            selectable_page.click_on_each_item(tab)
            all_items_unselected = selectable_page.check_if_all_items_are_not_selected(tab)
            assert all_items_unselected, "Items cannot be unselected"

    class TestResizable:
        link = "https://demoqa.com/resizable"

        def test_resizable_box_cannot_break_max_and_min_size_limits(self, browser):
            resizable_page = ResizablePage(browser, self.link)
            resizable_page.open()
            initial_size = resizable_page.get_resizable_box_width_and_height()
            assert initial_size == ("200px", "200px"), "Initial size of resizable box is incorrect"
            resizable_page.change_resizable_box_size(operation="increase", width=301, height=101)
            increased_size = resizable_page.get_resizable_box_width_and_height()
            assert increased_size == ("500px", "300px"), "Resizable box breaks max limit size"
            resizable_page.change_resizable_box_size(operation="decrease", width=-351, height=-151)
            decreased_size = resizable_page.get_resizable_box_width_and_height()
            assert decreased_size == ("150px", "150px"), "Resizable box breaks min limit size"

        def test_resizable_element_can_be_increased_and_decreased(self, browser):
            resizable_page = ResizablePage(browser, self.link)
            resizable_page.open()
            initial_size = resizable_page.get_resizable_width_and_height()
            resizable_page.change_resizable_size(operation="increase", width="random_value", height="random_value")
            increased_size = resizable_page.get_resizable_width_and_height()
            assert initial_size != increased_size, "Resizable element is not increased"
            resizable_page.change_resizable_size(operation="decrease", width="random_value", height="random_value")
            decreased_size = resizable_page.get_resizable_width_and_height()
            assert increased_size != decreased_size, "Resizable element is not decreased"