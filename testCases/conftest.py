from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError("Browser not supported: {}".format(browser))
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

def mock_captcha_validation():
    return True  # Always pass


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
    if hasattr(config, '_metadata'):
        config._metadata['Project Name'] = 'nopCommerce'
        config._metadata['Module Name'] = 'Login'
        config._metadata['Tester'] = 'Uthira'

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
