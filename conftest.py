from selene import browser
import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_config():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.window_width = 1690
    browser.config.window_height = 1080
    browser.config.timeout = 5.0

    yield

    browser.quit()