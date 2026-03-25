function waysToChange(n: number): number {
    const MOD = 1000000007n;
    const coins = [1, 5, 10, 25];
    const dp = new Array(n + 1).fill(0n);
    dp[0] = 1n;
    for (const coin of coins) {
        for (let i = coin; i <= n; i++) {
            dp[i] = (dp[i] + dp[i - coin]) % MOD;
        }
    }
    return Number(dp[n]);
}

console.log(waysToChange(5));   // 2
console.log(waysToChange(10));  // 4
