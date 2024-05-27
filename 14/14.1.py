# 1
def draw_triangle() -> None:
    for i in range(8):
        print(
            ("*" * i).rjust(15 // 2, " "),
            "*",
            ("*" * i),
            sep="",
        )


draw_triangle()


# 2
def get_shipping_cost(quantity: int) -> int:
    result = 0

    if quantity > 0:
        result += 1000

    for _ in range(quantity - 1):
        result += 120

    return result


print(get_shipping_cost(int(input())))


# 3
from math import factorial


def compute_binom(n: int, k: int) -> int:
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


print(compute_binom(int(input()), int(input())))


# 4
def number_to_words(num: int) -> str:
    d = {
        1: "один",
        2: "два",
        3: "три",
        4: "четыре",
        5: "пять",
        6: "шесть",
        7: "семь",
        8: "восемь",
        9: "девять",
        10: "десять",
        11: "одиннадцать",
        12: "двенадцать",
        13: "тринадцать",
        14: "четырнадцать",
        15: "пятнадцать",
        16: "шестнадцать",
        17: "семнадцать",
        18: "восемнадцать",
        19: "девятнадцать",
        20: "двадцать",
        30: "тридцать",
        40: "сорок",
        50: "пятьдесят",
        60: "шестьдесят",
        70: "семьдесят",
        80: "восемьдесят",
        90: "девяносто",
    }

    if num in d:
        return d[num]
    else:
        tens = num // 10 * 10
        ones = num % 10
        return f"{d[tens]} {d[ones]}"


print(number_to_words(int(input())))


# 5
print(
    {
        "en": [
            "january",
            "february",
            "march",
            "april",
            "may",
            "june",
            "july",
            "august",
            "september",
            "october",
            "november",
            "december",
        ],
        "ru": [
            "январь",
            "февраль",
            "март",
            "апрель",
            "май",
            "июнь",
            "июль",
            "август",
            "сентябрь",
            "октябрь",
            "ноябрь",
            "декабрь",
        ],
    }[input()][int(input()) - 1]
)


# 6
def is_magic(date: str) -> bool:
    d, m, y = date.split(".")

    return int(d) * int(m) == int(y[2:])


print(is_magic(input()))


# 7
from typing import Dict


def is_pangram(text: str) -> bool:
    char_to_counter: Dict[str, int] = dict()

    for code in range(ord("a"), ord("z") + 1):
        char = chr(code)
        char_to_counter[char] = 0

    for char in text:
        if char == " ":
            continue

        char_to_counter[char.lower()] += 1

    for char in char_to_counter:
        if char_to_counter[char] == 0:
            return False

    return True


print(is_pangram(input()))
