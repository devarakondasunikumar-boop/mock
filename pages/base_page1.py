from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


## click and send_keys()

class Basepage:

    def __int__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.driver.find_element(*locator).click()
        ## self.wait.until(EC.visiablity_of_element_locator(locator)).click()

    def send_keys(self, locator, value):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(value)


