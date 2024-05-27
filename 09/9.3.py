# 1
имя, фамилия = input().split()

print("YES" if имя.istitle() and фамилия.istitle() else "NO")


# 2
s = input()

# for char in s:
#     if char.islower():
#         print(char.upper(), end="")
#     else:
#         print(char.lower(), end="")

print(s.swapcase())


# 3
print("YES" if "хорош" in input().lower() else "NO")


# 4
s = input()
counter = 0

for char in s:
    if char.islower():
        counter += 1

print(counter)
