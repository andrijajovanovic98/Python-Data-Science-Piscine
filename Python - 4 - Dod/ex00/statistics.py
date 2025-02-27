def findMiddle(lst):
    """Return the middle from the list"""
    middle = len(lst) // 2

    if len(lst) % 2 != 0:
        return lst[middle]
    else:
        return (lst[middle] + lst[middle - 1]) / 2


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Computes various statistical measures based on given *args and **kwargs.
"""
    try:
        if not args:
            print("ERROR")
            return

        valid_metrics = {"mean", "median", "quartile", "std", "var"}
        requested_metrics = {
            value for value in kwargs.values() if value in valid_metrics}

        if not requested_metrics:
            print("ERROR")
            return

        if not kwargs:
            print("ERROR")
            return

        if "mean" in kwargs.values():
            mean_value = sum(args) / len(args)
            print(f"Mean: {mean_value}")

        if "median" in kwargs.values():
            median_value = sorted(args)
            median_value = findMiddle(median_value)
            print(f"Median: {median_value}")

        if "std" in kwargs.values():
            avarage = sum(args) / len(args)
            remeinde = []

            for x in args:
                remeinde.append((x - avarage)**2)
            another_number = sum(remeinde) / len(args)
            sqrt = another_number ** 0.5
            print(f"std: {sqrt}")

        if "var" in kwargs.values():
            avarage = sum(args) / len(args)
            remeinde = []

            for x in args:
                remeinde.append((x - avarage)**2)
            another_number = sum(remeinde) / len(args)
            print(f"var: {another_number}")

        if "quartile" in kwargs.values():
            sorted_args = sorted(args)
            middle = len(sorted_args) // 2

            lower_half = sorted_args[:middle]
            upper_half = sorted_args[middle:]

            def get_middle(lst):
                return lst[len(lst) // 2]
            q1 = float(get_middle(lower_half))
            q3 = float(get_middle(upper_half))

            print(f"Quartile: [{q1}, {q3}]")

    except Exception as e:
        print(f"Unexcepted error: {e}")
