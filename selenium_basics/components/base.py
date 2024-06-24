from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Base:
    BASE_VAR = "Base Var"
    # pass
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        # extract locator values, tuple of 2 strings
        by, value = locator
        # use  webdriver wait + EC element to be  clickable
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, value)))
        # click the element
        element.click()

