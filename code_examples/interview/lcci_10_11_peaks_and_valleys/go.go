package main

import (
	"fmt"
	"sort"
)

func wiggleSort(nums []int) {
	sort.Ints(nums)
	for i := 0; i+1 < len(nums); i += 2 {
		nums[i], nums[i+1] = nums[i+1], nums[i]
	}
}

func main() {
	nums := []int{5, 3, 1, 2, 3}
	wiggleSort(nums)
	fmt.Println(nums)
}
