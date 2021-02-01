from QA import qa
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Locators:

    def __init__(self):
        self.driver = qa.create_webdriver_instance()

    def id_locator(self, id_name):
        WebDriverWait(self.driver, 20).until((EC.presence_of_element_located(id_name)))
        return self.driver.find_element(id_name)

    def name_locator(self,name):
        WebDriverWait(self.driver, 20).until((EC.presence_of_element_located(name)))
        return self.driver.find_element_by_class_name(name)

    def class_locator(self, class_name):
        WebDriverWait(self.driver, 20).until((EC.presence_of_element_located(class_name)))
        return self.driver.find_element(class_name)

    def xpath_locator(self, xpath):
        WebDriverWait(self.driver, 20).until((EC.presence_of_element_located(xpath)))
        return self.driver.find_element(xpath)

    def title_locator(self):
        WebDriverWait(self.driver, 20).until((EC.title_is("Flipkart")))
        return self.driver.title
