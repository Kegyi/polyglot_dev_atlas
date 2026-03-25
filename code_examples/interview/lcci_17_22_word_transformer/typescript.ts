function findLadders(beginWord: string, endWord: string, wordList: string[]): string[] {
    const wordSet = new Set(wordList);
    if (!wordSet.has(endWord)) return [];

    const queue: string[][] = [[beginWord]];
    const visited = new Set([beginWord]);

    while (queue.length > 0) {
        const path = queue.shift()!;
        const cur = path[path.length - 1];
        const arr = cur.split('');
        for (let i = 0; i < arr.length; i++) {
            const orig = arr[i];
            for (let c = 0; c < 26; c++) {
                const ch = String.fromCharCode(97 + c);
                if (ch === orig) continue;
                arr[i] = ch;
                const nxt = arr.join('');
                if (nxt === endWord) return [...path, nxt];
                if (wordSet.has(nxt) && !visited.has(nxt)) {
                    visited.add(nxt);
                    queue.push([...path, nxt]);
                }
                arr[i] = orig;
            }
        }
    }
    return [];
}
