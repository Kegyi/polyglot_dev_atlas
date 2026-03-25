package main

import "fmt"

func tictactoe(board []string) string {
	n := len(board)
	winner := func(c byte) bool {
		for i := 0; i < n; i++ {
			row, col := true, true
			for j := 0; j < n; j++ {
				row = row && board[i][j] == c
				col = col && board[j][i] == c
			}
			if row || col {
				return true
			}
		}
		diag1, diag2 := true, true
		for i := 0; i < n; i++ {
			diag1 = diag1 && board[i][i] == c
			diag2 = diag2 && board[i][n-1-i] == c
		}
		return diag1 || diag2
	}

	if winner('X') {
		return "X"
	}
	if winner('O') {
		return "O"
	}
	for _, row := range board {
		for i := 0; i < len(row); i++ {
			if row[i] == ' ' {
				return "Pending"
			}
		}
	}
	return "Draw"
}

func main() {
	fmt.Println(tictactoe([]string{"O X", " XO", "X O"}))
	fmt.Println(tictactoe([]string{"OOX", "XXO", "OXO"}))
}
