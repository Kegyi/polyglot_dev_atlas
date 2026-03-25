from typing import List


def map_digit(ch: str) -> str:
    if ch <= "c":
        return "2"
    if ch <= "f":
        return "3"
    if ch <= "i":
        return "4"
    if ch <= "l":
        return "5"
    if ch <= "o":
        return "6"
    if ch <= "s":
        return "7"
    if ch <= "v":
        return "8"
    return "9"


def get_valid_t9_words(num: str, words: List[str]) -> List[str]:
    ans = []
    for word in words:
        if len(word) != len(num):
            continue
        if all(map_digit(word[i]) == num[i] for i in range(len(word))):
            ans.append(word)
    return ans


def main() -> None:
    print(get_valid_t9_words("8733", ["tree", "used", "true"]))


if __name__ == "__main__":
    main()
