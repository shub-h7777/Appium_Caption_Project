import time
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait

from Base.webdriver import AppiumConfig


class TestBookingApp(AppiumConfig):

    def test_booking(self):
        action = TouchAction(self.driver)

        self.driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="Flights"]').click()
        time.sleep(2) #it is necessary due to pre airport selected is random.
        action.tap(x=493, y=690).perform()

        #click on Pre selected airport and remove it
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'UiSelector().descriptionContains("Remove")').click()


        #enter the airport name
        self.driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@text="Airport or city"]').send_keys("AM")
        self.driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="AMD Sardar Vallabhbhai Patel International Airport"]').click()
        self.driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Where to?"]').click()
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Airport or city"]').send_keys("DX")
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'UiSelector().textContains("DXB ")').click()

        #click on "Direct flights only" and click on search
        action.tap(x=983, y=1445).perform()
        action.tap(x=545, y=1300).perform()
        time.sleep(10)
        print(self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'UiSelector().textContains("results")').text)
