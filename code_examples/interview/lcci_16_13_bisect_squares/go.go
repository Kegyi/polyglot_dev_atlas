package main

import (
	"fmt"
	"math"
)

func cutSquares(square1 []int, square2 []int) []float64 {
	x1, y1, s1 := float64(square1[0]), float64(square1[1]), float64(square1[2])
	x2, y2, s2 := float64(square2[0]), float64(square2[1]), float64(square2[2])

	cx1, cy1 := x1+s1/2.0, y1+s1/2.0
	cx2, cy2 := x2+s2/2.0, y2+s2/2.0

	if math.Abs(cx1-cx2) < 1e-9 {
		x := cx1
		yBottom := math.Min(y1, y2)
		yTop := math.Max(y1+s1, y2+s2)
		return []float64{x, yBottom, x, yTop}
	}

	k := (cy2 - cy1) / (cx2 - cx1)
	b := cy1 - k*cx1

	var px1, py1, px2, py2 float64
	if math.Abs(k) <= 1 {
		px1 = math.Min(x1, x2)
		px2 = math.Max(x1+s1, x2+s2)
		py1 = k*px1 + b
		py2 = k*px2 + b
	} else {
		py1 = math.Min(y1, y2)
		py2 = math.Max(y1+s1, y2+s2)
		px1 = (py1 - b) / k
		px2 = (py2 - b) / k
	}

	if px1 > px2 || (math.Abs(px1-px2) < 1e-9 && py1 > py2) {
		px1, px2 = px2, px1
		py1, py2 = py2, py1
	}
	return []float64{px1, py1, px2, py2}
}

func main() {
	fmt.Println(cutSquares([]int{-1, -1, 2}, []int{0, -1, 2}))
}
