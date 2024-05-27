# 1
n = int(input())

while n > 0:
    last = n % 10
    n //= 10

    print(last)


# 2
# n = int(input())

# while n > 0:
#     last = n % 10
#     n //= 10

#     print(last, end="")

print(input()[::-1])


# 3
# from math import inf

# n = int(input())
# min = inf
# max = -inf

# while n > 0:
#     last = n % 10
#     n //= 10

#     if last < min:
#         min = last

#     if last > max:
#         max = last

# print(f"Максимальная цифра равна {max}")
# print(f"Минимальная цифра равна {min}")

digits = list(map(int, input()))

print(f"Максимальная цифра равна {max(digits)}")
print(f"Минимальная цифра равна {min(digits)}")


# 4
from functools import reduce

digits = list(map(int, input()))

print(sum(digits))
print(len(digits))
print(reduce(lambda acc, digit: acc * digit, digits, 1))
print(sum(digits) / len(digits))
print(digits[0])
print(digits[0] + digits[len(digits) - 1])


# 5
n = int(input())
last = n

while n > 9:
    last = n % 10
    n //= 10

print(last)


# 6
n = int(input())
last = n % 10

while n > 0:
    curr = n % 10
    n //= 10

    if curr != last:
        print("NO")
        break
else:
    print("YES")


# 7
n = int(input())
prev = n % 10

while n > 0:
    curr = n % 10
    n //= 10

    if curr < prev:
        print("NO")
        break

    prev = curr
else:
    print("YES")
