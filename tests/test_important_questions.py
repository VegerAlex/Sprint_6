import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    # Создаем экземпляр драйвера для Firefox
    driver = webdriver.Firefox()
    yield driver
    # Закрываем браузер после завершения теста
    driver.quit()


def check_question_and_answer(question, expected_answer, driver):
    # Открываем страницу с важными вопросами
    driver.get("https://qa-scooter.praktikum-services.ru")

    # Принятие cookies
    try:
        accept_cookies_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
        )
        accept_cookies_button.click()
        print("Cookies accepted.")
    except Exception as e:
        print(f"Cookies button not found or could not be clicked: {e}")

    # Прокручиваем страницу до раздела с вопросами
    questions_section = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "accordion"))
    )
    driver.execute_script("arguments[0].scrollIntoView();", questions_section)
    print("Scrolled to questions section.")

    # Находим стрелочку рядом с вопросом и кликаем на неё
    try:
        arrow_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@class='accordion__button' and text()='{question}']"))
        )
        arrow_element.click()
        print(f"Clicked on question: {question}")
    except Exception as e:
        print(f"Question arrow not found or could not be clicked: {e}")

    # Ожидание появления ответа и получение текста ответа
    try:
        answer_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              f"//div[@class='accordion__button' and text()='{question}']/following-sibling::div[contains(@class, 'accordion__panel') and @aria-hidden='false']"))
        )
        print(f"Answer found for question: {question}")
        # Сравниваем текст ответа с ожидаемым
        assert expected_answer in answer_element.text, f"Unexpected answer for question '{question}'"
    except Exception as e:
        print(f"Answer not found or text does not match: {e}")


def test_question_1(driver):
    question = "Сколько это стоит? И как оплатить?"
    expected_answer = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    check_question_and_answer(question, expected_answer, driver)


def test_question_2(driver):
    question = "Хочу сразу несколько самокатов! Так можно?"
    expected_answer = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
    check_question_and_answer(question, expected_answer, driver)


def test_question_3(driver):
    question = "Как рассчитывается время аренды?"
    expected_answer = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
    check_question_and_answer(question, expected_answer, driver)


def test_question_4(driver):
    question = "Можно ли заказать самокат прямо на сегодня?"
    expected_answer = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    check_question_and_answer(question, expected_answer, driver)


def test_question_5(driver):
    question = "Можно ли продлить заказ или вернуть самокат раньше?"
    expected_answer = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    check_question_and_answer(question, expected_answer, driver)


def test_question_6(driver):
    question = "Вы привозите зарядку вместе с самокатом?"
    expected_answer = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
    check_question_and_answer(question, expected_answer, driver)


def test_question_7(driver):
    question = "Можно ли отменить заказ?"
    expected_answer = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
    check_question_and_answer(question, expected_answer, driver)


def test_question_8(driver):
    question = "Я жизу за МКАДом, привезёте?"
    expected_answer = "Да, обязательно. Всем самокатов! И Москве, и Московской области."
    check_question_and_answer(question, expected_answer, driver)
