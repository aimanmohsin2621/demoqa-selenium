from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage

class AlertsPage(BasePage):
    URL = "https://demoqa.com/alerts"

    ALERT_BUTTON = (By.ID, "alertButton")

    def open_alerts_page(self):
        """Open the Alerts page"""
        self.open(self.URL)

    def trigger_alert(self):
        """Click the button to trigger alert"""
        self.click(self.ALERT_BUTTON)
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        return text
