import logging
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

#appium_server_url = 'http://127.0.0.1:4723/wd/hub'

@pytest.fixture(scope="function")
def setup_driver():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(message)s', '%Y-%m-%d %H:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info(":::Initializing Appium driver:::")
    appium_server_url = 'http://127.0.0.1:4723/wd'
    capabilities = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "platformVersion": "10",
    "deviceName": "emulator-5554",
    "appPackage": "com.breemobile",
    "appActivity": "com.breemobile.MainActivity",
    "noReset": False
    }

    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    yield driver, logger

    logger.info(":::Quitting Appium Driver:::")
    driver.terminate_app("com.breemobile")