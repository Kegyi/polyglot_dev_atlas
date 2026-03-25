from typing import List


def find_string(words: List[str], target: str) -> int:
    left, right = 0, len(words) - 1
    answer = -1
    while left <= right:
        mid = (left + right) // 2
        lo = mid
        hi = mid
        actual = -1
        while lo >= left or hi <= right:
            if lo >= left and words[lo]:
                actual = lo
                break
            if hi <= right and words[hi]:
                actual = hi
                break
            lo -= 1
            hi += 1
        if actual == -1:
            break
        if words[actual] == target:
            answer = actual
            right = actual - 1
        elif words[actual] < target:
            left = actual + 1
        else:
            right = actual - 1
    return answer


def main() -> None:
    words = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    print(find_string(words, "ta"))
    print(find_string(words, "ball"))


if __name__ == "__main__":
    main()
