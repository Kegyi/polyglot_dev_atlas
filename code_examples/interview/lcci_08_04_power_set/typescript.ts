function subsets(nums: number[]): number[][] {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const result: number[][] = [];
    for (let mask = 0; mask < (1 << n); mask++) {
        const subset: number[] = [];
        for (let i = 0; i < n; i++) {
            if (mask & (1 << i)) subset.push(nums[i]);
        }
        result.push(subset);
    }
    return result;
}

for (const s of subsets([1, 2, 3])) {
    console.log(JSON.stringify(s));
}
