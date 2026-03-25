from typing import List


def search(arr: List[int], target: int) -> int:
    if not arr:
        return -1
    left, right = 0, len(arr) - 1
    while left < right and arr[left] == arr[right]:
        right -= 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[right]:
            if arr[left] <= target <= arr[mid]:
                right = mid
            else:
                left = mid + 1
        elif arr[mid] < arr[right]:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid
        else:
            right -= 1
    return left if arr[left] == target else -1


def main() -> None:
    arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    print(search(arr, 5))
    print(search(arr, 11))


if __name__ == "__main__":
    main()
