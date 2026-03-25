function permutation(S: string): string[] {
    const chars = S.split("").sort();
    const result: string[] = [];
    const used = new Array(chars.length).fill(false);
    const path: string[] = [];

    function backtrack(): void {
        if (path.length === chars.length) {
            result.push(path.join(""));
            return;
        }
        for (let i = 0; i < chars.length; i++) {
            if (used[i]) continue;
            if (i > 0 && chars[i] === chars[i - 1] && !used[i - 1]) continue;
            used[i] = true;
            path.push(chars[i]);
            backtrack();
            path.pop();
            used[i] = false;
        }
    }

    backtrack();
    return result;
}

for (const p of permutation("qqe")) {
    console.log(p);
}
