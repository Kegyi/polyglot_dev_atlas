from collections import Counter
import heapq


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    freq = Counter(nums)
    heap: list[tuple[int, int]] = []

    for value, count in freq.items():
        heapq.heappush(heap, (count, value))
        if len(heap) > k:
            heapq.heappop(heap)

    # Highest-frequency values should be first in the final output.
    return [value for _, value in sorted(heap, reverse=True)]


def main() -> None:
    nums = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5, 5]
    k = 2
    result = top_k_frequent(nums, k)
    print("top k frequent:", *result)


if __name__ == "__main__":
    main()
