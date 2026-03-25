def trailing_zeroes(n: int) -> int:
    ans = 0
    while n > 0:
        n //= 5
        ans += n
    return ans


def main() -> None:
    print(trailing_zeroes(3))
    print(trailing_zeroes(5))


if __name__ == "__main__":
    main()
