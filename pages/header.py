import allure
from .base_page import BasePage
from locators.header_locators import HeaderLocators
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

    @allure.step("Клик по ссылке 'Как это работает'")
    def click_how_it_works(self):
        self.click_element(HeaderLocators.HOW_IT_WORKS)

    @allure.step("Клик по ссылке 'О компании'")
    def click_about_us(self):
        self.click_element(HeaderLocators.ABOUT_US)

    @allure.step("Клик по ссылке 'Контакты'")
    def click_contacts(self):
        self.click_element(HeaderLocators.CONTACTS)


