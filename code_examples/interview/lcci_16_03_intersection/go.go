package main

import (
	"fmt"
	"math"
	"sort"
)

const eps = 1e-9

func lessPoint(a, b []float64) bool {
	if math.Abs(a[0]-b[0]) > eps {
		return a[0] < b[0]
	}
	return a[1] < b[1]-eps
}

func cross(a, b, c []float64) float64 {
	return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
}

func onSegment(a, b, p []float64) bool {
	return math.Abs(cross(a, b, p)) < eps &&
		math.Min(a[0], b[0])-eps <= p[0] && p[0] <= math.Max(a[0], b[0])+eps &&
		math.Min(a[1], b[1])-eps <= p[1] && p[1] <= math.Max(a[1], b[1])+eps
}

func intersection(start1, end1, start2, end2 []float64) []float64 {
	if lessPoint(end1, start1) {
		start1, end1 = end1, start1
	}
	if lessPoint(end2, start2) {
		start2, end2 = end2, start2
	}

	d1 := cross(start1, end1, start2)
	d2 := cross(start1, end1, end2)
	d3 := cross(start2, end2, start1)
	d4 := cross(start2, end2, end1)

	if ((d1 > eps && d2 > eps) || (d1 < -eps && d2 < -eps)) ||
		((d3 > eps && d4 > eps) || (d3 < -eps && d4 < -eps)) {
		return []float64{}
	}

	a1 := end1[1] - start1[1]
	b1 := start1[0] - end1[0]
	c1 := a1*start1[0] + b1*start1[1]

	a2 := end2[1] - start2[1]
	b2 := start2[0] - end2[0]
	c2 := a2*start2[0] + b2*start2[1]

	det := a1*b2 - a2*b1
	if math.Abs(det) < eps {
		candidates := make([][]float64, 0, 4)
		if onSegment(start1, end1, start2) {
			candidates = append(candidates, start2)
		}
		if onSegment(start1, end1, end2) {
			candidates = append(candidates, end2)
		}
		if onSegment(start2, end2, start1) {
			candidates = append(candidates, start1)
		}
		if onSegment(start2, end2, end1) {
			candidates = append(candidates, end1)
		}
		if len(candidates) == 0 {
			return []float64{}
		}
		sort.Slice(candidates, func(i, j int) bool {
			if math.Abs(candidates[i][0]-candidates[j][0]) > eps {
				return candidates[i][0] < candidates[j][0]
			}
			return candidates[i][1] < candidates[j][1]-eps
		})
		return candidates[0]
	}

	x := (b2*c1 - b1*c2) / det
	y := (a1*c2 - a2*c1) / det
	p := []float64{x, y}
	if onSegment(start1, end1, p) && onSegment(start2, end2, p) {
		return p
	}
	return []float64{}
}

func main() {
	fmt.Println(intersection([]float64{0, 0}, []float64{1, 0}, []float64{1, 1}, []float64{0, -1}))
}
