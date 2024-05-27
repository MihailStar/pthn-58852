# 1
numbers = [8, 9, 10, 11]

numbers[1] = 17
# numbers.extend([4, 5, 6])
numbers += [4, 5, 6]
del numbers[0]
numbers *= 2
numbers.insert(3, 25)

print(numbers)


# 2
numbers = [int(number) for number in input().split()]
min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))
numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

print(*numbers)


# 3
from collections import Counter

word_to_counter = Counter(input().split())
number_of = sum(map(lambda a: word_to_counter[a], ("a", "an", "the", "A", "An", "The")))

print(f"Общее количество артиклей: {number_of}")


# 4
for _ in range(int(input()[1:])):
    string = input()
    hash_index = string.find("#")

    if hash_index == -1:
        print(string.rstrip())
    else:
        print(string[:hash_index].rstrip())


# 5
numbers = [int(number) for number in input().split()]

print(*sorted(numbers))
print(*sorted(numbers, reverse=True))
