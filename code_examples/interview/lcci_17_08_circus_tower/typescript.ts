function bestSeqAtIndex(height: number[], weight: number[]): number {
    const people: Array<[number, number]> = [];
    for (let i = 0; i < height.length; i++) {
        people.push([height[i], weight[i]]);
    }
    people.sort((a, b) => a[0] - b[0] || b[1] - a[1]);

    const lis: number[] = [];
    for (const [, w] of people) {
        let l = 0, r = lis.length;
        while (l < r) {
            const m = (l + r) >> 1;
            if (lis[m] < w) l = m + 1;
            else r = m;
        }
        if (l === lis.length) lis.push(w);
        else lis[l] = w;
    }
    return lis.length;
}

console.log(bestSeqAtIndex([65, 70, 56, 75, 60, 68], [100, 150, 90, 190, 95, 110])); // 6
console.log(bestSeqAtIndex([65, 70, 56, 75], [100, 150, 90, 190])); // 4
