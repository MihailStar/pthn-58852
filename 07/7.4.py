# 1
inputed = input()

while inputed != "КОНЕЦ":
    print(inputed)
    inputed = input()


# 2
inputed = input()

while True:
    if inputed in ("КОНЕЦ", "конец"):
        break

    print(inputed)
    inputed = input()


# 3
counter = 0

while not input() in ("стоп", "хватит", "достаточно"):
    counter += 1

print(counter)


# 4
inputed: str

while not int(inputed := input()) % 7:
    print(inputed)


# 5
inputed: str
counter = 0

while not (inputed := input()).startswith("-"):
    counter += int(inputed)

print(counter)


# 6
grade: int
counter = 0

while 0 < (grade := int(input())) < 6:
    if grade == 5:
        counter += 1

print(counter)


# 7
payment = int(input())
counter = 0

for coin in (25, 10, 5, 1):
    while payment >= coin:
        payment -= coin
        counter += 1

print(counter)
