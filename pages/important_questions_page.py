import allure
from .base_page import BasePage
from locators.important_questions_page_locators import ImportantQuestionsPageLocators

class ImportantQuestionsPage(BasePage):
    @allure.step("Клик по вопросу")
    def click_question(self, index):
        questions = self.wait_for_element_visible(ImportantQuestionsPageLocators.QUESTIONS)
        questions[index].click()

    @allure.step("Получение текста ответа")
    def get_answer_text(self, index):
        questions = self.wait_for_element_visible(ImportantQuestionsPageLocators.QUESTIONS)
        return questions[index].find_element(By.XPATH, "./following-sibling::div").text

    @allure.step("Проверка отображения текста ответа")
    def is_text_displayed(self, index):
        questions = self.wait_for_element_visible(ImportantQuestionsPageLocators.QUESTIONS)
        return questions[index].find_element(By.XPATH, "./following-sibling::div").is_displayed()
