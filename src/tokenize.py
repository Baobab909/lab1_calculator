from src.token import Token

def tokenize(expr: str) -> list[Token]:
    """
    Пример функции, которая выполняет операцию возведения в степень
    :param target:  Число, которое будут возводить в степень
    :param input_two: Степень в которую будут возводить число
    :return: Возвращает число возведенное в степень
    """

    tokens: list[Token] = []

    tokens.append(("+", None))
    tokens.append(("num", 1))

    return tokens
