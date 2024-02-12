import pytest
from selene import browser
from dotenv import load_dotenv
import os

load_dotenv()
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')


@pytest.fixture()
def base_url():
    base_url = 'https://demowebshop.tricentis.com'
    return base_url


@pytest.fixture(scope='function', autouse=True)
def browser_configs(base_url):
    browser.config.base_url = base_url
    browser.config.timeout = 2.0
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()

