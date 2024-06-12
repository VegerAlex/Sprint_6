from selenium.webdriver.common.by import By

class Header:
    def __init__(self, driver):
        self.driver = driver
        self.scooter_logo = driver.find_element(By.CSS_SELECTOR, ".Header_LogoScooter__3lsAR")
        self.yandex_logo = driver.find_element(By.CSS_SELECTOR, ".Header_LogoYandex__3TSOI")

    def click_scooter_logo(self):
        self.scooter_logo.click()

    def click_yandex_logo(self):
        self.yandex_logo.click()
