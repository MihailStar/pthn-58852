# 1
year = int(input())

print("YES" if year % 100 == 0 else "NO")


# 2
y1, x1, y2, x2 = (int(input()) for _ in range(4))

print("YES" if (y1 + x1) % 2 == (y2 + x2) % 2 else "NO")


# 3
age, gender = (int(input()), input())

print("YES" if 9 < age < 16 and gender == "f" else "NO")


# 4
digit = input()
map = {
    "1": "I",
    "2": "II",
    "3": "III",
    "4": "IV",
    "5": "V",
    "6": "VI",
    "7": "VII",
    "8": "VIII",
    "9": "IX",
    "10": "X",
}

print(map[digit] if digit in map else "ошибка")


# 5
number = int(input())

if number % 2 == 0:
    if 1 < number < 6 or number > 20:
        print("NO")
    elif 5 < number < 21:
        print("YES")
else:
    print("YES")


# 6
y1, x1, y2, x2 = (int(input()) for _ in range(4))

# @tutorial https://stepik.org/lesson/292172/step/6?discussion=1651821&unit=273659
print("YES" if y1 - x1 == y2 - x2 or y1 + x1 == y2 + x2 else "NO")


# 7
y1, x1, y2, x2 = (int(input()) for _ in range(4))

if (
    (y1 - 2 == y2 and x1 + 1 == x2)
    or (y1 - 1 == y2 and x1 + 2 == x2)
    or (y1 + 1 == y2 and x1 + 2 == x2)
    or (y1 + 2 == y2 and x1 + 1 == x2)
    or (y1 + 2 == y2 and x1 - 1 == x2)
    or (y1 + 1 == y2 and x1 - 2 == x2)
    or (y1 - 1 == y2 and x1 - 2 == x2)
    or (y1 - 2 == y2 and x1 - 1 == x2)
):
    print("YES")
else:
    print("NO")


# 8
y1, x1, y2, x2 = (int(input()) for _ in range(4))

# @tutorial `# 6`
print(
    "YES" if y1 - x1 == y2 - x2 or y1 + x1 == y2 + x2 or y1 == y2 or x1 == x2 else "NO"
)
