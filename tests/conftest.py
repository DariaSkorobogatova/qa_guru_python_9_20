import pytest
from selenium import webdriver
from selene import browser
LOGIN = 'testqaguruapi@mail.ru'
PASSWORD = 'Password123!'


@pytest.fixture()
def base_url():
    base_url = 'https://demowebshop.tricentis.com'
    return base_url


@pytest.fixture(scope='function', autouse=True)
def browser_configs(base_url):
    browser.config.base_url = base_url
    browser.config.timeout = 2.0
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    browser.config.driver_options = options
    yield
    browser.quit()

