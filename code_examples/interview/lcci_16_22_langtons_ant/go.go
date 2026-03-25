package main

import "fmt"

func key(r int, c int) string {
	return fmt.Sprintf("%d#%d", r, c)
}

func printKMoves(k int) []string {
	r, c, dir := 0, 0, 0
	dr := []int{0, 1, 0, -1}
	dc := []int{1, 0, -1, 0}
	dirs := "RDLU"

	black := map[string]bool{}
	minR, maxR, minC, maxC := 0, 0, 0, 0

	for step := 0; step < k; step++ {
		cur := key(r, c)
		if black[cur] {
			delete(black, cur)
			dir = (dir + 3) % 4
		} else {
			black[cur] = true
			dir = (dir + 1) % 4
		}
		r += dr[dir]
		c += dc[dir]
		if r < minR {
			minR = r
		}
		if r > maxR {
			maxR = r
		}
		if c < minC {
			minC = c
		}
		if c > maxC {
			maxC = c
		}
	}

	for p := range black {
		var br, bc int
		fmt.Sscanf(p, "%d#%d", &br, &bc)
		if br < minR {
			minR = br
		}
		if br > maxR {
			maxR = br
		}
		if bc < minC {
			minC = bc
		}
		if bc > maxC {
			maxC = bc
		}
	}

	board := make([]string, 0, maxR-minR+1)
	for i := minR; i <= maxR; i++ {
		row := make([]byte, 0, maxC-minC+1)
		for j := minC; j <= maxC; j++ {
			if i == r && j == c {
				row = append(row, dirs[dir])
			} else if black[key(i, j)] {
				row = append(row, 'X')
			} else {
				row = append(row, '_')
			}
		}
		board = append(board, string(row))
	}
	return board
}

func main() {
	fmt.Println(printKMoves(2))
}
