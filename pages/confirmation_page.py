from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ConfirmationPage:
    def __init__(self, driver):
        self.driver = driver

    def is_confirmation_displayed(self):
        confirmation = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".Order_ModalHeader__3FDaJ"))
        )
        return confirmation.is_displayed()
