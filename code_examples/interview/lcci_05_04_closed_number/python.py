def find_closed_numbers(num: int) -> tuple[int, int]:
    bigger = num
    smaller = num

    # Next larger: find rightmost '01' and flip to '10'
    for i in range(1, 32):
        if (bigger >> (i - 1)) & 1 == 1 and (bigger >> i) & 1 == 0:
            bigger |= (1 << i)
            bigger &= ~(1 << (i - 1))
            break

    # Next smaller: find rightmost '10' and flip to '01'
    for i in range(1, 32):
        if (smaller >> (i - 1)) & 1 == 0 and (smaller >> i) & 1 == 1:
            smaller &= ~(1 << i)
            smaller |= (1 << (i - 1))
            break

    return bigger, smaller


def main() -> None:
    bigger, smaller = find_closed_numbers(2)
    print(bigger)
    print(smaller)


if __name__ == "__main__":
    main()
