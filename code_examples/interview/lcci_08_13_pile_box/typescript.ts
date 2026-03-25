function pileBox(box: number[][]): number {
    box.sort((a, b) => a[0] !== b[0] ? b[0] - a[0] : b[1] - a[1]);
    const n = box.length;
    const dp = box.map(b => b[2]);
    let ans = Math.max(...dp);
    for (let i = 1; i < n; i++) {
        for (let j = 0; j < i; j++) {
            if (box[j][0] > box[i][0] && box[j][1] > box[i][1] && box[j][2] > box[i][2]) {
                dp[i] = Math.max(dp[i], dp[j] + box[i][2]);
            }
        }
        ans = Math.max(ans, dp[i]);
    }
    return ans;
}

console.log(pileBox([[2,2,2],[3,3,3],[4,4,4]])); // 9
