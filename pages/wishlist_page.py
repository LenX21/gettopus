from pages.base_page import Page
from locators.locators import WishlistLocators
from pages.home_page import HomePage
from locators import locators as cl


class WishlistPage(Page):

    def verify_products_names(self):
        self.wait_for_element_appears(*WishlistLocators.WISHLIST_TITLE)
        wishlist_names = [product.text for product in
                          self.find_elements(*WishlistLocators.get_product_attributes(cl.WishlistData.NAME))]
        assert sorted(HomePage.products_names) == sorted(wishlist_names), \
            f"Error. Wishlist contains incorrect list of products. " \
            f"Expected: {HomePage.products_names}\nActual:{wishlist_names}"
