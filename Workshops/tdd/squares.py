def is_valid_square(sides: list[int]) -> bool:
    """Returns True if sides form a valid square"""
    return True if all(x == sides[0] for x in sides) and len(sides) == 4 else False
