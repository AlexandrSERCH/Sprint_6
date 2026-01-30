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

    def click_on_question_from_faq(self, index: str):
        locator = self.get_locator_question_in_faq(index)

        question_text = self.get_text(locator)
        with allure.step(f"Нажать на вопрос: '{question_text}'"):
            self.click(locator)

        return self

    def get_text_answer_from_question(self, index: str):
        locator = self.get_locator_answer_in_faq(index)

        answer_text = self.get_text(locator)
        with allure.step(f"Получить фактический текст ответа: '{answer_text}'"):
            return answer_text




