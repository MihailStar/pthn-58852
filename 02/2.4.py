# 1
number = int(input())

print(number, number + 1, number + 2, sep="\n")


# 2
print(sum(map(int, (input(), input(), input()))))


# 3
rib_length = int(input())

print(f"Объем = {rib_length ** 3}")
print(f"Площадь полной поверхности = {6 * rib_length ** 2}")


# 4
a, b = (int(input()) for _ in range(2))

print(3 * (a + b) ** 3 + 275 * b**2 - 127 * a - 41)


# 5
n = int(input())

print(f"Следующее за числом {n} число: {n+1}")
print(f"Для числа {n} предыдущее число: {n-1}")


# 6
prices: list[int] = []

try:
    for price in iter(input, ""):
        prices.append(int(price))
except EOFError:
    pass

print(sum(prices) * 3)


# 7
a, b = (int(v) for v in (input(), input()))

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")


# 8
a1, d, n = (int(v) for v in (input() for _ in range(3)))

print(a1 + d * (n - 1))


# 9
n = int(input())

print(*(n * i for i in range(1, 6)), sep="---")
