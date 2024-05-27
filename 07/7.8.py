# 1
n = int(input())

for _y in range(n):
    for _x in range(3):
        print(n, end=" ")
    print()


# 2
n = int(input())

for y in range(n):
    for _x in range(5):
        print(y + 1, end=" ")
    print()


# 3
n = int(input())

for operand_a in range(1, n + 1):
    for operand_b in range(1, 10):
        print(f"{operand_a} + {operand_b} = {operand_a + operand_b}")
    print("")


# 4
from math import floor

n = int(input())

for i in range(floor(n / 2)):
    print("*" * (i + 1))

for i in range(floor(n / 2), -1, -1):
    print("*" * (i + 1))


# 5
n = int(input())

for x in range(1, n + 1):
    print(str(x) * x)
