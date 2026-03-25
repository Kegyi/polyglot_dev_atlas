function mapDigit(ch: string): string {
    if (ch <= "c") return "2";
    if (ch <= "f") return "3";
    if (ch <= "i") return "4";
    if (ch <= "l") return "5";
    if (ch <= "o") return "6";
    if (ch <= "s") return "7";
    if (ch <= "v") return "8";
    return "9";
}

function getValidT9Words(num: string, words: string[]): string[] {
    const ans: string[] = [];
    for (const word of words) {
        if (word.length !== num.length) continue;
        let ok = true;
        for (let i = 0; i < word.length; i++) {
            if (mapDigit(word[i]) !== num[i]) {
                ok = false;
                break;
            }
        }
        if (ok) ans.push(word);
    }
    return ans;
}

console.log(getValidT9Words("8733", ["tree", "used", "true"]));
