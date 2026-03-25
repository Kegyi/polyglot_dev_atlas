function smallestDifference(a: number[], b: number[]): number {
    a.sort((x, y) => x - y);
    b.sort((x, y) => x - y);
    let i = 0;
    let j = 0;
    let ans = Number.MAX_SAFE_INTEGER;
    while (i < a.length && j < b.length) {
        ans = Math.min(ans, Math.abs(a[i] - b[j]));
        if (a[i] < b[j]) {
            i += 1;
        } else {
            j += 1;
        }
    }
    return ans;
}

console.log(smallestDifference([1, 3, 15, 11, 2], [23, 127, 235, 19, 8]));
