from selenium.webdriver.common.by import By
from strenum import StrEnum


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
    ADD_TO_CARD_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"][name="add-to-cart"]')
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'h1.product-title.product_title.entry-title')
    PRODUCT_SHORT_DESCRIPTION = (By.CSS_SELECTOR, 'div.product-short-description')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price.product-page-price.price-on-sale')
