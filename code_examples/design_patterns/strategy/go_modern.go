package main

import "fmt"

// Modern Go Strategy using function values.
// No Strategy interface or struct implementations needed.

type Strategy func(a, b int) int

type Calculator struct {
	strategy Strategy
}

func (c *Calculator) Execute(a, b int) int {
	return c.strategy(a, b)
}

func main() {
	calc := &Calculator{strategy: func(a, b int) int { return a + b }}
	fmt.Println("Add:", calc.Execute(5, 3))

	calc.strategy = func(a, b int) int { return a - b }
	fmt.Println("Subtract:", calc.Execute(5, 3))

	calc.strategy = func(a, b int) int { return a * b }
	fmt.Println("Multiply:", calc.Execute(5, 3))
}
