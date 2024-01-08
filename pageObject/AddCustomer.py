import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class AddCustomer:
    # Writing x path for each web element
    link_customer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    link_customer_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btn_addnew_xpath = "//a[@href='/Admin/Customer/Create']"

    text_email_xpath = "//input[@id='Email']"
    text_password_xpath = "//input[@id='Password']"
    text_fname_xpath = "//input[@id='FirstName']"
    text_lname_xpath = "//input[@id='LastName']"
    rdbm_gender_xpath = "//input[@id='Gender_Male']"
    rdbf_gender_xpath = "//input[@id='Gender_Female']"
    text_date_xpath = "//input[@id='DateOfBirth']"
    text_company_xpath = "//input[@id='Company']"
    drpdn_customer_role_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitem_administrator_xpath = "//li[contains(text(),'Administrators')]"
    lstitem_registered_xpath = "//li[contains(text(),'Registered')]"
    lstitem_guests_xpath = "//li[contains(text(),'Guests')]"
    lstitem_vendors_xpath = "//li[contains(text(),'Vendors')]"
    drpdn_vendor_xpath = "///*[@id='VendorId]"
    text_admin_area_xpath = "//textarea[@id='AdminComment']"
    btn_save_xpath = "//button[@name='save']"
    
    # initializing driver 
    def __init__(self, driver):
        self.driver = driver

    # functions for individual driver element
    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.link_customer_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.link_customer_menuitem_xpath).click()

    def clickAddNewCustomer(self):
        self.driver.find_element(By.XPATH, self.btn_addnew_xpath).click()

    def addEmail(self, email):
        self.driver.find_element(By.XPATH, self.text_email_xpath).send_keys(email)

    def addPassword(self, password):
        self.driver.find_element(By.XPATH, self.text_password_xpath).send_keys(password)

    def addFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.text_fname_xpath).send_keys(fname)

    def addLastName(self, lname):
        self.driver.find_element(By.XPATH, self.text_lname_xpath).send_keys(lname)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH, self.rdbm_gender_xpath).click()
        elif gender == "Female":
            self.driver.find_element(By.XPATH, self.rdbf_gender_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rdbm_gender_xpath).click()

    def setDOB(self, dob):
        self.driver.find_element(By.XPATH, self.text_date_xpath).send_keys(dob)
    
    def setCompanyName(self, company):
        self.driver.find_element(By.XPATH, self.text_company_xpath).send_keys(company)
  
    def setCustomerRole(self, role):
        self.driver.find_element(By.XPATH, self.drpdn_customer_role_xpath).click()
        time.sleep(3)
        if role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_registered_xpath)
        
        if role == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_administrator_xpath)
        
        elif role == "Guests":
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//ul[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_guests_xpath)

        elif role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_registered_xpath)
       
        elif role == "Vendors":
            self.listitem=self.driver.find_element(By.XPATH, self.lstitem_vendors_xpath)

        else:
            self.listitem=self.driver.find_element(By.XPATH, self.lstitem_guests_xpath)
        time.sleep(3)

        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setVendor(self, value):
        vendor = self.driver.find_element(By.XPATH, self.drpdn_vendor_xpath).click()
        vendor_data = Select(vendor)
        vendor_data.select_by_visible_text(value)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.text_admin_area_xpath).send_keys(content)

    def clickSave(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()
        
    






