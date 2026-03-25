package main

import "fmt"

type point struct {
	r int
	c int
}

func shortestPathSteps(grid [][]int) int {
	rows := len(grid)
	cols := len(grid[0])
	if grid[0][0] == 1 || grid[rows-1][cols-1] == 1 {
		return -1
	}

	dist := make([][]int, rows)
	for r := 0; r < rows; r++ {
		dist[r] = make([]int, cols)
		for c := 0; c < cols; c++ {
			dist[r][c] = -1
		}
	}

	dirs := []point{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	queue := []point{{0, 0}}
	dist[0][0] = 0

	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]

		if cur.r == rows-1 && cur.c == cols-1 {
			return dist[cur.r][cur.c]
		}

		for _, d := range dirs {
			nr := cur.r + d.r
			nc := cur.c + d.c
			if nr < 0 || nr >= rows || nc < 0 || nc >= cols {
				continue
			}
			if grid[nr][nc] == 1 || dist[nr][nc] != -1 {
				continue
			}
			dist[nr][nc] = dist[cur.r][cur.c] + 1
			queue = append(queue, point{nr, nc})
		}
	}

	return -1
}

func main() {
	grid := [][]int{
		{0, 0, 1, 0, 0},
		{1, 0, 1, 0, 1},
		{0, 0, 0, 0, 0},
		{0, 1, 1, 1, 0},
		{0, 0, 0, 1, 0},
	}

	fmt.Printf("shortest steps: %d\n", shortestPathSteps(grid))
}
