package main

import "fmt"

func getKthMagicNumber(k int) int {
	dp := make([]int, k+1)
	dp[1] = 1
	i3, i5, i7 := 1, 1, 1
	for i := 2; i <= k; i++ {
		a := dp[i3] * 3
		b := dp[i5] * 5
		c := dp[i7] * 7
		dp[i] = a
		if b < dp[i] {
			dp[i] = b
		}
		if c < dp[i] {
			dp[i] = c
		}
		if dp[i] == a {
			i3++
		}
		if dp[i] == b {
			i5++
		}
		if dp[i] == c {
			i7++
		}
	}
	return dp[k]
}

func main() {
	fmt.Println(getKthMagicNumber(5)) // 9
	fmt.Println(getKthMagicNumber(1)) // 1
}
