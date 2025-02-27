class calculator:
    """Performs vector operations."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculates and prints the dot product."""
        result = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot Product: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Calculates and prints the vector sum."""
        result = [float(x + y) for x, y in zip(V1, V2)]
        print(f"Vector Addition: {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Calculates and prints the vector difference."""
        result = [float(x - y) for x, y in zip(V1, V2)]
        print(f"Vector Subtraction: {result}")
