# 1
a, b = (int(input()) for _ in range(2))
counter = 0

for i in range(a, b + 1):
    cube = i**3
    end = cube % 10

    if end == 4 or end == 9:
        counter += 1

print(counter)


# 2
numbers = (int(input()) for _ in range(int(input())))

print(sum(numbers))


# 3
from math import log

n = int(input())
temp = 1

for i in range(2, n + 1):
    temp += 1 / i

print(temp - log(n))


# 4
n = int(input())
counter = 0

for i in range(1, n + 1):
    square = i**2
    end = square % 10

    if end in (2, 5, 8):
        counter += i

print(counter)


# 5
from math import factorial

print(factorial(int(input())))


# 6
from functools import reduce

print(
    reduce(
        lambda n1, n2: n1 * n2,
        filter(lambda n: n != 0, (int(input()) for _ in range(10))),
        1,
    )
)


# 7
n = int(input())
total = 0

for i in range(1, n + 1):
    if n % i == 0:
        total += i

print(total)


# 8
n = int(input())
total = 1

for i in range(2, n + 1):
    if i % 2 == 0:
        total -= i
    else:
        total += i

print(total)


# 9
sorted_numbers = sorted(int(input()) for _ in range(int(input())))

print(sorted_numbers[-1])
print(sorted_numbers[-2])


# 10
print(
    "YES" if all(map(lambda n: n % 2 == 0, (int(input()) for _ in range(10)))) else "NO"
)


# 11
from functools import cache

n = int(input())


@cache
def fibonacci(n: int) -> int:
    return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)


print(*(fibonacci(i) for i in range(1, n + 1)))
