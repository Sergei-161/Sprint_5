from selenium.webdriver.common.by import By


class TestLocators:
    """
    Локаторы для элементов страницы Stellar Burgers
    Используются различные стратегии поиска для надежности
    """
    
    # === РЕГИСТРАЦИЯ ===
    INPUT_NAME = (By.XPATH, "//label[contains(text(),'Имя')]/following-sibling::input")
    INPUT_EMAIL = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")
    INPUT_PASSWORD = (By.NAME, "Пароль")  # По имени поля
    BUTTON_SUBMIT = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
    NOTIFICATION_INCORRECT_PASSWORD = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")
    BUTTON_LOGIN_IN_REG_FORM = (By.XPATH, "//a[contains(text(),'Войти')]")
    
    # === АВТОРИЗАЦИЯ ===
    BUTTON_LOGIN_MAIN = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")
    INPUT_EMAIL_AUTH = (By.NAME, "name")  # По имени поля
    INPUT_PASSWORD_AUTH = (By.NAME, "Пароль")  # По имени поля
    BUTTON_LOGIN = (By.XPATH, "//button[contains(text(),'Войти')]")
    BUTTON_REGISTER = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")
    
    # === ВОССТАНОВЛЕНИЕ ПАРОЛЯ ===
    BUTTON_FORGOT_PASSWORD = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")
    BUTTON_LOGIN_PASSWORD_RECOVERY = (By.XPATH, "//a[contains(text(),'Войти')]")
    
    # === ЛИЧНЫЙ КАБИНЕТ ===
    PROFILE_SECTION = (By.XPATH, "//a[contains(@href,'/account/profile')]")
    ORDER_HISTORY_SECTION = (By.XPATH, "//a[contains(@href,'/account/order-history')]")
    BUTTON_LOGOUT = (By.XPATH, "//button[contains(text(),'Выход')]")
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    
    # === ГЛАВНАЯ СТРАНИЦА ===
    BUTTON_MAKE_ORDER = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    BUTTON_CONSTRUCTOR_HEADER = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")  # По классу
    
    # === КОНСТРУКТОР ===
    SECTION_BUNS = (By.XPATH, "//span[contains(text(),'Булки')]")
    SECTION_SAUCES = (By.XPATH, "//span[contains(text(),'Соусы')]")
    SECTION_FILLINGS = (By.XPATH, "//span[contains(text(),'Начинки')]")
    ACTIVE_SECTION = (By.CLASS_NAME, "tab_tab_type_current__2BEPc")  # По классу активного элемента