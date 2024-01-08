import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class SearchCustomer:
    
    text_email_search_id = "SearchEmail"
    text_fname_search_id = "SearchFirstName"
    text_lname_search_id = "SearchLastName"
    btn_search_xpath = "//button[@id='search-customers']"

    tbl_search_result_xpath = "//table[@id='grid']"
    table_xpath = "table[@id='customers-grid']"
    table_row_xpath = "//table[@id='customers-grid']//tbody/tr"
    table_column_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    
    def setEmail(self, email):
        self.driver.find_element(By.ID, self.text_email_search_id).clear()
        self.driver.find_element(By.ID, self.text_email_search_id).send_keys(email)

    def setFirstName(self, fname):
        self.driver.find_element(By.ID, self.text_fname_search_id).clear()
        self.driver.find_element(By.ID, self.text_fname_search_id).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.ID, self.text_lname_search_id).clear()
        self.driver.find_element(By.ID, self.text_lname_search_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.XPATH, self.btn_search_xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.table_row_xpath))
    
    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.table_column_xpath))
    
    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
            return flag
        
    def searchCustomerByName(self, name):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            Name = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if Name == name:
                flag = True
                break
            return flag





