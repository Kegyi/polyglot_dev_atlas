function waysToStep(n: number): number {
    const MOD = 1000000007n;
    if (n === 1) return 1;
    if (n === 2) return 2;
    if (n === 3) return 4;
    let a = 1n, b = 2n, c = 4n;
    for (let i = 3; i < n; i++) {
        [a, b, c] = [b, c, ((a + b) % MOD + c) % MOD];
    }
    return Number(c);
}

console.log(waysToStep(3)); // 4
console.log(waysToStep(5)); // 13
