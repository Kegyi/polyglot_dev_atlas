package main

import "fmt"

func search(arr []int, target int) int {
	if len(arr) == 0 {
		return -1
	}
	left, right := 0, len(arr)-1
	for left < right && arr[left] == arr[right] {
		right--
	}
	for left < right {
		mid := (left + right) / 2
		if arr[mid] > arr[right] {
			if arr[left] <= target && target <= arr[mid] {
				right = mid
			} else {
				left = mid + 1
			}
		} else if arr[mid] < arr[right] {
			if arr[mid] < target && target <= arr[right] {
				left = mid + 1
			} else {
				right = mid
			}
		} else {
			right--
		}
	}
	if arr[left] == target {
		return left
	}
	return -1
}

func main() {
	arr := []int{15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}
	fmt.Println(search(arr, 5))
	fmt.Println(search(arr, 11))
}
