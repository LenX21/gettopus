from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from app.application import Application
from app.config import EnvironmentData
from app.logger import MyListener, logger


def browser_init(context):
    chromedriver = EnvironmentData.CHROME_EXECUTABLE_PATH
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    context.driver = EventFiringWebDriver(webdriver.Chrome(chromedriver, chrome_options=chrome_options), MyListener())

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)
    logger.info(f'\nStarted step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        logger.info(f'\nStep failed:{step}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()