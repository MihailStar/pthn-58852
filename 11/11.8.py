# 1
a: list[int] = []

print(sorted(a))


# 2
a: list[int] = []
a_length = len(a)

for shift in range(a_length):
    maximum_index = a_length - 1 - shift

    for index in range(a_length - shift):
        if a[index] > a[maximum_index]:
            maximum_index = index

    a[a_length - 1 - shift], a[maximum_index] = (
        a[maximum_index],
        a[a_length - 1 - shift],
    )

print(a)
