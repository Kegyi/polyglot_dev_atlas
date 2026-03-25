function missingTwo(nums: number[]): number[] {
    const n = nums.length + 2;
    let xor = 0;
    for (const v of nums) xor ^= v;
    for (let i = 1; i <= n; i++) xor ^= i;
    const diff = xor & (-xor);
    let a = 0;
    for (const v of nums) if (v & diff) a ^= v;
    for (let i = 1; i <= n; i++) if (i & diff) a ^= i;
    const b = xor ^ a;
    return [a, b];
}
