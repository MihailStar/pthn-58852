# 1
a, b = float(input()), float(input())
s = a * b / 2

print(s)


# 2
s, v1, v2 = (float(input()) for _ in range(3))

# @tutorial https://stepik.org/lesson/265105/step/4?discussion=3415760&unit=246053
print(s / (v1 + v2))


# 3
n = float(input())

print("Обратного числа не существует" if n == 0 else str(1 / n))


# 4
f = float(input())
c = 5 / 9 * (f - 32)

print(c)


# 5
n = int(input())
a = 0.0

if n > 0:
    a += 10.5
if n > 1:
    a += 10.5
if n > 2:
    a += (n - 2) * 4

print(a)


# 6
n = float(input())

# @tutorial https://stepik.org/lesson/265105/step/8?discussion=1603405&unit=246053
print(int((n * 10) % 10))


# 7
from math import modf

n = float(input())

# print(n % 1)
# print(n - int(n))
print(modf(n)[0])


# 8
numbers = [int(input()) for _ in range(5)]

print(f"Наименьшее число = {min(numbers)}")
print(f"Наибольшее число = {max(numbers)}")


# 9
numbers = [int(input()) for _ in range(3)]

print(*sorted(numbers, reverse=True), sep="\n")


# 10
digits = sorted(map(int, input()))

print("Число", "интересное" if digits[2] - digits[0] == digits[1] else "неинтересное")


# 11
from functools import reduce

numbers = [float(input()) for _ in range(5)]

print(reduce(lambda acc, number: acc + abs(number), numbers, 0))


# 12
p1, p2, q1, q2 = (float(input()) for _ in range(4))

print(abs(p1 - q1) + abs(p2 - q2))
