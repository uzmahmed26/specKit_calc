# Quickstart: Basic Calculator Library

This guide explains how to use the `calculator` library.

## Installation

This library is part of the `calculator-project` and does not require separate installation.

## Usage

The primary interface to the library is the `calculate` function, which is located in the `calculator.main` module.

### Function Signature

```python
def calculate(expression: str) -> int | float:
    """
    Evaluates a mathematical expression from a string.

    Args:
        expression: A string containing the mathematical expression.
                    Numbers and operators must be separated by spaces.

    Returns:
        The result of the calculation as an integer or float.

    Raises:
        InvalidExpressionError: For malformed expressions.
        DivisionByZeroError: For division by zero.
    """
```

### Example

```python
from calculator.main import calculate
from calculator.exceptions import InvalidExpressionError, DivisionByZeroError

try:
    # Basic arithmetic
    result1 = calculate("5 + 3")
    print(f"5 + 3 = {result1}")  # Output: 8

    # Expression with parentheses
    result2 = calculate("(10 + 6) / 2")
    print(f"(10 + 6) / 2 = {result2}")  # Output: 8

    # Expression with constants
    result3 = calculate("pi * 2")
    print(f"pi * 2 = {result3}") # Output: 6.283185307

    # Invalid expression
    calculate("5+3")

except InvalidExpressionError as e:
    print(f"Error: {e}") # Output: Error: Numbers and operators must be separated by spaces.

except DivisionByZeroError as e:
    print(f"Error: {e}")

```
