# 1
p1 = input()
p2 = input()

print(f"Пароль{' ' if p1 == p2 else ' не '}принят")


# 2
n = int(input())

print("Четное" if not n % 2 else "Нечетное")


# 3
ds = list(input())

print("ДА" if int(ds[0]) + int(ds[3]) == int(ds[1]) - int(ds[2]) else "НЕТ")


# 4
age = int(input())

print(f"Доступ {'запрещен' if age < 18 else 'разрешен'}")


# 5
a, b, c = (int(input()) for _ in range(3))

print("YES" if b - a == c - b else "NO")


# 6
print(min(int(input()) for _ in range(2)))


# 7
print(min(int(input()) for _ in range(4)))


# 8
age = int(input())
verdict = ""

if age > 59:
    verdict = "старость"
elif age > 24:
    verdict = "зрелость"
elif age > 13:
    verdict = "молодость"
else:
    verdict = "детство"

print(verdict)


# 9
numbers = (int(input()) for _ in range(3))

print(sum(filter(lambda number: number > 0, numbers)))
