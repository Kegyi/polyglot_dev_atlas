package main

import "fmt"

func findSwapValues(array1 []int, array2 []int) []int {
	sum1, sum2 := 0, 0
	for _, x := range array1 {
		sum1 += x
	}
	for _, y := range array2 {
		sum2 += y
	}
	diff := sum1 - sum2
	if diff%2 != 0 {
		return []int{}
	}
	target := diff / 2

	set2 := map[int]bool{}
	for _, y := range array2 {
		set2[y] = true
	}
	for _, x := range array1 {
		y := x - target
		if set2[y] {
			return []int{x, y}
		}
	}
	return []int{}
}

func main() {
	fmt.Println(findSwapValues([]int{4, 1, 2, 1, 1, 2}, []int{3, 6, 3, 3}))
}
