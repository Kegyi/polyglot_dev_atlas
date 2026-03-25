from typing import List
import heapq


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        h = []
        for x in arr:
            heapq.heappush(h, -x)
            if len(h) > k:
                heapq.heappop(h)
        return [-x for x in h]
