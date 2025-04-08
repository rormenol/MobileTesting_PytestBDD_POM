from tests.pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class SetPasswordPage(BasePage):
    def __init__(self, driver, logger):
        super().__init__(driver, logger)
        self.locator_map = {
            "password_text" : (AppiumBy.XPATH, '(//android.widget.EditText[@text="@breepassword1"])[1]'),
            "confirm_password_text" : (AppiumBy.XPATH,'(//android.widget.EditText[@text="@breepassword1"])[2]'),
            "next_button": (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Next"]/android.view.ViewGroup'),
            "password_eye_icon": (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView[2]'),
            "confirmation_password_eye_icon": (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView[2]')

        }

    def enter_pasword(self, password):
        self.enter_text(self.locator_map['password_text'], password)
        pass

    def enter_confirmation_password(self, password):
        self.enter_text(self.locator_map['confirm_password_text'], password)
        pass

    def tap_next_button(self):
        self.tap_element(self.locator_map['next_button'])
        pass

    def tap_password_eye_icon(self):
        self.tap_element(self.locator_map['password_eye_icon'])
        pass

    def tap_confirmation_password_eye_icon(self):
        self.tap_element(self.locator_map['confirmation_password_eye_icon'])
        pass