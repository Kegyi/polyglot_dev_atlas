package main

import (
	"fmt"
	"strings"
)

func urlify(s string, trueLength int) string {
	var b strings.Builder
	for i := 0; i < trueLength; i++ {
		if s[i] == ' ' {
			b.WriteString("%20")
		} else {
			b.WriteByte(s[i])
		}
	}
	return b.String()
}

func main() {
	fmt.Println(urlify("Mr John Smith    ", 13))
}
