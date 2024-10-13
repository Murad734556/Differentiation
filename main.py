"""Модуль для получения производной от функции"""

import argparse

from functions.function import Function


def diff(function: str, variable: str = "x", **values: dict) -> str:
    """
    Функция, которая берет производную от данной математической функции.

    Args:
        function (str): Функция, от которой получаем производную.
        variable (str, optional): Переменная от которой берем производную.\
            По дефолту 'x'
        **values: Аргументы переменных функции.\
            Если указано, вычисляется производная в заданной точке.

    Returns:
        str: Производная функции.
    """
    if values:
        return str(Function(function).derive(variable, **values))
    return str(Function(function).diff(variable))


def main() -> None:
    """
    Выводит производную от определенной функции
    """
    parser = argparse.ArgumentParser(
        prog="derivative",
        description='Module with functionallity for\
            differentiation mathematical functions.\
            (e.g. [derivative.diff("x^2") -> "2.0*x"],\
                [derivative.diff("x^2", x=2) -> "4.0"])',
    )
    _ = parser.parse_args()

    while True:
        user_input = input("Введите функцию (или 'stop' для выхода): ")
        if user_input.strip().lower() == "stop":
            print("До встречи!")
            break
        result = diff(user_input)
        print(result)


if __name__ == "__main__":
    main()
