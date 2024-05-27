# 1
count = 0
p = 1  # 1

for _ in range(10):  # 2
    x = int(input())

    if x > -1:  # 3
        count += 1
        p *= x

if count > 0:
    print(count)  # 4
    print(p)
else:
    print("NO")


# 2
mx = -1e6  # 1
s = 0

for _ in range(10):  # 2
    x = int(input())

    if x < 0:
        s += x  # 3

        if x > mx:  # 4
            mx = x

if s < 0:  # 5
    print(s)
    print(mx)
else:
    print("NO")


# 3
print(sum(filter(lambda n: n % 2 == 0, (int(input()) for _ in range(7)))))


# 4
xxl = sorted(filter(lambda n: n % 3 == 0, map(int, input())))

print(xxl[-1] if xxl else "NO")


# 5
n = int(input())

while n > 9:  # 1
    n //= 10  # 2

print(n)


# 6
from functools import reduce

print(reduce(lambda a, n: a * n, map(int, input())))
