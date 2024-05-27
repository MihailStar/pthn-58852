# 1
s = "Python rocks!"

print(len(s))


# 2
s = "Python rocks!"

print(s[4 - 1])


# 3
s = "Python rocks!"

print(s[1:5])


# 4
s = "    Python rocks!     "

print(s.strip())


# 5
s = "Python rocks!"

print(s.upper())


# 6
s = "Python rocks!"

print(s.replace("o", "@"))


# 7
s = input()

print(*(char for index, char in enumerate(s) if index % 3 != 0), sep="")


# 8
# from re import sub

# s = input()

# print(sub(r"1", "one", s))

print(input().replace("1", "one"))


# 9
print(input().replace("@", ""))


# 10
s = input()
first_index = s.find("f")

if first_index == -1:
    print(-2)
else:
    second_index = s.find("f", first_index + 1)

    if second_index == -1:
        print(-1)
    else:
        print(second_index)


# 11
s = input()
first_index = s.find("h")
last_index = s.rfind("h")

print(
    s[: first_index + 1],
    s[first_index + 1 : last_index][::-1],
    s[last_index:],
    sep="",
)
