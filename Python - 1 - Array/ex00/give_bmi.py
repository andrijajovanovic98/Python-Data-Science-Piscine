def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Computes the BMI values from height and weight lists."""

    try:
        if len(height) != len(weight):
            raise ValueError("Lists must be of the same length")

        for index in range(0, len(height)):
            if (
                not isinstance(height[index], (int, float))
                or not isinstance(weight[index], (int, float))
            ):
                raise TypeError("The values need to be float or int")

        calculated_bmi = []
        for x in range(0, len(height)):
            bmi_value = weight[x] / (height[x] ** 2)
            calculated_bmi.append(bmi_value)

        return (calculated_bmi)

    except Exception as e:
        print(f"Error: {e}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Checks if BMI values exceed the given limit."""

    try:
        for index in range(0, len(bmi)):
            if not isinstance(bmi[index], (int, float)):
                raise ValueError("Only integers or floats")

        if not isinstance(limit, int):
            raise ValueError("BMI list must contain only integers or floats")

        result = []
        for b in bmi:
            if b > limit:
                result.append(True)
            else:
                result.append(False)

        return (result)

    except Exception as e:
        print(f"Error: {e}")
        return []
