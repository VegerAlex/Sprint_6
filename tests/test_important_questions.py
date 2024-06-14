import pytest
import allure
from pages.main_page import MainPage
from pages.important_questions_page import ImportantQuestionsPage
from locators.urls import URLs

@pytest.mark.parametrize("question, expected_answer", [
    ("Сколько это стоит? И как оплатить?", "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
    ("Хочу сразу несколько самокатов! Так можно?", "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
    ("Как рассчитывается время аренды?", "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
    ("Можно ли заказать самокат прямо на сегодня?", "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
    ("Можно ли продлить заказ или вернуть самокат раньше?", "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
    ("Вы привозите зарядку вместе с самокатом?", "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
    ("Можно ли отменить заказ?", "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
    ("Я живу за МКАДом, привезёте?", "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
])
def test_important_questions(driver, question, expected_answer):
    with allure.step("Открытие главной страницы"):
        driver.get(URLs.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.click_order_bottom()

    with allure.step("Открытие раздела важных вопросов"):
        important_questions_page = ImportantQuestionsPage(driver)
        question_index = important_questions_page.get_question_index(question)
        important_questions_page.click_question(question_index)

    with allure.step("Проверка текста ответа"):
        assert important_questions_page.is_text_displayed(question_index)
        assert expected_answer in important_questions_page.get_answer_text(question_index)
