package main

import "fmt"

func floodFill(image [][]int, sr int, sc int, newColor int) [][]int {
	old := image[sr][sc]
	if old == newColor {
		return image
	}
	r, c := len(image), len(image[0])

	var dfs func(i, j int)
	dfs = func(i, j int) {
		if i < 0 || i >= r || j < 0 || j >= c || image[i][j] != old {
			return
		}
		image[i][j] = newColor
		dfs(i+1, j)
		dfs(i-1, j)
		dfs(i, j+1)
		dfs(i, j-1)
	}

	dfs(sr, sc)
	return image
}

func main() {
	image := [][]int{{1, 1, 1}, {1, 1, 0}, {1, 0, 1}}
	result := floodFill(image, 1, 1, 2)
	for _, row := range result {
		fmt.Println(row)
	}
}
