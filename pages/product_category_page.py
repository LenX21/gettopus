from time import sleep
from app.logger import logger
from locators import locators as cl
from app.config import TestData
from locators.ProductCategory import ProductCategoryLocators
from pages.base_page import Page


class ProductCategoryPage(Page):
    # def verify_category_is_opened_by_title(self, category_title):
    #     self.wait_title_contains(category_title)

    def open_product_category_page_by_name(self, category_name):
        self.open_page(self._test_data.get_product_link_by_name(category_name))

    def hover_over_product_by_number(self, number: int):
        self.mouse_hover_action(*cl.ProductCategoryLocators.get_product_locator_by_number(number))

    # TODO: duplicated by ProductPage.get_search_for(self, text) - keep only one
    def verify_category_is_opened(self, category_title):
        actual_result = self.current_open_category()
        assert actual_result == category_title.upper(), "Error. Incorrect category is opened. " \
                                                        f"Expected result: {category_title.upper()} - " \
                                                        f"Actual result: {actual_result}"

    def current_open_category(self):
        return self.find_element(*ProductCategoryLocators.PAGE_TITLE_ROW).text.split('/')[-1].strip()

    def verify_all_products_title(self):
        pass

    def verify_all_products_category(self, category_title):
        self.verify_product_attribute('CATEGORY', category_title)

    def verify_all_products_contain_title(self, title: str):
        for product in self.all_products_in_category():
            current = product.find_element_by_css_selector(cl.ProductAttributes.NAME)
            assert title.upper() in current.text.upper(), \
                f'Error. Product title should contains {title} in name. Current name {current.text}'

    def verify_all_products_price(self, start=False, end=False):
        if start:
            print('Start price')
        if end:
            print("End price")

    def verify_product_attribute(self, attribute: str, attribute_value: str):
        expected_category = self._test_data.PRODUCT_CATEGORIES[attribute_value.lower()].product_category
        for product in self.all_products_in_category():
            current = product.find_element_by_css_selector(cl.ProductAttributes[attribute])
            assert current.text.upper() == expected_category, \
                f'Error. Expected {attribute} should be {expected_category}. Actual result is {current.text}'

    def correct_category_is_opened(self, category_title):
        self.verify_category_is_opened(category_title)
        self.verify_product_attribute('CATEGORY', category_title)

    def all_products_in_category(self):
        return self.find_elements(*ProductCategoryLocators.PRODUCTS)

    def open_product_page(self, product_name='', product_number=0):
        self.wait_for_element_appears(*ProductCategoryLocators.PAGE_TITLE_ROW)
        if product_name:
            for product in self.all_products_in_category():
                if product.find_element_by_css_selector(cl.ProductAttributes.NAME).text.upper() == product_name.upper():
                    product.click()
                    break
        elif product_number:
            self.all_products_in_category()[product_number-1].click()
        else:
            raise ValueError('No search criteria specified')

    def number_of_products_is_shown(self):
        text_per_page = self.find_element(*ProductCategoryLocators.RESULT_COUNT).text
        for word in text_per_page.split():
            if word.isdigit():
                logger.info(f'{text_per_page}, Get number: {word} to count products per page')
                return int(word)

    def compare_number_products_shown_per_page(self):
        number_per_page = self.number_of_products_is_shown()
        assert len(self.all_products_in_category()) == number_per_page, \
            f"Error. Amount of products on page should be: {number_per_page}. Current amount {len(self.all_products_in_category())}"

