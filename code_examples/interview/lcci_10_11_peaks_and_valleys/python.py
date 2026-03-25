from typing import List


def wiggle_sort(nums: List[int]) -> None:
    nums.sort()
    for index in range(0, len(nums) - 1, 2):
        nums[index], nums[index + 1] = nums[index + 1], nums[index]


def main() -> None:
    nums = [5, 3, 1, 2, 3]
    wiggle_sort(nums)
    print(nums)


if __name__ == "__main__":
    main()
