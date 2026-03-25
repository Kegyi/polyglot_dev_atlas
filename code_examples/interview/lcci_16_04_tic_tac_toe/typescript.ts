function tictactoe(board: string[]): string {
    const n = board.length;

    const winner = (c: string): boolean => {
        for (let i = 0; i < n; i++) {
            let row = true;
            let col = true;
            for (let j = 0; j < n; j++) {
                row = row && board[i][j] === c;
                col = col && board[j][i] === c;
            }
            if (row || col) return true;
        }
        let diag1 = true;
        let diag2 = true;
        for (let i = 0; i < n; i++) {
            diag1 = diag1 && board[i][i] === c;
            diag2 = diag2 && board[i][n - 1 - i] === c;
        }
        return diag1 || diag2;
    };

    if (winner("X")) return "X";
    if (winner("O")) return "O";
    for (const row of board) {
        for (const ch of row) {
            if (ch === " ") return "Pending";
        }
    }
    return "Draw";
}

console.log(tictactoe(["O X", " XO", "X O"]));
console.log(tictactoe(["OOX", "XXO", "OXO"]));
