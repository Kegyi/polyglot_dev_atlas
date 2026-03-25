package main

import (
	"fmt"
	"sort"
)

func pileBox(box [][]int) int {
	sort.Slice(box, func(i, j int) bool {
		if box[i][0] != box[j][0] {
			return box[i][0] > box[j][0]
		}
		return box[i][1] > box[j][1]
	})
	n := len(box)
	dp := make([]int, n)
	for i := range dp {
		dp[i] = box[i][2]
	}
	ans := dp[0]
	for i := 1; i < n; i++ {
		for j := 0; j < i; j++ {
			if box[j][0] > box[i][0] && box[j][1] > box[i][1] && box[j][2] > box[i][2] {
				if dp[j]+box[i][2] > dp[i] {
					dp[i] = dp[j] + box[i][2]
				}
			}
		}
		if dp[i] > ans {
			ans = dp[i]
		}
	}
	return ans
}

func main() {
	fmt.Println(pileBox([][]int{{2, 2, 2}, {3, 3, 3}, {4, 4, 4}})) // 9
}
