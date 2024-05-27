# 1
numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]

print(sum(number**2 for number in numbers))


# 2
numbers = [int(input()) for _ in range(int(input()))]

print(*numbers, sep="\n")
print()
print(*(number**2 + 2 * number + 1 for number in numbers), sep="\n")


# 3
numbers = [int(input()) for _ in range(int(input()))]
minimum = min(numbers)
maximum = max(numbers)

print(
    *(number for number in numbers if number != minimum and number != maximum), sep="\n"
)


# 4
words = [input() for _ in range(int(input()))]
displayed: dict[str, str] = {}

for word in words:
    if word in displayed:
        continue

    displayed[word] = word

    print(word)


# 5
strings = [input() for _ in range(int(input()))]
request = input().lower()

print(*(string for string in strings if request in string.lower()), sep="\n")


# 6
strings = [input() for _ in range(int(input()))]
requests = [input().lower() for _ in range(int(input()))]

print(
    *(
        string
        for string in strings
        if all(request in string.lower() for request in requests)
    ),
    sep="\n"
)


# 7
negatives, zeros, positives = [], [], []

for number in (int(input()) for _ in range(int(input()))):
    if number < 0:
        negatives.append(number)
    elif number > 0:
        positives.append(number)
    else:
        zeros.append(number)

print(*negatives + zeros + positives, sep="\n")
