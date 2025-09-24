from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from data import SectionData


class TestConstructorSections:
    """Тесты переключения разделов конструктора"""
    
    def test_navigate_from_buns_to_fillings(self, driver, login):
        """
        Переход из раздела 'Булки' в 'Начинки' (с авторизацией)
        Шаги:
        1. Авторизоваться в системе
        2. Нажать на раздел 'Начинки'
        3. Проверить активацию раздела
        """
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER)
        )
        
        driver.find_element(*TestLocators.SECTION_FILLINGS).click()
        active_section = driver.find_element(*TestLocators.ACTIVE_SECTION).text
        assert active_section == SectionData.NAMES["fillings"]


    def test_navigate_from_sauces_to_fillings(self, driver):
        """
        Переход из 'Соусы' в 'Начинки' (без авторизации)
        """
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_LOGIN_MAIN)
        )
        
        driver.find_element(*TestLocators.SECTION_SAUCES).click()
        driver.find_element(*TestLocators.SECTION_FILLINGS).click()
        active_section = driver.find_element(*TestLocators.ACTIVE_SECTION).text
        assert active_section == SectionData.NAMES["fillings"]


    def test_navigate_from_buns_to_sauces(self, driver, login):
        """
        Переход из 'Булки' в 'Соусы' (с авторизацией)
        """
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER)
        )
        
        driver.find_element(*TestLocators.SECTION_SAUCES).click()
        active_section = driver.find_element(*TestLocators.ACTIVE_SECTION).text
        assert active_section == SectionData.NAMES["sauces"]


    def test_navigate_from_fillings_to_sauces(self, driver):
        """
        Переход из 'Начинки' в 'Соусы' (без авторизации)
        """
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_LOGIN_MAIN)
        )
        
        driver.find_element(*TestLocators.SECTION_FILLINGS).click()
        driver.find_element(*TestLocators.SECTION_SAUCES).click()
        active_section = driver.find_element(*TestLocators.ACTIVE_SECTION).text
        assert active_section == SectionData.NAMES["sauces"]


    def test_navigate_from_sauces_to_buns(self, driver, login):
        """
        Переход из 'Соусы' в 'Булки' (с авторизацией)
        """
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER)
        )
        
        driver.find_element(*TestLocators.SECTION_SAUCES).click()
        driver.find_element(*TestLocators.SECTION_BUNS).click()
        active_section = driver.find_element(*TestLocators.ACTIVE_SECTION).text
        assert active_section == SectionData.NAMES["buns"]
        

    def test_navigate_to_buns_from_fillings(self, driver):
        """
        Переход из 'Начинки' в 'Булки' (без авторизации)
        """
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_LOGIN_MAIN)
        )
        
        driver.find_element(*TestLocators.SECTION_FILLINGS).click()
        driver.find_element(*TestLocators.SECTION_BUNS).click()
        active_section = driver.find_element(*TestLocators.ACTIVE_SECTION).text
        assert active_section == SectionData.NAMES["buns"] 