package main

import "fmt"

func main() {
	values := []int{1, 2, 3, 4, 5}
	fmt.Println("original:", values)

	doubled := make([]int, 0, len(values))
	for _, v := range values {
		doubled = append(doubled, v*2)
	}

	evens := make([]int, 0, len(doubled))
	total := 0
	for _, v := range doubled {
		if v%2 == 0 {
			evens = append(evens, v)
			total += v
		}
	}

	fmt.Println("doubled:", doubled)
	fmt.Println("evens:", evens)
	fmt.Println("sum of evens in doubled:", total)
}
