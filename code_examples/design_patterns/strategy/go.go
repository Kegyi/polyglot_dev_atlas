package main

import "fmt"

type Strategy interface {
	Execute(int, int) int
}

type AddStrategy struct{}

func (s *AddStrategy) Execute(a, b int) int {
	return a + b
}

type SubtractStrategy struct{}

func (s *SubtractStrategy) Execute(a, b int) int {
	return a - b
}

type MultiplyStrategy struct{}

func (s *MultiplyStrategy) Execute(a, b int) int {
	return a * b
}

type Context struct {
	strategy Strategy
}

func (c *Context) SetStrategy(s Strategy) {
	c.strategy = s
}

func (c *Context) ExecuteStrategy(a, b int) int {
	return c.strategy.Execute(a, b)
}

func main() {
	ctx := &Context{}

	ctx.SetStrategy(&AddStrategy{})
	fmt.Printf("Add: %d\n", ctx.ExecuteStrategy(5, 3))

	ctx.SetStrategy(&SubtractStrategy{})
	fmt.Printf("Subtract: %d\n", ctx.ExecuteStrategy(5, 3))

	ctx.SetStrategy(&MultiplyStrategy{})
	fmt.Printf("Multiply: %d\n", ctx.ExecuteStrategy(5, 3))
}
