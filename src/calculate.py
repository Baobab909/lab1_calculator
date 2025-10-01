from src.tokenize import tokenize
from src.rpn import rpn

def calculate(expr: str) -> int | float:
    """
    Пример функции, которая выполняет операцию возведения в степень
    :param expr:  Число, которое будут возводить в степень
    :return: Возвращает число возведенное в степень
    """

    tokens = tokenize(expr)
    result = rpn(tokens)

    return result
