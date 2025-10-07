from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_open_demoqa():
    """Verify DemoQA website loads correctly"""
    service = Service(r"C:\Users\aiman\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://demoqa.com")

    # Wait until the page title contains "DEMOQA" (up to 10 seconds)
    WebDriverWait(driver, 10).until(lambda d: "DEMOQA" in d.title.upper())

    print("Page title:", driver.title)
    assert "DEMOQA" in driver.title.upper(), f"Expected 'DEMOQA' in title but got '{driver.title}'"

    driver.quit()

