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

    @allure.step("Переход на страницу 'Как это работает'")
    def click_how_it_works(self):
        self.click_element(HeaderLocators.HOW_IT_WORKS)

    @allure.step("Переход на страницу 'О компании'")
    def click_about_us(self):
        self.click_element(HeaderLocators.ABOUT_US)

    @allure.step("Переход на страницу 'Контакты'")
    def click_contacts(self):
        self.click_element(HeaderLocators.CONTACTS)

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Ожидание открытия новой вкладки и переключение на неё")
    def switch_to_new_window(self):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Закрытие текущей вкладки и переключение на первоначальную")
    def close_current_window_and_switch_back(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
