package main

import "fmt"

func waysToChange(n int) int {
	const MOD = 1000000007
	coins := []int{1, 5, 10, 25}
	dp := make([]int, n+1)
	dp[0] = 1
	for _, coin := range coins {
		for i := coin; i <= n; i++ {
			dp[i] = (dp[i] + dp[i-coin]) % MOD
		}
	}
	return dp[n]
}

func main() {
	fmt.Println(waysToChange(5))  // 2
	fmt.Println(waysToChange(10)) // 4
}
