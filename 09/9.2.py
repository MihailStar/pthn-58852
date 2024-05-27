# 1
s = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(s[:12])


# 2
s = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(s[-9:])


# 3
s = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(s[::7])


# 4
s = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(s[::-1])


# 5
s = input()

print("YES" if s == s[::-1] else "NO")


# 6
s = input()

print(len(s))
print(s * 3)
print(s[0])
print(s[:3])
print(s[-3:])
print(s[::-1])
print(s[1:-1])


# 7
s = input()

print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])


# 8
from math import ceil

s = input()

print(f"{s[ceil(len(s) / 2) :]}{s[: ceil(len(s) / 2)]}")
