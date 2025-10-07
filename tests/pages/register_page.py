from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage

class RegisterPage(BasePage):
    URL = "https://demoqa.com/register"

    # Locators for the form fields
    FIRST_NAME = (By.ID, "firstname")
    LAST_NAME = (By.ID, "lastname")
    USERNAME = (By.ID, "userName")
    PASSWORD = (By.ID, "password")
    REGISTER_BUTTON = (By.ID, "register")

    def open_register_page(self):
        """Open the registration page"""
        self.open(self.URL)

    def register_user(self, first_name, last_name, username, password):
        """Fill out and submit the registration form"""
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.REGISTER_BUTTON)
