package main

import (
	"fmt"
	"sort"
)

func main() {
	values := []int{9, 3, 7, 1, 5}
	sort.Ints(values)

	index := sort.SearchInts(values, 7)
	foundIndex := -1
	if index < len(values) && values[index] == 7 {
		foundIndex = index
	}

	fmt.Println("sorted:", values)
	fmt.Println("contains 7:", foundIndex >= 0)
	fmt.Println("index of 7:", foundIndex)
}
