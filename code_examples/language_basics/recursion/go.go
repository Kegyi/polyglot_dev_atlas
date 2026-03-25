package main

import "fmt"

func factorial(n int) int {
	if n <= 1 {
		return 1
	}
	return n * factorial(n-1)
}

func sumRecursive(values []int, index int) int {
	if index >= len(values) {
		return 0
	}
	return values[index] + sumRecursive(values, index+1)
}

func main() {
	values := []int{1, 2, 3, 4}
	fmt.Println("factorial(5):", factorial(5))
	fmt.Println("sumRecursive(values):", sumRecursive(values, 0))
}
