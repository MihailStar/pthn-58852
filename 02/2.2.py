# 1
print("Здравствуй, мир!")


# 2
print(4, 8, 15, 16, 23, 42, sep=" ")


# 3
print(4, 8, 15, 16, 23, 42, sep="\n")


# 4
for i in range(1, 7 + 1):
    print("*" * i)


# 5
name = input()

print(f"Привет, {name}")


# 6
team_name = input()

print(f"{team_name} - чемпион!")


# 7
strings: list[str] = []

for i in range(3):
    strings.append(input())

print(*strings, sep="\n")


# 8
strings = [input(), input(), input()]

for i in range(len(strings) - 1, -1, -1):
    print(strings[i])
