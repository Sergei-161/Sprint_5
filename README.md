# SPRINT_5
О проекте
Проект представляет собой набор автоматизированных UI-тестов для сервиса Stellar Burgers - космического фастфуда, где можно собрать и заказать бургер из необычных ингредиентов.

Базовый URL: https://stellarburgers.nomoreparties.site/

Технологии
Python 3.15  - язык программирования

Selenium WebDriver 4.35 - автоматизация браузера

pytest==8.4.1 - фреймворк для тестирования

Chrome Driver - управление браузером Chrome


Структура проекта
text
Sprint_5/
│
├── tests/                          # Директория с тестами
│   ├── test_login.py      # Тесты авторизации
│   ├── test_registration.py        # Тесты регистрации
│   ├── test_logout.py              # Тесты выхода из системы
│   ├── test_to_personal_account.py  # Тесты навигации в ЛК
│   ├── test_from_personal_account_to_constructor.py       # Тесты навигации в конструктор
│   └── test_constructor_sections.py  # Тесты переключения разделов
│
├── conftest.py                     # Фикстуры Pytest
├── locators.py                     # Локаторы элементов
├── data.py                         # Тестовые данные
├── helpers.py                      # Вспомогательные функции
├── requirements.txt                # Зависимости проекта
└── README.md                       # Документация

 Тестовые сценарии
 Тесты авторизации (test_login.py)
 
✅ Вход через кнопку "Войти в аккаунт"
- test_login_via_main_login_button

✅ Вход через "Личный кабинет"  
- test_login_via_personal_account_button

✅ Вход через форму регистрации
- test_login_via_registration_form

✅ Вход через форму восстановления пароля
- test_login_via_password_recovery_form


 Тесты регистрации (test_registration.py)
 
✅ Успешная регистрация нового пользователя
- test_registration_new_account_success_submit

✅ Регистрация с пустым именем
- test_registration_name_is_empty_submit

✅ Регистрация с невалидным email (без @)
- test_registration_invalid_email_no_at_symbol

✅ Регистрация с неполным доменом email
- test_registration_email_no_domain

✅ Регистрация с валидными паролями разной длины
- test_registration_valid_length_password_submit

✅ Регистрация с короткими паролями
- test_registration_invalid_length_password_submit

✅ Проверка сообщения об ошибке пароля
- test_registration_short_password_error

✅ Регистрация существующего пользователя
- test_registration_existing_user_failed


 Тесты выхода из системы (test_logout.py)
 
✅ Успешный выход из личного кабинета
- test_logout_of_personal_account


Тесты навигации (test_to_from *.py)

✅ Переход в личный кабинет
- test_go_to_personal_account

✅ Возврат в конструктор из ЛК через заголовок
- test_return_via_constructor_button

✅ Возврат в конструктор из ЛК через логотип
- test_return_via_logo


Тесты конструктора (test_constructor_sections.py)

✅ Переключение между разделами: Булки ↔ Соусы ↔ Начинки
- test_navigate_from_buns_to_fillings
- test_navigate_from_sauces_to_fillings
- test_navigate_from_buns_to_sauces
- test_navigate_from_fillings_to_sauces
- test_navigate_from_sauces_to_buns
- test_navigate_to_buns_from_fillings


✅ Тесты с авторизацией и без авторизации

Локаторы
Проект использует различные стратегии поиска элементов:

python
# По XPath с contains()
BUTTON_LOGIN_MAIN = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")

# По имени поля
INPUT_PASSWORD = (By.NAME, "Пароль")

# По классу
LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")

# По href
PROFILE_SECTION = (By.XPATH, "//a[contains(@href,'/account/profile')]")
Генерация данных
Для регистрации используются уникальные данные:

python
# Email в формате: имя_фамилия_номер_когорты_3цифры@домен
def generate_random_email():
    return f'sergei_nechitailo_30_123{random.randint(100, 999)}@yandex.ru'

# Случайные пароли длиной 8-12 символов
def generate_random_password():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8, 12))
 Команды для запуска
Основные команды:
bash
# Запуск всех тестов
pytest -v

# Запуск с отчетом
pytest -v --html=report.html

# Запуск только регистрации
pytest tests/test_registration.py -v

# Запуск только авторизации  
pytest tests/test_logo.py -v
Параметры запуска:
bash
# Подробный вывод
pytest -v

# Без захвата вывода (видно print)
pytest -s

# Остановка после первого падения
pytest -x

# Запуск помеченных тестов
pytest -m "registration"
 Особенности реализации
Автономные тесты - каждый тест независим и сам управляет браузером

Явные ожидания - использование WebDriverWait для стабильности

Фикстуры Pytest - правильное управление ресурсами

Случайные данные - уникальные данные для каждого запуска

Разные стратегии локаторов - повышение надежности тестов




