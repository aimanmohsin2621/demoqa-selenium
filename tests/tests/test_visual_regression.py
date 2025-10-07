import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from tests.utils.visual_diff import compare_images
import os

class TestVisualRegression(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        service = Service(r"C:\Users\aiman\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.get("https://demoqa.com")

    def test_screenshot_compare(self):
        cls = self.__class__
        cls.driver.save_screenshot("artifacts/current_home.png")
        base_img = "artifacts/base_home.png"
        current_img = "artifacts/current_home.png"

        # If base image doesn't exist, create it first time
        if not os.path.exists(base_img):
            print("⚙️ Base image not found. Saving current as base reference.")
            os.rename(current_img, base_img)
            assert True
            return

        # Try comparing the two images
        try:
            match = compare_images(base_img, current_img)
            assert match, "❌ Page visuals have changed!"
        except Exception as e:
            print("⚠️ Visual comparison failed:", e)
            assert False

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
