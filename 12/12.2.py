# 1
print([i for i in range(2, int(input()) + 1, 2)])


# 2
print(*(int(a) + int(b) for a, b in zip(input().split(), input().split())))


# 3
digits = input().split()

print("+".join(digits), "=", sum(map(int, digits)), sep="")


# 4
from re import fullmatch

print("NO" if not fullmatch(r"(?:7-)?\d\d\d-\d\d\d-\d\d\d\d", input()) else "YES")


# 5
print(max(len(word) for word in input().split()))


# 6
print(" ".join(f"{word[1:]}{word[0]}ки" for word in input().split()))
