import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.confirmation_page import ConfirmationPage
from locators.urls import URLs

@pytest.mark.parametrize("name, surname, address, phone", [
    ("Иван", "Иванов", "ул. Пушкина, д. 1", "+79999999999"),
    ("Петр", "Петров", "ул. Лермонтова, д. 2", "+79888888888")
])
def test_order_scooter(driver, name, surname, address, phone):
    with allure.step("Открытие главной страницы"):
        driver.get(URLs.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.click_order_bottom()

    with allure.step("Заполнение формы заказа"):
        order_page = OrderPage(driver)
        order_page.fill_order_form(name, surname, address, phone)

    with allure.step("Проверка отображения подтверждения"):
        confirmation_page = ConfirmationPage(driver)
        assert confirmation_page.is_confirmation_displayed()

