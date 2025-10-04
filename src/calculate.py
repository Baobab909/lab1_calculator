from src.tokenize import isNumber
from src.tokenize import isOp
from src.operators import Operation
from src.rpn import infix_to_postfix


def Compute(postfix_tokens):
    """
    Вычисляет выражение в постфиксной записи (RPN)
    :param postfix_tokens: Список токенов в постфиксной записи
    :return: Стек с результатом вычисления
    """
    # вычисление выражения в RPN записи
    stack = []

    for token in postfix_tokens:
        if isNumber(token):
            # преобразуем в int или float
            if '.' in token:
                num = float(token)
            else:
                num = int(token)
            stack.append(num)

        elif isOp(token):
            # унарные операции
            if token in ['u+', 'u-']:
                if not stack:
                    raise SyntaxError("Недостаточно операндов для унарного оператора")
                op1 = stack.pop()
                result = Operation(token, op1)
                stack.append(result) # извлекаю один операнд, применяю операцию, результат в стек

            # бинарные операции
            else:
                if len(stack) < 2:
                    raise SyntaxError(f"Недостаточно операндов для операции {token}")
                op2 = stack.pop()
                op1 = stack.pop()
                result = Operation(token, op1, op2)
                stack.append(result)
    return stack


def calc(expr: str) -> None:
    """
    Основная функция вычисления математического выражения
    :param expr: Строка с математическим выражением для вычисления
    :return: None (результат выводится в консоль)
    """
    # основная функция вычисления
    try:
        if not expr.strip():
            print("Пустое выражение")
            return

        # преобразуем инфиксную запись в постфиксную
        postfix_tokens = infix_to_postfix(expr)

        # вычисляем постфиксное выражение
        stack = Compute(postfix_tokens)

        # проверяем результат
        if len(stack) == 1:
            result = stack[0]
            # форматируем вывод
            if isinstance(result, int):
                print(f"Результат: {result}")
            else:
                # убираем лишние нули после точки
                formatted = f"{result:.10f}"
                formatted = formatted.rstrip('0').rstrip('.') if '.' in formatted else formatted
                print(f"Результат: {formatted}")
        else:
            print("Ошибка")

    except Exception as e:
        print(f"Ошибка: {e}")
