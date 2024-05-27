# 1
s = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(s[s.find(",")])


# 2
s = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(s[s.find("w")])


# 3
s = input()

for i in range(0, len(s), 2):
    print(s[i])


# 4
# print(*input()[::-1], sep="\n")

s = input()

for i in range(len(s) - 1, -1, -1):
    print(s[i])


# 5
имя, фамилия, отчество = input(), input(), input()

print(фамилия[0], имя[0], отчество[0], sep="")


# 6
s = input()

print(sum(int(digit) for digit in s))


# 7
from string import digits

s = input()

for index in range(len(s)):
    char = s[index]

    if char in digits:
        print("Цифра")
        break

else:
    print("Цифр нет")


# 8
s = input()

print(f"Символ + встречается {s.count('+')} раз")
print(f"Символ * встречается {s.count('*')} раз")


# 9
s = input()
counter = 0

for index in range(len(s) - 1):
    if s[index] == s[index + 1]:
        counter += 1

print(counter)


# 10
s = input()

print(
    f'Количество гласных букв равно {sum(1 for char in s if char.lower() in "ауоыиэяюе")}'
)
print(
    f'Количество согласных букв равно {sum(1 for char in s if char.lower() in "бвгджзйклмнпрстфхцчшщ")}'
)


# 11
print(bin(int(input()))[2:])
