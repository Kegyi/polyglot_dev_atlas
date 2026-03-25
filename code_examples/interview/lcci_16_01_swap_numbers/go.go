package main

import "fmt"

func swapNumbers(numbers []int) []int {
	return []int{numbers[1], numbers[0]}
}

func main() {
	fmt.Println(swapNumbers([]int{1, 2}))
}
