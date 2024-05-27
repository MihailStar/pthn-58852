# 1
from typing import Final, Literal, Union

CODE: Final[dict[str, int]] = {
    "A": ord("A"),
    "Z": ord("Z"),
    "a": ord("a"),
    "z": ord("z"),
}
ABC_LENGTH = CODE["z"] - CODE["a"] + 1


def encode(
    text: str,
    shift: int,
) -> str:
    """@tutorial https://github.com/mihailstar/node-bas/blob/master/01/src/сaesar-cipher.ts"""

    result = ""

    for char in text:
        code = ord(char)
        case: Union[Literal["lower"], Literal["upper"], None] = None

        if code >= CODE["A"] and code <= CODE["Z"]:
            case = "upper"

        if code >= CODE["a"] and code <= CODE["z"]:
            case = "lower"

        if case == None:
            result += char
            continue

        code_with_shift = (
            (code - CODE["A" if case == "upper" else "a"] + shift) % ABC_LENGTH
        ) + CODE["A" if case == "upper" else "a"]

        result += chr(code_with_shift)

    return result


for word in input().split():
    print(encode(word, sum(1 for char in word if char.isalpha())), end=" ")
