function generateParenthesis(n: number): string[] {
    const result: string[] = [];

    function bt(cur: string, open: number, close: number): void {
        if (cur.length === 2 * n) { result.push(cur); return; }
        if (open < n) bt(cur + "(", open + 1, close);
        if (close < open) bt(cur + ")", open, close + 1);
    }

    bt("", 0, 0);
    return result;
}

for (const s of generateParenthesis(3)) {
    console.log(s);
}
