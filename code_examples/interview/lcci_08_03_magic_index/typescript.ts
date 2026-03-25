function findMagicIndex(nums: number[]): number {
    let lo = 0, hi = nums.length - 1;
    while (lo <= hi) {
        const mid = (lo + hi) >> 1;
        if (nums[mid] === mid) return mid;
        if (nums[mid] < mid) lo = mid + 1;
        else hi = mid - 1;
    }
    return -1;
}

console.log(findMagicIndex([-1, 1, 3, 4, 6])); // 1
console.log(findMagicIndex([0, 2, 3, 4, 5]));  // 0
