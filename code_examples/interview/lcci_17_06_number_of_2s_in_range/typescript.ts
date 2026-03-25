function numberOf2sInRange(n: number): number {
    let count = 0;
    for (let m = 1; m <= n; m *= 10) {
        const a = Math.trunc(n / m);
        const b = n % m;
        const digit = a % 10;
        if (digit > 2) {
            count += (Math.trunc(a / 10) + 1) * m;
        } else if (digit === 2) {
            count += Math.trunc(a / 10) * m + b + 1;
        } else {
            count += Math.trunc(a / 10) * m;
        }
    }
    return count;
}

console.log(numberOf2sInRange(25)); // 9
console.log(numberOf2sInRange(20)); // 2
