function maxAliveYear(birth: number[], death: number[]): number {
    const diff = new Array<number>(102).fill(0);
    for (let i = 0; i < birth.length; i++) {
        diff[birth[i] - 1900] += 1;
        if (death[i] + 1 <= 2000) {
            diff[death[i] + 1 - 1900] -= 1;
        }
    }

    let bestYear = 1900;
    let alive = 0;
    let bestAlive = -1;
    for (let i = 0; i <= 100; i++) {
        alive += diff[i];
        if (alive > bestAlive) {
            bestAlive = alive;
            bestYear = 1900 + i;
        }
    }
    return bestYear;
}

console.log(maxAliveYear([1900, 1901, 1950], [1948, 1951, 2000]));
