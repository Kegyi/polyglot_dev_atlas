package main

import (
	"fmt"
	"strings"
)

func main() {
	first := "hello"
	second := "world"
	joined := first + " " + second

	part := joined[:5]
	replaced := strings.Replace(joined, "hello", "hi", 1)
	words := strings.Fields(joined)

	fmt.Println("joined:", joined)
	fmt.Println("part:", part)
	fmt.Println("replaced:", replaced)
	fmt.Println("tokens:", words)
}
