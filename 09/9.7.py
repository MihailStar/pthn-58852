# 1
a, b = map(int, (input(), input()))

for i in range(a, b + 1):
    print(chr(i), end=" ")


# 2
s = input()

for char in s:
    print(ord(char), end=" ")


# 3
from typing import Final

CODE: Final[dict[str, int]] = {"a": ord("a"), "z": ord("z")}
ABC_LENGTH = CODE["z"] - CODE["a"] + 1


def decode(
    text: str,
    shift: int,
) -> str:
    """@tutorial https://github.com/mihailstar/node-bas/blob/master/01/src/сaesar-cipher.ts"""

    result = ""

    for char in text:
        code = ord(char)
        code_with_shift = ((code - CODE["a"] - shift) % ABC_LENGTH) + CODE["a"]

        result += chr(code_with_shift)

    return result


shift, text = int(input()), input()

print(decode(text, shift))
