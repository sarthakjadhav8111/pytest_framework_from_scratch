from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver = webdriver.Chrome()
        print("launching chrome")
        return driver
    elif browser=="edge":
        driver = webdriver.Edge()
        print("launching edge")
        return driver
    else:
        driver = webdriver.Chrome()
        return driver

# run test on desired browser through CLI

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# Generate pytest html reports #

# this is hook for adding environment into html report
def pytest_configure(config):
    config.metadata = {'Project Name':'nop commerce'}
    config.metadata = {'Module Name':'Customers'}
    config.metadata = {'Tester':'Sarthak'}

# this is hook for delete/modify environment into html report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

