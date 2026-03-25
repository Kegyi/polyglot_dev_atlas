from typing import List


class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        i1 = i2 = -1
        ans = float('inf')
        for i, w in enumerate(words):
            if w == word1:
                i1 = i
            if w == word2:
                i2 = i
            if i1 != -1 and i2 != -1:
                ans = min(ans, abs(i1 - i2))
        return int(ans)


def main():
    sol = Solution()
    print(sol.findClosest(["I","am","a","student","from","a","university","in","a","city"], "a", "student"))  # 1
    print(sol.findClosest(["aa", "bb"], "aa", "bb"))  # 1


if __name__ == "__main__":
    main()
