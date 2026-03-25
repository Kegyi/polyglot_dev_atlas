function merge(a: number[], m: number, b: number[], n: number): void {
    let i = m - 1;
    let j = n - 1;
    let k = m + n - 1;
    while (j >= 0) {
        if (i >= 0 && a[i] > b[j]) {
            a[k--] = a[i--];
        } else {
            a[k--] = b[j--];
        }
    }
}

const mergedValues = [1, 2, 3, 0, 0, 0];
merge(mergedValues, 3, [2, 5, 6], 3);
console.log(mergedValues);
