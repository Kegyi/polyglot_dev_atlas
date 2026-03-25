const MOD = BigInt(1_000_000_007);

function countEval(s: string, result: number): number {
    const n = s.length;
    // dp[i][j] = [ways_false, ways_true]
    const dp: [bigint, bigint][][] = Array.from({length: n}, () =>
        Array.from({length: n}, () => [0n, 0n] as [bigint, bigint])
    );
    for (let i = 0; i < n; i += 2) {
        dp[i][i][s[i] === '1' ? 1 : 0] = 1n;
    }
    for (let size = 3; size <= n; size += 2) {
        for (let i = 0; i <= n - size; i += 2) {
            const j = i + size - 1;
            for (let k = i + 1; k < j; k += 2) {
                const op = s[k];
                const lf = dp[i][k-1][0], lt = dp[i][k-1][1];
                const rf = dp[k+1][j][0], rt = dp[k+1][j][1];
                if (op === '&') {
                    dp[i][j][1] = (dp[i][j][1] + lt * rt) % MOD;
                    dp[i][j][0] = (dp[i][j][0] + lf*rf + lf*rt + lt*rf) % MOD;
                } else if (op === '|') {
                    dp[i][j][1] = (dp[i][j][1] + lt*rt + lf*rt + lt*rf) % MOD;
                    dp[i][j][0] = (dp[i][j][0] + lf*rf) % MOD;
                } else { // '^'
                    dp[i][j][1] = (dp[i][j][1] + lf*rt + lt*rf) % MOD;
                    dp[i][j][0] = (dp[i][j][0] + lf*rf + lt*rt) % MOD;
                }
            }
        }
    }
    return Number(dp[0][n-1][result]);
}

console.log(countEval("1^0|0|1", 0));      // 2
console.log(countEval("0&0&0&1^1|0", 1));  // 10
