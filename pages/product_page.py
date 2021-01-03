import time

from app.config import TestData
from app.logger import logger
from locators.locators import ProductPageLocators
from pages.base_page import Page


class ProductPage(Page):

    def open_product_page(self):
        self.open_page(TestData.PRODUCT_PAGE_AIRPODS)

    def add_product_to_the_card(self):
        pass

    # TODO: Never used - remove it
    def verify_product_data(self):
        self.wait_for_element_appears(*ProductPageLocators.PRODUCT_TITLE)
        # print(self.find_element(*ProductPageLocators.PRODUCT_TITLE).text)
        # print(self.find_element(*ProductPageLocators.PRODUCT_SHORT_DESCRIPTION).text)
        logger.info(f'current product: {self.find_element(*ProductPageLocators.PRODUCT_TITLE).text}')
        assert self.products_titles() != '', \
            f"Error. Title should be present for all products. Current title: {self.products_titles()}"
        assert self.product_price() > 0, f"Error. Price should be more than 0. Current price {self.product_price()}"
        description = self.find_element(*ProductPageLocators.PRODUCT_SHORT_DESCRIPTION).text
        assert description != '', \
            f"Error. Description should be present for all products. Current description: {description}"
        self.verify_image_is_loaded(self.find_element(*ProductPageLocators.PRODUCT_IMAGE))

    def verify_product_title(self, product_title_search_text):
        current_title = self.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        assert current_title.lower().strip() == product_title_search_text.lower().strip(), \
            f"Error. Incorrect title is shown. Expected: {product_title_search_text} - Actual: {current_title}"

    def verify_empty_search_result(self, text_to_verify: str):
        search_result = self.find_element(*ProductPageLocators.EMPTY_SEARCH_RESULT).text
        assert search_result.strip() == text_to_verify.strip(), \
            f"Error. Expected: {text_to_verify} - Actual:{search_result} "

    # TODO: duplicated by ProductCategoryPage.verify_category_is_opened(self, text) - keep only one
    def get_search_for(self, text):
        search_result_for = self.find_element(*ProductPageLocators.SEARCH_RESULT_FOR).text.split("/")[-1].strip()
        logger.info(f'Search for: {search_result_for} - result is "{search_result_for.split("/")[-1].strip()}"')
        assert text.upper() in search_result_for.split("/")[-1].strip().upper(), \
            f"Error. Search result should contain word: {text.upper()}. Actual result: '{search_result_for}'"

    def add_product_to_cart(self):
        # self.verify_product_data()
        self.click(*ProductPageLocators.ADD_TO_CARD_BUTTON)

    def get_product_price(self):
        currency_symbol = self.find_element(*ProductPageLocators.CURRENCY_SYMBOL).text
        prices = self.find_elements(*ProductPageLocators.PRODUCT_PRICES)
        if len(prices) > 1:
            price = self.find_element(*ProductPageLocators.PRODUCT_PRICE_ONSALE)
        else:
            price = prices[0]
        return float(price.text.split(currency_symbol)[1].replace(',', ''))

    def products_titles(self):
        return self.find_element(*ProductPageLocators.PRODUCT_TITLE).text

    def product_price(self):
        return self.get_product_price()

    def verify_image_is_loaded(self, image_obj):
        # print(image_is_selected.size)
        image_is_loaded = \
            self.driver.execute_script(
                "return arguments[0].complete && typeof arguments[0].naturalWidth != \"undefined\" && arguments[0].naturalWidth > 0",
                image_obj)
        print(self.driver.execute_script(
            "return arguments[0].complete && typeof arguments[0].naturalWidth != \"undefined\" && arguments[0].naturalWidth > 0",
            image_obj))
        assert image_is_loaded, "Error. Image is not loaded"

    def zoom_in_product_image(self):
        self.wait_for_element_appears(*ProductPageLocators.PRODUCT_IMAGE)
        self.click(*ProductPageLocators.PRODUCT_IMAGE)
        self.wait_for_element_appears(*ProductPageLocators.PHOTOSWIPE)

    def close_zoom_image(self):
        self.wait_for_element_appears(*ProductPageLocators.PHOTOSWIPE)
        self.mouse_hover_action(*ProductPageLocators.PHOTOSWIPE_TOP_BAR)
        self.click(*ProductPageLocators.PHOTOSWIPE_CLOSE_BTN)
        self.wait_for_element_appears(*ProductPageLocators.PHOTOSWIPE_HIDDEN)

    def swipe_between_zoom_in_images(self):
        all_zoom_in_images = self.find_elements(*ProductPageLocators.PHOTOSWIPE_IMAGES)
        for _ in range(4):
            print('Click Arrow')
            self.mouse_hover_action(*ProductPageLocators.PHOTOSWIPE_TOP_BAR)
            self.find_element(*ProductPageLocators.PHOTOSWIPE_IS_CLICKABLE)
            self.click(*ProductPageLocators.PHOTOSWIPE_ARROW_RIGHT)
            print(self.find_element(*ProductPageLocators.PHOTOSWIPE_COUNTER).text)
            for image in all_zoom_in_images:
                print(image.get_attribute('style'))

