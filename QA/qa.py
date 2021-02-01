import logging as log
import os
from data.config import settings
from Pages.Locators import HomePageLocator as HP

from selenium import webdriver
from selenium.common import exceptions as selenium_exception
from selenium.webdriver.firefox.options import Options as firefox_options
from selenium.webdriver.firefox.options import Options as chrome_options
from selenium.webdriver.firefox.options import Options as selenium_options


def create_instance(context):
    try:
        context.browser = str(settings['browser']).lower()
        if context.browser == "firefox":
            options = firefox_options
            options.headless = True
            browser_options = selenium_options()
            capabilities = webdriver.DesiredCapabilities().FIREFOX
            capabilities["marionette"] = True
            driver = webdriver.Firefox(options=browser_options, capabilities=capabilities,
                                       executable_path="Resource/geckodriver.exe")

        elif context.browser == "chrome":
            options = chrome_options
            options.headless = True
            browser_options = selenium_options()
            capabilities = webdriver.DesiredCapabilities().CHROME
            capabilities["marionette"] = True
            driver = webdriver.Chrome(options=browser_options, capabilities=capabilities,
                                      executable_path="Resource/chromedriver.exe")
        else:
            log.error(msg="There are two web browser options are available i.e. chrome and firefox")

    except selenium_exception:
        raise
    return driver


def create_webdriver_instance(context):
    context.browser = str(settings['browser']).lower()
    if context.browser == "firefox":
        driver = webdriver.Firefox("Resource/geckodriver.exe")
        return driver


def launch_website(context, url):
    log.info(url)
    isinstance(context.driver,create_webdriver_instance)
    context.driver.get(url)


def close_browser(context):
    isinstance(context.driver,create_webdriver_instance)
    context.driver.close()