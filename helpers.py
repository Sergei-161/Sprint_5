import random
import string


def generate_random_email():
    """
    Генерация случайного email в формате имя_фамилия_номер_когорты_рандом@домен
    """
    random_digits = random.randint(100, 999)
    return f'sergei_nechitailo_30_123{random_digits}@yandex.ru'


def generate_random_password():
    """
    Генерация случайного пароля длиной 8-12 символов
    Состоит из букв и цифр
    """
    length = random.randint(8, 12)
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def generate_name():
    """
    Генерация случайного имени и фамилии
    """
    names = ['Aleksey', 'Maria', 'Dmitriy', 'Ekaterina', 'Sergey', 'Olga']
    surnames = ['Ivanov', 'Petrova', 'Sidorov', 'Smirnova', 'Kuznecov', 'Popova']
    return f'{random.choice(names)} {random.choice(surnames)}'