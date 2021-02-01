from behave import step
from nose.tools import *
from Pages.Locators import HomePageLocator as HP
from QA import qa


@step('Launch the Flipkart website (.*)')
def launch_flipkart(context,website):
    context.driver = qa.create_webdriver_instance()
    context.return_url = qa.launch_website(website)

    assert_true(context.return_url == website, msg="The website we are getting is wrong {}".format(context.return_url))


@step('Verify the Flipkart logo on the homepage')
def verify_logo(context):
    context.get_title = HP.Locators.title_locator()

    assert_equal(context.get_title,"Flipkart", msg="Redirected to this {} wrong URL".format(context.get_title))


@step('Verify the visibility of search text field')
def verify_visiblity(context):
    context.get_search = HP.Locators.name_locator('q')
    assert_true(context.get_search.is_displayed(),msg="Search box is not being displayed")


@step('Enter the value in search box (.*)')
def enter_search(context, value):
    context.enter_value = HP.Locators.name_locator('q')
    context.enter_value.send_keys(value)


@step('Verify the name of the mobile (.*)')
def product_name(context,mobile_name):
    context.m_name = HP.Locators.xpath_locator("//div[contains(text(),'POCO M2 (Slate Blue, 64 GB)')]")
    assert_true(context.m_name.text,mobile_name, msg ="Maybe mobile is not available, please search")


@step('Close the browser')
def close_browser(context):
    context.close = qa.close_browser()
