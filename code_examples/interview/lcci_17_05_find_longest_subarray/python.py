from typing import List


class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        first = {0: -1}
        s = 0
        max_len = 0
        start = 0
        for i, x in enumerate(array):
            s += 1 if x[0].isalpha() else -1
            if s in first:
                length = i - first[s]
                if length > max_len:
                    max_len = length
                    start = first[s] + 1
            else:
                first[s] = i
        return array[start:start + max_len]


def main():
    sol = Solution()
    arr1 = ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]
    print(' '.join(sol.findLongestSubarray(arr1)))  # A 1 B C D 2 3 4 E 5 F G 6 7

    arr2 = ["A", "A"]
    res2 = sol.findLongestSubarray(arr2)
    print("(empty)" if not res2 else ' '.join(res2))


if __name__ == "__main__":
    main()
