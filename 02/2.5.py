# 1
b1, q, n = (int(d) for d in (input() for _ in range(3)))

print(b1 * q ** (n - 1))


# 2
print(int(input()) // 100)


# 3
n, k = (int(d) for d in (input() for _ in range(2)))

print(*divmod(k, n), sep="\n")


# 4
n = int(input())

print(int(n / 2 if n % 2 == 0 else (n + 1) / 2))


# 5
place = int(input())

print((place - 1) // 4 + 1)


# 6
minutes = int(input())

print(f"{minutes} мин - это {minutes // 60} час {minutes % 60} минут.")


# 7
from functools import reduce

numbers = [int(digit) for digit in input()]

print(f"Сумма цифр = {reduce(lambda x, y: x + y, numbers, 0)}")
print(f"Произведение цифр = {reduce(lambda x, y: x * y, numbers, 1)}")


# 8
a, b, c = input()

print(
    f"{a}{b}{c}",
    f"{a}{c}{b}",
    f"{b}{a}{c}",
    f"{b}{c}{a}",
    f"{c}{a}{b}",
    f"{c}{b}{a}",
    sep="\n",
)


# 9
digits = list(input())

print(
    f"Цифра в позиции тысяч равна {digits[0]}",
    f"Цифра в позиции сотен равна {digits[1]}",
    f"Цифра в позиции десятков равна {digits[2]}",
    f"Цифра в позиции единиц равна {digits[3]}",
    sep="\n",
)
