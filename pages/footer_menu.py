import time

from app.logger import logger
from pages.base_page import Page
from locators import locators as cl


def get_locator(element: str):
    return cl.ProductCategoryFooter[element].value.locator


def get_value(element: str):
    return cl.ProductCategoryFooter[element].value


class FooterMenu(Page):
    product_category = {
        'BEST SELLING': 'BEST_SELLING',
        'LATEST': 'LATEST',
        'TOP RATED': 'TOP_RATED'
    }

    def category_products(self, category_name: str):
        return self.find_elements(*get_value(category_name).category_content)
        # best_selling_items = cl.ProductCategoryFooter.BEST_SELLING.value.category_content
        # for product in self.find_elements(*get_value('BEST_SELLING').category_content):
        # print(best_selling_items)
        # print(self.find_elements(*best_selling_items))
        # for product in self.find_elements(*best_selling_items):
        #     print(product.text)

    def verify_category_content_is_not_empty(self, category_name: str):
        category = self.product_category[category_name]
        title = self.find_element(*get_value(category).category_title)
        assert title.text.upper() == category_name
        assert len(self.category_products(category)) != 0

    def verify_copyright(self, text_to_verify: str):
        assert text_to_verify.lower() in self.find_element(*get_locator('COPYRIGHTS')).text.lower()

    def open_category(self, category_name):
        self.click(*get_locator(category_name))

    def verify_products_attribute(self, category_name):
        no_errors = True
        category = self.product_category[category_name]
        for product in self.category_products(category):
            title = product.find_element(*get_value(category).category_product_title).text
            price = self.get_price(product, category)
            # print(f'Title: {title}\tPrice {price}')
            if not title or not price:
                logger.error(f"Product has no Title or Price: '{title}' - '{price}'")
                no_errors = False
        assert no_errors, "Product(s) doesn't have title ot price"

    def get_price(self, product_obj, category_name: str):
        prices = product_obj.find_elements(*get_value(category_name).category_product_price)
        if len(prices) == 1:
            return self.convert_price_to_float(prices[0].text)
        new_price = product_obj.find_element(*get_value(category_name).category_product_price_onsale_new)
        return self.convert_price_to_float(new_price.text)

    def convert_price_to_float(self, price_text: str):
        currency_symbol = self.find_element(*get_locator('CURRENCY')).text
        return float(price_text.split(currency_symbol)[1].replace(",", ""))


        # old_price = product_obj.find_element(*get_value(category_name).category_product_price_onsale_old).text
        # new_price = product_obj.find_element(*get_value(category_name).category_product_price_onsale_new).text
        # print(f'Old price: {float(old_price.split(currency_symbol)[1].replace(",", ""))}'
        #       f' New price: {new_price.split(currency_symbol)[1]}')
        # price = product_obj.find_element(*get_value(category_name).category_product_price_onsale_new).text