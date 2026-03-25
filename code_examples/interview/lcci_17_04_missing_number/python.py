from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for i, x in enumerate(nums, 1):
            ans ^= i ^ x
        return ans


def main():
    sol = Solution()
    print(sol.missingNumber([3, 0, 1]))              # 2
    print(sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 8


if __name__ == "__main__":
    main()
