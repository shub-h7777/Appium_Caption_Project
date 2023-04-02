import pytest
from appium import webdriver


class AppiumConfig():
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {
            "deviceName": "Google Pixel 4",
            "platformName": "Android",
            "app": r"C:\Users\150286\Python BootCamp\components\Booking.apk",
            "noReset": True

        }

        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub",
                                       desired_capabilities=des_cap)
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()
