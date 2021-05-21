from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="./drivers/chromedriver")
    elif browser == 'firefox':
        print("test")
        driver = webdriver.Firefox(executable_path="./drivers/geckodriver")
    else:
        try:
            driver = webdriver.Chrome(executable_path="./drivers/chromedriver")
        except:
            driver = webdriver.Firefox(executable_path="./drivers/geckodriver")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
    config._metadata['Project Name'] = 'UAHEP'
    config._metadata['Module Name'] = 'Add grievance'
    config._metadata['Tester'] = 'Bipin'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
