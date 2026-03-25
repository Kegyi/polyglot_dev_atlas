function pondSizes(land: number[][]): number[] {
    const m = land.length;
    const n = land[0].length;

    const dfs = (r: number, c: number): number => {
        if (r < 0 || r >= m || c < 0 || c >= n || land[r][c] !== 0) return 0;
        land[r][c] = -1;
        let size = 1;
        for (let dr = -1; dr <= 1; dr++) {
            for (let dc = -1; dc <= 1; dc++) {
                if (dr !== 0 || dc !== 0) size += dfs(r + dr, c + dc);
            }
        }
        return size;
    };

    const ans: number[] = [];
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (land[i][j] === 0) ans.push(dfs(i, j));
        }
    }
    ans.sort((a, b) => a - b);
    return ans;
}

console.log(pondSizes([[0, 2, 1, 0], [0, 1, 0, 1], [1, 1, 0, 1], [0, 1, 0, 1]]));
