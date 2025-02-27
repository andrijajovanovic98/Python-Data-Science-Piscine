import sys

def is_number(num):
    return num.lstrip('-').isdigit()

if __name__ == "__main__":

    try:
        if len(sys.argv) == 1:
            sys.exit(0)

        if is_number(sys.argv[1]) == False:
            raise AssertionError("AssertionError: argument is not an integer")

        if len(sys.argv) > 2:
            raise AssertionError("AssertionError: more then one argument is provided")

        number = int(sys.argv[1])
        if (number % 2 == 0):
            print("Im Even")
        else:
            print("Im Odd")
    except AssertionError as e:
        print(f"{e}")