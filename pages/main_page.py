import allure
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    @allure.step("Клик по верхней кнопке заказа")
    def click_order_top(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Клик по нижней кнопке заказа")
    def click_order_bottom(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
