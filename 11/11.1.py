# 1
# n = int(input())

# print([i for i in range(1, n + 1)])

print(list(range(1, int(input()) + 1)))


# 2
n = int(input())

print([chr(ord("a") + i) for i in range(0, n)])
