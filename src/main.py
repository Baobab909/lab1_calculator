import sys
from src.calculate import calc


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    print("Калькулятор")
    print("Поддерживает: унарные +/-, **, * / // %, + -")
    print("Введите выражение:")

    for line in sys.stdin:
        line = line.rstrip()
        if line == 'finish <3':
            break
        calc(line)

if __name__ == "__main__":
    main()
