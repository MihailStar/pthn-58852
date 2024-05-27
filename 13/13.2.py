# 1
from math import floor


def draw_triangle(fill: str, base: int) -> None:
    for i in range(floor(base / 2)):
        print(fill * (i + 1))

    for i in range(floor(base / 2), -1, -1):
        print(fill * (i + 1))


draw_triangle(input(), int(input()))


# 2
def print_fio(name: str, surname: str, patronymic: str) -> None:
    print(f"{surname[0]}{name[0]}{patronymic[0]}".upper())


print_fio(input(), input(), input())


# 3
def print_digit_sum(num: int) -> None:
    print(sum(map(int, str(num))))


print_digit_sum(int(input()))
