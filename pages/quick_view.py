from app.logger import logger
from pages.base_page import Page
from locators import locators as cl
from time import sleep


class QuickView(Page):

    def open_quick_view_for_product_by_number(self, product_number: int):
        self.mouse_hover_action(*cl.ProductCategoryLocators.get_product_locator_by_number(product_number))
        self.click(*cl.QuickViewLocators.QUICK_VIEW_PRODUCT_LINK.get_quick_view_for_product_by_number(product_number))

    def verify_quick_view_is_opened(self):
        self.wait_for_element_appears(*cl.QuickViewLocators.QUICK_VIEW.locator)

    def verify_quick_view_is_opened_for_product_by_number(self, product_number: int):
        self.verify_quick_view_is_opened()
        title_shown_on_category_page = \
            self.find_element(*cl.ProductCategoryLocators.get_product_title_by_number(product_number)).text
        title_on_quick_view_window = \
            self.find_element(*cl.QuickViewLocators.QUICK_VIEW_PRODUCT_TITLE.locator).text
        assert title_shown_on_category_page == title_on_quick_view_window, \
            f"Error. Title is shown on category page and quick view should be the same. " \
            f"Title on the page: {title_shown_on_category_page} - Title quick view: {title_on_quick_view_window}"

    def close_quick_view_x(self):
        self.click(*cl.QuickViewLocators.QUICK_VIEW_CLOSE_BTN.locator)

    def verify_quick_view_is_closed(self):
        self.wait_for_element_disappears(*cl.QuickViewLocators.QUICK_VIEW.locator)

    def click_button_add_to_cart(self):
        self.click(*cl.QuickViewLocators.QUICK_VIEW_ADD_TO_CART_BTN.locator)

