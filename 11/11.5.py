# 1
print(*input().split(), sep="\n")


# 2
print(*map(lambda word: f"{word[0]}.", input().split()), sep="")


# 3
print(*input().split("\\"), sep="\n")


# 4
# print(*map(lambda digit: "+" * int(digit), input().split()), sep="\n")

print("\n".join(map(lambda digit: "+" * int(digit), input().split())))


# 5
from re import fullmatch

# @tutorial https://github.com/mihailstar/pthn-urfu-pyap/blob/master/src/1.1.4/g.py#L12
part_of_ip = r"(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])"
ip = rf"^{part_of_ip}\.{part_of_ip}\.{part_of_ip}\.{part_of_ip}$"

print("НЕТ" if not fullmatch(ip, input()) else "ДА")


# 6
s, separator = input(), input()

# print(separator.join(list(s)))

print(separator.join(s))


# 7
from collections import Counter
from math import comb

numbers = [int(digit) for digit in input().split()]
number_to_counter = Counter(numbers)
pair = 2

print(
    sum(
        map(
            lambda counter: comb(counter, pair),
            number_to_counter.values(),
        )
    )
)
