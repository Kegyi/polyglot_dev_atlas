package main

import "fmt"

func findClosedNumbers(num int) (int, int) {
	bigger, smaller := num, num

	for i := 1; i < 32; i++ {
		if bigger>>(i-1)&1 == 1 && bigger>>i&1 == 0 {
			bigger |= 1 << i
			bigger &^= 1 << (i - 1)
			break
		}
	}

	for i := 1; i < 32; i++ {
		if smaller>>(i-1)&1 == 0 && smaller>>i&1 == 1 {
			smaller &^= 1 << i
			smaller |= 1 << (i - 1)
			break
		}
	}

	return bigger, smaller
}

func main() {
	bigger, smaller := findClosedNumbers(2)
	fmt.Println(bigger)
	fmt.Println(smaller)
}
