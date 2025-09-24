from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators
from data import TestUser


class TestLogin:
    """Тесты авторизации в системе Stellar Burgers"""
    
    def test_login_via_main_login_button(self, driver):
        """
        Успешный вход через кнопку 'Войти в аккаунт' на главной странице
        Шаги:
        1. Открыть главную страницу
        2. Нажать кнопку 'Войти в аккаунт'
        3. Заполнить валидные email и пароль
        4. Нажать кнопку 'Войти'
        5. Проверить успешную авторизацию
        """
        driver.find_element(*TestLocators.BUTTON_LOGIN_MAIN).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_REGISTER)
        )
        
        driver.find_element(*TestLocators.INPUT_EMAIL_AUTH).send_keys(TestUser.EXISTING_EMAIL)
        driver.find_element(*TestLocators.INPUT_PASSWORD_AUTH).send_keys(TestUser.EXISTING_PASSWORD)
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER)
        )
        assert driver.find_element(*TestLocators.BUTTON_MAKE_ORDER).is_displayed()


    def test_login_via_personal_account_button(self, driver):
        """
        Успешный вход через кнопку 'Личный кабинет'
        """
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_REGISTER)
        )
        
        driver.find_element(*TestLocators.INPUT_EMAIL_AUTH).send_keys(TestUser.EXISTING_EMAIL)
        driver.find_element(*TestLocators.INPUT_PASSWORD_AUTH).send_keys(TestUser.EXISTING_PASSWORD)
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER)
        )
        assert driver.find_element(*TestLocators.BUTTON_MAKE_ORDER).is_displayed()


    def test_login_via_registration_form(self, driver):
        """
        Успешный вход через форму регистрации
        """
        driver.find_element(*TestLocators.BUTTON_LOGIN_MAIN).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_REGISTER)
        )
        
        driver.find_element(*TestLocators.BUTTON_REGISTER).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_SUBMIT)
        )
        
        driver.find_element(*TestLocators.BUTTON_LOGIN_IN_REG_FORM).click()
        
        driver.find_element(*TestLocators.INPUT_EMAIL_AUTH).send_keys(TestUser.EXISTING_EMAIL)
        driver.find_element(*TestLocators.INPUT_PASSWORD_AUTH).send_keys(TestUser.EXISTING_PASSWORD)
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER)
        )
        assert driver.find_element(*TestLocators.BUTTON_MAKE_ORDER).is_displayed()
        

    def test_login_via_password_recovery_form(self, driver):
        """
         Успешный вход через форму восстановления пароля
        """
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_REGISTER)
        )
        
        driver.find_element(*TestLocators.BUTTON_FORGOT_PASSWORD).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_LOGIN_PASSWORD_RECOVERY)
        )
        
        driver.find_element(*TestLocators.BUTTON_LOGIN_PASSWORD_RECOVERY).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_REGISTER)
        )
        driver.find_element(*TestLocators.INPUT_EMAIL_AUTH).send_keys(TestUser.EXISTING_EMAIL)
        driver.find_element(*TestLocators.INPUT_PASSWORD_AUTH).send_keys(TestUser.EXISTING_PASSWORD)
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER)
        )
        assert driver.find_element(*TestLocators.BUTTON_MAKE_ORDER).is_displayed()