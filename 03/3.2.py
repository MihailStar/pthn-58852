# 1
width = 17
height = 4

print("*" * width)
for _ in range(height - 2):
    print("*", " " * (width - 2), "*", sep="")
print("*" * width)


# 2
a, b = (int(d) for d in (input() for _ in range(2)))

print(f"Квадрат суммы {a} и {b} равен {(a + b) ** 2}")
print(f"Сумма квадратов {a} и {b} равна {a**2 + b**2}")


# 3
a, b, c, d = (int(d) for d in (input() for _ in range(4)))

print(a**b + c**d)


# 4
n = input()

print(int(f"{n}") + int(f"{n}{n}") + int(f"{n}{n}{n}"))
