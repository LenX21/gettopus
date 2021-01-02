from pages.cart_page import CartPage
from pages.footer_menu import FooterMenu
from pages.home_page import HomePage
from pages.login_form import LoginForm
from pages.product_category_page import ProductCategoryPage
from pages.product_page import ProductPage
from pages.quick_view import QuickView
from pages.top_menu_page import TopMenuPage
from pages.wishlist_page import WishlistPage




class Application:

    def __init__(self, driver):
        self.driver = driver

        self.home_page = HomePage(self.driver)
        self.wishlist_page = WishlistPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.product_category_page = ProductCategoryPage(self.driver)
        self.top_menu = TopMenuPage(self.driver)
        self.login_form = LoginForm(self.driver)
        self.cart_page = CartPage(self.driver)
        self.footer_menu = FooterMenu(self.driver)
        self.quick_view = QuickView(self.driver)

