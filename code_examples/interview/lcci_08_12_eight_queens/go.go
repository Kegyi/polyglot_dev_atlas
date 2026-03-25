package main

import (
	"fmt"
	"strings"
)

func solveNQueens(n int) [][]string {
	result := [][]string{}
	usedCols := map[int]bool{}
	diag1 := map[int]bool{}
	diag2 := map[int]bool{}
	board := make([][]byte, n)
	for i := range board {
		board[i] = []byte(strings.Repeat(".", n))
	}

	var bt func(row int)
	bt = func(row int) {
		if row == n {
			snapshot := make([]string, n)
			for i, r := range board {
				snapshot[i] = string(r)
			}
			result = append(result, snapshot)
			return
		}
		for col := 0; col < n; col++ {
			if usedCols[col] || diag1[row-col] || diag2[row+col] {
				continue
			}
			board[row][col] = 'Q'
			usedCols[col] = true
			diag1[row-col] = true
			diag2[row+col] = true
			bt(row + 1)
			board[row][col] = '.'
			delete(usedCols, col)
			delete(diag1, row-col)
			delete(diag2, row+col)
		}
	}

	bt(0)
	return result
}

func main() {
	result := solveNQueens(4)
	fmt.Printf("%d solutions\n", len(result))
	for _, board := range result {
		for _, row := range board {
			fmt.Println(row)
		}
		fmt.Println()
	}
}
