from app.logger import logger
from locators.locators import ProductPageLocators
from pages.base_page import Page
from pages.top_menu_page import TopMenuPage


class ProductPage(Page):
    def add_product_to_the_card(self):
        pass

    # TODO: Never used - remove it
    def verify_product_data(self):
        self.wait_for_element_appears(*ProductPageLocators.PRODUCT_TITLE)
        print(self.find_element(*ProductPageLocators.PRODUCT_SHORT_DESCRIPTION).text)
        print(self.find_element(*ProductPageLocators.PRODUCT_TITLE).text)
        logger.info(f'current product: {self.find_element(*ProductPageLocators.PRODUCT_TITLE).text}')
        # self.find_element(*ProductPageLocators.PRODUCT_PRICE)
        # self.find_element(*ProductPageLocators.PRODUCT_PRICE)

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

    def get_products_titles(self):
        return self.find_element(*ProductPageLocators.PRODUCT_TITLE).text


