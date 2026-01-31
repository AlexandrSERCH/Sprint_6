import allure

from core.config import site_url


class TestRedirectFromOrder:

    @allure.epic("Редиректы")
    @allure.feature("Редиректы со страницы заказа")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("UI", "regress", "Заказы")
    @allure.label("owner", "Александр")
    @allure.title("Редирект со страницы заказа на главную")
    def test_redirect_from_order_to_main_page(self, browser, order_page):
        order_page.click_scooter_logo()

        expected_url = site_url()
        actual_url = browser.current_url

        with allure.step("Успешный переход на главную страницу"):
            assert actual_url == expected_url

    @allure.epic("Редиректы")
    @allure.feature("Редиректы со страницы заказа")
    @allure.severity(allure.severity_level.MINOR)
    @allure.tag("UI", "regress", "Заказы")
    @allure.label("owner", "Александр")
    @allure.title("Редирект со страницы заказа на Дзен")
    def test_redirect_from_order_to_dzen_page(self, order_page):
        expected_title = "Дзен — главная новостная информационная платформа, которая помогает миллионам людей узнавать, что происходит в мире."

        order_page.click_yandex_logo()

        with allure.step("Переход на открывшуюся вкладку"):
            order_page.switch_to_second_tab()

        with allure.step(f"Заголовок перенаправенной страницы равен ожидаемому заголовку: '{expected_title}'"):
            assert order_page.title_equal(expected_title)





