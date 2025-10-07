import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class TestPracticeForm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        service = Service(r"C:\Users\aiman\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.get("https://demoqa.com/automation-practice-form")

    def test_form_loads(self):
        header = self.driver.find_element(By.CLASS_NAME, "practice-form-wrapper")
        self.assertTrue(header.is_displayed())

    def test_submit_button_visible(self):
        button = self.driver.find_element(By.ID, "submit")
        self.assertTrue(button.is_enabled())

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
