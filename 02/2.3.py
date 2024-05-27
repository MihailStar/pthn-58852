# 1
print("I", "like", "Python", sep="***")


# 2
name = input()

print(f"Привет, {name}", end="!")


# 3
delimiter, *strings = (input() for _ in range(4))

print(*strings, sep=delimiter)
