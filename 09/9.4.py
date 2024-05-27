# 1
# print(len(input().split(" ")))

print(input().count(" ") + 1)


# 2
from collections import Counter

letter_to_counter = Counter(input().upper())

print("Аденин: {}".format(letter_to_counter["А"]))
print("Гуанин: {}".format(letter_to_counter["Г"]))
print("Цитозин: {}".format(letter_to_counter["Ц"]))
print("Тимин: {}".format(letter_to_counter["Т"]))


# 3
counter = 0

for _ in range(int(input())):
    if input().count("11") > 2:
        counter += 1

print(counter)


# 4
from re import sub

print(len(sub(r"\D", "", input())))


# 5
# s = input()

# print("YES" if s.endswith(".com") or s.endswith(".ru") else "NO")

print("YES" if input().endswith((".com", ".ru")) else "NO")


# 6
from collections import Counter

char_to_counter = Counter(input())
max_item: tuple[str, int] = ("", 0)

for item in char_to_counter.items():
    if item[1] >= max_item[1]:
        max_item = item

print(max_item[0])


# 7
s = input()
f_counter = s.count("f")

if f_counter > 1:
    print(s.index("f"), s.rindex("f"))
elif f_counter > 0:
    print(s.index("f"))
else:
    print("NO")


# 8
from re import sub

print((sub(r"h.*h", "", input())))
