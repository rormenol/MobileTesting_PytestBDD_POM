import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
    
    def tap_element(self, locator, timeout = 10):
        """Clicks on an element located by a locator"""
        try:
            self.logger.info(f":::::Before searching the element {locator}")
            element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            self.logger.info(f":::::Element found and then executing the tap {locator}")
            element.click()
            
        except TimeoutException:
            self.logger.info(f'e--tap_element - Element cannot be found {locator}')
            pytest.fail(f"e--Element cannot be found {locator}")
    
    def enter_text(self, locator, text, timeout = 10):
        """Activates the input element and send the text"""
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            element.click()
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            self.logger.info('e--enter_text - Element cannot be found')
            pytest.fail(f"e--Element cannot be found {locator}")
    
    def get_element_text(self, locator, timeout = 15):
        """Get the text of the element"""
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return element.text
        except TimeoutException:
            self.logger.info('e--get_element_text - Element cannot be found')
            return None

    def swipe(self, start_x, start_y, end_x, end_y, duration = 500):
        """Performs a swipe action"""
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def is_element_visible(self, locator, timeout = 10):
        """search the element and returns True if it is found"""
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            self.logger.info(f'e--Is visible? - Element cannot be found {locator}')
            return False
    
    def get_element_content_desc(self, locator, timeout = 10):
        #element = self.driver.find_element(locator)
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return element.get_attribute("content-desc")
        
        except TimeoutException:
            self.logger.info('e--get_element_text - Element cannot be found')
            return None
        
    def get_element(self, locator, timeout = 10):
        """return an element searched by a locator"""
        try:
            self.logger.info(f":::::Before searching the element {locator}")
            element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            self.logger.info(f":::::Element found and then returning the element {locator}")
            return element
            
        except TimeoutException:
            self.logger.info(f'e--get_element - Element cannot be found {locator}')
            pytest.fail(f"e--Element cannot be found {locator}")
            return None
    
        



    