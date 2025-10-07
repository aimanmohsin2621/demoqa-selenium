from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://demoqa.com/login"

    # Locators for elements on the login page
    USERNAME = (By.ID, "userName")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")

    def open_login_page(self):
        """Open the login page"""
        self.open(self.URL)

    def login(self, username, password):
        """Perform login action"""
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
