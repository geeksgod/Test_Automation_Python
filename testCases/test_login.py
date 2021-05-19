import time

import allure
import pytest
from allure_commons.types import AttachmentType

from pageObjects.LoginPage import LoginPage
from testCases.conftest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import excelUtils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.severity(allure.severity_level.CRITICAL)
class Test0001:
    baseUrl = ReadConfig.get_application_url()
    username = ReadConfig.get_user_name()
    password = ReadConfig.get_user_password()
    logger = LogGen.log_gen()
    driver = None

    def test_correct_login_info(self, setup):
        self.logger.info("logging test with correct info")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        lp = LoginPage(self.driver)
        lp.set_username(self.username)
        lp.set_password(self.password)
        lp.click_loginbutton()
        url = self.driver.current_url
        if "dashboard" in url.lower():
            assert True
        else:
            assert False

        self.driver.close()

    def test_blank(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        lp = LoginPage(self.driver)
        lp.click_loginbutton()
        time.sleep(2)
        try:
            errors = self.driver.find_elements_by_xpath('//span[@class="msg-error"]')
            for error in errors:
                if error.is_displayed():
                    print(error.text)
                    self.logger.info("test_blank faile due to error" + error.text)
                else:
                    print('cant read the text')
        except:
            print("wrong")

        self.driver.quit()

    def test_excel_incorrect_email(self, setup):
        row_count = excelUtils.getRowCount("./testData/loginTestData.xlsx", 'Sheet1')
        username = excelUtils.readData("./testData/loginTestData.xlsx", 'Sheet1', 2, 1)
        password = excelUtils.readData("./testData/loginTestData.xlsx", 'Sheet1', 2, 2)
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        lp = LoginPage(self.driver)
        lp.set_username(username)
        lp.set_password(password)
        lp.click_loginbutton()
        try:
            errors = self.driver.find_elements_by_xpath('//span[@class="msg-error"]')
            for error in errors:
                if error.is_displayed():
                    print(error.text)
                    self.logger.info("incorrect email faile due to error" + error.text)
                else:
                    print('cant read the text')
        except:
            print("No")

        self.driver.close()
        print(username, password)

    def test_excel_incorrect_pass(self, setup):
        row_count = excelUtils.getRowCount("./testData/loginTestData.xlsx", 'Sheet1')
        username = excelUtils.readData("./testData/loginTestData.xlsx", 'Sheet1', 3, 1)
        password = excelUtils.readData("./testData/loginTestData.xlsx", 'Sheet1', 3, 2)
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        lp = LoginPage(self.driver)
        lp.set_username(username)
        lp.set_password(password)
        lp.click_loginbutton()
        try:
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/button')
            assert False
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="test information creation",
                          attachment_type=AttachmentType.PNG)
            assert True



        self.driver.close()
        print(username, password)
