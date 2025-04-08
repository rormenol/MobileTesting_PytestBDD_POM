from tests.pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class CheckEmailPage(BasePage):
    def __init__(self, driver, logger):
        super().__init__(driver, logger)
        self.locator_map ={
            'gotostore_button': (AppiumBy.XPATH, '//android.widget.TextView[@text="Go to store"]'),
            'emailaddress_text': (AppiumBy.XPATH,'//android.widget.EditText[@text="john@trybree.com"]'),
            'next_button': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Next"]/android.view.ViewGroup'),
            'invalid_email_message': (AppiumBy.XPATH,'//android.widget.TextView[@text="Invalid email address"]'),
            'miss_you_message': (AppiumBy.XPATH,'//android.widget.TextView[@text="We missed you!"]')

        }

    def tap_go_to_store_button(self):
        if self.is_element_visible(self.locator_map['gotostore_button'], 5):
            self.logger.info(":::Pop up to update app is active. Tapping Go to store button")
            self.tap_element(self.locator_map['gotostore_button'])
        else:
            self.logger.info(":::Pop up to update app is not active. Doing nothing")
    
    def enter_email(self, email):
        self.tap_go_to_store_button()
        self.enter_text(self.locator_map['emailaddress_text'], email)

    def tap_next_button(self):
        self.tap_element(self.locator_map['next_button']) 

    def is_email_invalid(self):
        return self.is_element_visible(self.locator_map['invalid_email_message'])

    def is_miss_you_message_visible(self):
        return self.is_element_visible(self.locator_map['miss_you_message'])