function masterMind(solution: string, guess: string): number[] {
    let hits = 0;
    const cs = new Array<number>(26).fill(0);
    const cg = new Array<number>(26).fill(0);
    for (let i = 0; i < 4; i++) {
        if (solution[i] === guess[i]) {
            hits += 1;
        } else {
            cs[solution.charCodeAt(i) - 65] += 1;
            cg[guess.charCodeAt(i) - 65] += 1;
        }
    }
    let pseudo = 0;
    for (let i = 0; i < 26; i++) {
        pseudo += Math.min(cs[i], cg[i]);
    }
    return [hits, pseudo];
}

console.log(masterMind("RGBY", "GGRR"));
