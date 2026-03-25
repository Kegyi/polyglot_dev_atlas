package main

import "fmt"

func setZeroes(matrix [][]int) {
	zeroRows := map[int]bool{}
	zeroCols := map[int]bool{}

	for r := 0; r < len(matrix); r++ {
		for c := 0; c < len(matrix[0]); c++ {
			if matrix[r][c] == 0 {
				zeroRows[r] = true
				zeroCols[c] = true
			}
		}
	}

	for r := 0; r < len(matrix); r++ {
		for c := 0; c < len(matrix[0]); c++ {
			if zeroRows[r] || zeroCols[c] {
				matrix[r][c] = 0
			}
		}
	}
}

func main() {
	matrix := [][]int{
		{1, 2, 3},
		{4, 0, 6},
		{7, 8, 9},
	}

	setZeroes(matrix)
	for _, row := range matrix {
		fmt.Printf("%d %d %d\n", row[0], row[1], row[2])
	}
}
