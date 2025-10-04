from src.tokenize import getToken
from src.operators import UnarOperators
from src.tokenize import isOp
from src.tokenize import isNumber
from src.constants import op_priory
from src.constants import op_right

def infix_to_postfix(expr: str) -> list:
    """
    Преобразует инфиксное выражение в постфиксную запись (RPN)
    :param expr: Математическое выражение в инфиксной записи
    :return: Список токенов в постфиксной записи
    """
    # из инфиксной в обратную польскую
    output = [] # выходная очередь для RPN
    stack = [] # стек для операндов

    # токенизация выражения
    tokens = []
    temp_expr = expr
    while token := getToken(temp_expr): # с помощью функции разбиваем на токены
        tokens.append(token)
        temp_expr = temp_expr[len(token):].lstrip()

    # обработка унарных операторов
    tokens = UnarOperators(tokens)

    # алгоритм сортировочной станции Дейкстры с учетом ассоциативности
    for token in tokens:
        if isNumber(token):
            output.append(token)

        elif token == '(':
            stack.append(token)

        elif token == ')':
            # выталкиваем операторы до открывающей скобки; проверяем, что нашли открывающую скобку и удаляем её из стека
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if not stack:
                raise SyntaxError("Некорректные скобки")
            stack.pop()  # удаляем '('

        elif isOp(token):
            # Для правоассоциативных операторов выталкиваем только операторы с большим приоритетом
            # Для левоассоциативных - операторы с большим или равным приоритетом
            while (stack and stack[-1] != '(' and ((op_right.get(token, False) and
                op_priory.get(stack[-1], 0) > op_priory.get(token, 0)) or (not op_right.get(token, False) and
                op_priory.get(stack[-1], 0) >= op_priory.get(token, 0)))):
                output.append(stack.pop())
            stack.append(token)

    # выталкиваем оставшиеся операторы
    while stack:
        if stack[-1] == '(':
            raise SyntaxError("Некорректные скобки")
        output.append(stack.pop())

    return output
