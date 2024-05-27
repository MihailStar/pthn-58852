# 1
keywords: list[str] = []

print([keyword[1:] for keyword in keywords])


# 2
keywords: list[str] = []

print([len(keyword) for keyword in keywords])


# 3
keywords: list[str] = []

print([keyword for keyword in keywords if len(keyword) > 4])


# 4
print([number for number in range(100, 1000 + 1) if str(number) == str(number)[::-1]])


# 5
n = int(input())

for number in (number**2 for number in range(1, n + 1)):
    print(number)


# 6
for number in (n**3 for n in (int(d) for d in input().split())):
    print(number, end=" ")


# 7
print(*(input().split()), sep="\n")


# 8
print(*(c for c in list(input()) if c.isdigit()), sep="")


# 9
print(
    *(n for n in (int(d) ** 2 for d in input().split()) if n % 10 != 4 and n % 2 == 0)
)
