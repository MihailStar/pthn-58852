# 1
n = int(input())
s = 0

while n > 0:
    if n % 2 == 0:
        s += n % 10

    n //= 10

print(s)


# 2
count = 0
maximum = -1e12

for _ in range(8):
    n = int(input())

    if n % 4 == 0:
        count += 1

        if n > maximum:
            maximum = n

if count > 0:
    print(count)
    print(maximum)
else:
    print("NO")


# 3
count = 0
maximum = -1e8

for _ in range(4):
    n = int(input())

    if n % 2 == 1:
        count += 1

        if n > maximum:
            maximum = n

if count > 0:
    print(count)
    print(maximum)
else:
    print("NO")


# 4
n = int(input())
width = 19

print("*" * width)
for _ in range(n - 2):
    print("*", "*", sep=" " * (width - 2))
print("*" * width)


# 5
print(input()[2])


# 6
# from functools import reduce
from math import prod

digits = [int(digit) for digit in input()]

print(digits.count(3))
print(digits.count(digits[-1]))
print(sum(1 for digit in digits if digit % 2 == 0))
print(sum(digit for digit in digits if digit > 5))
# print(
#     reduce(lambda acc, digit: acc * digit, (digit for digit in digits if digit > 7), 1)
# )
print(prod(digit for digit in digits if digit > 7))
print(sum(1 for digit in digits if digit == 0 or digit == 5))
