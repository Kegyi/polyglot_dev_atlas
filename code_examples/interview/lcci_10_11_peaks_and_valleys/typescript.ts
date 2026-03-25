function wiggleSort(nums: number[]): void {
    nums.sort((a, b) => a - b);
    for (let index = 0; index + 1 < nums.length; index += 2) {
        [nums[index], nums[index + 1]] = [nums[index + 1], nums[index]];
    }
}

const demoValues = [5, 3, 1, 2, 3];
wiggleSort(demoValues);
console.log(demoValues);
