from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    result = []
    for mask in range(1 << n):
        subset = [nums[i] for i in range(n) if mask & (1 << i)]
        result.append(subset)
    return result

def main():
    for s in subsets([1, 2, 3]):
        print(s)

if __name__ == "__main__":
    main()
