# 1
n, k = input(), input()

if n > k:
    print("NO")
elif n < k:
    print("YES")
else:
    print("Don't know")


# 2
a, b, c = (int(input()) for _ in range(3))

if a == b and b == c:
    print("Равносторонний")
elif a == b or b == c or c == a:
    print("Равнобедренный")
else:
    print("Разносторонний")


# 3
print(sorted(int(input()) for _ in range(3))[1])


# 4
m = int(input())

if m in (1, 3, 5, 7, 8, 10, 12):
    print(31)
elif m in (4, 6, 9, 11):
    print(30)
else:
    print(28)


# 5
weight = int(input())

if weight < 60:
    print("Легкий вес")
elif weight < 64:
    print("Первый полусредний вес")
elif weight < 69:
    print("Полусредний вес")


# 6
operand_a, operand_b, operator = (int(input()), int(input()), input())

if operator == "+":
    print(operand_a + operand_b)
elif operator == "-":
    print(operand_a - operand_b)
elif operator == "*":
    print(operand_a * operand_b)
elif operator == "/":
    if operand_b == 0:
        print("На ноль делить нельзя!")
    else:
        print(operand_a / operand_b)
else:
    print("Неверная операция")


# 7
from typing import Final

pairOfСolor = (input(), input())
pairOfСolorToСolorMix: Final[dict[tuple[str, str], str]] = {
    ("красный", "красный"): "красный",
    ("красный", "желтый"): "оранжевый",
    ("желтый", "красный"): "оранжевый",
    ("желтый", "желтый"): "желтый",
    ("желтый", "синий"): "зеленый",
    ("синий", "желтый"): "зеленый",
    ("синий", "синий"): "синий",
    ("синий", "красный"): "фиолетовый",
    ("красный", "синий"): "фиолетовый",
}

if pairOfСolor in pairOfСolorToСolorMix:
    print(pairOfСolorToСolorMix[pairOfСolor])
else:
    print("ошибка цвета")


# 8
from typing import Callable

n = int(input())

isEven: Callable[[int], bool] = lambda n: n % 2 == 0

if n == 0:
    print("зеленый")
elif 0 < n < 11 or 18 < n < 29:  # [1, 10] и [19, 28]
    print("черный" if isEven(n) else "красный")
elif 10 < n < 19 or 28 < n < 37:  # [11, 18] и [29, 36]
    print("красный" if isEven(n) else "черный")
else:
    print("ошибка ввода")


# 9
a1, b1, a2, b2 = (int(input()) for _ in range(4))  # [a1, b1] и [a2, b2]

if a2 < a1:
    a1, b1, a2, b2 = (a2, b2, a1, b1)

if b1 < a2:
    print("пустое множество")
elif b1 == a2:
    print(a2)
else:
    print(
        a2,
        min(b1, b2),
    )
