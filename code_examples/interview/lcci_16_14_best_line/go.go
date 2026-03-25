package main

import "fmt"

func collinear(a, b, c []int) bool {
	x1, y1 := int64(b[0]-a[0]), int64(b[1]-a[1])
	x2, y2 := int64(c[0]-a[0]), int64(c[1]-a[1])
	return x1*y2 == x2*y1
}

func bestLine(points [][]int) []int {
	n := len(points)
	bestI, bestJ, bestCount := 0, 1, 2
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			count := 2
			for k := j + 1; k < n; k++ {
				if collinear(points[i], points[j], points[k]) {
					count++
				}
			}
			if count > bestCount || (count == bestCount && (i < bestI || (i == bestI && j < bestJ))) {
				bestI, bestJ, bestCount = i, j, count
			}
		}
	}
	return []int{bestI, bestJ}
}

func main() {
	fmt.Println(bestLine([][]int{{0, 0}, {1, 1}, {1, 0}, {2, 2}}))
}
