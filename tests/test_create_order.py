import allure
import pytest

from data.order_data import get_order_datasets


class TestCreateOrder:

    @allure.epic("Заказы")
    @allure.feature("Оформление заказа")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("UI", "regress", "Заказы")
    @allure.label("owner", "Александр")
    @allure.title("Создание заказа")
    @pytest.mark.parametrize("order_data", get_order_datasets())
    def test_create_order(self, order_page, order_data):

         order_page.enter_first_name(order_data.first_name)
         order_page.enter_last_name(order_data.last_name)
         order_page.enter_addres_delivery(order_data.address_delivery)
         order_page.select_metro_station(order_data.metro_station.value)
         order_page.enter_phone(order_data.phone)
         order_page.click_next_button_on_first_order_page()

         order_page.enter_delivery_date(order_data.delivery_date.value)
         order_page.select_rental_period(order_data.rental_period.value)
         order_page.select_color(order_data.color.name)
         order_page.enter_comment(order_data.comment)
         order_page.click_order_button_under_form()
         order_page.confirm_order()

         order_page.succes_modal_with_text("Заказ оформлен")
