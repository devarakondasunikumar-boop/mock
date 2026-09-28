from selenium.webdriver.common.by import By
from mock1.pages.login import Loginpage


class LoginPage(BasePage):
    From = (By.XPATH,'//input[@placeholder="From"]')
    To = (By.XPATH,'//input[@placeholder="To"]')
    search = (By.XPATH,'//button[contains((text)."search")]')

    def enter_from(self,city):
        self.send_keys(self.From,city)

    def enter_to(self,city):
        self.send_keys(self.To,city)

    def search(self):
        self.click(self.search)



