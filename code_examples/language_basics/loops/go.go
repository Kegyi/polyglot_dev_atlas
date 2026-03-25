package main

import "fmt"

func main() {
	values := []int{1, 2, 3, 4, 5}

	for i := 0; i < len(values); i++ {
		fmt.Println("for index:", i, "->", values[i])
	}

	for _, v := range values {
		if v == 3 {
			continue
		}
		fmt.Println("range:", v)
	}

	i := 0
	for i < len(values) {
		if values[i] == 4 {
			break
		}
		fmt.Println("while-style:", values[i])
		i++
	}

	c := 0
	for {
		fmt.Println("infinite-loop iteration:", c)
		c++
		if c >= 2 {
			break
		}
	}
}
