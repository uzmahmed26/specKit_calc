class CalculatorError(Exception):
    """Base class for exceptions in the calculator."""

    pass


class InvalidExpressionError(CalculatorError):
    """Raised when the input expression is invalid."""

    pass


class DivisionByZeroError(CalculatorError):
    """Raised when division by zero is attempted."""

    pass
