function missingNumber(nums: number[]): number {
    let ans = 0;
    for (let i = 0; i < nums.length; i++) {
        ans ^= (i + 1) ^ nums[i];
    }
    return ans;
}

console.log(missingNumber([3, 0, 1]));                   // 2
console.log(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])); // 8
