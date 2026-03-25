package main

import "fmt"

func isUnique(s string) bool {
	seen := [256]bool{}
	for i := 0; i < len(s); i++ {
		ch := s[i]
		if seen[ch] {
			return false
		}
		seen[ch] = true
	}
	return true
}

func main() {
	fmt.Printf("leetcode -> %t\n", isUnique("leetcode"))
	fmt.Printf("abc -> %t\n", isUnique("abc"))
}
