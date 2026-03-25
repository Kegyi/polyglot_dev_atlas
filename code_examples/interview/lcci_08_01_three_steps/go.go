package main

import "fmt"

func waysToStep(n int) int {
	const MOD = 1000000007
	if n == 1 {
		return 1
	}
	if n == 2 {
		return 2
	}
	if n == 3 {
		return 4
	}
	a, b, c := 1, 2, 4
	for i := 3; i < n; i++ {
		a, b, c = b, c, ((a+b)%MOD+c)%MOD
	}
	return c
}

func main() {
	fmt.Println(waysToStep(3)) // 4
	fmt.Println(waysToStep(5)) // 13
}
