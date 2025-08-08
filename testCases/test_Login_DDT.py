import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageObjects.LoginPage import LoginPage
from utilities import xlutils
from utilities.readProperties import  readconfig
from utilities.customLogger import LogGen


class TestLoginDDT_002:

    baseurl = readconfig.getAppUrl()
    path = ".\\TestData\\TestData.xlsx"
    logger = LogGen.loggen()




    def test_login(self,setup):
        self.logger.info("Test login page with DDT---- This is my log statement")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)

        self.rows = xlutils.getRowCount(self.path, 'Sheet1')
        print("NO.of rows in Excel:", self.rows)

        lst_status = []
        for r in range(2, self.rows + 1):
            self.username = xlutils.readData(self.path, 'Sheet1', r, 1)
            self.password = xlutils.readData(self.path, 'Sheet1', r, 2)
            self.exp = xlutils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUsername(self.username)
            self.lp.setPassword(self.password)

            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title

            if "Dashboard / nopCommerce administration" or "Just a moment" in act_title:
                if self.exp == "Pass":
                    self.logger.info("Login test passed for username: " + self.username)
                    #self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("Login test failed for username: " + self.username)
                    #self.lp.clickLogout()
                    lst_status.append("Fail")
            elif "Dashboard / nopCommerce administration" or "Just a moment" not in act_title:
                if self.exp == "Pass":
                    self.logger.info("Login test failed for username: " + self.username)
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("Login test passed for username: " + self.username)
                    lst_status.append("Pass")


            if "Fail" not in lst_status:
                self.logger.info("Login test passed for all users")
                self.driver.save_screenshot(".\\Screenshots\\" + "testLoginDDT.png")
                assert True
                self.driver.close()
            else:
                self.logger.info("Login test failed for some users")
                self.driver.save_screenshot(".\\Screenshots\\" + "testLoginDDT_Fail.png")
                self.driver.close()
                assert False

        self.logger.info("Login DDT test passed for all users")





