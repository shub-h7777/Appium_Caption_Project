import pytest
from appium import webdriver
from Utilities import read_utils


class AppiumConfig():
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        json_dic = read_utils.get_dic_from_json("../Test_data/config.json")

        if json_dic["device"] == "local":
            des_cap = {
                "deviceName": "Google Pixel 4",
                "platformName": "Android",
                "app": r"C:\Users\150286\Python BootCamp\components\Booking.apk",
                "noReset": True

            }
            self.driver = webdriver.Remote(command_executor=f"http://localhost:{json_dic['port']}/wd/hub",
                                           desired_capabilities=des_cap)
        else:
            des_cap = {
                "app": "bs://73ea1396f0b902044773b994824f440727f77f9c",
                "platformVersion": "9.0",
                "deviceName": "Google Pixel 3",
                "bstack:options": {
                    "projectName": "First Behave Android Project",
                    "buildName": "browserstack-build-1",
                    "sessionName": "BStack first_test",
                    # Set your access credentials
                    "userName": "shubham_vMsZey",
                    "accessKey": "PfytQFzr4F2xnm99CQfK"
                }
            }

        self.driver = webdriver.Remote(command_executor="http://hub.browserstack.com/wd/hub",
                                       desired_capabilities=des_cap)
        self.driver.implicitly_wait(15)
        yield
        self.driver.quit()
