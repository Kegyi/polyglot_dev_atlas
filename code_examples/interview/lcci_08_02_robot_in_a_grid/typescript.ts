function pathWithObstacles(obstacleGrid: number[][]): number[][] {
    const r = obstacleGrid.length, c = obstacleGrid[0].length;
    const path: number[][] = [];
    const visited = Array.from({ length: r }, () => new Array(c).fill(false));

    function dfs(i: number, j: number): boolean {
        if (i >= r || j >= c || obstacleGrid[i][j] === 1 || visited[i][j]) return false;
        visited[i][j] = true;
        path.push([i, j]);
        if (i === r - 1 && j === c - 1) return true;
        if (dfs(i + 1, j) || dfs(i, j + 1)) return true;
        path.pop();
        return false;
    }

    dfs(0, 0);
    return path;
}

console.log(JSON.stringify(pathWithObstacles([[0,0,0],[0,1,0],[0,0,0]])));
