#!/usr/bin/env python3
from bisect import bisect_left


def main() -> None:
    values = [9, 3, 7, 1, 5]
    ordered = sorted(values)

    index = bisect_left(ordered, 7)
    found_index = index if index < len(ordered) and ordered[index] == 7 else -1

    print("sorted:", ordered)
    print("contains 7:", 7 in ordered)
    print("index of 7:", found_index)


if __name__ == "__main__":
    main()
