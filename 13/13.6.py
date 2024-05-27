# 1
from typing import Tuple


def get_middle_point(x1: int, y1: int, x2: int, y2: int) -> Tuple[float, float]:
    return ((x1 + x2) / 2, (y1 + y2) / 2)


print(*get_middle_point(*(int(input()) for _ in range(4))))


# 2
from math import pi
from typing import Tuple


def get_circle(radius: float) -> Tuple[float, float]:
    return (2 * pi * radius, pi * radius**2)


print(*get_circle(float(input())))


# 3
from math import sqrt
from typing import Tuple


def solve(a: int, b: int, c: int) -> Tuple[float, float]:
    d = b**2 - 4 * a * c

    if d > 0:
        root1 = (-b - sqrt(d)) / (2 * a)
        root2 = (-b + sqrt(d)) / (2 * a)
        root1, root2 = sorted((root1, root2))
    else:
        root1 = -b / (2 * a)
        root2 = root1

    return (root1, root2)


print(*solve(*(int(input()) for _ in range(3))))
