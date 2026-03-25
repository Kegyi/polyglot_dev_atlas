function divingBoard(shorter: number, longer: number, k: number): number[] {
    if (k === 0) return [];
    if (shorter === longer) return [shorter * k];
    const ans: number[] = [];
    for (let i = 0; i <= k; i++) {
        ans.push(shorter * (k - i) + longer * i);
    }
    return ans;
}

console.log(divingBoard(1, 2, 3));
