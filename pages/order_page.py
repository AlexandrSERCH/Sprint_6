from enum import Enum

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OrderPage(BasePage):

    # Первая страница заказа

    FIRST_NAME_FIELD = (By.XPATH, ".//input[contains(@placeholder, 'Имя')]")
    LAST_NAME_FIELD = (By.XPATH, ".//input[contains(@placeholder, 'Фамилия')]")
    ADDRESS_DELIVERY_FIELD = (By.XPATH, ".//input[contains(@placeholder, 'Адрес')]")
    METRO_STATION_DROPDAWN = (By.XPATH, ".//input[contains(@placeholder, 'Станция')]")
    METRO_STATION_ITEM_AFTER_SEARCH = (By.CSS_SELECTOR, "button.select-search__option")
    PHONE_FIELD = (By.XPATH, ".//input[contains(@placeholder, 'Телефон')]")
    NEXT_BUTTON_ON_FIRST_ORDER_PAGE = (By.XPATH, ".//div[contains(@class, 'NextButton')]//button")


    @allure.step("Заполнить имя: {first_name}")
    def enter_first_name(self, first_name: str):
        self.send_keys(self.FIRST_NAME_FIELD, first_name)

        return self

    @allure.step("Заполнить фамилию: {last_name}")
    def enter_last_name(self, last_name: str):
        self.send_keys(self.LAST_NAME_FIELD, last_name)

        return self

    @allure.step("Заполнить адрес: {addres_delivery}")
    def enter_addres_delivery(self, addres_delivery: str):
        self.send_keys(self.ADDRESS_DELIVERY_FIELD, addres_delivery)

        return self

    @allure.step("Выбрать станцию метро: {metro_station}")
    def select_metro_station(self, metro_station: str):

        with allure.step("Нажать на дропдаун станции метро и ввести станцию"):
            self.click(self.METRO_STATION_DROPDAWN)
            self.send_keys(self.METRO_STATION_DROPDAWN, metro_station)

        with allure.step("Выбрать первое значение из результата поиска"):
            self.click(self.METRO_STATION_ITEM_AFTER_SEARCH)

            return self

    @allure.step("Заполнить телефон: {phone}")
    def enter_phone(self, phone):
        self.send_keys(self.PHONE_FIELD, phone)

        return self

    @allure.step("Нажать кнопку 'Далее' на первой странице заказа")
    def click_next_button_on_first_order_page(self):
        self.click(self.NEXT_BUTTON_ON_FIRST_ORDER_PAGE)

        return  self