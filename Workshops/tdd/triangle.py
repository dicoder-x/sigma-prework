def is_valid_triangle(angles: list[int]) -> bool:
    return True if sum(angles) == 180 else False


def is_valid_equilateral_triangle(angles: list[int]) -> bool:
    return True if all(x == angles[0] for x in angles) else False


def get_triangle_type(angles: list[int]) -> str:
    if angles[0] == angles[1] == angles[2]:
        return "equilateral"
    elif angles[0] == angles[1] or angles[1] == angles[2] or angles[0] == angles[2]:
        return "isoceles"
    else:
        return "not triangles"
