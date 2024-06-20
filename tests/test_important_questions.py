import pytest
import allure
from pages.important_questions_page import ImportantQuestionsPage
from locators.urls import URLs

@allure.suite("Тесты важных вопросов")
class TestImportantQuestions:
    @allure.title("Тест отображения ответов на важные вопросы")
    @pytest.mark.parametrize("question, expected_answer", [
        ("Можно ли отменить заказ?", "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        ("Я живу за МКАДом, привезёте?", "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
    ])
    def test_important_questions(self, driver, question, expected_answer):
        with allure.step("Открытие страницы важных вопросов"):
            driver.get(URLs.IMPORTANT_QUESTIONS_PAGE)
            important_questions_page = ImportantQuestionsPage(driver)
            important_questions_page.wait_for_page_to_load()

        with allure.step(f"Проверка ответа на вопрос '{question}'"):
            important_questions_page.click_question(question)
            answer_text = important_questions_page.get_answer_text(question)
            assert answer_text == expected_answer
