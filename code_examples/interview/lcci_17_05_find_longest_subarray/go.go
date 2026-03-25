package main

import (
	"fmt"
	"strings"
	"unicode"
)

func findLongestSubarray(array []string) []string {
	first := map[int]int{0: -1}
	s, maxLen, start := 0, 0, 0
	for i, x := range array {
		if unicode.IsLetter(rune(x[0])) {
			s++
		} else {
			s--
		}
		if idx, ok := first[s]; ok {
			if length := i - idx; length > maxLen {
				maxLen = length
				start = idx + 1
			}
		} else {
			first[s] = i
		}
	}
	return array[start : start+maxLen]
}

func main() {
	arr1 := []string{"A", "1", "B", "C", "D", "2", "3", "4", "E", "5", "F", "G", "6", "7", "H", "I", "J", "K", "L", "M"}
	fmt.Println(strings.Join(findLongestSubarray(arr1), " ")) // A 1 B C D 2 3 4 E 5 F G 6 7

	arr2 := []string{"A", "A"}
	res2 := findLongestSubarray(arr2)
	if len(res2) == 0 {
		fmt.Println("(empty)")
	} else {
		fmt.Println(strings.Join(res2, " "))
	}
}
