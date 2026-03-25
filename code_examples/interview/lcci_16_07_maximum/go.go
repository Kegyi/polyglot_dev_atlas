package main

import "fmt"

func maximum(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	fmt.Println(maximum(1, 2))
}
