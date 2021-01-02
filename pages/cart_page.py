from time import sleep

from app.config import TestData
from locators.locators import CartLocators
from pages.base_page import Page


class CartPage(Page):

    def verify_cart_is_opened(self):
        pass

    def verify_cart_is_empty(self, message: str):
        empty_cart = self.find_element(*CartLocators.EMPTY_CART)
        assert empty_cart.text == message, \
            f"Error. Empty cart message should be: {message}. Actual message: {empty_cart.text}"

    def current_state(self, shopping_cart_state: str):
        assert self.find_element(*CartLocators.CART_CURRENT_STATE).text.upper() == \
               shopping_cart_state.upper(), \
            f"Error. Shopping cart first step to purchase should be: {shopping_cart_state.upper()}"
