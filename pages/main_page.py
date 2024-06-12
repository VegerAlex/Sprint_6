from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.order_button_top = driver.find_element(By.CSS_SELECTOR, ".Button_Button__ra12g")
        self.order_button_bottom = driver.find_element(By.CSS_SELECTOR, ".Button_Button__ra12g.Button_Middle__1CSJM")

    def click_order_top(self):
        self.order_button_top.click()

    def click_order_bottom(self):
        self.order_button_bottom.click()
