import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from data import TestUser


@pytest.fixture(scope="function")
def driver():
    """Фикстура для инициализации и закрытия веб-драйвера"""
    # Настройка опций Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    options.add_argument("--incognito")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    # Инициализация драйвера
    driver = webdriver.Chrome(options=options)
    driver.get("https://stellarburgers.nomoreparties.site/")
    
    yield driver
    # Закрытие драйвера после теста
    driver.quit()


@pytest.fixture
def login(driver):
    """Фикстура для авторизации пользователя перед тестами"""
    # Переход к форме авторизации
    driver.find_element(*TestLocators.BUTTON_LOGIN_MAIN).click()
    
    # Ожидание загрузки формы
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(TestLocators.BUTTON_REGISTER)
    )
    
    # Ввод учетных данных
    driver.find_element(*TestLocators.INPUT_EMAIL_AUTH).send_keys(TestUser.EXISTING_EMAIL)
    driver.find_element(*TestLocators.INPUT_PASSWORD_AUTH).send_keys(TestUser.EXISTING_PASSWORD)
    
    # Выполнение входа
    driver.find_element(*TestLocators.BUTTON_LOGIN).click()
    
    # Ожидание успешной авторизации
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER)
    )