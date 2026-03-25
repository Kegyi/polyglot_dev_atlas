type Point = { r: number; c: number };

function shortestPathSteps(grid: number[][]): number {
  const rows = grid.length;
  const cols = grid[0].length;

  if (grid[0][0] === 1 || grid[rows - 1][cols - 1] === 1) {
    return -1;
  }

  const dist = Array.from({ length: rows }, () => Array(cols).fill(-1));
  const queue: Point[] = [{ r: 0, c: 0 }];
  dist[0][0] = 0;

  const dirs: Point[] = [
    { r: 1, c: 0 },
    { r: -1, c: 0 },
    { r: 0, c: 1 },
    { r: 0, c: -1 },
  ];

  for (let head = 0; head < queue.length; head++) {
    const { r, c } = queue[head];

    if (r === rows - 1 && c === cols - 1) {
      return dist[r][c];
    }

    for (const d of dirs) {
      const nr = r + d.r;
      const nc = c + d.c;
      if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) {
        continue;
      }
      if (grid[nr][nc] === 1 || dist[nr][nc] !== -1) {
        continue;
      }

      dist[nr][nc] = dist[r][c] + 1;
      queue.push({ r: nr, c: nc });
    }
  }

  return -1;
}

function main(): void {
  const grid = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
  ];

  console.log(`shortest steps: ${shortestPathSteps(grid)}`);
}

main();
