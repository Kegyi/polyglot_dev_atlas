class Operations:
    def minus(self, a: int, b: int) -> int:
        return a - b

    def multiply(self, a: int, b: int) -> int:
        return a * b

    def divide(self, a: int, b: int) -> int:
        return int(a / b)


def main() -> None:
    ops = Operations()
    print(ops.minus(10, 3))
    print(ops.multiply(6, -4))
    print(ops.divide(20, 5))


if __name__ == "__main__":
    main()
