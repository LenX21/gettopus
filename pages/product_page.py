from locators.locators import ProductPageLocators
from pages.base_page import Page

class ProductPage(Page):
    def add_product_to_the_card(self):
        pass

    def verify_product_data(self):
        self.wait_for_element_appears(*ProductPageLocators.PRODUCT_TITLE)
        self.find_element(*ProductPageLocators.PRODUCT_SHORT_DESCRIPTION)
        self.find_element(*ProductPageLocators.PRODUCT_PRICE)
        self.find_element(*ProductPageLocators.PRODUCT_PRICE)