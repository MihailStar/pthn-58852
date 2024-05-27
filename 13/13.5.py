# 1
def is_valid_triangle(side1: int, side2: int, side3: int) -> bool:
    return side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1


print(is_valid_triangle(int(input()), int(input()), int(input())))


# 2
def is_prime(num: int) -> bool:
    """@tutorial https://github.com/mihailstar/pthn-urfu-pyap/blob/master/09/9.2.py#L81"""

    if num < 2:
        return False

    for divisor in range(2, int(num**0.5) + 1):
        if num % divisor == 0:
            return False

    return True


print(is_prime(int(input())))


# 3
def is_prime(num: int) -> bool:
    """@tutorial https://github.com/mihailstar/pthn-urfu-pyap/blob/master/09/9.2.py#L81"""

    if num < 2:
        return False

    for divisor in range(2, int(num**0.5) + 1):
        if num % divisor == 0:
            return False

    return True


def get_next_prime(num: int) -> int:
    i = 1

    while True:
        next_num = num + i

        if is_prime(next_num):
            return next_num

        i += 1


print(get_next_prime(int(input())))


# 4
from re import search


def is_password_good(password: str) -> bool:
    return (
        len(password) > 7
        and search(r"[A-Z]", password) is not None
        and search(r"[a-z]", password) is not None
        and search(r"\d", password) is not None
    )


print(is_password_good(input()))


# 5
def is_one_away(word1: str, word2: str) -> bool:
    if not len(word1) == len(word2):
        return False

    counter = 0

    for char1, char2 in zip(word1, word2):
        if not char1 == char2:
            counter += 1

    return counter == 1


print(is_one_away(input(), input()))


# 6
from re import sub


def is_palindrome(text: str) -> bool:
    normalized_text = sub(r"[ ,.!?-]", "", text.lower())

    return normalized_text == "".join(reversed(list(normalized_text)))


print(is_palindrome(input()))


# 7
def is_prime(num: int) -> bool:
    """@tutorial https://github.com/mihailstar/pthn-urfu-pyap/blob/master/09/9.2.py#L81"""

    if num < 2:
        return False

    for divisor in range(2, int(num**0.5) + 1):
        if num % divisor == 0:
            return False

    return True


def is_valid_password(password: str) -> bool:
    parts = password.split(":")

    if len(parts) != 3:
        return False

    return (
        parts[0] == parts[0][::-1]
        and is_prime(int(parts[1]))
        and int(parts[2]) % 2 == 0
    )


print(is_valid_password(input()))


# 8
def is_correct_bracket(text: str) -> bool:
    while True:
        index = text.find("()")

        if index == -1:
            break

        text = text[:index] + text[index + 2 :]

    return len(text) == 0


print(is_correct_bracket(input()))


# 9
def convert_to_python_case(text: str) -> str:
    result = text[0].lower()

    for index in range(1, len(text)):
        char = text[index]
        result += f"_{char.lower()}" if char.isupper() else char

    return result


print(convert_to_python_case(input()))
