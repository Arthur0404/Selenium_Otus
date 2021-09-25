import pytest
from selenium import webdriver
from selenium.webdriver.opera.options import Options as OperaOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "opera"], help="Browser")
    parser.addoption("--maximized", action="store_true", help="Maximize browser window")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--url", default="http://localhost/")


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")

    def fin():
        print("Test is close")
        driver.quit()

    request.addfinalizer(fin)

    driver = None

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless: options.headless = True
        driver = webdriver.Chrome("/usr/local/bin/chromedriver")

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless: options.headless = True
        driver = webdriver.Firefox(options=options)

    elif browser == "opera":
        options = OperaOptions()
        if headless: options.headless == True
        driver = webdriver.Opera(options=options)

    if maximized:
        driver.maximize_window()

    return driver
