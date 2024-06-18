import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.confirmation_page import ConfirmationPage
from pages.header import Header
from locators.urls import URLs

@allure.suite("Тесты заказа самоката")
class TestOrderScooter:
    @allure.title("Тест заказа самоката")
    def test_order_scooter(self, driver):
        with allure.step("Открытие главной страницы"):
            driver.get(URLs.MAIN_PAGE)
            main_page = MainPage(driver)
            main_page.click_order_top()

        with allure.step("Заполнение формы заказа"):
            order_page = OrderPage(driver)
            order_page.fill_order_form("Имя", "Фамилия", "Адрес", "Станция метро", "89001234567", "Комментарий")

        with allure.step("Подтверждение заказа"):
            confirmation_page = ConfirmationPage(driver)
            confirmation_page.confirm_order()

        with allure.step("Проверка отображения подтверждения"):
            assert confirmation_page.is_confirmation_displayed()

    @allure.title("Тест на переход по ссылкам")
    def test_navigation_links(self, driver):
        with allure.step("Открытие главной страницы"):
            driver.get(URLs.MAIN_PAGE)
            header = Header(driver)

        with allure.step("Переход на страницу 'Как это работает'"):
            header.click_how_it_works()
            assert driver.current_url == URLs.HOW_IT_WORKS_PAGE

        with allure.step("Переход на страницу 'О компании'"):
            header.click_about_us()
            assert driver.current_url == URLs.ABOUT_US_PAGE

        with allure.step("Переход на страницу 'Контакты'"):
            header.click_contacts()
            assert driver.current_url == URLs.CONTACTS_PAGE

    @allure.title("Тест перехода по логотипу Scooter")
    def test_scooter_logo(self, driver):
        with allure.step("Открытие страницы 'Как это работает'"):
            driver.get(URLs.HOW_IT_WORKS_PAGE)
            header = Header(driver)

        with allure.step("Клик по логотипу Scooter"):
            header.click_scooter_logo()
            assert driver.current_url == URLs.MAIN_PAGE

    @allure.title("Тест перехода по логотипу Яндекс")
    def test_yandex_logo(self, driver):
        with allure.step("Открытие главной страницы"):
            driver.get(URLs.MAIN_PAGE)
            header = Header(driver)

        with allure.step("Клик по логотипу Яндекс"):
            header.click_yandex_logo()
            driver.switch_to.window(driver.window_handles[-1])
            assert "dzen.ru" in driver.current_url
