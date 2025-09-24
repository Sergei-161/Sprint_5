from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators


class TestToPersonalAccount:
    """Тесты навигации в личный кабинет"""
    
    def test_go_to_personal_account(self, driver, login):
        """
        Переход из конструктора в личный кабинет
        Шаги:
        1. Авторизоваться в системе
        2. Нажать кнопку 'Личный кабинет'
        3. Проверить загрузку страницы личного кабинета
        """
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.PROFILE_SECTION)
        )
        assert driver.find_element(*TestLocators.ORDER_HISTORY_SECTION).is_displayed() 