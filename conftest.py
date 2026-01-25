import allure
import pytest
from selenium import webdriver

from core.config import site_url
from pages.main_page import MainPage
from utlis.attach import attach_screenshot


@pytest.fixture(scope="function", autouse=True)
def browser():
    driver = webdriver.Firefox()
    driver.maximize_window()

    yield driver

    attach_screenshot(driver)
    driver.quit()

@pytest.fixture
def main_page(browser):
    url = site_url()
    with allure.step(f"Открыть главную страницу: {url}"):
        browser.get(url)

    return MainPage(browser)


'''
Хук, который отлавливает момент падения теста и делает скриншот.
Необходим, чтобы успеть сделать скриншот, если на экране, к примеру
помешал поп-ап, на странице не видно необходимый элемент или элемент не отобразился и т.п.
'''
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("browser")
        if driver:
            with allure.step("Скриншот при падении"):
                attach_screenshot(driver)