function findSwapValues(array1: number[], array2: number[]): number[] {
    const sum1 = array1.reduce((a, b) => a + b, 0);
    const sum2 = array2.reduce((a, b) => a + b, 0);
    const diff = sum1 - sum2;
    if (diff % 2 !== 0) return [];
    const target = diff / 2;

    const set2 = new Set(array2);
    for (const x of array1) {
        const y = x - target;
        if (set2.has(y)) return [x, y];
    }
    return [];
}

console.log(findSwapValues([4, 1, 2, 1, 1, 2], [3, 6, 3, 3]));
