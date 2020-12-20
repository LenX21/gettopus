from selenium.webdriver import ActionChains
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.driver.wait = WebDriverWait(self.driver, 15)

    @staticmethod
    def _wrap_elements(result):
        # handle the case if EventFiringWebElement instead of WebElement
        if isinstance(result, EventFiringWebElement):
            return result.wrapped_element
        return result

    def get_title(self):
        return self.driver.title

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def open_page(self, url: str):
        self.driver.get(url)

    def input_text(self, text: str, *locator):
        self.driver.find_element(*locator).send_keys(text)

    # Update with new method with FiringEvent verification
    # def find_element(self, *locator):
    #     """
    #     :param locator: Search strategy and locator of webelement (ex. (By.ID, 'id'))
    #     :return:
    #     """
    #     return self.driver.find_element(*locator)
    def find_element(self, *locator):
        webelement = self.driver.find_element(*locator)
        return self._wrap_elements(webelement)

    def find_elements(self, *locator):
        """
        :param locator: Search strategy and locator of the group webelements (ex. (By.ID, 'id'))
        :return: group of elements
        """
        return self.driver.find_elements(*locator)

    def verify_expected_text(self, expected_text: str, *locator):
        """
        Search for a webelement, get its text, compare with expected_text
        :param expected_text: Text to be in webelement
        :param locator: Search strategy and locator of webelement (ex. (By.ID, 'id'))
        """
        result = self.driver.find_element(*locator)
        assert result.text.strip(
            '"') == expected_text, f'Error. Expected result:{expected_text}, got result: {result.text}'

    def verify_page_title(self, expected_text: str):
        """
        :param expected_text: Title of the page that we expected to see
        :return:
        """
        page_title = self.driver.title
        assert page_title == expected_text, f"Error. Expected page title: {expected_text}, got title {page_title}"

    def wait_for_element_appears(self, *locator):
        self.driver.wait.until(ec.visibility_of_element_located(locator))

    def wait_for_element_disappears(self, *locator):
        self.driver.wait.until(ec.invisibility_of_element_located(locator))

    def wait_element_is_clickable(self, *locator):
        self.driver.wait.until(ec.element_to_be_clickable(locator))

    def wait_title_contains(self, title_text):
        self.driver.wait.until(ec.title_contains(title_text))

    def wait_for_url_matches(self, url):
        self.driver.wait.until(ec.url_matches(url))

    def wait_new_window(self):
        self.driver.wait.until(ec.new_window_is_opened)
        # WebDriverWait(context.driver, 5).until(ec.new_window_is_opened)

    def open_link_in_new_tab(self, url: str):
        self.driver.execute_script(f"window.open('{url}')")
        self.driver.wait.until(ec.new_window_is_opened)

    def get_all_open_windows(self):
        return self.driver.window_handles

    def get_current_open_window(self):
        return self.driver.current_window_handle

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.get_all_open_windows()[1])

    def switch_to_first_window(self, close_current_window=False):
        if close_current_window:
            self.close_current_window()
        self.driver.switch_to.window(self.get_all_open_windows()[0])

    def close_current_window(self):
        self.driver.close()

    def mouse_hover_action(self, *locator):
        """
        Hover mouse over a webelement
        :param locator: Search strategy and locator of webelements (ex. (By.ID, 'id'))
        """
        self.wait_for_element_appears(*locator)
        ActionChains(self.driver).move_to_element(self.find_element(*locator)).perform()



