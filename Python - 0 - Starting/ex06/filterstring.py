import sys


def filter_words(string, n):
    """Filters words from the given string
    that are longer than n characters."""

    words = string.split()

    filtered = [word for word in words if (lambda w: len(w) > n)(word)]

    return filtered


def validate_arguments(args):
    """Validates the input arguments and returns values or raises an error."""

    if len(args) != 3:
        raise AssertionError("AssertionError: the arguments are bad")

    input_string = args[1]

    try:
        n = int(args[2])
    except ValueError:
        raise ValueError("ValueError: the second argument must be an integer")

    return input_string, n


def main():
    """The main function that runs the program."""

    input_string, n = validate_arguments(sys.argv)
    result = filter_words(input_string, n)
    print(result)


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, ValueError) as e:
        print(f"{e}")
