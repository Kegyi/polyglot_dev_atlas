package main

import "fmt"

func insert(N int, M int, i int, j int) int {
	mask := ^(((1 << (j - i + 1)) - 1) << i)
	return (N & mask) | (M << i)
}

func main() {
	fmt.Println(insert(1024, 19, 2, 6))
	fmt.Println(insert(0, 19, 0, 4))
}
