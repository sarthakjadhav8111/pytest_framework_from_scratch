Selenium Hybrid Framework

Application Used: 
--front end:  https://demo.nopcommerce.com/
--back end:   https://admin-demo.nopcommerce.com

Step-1:
-- Create New Project & Install Required Packages/Plugins
* Selenium
* pytest
* pytest-html= pytest html reports
* pytest-xdist= run tests parallel
* Openpyxl
* Allure-pytest= to generate reports

Step-2:
--Create folder structure

Step-3:
-- Automating Login Test cases
    -Create LoginPage Object Class Under pageObjects
    -CreatenLoginTest Under testCases
    - Create conftest.py under testCases

Step-4:
-- Capture screenshots of failure test cases

Step-5:
-- Read common values from config.ini file from configurations folder

Step-6:
--Adding logs to test cases
  - add custom logs to logger.py under utilities Packages
  - add logs to login test case

Step-7:
-- Run test cases on desired browser
  - update conftest.py with required fixtires
  - pass browser name as argument in command line 
  -- Commands-->
    - pytest -s -v testCases/test_login.py --browser chrome
    - pytest -s -v testCases/test_login.py --browser edge

Step-7:(optional)-- to run test cases parallel(n=2 means i have 2 testcases)
  --    - pytest -s -v -n=2 testCases/test_login.py --browser chrome

Step-8:
-- Generate html reports
  - to generate report update conftest.py with pytest hooks
  - to generate html report run below command

  command:-  
      pytest -s -v -n=2 --html=reports\report.html testCases/test_login.py --browser chrome 

Step-9:
-- Automating data driven test cases
  - prepare test data in excel sheet, place the excel file inside test data folder
  - create excelutil.py under utilities Package
  - create LoginDataDrivenTest under testCases
  - run the test case 

Step-10:
--Adding new test cases
  - add new customer
  - search customer by email
  - search customer by name

