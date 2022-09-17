import re
import json
from typing import Any


def get_login() -> list[str]:
    """
    Загружает данные о студентах из файла
    :return: Выводит список логинов студентов
    """
    list_login = []
    with open('student.json') as file:
        contents: Any = json.load(file)
    for i in contents:
        list_login.append(i['login'])
    return list_login


def correct_login(list_login: list[str]):
    """
    Проверка логина по регулярному выражению
    :param list_login: Список логинов студентов
    :return: Возвращаем строку с логином и его корректностью
    """
    response = re.compile(r'^[a-z][A-Za-z0-9]+[\W |_]{1}[a-z0-9]$')
    for login in list_login:
        is_correct_login = response.search(login)
        k = bool(is_correct_login)
        print(f' Логин {login} {"корректен" if k else "не корректен"}')


def main():
    correct_login(get_login())


if __name__ == '__main__':
    main()
