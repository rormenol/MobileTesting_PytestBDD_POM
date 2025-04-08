from tests.pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class SMSVerificationPage(BasePage):
    def __init__(self, driver, logger):
        super().__init__(driver, logger)
        self.locator_map ={
            'title':(AppiumBy.XPATH,'//android.widget.TextView[@text="SMS verification"]')
        }

    def is_title_visible(self):
        """returns true if the page title is visible"""
        return self.is_element_visible(self.locator_map['title'])