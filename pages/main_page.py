import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    ACCORDION_WITH_QUESTIONS = (By.CLASS_NAME, "accordion")

    @staticmethod
    def get_locator_question_in_faq(index):
        return By.XPATH, f".//div[@id='accordion__heading-{index}']"

    @staticmethod
    def get_locator_answer_in_faq(index):
        return By.XPATH, f".//div[@id='accordion__panel-{index}']"

    @allure.step("Проскроллить к блоку 'Вопросы о важном'")
    def scroll_to_accordion_with_questions(self):
        self.scroll_to(self.ACCORDION_WITH_QUESTIONS)

        return self

    @allure.step("Нажать на вопрос № {index}")
    def click_on_question_from_faq(self, index: str):
        locator = self.get_locator_question_in_faq(index)
        self.click(locator)

        return self

    @allure.step("Получить текст ответа на вопрос № {index}")
    def get_text_answer_from_question(self, index: str):
        locator = self.get_locator_answer_in_faq(index)

        return self.get_text(locator)

