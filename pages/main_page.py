import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    ACCORDION_WITH_QUESTIONS = (By.CLASS_NAME, "accordion")

    @allure.step("Проскроллить к блоку 'Вопросы о важном'")
    def scroll_to_accordion_with_questions(self):
        self.scroll_to(self.ACCORDION_WITH_QUESTIONS)

        return self
