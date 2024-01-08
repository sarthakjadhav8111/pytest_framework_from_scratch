import pytest
import time
from selenium import webdriver
from pageObject.LoginPage import Login
from pageObject.AddCustomer import AddCustomer
from pageObject.SearchCustomer import SearchCustomer
from configurations.readProperties import ReadConfig
from utilities.customLogger import LogGen

class TestCustomerSearchByEmail_003:
    page_url = ReadConfig.get_aplication_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_search_customer_by_email(self, setup):
        self.logger.info("********search customer by email start********")
        self.driver = setup
        self.driver.get(self.page_url)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************login successfull**********")

        self.logger.info("**********customer search start*********")

        self.adc = AddCustomer(self.driver)
        self.adc.clickOnCustomerMenu()
        self.adc.clickOnCustomerMenuItem()

        search_customer = SearchCustomer(self.driver)
        # search_customer.setEmail("james_pan@nopCommerce.com")
        # calling set name method now
        search_customer.setFirstName("Victoria")
        search_customer.setLastName("Terces")

        search_customer.clickSearch()

        time.sleep(10)
        # status = search_customer.searchCustomerByEmail("james_pan@nopCommerce.com")
        status = search_customer.searchCustomerByName("Victoria Terces")

        assert True == status
        self.logger.info("*********Test Case Search by customer finished**********")

        self.driver.close()

