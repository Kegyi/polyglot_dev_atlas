package main

import "fmt"

const modBE = 1_000_000_007

func countEval(s string, result int) int {
	n := len(s)
	// dp[i][j][v] = ways substring s[i..j] evaluates to v
	dp := make([][][2]int64, n)
	for i := range dp {
		dp[i] = make([][2]int64, n)
	}
	for i := 0; i < n; i += 2 {
		dp[i][i][s[i]-'0'] = 1
	}
	for size := 3; size <= n; size += 2 {
		for i := 0; i <= n-size; i += 2 {
			j := i + size - 1
			for k := i + 1; k < j; k += 2 {
				op := s[k]
				lf, lt := dp[i][k-1][0], dp[i][k-1][1]
				rf, rt := dp[k+1][j][0], dp[k+1][j][1]
				switch op {
				case '&':
					dp[i][j][1] = (dp[i][j][1] + lt*rt) % modBE
					dp[i][j][0] = (dp[i][j][0] + lf*rf + lf*rt + lt*rf) % modBE
				case '|':
					dp[i][j][1] = (dp[i][j][1] + lt*rt + lf*rt + lt*rf) % modBE
					dp[i][j][0] = (dp[i][j][0] + lf*rf) % modBE
				case '^':
					dp[i][j][1] = (dp[i][j][1] + lf*rt + lt*rf) % modBE
					dp[i][j][0] = (dp[i][j][0] + lf*rf + lt*rt) % modBE
				}
			}
		}
	}
	return int(dp[0][n-1][result])
}

func main() {
	fmt.Println(countEval("1^0|0|1", 0))     // 2
	fmt.Println(countEval("0&0&0&1^1|0", 1)) // 10
}
