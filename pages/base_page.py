import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидание видимости элемента")
    def wait_for_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Клик по элементу")
    def click_element(self, locator):
        element = self.wait_for_element_visible(locator)
        element.click()

    @allure.step("Отправка текста в элемент")
    def send_keys_to_element(self, locator, text):
        element = self.wait_for_element_visible(locator)
        element.send_keys(text)
