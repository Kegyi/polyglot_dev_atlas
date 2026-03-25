from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0
        for x in nums:
            if count == 0:
                candidate = x
            count += 1 if x == candidate else -1
        return candidate if nums.count(candidate) > len(nums) // 2 else -1


def main():
    sol = Solution()
    print(sol.majorityElement([1, 2, 5, 9, 5, 9, 5, 5, 5]))  # 5
    print(sol.majorityElement([3, 2]))  # -1


if __name__ == "__main__":
    main()
