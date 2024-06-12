from selenium.webdriver.common.by import By

class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.name_field = driver.find_element(By.XPATH, "//input[@placeholder='* Имя']")
        self.surname_field = driver.find_element(By.XPATH, "//input[@placeholder='* Фамилия']")
        self.address_field = driver.find_element(By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
        self.phone_field = driver.find_element(By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
        self.submit_button = driver.find_element(By.CSS_SELECTOR, ".Button_Button__ra12g.Button_Middle__1CSJM")

    def fill_order_form(self, name, surname, address, phone):
        self.name_field.send_keys(name)
        self.surname_field.send_keys(surname)
        self.address_field.send_keys(address)
        self.phone_field.send_keys(phone)
        self.submit_button.click()

