function massage(nums: number[]): number {
    let f = 0, g = 0;
    for (const x of nums) {
        [f, g] = [g + x, Math.max(f, g)];
    }
    return Math.max(f, g);
}
