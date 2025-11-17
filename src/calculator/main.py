import ast
import math
import operator as op
from .exceptions import InvalidExpressionError, DivisionByZeroError

# supported operators
operators = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
}

# supported functions
functions = {
    "sqrt": math.sqrt,
}

# supported constants
constants = {
    "pi": math.pi,
    "e": math.e,
}


def calculate(expression: str) -> int | float:
    """
    Evaluates a mathematical expression from a string.

    Args:
        expression: A string containing the mathematical expression.

    Returns:
        The result of the calculation as an integer or float.

    Raises:
        InvalidExpressionError: For malformed expressions.
        DivisionByZeroError: For division by zero.
    """
    try:
        tree = ast.parse(expression, mode="eval").body
    except (SyntaxError, TypeError):
        raise InvalidExpressionError("Invalid expression")

    try:
        return eval_expr(tree)
    except ZeroDivisionError:
        raise DivisionByZeroError("Division by zero")


def eval_expr(node):
    """
    Recursively evaluate an expression tree.
    """
    if isinstance(node, ast.Constant):
        return node.value
    elif isinstance(node, ast.Name):
        if node.id in constants:
            return constants[node.id]
        else:
            raise InvalidExpressionError(f"Unsupported name: {node.id}")
    elif isinstance(node, ast.BinOp):
        left = eval_expr(node.left)
        right = eval_expr(node.right)
        return operators[type(node.op)](left, right)
    elif isinstance(node, ast.Call):
        if isinstance(node.func, ast.Name) and node.func.id in functions:
            args = [eval_expr(arg) for arg in node.args]
            return functions[node.func.id](*args)

    raise InvalidExpressionError("Unsupported operation")
