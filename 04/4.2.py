# 1
x = int(input())

print("Принадлежит" if -1 < x < 17 else "Не принадлежит")


# 2
x = int(input())

print("Принадлежит" if x <= -3 or x >= 7 else "Не принадлежит")


# 3
x = int(input())

print("Принадлежит" if -30 < x < -1 or 7 < x < 26 else "Не принадлежит")


# 4
x = int(input())

print("YES" if (1000 <= x <= 9999) and (x % 7 == 0 or x % 17 == 0) else "NO")


# 5
a, b, c = (int(input()) for _ in range(3))

print("YES" if a + b > c and a + c > b and b + c > a else "NO")


# 6
year = int(input())

# @tutorial https://github.com/mihailstar/exercism-tasks/blob/master/leap.js
print("YES" if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else "NO")


# 7
y_from, x_from, y_to, x_to = (int(input()) for _ in range(4))

print("YES" if y_from == y_to or x_from == x_to else "NO")


# 8
y_from, x_from, y_to, x_to = (int(input()) for _ in range(4))

if (
    (y_from + 1 == y_to and x_from == x_to)         # ↑
    or (y_from + 1 == y_to and x_from + 1 == x_to)  # ↗
    or (y_from == y_to and x_from + 1 == x_to)      # →
    or (y_from - 1 == y_to and x_from + 1 == x_to)  # ↘
    or (y_from - 1 == y_to and x_from == x_to)      # ↓
    or (y_from - 1 == y_to and x_from - 1 == x_to)  # ↙
    or (y_from == y_to and x_from - 1 == x_to)      # ←
    or (y_from + 1 == y_to and x_from - 1 == x_to)  # ↖
):
    print("YES")
else:
    print("NO")
