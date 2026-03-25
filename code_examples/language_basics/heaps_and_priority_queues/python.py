#!/usr/bin/env python3
import heapq


def main() -> None:
    data = [3, 1, 4, 1, 5, 9]

    # min-heap (default)
    min_heap: list[int] = []
    for v in data:
        heapq.heappush(min_heap, v)
    print("min:", min_heap[0])  # 1
    print("drain min-heap:", [heapq.heappop(min_heap) for _ in range(len(min_heap))])  # [1,1,3,4,5,9]

    # max-heap via negation
    max_heap: list[int] = []
    for v in data:
        heapq.heappush(max_heap, -v)
    print("max:", -max_heap[0])  # 9


if __name__ == "__main__":
    main()
