from collections import defaultdict
from typing import List


def pair_sums(nums: List[int], target: int) -> List[List[int]]:
    freq: dict[int, int] = defaultdict(int)
    ans = []
    for x in nums:
        y = target - x
        if freq[y] > 0:
            freq[y] -= 1
            ans.append([min(x, y), max(x, y)])
        else:
            freq[x] += 1
    return ans


def main() -> None:
    print(pair_sums([5, 6, 5], 11))


if __name__ == "__main__":
    main()
