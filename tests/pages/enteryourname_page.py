from tests.pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait

class EnterYourNamePage(BasePage):
    def __init__(self, driver, logger):
        super().__init__(driver, logger)
        self.locator_map = {
            'first_name_text': (AppiumBy.XPATH,'//android.widget.EditText[@text="John"]'),
            'last_name_text': (AppiumBy.XPATH,'//android.widget.EditText[@text="Smith"]'),
            'dateofbirth_text': (AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="Date of birth, MM/DD/YYYY"]'),
            'next_button': (AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="Next"]/android.view.ViewGroup'),
            'date_picker':(AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="com.breemobile:id/pickerWrapper"]'),
            'date_cancel_button':(AppiumBy.XPATH,'//android.widget.Button[@resource-id="android:id/button2"]'),
            'date_confirm_button':(AppiumBy.XPATH,'//android.widget.Button[@resource-id="android:id/button1"]')
        }
        self.month_location = {}
        self.day_location = {}
        self.year_location = {}
        self.pixels_to_add_one = 220

    def enter_first_name_text(self, firstname):
        self.enter_text(self.locator_map['first_name_text'], firstname)
        pass

    def enter_last_name_text(self, lastname):
        self.enter_text(self.locator_map['last_name_text'], lastname)
        pass

    def enter_date_of_birth(self, dateofbirth):
        self.tap_element(self.locator_map['dateofbirth_text'])
        date_element = self.get_element(self.locator_map['date_picker'])
        location = date_element.location

        self.month_location['x'] = location['x'] + 461
        self.month_location['y'] = location['y'] + 325
        self.day_location['x'] = location['x'] + 706
        self.day_location['y'] = location['y'] + 325
        self.year_location['x'] = location['x'] + 884
        self.year_location['y'] = location['y'] + 325
        self.logger.info(f"::The location of date_element is {location}")
        split_date = dateofbirth.split('/')
        month = int(split_date[0])
        day = int(split_date[1])
        year = int(split_date[2])
        self.change_new_date(month, day, year)

        self.tap_element(self.locator_map['date_confirm_button'])
        
        pass

    def change_new_date(self, month: int, day: int, year: int):
        """Internal function to change the date"""
        self.change_month(month)
        self.change_day(day)
        self.change_year(year)

    def change_month(self, new_month):
        #getting the month position
        x = self.month_location['x']
        y = self.month_location['y']
            
        #if value less than 7 or equal
        if new_month <= 7:
            #swipe y by -200 per (month-1)
            for _ in range(new_month-1):
                self.swipe(x,y,x,y-200)
        #else (if value greater than 7)
        else:
            #swipe y by +200 per 12-(month-1)
            for _ in range(12-(new_month-1)):
                self.swipe(x,y,x,y+200)

    def change_day(self, new_day: int):
        #getting the day position
        x = self.day_location['x']
        y = self.day_location['y']
            
        #if value less than 16 or equal
        if new_day <= 16:
            #swipe y by -200 per (day-1)
            for _ in range(new_day-1):
                self.swipe(x,y,x,y-200)
        #else (if value greater than 7)
        else:
            #swipe y by +200 per 12-(day-1)
            for _ in range(31-(new_day-1)):
                self.swipe(x,y,x,y+200)

    def change_year(self, new_year: int):
        #getting the year position
        x = self.year_location['x']
        y = self.year_location['y']
            
        #if value less than 1990 or equal
        if new_year >= 1990:
            #swipe y by -200 per (year-1)
            for _ in range(new_year-1990):
                self.swipe(x,y,x,y-200)
        #else (if value greater than 7)
        else:
            #swipe y by +200 per 1990 - new_year
            for _ in range(1990-new_year):
                self.swipe(x,y,x,y+200)

    def tap_next_button(self):
        self.tap_element(self.locator_map['next_button'])
        pass

    
