package main

import (
	"fmt"
	"strings"
)

func binaryToString(n float64) string {
	var sb strings.Builder
	sb.WriteString("0.")
	for n > 0 {
		if sb.Len() > 32 {
			return "ERROR"
		}
		n *= 2
		if n >= 1 {
			sb.WriteByte('1')
			n -= 1
		} else {
			sb.WriteByte('0')
		}
	}
	return sb.String()
}

func main() {
	fmt.Println(binaryToString(0.625))
	fmt.Println(binaryToString(0.1))
}
