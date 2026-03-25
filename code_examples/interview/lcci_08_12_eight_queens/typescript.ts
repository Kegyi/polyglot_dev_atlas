function solveNQueens(n: number): string[][] {
    const result: string[][] = [];
    const usedCols = new Set<number>();
    const diag1 = new Set<number>();
    const diag2 = new Set<number>();
    const board: string[][] = Array.from({ length: n }, () => Array(n).fill("."));

    function bt(row: number): void {
        if (row === n) {
            result.push(board.map(r => r.join("")));
            return;
        }
        for (let col = 0; col < n; col++) {
            if (usedCols.has(col) || diag1.has(row - col) || diag2.has(row + col)) continue;
            board[row][col] = "Q";
            usedCols.add(col); diag1.add(row - col); diag2.add(row + col);
            bt(row + 1);
            board[row][col] = ".";
            usedCols.delete(col); diag1.delete(row - col); diag2.delete(row + col);
        }
    }

    bt(0);
    return result;
}

const result = solveNQueens(4);
console.log(`${result.length} solutions`);
for (const board of result) {
    for (const row of board) console.log(row);
    console.log();
}
