from tests.pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class InitialPage(BasePage):

    def __init__(self, driver, logger):
        super().__init__(driver, logger)
        self.locator_map ={
            'signup_button': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Sign up"]/android.view.ViewGroup'),
            'login_button': (AppiumBy.XPATH,'//android.widget.TextView[@text="Log in"]'),
            'gotostore_button': (AppiumBy.XPATH, '//android.widget.TextView[@text="Go to store"]'),
        }

    def tap_login_button(self):
        self.logger.info(":::Tapping Login button")
        self.tap_element(self.locator_map['login_button'])

    def tap_signup_button(self):
        self.tap_go_to_store_button()
        self.logger.info(":::Tapping SignUp button")
        self.tap_element(self.locator_map['signup_button'])
    
    def tap_go_to_store_button(self):
        if self.is_element_visible(self.locator_map['gotostore_button'], 5):
            self.logger.info(":::Pop up to update app is active. Tapping Go to store button")
            self.tap_element(self.locator_map['gotostore_button'])
        else:
            self.logger.info(":::Pop up to update app is not active. Doing nothing")
    
        