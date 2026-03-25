package main

import (
	"fmt"
	"sort"
)

func subsets(nums []int) [][]int {
	sort.Ints(nums)
	n := len(nums)
	result := [][]int{}
	for mask := 0; mask < (1 << n); mask++ {
		subset := []int{}
		for i := 0; i < n; i++ {
			if mask&(1<<i) != 0 {
				subset = append(subset, nums[i])
			}
		}
		result = append(result, subset)
	}
	return result
}

func main() {
	for _, s := range subsets([]int{1, 2, 3}) {
		fmt.Println(s)
	}
}
