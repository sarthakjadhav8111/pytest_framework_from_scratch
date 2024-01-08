import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObject.LoginPage import Login
from pageObject.AddCustomer import AddCustomer
from configurations.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import excel_util
import string
import random

class Test_002_AddCustomer:
    page_url = ReadConfig.get_aplication_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def testAddCustomer(self, setup):
        self.logger.info("*********Test_003_AddCustomer_Start************")
        self.driver = setup
        self.driver.get(self.page_url)
        self.driver.maximize_window()

        # First need to login on website

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*********login success*******")

        # after login clicking on customer--> Customer--> Add User

        self.logger.info("*******Started Adding Customer *********")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.addcust.clickAddNewCustomer()

        # start filling form
        # here we need to pass data one by one but if we hardcode values then my test case will work only
        # once and it will not execute from next iteration so we need to pass values dynamically

        self.logger.info("***********starting adding customer info*********")
        self.email = random_generator()+"@gamil.com"
        self.addcust.addEmail(self.email)
        self.addcust.addPassword("test@123")
        self.addcust.addFirstName("xyz")
        self.addcust.addLastName("abc")
        self.addcust.setGender("Male")
        self.addcust.setDOB("01/01/2024")
        self.addcust.setCompanyName("abc")
        time.sleep(3)
        self.addcust.setCustomerRole("Guests")
        time.sleep(50)
        self.addcust.setVendor("Vendor 1")
        self.addcust.setAdminContent("This is for testing......")
        self.addcust.clickSave()

        self.logger.info("*********Customer validation started*********")
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********** Add Customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\screenshots\\"+ "test_addCustomer_scr.png")
            self.logger.error("******add customer test failed ***********")
            assert False

        self.driver.close()
        self.logger.info("*******Test_003_AddCustomer_End********")

# Write random method to generate values randomly each time

def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
        return ''.join(random.choice(chars) for i in range(size))


# def test(size=8):
#     chars=string.ascii_lowercase+string.digits
#     for i in range(size):
#          return ''.join(random.choice(chars))
     


