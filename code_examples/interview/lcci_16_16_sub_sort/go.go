package main

import (
	"fmt"
	"math"
)

func subSort(array []int) []int {
	n := len(array)
	left, right := -1, -1

	maxSeen := math.MinInt
	for i := 0; i < n; i++ {
		if array[i] < maxSeen {
			right = i
		} else {
			maxSeen = array[i]
		}
	}

	minSeen := math.MaxInt
	for i := n - 1; i >= 0; i-- {
		if array[i] > minSeen {
			left = i
		} else {
			minSeen = array[i]
		}
	}

	if left == -1 {
		return []int{-1, -1}
	}
	return []int{left, right}
}

func main() {
	fmt.Println(subSort([]int{1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19}))
}
