package main

import (
	"fmt"
	"sort"
)

func pondSizes(land [][]int) []int {
	m, n := len(land), len(land[0])
	var dfs func(int, int) int
	dfs = func(r int, c int) int {
		if r < 0 || r >= m || c < 0 || c >= n || land[r][c] != 0 {
			return 0
		}
		land[r][c] = -1
		size := 1
		for dr := -1; dr <= 1; dr++ {
			for dc := -1; dc <= 1; dc++ {
				if dr != 0 || dc != 0 {
					size += dfs(r+dr, c+dc)
				}
			}
		}
		return size
	}

	ans := make([]int, 0)
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if land[i][j] == 0 {
				ans = append(ans, dfs(i, j))
			}
		}
	}
	sort.Ints(ans)
	return ans
}

func main() {
	fmt.Println(pondSizes([][]int{{0, 2, 1, 0}, {0, 1, 0, 1}, {1, 1, 0, 1}, {0, 1, 0, 1}}))
}
