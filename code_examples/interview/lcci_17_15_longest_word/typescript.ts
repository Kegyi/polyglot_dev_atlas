function longestWord(words: string[]): string {
    const wordSet = new Set(words);

    function canBuild(w: string): boolean {
        if (w === '') return true;
        for (let i = 1; i <= w.length; i++) {
            if (wordSet.has(w.slice(0, i)) && canBuild(w.slice(i))) {
                return true;
            }
        }
        return false;
    }

    words.sort((a, b) => b.length - a.length || a.localeCompare(b));

    for (const w of words) {
        wordSet.delete(w);
        if (canBuild(w)) return w;
        wordSet.add(w);
    }
    return '';
}
