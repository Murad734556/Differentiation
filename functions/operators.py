"""Модуль описания операторов"""

import math
from enum import Enum


class OperatorType(Enum):
    """
    Класс Enum для описания типа оператора.
    """

    BINARY = 0
    PREFIX = 1
    POSTFIX = 2


class Associativity(Enum):
    """
    Класс Enum для описания ассоциативности операторов.
    """

    NONE = 0
    ASSOCIATIVE = 1
    LEFT_ASSOCIATIVE = 2
    RIGHT_ASSOCIATIVE = 3


class Operator:
    """
    Класс для операторов.

    Args:
        operator_type (OperatorType): Тип оператора.
        associativity (Associativity): Ассоциативность оператора.
        priority (int): Приоритет оператора.
        func (callable): Соответствующая функция оператора.
    """

    def __init__(
        self,
        operator_type: OperatorType,
        associativity: Associativity,
        priority: int,
        func: callable,
    ) -> None:
        self._operator_type = operator_type
        self._associativity = associativity
        self._priority = priority
        self._function = func

    @property
    def operator_type(self) -> OperatorType:
        """
        Свойство, содержащее тип оператора.

        Returns:
            OperatorType: Тип оператора.
        """
        return self._operator_type

    @property
    def associativity(self) -> Associativity:
        """
        Свойство, содержащее ассоциативность оператора.

        Returns:
            Associativity: Ассоциативность оператора
        """
        return self._associativity

    @property
    def priority(self) -> int:
        """
        Свойство, содержащее приоритет оператора.

        Returns:
            int: приоритет оператора.
        """
        return self._priority

    def calculate(self, *args) -> float:
        """
        Метод, вычисляющий результат оператора с заданными аргументами.

        Args:
            *args: Аргументы для оператора.

        Returns:
            float: Результат.
        """
        return self._function(*args)


OPERATORS = {
    "+": Operator(
        OperatorType.BINARY, Associativity.ASSOCIATIVE, 0, lambda x, y: x + y
    ),
    "-": Operator(
        OperatorType.BINARY, Associativity.LEFT_ASSOCIATIVE, 0, lambda x, y: x - y
    ),
    "unary-": Operator(OperatorType.PREFIX, Associativity.NONE, 1, lambda x: -x),
    "*": Operator(
        OperatorType.BINARY, Associativity.ASSOCIATIVE, 1, lambda x, y: x * y
    ),
    "/": Operator(
        OperatorType.BINARY, Associativity.LEFT_ASSOCIATIVE, 1, lambda x, y: x / y
    ),
    "^": Operator(
        OperatorType.BINARY, Associativity.RIGHT_ASSOCIATIVE, 2, lambda x, y: x**y
    ),
    "sqrt": Operator(OperatorType.PREFIX, Associativity.NONE, 3, math.sqrt),
    "exp": Operator(OperatorType.PREFIX, Associativity.NONE, 3, math.exp),
    "ln": Operator(OperatorType.PREFIX, Associativity.NONE, 3, math.log),
    "sin": Operator(OperatorType.PREFIX, Associativity.NONE, 3, math.sin),
    "cos": Operator(OperatorType.PREFIX, Associativity.NONE, 3, math.cos),
    "tg": Operator(OperatorType.PREFIX, Associativity.NONE, 3, math.tan),
}

CONSTANTS = {
    "e": math.e,
    "pi": math.pi,
    "tau": math.tau,
    "phi": (1 + math.sqrt(5)) / 2,
}
