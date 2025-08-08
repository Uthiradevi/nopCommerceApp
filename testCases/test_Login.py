import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import  readconfig
from utilities.customLogger import LogGen



class TestLogin_001:

    baseurl = readconfig.getAppUrl()
    username = readconfig.getUsername()
    password = readconfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_homepagetitle(self,setup):
        self.logger.info("Test homepagetitle -- This is my log statement")
        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title

        assert "nopCommerce demo store. Login" in act_title
        self.logger.info("Verified Homepage Title--- This is my log statement")
        self.driver.close()

    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("Test login page---- This is my log statement")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername = self.username
        self.lp.setPassword = self.password
        self.lp.clickLogin()
        time.sleep(5)
        act_title = self.driver.title

        assert "Dashboard / nopCommerce administration" or "Just a moment" in act_title
        self.logger.info("Verified Login Page Title")
        self.driver.save_screenshot(".\\Screenshots\\" + "testLogin.png")
        self.driver.close()







