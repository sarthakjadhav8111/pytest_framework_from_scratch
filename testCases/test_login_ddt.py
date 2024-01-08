import pytest
import time
from selenium import webdriver
from pageObject.LoginPage import Login
from configurations.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import excel_util


class Test_001_DDT_Login:
    page_url = ReadConfig.get_aplication_url()
    path = ".//testData//LoginData.xlsx"
    logger = LogGen.loggen()

    def test_login_ddt(self, setup):

        self.logger.info("********** Test_001_DDT_Login **********")
        self.logger.info("********** Verifying Home Page title **********")

        self.driver = setup
        self.driver.get(self.page_url)

        self.lp = Login(self.driver)

        self.rows = excel_util.getRowCount(self.path, "Sheet1")
        
        lst_status = [] 
        for row in range(2,self.rows+1):
            self.user = excel_util.readData(self.path, "Sheet1", row, 1)
            self.password = excel_util.readData(self.path, "Sheet1", row, 2)
            self.exp = excel_util.readData(self.path, "Sheet1", row, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            title_after_login = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if title_after_login == exp_title:
                if self.exp=="Pass":
                    self.logger.info("**********Test Passes ************")
                    self.lp.clickLogout()
                    lst_status.append("Pass")

                elif self.exp=="Fail":
                    self.logger.info("**********Test Failed ************")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
                
            elif title_after_login != exp_title:
                if self.exp=="Pass":
                    self.logger.info("**********Test Failed ************")
                    lst_status.append("Fail")

                elif self.exp=="Fail":
                    self.logger.info("**********Test Passed ************")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("******** Login DDT Test Passed ********")
            self.driver.close()
            assert True
        else:
            self.logger.info("******* Login DDt Test Failed ********")
            self.driver.close()
            assert False

        self.logger.info("******* End of Login DDt Test ********")
        self.logger.info("******* Completed ********")

    
            








