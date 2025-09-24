import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators
from helpers import generate_random_email, generate_random_password, generate_name
from data import TestUser


class TestRegistration:
    """Тесты регистрации нового пользователя"""
    
    def test_registration_new_account_success_submit(self, driver):
        """
        Успешная регистрация нового аккаунта
        Шаги:
        1. Перейти к форме регистрации
        2. Заполнить все поля валидными данными
        3. Нажать кнопку 'Зарегистрироваться'
        4. Проверить переход на страницу авторизации
        """
        random_email = generate_random_email()
        random_password = generate_random_password()
        random_name = generate_name()
        
        driver.find_element(*TestLocators.BUTTON_LOGIN_MAIN).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_REGISTER)
        )
        
        driver.find_element(*TestLocators.BUTTON_REGISTER).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_SUBMIT)
        )
        
        driver.find_element(*TestLocators.INPUT_NAME).send_keys(random_name)
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(random_email)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(random_password)
        driver.find_element(*TestLocators.BUTTON_SUBMIT).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_LOGIN)
        )
        assert driver.find_element(*TestLocators.BUTTON_REGISTER).is_displayed()


    def test_registration_name_is_empty_submit(self, driver):
        """
         Регистрация с пустым полем 'Имя'
        Ожидаемый результат: Форма не отправляется,ошибка валидации
        """
        random_email = generate_random_email()
        random_password = generate_random_password()
        
        driver.find_element(*TestLocators.BUTTON_LOGIN_MAIN).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_REGISTER)
        )
        driver.find_element(*TestLocators.BUTTON_REGISTER).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_SUBMIT)
        )
        
        driver.find_element(*TestLocators.INPUT_NAME).send_keys('')
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(random_email)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(random_password)
        driver.find_element(*TestLocators.BUTTON_SUBMIT).click()
        
        assert driver.find_element(*TestLocators.BUTTON_SUBMIT).is_displayed()


    def test_registration_invalid_email_no_at_symbol(self, driver):
        """
        Регистрация с невалидным email без символа @ при валидных имени и пароле
        Ожидаемый результат: Форма не отправляется, ошибка валидации
        """
        random_password = generate_random_password()
        invalid_email = "invalidemail.example.com"
        
        driver.find_element(*TestLocators.BUTTON_LOGIN_MAIN).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_REGISTER)
        )
        driver.find_element(*TestLocators.BUTTON_REGISTER).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_SUBMIT)
        )
        
        driver.find_element(*TestLocators.INPUT_NAME).send_keys(TestUser.EXISTING_NAME)
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(invalid_email)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(random_password)
        driver.find_element(*TestLocators.BUTTON_SUBMIT).click()
        
        assert driver.find_element(*TestLocators.BUTTON_SUBMIT).is_displayed()


    def test_registration_email_no_domain(self, driver):
        """
        Регистрация с email без домена верхнего уровня при валидных имени и пароле
        Ожидаемый результат: Форма не отправляется, ошибка валидации email
        """
        random_password = generate_random_password()
        invalid_email = "test@example."
        
        driver.find_element(*TestLocators.BUTTON_LOGIN_MAIN).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_REGISTER)
        )
        driver.find_element(*TestLocators.BUTTON_REGISTER).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_SUBMIT)
        )
        
        driver.find_element(*TestLocators.INPUT_NAME).send_keys(TestUser.EXISTING_NAME)
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(invalid_email)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(random_password)
        driver.find_element(*TestLocators.BUTTON_SUBMIT).click()
        
        assert driver.find_element(*TestLocators.BUTTON_SUBMIT).is_displayed()


    @pytest.mark.parametrize('valid_password', ['123456', '1234567', '123456789012'])
    def test_registration_valid_length_password_submit(self, driver, valid_password):
        """
        Регистрация с валидными паролями разной длины
        """
        random_email = generate_random_email()
        
        driver.find_element(*TestLocators.BUTTON_LOGIN_MAIN).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_REGISTER)
        )
        driver.find_element(*TestLocators.BUTTON_REGISTER).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_SUBMIT)
        )
        
        driver.find_element(*TestLocators.INPUT_NAME).send_keys(TestUser.EXISTING_NAME)
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(random_email)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(valid_password)
        driver.find_element(*TestLocators.BUTTON_SUBMIT).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_LOGIN)
        )
        assert driver.find_element(*TestLocators.BUTTON_REGISTER).is_displayed()


    @pytest.mark.parametrize('wrong_password', ['12345', '1234', '1', ''])
    def test_registration_invalid_length_password_submit(self, driver, wrong_password):
        """
        Регистрация с невалидными паролями (короткие)
        """
        random_email = generate_random_email()
        
        driver.find_element(*TestLocators.BUTTON_LOGIN_MAIN).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_REGISTER)
        )
        driver.find_element(*TestLocators.BUTTON_REGISTER).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_SUBMIT)
        )
        
        driver.find_element(*TestLocators.INPUT_NAME).send_keys(TestUser.EXISTING_NAME)
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(random_email)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(wrong_password)
        driver.find_element(*TestLocators.BUTTON_SUBMIT).click()
        
        assert driver.find_element(*TestLocators.BUTTON_SUBMIT).is_displayed()


    @pytest.mark.parametrize('wrong_password', ['12345', '1234', '1'])
    def test_registration_short_password_error(self, driver, wrong_password):
        """
        Проверка сообщения об ошибке для короткого пароля
        """
        random_email = generate_random_email()
        
        driver.find_element(*TestLocators.BUTTON_LOGIN_MAIN).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_REGISTER)
        )
        driver.find_element(*TestLocators.BUTTON_REGISTER).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_SUBMIT)
        )
        
        driver.find_element(*TestLocators.INPUT_NAME).send_keys(TestUser.EXISTING_NAME)
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(random_email)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(wrong_password)
        driver.find_element(*TestLocators.BUTTON_SUBMIT).click()
        
        error_text = driver.find_element(*TestLocators.NOTIFICATION_INCORRECT_PASSWORD).text
        assert error_text == 'Некорректный пароль'
        

    def test_registration_existing_user_failed(self, driver):
        """
        Попытка регистрации уже существующего пользователя
        Ожидаемый результат: Регистрация не проходит
        """
        driver.find_element(*TestLocators.BUTTON_LOGIN_MAIN).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_REGISTER)
        )
        driver.find_element(*TestLocators.BUTTON_REGISTER).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_SUBMIT)
        )
        
        driver.find_element(*TestLocators.INPUT_NAME).send_keys(TestUser.EXISTING_NAME)
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(TestUser.EXISTING_EMAIL)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(TestUser.EXISTING_PASSWORD)
        driver.find_element(*TestLocators.BUTTON_SUBMIT).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_SUBMIT)
        )
        assert driver.find_element(*TestLocators.BUTTON_SUBMIT).is_displayed() 