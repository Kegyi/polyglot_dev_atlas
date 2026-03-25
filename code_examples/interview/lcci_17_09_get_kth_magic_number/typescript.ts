function getKthMagicNumber(k: number): number {
    const dp: number[] = Array(k + 1).fill(0);
    dp[1] = 1;
    let i3 = 1, i5 = 1, i7 = 1;
    for (let i = 2; i <= k; i++) {
        const a = dp[i3] * 3;
        const b = dp[i5] * 5;
        const c = dp[i7] * 7;
        dp[i] = Math.min(a, b, c);
        if (dp[i] === a) i3++;
        if (dp[i] === b) i5++;
        if (dp[i] === c) i7++;
    }
    return dp[k];
}

console.log(getKthMagicNumber(5)); // 9
console.log(getKthMagicNumber(1)); // 1
