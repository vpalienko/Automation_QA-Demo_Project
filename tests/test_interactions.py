from pages.interactions_page import SortablePage, SelectablePage
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