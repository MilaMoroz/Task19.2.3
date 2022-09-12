import pytest
from app.calculator import Calculator


class TestCalc: # тестируем весь калькулятор нажатием на зелёную стрелку
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):  # умножение
        assert self.calc.multiply(self, 3, 3) == 9 # положительный тест

    def test_division_calculate_correctly(self):  # деление
        assert self.calc.division(self, 9, 3) == 3 # положительный тест

    def test_subtraction_calculate_correctly(self):  # вычитание
        assert self.calc.subtraction(self, 6, 2) == 4 # положительный тест

    def test_adding_calculate_correctly(self):  # сложение
        assert self.calc.adding(self, 7, 2) == 9 # положительный тест

    def test_multiply_calculation_failed(self):  # умножение
        assert self.calc.multiply(self, 2, 2) == 5  # негативный тест

    def test_division_calculation_failed(self):  # деление
        assert self.calc.division(self, 10, 2) == 6  # негативный тест

    def test_subtraction_calculation_failed(self):  # вычитание
        assert self.calc.subtraction(self, 9, 3) == 4  # негативный тест

    def test_adding_calculation_failed(self):  # сложение
        assert self.calc.adding(self, 4, 2) == 5  # негативный тест