package main

import "fmt"

func majorityElement(nums []int) int {
	candidate, count := 0, 0
	for _, x := range nums {
		if count == 0 {
			candidate = x
		}
		if x == candidate {
			count++
		} else {
			count--
		}
	}

	count = 0
	for _, x := range nums {
		if x == candidate {
			count++
		}
	}
	if count > len(nums)/2 {
		return candidate
	}
	return -1
}

func main() {
	fmt.Println(majorityElement([]int{1, 2, 5, 9, 5, 9, 5, 5, 5})) // 5
	fmt.Println(majorityElement([]int{3, 2}))                      // -1
}
