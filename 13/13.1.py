# 1
def draw_box() -> None:
    width = 10
    height = 14

    print("*" * width)
    for _ in range(height - 2):
        print(f"*{' '*(width-2)}*")
    print("*" * width)


draw_box()


# 2
def draw_triangle() -> None:
    n = 10

    for i in range(1, n + 1):
        print("*" * i)


draw_triangle()
