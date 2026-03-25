package main

import "fmt"

type Operations struct{}

func (Operations) Minus(a int, b int) int {
	return a - b
}

func (Operations) Multiply(a int, b int) int {
	return a * b
}

func (Operations) Divide(a int, b int) int {
	return a / b
}

func main() {
	ops := Operations{}
	fmt.Println(ops.Minus(10, 3))
	fmt.Println(ops.Multiply(6, -4))
	fmt.Println(ops.Divide(20, 5))
}
