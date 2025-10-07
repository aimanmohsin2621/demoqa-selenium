import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from tests.utils.api_client import APIClient

class TestBookStoreE2E(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        service = Service(r"C:\Users\aiman\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.get("https://demoqa.com/books")
        cls.api = APIClient()

    def test_api_books(self):
        """Verify the Book Store API returns books."""
        data = self.api.get_books()
        self.assertIn("books", data)

    def test_page_title(self):
        """Verify the Books page title."""
        self.assertIn("DEMOQA", self.driver.title.upper())


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
