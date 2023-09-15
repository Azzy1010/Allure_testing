import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
global driver


@pytest.fixture
def setup():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield
    driver.quit()


def test_website_title_chrome(setup):
    driver.get('https://www.google.com')
    title = driver.title
    # pyautogui.alert(text = f'{item}')
    if title == 'Google':
        assert True
    else:
        allure.attach(driver.get_screenshot_as_png(), name='Chrome_failed',attachment_type=AttachmentType.PNG)
        driver.close()
        assert False


