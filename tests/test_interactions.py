from pages.interactions_page import SortablePage
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