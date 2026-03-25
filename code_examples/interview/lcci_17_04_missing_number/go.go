package main

import "fmt"

func missingNumber(nums []int) int {
	ans := 0
	for i, x := range nums {
		ans ^= (i + 1) ^ x
	}
	return ans
}

func main() {
	fmt.Println(missingNumber([]int{3, 0, 1}))                   // 2
	fmt.Println(missingNumber([]int{9, 6, 4, 2, 3, 5, 7, 0, 1})) // 8
}
