# 1
from math import sqrt

x1, y1, x2, y2 = (float(input()) for _ in range(4))
p = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

print(p)


# 2
from math import pi

r = float(input())
s = pi * r**2
c = 2 * pi * r

print(s, c, sep="\n")


# 3
from math import sqrt

a, b = (float(input()) for _ in range(2))

print((a + b) / 2)
print(sqrt(a * b))
print(2 * a * b / (a + b))
print(sqrt((a**2 + b**2) / 2))


# 4
from math import cos, pi, sin, tan

degrees = float(input())
radians = degrees * pi / 180

print(sin(radians) + cos(radians) + tan(radians) ** 2)


# 5
from math import ceil, floor

x = float(input())

print(ceil(x) + floor(x))


# 6
from math import sqrt

a, b, c = (float(input()) for _ in range(3))
d = b**2 - 4 * a * c

if d > 0:
    print(*sorted(((-b - sqrt(d)) / (2 * a), (-b + sqrt(d)) / (2 * a))), sep="\n")
elif d < 0:
    print("Нет корней")
else:
    print(-b / (2 * a))


# 7
from math import pi, tan

n, a = int(input()), float(input())
s = (n * a**2) / (4 * tan(pi / n))

print(s)
