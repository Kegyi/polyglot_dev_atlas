from typing import List


def max_alive_year(birth: List[int], death: List[int]) -> int:
    diff = [0] * 102
    for b, d in zip(birth, death):
        diff[b - 1900] += 1
        if d + 1 <= 2000:
            diff[d + 1 - 1900] -= 1

    best_year = 1900
    alive = 0
    best_alive = -1
    for i in range(101):
        alive += diff[i]
        if alive > best_alive:
            best_alive = alive
            best_year = 1900 + i
    return best_year


def main() -> None:
    print(max_alive_year([1900, 1901, 1950], [1948, 1951, 2000]))


if __name__ == "__main__":
    main()
