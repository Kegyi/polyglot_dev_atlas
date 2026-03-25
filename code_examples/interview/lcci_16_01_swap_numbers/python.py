from typing import List


def swap_numbers(numbers: List[int]) -> List[int]:
    return [numbers[1], numbers[0]]


def main() -> None:
    print(swap_numbers([1, 2]))


if __name__ == "__main__":
    main()
