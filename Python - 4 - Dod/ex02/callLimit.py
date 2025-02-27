from typing import Callable, Any


def callLimit(limit: int) -> Callable:
    """
    A decorator that limits the number of times a function can be called.
    """
    def callLimiter(function: Callable) -> Callable:
        """Wrapper function to enforce call limit."""
        count = 0

        def limit_function(*args: Any, **kwargs: Any):
            """Inner function to track calls."""
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwargs)
            else:
                print(f"Error: {function} call too many times")
                return None

        return limit_function

    return callLimiter
