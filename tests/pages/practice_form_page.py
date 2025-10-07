from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage

class PracticeFormPage(BasePage):
    URL = "https://demoqa.com/automation-practice-form"

    # Locators
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    GENDER = (By.CSS_SELECTOR, "label[for='gender-radio-1']")
    MOBILE = (By.ID, "userNumber")
    SUBMIT_BUTTON = (By.ID, "submit")

    def open_practice_form(self):
        """Open the Practice Form page"""
        self.open(self.URL)

    def fill_form(self, first, last, email, mobile):
        """Fill in the basic form fields"""
        self.type(self.FIRST_NAME, first)
        self.type(self.LAST_NAME, last)
        self.type(self.EMAIL, email)
        self.click(self.GENDER)
        self.type(self.MOBILE, mobile)

    def submit_form(self):
        """Submit the form"""
        self.click(self.SUBMIT_BUTTON)
