# 1
m, n = (int(input()) for _ in range(2))

print(*(str(i) for i in range(m, n + 1)), sep="\n")


# 2
m, n = (int(input()) for _ in range(2))

print(
    *range(
        m,
        n + 1 if m < n else n - 1,
        1 if m < n else -1,
    ),
    sep="\n",
)


# 3
m, n = (int(input()) for _ in range(2))

# print(*range(m - 1 if m % 2 == 0 else m, n - 1, -2), sep="\n")
print(*range(m + m % 2 - 1, n - 1, -2), sep="\n")


# 4
m, n = (int(input()) for _ in range(2))

print(
    *(
        i
        for i in (range(m, n + 1))
        if (i % 17 == 0) or (i % 10 == 9) or (i % 3 == 0 and i % 5 == 0)
    ),
    sep="\n",
)

# 5
n = int(input())

for i in range(1, 10 + 1):
    print(f"{n} x {i} = {n * i}")
