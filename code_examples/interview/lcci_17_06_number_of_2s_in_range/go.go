package main

import "fmt"

func numberOf2sInRange(n int) int {
	count := 0
	for m := 1; m <= n; m *= 10 {
		a, b := n/m, n%m
		digit := (a % 10)
		if digit > 2 {
			count += (a/10 + 1) * m
		} else if digit == 2 {
			count += (a/10)*m + b + 1
		} else {
			count += (a / 10) * m
		}
	}
	return count
}

func main() {
	fmt.Println(numberOf2sInRange(25)) // 9
	fmt.Println(numberOf2sInRange(20)) // 2
}
