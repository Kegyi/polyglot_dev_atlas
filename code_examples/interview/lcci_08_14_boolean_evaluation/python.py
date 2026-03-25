MOD = 10**9 + 7

def countEval(s: str, result: int) -> int:
    n = len(s)
    # dp[i][j] = [ways_false, ways_true] for s[i..j]
    dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
    for i in range(0, n, 2):
        dp[i][i][int(s[i])] = 1
    for size in range(3, n + 1, 2):
        for i in range(0, n - size + 1, 2):
            j = i + size - 1
            for k in range(i + 1, j, 2):
                op = s[k]
                lf, lt = dp[i][k-1]
                rf, rt = dp[k+1][j]
                if op == '&':
                    dp[i][j][1] = (dp[i][j][1] + lt * rt) % MOD
                    dp[i][j][0] = (dp[i][j][0] + lf*rf + lf*rt + lt*rf) % MOD
                elif op == '|':
                    dp[i][j][1] = (dp[i][j][1] + lt*rt + lf*rt + lt*rf) % MOD
                    dp[i][j][0] = (dp[i][j][0] + lf * rf) % MOD
                else:  # '^'
                    dp[i][j][1] = (dp[i][j][1] + lf*rt + lt*rf) % MOD
                    dp[i][j][0] = (dp[i][j][0] + lf*rf + lt*rt) % MOD
    return dp[0][n-1][result]

def main():
    print(countEval("1^0|0|1", 0))       # 2
    print(countEval("0&0&0&1^1|0", 1))   # 10

if __name__ == "__main__":
    main()
