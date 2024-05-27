# 1
print(
    '"Python is a great language!", said Fred. "I don\'t ever remember having this much fun before."'
)


# 2
введенное_имя = input()
введенная_фамилия = input()

print(f"Hello {введенное_имя} {введенная_фамилия}! You have just delved into Python")


# 3
title = input()

print(f"Футбольная команда {title} имеет длину {len(title)} символов")


# 4
sorted_cities = sorted((input() for _ in range(3)), key=len)

print(sorted_cities[0], sorted_cities[-1], sep="\n")


# 5
sorted_string_lengths = sorted((len(input()) for _ in range(3)))
is_arithmetic_progression_possible = (
    sorted_string_lengths[2] - sorted_string_lengths[1]
    == sorted_string_lengths[1] - sorted_string_lengths[0]
)

print("YES" if is_arithmetic_progression_possible else "NO")


# 6
print("YES" if "синий" in input() else "NO")


# 7
string = input()

print("YES" if "суббота" in string or "воскресенье" in string else "NO")


# 8
import re as regexp

print("YES" if regexp.fullmatch(r"[^@]+@[^@]+\.[^@]+", input()) else "NO")
