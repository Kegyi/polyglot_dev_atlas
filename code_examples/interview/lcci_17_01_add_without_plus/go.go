package main

import "fmt"

func add(a int, b int) int {
	for b != 0 {
		carry := uint(a&b) << 1
		a = a ^ b
		b = int(carry)
	}
	return a
}

func main() {
	fmt.Println(add(1, 2))   // 3
	fmt.Println(add(3, -2))  // 1
	fmt.Println(add(-1, -2)) // -3
}
