from bisect import bisect_left
from typing import List


class Solution:
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        people = sorted(zip(height, weight), key=lambda x: (x[0], -x[1]))
        lis: List[int] = []
        for _, w in people:
            i = bisect_left(lis, w)
            if i == len(lis):
                lis.append(w)
            else:
                lis[i] = w
        return len(lis)


def main():
    sol = Solution()
    print(sol.bestSeqAtIndex([65, 70, 56, 75, 60, 68], [100, 150, 90, 190, 95, 110]))  # 6
    print(sol.bestSeqAtIndex([65, 70, 56, 75], [100, 150, 90, 190]))  # 4


if __name__ == "__main__":
    main()
