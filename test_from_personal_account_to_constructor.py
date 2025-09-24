from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators


class TestFromPersonalAccountToConstructor:
    """Тесты навигации в конструктор"""
    
    def test_return_via_constructor_button(self, driver, login):
        """
        Возврат из ЛК в конструктор через заголовок
        Шаги:
        1. Авторизоваться и перейти в ЛК
        2. Нажать кнопку 'Конструктор' в заголовке
        3. Проверить возврат на главную страницу
        """
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.PROFILE_SECTION)
        )
        
        driver.find_element(*TestLocators.BUTTON_CONSTRUCTOR_HEADER).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER)
        )
        assert driver.find_element(*TestLocators.BUTTON_MAKE_ORDER).is_displayed()
        

    def test_return_via_logo(self, driver, login):
        """
        Возврат из ЛК в конструктор через логотип
        """
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.PROFILE_SECTION)
        )
        
        driver.find_element(*TestLocators.LOGO).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER)
        )
        assert driver.find_element(*TestLocators.BUTTON_MAKE_ORDER).is_displayed()