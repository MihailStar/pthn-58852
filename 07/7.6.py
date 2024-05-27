# 1
n = int(input())

for i in range(2, n + 1):
    if n % i == 0:
        print(i)
        break


# 2
n = int(input())

for i in range(1, n + 1):
    if 4 < i < 10 or 16 < i < 38 or 77 < i < 88:
        continue
    print(i)
