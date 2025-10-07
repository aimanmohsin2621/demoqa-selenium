from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage

class FramesPage(BasePage):
    URL = "https://demoqa.com/frames"

    FRAME = (By.ID, "frame1")
    TEXT = (By.ID, "sampleHeading")

    def open_frames_page(self):
        """Open the Frames page"""
        self.open(self.URL)

    def get_frame_text(self):
        """Switch to frame and get its text"""
        frame = self.find(self.FRAME)
        self.driver.switch_to.frame(frame)
        text = self.find(self.TEXT).text
        self.driver.switch_to.default_content()
        return text
