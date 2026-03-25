package main

import (
	"errors"
	"fmt"
)

func add(a, b int) int {
	return a + b
}

func safeDiv(a, b float64) (float64, error) {
	if b == 0 {
		return 0, errors.New("division by zero")
	}
	return a / b, nil
}

func main() {
	fmt.Println("add(2, 3):", add(2, 3))

	if v, err := safeDiv(10, 2); err == nil {
		fmt.Println("safeDiv(10, 2):", v)
	}

	if _, err := safeDiv(10, 0); err != nil {
		fmt.Println("error:", err)
	}
}
