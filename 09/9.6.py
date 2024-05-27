# 1
s = "In {0}, someone paid {1} {2} for two pizzas."

print(s.format("2010", "10k", "Bitcoin"))


# 2
year = 2010
amount = "10K"
currency = "Bitcoin"

print(f"In {year}, someone paid {amount} {currency} for two pizzas.")


# 3
print(f"На {input()}: 1$ = {input()}₽, 1¥ = {input()}₽")


# 4
day, current_weight = int(input()), float(input())
starting_weight = 100
expected_weight = starting_weight - (starting_weight - 88) / 60 * day

print(
    "Что-то пошло не так" if current_weight > expected_weight else "Все идет по плану"
)
print(
    f"#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {current_weight} кг, ЦЕЛЬ по ВЕСУ = {expected_weight} кг"
)
