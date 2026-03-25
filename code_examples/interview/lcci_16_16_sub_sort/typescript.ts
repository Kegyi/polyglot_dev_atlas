function subSort(array: number[]): number[] {
    const n = array.length;
    let left = -1;
    let right = -1;

    let maxSeen = Number.NEGATIVE_INFINITY;
    for (let i = 0; i < n; i++) {
        if (array[i] < maxSeen) {
            right = i;
        } else {
            maxSeen = array[i];
        }
    }

    let minSeen = Number.POSITIVE_INFINITY;
    for (let i = n - 1; i >= 0; i--) {
        if (array[i] > minSeen) {
            left = i;
        } else {
            minSeen = array[i];
        }
    }

    return left === -1 ? [-1, -1] : [left, right];
}

console.log(subSort([1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19]));
