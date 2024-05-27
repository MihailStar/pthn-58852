# 1
numbers = (
    [2, 6, 3, 14, 10, 4, 11, 16, 12, 5]
    + [4, 16, 1, 0, 8, 16, 10, 10, 8, 5]
    + [1, 11, 10, 10, 12, 0, 0, 6, 14, 8]
    + [2, 12, 14, 5, 6, 12, 1, 2, 10, 14]
    + [9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
)

print(len(numbers))
print(numbers[-1])
print(numbers[::-1])
print("YES" if 5 in numbers and 17 in numbers else "NO")
print(numbers[1:-1])


# 2
print([input() for _ in range(int(input()))])


# 3
print([chr(ord("a") + i) * (i + 1) for i in range(ord("z") - ord("a") + 1)])


# 4
print([int(input()) ** 3 for _ in range(int(input()))])


# 5
n = int(input())

print([i for i in range(1, n + 1) if n % i == 0])


# 6
numbers = [int(input()) for _ in range(int(input()))]

print([numbers[index] + numbers[index + 1] for index in range(len(numbers) - 1)])


# 7
numbers = [int(input()) for _ in range(int(input()))]

# print([number for index, number in enumerate(numbers) if index % 2 == 0])

del numbers[1::2]

print(numbers)


# 8
words = [input() for _ in range(int(input()))]
index = int(input()) - 1

for word in words:
    if len(word) - 1 < index:
        continue

    print(word[index], end="")


# 9
acc: list[str] = []

for _ in range(int(input())):
    acc.extend(input())

print(acc)
