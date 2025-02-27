def is_nan(value):
    return isinstance(value, float) and value != value


def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: None {type(object)}")
        return 0

    if is_nan(object):
        print("Cheese: nan <class 'float'>")
        return 0

    if object is False:
        print(f"Fake: {object} {type(object)}")
        return 0

    if object == 0:
        print(f"Zero: {object} {type(object)}")
        return 0

    if object == "":
        print(f"Empty: {object} {type(object)}")
        return 0

    print("Type not Found")
    return 1
