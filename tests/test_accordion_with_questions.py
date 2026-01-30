import allure
import pytest

from data.accordion_faq_data import get_index_question_and_answers_with_faq


class TestAccordionsWithQuestions:

    @allure.epic("Главная страница")
    @allure.feature("Блок 'Вопросы о важном'")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("UI", "regress", "Главная страница")
    @allure.label("owner", "Александр")
    @allure.title("Отображение ожидаемых ответов при нажатии на вопрос")
    @pytest.mark.parametrize("index,expected_answer_text", get_index_question_and_answers_with_faq())
    def test_dropdown_displays_expected_text(self, main_page, index, expected_answer_text):
        main_page.scroll_to_accordion_with_questions()
        main_page.click_on_question_from_faq(index)

        actual_answer_text = main_page.get_text_answer_from_question(index)

        with allure.step(f"Проверить, что ожидаемый текст: ответа '{expected_answer_text}' соответствует фактическому"):
            assert actual_answer_text == expected_answer_text

