from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators


class TestLogout:
    """Тесты выхода из системы"""
    
    def test_logout_of_personal_account(self, driver, login):
        """
        Успешный выход из личного кабинета
        Шаги:
        1. Авторизоваться в системе
        2. Перейти в личный кабинет
        3. Нажать кнопку 'Выход'
        4. Проверить возврат на страницу авторизации
        """
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER)
        )
        
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.PROFILE_SECTION)
        )
        
        driver.find_element(*TestLocators.BUTTON_LOGOUT).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_LOGIN)
        )
        assert driver.find_element(*TestLocators.BUTTON_LOGIN).is_displayed() 