package main

import "fmt"

func checkPermutation(a string, b string) bool {
	if len(a) != len(b) {
		return false
	}

	freq := [256]int{}
	for i := 0; i < len(a); i++ {
		freq[a[i]]++
	}
	for i := 0; i < len(b); i++ {
		freq[b[i]]--
		if freq[b[i]] < 0 {
			return false
		}
	}
	return true
}

func main() {
	fmt.Printf("abcde vs edcba -> %t\n", checkPermutation("abcde", "edcba"))
	fmt.Printf("abc vs abz -> %t\n", checkPermutation("abc", "abz"))
}
