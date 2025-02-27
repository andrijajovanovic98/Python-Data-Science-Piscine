import sys


def print_function(message):
    """This function print out the values"""

    punctuation_marks = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    print(f"The text contains {len(message)} characters: ")
    print(sum(1 for c in message if c.isupper()), "upper letters")
    print(sum(1 for c in message if c.islower()), "lower letters")
    print(sum
          (1 for c in message if c in punctuation_marks), "punctuation marks")
    print(sum(1 for c in message if c.isspace()), "spaces")
    print(sum(1 for c in message if c.isdigit()), "digits")


def main():
    """The main function"""

    if len(sys.argv) > 2:
        raise (AssertionError
              ("AssertionError: more then one argument is provided"))

    if len(sys.argv) == 2:
        message = sys.argv[1]
        print_function(message)
    else:
        message = input("What is the text to count?\n") + "\n"
        print_function(message)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"{e}")
