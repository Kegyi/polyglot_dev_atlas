from typing import List


def sub_sort(array: List[int]) -> List[int]:
    n = len(array)
    left = right = -1

    max_seen = -10**18
    for i, value in enumerate(array):
        if value < max_seen:
            right = i
        else:
            max_seen = value

    min_seen = 10**18
    for i in range(n - 1, -1, -1):
        if array[i] > min_seen:
            left = i
        else:
            min_seen = array[i]

    return [left, right] if left != -1 else [-1, -1]


def main() -> None:
    print(sub_sort([1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19]))


if __name__ == "__main__":
    main()
