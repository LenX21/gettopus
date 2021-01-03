from selenium.webdriver.common.by import By

from locators import locators as cl


class QuickViewLocators:
    def __init__(self, category_name=None, locator_id=None, css_selector=None):
        self._category_name = category_name
        self.id = locator_id
        self.css_selector = css_selector

    @property
    def locator(self):
        if self.id:
            return By.ID, self.id
        if self.css_selector:
            return By.CSS_SELECTOR, self.css_selector
        raise ValueError('Neither ID or LOCATOR defined')

    def get_quick_view_for_product_by_number(self, number: int):
        selector, locator = self.locator
        return selector, f'{cl.ProductCategoryLocators.PRODUCTS[1]}:nth-of-type({number}) {locator}'
# #     'div.product-small.col.has-hover:nth-of-type(1) a.quick-view.quick-view-added'
