"""Read a square-printing function."""

def print_square(size):
    """Print a square with the # character.

    Args:
        size (int): The length of each side of the square.
    Raises:
        TypeError: If size is not an int type.
        ValueError: If size is negative.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an int type")
    if size < 0:
        raise ValueError("size must be non-negative")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
