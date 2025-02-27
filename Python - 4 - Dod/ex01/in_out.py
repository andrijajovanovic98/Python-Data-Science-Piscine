def square(x: int | float) -> int | float:
    """Returns the square of the given number."""
    return (x ** 2)


def pow(x: int | float) -> int | float:
    """Returns the exponentiation of the number by itself (x^x)."""
    return (x**x)


def outer(x: int | float, function) -> object:
    """Takes a number and a function, and returns a
      callable object (inner function)."""
    current_value = x

    def inner() -> float:
        nonlocal current_value
        current_value = function(current_value)
        return current_value

    return inner
