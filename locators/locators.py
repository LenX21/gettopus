from selenium.webdriver.common.by import By
from strenum import StrEnum
from enum import Enum

from locators.FooterMenu import FooterLocators
from locators.ProductCategory import ProductCategoryLocators
from locators.QuickView import QuickViewLocators
from locators.TopMenu import TopMenuLocators


class WishlistData(StrEnum):
    NAME = 'td.product-name'
    IMAGE = 'td.product-thumbnail'
    REMOVE = 'product-remove'


class ProductAttributes(StrEnum):
    NAME = 'p.name.product-title'
    CATEGORY = 'p.category.uppercase'
    IMAGE = 'img[src*="https"]'
    PRICE = 'span.price'
    ONSALE = 'span.onsale'
    RATING = 'div.star-rating'


class ProductCategoriesTopMenu(Enum):
    # category:
    MAC = TopMenuLocators(category_name='MACBOOK', locator_id='menu-item-468')
    IPHONE = TopMenuLocators(category_name='IPHONE', locator_id='menu-item-469')
    IPAD = TopMenuLocators(category_name='IPAD', locator_id='menu-item-470')
    WATCH = TopMenuLocators(category_name='WATCH', locator_id='menu-item-471')
    ACCESSORIES = TopMenuLocators(category_name='AIRPODS', locator_id='menu-item-472')
    # other:
    ACCOUNT = TopMenuLocators(css_selector='a.nav-top-link.nav-top-not-logged-in[data-open="#login-form-popup"]')
    LOGO = TopMenuLocators(css_selector='a[rel="home"]')
    PRICE = TopMenuLocators(css_selector='span.cart-price')
    CART = TopMenuLocators(css_selector='li.cart-item.has-icon.has-dropdown span.cart-icon.image-icon')
    TOOLTIP = TopMenuLocators(css_selector='li.cart-item.has-icon.has-dropdown.current-dropdown')
    CURRENCY = TopMenuLocators(css_selector='span.woocommerce-Price-currencySymbol')


# ProductCategoriesTopMenu.MAC

class ProductCategoryFooter(Enum):
    MAC = FooterLocators(category_name='MACBOOK', css_selector='li.menu-item-468')
    IPHONE = FooterLocators(category_name='IPHONE', css_selector='li.menu-item-469')
    IPAD = FooterLocators(category_name='IPAD', css_selector='li.menu-item-470')
    WATCH = FooterLocators(category_name='WATCH', css_selector='li.menu-item-471')
    ACCESSORIES = FooterLocators(category_name='AIRPODS', css_selector='li.menu-item-472')
    BEST_SELLING = FooterLocators(locator_id='woocommerce_products-11')
    LATEST = FooterLocators(locator_id='woocommerce_products-12')
    TOP_RATED = FooterLocators(locator_id='woocommerce_top_rated_products-3')
    COPYRIGHTS = FooterLocators(css_selector='div.copyright-footer')
    CURRENCY = FooterLocators(css_selector='span.woocommerce-Price-currencySymbol')


class ProductCategoriesTopMenuOther(Enum):
    SEARCH_ICON_CATEGORY = TopMenuLocators(css_selector='a[aria-label] i.icon-search')
    SEARCH_ICON_NEAR_SEARCH_FIELD = \
        TopMenuLocators(css_selector='div.flex-col.flex-grow '
                                     'button.ux-search-submit.submit-button.secondary.button.icon'
                                     '[value="Search"][type="submit"]')
    SEARCH_FIELD = TopMenuLocators(locator_id='woocommerce-product-search-field-0')
    EMPTY_CART = \
        TopMenuLocators(css_selector='ul.nav-dropdown.nav-dropdown-default p.woocommerce-mini-cart__empty-message')
    # LOGIN = TopMenuLocators(css_selector='a.nav-top-link.nav-top-not-logged-in[data-open="#login-form-popup"]')
    # LOGO = TopMenuLocators(css_selector='a[rel="home"]')
    # CART = TopMenuLocators(css_selector='span.cart-price')
    # CART_ICON = TopMenuLocators(css_selector='li.cart-item.has-icon.has-dropdown span.cart-icon.image-icon')


class HomePageLocators:
    CURRENT_LATEST_PRODUCTS_ON_SALE = None
    TOP_BANNER = (By.CSS_SELECTOR, 'div.slider-wrapper.relative')

    # TOP_BANNER_RIGHT_ARROW = (By.CSS_SELECTOR,
    #                           'div.slider-wrapper.relative button.flickity-button.flickity-prev-next-button.next')
    # TOP_BANNER_LEFT_ARROW = (By.CSS_SELECTOR,
    #                          'div.slider-wrapper.relative button.flickity-button.flickity-prev-next-button.previous')
    # TOP_BANNER_DOTS_1_SELECTED = (By.CSS_SELECTOR,
    #                               'div.slider-wrapper.relative li[aria-label="Page dot 1"].dot.is-selected')
    # TOP_BANNER_DOTS_1_NOT_SELECTED = (By.CSS_SELECTOR,
    #                                   'div.slider-wrapper.relative li[aria-label="Page dot 1"].dot')
    # TOP_BANNER_DOTS_2_SELECTED = (By.CSS_SELECTOR,
    #                               'div.slider-wrapper.relative li[aria-label="Page dot 2"].dot.is-selected')
    # TOP_BANNER_DOTS_2_NOT_SELECTED = (By.CSS_SELECTOR, 'div.slider-wrapper.relative li[aria-label="Page dot 2"].dot')
    #   Only thore should remains in the end
    TOP_BANNER_CATEGORY_LINK = (By.CSS_SELECTOR,
                                'div.slider-wrapper.relative div.banner.is-selected a[href*="product-category"]')
    TOP_BANNER_SELECTED = (By.CSS_SELECTOR,
                           'div.slider-wrapper.relative div.banner.has-hover.is-selected')
    TOP_BANNER_ALL = (By.CSS_SELECTOR,
                      'div.slider-wrapper.relative div.banner.has-hover')
    TOP_BANNER_SELECTED_DOT = (By.CSS_SELECTOR,
                               'div.slider-wrapper.relative li.dot.is-selected')
    TOP_BANNER_ALL_DOTS = (By.CSS_SELECTOR,
                           'div.slider-wrapper.relative li.dot')

    PRODUCT_SECTIONS = (By.CSS_SELECTOR, 'div.container.section-title-container')
    # LATEST_PRODUCT_ON_SALE = (By.XPATH,
    #                           '//span[@class="section-title-main" and contains(text(), "Latest products on sale")]')
    # TODO: Duplicated by Product_category
    LATEST_PRODUCTS_ON_SALE = (By.CSS_SELECTOR,
                               'div.product-small.col.has-hover.product.type-product')
    CONTENT_SECTION = (By.ID, 'content')
    MAIN_CONTENT_SECTIONS = (By.CSS_SELECTOR, 'div.container.section-title-container')
    PRODUCT_ON_SALE_QUICK_VIEW = (By.CSS_SELECTOR, 'a.quick-view.quick-view-added')

    # Quick View Section
    quick_view_content = 'div.mfp-content'
    # g = 'div.mfp-content div.slide.is-selected img[src*="https://gettop.us/wp-content/uploads/2013/08/mc13-4-600x338.jpeg"]'
    QUICK_VIEW_CLOSE = (By.CSS_SELECTOR, 'button[title*="Close"].mfp-close')
    QUICK_VIEW_CONTENT_IS_READY = (By.CSS_SELECTOR, 'div.mfp-bg.mfp-ready')
    # QUICK_VIEW_CONTENT_TEXT_ALL = (By.CSS_SELECTOR, 'div.mfp-content div.product-lightbox-inner')
    QUICK_VIEW_CONTENT_TEXT_ALL = (By.CSS_SELECTOR, f'{quick_view_content} div.product-lightbox-inner')
    # QUICK_VIEW_CONTENT_IMAGES = (By.CSS_SELECTOR, 'div.slide[aria-selected="false"] img')
    # QUICK_VIEW_IMAGE_DOTS = (By.CSS_SELECTOR, 'div.mfp-content li.dot[aria-label*="Page dot"]')
    # $$('div.mfp-content li.dot[aria-label*="Page dot"]:not(.is-selected)')
    QUICK_VIEW_IMAGE_DOTS_NOT_SELECTED = (By.CSS_SELECTOR,
                                          f'{quick_view_content} li.dot[aria-label*="Page dot"]:not(.is-selected)')
    QUICK_VIEW_CURRENT_IMAGE = (By.CSS_SELECTOR, f'{quick_view_content} div.slide.is-selected img')
    MAIN_CONTENT_CATEGORIES = (By.CSS_SELECTOR, 'div.product-category.col')
    MAIN_CONTENT_CATEGORIES_IS_SELECTED = (By.CSS_SELECTOR, 'div.product-category.col.is-selected')

    @staticmethod
    def get_category_name():
        categories = HomePageLocators.MAIN_CONTENT_CATEGORIES[1]
        categories_attribute = 'h5.uppercase.header-title'
        return By.CSS_SELECTOR, f'{categories} {categories_attribute}'.strip()

    @staticmethod
    def navigate_between_banners(direction: str):
        return (By.CSS_SELECTOR,
                f'div.slider-wrapper.relative button.flickity-button.flickity-prev-next-button.{direction}')

    @staticmethod
    def get_dot_top_banner_by_number(number: int, is_selected=False):
        selection = '.dot.is-selected' if is_selected else ''
        return By.CSS_SELECTOR, f'div.slider-wrapper.relative li.dot[aria-label="Page dot {number}"]{selection}'

    @staticmethod
    def set_current_product(product_webelement):
        HomePageLocators.CURRENT_LATEST_PRODUCTS_ON_SALE = HomePageLocators.get_current_product_css_locator(
            product_webelement)

    @staticmethod
    def get_current_product_css_locator(webelement):
        class_css = '.'.join(webelement.get_attribute("class").split(" "))
        return By.CSS_SELECTOR, f'div.{class_css}'

    # @staticmethod
    # def get_wishlist_heart_icon_for_product_on_sale(product, is_added=False):
    #     if isinstance(product, tuple):
    #         current_product_css = product[1]
    #     else:
    #         current_product_css = HomePageLocators.get_current_product_css_locator(product)[1]
    #     wish_button_css = WishlistLocators.get_wish_button(is_added=is_added)[1]
    #     return By.CSS_SELECTOR, ' '.join([current_product_css, wish_button_css])

    @staticmethod
    def get_wishlist_heart_icon_for_product_on_sale(product, is_added=False):
        wish_button_css = WishlistLocators.get_wish_button(is_added=is_added)[1]
        return By.CSS_SELECTOR, ' '.join([HomePageLocators.get_product_css(product), wish_button_css])

    @staticmethod
    def get_quick_view_link_path(product):
        return By.CSS_SELECTOR, \
               ' '.join([HomePageLocators.get_product_css(product), HomePageLocators.PRODUCT_ON_SALE_QUICK_VIEW[1]])

    @staticmethod
    def get_product_css(product):
        if isinstance(product, tuple):
            return product[1]
        return HomePageLocators.get_current_product_css_locator(product)[1]

    @staticmethod
    def get_quick_view_image_locator(image_obj):
        image_obj.get_attribute("src")
        return By.CSS_SELECTOR, \
               f'{HomePageLocators.QUICK_VIEW_CURRENT_IMAGE[1]}[src="{image_obj.get_attribute("src")}"]'


class WishlistLocators:
    MAIN_FIELD = (By.ID, 'main')
    WISHLIST_TITLE = (By.CSS_SELECTOR, 'main#main div.my-account-header.page-title.normal-title')
    WISHLIST_MAIN_TABLE_CONTENT = (By.CSS_SELECTOR, 'table.shop_table.cart.wishlist_table.wishlist_view')
    WISHLIST_CONTENT_ALL_ITEMS = (By.CSS_SELECTOR, 'tbody.wishlist-items-wrapper tr')
    # WISHLIST_CONTENT_ALL_PRODUCTS_NAMES = (By.CSS_SELECTOR, 'tbody.wishlist-items-wrapper tr td.product-name')
    WISHLIST_CONTENT_PRODUCT_ADDED_POP = (By.CSS_SELECTOR, 'div#yith-wcwl-popup-message[style*="display: block"]')

    # WISHLIST_BUTTON_CSS = (By.CSS_SELECTOR, 'button.wishlist-button.button.is-outline.circle.icon')

    @staticmethod
    def get_wish_button(is_added=False):
        added = '.wishlist-added' if is_added else ''
        # return By.CSS_SELECTOR, 'button.wishlist-button.button.is-outline.circle.icon.wishlist-added'
        return By.CSS_SELECTOR, f'button.wishlist-button.button.is-outline.circle.icon{added}'

    @staticmethod
    def get_product_attributes(attribute_css_locator: WishlistData):
        return By.CSS_SELECTOR, f'tbody.wishlist-items-wrapper tr {attribute_css_locator}'


class ProductPageLocators:
    PHOTOSWIPE_HIDDEN = By.CSS_SELECTOR, 'div.pswp[aria-hidden="true"]'
    PHOTOSWIPE = By.CSS_SELECTOR, 'div.pswp.pswp--open.pswp--visible'
    PHOTOSWIPE_TOP_BAR = By.CSS_SELECTOR, 'pswp__top-bar'
    PHOTOSWIPE_IS_CLICKABLE = By.CSS_SELECTOR, 'div.pswp__ui.pswp__ui--fit:not(.pswp__ui--idle)'
    PHOTOSWIPE_ARROW_RIGHT = By.CSS_SELECTOR, 'button.pswp__button--arrow--right'
    PHOTOSWIPE_IMAGES = By.CSS_SELECTOR, 'div.pswp__container div.pswp__item'
    PHOTOSWIPE_COUNTER = By.CSS_SELECTOR, 'div.pswp__ui div.pswp__counter'
    PHOTOSWIPE_CLOSE_BTN = By.CSS_SELECTOR, 'button.pswp__button.pswp__button--close'
    ADD_TO_CARD_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"][name="add-to-cart"]')
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'h1.product-title.product_title.entry-title')
    PRODUCT_IMAGE = By.CSS_SELECTOR, 'div.woocommerce-product-gallery__image.slide.first.is-selected img'
    PRODUCT_ALL_IMAGES = By.CSS_SELECTOR, 'div.woocommerce-product-gallery__image.slide img'
    PRODUCT_SHORT_DESCRIPTION = (By.CSS_SELECTOR, 'div.product-short-description')
    PRODUCT_PRICE_ONSALE = By.CSS_SELECTOR, 'p.price.product-page-price :not(del) span.woocommerce-Price-amount.amount'
    # PRODUCT_PRICE_ONSALE = By.CSS_SELECTOR, 'p.price.product-page-price.price-on-sale'
    PRODUCT_PRICE_ORIGIN = By.CSS_SELECTOR, 'p.price.product-page-price del span.woocommerce-Price-amount.amount'
    PRODUCT_PRICES = By.CSS_SELECTOR, 'p.price.product-page-price span.woocommerce-Price-amount.amount'
    CURRENCY_SYMBOL = By.CSS_SELECTOR, 'p.price.product-page-price span.woocommerce-Price-currencySymbol'
    EMPTY_SEARCH_RESULT = (By.CSS_SELECTOR, 'div.shop-container p.woocommerce-info')
    SEARCH_RESULT_FOR = (By.CSS_SELECTOR, 'nav.woocommerce-breadcrumb.breadcrumbs.uppercase')
    # SEARCH_RESULT_FOR = (By.CSS_SELECTOR, 'nav.woocommerce-breadcrumb.breadcrumbs.uppercase span.divider:last-child')


class LoginFormLocators:
    LOGIN_FORM = By.CSS_SELECTOR, 'div.account-login-inner'


class CartLocators:
    EMPTY_CART = By.CSS_SELECTOR, 'div.text-center p.cart-empty'
    RETURN_TO_SHOP_BTN = By.CSS_SELECTOR, 'a.button.primary.wc-backward'
    CART_PAGE_TITLE = By.CSS_SELECTOR, 'div.checkout-page-title.page-title'
    CART_CURRENT_STATE = By.CSS_SELECTOR, 'div.checkout-page-title.page-title a.current'


class QuickViewWindowLocators(Enum):
    # self.quick_view_container = 'div.product-quick-view-container'
    QUICK_VIEW = QuickViewLocators(css_selector='div.product-quick-view-container')
    QUICK_VIEW_CLOSE_BTN = QuickViewLocators(css_selector='button[title*="Close"].mfp-close')
    QUICK_VIEW_PRODUCT_LINK = QuickViewLocators(css_selector='a.quick-view.quick-view-added')
    QUICK_VIEW_DOTS = QuickViewLocators(css_selector='div.product-quick-view-container li.dot')
    QUICK_VIEW_PRODUCT_TITLE = QuickViewLocators(css_selector='div.product-info.summary.entry-summary h1')
    QUICK_VIEW_ADD_TO_CART_BTN = QuickViewLocators(css_selector='button[type="submit"][name="add-to-cart"]')
    QUICK_VIEW_DOT_SELECTED = QuickViewLocators(css_selector='div.product-quick-view-container li.dot.is-selected')
    QUICK_VIEW_DOTS_DONT_SELECTED = \
        QuickViewLocators(css_selector='div.product-quick-view-container li.dot:not(.is-selected)')


