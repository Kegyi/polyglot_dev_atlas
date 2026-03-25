from typing import List

def findMagicIndex(nums: List[int]) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == mid:
            return mid
        if nums[mid] < mid:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

def main():
    print(findMagicIndex([-1, 1, 3, 4, 6]))  # 1
    print(findMagicIndex([0, 2, 3, 4, 5]))   # 0

if __name__ == "__main__":
    main()
