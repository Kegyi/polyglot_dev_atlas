function floodFill(image: number[][], sr: number, sc: number, newColor: number): number[][] {
    const old = image[sr][sc];
    if (old === newColor) return image;
    const r = image.length, c = image[0].length;

    function dfs(i: number, j: number): void {
        if (i < 0 || i >= r || j < 0 || j >= c || image[i][j] !== old) return;
        image[i][j] = newColor;
        dfs(i + 1, j); dfs(i - 1, j); dfs(i, j + 1); dfs(i, j - 1);
    }

    dfs(sr, sc);
    return image;
}

const result = floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2);
for (const row of result) {
    console.log(row);
}
