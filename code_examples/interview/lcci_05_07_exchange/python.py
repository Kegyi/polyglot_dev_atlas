def exchange_bits(num: int) -> int:
    u = num & 0xFFFFFFFF
    return (((u & 0xAAAAAAAA) >> 1) | ((u & 0x55555555) << 1)) & 0xFFFFFFFF


def main() -> None:
    print(exchange_bits(2))
    print(exchange_bits(3))


if __name__ == "__main__":
    main()
