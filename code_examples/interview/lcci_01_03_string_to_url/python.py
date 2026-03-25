def urlify(s: str, true_length: int) -> str:
    return "".join("%20" if ch == " " else ch for ch in s[:true_length])


def main() -> None:
    print(urlify("Mr John Smith    ", 13))


if __name__ == "__main__":
    main()
