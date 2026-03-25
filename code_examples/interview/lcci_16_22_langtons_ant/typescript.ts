function key(r: number, c: number): string {
    return `${r}#${c}`;
}

function printKMoves(k: number): string[] {
    let r = 0;
    let c = 0;
    let dir = 0;
    const dr = [0, 1, 0, -1];
    const dc = [1, 0, -1, 0];
    const dirs = "RDLU";

    const black = new Set<string>();
    let minR = 0;
    let maxR = 0;
    let minC = 0;
    let maxC = 0;

    for (let step = 0; step < k; step++) {
        const cur = key(r, c);
        if (black.has(cur)) {
            black.delete(cur);
            dir = (dir + 3) % 4;
        } else {
            black.add(cur);
            dir = (dir + 1) % 4;
        }
        r += dr[dir];
        c += dc[dir];
        minR = Math.min(minR, r);
        maxR = Math.max(maxR, r);
        minC = Math.min(minC, c);
        maxC = Math.max(maxC, c);
    }

    for (const p of black) {
        const [br, bc] = p.split("#").map(Number);
        minR = Math.min(minR, br);
        maxR = Math.max(maxR, br);
        minC = Math.min(minC, bc);
        maxC = Math.max(maxC, bc);
    }

    const board: string[] = [];
    for (let i = minR; i <= maxR; i++) {
        let row = "";
        for (let j = minC; j <= maxC; j++) {
            if (i === r && j === c) row += dirs[dir];
            else if (black.has(key(i, j))) row += "X";
            else row += "_";
        }
        board.push(row);
    }
    return board;
}

console.log(printKMoves(2));
