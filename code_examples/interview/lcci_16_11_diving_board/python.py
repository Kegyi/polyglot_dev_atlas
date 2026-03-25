from typing import List


def diving_board(shorter: int, longer: int, k: int) -> List[int]:
    if k == 0:
        return []
    if shorter == longer:
        return [shorter * k]
    return [shorter * (k - i) + longer * i for i in range(k + 1)]


def main() -> None:
    print(diving_board(1, 2, 3))


if __name__ == "__main__":
    main()
