from typing import List


def find_swap_values(array1: List[int], array2: List[int]) -> List[int]:
    diff = sum(array1) - sum(array2)
    if diff % 2 != 0:
        return []
    target = diff // 2
    set2 = set(array2)
    for x in array1:
        y = x - target
        if y in set2:
            return [x, y]
    return []


def main() -> None:
    print(find_swap_values([4, 1, 2, 1, 1, 2], [3, 6, 3, 3]))


if __name__ == "__main__":
    main()
