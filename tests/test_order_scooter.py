import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    # Закрываем всплывающее окно с куки
    try:
        cookie_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='да все привыкли']"))
        )
        cookie_button.click()
    except:
        pass  # Если всплывающее окно не появляется, просто продолжаем
    yield driver
    driver.quit()

@pytest.mark.parametrize("name, surname, address, metro_station, phone, delivery_date, rental_period, color, comment", [
    ("Иван", "Иванов", "Москва, ул. Пушкина", "Сокольники", "+79991234567", "2024-06-15", "двое суток", "чёрный жемчуг",
     "Без звонка"),
    ("Анна", "Петрова", "Санкт-Петербург, ул. Колотушкина", "Парк Культуры", "+79997654321", "2024-06-20", "трое суток",
     "серая безысходность", "Позвоните за час")
])
def test_order_scooter(driver, name, surname, address, metro_station, phone, delivery_date, rental_period, color,
                       comment):
    # Нажимаем на кнопку "Заказать" вверху страницы
    order_button_top = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='Button_Button__ra12g']"))
    )
    order_button_top.click()

    # Заполняем форму "Для кого самокат"
    name_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='* Имя']"))
    )
    surname_field = driver.find_element(By.XPATH, "//input[@placeholder='* Фамилия']")
    address_field = driver.find_element(By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    metro_field = driver.find_element(By.XPATH, "//input[@placeholder='* Станция метро']")
    phone_field = driver.find_element(By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    next_button = driver.find_element(By.CSS_SELECTOR, ".Button_Button__ra12g.Button_Middle__1CSJM")

    name_field.send_keys(name)
    surname_field.send_keys(surname)
    address_field.send_keys(address)
    metro_field.click()

    # Прокручиваем выпадающий список и выбираем станцию метро
    while True:
        metro_options = driver.find_elements(By.XPATH, "//div[@class='select-search__options']//div")
        for option in metro_options:
            if metro_station in option.text:
                option.click()
                break
        else:
            # Если станция не найдена, прокручиваем вниз
            metro_options[-1].send_keys(Keys.PAGE_DOWN)
            continue
        break

    phone_field.send_keys(phone)
    next_button.click()

    # Заполняем форму "Про аренду"
    date_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='* Когда привезти самокат']"))
    )
    rental_period_field = driver.find_element(By.XPATH, "//div[contains(text(), 'срок аренды')]")
    color_black_checkbox = driver.find_element(By.XPATH, "//input[@id='black']")
    color_grey_checkbox = driver.find_element(By.XPATH, "//input[@id='grey']")
    comment_field = driver.find_element(By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    order_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Заказать')]")

    date_field.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//div[@aria-label='{delivery_date}']"))
    ).click()

    rental_period_field.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), '{rental_period}')]"))
    ).click()

    if color == "чёрный жемчуг":
        color_black_checkbox.click()
    elif color == "серая безысходность":
        color_grey_checkbox.click()

    comment_field.send_keys(comment)
    order_button.click()

    # Подтверждаем заказ в модальном окне
    confirm_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Да')]"))
    )
    confirm_button.click()

    # Проверяем, что заказ успешно создан
    order_success_modal = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".Order_ModalHeader__3FDaJ"))
    )
    assert order_success_modal.is_displayed()

def test_click_scooter_logo(driver):
    header_scooter_logo = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//img[@alt='Scooter Logo']"))
    )
    header_scooter_logo.click()
    assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

def test_click_yandex_logo(driver):
    header_yandex_logo = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//img[@alt='Yandex Logo']"))
    )
    main_window = driver.current_window_handle
    header_yandex_logo.click()
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    new_window = [window for window in driver.window_handles if window != main_window][0]
    driver.switch_to.window(new_window)
    assert "dzen.ru" in driver.current_url
    driver.close()
    driver.switch_to.window(main_window)
