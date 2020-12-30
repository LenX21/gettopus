from pages.base_page import Page
from locators.locators import LoginFormLocators


class LoginForm(Page):
    def verify_login_window_is_shown(self):
        self.wait_for_element_appears(*LoginFormLocators.LOGIN_FORM)