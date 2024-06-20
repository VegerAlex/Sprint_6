import allure
from .base_page import BasePage
from locators.confirmation_page_locators import ConfirmationPageLocators

class ConfirmationPage(BasePage):
    @allure.step("Проверка отображения подтверждения")
    def is_confirmation_displayed(self):
        confirmation = self.wait_for_element_visible(ConfirmationPageLocators.CONFIRMATION)
        return confirmation.is_displayed()

