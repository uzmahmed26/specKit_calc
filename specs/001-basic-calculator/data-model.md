# Data Model: Basic Calculator

This feature is a self-contained library that processes string inputs and returns numeric outputs.

## Entities

There are no persistent entities or complex data models required for this feature. The data is transient and processed within the `calculate` function.

### Custom Error Classes

The library will define the following custom exception classes for error handling:

-   `CalculatorError`: A base class for all calculator-related errors.
-   `InvalidExpressionError`: Raised for malformed expressions, invalid characters, or incorrect syntax.
-   `DivisionByZeroError`: Raised specifically when a division by zero is attempted.
