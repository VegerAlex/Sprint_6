import allure
from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):
    @allure.step("Заполнение формы заказа")
    def fill_order_form(self, name, surname, address, phone):
        self.send_keys_to_element(OrderPageLocators.NAME_FIELD, name)
        self.send_keys_to_element(OrderPageLocators.SURNAME_FIELD, surname)
        self.send_keys_to_element(OrderPageLocators.ADDRESS_FIELD, address)
        self.send_keys_to_element(OrderPageLocators.PHONE_FIELD, phone)
        self.click_element(OrderPageLocators.SUBMIT_BUTTON)


