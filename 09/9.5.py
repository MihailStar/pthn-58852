# 1
nickname = input()

if (
    nickname.startswith("@")
    and 4 < len(nickname) < 16
    and nickname == nickname.lower()
    and nickname[1::].isalnum()
):
    print("Correct")
else:
    print("Incorrect")


# 2
for index, _ in enumerate(range(int(input())), 1):
    comment = input()

    print(f"{index}:", comment if comment.strip() else "COMMENT SHOULD BE DELETED")


# 3
from re import fullmatch

letter = r"[АВЕКМНОРСТУХ]"
number = r"[0123456789]"
reg_number = (
    rf"{letter}{number}{number}{number}{letter}{letter}_{number}{number}{number}?"
)

print("YES" if fullmatch(reg_number, input()) else "NO")
