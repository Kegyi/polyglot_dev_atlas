function findClosest(words: string[], word1: string, word2: string): number {
    let i1 = -1, i2 = -1;
    let ans = Number.MAX_SAFE_INTEGER;
    for (let i = 0; i < words.length; i++) {
        if (words[i] === word1) i1 = i;
        if (words[i] === word2) i2 = i;
        if (i1 !== -1 && i2 !== -1) {
            ans = Math.min(ans, Math.abs(i1 - i2));
        }
    }
    return ans;
}

console.log(findClosest(["I","am","a","student","from","a","university","in","a","city"], "a", "student")); // 1
console.log(findClosest(["aa", "bb"], "aa", "bb")); // 1
