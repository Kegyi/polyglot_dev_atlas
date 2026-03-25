package main

import "fmt"

func hanota(A *[]int, B *[]int, C *[]int) {
	var move func(n int, src, aux, dst *[]int)
	move = func(n int, src, aux, dst *[]int) {
		if n == 0 {
			return
		}
		move(n-1, src, dst, aux)
		*dst = append(*dst, (*src)[len(*src)-1])
		*src = (*src)[:len(*src)-1]
		move(n-1, aux, src, dst)
	}
	move(len(*A), A, B, C)
}

func main() {
	A := []int{2, 1, 0}
	B := []int{}
	C := []int{}
	hanota(&A, &B, &C)
	fmt.Println("A:", A)
	fmt.Println("B:", B)
	fmt.Println("C:", C)
}
