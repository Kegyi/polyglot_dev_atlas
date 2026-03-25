package main

import (
	"fmt"
	"math"
	"sort"
)

func smallestDifference(a []int, b []int) int {
	sort.Ints(a)
	sort.Ints(b)
	i, j := 0, 0
	ans := int64(math.MaxInt64)
	for i < len(a) && j < len(b) {
		diff := int64(a[i]) - int64(b[j])
		if diff < 0 {
			diff = -diff
		}
		if diff < ans {
			ans = diff
		}
		if a[i] < b[j] {
			i++
		} else {
			j++
		}
	}
	return int(ans)
}

func main() {
	fmt.Println(smallestDifference([]int{1, 3, 15, 11, 2}, []int{23, 127, 235, 19, 8}))
}
