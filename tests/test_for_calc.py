from src.calculate import calc

class TestCalculator:
    def test_baza(self):
        """
        Тест для простых выражений
        """
        assert calc('555 + 5') == 560
        assert calc('494 - 33') == 461
        assert calc('20 * 5') == 100
        assert calc('44 / 2') == 22
        assert calc('30 // 2') == 15
        assert calc('77 % 2') == 1
        # тесты для возведения в степень
        assert calc('0 ** 0')
        assert calc('45 ** 2') == 2025
        assert calc('4 ** 0.5') == 2
        #assert calc('5 ** 2 ** 3') == 390625

    def test_unary(self):
        """
        Тест для унарных операций
        """
        assert calc('+7') == 7
        assert calc('-7') == -7
        assert calc('5 + (-2)') == 3
        assert calc('5 - (+2)') == 3

    def test_priory(self):
        """
        Тест для приоритета операций и скобок
        """
        assert calc('(4 + 5) * 3') == 27
        assert calc('12 + 5 * 11') == 67
        assert calc('(2 + 11) * (4 - 3) // 2') == 6
        assert calc('4 * (11 + 4)') == 60
        assert calc('10 - 4 / 2') == 8
        #assert calc('48 / 6 / 2') == 4
    def test_hard(self):
        assert calc('((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1))') == 5
        assert calc('3 + 4 * 2 / (1 - 5) ** 2') == 3.5
        assert calc('2 ** (1 + 2) * 3 - 10 / (4 + 1)') == 22
        assert calc('(-1) * (2 + 3 * (4 - 6 / 3)) - 5') == -13
        assert calc('')
