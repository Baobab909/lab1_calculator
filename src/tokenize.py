def isNumber(tok: str) -> bool:
    """
    Проверяет, является ли токен числом
    :param tok: Токен для проверки
    :return: True если токен является числом, False в противном случае
    """
    # проверяю, является ли токен числом
    if not tok: # если токен пустой, то false
        return False
    # убираю точку и минус для проверки
    clean_tok = tok.replace('.', '').replace('-', '')
    # isdigit проверяет состоит ли токен из '0123456789'
    return clean_tok.isdigit() and tok.count('.') <= 1 and tok.count('-') <= 1


def isOp(tok:str) -> bool:
    """
    Проверяет, является ли токен оператором
    :param tok: Токен для проверки
    :return: True если токен является оператором, False в противном случае
    """
    # проверка, что этот токен операция
    return tok in ['+', '-', '*', '/', '//', '%', '**', 'u+', 'u-']


def getToken(expr: str) -> str | None:
    """
    Извлекает следующий токен из строки выражения
    :param expr: Строка с математическим выражением
    :return: Извлеченный токен или None, если строка пустая
    """
    # извлекает токены из строки
    if not expr: # если строка выражения пустая, то возвращаем none
        return None

    # пропускаем пробелы, isspace проверяет на пробелы
    while expr and expr[0].isspace():
        expr = expr[1:]

    if not expr: # если пропуска пробелов строка пустая, то вернем none
        return None

    # проверяем многосимвольные операторы
    if len(expr) >= 2:
        two = expr[:2]
        if two in ['**', '//']:
            return two

    # проверяем числа (если оно цифра, или отрицательное, или дробное)
    if expr[0].isdigit() or (expr[0] == '-' and len(expr) > 1 and (expr[1].isdigit() or expr[1] == '.')):
        i = 0  # индекс для прохода по строке
        dot = False  # флаг, была ли уже точка в числе

        while i < len(expr) and (expr[i].isdigit() or (expr[i] == '.' and not dot and i > 0) or (
                expr[i] == '-' and i == 0)):  # иду, пока есть символ и текущ символ - цифра, или точка, или минус
            if expr[i] == '.':
                dot = True
            i += 1

        return expr[:i]  # возвращаю строку от начала до текущего индекса - это и есть число

    # верну первый символ, если не число и не '**' и не '//'
    return expr[0]
