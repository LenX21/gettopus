from enum import Enum

from selenium.webdriver.common.by import By


class TopMenuTooltipElements(Enum):
    VIEW_CART_BTN = 'p.buttons a.button.wc-forward:not(.checkout)'
    CHECKOUT_BTN = 'p.buttons a.button.checkout.wc-forward'
    REMOVE_PRODUCT_BTN = 'a.remove.remove_from_cart_button'
    SUBTOTAL = 'p.woocommerce-mini-cart__total.total span.amount'
    ALL_PRODUCTS = 'li.woocommerce-mini-cart-item.mini_cart_item'
    PRODUCT_TITLE = 'a:not(.remove_from_cart_button)'
    # CURRENCY = By.CSS_SELECTOR, 'span.woocommerce-Price-currencySymbol'
    # TOOLTIP = By.CSS_SELECTOR, 'li.cart-item.has-icon.has-dropdown.current-dropdown'
    # REMOVE_PRODUCT_BTN = By.CSS_SELECTOR, 'a.remove.remove_from_cart_button'
    # PRODUCT_TITLE = By.CSS_SELECTOR, 'a:not(.remove_from_cart_buttton)'
    # PAGE_TITLE_ROW = (By.CSS_SELECTOR, 'nav.woocommerce-breadcrumb.breadcrumbs.uppercase')
    # ALL_PRODUCTS = 'li.woocommerce-mini-cart-item.mini_cart_item'
    # ALL_PRODUCTS = 'li.woocommerce-mini-cart-item.mini_cart_item a:not(.remove_from_cart_button)'



class TopMenuLocators:
    def __init__(self, category_name=None, locator_id=None, css_selector=None):
        self._category_name = category_name
        self.id = locator_id
        self.css_selector = css_selector

    @property
    def category_name(self):
        return self._category_name

    @property
    def locator(self):
        if self.id:
            return By.ID, self.id
        if self.css_selector:
            return By.CSS_SELECTOR, self.css_selector
        raise ValueError('Neither ID or LOCATOR defined')

    @property
    def category_drop_down_menu(self):
        if self.id:
            return By.CSS_SELECTOR, \
                   f'li#{self.id}.menu-item.menu-item-has-children.has-dropdown ul.sub-menu.nav-dropdown'
        raise ValueError('Neither ID or LOCATOR defined')

    @property
    def dd_items(self):
        selector, dd_menu = self.category_drop_down_menu
        return selector, ' '.join((dd_menu, 'li'))

    def get_cart_tooltip_elements(self, element_name: str):
        selector, locator = self.locator
        return selector, ' '.join((locator, TopMenuTooltipElements[element_name].value))

    @property
    def cart_added_product_title(self):
        return By.CSS_SELECTOR, TopMenuTooltipElements.PRODUCT_TITLE.value








