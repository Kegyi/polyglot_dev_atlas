from typing import List


def smallest_difference(a: List[int], b: List[int]) -> int:
    a.sort()
    b.sort()
    i = j = 0
    ans = 1 << 63
    while i < len(a) and j < len(b):
        ans = min(ans, abs(a[i] - b[j]))
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    return ans


def main() -> None:
    print(smallest_difference([1, 3, 15, 11, 2], [23, 127, 235, 19, 8]))


if __name__ == "__main__":
    main()
