import pytest
from selenium import webdriver
from pageObject.LoginPage import Login
from configurations.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    page_url = ReadConfig.get_aplication_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    logger = LogGen.loggen()

    # adding markers
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_page_title(self, setup):

        self.logger.info("********** Test_001_Login **********")
        self.logger.info("********** Verifying login Page title **********")

        self.driver = setup
        self.driver.get(self.page_url)
        actual_title = self.driver.title

        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********** login Page title test case passed **********")
        
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_login_page_title.png")
            self.driver.close()
            self.logger.error("********** login Page title test case failed **********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):

        self.logger.info("********** Test_001_Login **********")
        self.logger.info("********** Verifying Home Page title **********")

        self.driver = setup
        self.driver.get(self.page_url)

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        title_after_login = self.driver.title

        if title_after_login=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("********** Home Page title test case passed **********")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("********** Home Page title test case failed **********")
            assert False








