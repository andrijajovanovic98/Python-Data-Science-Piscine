def slice_me(family: list, start: int, end: int) -> list:
    """Slices a 2D list"""

    try:
        if not all(isinstance(row, list) and len(row) ==
                   len(family[0]) for row in family):
            raise ValueError("All rows must be lists of the same length.")

        rows = len(family)
        cols = len(family[0])
        print(f"My shape is ({rows}, {cols})")

        sliced_family = family[start:end]

        new_rows = len(sliced_family)
        print(f"My new shape is : ({new_rows}, {cols})")

        return sliced_family
    except Exception as e:
        print(f"{e}")
