import allure


class TestAccordionsWithQuestions:

    @allure.epic("Главная страница")
    @allure.feature("Блок 'Вопросы о важном'")
    @allure.severity(allure.severity_level.NORMAL)  # Критичность дефекта при падении теста
    @allure.tag("UI", "regress", "Главная страница")
    @allure.label("owner", "Александр")
    @allure.title("Отображение ожидаемых ответов при нажатии на вопрос")
    def test_dropdown_displays_expected_text(self, main_page):
        main_page.scroll_to_accordion_with_questions()
