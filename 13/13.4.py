# 1
def convert_to_miles(km: float) -> float:
    return km * 0.6214


print(convert_to_miles(int(input())))


# 2
from calendar import monthrange


def get_days(month: int) -> int:
    _first_weekday, number_of_days = monthrange(2023, month)

    return number_of_days


print(get_days(int(input())))


# 3
from typing import List


def get_factors(num: int) -> List[int]:
    divisors: List[int] = []

    for divisor in range(1, num + 1):
        if num % divisor == 0:
            divisors.append(divisor)

    return divisors


print(get_factors(int(input())))


# 4
from typing import List


def get_factors(num: int) -> List[int]:
    divisors: List[int] = []

    for divisor in range(1, num // 2 + 1):
        if num % divisor == 0:
            divisors.append(divisor)

    divisors.append(num)

    return divisors


def number_of_factors(num: int) -> int:
    return len(get_factors(num))


print(number_of_factors(int(input())))


# 5
from typing import List


def find_all(string: str, symbol: str) -> List[int]:
    indexs: List[int] = []

    try:
        indexs.append(string.index(symbol))

        while True:
            indexs.append(string.index(symbol, indexs[-1] + 1))
    except ValueError:
        pass

    return indexs


print(find_all(input(), input()))


# 6
from typing import List


def merge(list1: List[int], list2: List[int]) -> List[int]:
    return sorted([*list1, *list2])


print(merge([int(c) for c in input().split()], [int(c) for c in input().split()]))


# 7
import itertools
from typing import Iterable, List


def quick_merge(*iterables: Iterable[int]) -> List[int]:
    return sorted(itertools.chain(*iterables))


print(
    *quick_merge(
        *([int(digit) for digit in input().split()] for _ in range(int(input())))
    )
)
