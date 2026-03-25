package main

import "fmt"

func pathWithObstacles(obstacleGrid [][]int) [][]int {
	r, c := len(obstacleGrid), len(obstacleGrid[0])
	path := [][]int{}
	visited := make([][]bool, r)
	for i := range visited {
		visited[i] = make([]bool, c)
	}

	var dfs func(i, j int) bool
	dfs = func(i, j int) bool {
		if i >= r || j >= c || obstacleGrid[i][j] == 1 || visited[i][j] {
			return false
		}
		visited[i][j] = true
		path = append(path, []int{i, j})
		if i == r-1 && j == c-1 {
			return true
		}
		if dfs(i+1, j) || dfs(i, j+1) {
			return true
		}
		path = path[:len(path)-1]
		return false
	}

	dfs(0, 0)
	return path
}

func main() {
	grid := [][]int{{0, 0, 0}, {0, 1, 0}, {0, 0, 0}}
	fmt.Println(pathWithObstacles(grid))
}
