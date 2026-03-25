package main

import "fmt"

func findMagicIndex(nums []int) int {
	lo, hi := 0, len(nums)-1
	for lo <= hi {
		mid := lo + (hi-lo)/2
		if nums[mid] == mid {
			return mid
		}
		if nums[mid] < mid {
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}
	return -1
}

func main() {
	fmt.Println(findMagicIndex([]int{-1, 1, 3, 4, 6})) // 1
	fmt.Println(findMagicIndex([]int{0, 2, 3, 4, 5}))  // 0
}
