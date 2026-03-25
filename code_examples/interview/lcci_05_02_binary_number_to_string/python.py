def binary_to_string(n: float) -> str:
    result = ["0."]
    while n > 0:
        if len(result) > 32:
            return "ERROR"
        n *= 2
        if n >= 1:
            result.append("1")
            n -= 1
        else:
            result.append("0")
    return "".join(result)


def main() -> None:
    print(binary_to_string(0.625))
    print(binary_to_string(0.1))


if __name__ == "__main__":
    main()
