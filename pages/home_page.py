from time import sleep

from selenium.common.exceptions import NoSuchElementException
from app.logger import logger
from pages.base_page import Page
from app.config import TestData
from locators.locators import HomePageLocators
from locators.ProductCategory import ProductCategoryLocators
from app.config import Directions
from locators import locators as cl


class HomePage(Page):
    CURRENT_ACTIVE_BANNER = None
    CURRENT_ACTIVE_DOT = None
    _products_names = []

    # def __init__(self, driver):
    #     super.__init__(driver)
    #     self.locators = ProductCategoryLocators('HOMR')

    def open_home_page(self):
        self.open_page(TestData.BASE_URL)

    def verify_home_page_is_opened(self):
        assert self.get_url() == TestData.BASE_URL, f"Error. Home page: {TestData.BASE_URL} should be opened. " \
                                                    f"Current page is {self.get_url()}"

    def get_active_banner(self):
        all_banners = self.find_elements(*HomePageLocators.TOP_BANNER_ALL)
        for banner in all_banners:
            if banner.get_attribute("aria-selected") == "true":
                return banner
        return None

    def set_active_banner(self):
        self.CURRENT_ACTIVE_BANNER = self.get_active_banner()
        logger.info(f'Set active banner like: {self.CURRENT_ACTIVE_BANNER.get_attribute("id")}')

    def set_active_dot(self):
        self.CURRENT_ACTIVE_DOT = self.find_element(*HomePageLocators.TOP_BANNER_SELECTED_DOT)
        logger.info(f'Set active dot like: {self.CURRENT_ACTIVE_DOT.get_attribute("aria-label")}')

    def get_all_banners(self):
        return self.find_elements(*HomePageLocators.TOP_BANNER_ALL)

    def hover_over_banner(self):
        self.wait_for_element_appears(*HomePageLocators.TOP_BANNER)
        self.mouse_hover_action(*HomePageLocators.TOP_BANNER)
        self.set_active_banner()

    def top_banner_arrow_click(self, direction: str):
        self.hover_over_banner()
        arrow = Directions[direction]
        logger.info(f'Click {arrow} arrow on the top banner Home page')
        self.click(*HomePageLocators.navigate_between_banners(arrow))

    def verify_banner_changed(self):
        assert len(self.get_all_banners()) >= 2, "Error, there are should be more then one banner"
        assert self.CURRENT_ACTIVE_BANNER != self.get_active_banner(), \
            f"Error, Banner on home page should be updated"
        self.CURRENT_ACTIVE_BANNER = None

    def click_dot_by_number_on_top_banner(self, dot_number: int):
        self.wait_element_is_clickable(*HomePageLocators.TOP_BANNER_SELECTED_DOT)
        logger.info(f'Click on Top Banner bottom dot {dot_number}')
        self.click(*HomePageLocators.get_dot_top_banner_by_number(dot_number))

    def verify_dot_with_specific_number_is_selected(self, dot_number: int):
        logger.info(f'Make sure that dot "{dot_number}" currently selected')
        self.wait_for_element_appears(*HomePageLocators.get_dot_top_banner_by_number(dot_number, is_selected=True))

    def open_product_category_by_clicking_on_active_banner(self, open_in_new_window=False):
        self.hover_over_banner()
        link_name_css = f'a[href*="{TestData.PRODUCT_CATEGORY_PARTIAL_LINK}"]'
        link_to_category = self.CURRENT_ACTIVE_BANNER.find_element_by_css_selector(link_name_css)
        link_to_category_text = link_to_category.get_attribute("href")
        category_name_from_link = link_to_category_text.strip('/').split('/')[-1]
        if open_in_new_window:
            self.open_link_in_new_tab(link_to_category_text)
            self.switch_to_new_window()
        else:
            link_to_category.click()
        expected_title = TestData.PRODUCT_CATEGORIES[category_name_from_link]
        self.wait_title_contains(expected_title)
        logger.info(f'Open page {link_to_category_text}. Current title: {self.get_title()}')

    def open_all_product_category_by_clicking_top_banner(self):
        for banner in range(1, len(self.get_all_banners()) + 1):
            self.click_dot_by_number_on_top_banner(banner)
            self.open_product_category_by_clicking_on_active_banner(open_in_new_window=True)
            self.switch_to_first_window(close_current_window=True)

    # def verify_titles_of_content_sections(self, section_title: str):
    #     xpath = f'//span[text()="{section_title}"]'
    #     self.find_element(*HomePageLocators.MAIN_CONTENT_SECTIONS).find_element_by_xpath(xpath)
    #     self.get_product_section_by_title(section_title)
    def verify_titles_of_content_sections(self, section_title: str):
        assert self.get_product_section_by_title(section_title), \
            f'Error. There is no section with title: "{section_title}" on Home page'

    def get_product_section_by_title(self, section_title: str):
        all_sections = self.find_elements(*HomePageLocators.MAIN_CONTENT_SECTIONS)
        for child in all_sections:
            title_from_span = child.find_element_by_css_selector('span.section-title-main').text
            if title_from_span.lower() == section_title.lower():
                logger.info(f'Section with title: "{section_title}" presents on the page')
                return child
        return None

    def get_products_on_sale(self):
        return self.find_elements(*HomePageLocators.LATEST_PRODUCTS_ON_SALE)

    # TODO - Duplicated by Product Category
    def verify_product_all_mandatory_attributes(self, section_title: str):
        no_errors = True
        logger.info(f"Verify product attribute for category '{section_title}'")
        for attribute in cl.ProductAttributes:
            for product in self.get_products_on_sale():
                logger.info(f"Verify product attribute: {attribute.name}")
                try:
                    product.find_element_by_css_selector(attribute.value)
                except NoSuchElementException:
                    logger.warning(product.get_attribute("class"))
                    no_errors = False
        assert no_errors, "Error. Product doesn't have requested attribute. See log for details"

    # TODO - Duplicated by Product Category
    # Keep only one type of verification
    # verify_product_all_mandatory_attributes or verify_product_mandatory_attribute
    # update and make it not by find_element_by_css_selector, but (By.CSS, '')
    def verify_product_mandatory_attribute(self, section_title: str, attribute: str):
        no_errors = True
        for product in self.get_products_on_sale():
            logger.info(f"Verify product attribute {attribute} for category {section_title}")
            try:
                product.find_element_by_css_selector(cl.ProductAttributes[attribute])
            except NoSuchElementException:
                logger.warning(product.get_attribute("class"))
                no_errors = False
        assert no_errors, "Error. Product doesn't have requested attribute. See log for details"

    def set_current_product(self, product_webelement):
        HomePageLocators.set_current_product(product_webelement)
        self._products_names.append(product_webelement.find_element_by_css_selector(cl.ProductAttributes.NAME).text)
        print('Test wish')
        print(self._products_names)

    @staticmethod
    def get_products_name_sorted(is_sorted=True):
        names = sorted(HomePage._products_names)
        HomePage._products_names = []
        return names

    def add_product_on_sale_to_wishlist(self, product_position: int):
        product_by_number = self.get_products_on_sale()[product_position - 1]
        self.mouse_hover_action(*HomePageLocators.get_current_product_css_locator(product_by_number))
        self.click(*HomePageLocators.get_wishlist_heart_icon_for_product_on_sale(product_by_number))
        self.wait_for_element_appears(
            *HomePageLocators.get_wishlist_heart_icon_for_product_on_sale(product_by_number, is_added=True))
        # HomePageLocators.set_current_product(product_by_number)
        # self.products_names.append(product_by_number.find_element_by_css_selector(cl.ProductAttributes.NAME).text)
        self.set_current_product(product_by_number)

    def open_wishlist(self):
        self.click(*HomePageLocators.get_wishlist_heart_icon_for_product_on_sale(
            HomePageLocators.CURRENT_LATEST_PRODUCTS_ON_SALE, is_added=True))

    def open_product_page_on_sale(self, product_position: int):
        product_by_number = self.get_products_on_sale()[product_position - 1]
        self.mouse_hover_action(*HomePageLocators.get_current_product_css_locator(product_by_number))
        self.click(*HomePageLocators.get_current_product_css_locator(product_by_number))

    # def open_quick_view_product_on_sale(self, product_position: int):
    #     product_by_number = self.get_products_on_sale()[product_position - 1]
    #     self.mouse_hover_action(*HomePageLocators.get_current_product_css_locator(product_by_number))
    #     self.click(*HomePageLocators.PRODUCT_ON_SALE_QUICK_VIEW)
    #     self.set_current_product(product_by_number)

    def open_quick_view_product_on_sale(self, product_position: int):
        product_by_number = self.get_products_on_sale()[product_position - 1]
        self.mouse_hover_action(*HomePageLocators.get_current_product_css_locator(product_by_number))
        HomePageLocators.get_quick_view_link_path(product_by_number)
        self.click(*HomePageLocators.get_quick_view_link_path(product_by_number))
        self.set_current_product(product_by_number)

    def verify_quick_view_title(self):
        self.find_elements(*HomePageLocators.QUICK_VIEW_CONTENT_TEXT_ALL)
        print(self.find_elements(*HomePageLocators.QUICK_VIEW_CONTENT_TEXT_ALL))
        for item in self.find_elements(*HomePageLocators.QUICK_VIEW_CONTENT_TEXT_ALL):
            item.find_element_by_css_selector("a").text
        current_quick_view_product_name = \
            self.find_element(*HomePageLocators.QUICK_VIEW_CONTENT_TEXT_ALL).find_element_by_css_selector("a").text
        quick_view_product_name = HomePage.get_products_name_sorted()
        assert len(quick_view_product_name) == 1, \
            f"Error. Only one name should be available for verification {quick_view_product_name}"
        assert quick_view_product_name[0] == current_quick_view_product_name, \
            f"Error. Incorrect name in Quick View for current product. " \
            f"Expected name: {quick_view_product_name[0]}\nActual name: {current_quick_view_product_name}"

    def close_quick_view_x(self):
        print('Test quick')
        self.verify_quick_view_title()
        self.click(*HomePageLocators.QUICK_VIEW_CLOSE)
        self.wait_for_element_disappears(*HomePageLocators.QUICK_VIEW_CONTENT_IS_READY)

    def switch_between_quick_view_images(self):
        # current_image = self.find_element(*HomePageLocators.QUICK_VIEW_CURRENT_IMAGE)
        # # print(HomePageLocators.get_quick_view_image_locator(current_image))
        # self.find_element(*HomePageLocators.get_quick_view_image_locator(current_image))
        not_selected_dots = self.find_elements(*HomePageLocators.QUICK_VIEW_IMAGE_DOTS_NOT_SELECTED)
        for dot in not_selected_dots:
            image_is_selected = self.find_element(*HomePageLocators.QUICK_VIEW_CURRENT_IMAGE)
            # print(image_is_selected.get_attribute("src"))
            # self.broken_link(image_is_selected)
            # image_is_selected = self.find_element(*HomePageLocators.QUICK_VIEW_CURRENT_IMAGE)
            # print(image_is_selected.get_attribute("src"))
            self.verify_image_is_loaded(image_is_selected)
            # self.find_element(*HomePageLocators.get_quick_view_image_locator(current_image))
            image_is_selected_locator = HomePageLocators.get_quick_view_image_locator(image_is_selected)
            logger.info(f'Current quick view image {image_is_selected_locator[1]}')
            logger.info(f'Next dot to click: {dot.get_attribute("aria-label")}')
            dot.click()
            self.wait_for_element_disappears(*image_is_selected_locator)
            # self.wait_for_element_disappears(*HomePageLocators.get_quick_view_image_locator(image_is_selected))

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

    def open_category_by_name(self, category_name):
        for category in self.find_elements(*HomePageLocators.MAIN_CONTENT_CATEGORIES):
            title = category.find_element(*HomePageLocators.get_category_name()).text
            if title.upper() != category_name.upper():
                continue
            logger.info(f'Open category: "{title}" by clicking on it')
            category.find_element(*HomePageLocators.get_category_name()).click()
            self.wait_title_contains(category_name)
            logger.info(f"Page with title '{self.driver.title}' is opened")
            return True
        return False



    # def broken_link(self, image_obj):
    #
    #     self.driver.execute_script("arguments[0].setAttribute('src','https://tst.jpg')", image_obj)

    # TODO: Implement correct banner rotation cycle
    #       Clicking NEXT should change banner id by 1, or switch to first of it was last banner
    # def get_current_banner(self):
    # banner_data = self.find_elements(*HomePageLocators.TOP_BANNER_ALL)
    # for item in banner_data:
    #     print(item.text)
    #     print(item.get_attribute("id"))
    #     print(item.get_attribute("aria-selected"))
    #     self.driver.wait.until(ec.visibility_of_element_located(HomePageLocators.TOP_BANNER))
    #     banner_data = self.find_elements(*HomePageLocators.TOP_BANNER_ALL)
    #     banner = self.driver.find_element_by_id(banner_data[0].get_attribute("id"))
    #     print('Benner')
    #     print(type(banner))
    #     for item in banner_data:
    #         if item.get_attribute("aria-selected") == "true":
    #             print(item.location)
    #             return item
    #
    #     # print(banner)
    #     return banner
    # current_selected_dot = self.find_element(*HomePageLocators.TOP_BANNER_SELECTED_DOT)
    # print(current_selected_dot.get_attribute("aria-label"))
    # current_selected_dot = self.find_element(*HomePageLocators.TOP_BANNER_SELECTED_DOT)
    # dot_to_check = self.find_element(*HomePageLocators.get_dot_top_banner_by_number(dot_number))
    # assert current_selected_dot.get_attribute("aria-label") == dot_to_check.get_attribute("aria-label"), \
    #     f"Error, Current selected dot should be equal to {dot_number}. " \
    #     f"Actual result: {current_selected_dot.get_attribute('aria-label')}"
    # print('Get dot info')
    # print(self.find_element(*HomePageLocators.get_dot_top_banner_by_number(dot_number)).get_attribute("aria-label"))
    # print('Get dot info - done')

    # print(self.CURRENT_ACTIVE_BANNER.text.lower())
    # print('Get category name')
    # print(self.CURRENT_ACTIVE_BANNER.find_element_by_css_selector('div.text-inner').text)
    #
    # print('a link')
    # print(self.CURRENT_ACTIVE_BANNER.find_element_by_css_selector('div.slider-wrapper.relative a + div').text)
    # print(self.CURRENT_ACTIVE_BANNER.find_element_by_css_selector(f'a[href*="{product_category}"]').get_attribute("href"))

    # assert category_name_from_link in self.CURRENT_ACTIVE_BANNER.text.lower(), \
    #     f"Error, Link to category and banner should contains the same info. " \
    #     f"Current link: {link_to_category.get_attribute('href')}" \
    #     f"Current banner: {self.CURRENT_ACTIVE_BANNER.text}"

    #
    # def check_product_title_on_sale(self):
    #     for product in self.get_products_on_sale():
    #         print(product.find_element_by_css_selector('img[src*="https"]').get_attribute("sizes"))
    #         print(product.find_element_by_css_selector('p.category.uppercase').text)
    #         print(product.find_element_by_css_selector('span.price').text)
    #         print(product.find_element_by_css_selector('p.name.product-title').text)
    #         print(product.find_element_by_css_selector('span.onsale').text)
    #         print(product.find_element_by_css_selector('div.star-rating').text)

    # def verify_product_mandatory_attributes(self, section_title: str):
    #     child = self.verify_titles_of_content_sections(section_title)
    #     following_sibling = child.find_element_by_xpath('following-sibling::div')
    #     print(following_sibling)
    #     print(following_sibling.get_attribute("class"))
    #     following_sibling.fint_elements()

    # def get_clothing_department_fashion_link_by_name(section_name):
    #     xpath = '//div[@id="nav-subnav"]/a[@class="nav-a nav-hasArrow"]/span[contains(text(), "{}")]'.format(
    #     section_name)
    #     return (By.XPATH, xpath)
    # def add_product_on_sale_to_wishlist_by_number(self, product_position: int):
    #     product_by_number = self.get_products_on_sale()[product_position-1]
    #     product_heart_icon = product_by_number.find_element(*WishlistLocators.get_wish_button())
    #     self.mouse_hover_action_webelement(product_by_number.find_element(*WishlistLocators.get_wish_button()))
    #     product_heart_icon.click()
    #     self.wait_for_element_appears(*WishlistLocators.WISHLIST_CONTENT_PRODUCT_ADDED_POP)
    #     print()
    #     product_heart_icon.click(product_by_number.find_element(*WishlistLocators.get_wish_button(is_added=True)))
    #     sleep(3)
