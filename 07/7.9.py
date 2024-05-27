# 1
a, b = map(int, (input(), input()))


def get_divisors(number: int) -> list[int]:
    divisors: list[int] = []

    for divisor in range(1, number + 1):
        if number % divisor == 0:
            divisors.append(divisor)

    return divisors


number_to_sum_divisors: dict[int, int] = {}

for number in range(a, b + 1):
    number_to_sum_divisors[number] = sum(get_divisors(number))

items = sorted(number_to_sum_divisors.items(), key=lambda item: item[1])
max_sum_divisors = items[-1][1]
max_number_and_max_sum_divisors = sorted(
    filter(lambda item: item[1] == max_sum_divisors, items), key=lambda item: item[0]
)[-1]

print(*max_number_and_max_sum_divisors)


# 2
n = int(input())
counter = 0

for y in range(1, n + 1):
    for x in range(y):
        counter += 1
        print(counter, end=" ")

    print()


# 3
for y in range(1, int(input()) + 1):
    for x in range(1, y + 1):
        print(x, end="")

    for x in range(y - 1, 0, -1):
        print(x, end="")

    print()


# 4
for n in range(1, int(input()) + 1):
    counter = 0

    for d in range(1, n + 1):
        if n % d == 0:
            counter += 1

    print(n, "+" * counter, sep="")


# 5
digits = input()
digital_root = int(digits)

while len(digits) > 1:
    digital_root = 0

    for digit in digits:
        digital_root += int(digit)

    digits = str(digital_root)

print(digital_root)


# 6
from math import factorial

n = int(input())
total = 0

for num in range(1, n + 1):
    total += factorial(num)

print(total)


# 7
a, b = map(int, (input(), input()))


def is_prime(num: int) -> bool:
    """@tutorial https://github.com/mihailstar/pthn-100707/blob/master/09/9.2.py#L81"""

    if num < 2:
        return False

    for divisor in range(2, int(num**0.5) + 1):
        if num % divisor == 0:
            return False

    return True


for num in range(a, b + 1):
    if is_prime(num):
        print(num)
