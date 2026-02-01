import allure
from selenium.webdriver.common.by import By

from data import order_data
from pages.base_page import BasePage


class OrderPage(BasePage):

    # Элементы хедера
    LOGO_SCOOTER = (By.XPATH, ".//img[@alt='Scooter']")
    LOGO_YANDEX = (By.XPATH, ".//img[@alt='Yandex']")

    # Первая страница заказа
    FIRST_NAME_FIELD = (By.XPATH, ".//input[contains(@placeholder, 'Имя')]")
    LAST_NAME_FIELD = (By.XPATH, ".//input[contains(@placeholder, 'Фамилия')]")
    ADDRESS_DELIVERY_FIELD = (By.XPATH, ".//input[contains(@placeholder, 'Адрес')]")
    METRO_STATION_DROPDOWN = (By.XPATH, ".//input[contains(@placeholder, 'Станция')]")
    METRO_STATION_ITEM_AFTER_SEARCH = (By.CSS_SELECTOR, "button.select-search__option")
    PHONE_FIELD = (By.XPATH, ".//input[contains(@placeholder, 'Телефон')]")
    NEXT_BUTTON_ON_FIRST_ORDER_PAGE = (By.XPATH, ".//div[contains(@class, 'NextButton')]//button")

    # Вторая страница заказа
    DELIVERY_DATE_FIELD = (By.XPATH, ".//input[contains(@placeholder, 'Когда привезти')]")
    CURRENT_DAY_IN_DATE_PICKER = (By.XPATH, ".//div[@class='react-datepicker']//div[@tabindex=0]")
    RENTAL_PERIOD_FILED = (By.CLASS_NAME, "Dropdown-control")
    COMMENT_FIELD = (By.XPATH, ".//input[contains(@placeholder, 'Комментарий')]")
    ORDER_BUTTON_UNDER_FORM = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")
    BUTTON_CONFIRM_ODER = (By.XPATH, ".//div[contains(@class, 'Order_Modal_')]//button[text()='Да']")
    SUCCESS_ORDER_MODAL_WINDOW = (By.XPATH, ".//div[contains(@class, 'Order_ModalHeader')]")


    def get_locator_from_current_day(self, offset_day):
        return By.XPATH, f"{self.CURRENT_DAY_IN_DATE_PICKER[1]}/following-sibling::div[{offset_day}]"

    @staticmethod
    def get_rental_period_option_locator(value):
        return By.XPATH, f".//div[text()='{value}']"

    @staticmethod
    def get_locator_color_input(value):
        return By.XPATH, f".//input[@id='{value}']"

    @staticmethod
    def get_locator_color_text(value):
        return By.XPATH, f".//input[@id='{value}']/.."

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
            self.click(self.METRO_STATION_DROPDOWN)
            self.send_keys(self.METRO_STATION_DROPDOWN, metro_station)

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

    @allure.step("Заполнить дату доставки на: {delivery_date}")
    def enter_delivery_date(self, delivery_date: str):

        with allure.step("Нажать на поле даты доставки"):
            self.click(self.DELIVERY_DATE_FIELD)

        with allure.step("Выбрать указанную дату"):
            allowed = [item.value for item in order_data.DeliveryDate]

            if delivery_date in allowed:

                if delivery_date == "завтра":
                    self.click(self.get_locator_from_current_day(1))
                elif delivery_date == "послезавтра":
                    self.click(self.get_locator_from_current_day(2))
            else:
                raise ValueError(f"Передано некорректное значение: '{delivery_date}'. Допустимые значение '{allowed}'")

        return self

    @allure.step("Выбрать срок аренды: {rental_period}")
    def select_rental_period(self, rental_period: str):

        with allure.step("Нажать на поле 'Срок аренды'"):
            self.click(self.RENTAL_PERIOD_FILED)

        with allure.step("Выбрать значение из выпадающего списка {rental_period}"):
            locator = self.get_rental_period_option_locator(rental_period)
            self.click(locator)

            return self

    def select_color(self, color: str):
        locator_input = self.get_locator_color_input(color.lower())
        locator_text = self.get_locator_color_text(color.lower())

        text_color = self.get_text(locator_text)

        with allure.step(f"Нажать на чекбокс цвета: '{text_color}'"):
            self.click(locator_input)

        return self

    @allure.step("Заполнить комментарий: {comment}")
    def enter_comment(self, comment: str):
        self.send_keys(self.COMMENT_FIELD, comment)

        return self

    @allure.step("Нажать кнопку 'Заказать' под формой")
    def click_order_button_under_form(self):
        self.click(self.ORDER_BUTTON_UNDER_FORM)

        return self

    @allure.step("Подтвердить заказ в модальном окне")
    def confirm_order(self):
        self.click(self.BUTTON_CONFIRM_ODER)

    @allure.step("Успешное отображение модального окна оформления заказа")
    def succes_modal_with_text(self, expected_text):

        with allure.step("Модальное окно отображается"):
            assert self.is_visible(self.SUCCESS_ORDER_MODAL_WINDOW)

        with allure.step(f"Текст в модальном окне содежит ожидаемый текст: '{expected_text}'"):
            actual_text = self.get_text(self.SUCCESS_ORDER_MODAL_WINDOW)
            assert expected_text in actual_text

    @allure.step("Нажать на лого 'Самокат'")
    def click_scooter_logo(self):
        self.click(self.LOGO_SCOOTER)

        return self

    @allure.step("Нажать на лого 'Яндекс'")
    def click_yandex_logo(self):
        self.click(self.LOGO_YANDEX)

        return self