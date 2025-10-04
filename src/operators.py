def Operation(op: str, op1: int | float, op2=None) -> int | float | SyntaxError:
    """
    Выполняет математическую операцию над операндами
    :param op: Оператор для выполнения
    :param op1: Первый операнд
    :param op2: Второй операнд (для бинарных операций)
    :return: Результат выполнения операции
    """
    try: # прописываем операции и ошибки
        if op == 'u+':
            return op1
        elif op == 'u-':
            return -op1

        elif op == '+':
            return op1 + op2
        elif op == '-':
            return op1 - op2
        elif op == '*':
            return op1 * op2
        elif op == '/':
            if op2 == 0:
                raise ZeroDivisionError("Нельзя делить на ноль")
            return op1 / op2
        elif op == '//':
            if op2 == 0:
                raise ZeroDivisionError("Нельзя делить на ноль")
            if not isinstance(op1, int) or not isinstance(op2, int):
                raise TypeError("Операция // допустима только для целых чисел")
            return op1 // op2
        elif op == '%':
            if op2 == 0:
                raise ZeroDivisionError("Нельзя делить по модулю на ноль")
            if not isinstance(op1, int) or not isinstance(op2, int):
                raise TypeError("Операция % допустима только для целых чисел")
            return op1 % op2
        elif op == '**':
            return op1 ** op2
        else:
            raise SyntaxError(op)

    except (ZeroDivisionError, TypeError) as e:
        raise e
    except Exception as e: # другие ошибки пойдут в ValueError
        raise ValueError("Ошибка при выполнении", op,":", e)


def UnarOperators(tokens: list) -> list:
    """
    Обрабатывает унарные операторы в списке токенов
    :param tokens: Список токенов для обработки
    :return: Обработанный список токенов с унарными операторами
    """
    # обработка унарных операторов
    p = []
    i = 0

    while i < len(tokens): # проходим по токенам
        token = tokens[i]
        if token in ['+', '-']:
            # проверяем, является ли оператор унарным
            if i == 0 or tokens[i - 1] in ['(', '+', '-', '*', '/', '//', '%', '**']:
                if token == '+':
                    p.append('u+')
                else:
                    p.append('u-')
            else:
                p.append(token)
        else:
            p.append(token)
        i += 1

    return p
