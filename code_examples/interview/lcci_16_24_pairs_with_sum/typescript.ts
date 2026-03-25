function pairSums(nums: number[], target: number): number[][] {
    const freq = new Map<number, number>();
    const ans: number[][] = [];
    for (const x of nums) {
        const y = target - x;
        const cnt = freq.get(y) ?? 0;
        if (cnt > 0) {
            freq.set(y, cnt - 1);
            ans.push([Math.min(x, y), Math.max(x, y)]);
        } else {
            freq.set(x, (freq.get(x) ?? 0) + 1);
        }
    }
    return ans;
}

console.log(pairSums([5, 6, 5], 11));
