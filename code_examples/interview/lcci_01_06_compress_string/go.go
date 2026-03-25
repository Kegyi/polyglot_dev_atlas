package main

import (
	"fmt"
	"strconv"
	"strings"
)

func compressString(s string) string {
	if len(s) == 0 {
		return s
	}

	var b strings.Builder
	run := 1

	for i := 1; i <= len(s); i++ {
		if i < len(s) && s[i] == s[i-1] {
			run++
			continue
		}

		b.WriteByte(s[i-1])
		b.WriteString(strconv.Itoa(run))
		run = 1
	}

	compressed := b.String()
	if len(compressed) < len(s) {
		return compressed
	}
	return s
}

func main() {
	fmt.Printf("aabcccccaaa -> %s\n", compressString("aabcccccaaa"))
	fmt.Printf("abbccd -> %s\n", compressString("abbccd"))
}
