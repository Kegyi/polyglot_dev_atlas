function shortestSeq(big: number[], small: number[]): number[] {
    const need = new Map<number, number>();
    for (const x of small) need.set(x, (need.get(x) ?? 0) + 1);
    const window = new Map<number, number>();
    let cnt = small.length;
    let j = 0, k = -1, mi = Infinity;
    for (let i = 0; i < big.length; i++) {
        const x = big[i];
        window.set(x, (window.get(x) ?? 0) + 1);
        if ((need.get(x) ?? 0) >= (window.get(x) ?? 0)) cnt--;
        while (cnt === 0) {
            if (i - j + 1 < mi) { mi = i - j + 1; k = j; }
            const lx = big[j];
            if ((need.get(lx) ?? 0) >= (window.get(lx) ?? 0)) cnt++;
            window.set(lx, (window.get(lx) ?? 0) - 1);
            j++;
        }
    }
    return k === -1 ? [] : [k, k + mi - 1];
}
