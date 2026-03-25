from typing import List


def max_sub_array(nums: List[int]) -> int:
    best = cur = nums[0]
    for value in nums[1:]:
        cur = max(value, cur + value)
        best = max(best, cur)
    return best


def main() -> None:
    print(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


if __name__ == "__main__":
    main()
