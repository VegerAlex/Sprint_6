from selenium.webdriver.common.by import By

class ImportantQuestionsPage:
    def __init__(self, driver):
        self.driver = driver
        self.questions = driver.find_elements(By.CSS_SELECTOR, ".accordion__button")

    def click_question(self, index):
        self.questions[index].click()

    def get_answer_text(self, index):
        return self.questions[index].find_element(By.XPATH, "./following-sibling::div").text

    def is_text_displayed(self, index):
        return self.questions[index].find_element(By.XPATH, "./following-sibling::div").is_displayed()
