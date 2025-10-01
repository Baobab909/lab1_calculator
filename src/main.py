from src.calculate import calculate


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    while expr := input("Ввод выражения: "):
        result = calculate(expr)
        print(result)

if __name__ == "__main__":
    main()
