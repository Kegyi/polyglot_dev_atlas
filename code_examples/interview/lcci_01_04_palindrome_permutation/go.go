package main

import (
	"fmt"
	"strings"
)

func canPermutePalindrome(s string) bool {
	freq := map[rune]int{}
	for _, ch := range strings.ToLower(s) {
		if ch == ' ' {
			continue
		}
		freq[ch]++
	}

	odd := 0
	for _, count := range freq {
		if count%2 == 1 {
			odd++
			if odd > 1 {
				return false
			}
		}
	}
	return true
}

func main() {
	fmt.Printf("tact coa -> %t\n", canPermutePalindrome("tact coa"))
	fmt.Printf("daily -> %t\n", canPermutePalindrome("daily"))
}
