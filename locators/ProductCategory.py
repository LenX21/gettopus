from selenium.webdriver.common.by import By


class ProductCategoryLocators:
    PAGE_TITLE_ROW = (By.CSS_SELECTOR, 'nav.woocommerce-breadcrumb.breadcrumbs.uppercase')
    #     h1.product-title.product_title.entry-title
    PRODUCTS = (By.CSS_SELECTOR, 'div.product-small.col.has-hover.product.type-product')
    RESULT_COUNT = By.CSS_SELECTOR, 'p.woocommerce-result-count.hide-for-medium'
    # PRODUCT_BY_NUMBER = By.CSS_SELECTOR, 'div.shop-container div.product-small.col.has-hover.product.type-product:nth-child(3)'

    # @staticmethod
    # def get_current_product_css_locator(webelement):
    #     class_css = '.'.join(webelement.get_attribute("class").split(" "))
    #     return By.CSS_SELECTOR, f'div.{class_css}'

    @staticmethod
    def get_product_locator_by_number(number: int):
        selector, locator = ProductCategoryLocators.PRODUCTS
        return selector, f'div.shop-container {locator}:nth-child({number})'

    @staticmethod
    def get_product_title_by_number(number: int):
        selector, locator = ProductCategoryLocators.PRODUCTS
        return selector, f'{locator}:nth-child({number}) p.name.product-title'
        # 'div.product-small.col.has-hover.product.type-product:nth-of-type(2) p.name.product-title'


