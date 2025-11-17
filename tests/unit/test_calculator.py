import pytest
from calculator.main import calculate
from calculator.exceptions import InvalidExpressionError, DivisionByZeroError


class TestCalculator:
    def test_add(self):
        assert calculate("2 + 3") == 5

    def test_subtract(self):
        assert calculate("5 - 3") == 2

    def test_multiply(self):
        assert calculate("2 * 3") == 6

    def test_divide(self):
        assert calculate("6 / 3") == 2

    def test_exponentiation(self):
        assert calculate("2 ** 3") == 8

    def test_sqrt(self):
        assert calculate("sqrt(9)") == 3

    def test_order_of_operations(self):
        assert calculate("5 * (3 + 2)") == 25
        assert calculate("(10 + 6) / 2") == 8

    def test_constants(self):
        assert calculate("pi") == 3.141592653589793
        assert calculate("e") == 2.718281828459045

    def test_division_by_zero(self):
        with pytest.raises(DivisionByZeroError):
            calculate("5 / 0")

    def test_invalid_expression(self):
        with pytest.raises(InvalidExpressionError):
            calculate("5 * + 3")

    def test_non_numeric_input(self):
        with pytest.raises(InvalidExpressionError):
            calculate("a + b")

    def test_empty_input(self):
        with pytest.raises(InvalidExpressionError):
            calculate("")

    def test_whitespace_input(self):
        with pytest.raises(InvalidExpressionError):
            calculate("   ")
