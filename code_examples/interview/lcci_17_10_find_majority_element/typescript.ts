function majorityElement(nums: number[]): number {
    let candidate = 0;
    let count = 0;
    for (const x of nums) {
        if (count === 0) candidate = x;
        count += (x === candidate ? 1 : -1);
    }
    let c = 0;
    for (const x of nums) {
        if (x === candidate) c++;
    }
    return c > Math.floor(nums.length / 2) ? candidate : -1;
}

console.log(majorityElement([1, 2, 5, 9, 5, 9, 5, 5, 5])); // 5
console.log(majorityElement([3, 2])); // -1
