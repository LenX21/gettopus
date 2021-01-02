from enum import Enum

from selenium.webdriver.common.by import By


class FooterElements(Enum):
    CATEGORY_PRODUCT_LIST = 'ul.product_list_widget li'
    CATEGORY_PRODUCT_TITLE = 'a'
    CATEGORY_PRODUCT_PRICE_NEW = 'ins span.woocommerce-Price-amount.amount'
    CATEGORY_PRODUCT_PRICE_OLD = 'del span.woocommerce-Price-amount.amount'
    CATEGORY_PRODUCT_PRICE = 'span.woocommerce-Price-amount.amount'
    CATEGORY_TITLE = 'span.widget-title'


class FooterLocators:
    def __init__(self, category_name=None, locator_id=None, css_selector=None):
        self._category_name = category_name
        self.id = locator_id
        self.root = 'footer#footer'
        self._css_selector = css_selector

    @property
    def locator(self):
        if self.id:
            return By.ID, self.id
        if self._css_selector:
            return By.CSS_SELECTOR, ' '.join((self.root, self._css_selector))
        raise ValueError('Neither ID or LOCATOR defined')

    @property
    def category_name(self):
        return self._category_name

    @property
    def category_content(self):
        selector, locator = self.locator
        if selector == 'id':
            locator = f'#{locator}'
        return By.CSS_SELECTOR, ' '.join((locator, FooterElements.CATEGORY_PRODUCT_LIST.value))

    @property
    def category_title(self):
        selector, locator = self.locator
        if selector == 'id':
            locator = f'#{locator}'
        return By.CSS_SELECTOR, ' '.join((locator, FooterElements.CATEGORY_TITLE.value))

    @property
    def category_product_price(self):
        return By.CSS_SELECTOR, FooterElements.CATEGORY_PRODUCT_PRICE.value

    @property
    def category_product_price_onsale_new(self):
        return By.CSS_SELECTOR, FooterElements.CATEGORY_PRODUCT_PRICE_NEW.value

    @property
    def category_product_price_onsale_old(self):
        return By.CSS_SELECTOR, FooterElements.CATEGORY_PRODUCT_PRICE_OLD.value

    @property
    def category_product_title(self):
        return By.CSS_SELECTOR, FooterElements.CATEGORY_PRODUCT_TITLE.value
