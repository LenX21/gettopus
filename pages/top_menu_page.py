from app.logger import logger
from pages.base_page import Page
from locators import locators as cl


def get_locator(element: str):
    return cl.ProductCategoriesTopMenu[element].value.locator


def get_value(element: str):
    return cl.ProductCategoriesTopMenu[element].value


def tooltip_dd():
    return get_value('TOOLTIP')


class TopMenuPage(Page):

    def open_category_by_name(self, category_name):
        # print(cl.ProductCategoriesTopMenu[category_name].value.get_category_name())
        # print(cl.ProductCategoriesTopMenu.MAC.value.get_category_name())
        self.click(*get_locator(category_name))

    def search_product(self, search_text):
        self.mouse_hover_action(*cl.ProductCategoriesTopMenuOther.SEARCH_ICON_CATEGORY.value.locator)
        self.input_text(search_text, *cl.ProductCategoriesTopMenuOther.SEARCH_FIELD.value.locator)
        self.click(*cl.ProductCategoriesTopMenuOther.SEARCH_ICON_NEAR_SEARCH_FIELD.value.locator)

    def hover_over_category_top_menu(self, category_name):
        self.mouse_hover_action(*get_value(category_name).locator)
        # self.verify_all_products_from_dd(category)

    def hover_over_icon(self, icon: str):
        self.mouse_hover_action(*get_locator(icon))

    def verify_all_products_from_dd(self, category_name: str):
        category = get_value(category_name)
        self.wait_for_element_appears(*category.category_drop_down_menu)
        logger.info(f'All items in drop-down menu should contain: {category.category_name} products')
        all_items = self.find_elements(*category.dd_items)
        for item in all_items:
            assert category.category_name.upper() in item.text.strip().upper(), \
                f"Error. Only product related to {category.category_name} should be shown." \
                f"Current product: {item.text}"

    def click_icon(self, icon_name):
        self.click(*get_locator(icon_name))

    def verify_empty_cart_message(self, message_to_verify):
        empty_cart = self.find_element(*cl.ProductCategoriesTopMenuOther.EMPTY_CART.value.locator)
        assert empty_cart.text == message_to_verify, \
            f"Error. Incorrect message. Expected text: {message_to_verify} - Actual text: {empty_cart.text}"

    def wait_until_price_updated(self):
        currency_symbol = self.find_element(*get_locator('CURRENCY')).text
        self.wait_till_text_updated(f'{currency_symbol}0.00', *get_locator('PRICE'))

    def verify_price(self, amount: str):
        self.wait_until_price_updated()
        assert self.find_element(*get_locator('PRICE')).text == amount

    def cart_icon_amount_of_added_product(self, amount: int):
        actual_amount = self.cart_icon_amount_of_products()
        assert actual_amount == amount, \
            f"Error. Amount of added product should be {amount}. Actual amount is {actual_amount}"

    def tooltip_subtotal(self) -> float:
        currency_symbol = self.find_element(*get_locator('CURRENCY')).text
        return float(self.find_element(*tooltip_dd().get_cart_tooltip_elements('SUBTOTAL')).text.split(currency_symbol)[
                         1].replace(',', ''))

    def tooltip_products_titles(self):
        tooltip = get_value('TOOLTIP')
        tooltip_products_titles = \
            (product.find_element(*tooltip.get_cart_tooltip_elements('PRODUCT_TITLE')).text
             for product in self.find_elements(*tooltip.get_cart_tooltip_elements('ALL_PRODUCTS')))
        return tooltip_products_titles

    def cart_icon_amount_of_products(self):
        return int(self.find_element(*get_locator('CART')).text)

    def verify_tooltip_subtotal_sum(self, sum_products_added_to_cart: int):
        print(f"Subtotal: {self.tooltip_subtotal()}")
        print(sum_products_added_to_cart)
        assert self.tooltip_subtotal() == sum_products_added_to_cart

    def verify_tooltip_products_added_to_cart(self, products_added):
        actual_list = self.tooltip_products_titles()
        print(actual_list)
        print(products_added)
        for i in products_added:
            print(i)
        assert sorted(actual_list) == sorted(tuple(products_added)), \
            f"Error. List of products added to cart should be: {products_added}. Actual set: {actual_list}"

    def open_cart_page(self):
        self.click(*get_value('TOOLTIP').get_cart_tooltip_elements('VIEW_CART_BTN'))

    def wait_cart_icon_updated(self, amount_of_items: int):
        self.driver.wait.until(lambda driver: int(driver.find_element(*get_locator('CART')).text) == amount_of_items)

    # def wait_cart_titles_updated(self, amount_of_products: int):
    #     self.driver.wait.until(lambda driver:
    #                            len(driver.find_elements(*get_value('TOOLTIP').get_cart_tooltip_elements('ALL_PRODUCTS'))) ==
    #                            amount_of_products)
    # # def tooltip_products(self):
    # #     tooltip = get_value('TOOLTIP')
    # #     for product in self.find_elements(*tooltip.get_cart_tooltip_elements('ALL_PRODUCTS')):
    # #         print(product.find_element(*tooltip.get_cart_tooltip_elements('PRODUCT_TITLE')).text)
    # #         print(product.get_attribute('href'))
    #
    # def tooltip_products(self):
    #     tooltip = get_value('TOOLTIP')
    #     for product in self.find_element(*tooltip.get_cart_tooltip_elements('CART')):
    #         print(product.find_element(*tooltip.get_cart_tooltip_elements('PRODUCT_TITLE')).text)
    #         print(product.get_attribute('href'))
    #
    # def tooltip_content(self, added_products_list):
    #     tooltip = tooltip_dd()
    #     print(f"Subtotal: {self.tooltip_subtotal()}")
    #     print(self.find_element(*tooltip.get_cart_tooltip_elements('REMOVE_PRODUCT')).get_attribute('aria-label'))
    #     print(self.find_element(*tooltip.get_cart_tooltip_elements('VIEW_CART')).text)
    #     print(self.find_element(*tooltip.get_cart_tooltip_elements('CHECKOUT')).text)
    #     print(self.find_elements(*tooltip.get_cart_tooltip_elements('ALL_PRODUCTS')))
    #     print(self.find_elements(*tooltip.get_cart_tooltip_elements('REMOVE_PRODUCT')))
    #     self.tooltip_products()

    # def tooltip_products(self):
    #     tooltip = get_value('TOOLTIP')
    #     for product in self.find_elements(*tooltip.get_cart_tooltip_elements('ALL_PRODUCTS')):
    #         print(self.find_elements(*tooltip.get_cart_tooltip_elements('ALL_PRODUCTS')))
    #         print(self.find_elements(*tooltip.get_cart_tooltip_elements('ALL_PRODUCTS')))
    #         print(tooltip.get_cart_tooltip_elements)
    #         print(tooltip.cart_added_product_title)
    #         print('Title:----')
    #         print(product.find_element(*tooltip.cart_added_product_title).text)
    #         print(product.find_element(*tooltip.get_cart_tooltip_elements('PRODUCT_TITLE')).text)
    #         print('Title:----')

    # def verify_all_titles_from_tooltip_products(self, products_added):
    #     tooltip_titles = self.tooltip_products_titles()
    #     return all([item in tooltip_titles for item in products_added])
