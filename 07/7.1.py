# 1
for _ in range(10):
    print("Python is awesome!")


# 2
string = input()

for _ in range(int(input())):
    print(string)


# 3
for char, number_of_col, number_of_row in (
    ("A", 3, 6),
    ("B", 4, 5),
    ("E", 1, 1),
    ("T", 5, 9),
    ("G", 1, 1),
):
    for _ in range(number_of_row):
        for _ in range(number_of_col):
            print(char, end="")
        print()


# 4
for _ in range(int(input())):
    print("*" * 19)


# 5
s = input()

for i in range(10):
    print(i, s)


# 6
for i in range(int(input()) + 1):
    print(f"Квадрат числа {i} равен {i**2}")


# 7
n = int(input())

for i in range(n):
    print("*" * (n - i))


# 8
m, p, n = (int(input()) for _ in range(3))

for i in range(n):
    print(str(i + 1), str(m * (1 + p / 100) ** i))
