import allure
from .base_page import BasePage
from locators.header_locators import HeaderLocators

class Header(BasePage):
    @allure.step("Клик по логотипу Scooter")
    def click_scooter_logo(self):
        self.click_element(HeaderLocators.SCOOTER_LOGO)

    @allure.step("Клик по логотипу Yandex")
    def click_yandex_logo(self):
        self.click_element(HeaderLocators.YANDEX_LOGO)

